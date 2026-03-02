"""
Momus Base Agent

base pipeline changes vs core pipeline:
- Phase 1 Round 2: inject best prior solution + full grader feedback as Additional Materials
  for all but one of the parallel solvers (maintains diversity).
- Phase 2: Top 3 candidate solutions with actual feedback (fixes empty feedback bug).
  Tie-break: prefer solutions from previous outer loops (conjecture-based) over Phase 1.
- Phase 2 Additional Materials: All proven lemmas + all unproven conjecture attempts with
  feedback (across all outer loops), providing complete context to the extractor.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from .momus_core_agent import MomusCoreAgent
from ..utils.logger import log_print
from ..utils.config_utils import get_template_required


@dataclass
class _MomusConjectureAttempt:
    statement: str
    proof: str
    grade: int
    grader_feedback: str
    outer_loop_idx: int
    kind: str  # "conjecture" | "negation"
    is_proven: bool


@dataclass
class _MomusConflictingAttempt:
    """A conflicting pair where both C and ¬C were proven (hallucination)"""
    conjecture: str
    negation: str
    proof_of_conjecture: str
    proof_of_negation: str
    grade_conjecture: int
    grade_negation: int
    feedback_conjecture: str
    feedback_negation: str
    outer_loop_idx: int


@dataclass
class _MomusSolutionMetadata:
    """Metadata for a solution, tracking where it came from and its properties"""
    solution: str
    feedback: str
    grade: int
    phase: int  # 1, 2, or 3
    outer_loop_idx: int = -1  # -1 for Phase 1 (no outer loop), 0+ for Phase 2/3
    round_num: Optional[int] = None  # For Phase 1: which solver-grader round (1 or 2)
    num_conjectures_used: int = 0  # Number of proven lemmas/conjectures used in generation
    is_improved: bool = False  # True if this was improved after feedback injection (Phase 1)


class MomusBaseAgent(MomusCoreAgent):
    def __init__(
        self,
        config_path: str = "imo_solver/config/momus_config.yaml",
        prompts_path: str = "imo_solver/prompts/momus_prompts.yaml",
        base_models_path: Optional[str] = None,
        log_file: str = "logs/momus_base.log",
    ):
        super().__init__(
            config_path=config_path,
            prompts_path=prompts_path,
            base_models_path=base_models_path,
            log_file=log_file,
        )

        # Unified solution tracking: all solutions ever generated with metadata
        self._momus_all_solutions: List[_MomusSolutionMetadata] = []

        # Persisted across outer loops for Loop 2 conjecture extraction
        self._momus_prev_conjecture_attempts: List[_MomusConjectureAttempt] = []
        # Persisted across outer loops: conjectures extracted but not proven (partial progress)
        self._momus_unproven_conjecture_attempts: List[_MomusConjectureAttempt] = []
        # Persisted across outer loops: conflicting attempts (both C and ¬C proven)
        self._momus_conflicting_attempts: List[_MomusConflictingAttempt] = []
        # Track which outer loop iterations produced proven lemmas
        self._momus_proven_lemma_loops: set[int] = set()

        log_print(f"\n{'='*80}")
        log_print("MOMUS BASE AGENT INITIALIZED")
        log_print(f"{'='*80}")

    # ========================================================================
    # base pipeline Solution Tracking Helpers
    # ========================================================================

    def _momus_add_solutions(
        self,
        solutions: List[str],
        feedbacks: List[str],
        grades: List[int],
        phase: int,
        outer_loop_idx: int = -1,
        round_num: Optional[int] = None,
        num_conjectures_used: int = 0,
        is_improved: bool = False,
    ) -> None:
        """Add solutions to the unified tracking list with metadata"""
        for sol, fb, grade in zip(solutions, feedbacks, grades):
            clean_solution = self._extract_final_blueprint(sol) or sol
            self._momus_all_solutions.append(
                _MomusSolutionMetadata(
                    solution=clean_solution,
                    feedback=fb,
                    grade=grade,
                    phase=phase,
                    outer_loop_idx=outer_loop_idx,
                    round_num=round_num,
                    num_conjectures_used=num_conjectures_used,
                    is_improved=is_improved,
                )
            )

    def _momus_get_best_solutions(
        self,
        phase: Optional[int] = None,
        outer_loop_idx: Optional[int] = None,
        round_num: Optional[int] = None,
        min_grade: int = 0,
        max_num: int = 3,
        prefer_conjecture_based: bool = True,
    ) -> List[_MomusSolutionMetadata]:
        """
        Filter and return best solutions from the unified list.
        
        Args:
            phase: Filter by phase (1, 2, or 3). None = any phase.
            outer_loop_idx: Filter by outer loop index. None = any.
            round_num: Filter by round number (for Phase 1). None = any.
            min_grade: Minimum grade threshold
            max_num: Maximum number to return
            prefer_conjecture_based: If True, prefer solutions with num_conjectures_used > 0 on grade ties
            
        Returns:
            List of solution metadata, sorted by grade (descending) with tie-break.
        """
        filtered = [
            s for s in self._momus_all_solutions
            if (phase is None or s.phase == phase)
            and (outer_loop_idx is None or s.outer_loop_idx == outer_loop_idx)
            and (round_num is None or s.round_num == round_num)
            and s.grade >= min_grade
        ]
        
        # Sort by grade (descending), then by num_conjectures_used if prefer_conjecture_based, then by outer_loop_idx (newer first)
        if prefer_conjecture_based:
            filtered.sort(key=lambda s: (s.grade, s.num_conjectures_used, s.outer_loop_idx), reverse=True)
        else:
            filtered.sort(key=lambda s: (s.grade, s.outer_loop_idx), reverse=True)
        
        return filtered[:max_num]

    # ========================================================================
    # PHASE 1 (base pipeline): Round 2 single-solver materials injection
    # ========================================================================

    def phase1_solver_grader_loop(
        self,
        problem: str
    ) -> Tuple[List[str], List[str], List[int], int]:
        """
        Override core:
        - Keep best solution + full grader feedback from Round 1 (after improvement)
        - In Round 2 Step 1, pass that as Additional Materials to exactly ONE solver.

        Args:
            problem: The problem statement

        Returns:
            (solutions, feedbacks, grades, max_grade) tuple (matching core signature)
        """
        log_print(f"\n{'='*80}")
        log_print("PHASE 1: SOLVER-GRADER LOOP (base pipeline)")
        log_print(f"{'='*80}")

        solutions: List[str] = []
        feedbacks: List[str] = []
        grades: List[int] = []
        max_grade = 0

        for round_num in range(1, self.max_solver_grader_rounds + 1):
            log_print(f"\n{'='*70}")
            log_print(f"SOLVER-GRADER ROUND {round_num}/{self.max_solver_grader_rounds}")
            log_print(f"{'='*70}")

            materials_by_solver_idx: Optional[Dict[int, str]] = None

            if round_num == 2:
                # Get top Round 1 solutions (prefer improved, else initial)
                # Get all Round 1 solutions, prefer improved ones
                round1_solutions = [
                    s for s in self._momus_all_solutions
                    if s.phase == 1 and s.outer_loop_idx == -1 and s.round_num == 1
                ]
                # Sort: improved first, then by grade
                round1_solutions.sort(key=lambda s: (s.is_improved, s.grade), reverse=True)
                # Take top solutions (enough for all solvers that will get materials)
                num_solvers_getting_materials = self.num_parallel_solvers - 1
                top_round1 = round1_solutions[:num_solvers_getting_materials]
                
                if top_round1:
                    # Give each solver a different top solution (or cycle if fewer solutions than solvers)
                    materials_by_solver_idx = {}
                    for i in range(num_solvers_getting_materials):
                        sol_metadata = top_round1[i % len(top_round1)]
                        formatted_materials = self._momus_format_phase1_round2_materials(
                            sol_metadata.solution, sol_metadata.feedback, sol_metadata.grade
                        )
                        materials_by_solver_idx[i] = formatted_materials
                    
                    grades_str = ", ".join([f"{s.grade}/7" for s in top_round1[:3]])  # Show first 3 grades
                    if len(top_round1) > 3:
                        grades_str += f", ... ({len(top_round1)} total)"
                    log_print(f"[MOMUS] Round 2: injecting top {len(top_round1)} Round 1 solution(s) (grades: {grades_str}) into {num_solvers_getting_materials}/{self.num_parallel_solvers} solvers (all except Solver {self.num_parallel_solvers})")

            solver_sessions, solutions = self.step1_parallel_solve(
                problem, materials_by_solver_idx=materials_by_solver_idx
            )
            if not solutions:
                log_print("✗ Step 1 failed")
                continue

            feedbacks, grades = self.step2_parallel_grade(problem, solutions)
            if not grades:
                log_print("✗ Step 2 failed")
                continue

            # Track solutions from this round (before feedback injection)
            if solutions and feedbacks and grades:
                self._momus_add_solutions(
                    solutions, feedbacks, grades,
                    phase=1, outer_loop_idx=-1, round_num=round_num, num_conjectures_used=0, is_improved=False
                )

            max_grade = max(grades) if grades else 0
            log_print(f"\nRound {round_num} - Max grade: {max_grade}/7")

            if max_grade == 7:
                log_print(f"✓ Perfect score detected in round {round_num}")
                return solutions, feedbacks, grades, max_grade
            if max_grade >= self.min_grade_for_phase2:
                log_print(f"✓ Sufficient score ({max_grade} >= {self.min_grade_for_phase2}), proceeding to Phase 2")
                return solutions, feedbacks, grades, max_grade

            # Step 3: Feedback injection
            log_print(f"\n--- Step 3: Feedback Injection (Round {round_num}) ---")
            # Extract relevant parts of feedback based on feedback_mode config
            extracted_feedbacks = [self._extract_feedback_for_injection(f) for f in feedbacks]
            improved_solutions = self.step3_feedback_injection(solver_sessions, extracted_feedbacks)
            if not improved_solutions:
                log_print("✗ Step 3 failed")
                continue

            # Step 4: Parallel Re-Grading
            log_print(f"\n--- Step 4: Parallel Re-Grading (Round {round_num}) ---")
            step4_result = self.step2_parallel_grade(problem, improved_solutions)
            if not step4_result or len(step4_result) != 2:
                log_print("✗ Step 4 failed (invalid return)")
                continue
            new_feedbacks, new_grades = step4_result

            solutions = improved_solutions
            feedbacks = new_feedbacks
            grades = new_grades
            max_grade = max(grades) if grades else 0
            log_print(f"\nAfter improvement - Max grade: {max_grade}/7")

            # Track improved solutions
            if solutions and new_feedbacks and new_grades:
                self._momus_add_solutions(
                    solutions, new_feedbacks, new_grades,
                    phase=1, outer_loop_idx=-1, round_num=round_num, num_conjectures_used=0, is_improved=True
                )

            # Solutions already tracked in unified list above, no need to store separately

            if max_grade == 7:
                log_print(f"✓ Perfect score after improvement in round {round_num}")
                return solutions, feedbacks, grades, max_grade
            if max_grade >= self.min_grade_for_phase2:
                log_print("✓ Sufficient score after improvement")
                return solutions, feedbacks, grades, max_grade

        log_print(f"\nPhase 1 completed after {self.max_solver_grader_rounds} rounds")
        return solutions, feedbacks, grades, max_grade

    def _momus_format_phase1_round2_materials(
        self, best_solution: str, best_feedback: str, best_grade: Optional[int]
    ) -> str:
        grade_str = f"{best_grade}/7" if isinstance(best_grade, int) else "unknown"
        return (
            "### base pipeline Additional Materials (from previous round)\n\n"
            f"**Best previous solution (grade {grade_str}):**\n{best_solution}\n\n"
            f"**Full grader feedback for that solution:**\n{best_feedback}\n"
        )

    # ========================================================================
    # STEP 1 (base pipeline): allow per-solver materials injection
    # ========================================================================

    def step1_parallel_solve(
        self, problem: str, materials_by_solver_idx: Optional[Dict[int, str]] = None
    ) -> Tuple[List[Any], List[str]]:
        """
        Override core to allow a per-solver `materials` payload.
        """
        # Copy core implementation structure, but build solve_prompt per solver.
        log_print(f"\n{'='*70}")
        log_print(f"STEP 1: PARALLEL INITIAL SOLVING (K={self.num_parallel_solvers})")
        log_print(f"{'='*70}")

        # Reuse the core early-returns
        if not getattr(self, "HAS_GENAI_SDK", True):
            # In core this constant is module-level; keep behavior consistent.
            pass

        # Defer to parent implementation by importing same globals it relies on.
        # (We use attributes/methods on self for everything else.)
        try:
            from concurrent.futures import ThreadPoolExecutor, as_completed
            from .momus_core_agent import HAS_GENAI_SDK, genai  # type: ignore
        except ImportError:
            # If imports fail, behave like core's missing SDK path.
            log_print("✗ google-genai SDK not installed")
            return [], []

        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return [], []

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return [], []

        try:
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            system_prompt = self.config_manager.get_role_prompt("solver", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("solver", system_prompt)
            log_print(f"Using model: {model_id}")

            def solve_single(solver_idx: int) -> Tuple[int, Any, str]:
                try:
                    log_print(f"\n[Solver {solver_idx+1}] Starting...")
                    chat = client.chats.create(model=model_id, config=gen_config)

                    materials = "None"
                    if materials_by_solver_idx and solver_idx in materials_by_solver_idx:
                        materials = materials_by_solver_idx[solver_idx]

                    solve_prompt = get_template_required(
                        "solve_instruction",
                        self.config_manager,
                        problem=problem,
                        materials=materials,
                    )

                    response = chat.send_message(solve_prompt)
                    self._log_api_call(
                        step_name=f"Step 1 - Solver {solver_idx+1}/{self.num_parallel_solvers}",
                        role="solver",
                        prompt=solve_prompt,
                        response=response,
                    )

                    solution = response.text
                    if solution:
                        solution = self.apply_answer_processor_rule1(chat, solution)
                        log_print(f"[Solver {solver_idx+1}] ✓ Generated and improved ({len(solution)} chars)")
                        return (solver_idx, chat, solution)
                    log_print(f"[Solver {solver_idx+1}] ✗ Failed (empty response)")
                    return (solver_idx, None, "")
                except Exception as e:
                    log_print(f"[Solver {solver_idx+1}] ✗ Error: {e}")
                    return (solver_idx, None, "")

            log_print(f"\nLaunching {self.num_parallel_solvers} solvers in parallel...")
            results: List[Optional[Tuple[Any, str]]] = [None] * self.num_parallel_solvers

            with ThreadPoolExecutor(max_workers=self.num_parallel_solvers) as executor:
                futures = {executor.submit(solve_single, i): i for i in range(self.num_parallel_solvers)}
                for future in as_completed(futures):
                    idx, chat, solution = future.result()
                    results[idx] = (chat, solution)

            solver_sessions: List[Any] = []
            solutions: List[str] = []
            for item in results:
                if not item:
                    continue
                chat, solution = item
                if solution and chat:
                    solver_sessions.append(chat)
                    solutions.append(solution)

            log_print(f"\nStep 1 complete: {len(solutions)}/{self.num_parallel_solvers} solutions generated")
            return solver_sessions, solutions

        except Exception as e:
            log_print(f"✗ Step 1 failed with error: {e}")
            import traceback
            traceback.print_exc()
            return [], []

    # ========================================================================
    # PHASE 2 (base pipeline): stash best conjecture attempt + feed into Loop 2 extractor
    # ========================================================================

    def _get_top_solutions(
        self,
        solutions: List[str],
        grades: List[int],
        feedbacks: Optional[List[str]],
        n: int,
    ) -> Tuple[List[str], List[str]]:
        """
        base pipeline tie-break for selecting top-N candidate solutions from current phase:
        - Primary: higher grade
        - Tie-break: prefer solutions that use conjectures (num_conjectures_used > 0)
        - Final tie-break: newer index preferred (more recent)
        """
        # Check which solutions are from previous outer loop Phase 3 (conjecture-based)
        prev_loop_phase3 = self._momus_get_best_solutions(phase=3, max_num=1000, prefer_conjecture_based=True)
        prev_loop_solution_set = {s.solution for s in prev_loop_phase3}

        def key(i: int) -> Tuple[int, int, int]:
            grade_val = int(grades[i] if i < len(grades) else 0)
            # Check if this solution is from previous outer loop Phase 3 (conjecture-based)
            solution_text = solutions[i] if i < len(solutions) else ""
            used_conjectures = 1 if (solution_text and solution_text in prev_loop_solution_set) else 0
            # final tiebreak: newer index preferred (more recent)
            return (grade_val, used_conjectures, i)

        sorted_indices = sorted(range(len(grades)), key=key, reverse=True)
        top_indices = sorted_indices[:n]

        top_solutions = [solutions[i] for i in top_indices]
        if feedbacks and len(feedbacks) == len(solutions):
            top_feedbacks = [feedbacks[i] for i in top_indices]
        else:
            top_feedbacks = ["" for _ in top_indices]

        return top_solutions, top_feedbacks

    def step6_conjecture_extraction(
        self, problem: str, solutions: List[str], feedbacks: List[str], outer_loop_idx: int = 0
    ) -> Optional[Dict[str, Any]]:
        """
        Override core: pass `materials` to the conjecture extractor prompt.
        - Candidate solutions area already includes top solutions + their feedback.
        - Additional Materials should include:
          1) all previously proven lemmas (across outer loops)
          2) any previously extracted-but-unproven conjecture attempts, with proof attempts + grader feedback
        """
        materials_parts: List[str] = []

        proven_lemmas = getattr(self, "_accumulated_proven_lemmas", []) or []
        if proven_lemmas:
            blocks = []
            for i, lemma in enumerate(proven_lemmas, 1):
                grade = lemma.get("grade", 0)
                grade_str = f"{grade}/7" if isinstance(grade, int) else "unknown"
                blocks.append(
                    f"### Proven Lemma {i} (Grade {grade_str})\n"
                    f"**Statement:**\n{lemma.get('conjecture','')}\n\n"
                    f"**Proof:**\n{lemma.get('proof','')}\n"
                )
            materials_parts.append("## Previously Proven Lemmas\n\n" + "\n\n".join(blocks))

        # Only include unproven attempts from iterations that did not prove a lemma
        unproven_from_failed_loops = [
            a for a in self._momus_unproven_conjecture_attempts
            if a.outer_loop_idx not in self._momus_proven_lemma_loops
        ]

        if unproven_from_failed_loops:
            blocks = []
            for i, a in enumerate(unproven_from_failed_loops, 1):
                grade_str = f"{a.grade}/7" if isinstance(a.grade, int) else "unknown"
                blocks.append(
                    f"### Unproven conjecture attempt {i} (Loop {a.outer_loop_idx + 1}, {a.kind}, grade {grade_str})\n"
                    f"**Statement:**\n{a.statement}\n\n"
                    f"**Best proof attempt so far:**\n{a.proof}\n\n"
                    f"**Grader feedback:**\n{a.grader_feedback}\n"
                )
            materials_parts.append("## Previously Extracted but Unproven Conjectures (Partial Progress)\n\n" + "\n\n".join(blocks))

        materials = "\n\n".join(materials_parts) if materials_parts else "None"
        if materials != "None":
            log_print(
                f"[MOMUS] Injecting into conjecture extractor: {len(proven_lemmas)} proven lemma(s), "
                f"{len(unproven_from_failed_loops)} unproven conjecture attempt(s) from failed loops"
            )

        # This is mostly core, but uses the momus prompt template which includes {materials}.
        from .momus_core_agent import HAS_GENAI_SDK, genai  # type: ignore

        loop_suffix = f" (Loop {outer_loop_idx + 1})" if outer_loop_idx > 0 else ""
        log_print(f"\n{'='*70}")
        log_print(f"STEP 6: CONJECTURE EXTRACTION{loop_suffix}")
        log_print(f"{'='*70}")

        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return None

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return None

        try:
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            system_prompt = self.config_manager.get_role_prompt("conjecture_extractor", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("conjecture_extractor", system_prompt)

            solutions_text = "\n\n".join([f"=== Solution {i+1} ===\n{sol}" for i, sol in enumerate(solutions)])
            grader_reports = "\n\n".join([f"=== Feedback for Solution {i+1} ===\n{fb}" for i, fb in enumerate(feedbacks)])

            extraction_prompt = get_template_required(
                "conjecture_extraction",
                self.config_manager,
                problem=problem,
                solutions=solutions_text,
                grader_reports=grader_reports,
                materials=materials,
            )

            log_print("Extracting conjectures...")
            chat = client.chats.create(model=model_id, config=gen_config)
            response = chat.send_message(extraction_prompt)

            self._log_api_call(
                step_name="Step 6 - Conjecture Extraction",
                role="conjecture_extractor",
                prompt=extraction_prompt,
                response=response,
            )

            followup_prompt = get_template_required("self_contained_followup", self.config_manager)
            response2 = chat.send_message(followup_prompt)
            self._log_api_call(
                step_name="Step 6 - Self-Contained Follow-up",
                role="conjecture_extractor",
                prompt=followup_prompt,
                response=response2,
            )

            result_text = response2.text
            conjectures_data = self._parse_conjectures_with_llm(result_text)
            if not conjectures_data:
                log_print("  Falling back to regex parser...")
                conjectures_data = self._parse_conjecture_extraction(result_text)

            if conjectures_data:
                num_conj = len(conjectures_data.get("conjectures", []))
                num_neg = len(conjectures_data.get("negations", []))
                log_print(f"✓ Extracted {num_conj} conjectures, {num_neg} negations")
                return conjectures_data

            log_print("✗ Failed to parse conjecture extraction")
            return None

        except Exception as e:
            log_print(f"✗ Step 6 failed with error: {e}")
            import traceback
            traceback.print_exc()
            return None

    def _momus_format_conjecture_extractor_materials(self, attempts: List[_MomusConjectureAttempt]) -> str:
        blocks = []
        for i, a in enumerate(attempts, 1):
            blocks.append(
                f"## Previous conjecture attempt {i}\n\n"
                f"**Conjecture/Statement:**\n{a.statement}\n\n"
                f"**Highest-scoring attempted proof (grade {a.grade}/7):**\n{a.proof}\n\n"
                f"**Full grader feedback for that attempt:**\n{a.grader_feedback}\n"
            )
        return "\n\n".join(blocks)

    # ========================================================================
    # STEP 8/VERIFY (base pipeline): retain grader feedback for best attempt
    # ========================================================================

    def step8_recursive_verification(
        self, problem: str, validated_conjectures: List[Dict[str, str]], outer_loop_idx: int = 0
    ) -> List[Dict[str, str]]:
        """
        Override core:
        - Keep full grader feedback for each verification attempt.
        - After Loop 1 verification, store the best attempt per conjecture pair for use in Loop 2 extractor materials.
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        loop_suffix = f" (Loop {outer_loop_idx + 1})" if outer_loop_idx > 0 else ""
        log_print(f"\n{'='*70}")
        log_print(f"STEP 8: RECURSIVE VERIFICATION (Individual){loop_suffix}")
        log_print(f"{'='*70}")

        tasks: List[Dict[str, Any]] = []
        for i, conj_dict in enumerate(validated_conjectures):
            tasks.append({"id": f"C{i+1}", "statement": conj_dict["conjecture"], "is_positive": True})
            tasks.append({"id": f"NC{i+1}", "statement": conj_dict["negation"], "is_positive": False})

        log_print(f"\nLaunching {len(tasks)} verification tasks in parallel...")

        # map task_id -> {proof, grade, feedback, statement}
        results: Dict[str, Dict[str, Any]] = {}
        with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
            future_to_task = {
                executor.submit(self._solve_and_grade_single_conjecture_momus, t["statement"], t["id"]): t
                for t in tasks
            }
            for future in as_completed(future_to_task):
                task = future_to_task[future]
                tid = task["id"]
                try:
                    proof, grade, feedback = future.result()
                    results[tid] = {
                        "statement": task["statement"],
                        "proof": proof,
                        "grade": grade,
                        "feedback": feedback,
                    }
                except Exception as e:
                    log_print(f"✗ Task {tid} failed: {e}")
                    results[tid] = {
                        "statement": task["statement"],
                        "proof": "",
                        "grade": 0,
                        "feedback": "",
                    }

        # Stash best attempt per conjecture pair (track unproven attempts as "partial progress")
        if validated_conjectures:
            attempts: List[_MomusConjectureAttempt] = []
            for i, _ in enumerate(validated_conjectures):
                pos = results.get(f"C{i+1}", {"grade": 0})
                neg = results.get(f"NC{i+1}", {"grade": 0})
                chosen = pos if pos.get("grade", 0) >= neg.get("grade", 0) else neg
                kind = "conjecture" if chosen is pos else "negation"
                grade_val = int(chosen.get("grade", 0) or 0)
                is_proven = grade_val >= self.conjecture_grade_threshold
                attempts.append(
                    _MomusConjectureAttempt(
                        statement=chosen.get("statement", ""),
                        proof=chosen.get("proof", ""),
                        grade=grade_val,
                        grader_feedback=chosen.get("feedback", ""),
                        outer_loop_idx=outer_loop_idx,
                        kind=kind,
                        is_proven=is_proven,
                    )
                )
            # Keep "prev attempts" for reference (last loop's set)
            self._momus_prev_conjecture_attempts = attempts
            # Append any unproven attempt to the long-term partial-progress list
            for a in attempts:
                if not a.is_proven and a.statement:
                    self._momus_unproven_conjecture_attempts.append(a)

        # Organize for conflict resolution (core expects positive/negative maps)
        positive_results: Dict[str, Dict[str, Any]] = {}
        negative_results: Dict[str, Dict[str, Any]] = {}
        for t in tasks:
            tid = t["id"]
            res = results.get(tid, {"proof": "", "grade": 0})
            if t["is_positive"]:
                positive_results[tid] = res
            else:
                negative_results[tid] = res

        proven_lemmas = self._momus_resolve_conflicts_with_feedback(validated_conjectures, positive_results, negative_results, outer_loop_idx)
        
        # Track which loops produced proven lemmas
        if proven_lemmas:
            self._momus_proven_lemma_loops.add(outer_loop_idx)
        
        return proven_lemmas

    def _momus_resolve_conflicts_with_feedback(
        self, validated_conjectures: List[Dict[str, str]],
        positive_results: Dict[str, Dict[str, Any]],
        negative_results: Dict[str, Dict[str, Any]],
        outer_loop_idx: int = -1
    ) -> List[Dict[str, Any]]:
        """
        base pipeline override: Same as core _resolve_conflicts but also includes grader feedback in proven lemmas.
        Momus: Stores conflicting attempts (both C and ¬C proven) instead of discarding them.
        """
        log_print("\nResolving conflicts and selecting proven lemmas...")
        
        proven_lemmas = []
        
        for i, conj_dict in enumerate(validated_conjectures):
            conj_id = f"C{i+1}"
            neg_id = f"NC{i+1}"
            
            # Get results
            pos_res = positive_results.get(conj_id, {"grade": 0, "proof": "", "feedback": ""})
            neg_res = negative_results.get(neg_id, {"grade": 0, "proof": "", "feedback": ""})
            
            pos_grade = pos_res.get("grade", 0)
            neg_grade = neg_res.get("grade", 0)
            
            log_print(f"\n  {conj_id}: Positive grade {pos_grade}, Negative grade {neg_grade}")
            
            # Check for conflict
            if pos_grade >= self.conjecture_grade_threshold and neg_grade >= self.conjecture_grade_threshold:
                log_print(f"    ⚠ CONFLICT DETECTED: Both proven (hallucination) - storing as conflicting attempt")
                # Store conflicting attempt instead of discarding
                self._momus_conflicting_attempts.append(
                    _MomusConflictingAttempt(
                        conjecture=conj_dict["conjecture"],
                        negation=conj_dict["negation"],
                        proof_of_conjecture=pos_res.get("proof", ""),
                        proof_of_negation=neg_res.get("proof", ""),
                        grade_conjecture=pos_grade,
                        grade_negation=neg_grade,
                        feedback_conjecture=pos_res.get("feedback", ""),
                        feedback_negation=neg_res.get("feedback", ""),
                        outer_loop_idx=outer_loop_idx,
                    )
                )
                continue
                
            # Select proven lemma
            if pos_grade >= self.conjecture_grade_threshold:
                proven_lemmas.append({
                    "conjecture": conj_dict["conjecture"],
                    "proof": pos_res.get("proof", ""),
                    "grade": pos_grade,
                    "feedback": pos_res.get("feedback", "")
                })
                log_print(f"    ✓ Positive conjecture proven (grade {pos_grade})")
            elif neg_grade >= self.conjecture_grade_threshold:
                proven_lemmas.append({
                    "conjecture": conj_dict["negation"],
                    "proof": neg_res.get("proof", ""),
                    "grade": neg_grade,
                    "feedback": neg_res.get("feedback", "")
                })
                log_print(f"    ✓ Negative conjecture proven (grade {neg_grade})")
            else:
                log_print(f"    ✗ Neither proven (grades {pos_grade}, {neg_grade})")
                
        log_print(f"\nConflict resolution complete: {len(proven_lemmas)} proven lemmas")
        return proven_lemmas

    def _solve_and_grade_single_conjecture_momus(self, statement: str, task_id: str) -> Tuple[str, int, str]:
        """
        base pipeline version of verification: return (proof, grade, full grader feedback text).
        """
        # Reuse core implementation but keep grader response text.
        from .momus_core_agent import HAS_GENAI_SDK, genai  # type: ignore
        from ..utils.config_utils import get_template_required

        if not HAS_GENAI_SDK:
            return "", 0, ""
            
        api_key = self._get_gemini_api_key()
        if not api_key:
            return "", 0, ""
            
        try:
            # Use persistent client to prevent garbage collection
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # 1. Solve
            log_print(f"[{task_id}] Solving...")
            solver_sys = self.config_manager.get_role_prompt("solver", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("solver", solver_sys)
            
            solve_prompt = get_template_required(
                "solve_instruction",
                self.config_manager,
                problem=statement,
                materials="None"
            )
            
            solver_chat = client.chats.create(model=model_id, config=gen_config)
            response = solver_chat.send_message(solve_prompt)
            
            self._log_api_call(
                step_name=f"Verify {task_id} - Solve",
                role="solver",
                prompt=solve_prompt,
                response=response
            )
            
            proof = response.text
            
            # Apply Rule 1
            proof = self.apply_answer_processor_rule1(solver_chat, proof)

            if not proof:
                log_print(f"[{task_id}] ✗ Empty proof")
                return "", 0, ""

            # Extract Final Blueprint for grading
            clean_proof = self._extract_final_blueprint(proof)

            if not clean_proof:
                log_print(f"[{task_id}] ✗ Failed to extract Final Blueprint, proof is empty after extraction")
                return "", 0, ""

            # 2. Grade (using clean proof)
            log_print(f"[{task_id}] Grading...")
            grader_sys = self.config_manager.get_role_prompt("grader", "system_prompt")
            g_model_id, g_gen_config = self._get_genai_model_config("grader", grader_sys)

            grader_chat = client.chats.create(model=g_model_id, config=g_gen_config)

            grade_prompt = get_template_required(
                "grade_instruction",
                self.config_manager,
                problem=statement,
                solution=clean_proof,
                materials="None"
            )
            
            g_response = grader_chat.send_message(grade_prompt)
            
            self._log_api_call(
                step_name=f"Verify {task_id} - Grade",
                role="grader",
                prompt=grade_prompt,
                response=g_response
            )
            
            grade = self._extract_grade(g_response.text)
            feedback_text = g_response.text if g_response.text else ""
            log_print(f"[{task_id}] Grade: {grade}/7")
            
            return proof, grade, feedback_text
            
        except Exception as e:
            log_print(f"[{task_id}] ✗ Error: {e}")
            return "", 0, ""

    # ========================================================================
    # PHASE 3 (base pipeline.1): tie-break + per-solver injection of prior-loop best
    # ========================================================================

    def phase3_final_solving(
        self,
        problem: str,
        proven_lemmas: List[Dict[str, str]],
        previous_solutions: List[str],
        previous_feedbacks: List[str],
        previous_grades: List[int],
        outer_loop_idx: int = 0,
    ) -> Tuple[Optional[str], int, List[str], List[int], List[str]]:
        """
        base pipeline.1: identical to core behavior, but we additionally cache the current loop's
        Phase 3 outputs so the NEXT outer loop can treat them as higher-priority tie-breakers
        and can inject the previous loop's best solution into one final solver.
        """
        best_solution, max_grade, final_solutions, grades, feedbacks = super().phase3_final_solving(
            problem,
            proven_lemmas,
            previous_solutions,
            previous_feedbacks,
            previous_grades,
            outer_loop_idx=outer_loop_idx,
        )

        # Track Phase 3 solutions in unified list
        if final_solutions and grades and feedbacks:
            num_conjectures = len(proven_lemmas) if proven_lemmas else 0
            self._momus_add_solutions(
                final_solutions, feedbacks, grades,
                phase=3, outer_loop_idx=outer_loop_idx,
                num_conjectures_used=num_conjectures, is_improved=False
            )
            log_print(f"[MOMUS] Tracked {len(final_solutions)} Phase 3 solution(s) with {num_conjectures} conjecture(s) used")

        return best_solution, max_grade, final_solutions, grades, feedbacks

    def _momus_pick_best_previous_solution(
        self,
        previous_solutions: List[str],
        previous_feedbacks: List[str],
        previous_grades: List[int],
    ) -> Tuple[str, str, int]:
        """
        base pipeline.1 tie-break: Use unified solution list to pick best previous solution.
        Prefers solutions that used conjectures (num_conjectures_used > 0) on grade ties.
        """
        if not previous_solutions or not previous_grades:
            return "", "", 0

        # Get best solution from unified list (prefers conjecture-based)
        best_solutions = self._momus_get_best_solutions(
            phase=None,  # Any phase
            min_grade=0,
            max_num=1,
            prefer_conjecture_based=True,
        )

        if best_solutions:
            best = best_solutions[0]
            # Find matching solution in previous_solutions list (for backward compatibility)
            # In case of exact match, use the unified list data
            return best.solution, best.feedback, best.grade
        
        # Fallback: use provided lists (shouldn't happen, but for safety)
        best_grade = max(previous_grades) if previous_grades else 0
        best_idx = max(range(len(previous_grades)), key=lambda i: previous_grades[i])
        return (
            previous_solutions[best_idx],
            previous_feedbacks[best_idx] if best_idx < len(previous_feedbacks) else "",
            best_grade
        )

    def _final_parallel_solve(
        self,
        problem: str,
        proven_lemmas: List[Dict[str, str]],
        previous_solutions: List[str],
        previous_feedbacks: List[str],
        previous_grades: List[int],
    ) -> Tuple[List[Any], List[str]]:
        """
        base pipeline override of core Step 10:
        - Break ties for "best previous solution" by preferring the previous outer-loop's
          Phase 3 solutions.
        - Give all but one final solver an extra section containing the previous outer-loop's
          best Phase 3 solution + feedback (when available), maintaining diversity by leaving
          one solver without this injection.
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from .momus_core_agent import HAS_GENAI_SDK, genai  # type: ignore

        if not HAS_GENAI_SDK:
            return [], []

        api_key = self._get_gemini_api_key()
        if not api_key:
            return [], []

        try:
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client
            system_prompt = self.config_manager.get_role_prompt("solver", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("solver", system_prompt)

            # Lemma materials (unchanged from core)
            if proven_lemmas:
                log_print(f"[MOMUS] _final_parallel_solve: received {len(proven_lemmas)} proven lemma(s)")
                for i, lemma in enumerate(proven_lemmas):
                    grade = lemma.get("grade", "missing")
                    log_print(f"  Lemma {i+1}: grade={grade} (type: {type(grade).__name__}), has_conjecture={bool(lemma.get('conjecture'))}, has_proof={bool(lemma.get('proof'))}")
                
                # Perfect lemmas: grade >= conjecture_grade_threshold (rigorously proven)
                # Partial lemmas: grade >= 3 but < conjecture_grade_threshold (partial proof)
                threshold = self.conjecture_grade_threshold
                perfect_lemmas = [l for l in proven_lemmas if l.get("grade", 0) >= threshold]
                partial_lemmas = [l for l in proven_lemmas if 3 <= l.get("grade", 0) < threshold]
                
                log_print(f"[MOMUS] Filtered: {len(perfect_lemmas)} perfect lemma(s) (grade >= {threshold}), {len(partial_lemmas)} partial lemma(s) (3 <= grade < {threshold})")

                materials_parts = []
                if perfect_lemmas:
                    materials_parts.append(
                        f"**Rigorously Proven Lemmas (Grade >= {threshold}/7):**\n"
                        "These conjectures have been rigorously proven. You may use them as Lemmas without further proof.\n"
                    )
                    for i, lemma in enumerate(perfect_lemmas, 1):
                        materials_parts.append(
                            f"\n**Lemma {i}:**\n{lemma['conjecture']}\n\n**Proof:**\n{lemma['proof']}\n"
                        )

                if partial_lemmas:
                    materials_parts.append(
                        f"\n**Conjectures with Partial Proofs (Grade 3-{threshold-1}):**\n"
                        "The following conjectures have partial proofs. Use them as reference material.\n"
                    )
                    for i, lemma in enumerate(partial_lemmas, 1):
                        grade_str = f"{lemma.get('grade', '?')}/7"
                        feedback = lemma.get('feedback', '')
                        feedback_section = f"\n\n**Grader Feedback:**\n{feedback}\n" if feedback else ""
                        materials_parts.append(
                            f"\n**Conjecture {i} (Grade {grade_str}):**\n{lemma['conjecture']}\n\n**Proof Attempt:**\n{lemma['proof']}{feedback_section}"
                        )

                base_additional_materials = "".join(materials_parts) if materials_parts else ""
                if base_additional_materials:
                    log_print(f"[MOMUS] Added lemma materials to prompt ({len(base_additional_materials)} chars)")
                else:
                    log_print(f"[MOMUS] WARNING: proven_lemmas was non-empty but no materials were generated (perfect={len(perfect_lemmas)}, partial={len(partial_lemmas)})")
            else:
                base_additional_materials = ""
                log_print(f"[MOMUS] _final_parallel_solve: no proven lemmas provided")
            
            # Momus: Add conflicting attempts (both C and ¬C proven) as "Student's attempted solution"
            if self._momus_conflicting_attempts:
                conflicting_section_parts = []
                conflicting_section_parts.append(
                    "\n\n**Student's attempted solution:**\n"
                    "The following are attempts where both a statement and its negation were proven. "
                    "These are not perfect and should be used with caution as reference material only.\n"
                )
                for i, conflict in enumerate(self._momus_conflicting_attempts, 1):
                    conflicting_section_parts.append(
                        f"\n**Attempted Solution {i}:**\n"
                        f"**Statement:**\n{conflict.conjecture}\n\n"
                        f"**Proof of Statement (Grade {conflict.grade_conjecture}/7):**\n{conflict.proof_of_conjecture}\n\n"
                        f"**Negation:**\n{conflict.negation}\n\n"
                        f"**Proof of Negation (Grade {conflict.grade_negation}/7):**\n{conflict.proof_of_negation}\n"
                    )
                conflicting_section = "".join(conflicting_section_parts)
                if base_additional_materials:
                    base_additional_materials += conflicting_section
                else:
                    base_additional_materials = conflicting_section.strip()
                log_print(f"[MOMUS] Added {len(self._momus_conflicting_attempts)} conflicting attempt(s) as 'Student's attempted solution'")

            # Add best previous solution (with base pipeline.1 tie-break)
            best_solution = ""
            best_feedback = ""
            best_grade = 0
            best_solutions = []  # Track for logging
            if previous_solutions and previous_grades:
                best_solutions = self._momus_get_best_solutions(
                    phase=None, max_num=1, prefer_conjecture_based=True
                )
                if best_solutions:
                    best = best_solutions[0]
                    best_solution = best.solution
                    best_feedback = best.feedback
                    best_grade = best.grade
                else:
                    # Fallback to provided lists
                    best_solution, best_feedback, best_grade = self._momus_pick_best_previous_solution(
                        previous_solutions, previous_feedbacks, previous_grades
                    )
                if base_additional_materials:
                    base_additional_materials += "\n\n"
                base_additional_materials += (
                    f"**Previous Solution (Grade {best_grade}/7):**\n"
                    f"The following is the a solution from previous attempts, along with its grader feedback.\n"
                    f"**Previous Solution:**\n{best_solution}\n\n"
                    f"**Grader Feedback:**\n{best_feedback}\n"
                )
                # Log with metadata about the solution
                phase_info = ""
                if best_solutions:
                    best = best_solutions[0]
                    phase_info = f" (Phase {best.phase}"
                    if best.num_conjectures_used > 0:
                        phase_info += f", {best.num_conjectures_used} conjecture(s) used"
                    phase_info += ")"
                log_print(
                    f"\n[MOMUS] Injecting into final solver: best previous solution (grade {best_grade}/7{phase_info}) in Additional Materials (base pipeline.1 tie-break enabled)"
                )

            if not base_additional_materials:
                base_additional_materials = "None"

            # Per-solver injection: previous outer-loop best (for all but one solver)
            prev_loop_section = ""
            # Get best solution from previous outer loop Phase 3
            prev_loop_best = self._momus_get_best_solutions(
                phase=3,  # Phase 3 only
                outer_loop_idx=None,  # Any outer loop, but prefer newer
                max_num=1,
                prefer_conjecture_based=True,
            )
            if prev_loop_best:
                prev_best = prev_loop_best[0]
                grade_str = f"{prev_best.grade}/7"
                prev_loop_section = (
                    "\n\n"
                    "The following is another student's solution.\n"
                    f"**Solution:**\n{prev_best.solution}\n\n"
                    f"**Grader Feedback:**\n{prev_best.feedback}\n"
                )

            def build_solve_prompt(extra_materials: str = "") -> str:
                additional_materials = base_additional_materials
                if extra_materials and additional_materials != "None":
                    additional_materials = additional_materials + extra_materials
                elif extra_materials and additional_materials == "None":
                    additional_materials = extra_materials.strip() or "None"

                return (
                    f"**The Problem:**\n{problem}\n\n"
                    f"**Additional Materials:**\n{additional_materials}\n\n"
                    "Please solve the problem above."
                )

            def final_solve_single(solver_idx: int) -> Tuple[int, Any, str]:
                try:
                    log_print(f"\n[Final Solver {solver_idx+1}] Starting...")

                    # base pipeline: inject previous outer-loop best into all but one solver (all except the last one)
                    # Leave the last solver without this injection to maintain diversity
                    num_solvers_getting_prev_loop = self.num_final_parallel_solvers - 1
                    should_inject = solver_idx < num_solvers_getting_prev_loop
                    solve_prompt = build_solve_prompt(prev_loop_section if should_inject and prev_loop_section else "")
                    if should_inject and prev_loop_section:
                        if prev_loop_best:
                            prev_best = prev_loop_best[0]
                            log_print(f"[MOMUS] Injecting into Final Solver {solver_idx+1}: previous outer-loop best solution (Phase 3, loop {prev_best.outer_loop_idx + 1}, grade {prev_best.grade}/7, {prev_best.num_conjectures_used} conjecture(s) used) as extra materials")
                        else:
                            log_print(f"[MOMUS] Final Solver {solver_idx+1}: injecting previous outer-loop best solution as extra materials")

                    chat = client.chats.create(model=model_id, config=gen_config)
                    response = chat.send_message(solve_prompt)

                    self._log_api_call(
                        step_name=f"Step 10 - Final Solver {solver_idx+1}",
                        role="solver",
                        prompt=solve_prompt,
                        response=response,
                    )

                    solution = response.text
                    solution = self.apply_answer_processor_rule1(chat, solution)

                    log_print(f"[Final Solver {solver_idx+1}] ✓ Generated and refined ({len(solution)} chars)")
                    return (solver_idx, chat, solution)
                except Exception as e:
                    log_print(f"[Final Solver {solver_idx+1}] ✗ Error: {e}")
                    return (solver_idx, None, "")

            # Launch all final solvers in parallel (all but one will get previous outer-loop best)
            total_solvers = self.num_final_parallel_solvers
            num_solvers_getting_prev_loop = total_solvers - 1
            log_print(f"\nLaunching {total_solvers} final solvers in parallel ({num_solvers_getting_prev_loop} with previous outer-loop best, 1 without for diversity)...")
            results: List[Optional[Tuple[Any, str]]] = [None] * total_solvers
            with ThreadPoolExecutor(max_workers=total_solvers) as executor:
                futures = {
                    executor.submit(final_solve_single, i): i for i in range(total_solvers)
                }
                for future in as_completed(futures):
                    idx, chat, solution = future.result()
                    results[idx] = (chat, solution)

            solver_sessions: List[Any] = []
            solutions: List[str] = []
            for item in results:
                if not item:
                    continue
                chat, solution = item
                if solution and chat:
                    solver_sessions.append(chat)
                    solutions.append(solution)

            normal_solvers = max(1, self.num_final_parallel_solvers - 1)
            total_solvers = normal_solvers + 1
            log_print(f"\nStep 10 complete: {len(solutions)}/{total_solvers} solutions generated")
            return solver_sessions, solutions

        except Exception as e:
            log_print(f"✗ Step 10 failed with error: {e}")
            import traceback

            traceback.print_exc()
            return [], []
