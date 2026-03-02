"""
Momus Core Agent: Dialectic Engine with Feedback Injection Loop

This agent implements the core Momus pipeline that:
Phase 1: Solver-Grader Loop with Feedback Injection
  1. Generate K initial solutions in parallel
  2. Sequential grading (single session with context)
  3. Feedback injection (inject feedback back to solver sessions)
  4. Re-grading (same grader session)
  5. Loop condition check (7/7 → verify, <5 → retry, >=5 → Phase 2)

Phase 2: Extraction & Recursive Verification
  6. Conjecture extraction from top solutions
  7. Quality control (self-contained check)
  8. Recursive verification (batch solve + split grade)

Phase 3: Integration & Final Solving
  9. Selection & conflict resolution (hallucination detection)
  10. Final parallel solving with proven lemmas
  11. Final grading loop

Key Innovation: Feedback injection loop + Batch solving with split grading
"""

from typing import Optional, Tuple, List, Dict, Any
import json
import re
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from .base_agent import BaseAgent, SolutionStatus
from ..utils.config_utils import get_template_required
from ..utils.logger import log_print, api_log_event

# Try to import genai SDK
try:
    from google import genai
    from google.genai import types
    HAS_GENAI_SDK = True
except ImportError:
    HAS_GENAI_SDK = False


class MomusCoreAgent(BaseAgent):
    """
    Momus core agent implementing dialectic engine with feedback injection loop

    Pipeline Overview:
    - Phase 1: Solver-Grader Loop (Steps 1-5)
    - Phase 2: Extraction & Recursive Verification (Steps 6-8)
    - Phase 3: Integration & Final Solving (Steps 9-11)
    """

    def __init__(
        self,
        config_path: str = "imo_solver/config/momus_config.yaml",
        prompts_path: str = "imo_solver/prompts/momus_prompts.yaml",
        base_models_path: Optional[str] = None,
        log_file: Optional[str] = None,
    ):
        """Initialize Momus core agent."""
        super().__init__(config_path, prompts_path, base_models_path, log_file)

        # Load execution parameters
        self.num_parallel_solvers = self.config_manager.execution.get("num_parallel_solvers", 3)
        self.max_solver_grader_rounds = self.config_manager.execution.get("max_solver_grader_rounds", 2)
        self.min_grade_for_phase2 = self.config_manager.execution.get("min_grade_for_phase2", 5)
        self.num_top_solutions = self.config_manager.execution.get("num_top_solutions", 2)
        self.max_verification_rounds = self.config_manager.execution.get("max_verification_rounds", 1)
        self.conjecture_grade_threshold = self.config_manager.execution.get("conjecture_grade_threshold", 5)
        self.num_final_parallel_solvers = self.config_manager.execution.get("num_final_parallel_solvers", 3)
        self.success_threshold = self.config_manager.execution.get("success_threshold", 7)
        self.rule2_verification_count = self.config_manager.execution.get("rule2_verification_count", 2)
        self.max_outer_loops = self.config_manager.execution.get("max_outer_loops", 1)

        log_print("\n" + "="*80)
        log_print("MOMUS CORE AGENT INITIALIZED")
        log_print("="*80)
        log_print(f"Phase 1 - Parallel solvers: {self.num_parallel_solvers}")
        log_print(f"Phase 1 - Max S-G rounds: {self.max_solver_grader_rounds}")
        log_print(f"Phase 2 - Top solutions: {self.num_top_solutions}")
        log_print(f"Phase 2 - Max verification rounds: {self.max_verification_rounds}")
        log_print(f"Phase 3 - Final parallel solvers: {self.num_final_parallel_solvers}")
        log_print(f"Max outer loops: {self.max_outer_loops}")
        log_print(f"Success threshold: {self.success_threshold}/7")
        log_print(f"Rule 2 verifications: {self.rule2_verification_count}")
        log_print("="*80)

        # Initialize API call counter with thread-safe lock
        self._api_call_count = 0
        self._api_call_lock = threading.Lock()

        # Persistent Gemini client - MUST be stored as instance variable
        # to prevent garbage collection which would close chat sessions
        self._genai_client = None

    # ========================================================================
    # MAIN PIPELINE
    # ========================================================================

    def run(
        self,
        problem_statement: str,
        max_runs: int = None,
        **kwargs
    ) -> Tuple[SolutionStatus, Optional[str]]:
        """
        Main execution method implementing the Momus core pipeline with outer loop

        Args:
            problem_statement: The IMO problem to solve
            max_runs: Not used in the core pipeline

        Returns:
            (SolutionStatus, solution_text) tuple
        """
        log_print("\n" + "="*80)
        log_print("STARTING MOMUS CORE PIPELINE")
        log_print("="*80)
        log_print(f"Problem:\n{problem_statement}\n")

        # Phase 1: Solver-Grader Loop (runs once, outside outer loop)
        solutions, feedbacks, grades, max_grade = self.phase1_solver_grader_loop(
            problem_statement
        )

        # Track all previous solutions, feedbacks, and grades for final solving
        all_previous_solutions = solutions.copy()
        all_previous_feedbacks = feedbacks.copy()
        all_previous_grades = grades.copy()

        if not solutions:
            log_print("✗ Phase 1 failed: No solutions generated")
            return (SolutionStatus.UNSOLVED, None)

        # Check for perfect score with Rule 2 verification
        if max_grade == 7:
            log_print(f"\n{'='*80}")
            log_print("PERFECT SCORE DETECTED - TRIGGERING RULE 2 VERIFICATION")
            log_print(f"{'='*80}")
            best_solution = self._get_best_solution(solutions, grades)
            if self.verify_perfect_solution_rule2(problem_statement, best_solution):
                log_print("\n✓ RULE 2 VERIFICATION PASSED - SUCCESS!")
                return (SolutionStatus.SOLVED, best_solution)
            else:
                log_print("\n✗ Rule 2 verification failed, treating as partial solution")

        # Check if we should retry or proceed to Phase 2
        if max_grade < self.min_grade_for_phase2:
            log_print(f"\n✗ Max grade {max_grade} < {self.min_grade_for_phase2}, should retry")
            log_print("(core pipeline: Retry not implemented in this version, continuing to Phase 2)")

        # Accumulate proven lemmas across outer loop iterations
        all_proven_lemmas: List[Dict[str, Any]] = []
        # Expose accumulated lemmas for subclasses (e.g., momus extractor materials)
        self._accumulated_proven_lemmas: List[Dict[str, Any]] = []
        best_final_solution = None
        best_final_grade = 0
        best_final_loop_idx = -1

        # Track current solutions and grades for iterative updates
        # Start with Phase 1 solutions, then use Phase 3 outputs for subsequent iterations
        current_solutions = solutions
        current_grades = grades
        current_feedbacks = feedbacks

        # =====================================================================
        # OUTER LOOP: Iterate Phase 2 & Phase 3
        # =====================================================================
        for outer_loop_idx in range(self.max_outer_loops):
            log_print(f"\n{'#'*80}")
            log_print(f"OUTER LOOP {outer_loop_idx + 1}/{self.max_outer_loops}")
            log_print(f"{'#'*80}")

            if all_proven_lemmas:
                log_print(f"Accumulated lemmas from previous iterations: {len(all_proven_lemmas)}")

            if outer_loop_idx > 0:
                log_print(f"Using solutions from previous Phase 3 ({len(current_solutions)} solutions)")

            # Phase 2: Extraction & Recursive Verification
            # Uses current_solutions (Phase 1 for first iteration, Phase 3 for subsequent)
            log_print(f"\n{'='*80}")
            log_print(f"PHASE 2: EXTRACTION & RECURSIVE VERIFICATION (Loop {outer_loop_idx + 1})")
            log_print(f"{'='*80}")
            new_proven_lemmas = self.phase2_extraction_and_verification(
                problem_statement,
                current_solutions,
                current_grades,
                current_feedbacks,
                outer_loop_idx=outer_loop_idx,
            )

            # Accumulate new lemmas (avoid duplicates by conjecture text)
            existing_conjectures = {l.get("conjecture", "") for l in all_proven_lemmas}
            for lemma in new_proven_lemmas:
                if lemma.get("conjecture", "") not in existing_conjectures:
                    all_proven_lemmas.append(lemma)
                    existing_conjectures.add(lemma.get("conjecture", ""))
            # keep in sync for downstream use (e.g., conjecture extractor materials)
            self._accumulated_proven_lemmas = list(all_proven_lemmas)

            log_print(f"\nTotal accumulated lemmas: {len(all_proven_lemmas)}")

            # Phase 3: Integration & Final Solving
            log_print(f"\n{'='*80}")
            log_print(f"PHASE 3: INTEGRATION & FINAL SOLVING (Loop {outer_loop_idx + 1})")
            log_print(f"{'='*80}")
            final_solution, final_grade, phase3_solutions, phase3_grades, phase3_feedbacks = self.phase3_final_solving(
                problem_statement, all_proven_lemmas, 
                all_previous_solutions, all_previous_feedbacks, all_previous_grades,
                outer_loop_idx=outer_loop_idx
            )

            # Update current_solutions for next iteration (iterative refinement)
            if phase3_solutions:
                current_solutions = phase3_solutions
                current_grades = phase3_grades
                current_feedbacks = phase3_feedbacks
                
                # Accumulate for next iteration's final solving
                all_previous_solutions.extend(phase3_solutions)
                all_previous_feedbacks.extend(phase3_feedbacks)
                all_previous_grades.extend(phase3_grades)
                
                log_print(f"Updated solutions for next iteration: {len(current_solutions)} solutions")

            if not final_solution:
                log_print(f"✗ Phase 3 failed in loop {outer_loop_idx + 1}: No final solution generated")
                continue

            # Track best solution across iterations
            # Prefer later iterations in case of ties (iterative refinement)
            is_better_grade = final_grade > best_final_grade
            is_tie_later_loop = final_grade == best_final_grade and outer_loop_idx > best_final_loop_idx
            if is_better_grade or is_tie_later_loop:
                best_final_grade = final_grade
                best_final_solution = final_solution
                best_final_loop_idx = outer_loop_idx
                if is_better_grade:
                    log_print(f"✓ New best solution: grade {final_grade}/7 (loop {outer_loop_idx + 1})")
                else:
                    log_print(f"✓ Updated best solution: grade {final_grade}/7 (tie-break, preferring later loop {outer_loop_idx + 1})")

            # Check final grade with Rule 2 verification
            if final_grade == 7:
                log_print(f"\n{'='*80}")
                log_print(f"PERFECT SCORE IN LOOP {outer_loop_idx + 1} - TRIGGERING RULE 2 VERIFICATION")
                log_print(f"{'='*80}")
                if self.verify_perfect_solution_rule2(problem_statement, final_solution):
                    log_print("\n✓ RULE 2 VERIFICATION PASSED - SUCCESS!")
                    return (SolutionStatus.SOLVED, final_solution)
                else:
                    log_print("\n✗ Rule 2 verification failed, continuing to next iteration")

        # End of outer loop
        log_print(f"\n{'='*80}")
        log_print(f"OUTER LOOP COMPLETED ({self.max_outer_loops} iterations)")
        log_print(f"{'='*80}")
        log_print(f"Best final grade: {best_final_grade}/7")

        if best_final_grade >= self.success_threshold:
            log_print(f"✓ Best grade {best_final_grade} >= threshold {self.success_threshold}")
            return (SolutionStatus.SOLVED, best_final_solution)

        log_print(f"\n✗ Best grade {best_final_grade} < {self.success_threshold}")
        return (SolutionStatus.UNSOLVED, best_final_solution)

    # ========================================================================
    # PHASE 1: SOLVER-GRADER LOOP
    # ========================================================================

    def phase1_solver_grader_loop(
        self, problem: str
    ) -> Tuple[List[str], List[str], List[int], int]:
        """
        Phase 1: Solver-Grader Loop with Feedback Injection

        Steps 1-5:
        1. Parallel initial solving (K solutions)
        2. Sequential grading (single grader session)
        3. Feedback injection (inject feedback back to solver sessions)
        4. Re-grading (same grader session)
        5. Loop condition & early exit

        Returns:
            (solutions, feedbacks, grades, max_grade) tuple
        """
        log_print(f"\n{'='*80}")
        log_print("PHASE 1: SOLVER-GRADER LOOP")
        log_print(f"{'='*80}")

        # Initialize variables in case all rounds fail
        solutions = []
        grades = []
        max_grade = 0

        for round_num in range(1, self.max_solver_grader_rounds + 1):
            log_print(f"\n{'='*70}")
            log_print(f"SOLVER-GRADER ROUND {round_num}/{self.max_solver_grader_rounds}")
            log_print(f"{'='*70}")

            # Step 1: Parallel initial solving
            solver_sessions, solutions = self.step1_parallel_solve(problem)
            if not solutions:
                log_print("✗ Step 1 failed")
                continue

            # Step 2: Parallel grading
            feedbacks, grades = self.step2_parallel_grade(
                problem, solutions
            )
            if not grades:
                log_print("✗ Step 2 failed")
                continue

            max_grade = max(grades) if grades else 0
            log_print(f"\nRound {round_num} - Max grade: {max_grade}/7")

            # Step 5: Early exit check
            if max_grade == 7:
                log_print(f"✓ Perfect score detected in round {round_num}")
                return solutions, feedbacks, grades, max_grade
            elif max_grade >= self.min_grade_for_phase2:
                log_print(f"✓ Sufficient score ({max_grade} >= {self.min_grade_for_phase2}), proceeding to Phase 2")
                return solutions, feedbacks, grades, max_grade

            # Step 3: Feedback injection
            log_print(f"\n--- Step 3: Feedback Injection (Round {round_num}) ---")
            # Extract relevant parts of feedback based on feedback_mode config
            extracted_feedbacks = [self._extract_feedback_for_injection(f) for f in feedbacks]
            improved_solutions = self.step3_feedback_injection(
                solver_sessions, extracted_feedbacks
            )
            if not improved_solutions:
                log_print("✗ Step 3 failed")
                continue

            # Step 4: Parallel Re-Grading
            log_print(f"\n--- Step 4: Parallel Re-Grading (Round {round_num}) ---")
            new_feedbacks, new_grades = self.step2_parallel_grade(
                problem, improved_solutions
            )

            # Update for next iteration
            solutions = improved_solutions
            grades = new_grades
            max_grade = max(grades) if grades else 0
            log_print(f"\nAfter improvement - Max grade: {max_grade}/7")

            # Check again after improvement
            if max_grade == 7:
                log_print(f"✓ Perfect score after improvement in round {round_num}")
                return solutions, new_feedbacks, grades, max_grade
            elif max_grade >= self.min_grade_for_phase2:
                log_print(f"✓ Sufficient score after improvement")
                return solutions, new_feedbacks, grades, max_grade

        # All rounds completed
        log_print(f"\nPhase 1 completed after {self.max_solver_grader_rounds} rounds")
        # Return final feedbacks (from last grading round)
        final_feedbacks = new_feedbacks if 'new_feedbacks' in locals() else []
        return solutions, final_feedbacks, grades, max_grade

    def step1_parallel_solve(
        self, problem: str
    ) -> Tuple[List[Any], List[str]]:
        """
        Step 1: Generate K initial solutions in PARALLEL using genai SDK

        Uses ThreadPoolExecutor for true parallel execution.

        Returns:
            (solver_sessions, solutions) tuple
            - solver_sessions: List of chat session objects (for Step 3 reuse)
            - solutions: List of solution strings
        """
        log_print(f"\n{'='*70}")
        log_print(f"STEP 1: PARALLEL INITIAL SOLVING (K={self.num_parallel_solvers})")
        log_print(f"{'='*70}")

        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return [], []

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return [], []

        try:
            # Use persistent client to prevent garbage collection
            # which would close chat sessions before Step 3 feedback injection
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Get system prompt
            system_prompt = self.config_manager.get_role_prompt("solver", "system_prompt")

            # Get model and config
            model_id, gen_config = self._get_genai_model_config("solver", system_prompt)
            log_print(f"Using model: {model_id}")

            # Build solve prompt
            solve_prompt = get_template_required(
                "solve_instruction",
                self.config_manager,
                problem=problem,
                materials="None"
            )

            def solve_single(solver_idx: int) -> Tuple[int, Any, str]:
                """Single solver task for parallel execution"""
                try:
                    log_print(f"\n[Solver {solver_idx+1}] Starting...")

                    # Create a new chat session for each solver
                    chat = client.chats.create(model=model_id, config=gen_config)
                    response = chat.send_message(solve_prompt)

                    self._log_api_call(
                        step_name=f"Step 1 - Solver {solver_idx+1}/{self.num_parallel_solvers}",
                        role="solver",
                        prompt=solve_prompt,
                        response=response
                    )

                    solution = response.text
                    if solution:
                        # Apply Rule 1 (Answer-Processor) immediately
                        solution = self.apply_answer_processor_rule1(chat, solution)
                        log_print(f"[Solver {solver_idx+1}] ✓ Generated and improved ({len(solution)} chars)")
                        return (solver_idx, chat, solution)
                    else:
                        log_print(f"[Solver {solver_idx+1}] ✗ Failed (empty response)")
                        return (solver_idx, None, "")
                except Exception as e:
                    log_print(f"[Solver {solver_idx+1}] ✗ Error: {e}")
                    return (solver_idx, None, "")

            # Execute solvers in parallel
            log_print(f"\nLaunching {self.num_parallel_solvers} solvers in parallel...")
            results = [None] * self.num_parallel_solvers

            with ThreadPoolExecutor(max_workers=self.num_parallel_solvers) as executor:
                futures = {
                    executor.submit(solve_single, i): i
                    for i in range(self.num_parallel_solvers)
                }

                for future in as_completed(futures):
                    idx, chat, solution = future.result()
                    results[idx] = (chat, solution)

            # Collect results in order - only keep successful pairs
            # Both lists must have same length for step3 feedback injection
            solver_sessions = []
            solutions = []
            for i, (chat, solution) in enumerate(results):
                if solution and chat:
                    solver_sessions.append(chat)
                    solutions.append(solution)
                # Skip failed solvers entirely to maintain alignment

            log_print(f"\nStep 1 complete: {len(solutions)}/{self.num_parallel_solvers} solutions generated")
            return solver_sessions, solutions

        except Exception as e:
            log_print(f"✗ Step 1 failed with error: {e}")
            import traceback
            traceback.print_exc()
            return [], []
    def step2_parallel_grade(
        self, problem: str, solutions: List[str]
    ) -> Tuple[List[str], List[int]]:
        """
        Step 2: Parallel Grading (independent sessions)
        
        Also used for Step 4 and Step 11.

        Returns:
            (feedbacks, grades) tuple
        """
        log_print(f"\n{'='*70}")
        log_print("STEP 2/4/11: PARALLEL GRADING")
        log_print(f"{'='*70}")

        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return [], []

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return [], []

        try:
            # Use persistent client to prevent garbage collection
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Get system prompt
            system_prompt = self.config_manager.get_role_prompt("grader", "system_prompt")

            # Get model and config
            model_id, gen_config = self._get_genai_model_config("grader", system_prompt)

            def grade_single(idx: int, solution: str) -> Tuple[int, str, int]:
                """Single grading task for parallel execution"""
                try:
                    if not solution:
                        log_print(f"[Grader {idx+1}] ✗ Solution is empty")
                        return (idx, "", 0)

                    log_print(f"[Grader {idx+1}] Starting...")

                    # Extract Final Blueprint for grading (don't grade the dialectic process)
                    clean_solution = self._extract_final_blueprint(solution)

                    if not clean_solution:
                        log_print(f"[Grader {idx+1}] ✗ Failed to extract Final Blueprint, solution is empty after extraction")
                        return (idx, "", 0)

                    # Create FRESH grader session
                    grader = client.chats.create(model=model_id, config=gen_config)

                    # Build grade prompt with clean solution
                    grade_prompt = get_template_required(
                        "grade_instruction",
                        self.config_manager,
                        problem=problem,
                        solution=clean_solution,
                        materials="None"
                    )

                    response = grader.send_message(grade_prompt)

                    self._log_api_call(
                        step_name=f"Parallel Grade {idx+1}",
                        role="grader",
                        prompt=grade_prompt,
                        response=response
                    )

                    feedback = response.text if response.text else ""
                    grade = self._extract_grade(feedback)
                    
                    log_print(f"[Grader {idx+1}] Grade: {grade}/7")
                    return (idx, feedback, grade)

                except Exception as e:
                    log_print(f"[Grader {idx+1}] ✗ Error: {e}")
                    return (idx, "", 0)

            # Execute graders in parallel
            log_print(f"\nLaunching {len(solutions)} graders in parallel...")
            results = [None] * len(solutions)
            
            with ThreadPoolExecutor(max_workers=len(solutions)) as executor:
                futures = {
                    executor.submit(grade_single, i, sol): i 
                    for i, sol in enumerate(solutions)
                }
                
                for future in as_completed(futures):
                    idx, feedback, grade = future.result()
                    results[idx] = (feedback, grade)

            # Unpack results
            feedbacks = [r[0] for r in results]
            grades = [r[1] for r in results]

            log_print(f"\nGrading complete: {grades}")
            return feedbacks, grades

        except Exception as e:
            log_print(f"✗ Parallel grading failed with error: {e}")
            import traceback
            traceback.print_exc()
            return [], []

    def step3_feedback_injection(
        self, solver_sessions: List[Any], feedbacks: List[str]
    ) -> List[str]:
        """
        Step 3: Feedback Injection - inject feedback back to solver sessions IN PARALLEL

        Uses ThreadPoolExecutor for true parallel execution.

        Returns:
            List of improved solution strings
        """
        log_print(f"\n{'='*70}")
        log_print("STEP 3: FEEDBACK INJECTION (Parallel)")
        log_print(f"{'='*70}")

        def inject_single(args: Tuple[int, Any, str]) -> Tuple[int, str]:
            """Single feedback injection task for parallel execution"""
            idx, session, feedback = args

            if session is None:
                log_print(f"[Feedback {idx+1}] ✗ Session is None, skipping")
                return (idx, "")

            log_print(f"[Feedback {idx+1}] Injecting...")

            # Build feedback injection prompt
            feedback_prompt = get_template_required(
                "feedback_injection",
                self.config_manager,
                feedback=feedback
            )

            try:
                # Send feedback to the SAME solver session
                response = session.send_message(feedback_prompt)

                self._log_api_call(
                    step_name=f"Step 3 - Feedback Injection {idx+1}",
                    role="solver",
                    prompt=feedback_prompt,
                    response=response
                )

                improved_solution = response.text

                # Apply Rule 1 (Answer-Processor) immediately after feedback injection
                improved_solution = self.apply_answer_processor_rule1(session, improved_solution)

                log_print(f"[Feedback {idx+1}] ✓ Improved ({len(improved_solution)} chars)")
                return (idx, improved_solution)

            except Exception as e:
                log_print(f"[Feedback {idx+1}] ✗ Failed: {e}")
                return (idx, "")

        # Prepare tasks
        tasks = [(i, session, feedback) for i, (session, feedback) in enumerate(zip(solver_sessions, feedbacks))]

        # Execute feedback injections in parallel
        log_print(f"\nInjecting feedback into {len(tasks)} solvers in parallel...")
        results = [None] * len(tasks)

        with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
            futures = {executor.submit(inject_single, task): task[0] for task in tasks}

            for future in as_completed(futures):
                idx, solution = future.result()
                results[idx] = solution

        log_print(f"\nStep 3 complete: {len([s for s in results if s])}/{len(solver_sessions)} improved")
        return results

    # Step 4: Re-grading (removed, use step2_parallel_grade instead)


    # ========================================================================
    # PHASE 2: EXTRACTION & RECURSIVE VERIFICATION
    # ========================================================================

    def phase2_extraction_and_verification(
        self,
        problem: str,
        solutions: List[str],
        grades: List[int],
        feedbacks: Optional[List[str]] = None,
        outer_loop_idx: int = 0
    ) -> List[Dict[str, str]]:
        """
        Phase 2: Extraction & Recursive Verification

        Steps 6-8:
        6. Conjecture extraction from top solutions
        7. Quality control (self-contained check)
        8. Recursive verification (batch solve + split grade)

        Args:
            problem: The problem statement
            solutions: List of solutions from Phase 1
            grades: List of grades corresponding to solutions
            outer_loop_idx: Current outer loop iteration index (0-based)

        Returns:
            List of proven lemmas: [{"conjecture": str, "proof": str}, ...]
        """
        loop_prefix = f"[Loop {outer_loop_idx + 1}] " if outer_loop_idx > 0 else ""

        # Step 6: Extract conjectures from top solutions
        top_solutions, top_feedbacks = self._get_top_solutions(
            solutions, grades, feedbacks, self.num_top_solutions
        )

        conjectures_data = self.step6_conjecture_extraction(
            problem, top_solutions, top_feedbacks, outer_loop_idx=outer_loop_idx
        )
        if not conjectures_data:
            log_print(f"✗ {loop_prefix}Step 6 failed: No conjectures extracted")
            return []

        # Step 7: Quality control
        validated_conjectures = self.step7_quality_control(conjectures_data, outer_loop_idx=outer_loop_idx)
        if not validated_conjectures:
            log_print(f"✗ {loop_prefix}Step 7 failed: No conjectures passed quality control")
            return []

        # Step 8: Recursive verification
        proven_lemmas = self.step8_recursive_verification(
            problem, validated_conjectures, outer_loop_idx=outer_loop_idx
        )

        return proven_lemmas

    def step6_conjecture_extraction(
        self, problem: str, solutions: List[str], feedbacks: List[str],
        outer_loop_idx: int = 0
    ) -> Optional[Dict[str, Any]]:
        """
        Step 6: Conjecture extraction from top solutions

        Returns:
            Dict with keys: "conjectures", "negations", "proof"
        """
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
            # Use persistent client to prevent garbage collection
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Get system prompt
            system_prompt = self.config_manager.get_role_prompt(
                "conjecture_extractor", "system_prompt"
            )

            # Get model and config
            model_id, gen_config = self._get_genai_model_config(
                "conjecture_extractor", system_prompt
            )

            # Format solutions
            solutions_text = "\n\n".join([
                f"=== Solution {i+1} ===\n{sol}"
                for i, sol in enumerate(solutions)
            ])

            # Format grader reports
            grader_reports = "\n\n".join([
                f"=== Feedback for Solution {i+1} ===\n{fb}"
                for i, fb in enumerate(feedbacks)
            ])

            # Build conjecture extraction prompt
            extraction_prompt = get_template_required(
                "conjecture_extraction",
                self.config_manager,
                problem=problem,
                solutions=solutions_text,
                grader_reports=grader_reports
            )

            log_print("Extracting conjectures...")

            # Create chat session
            chat = client.chats.create(model=model_id, config=gen_config)
            response = chat.send_message(extraction_prompt)

            self._log_api_call(
                step_name="Step 6 - Conjecture Extraction",
                role="conjecture_extractor",
                prompt=extraction_prompt,
                response=response
            )

            # Follow-up for self-contained check
            followup_prompt = get_template_required(
                "self_contained_followup",
                self.config_manager
            )

            response2 = chat.send_message(followup_prompt)

            self._log_api_call(
                step_name="Step 6 - Self-Contained Follow-up",
                role="conjecture_extractor",
                prompt=followup_prompt,
                response=response2
            )

            result_text = response2.text

            # Parse conjectures and negations using LLM parser (primary)
            # Falls back to regex parser if LLM fails
            conjectures_data = self._parse_conjectures_with_llm(result_text)

            if not conjectures_data:
                log_print("  Falling back to regex parser...")
                conjectures_data = self._parse_conjecture_extraction(result_text)

            if conjectures_data:
                num_conj = len(conjectures_data.get('conjectures', []))
                num_neg = len(conjectures_data.get('negations', []))
                log_print(f"✓ Extracted {num_conj} conjectures, {num_neg} negations")
                return conjectures_data
            else:
                log_print("✗ Failed to parse conjecture extraction")
                return None

        except Exception as e:
            log_print(f"✗ Step 6 failed with error: {e}")
            import traceback
            traceback.print_exc()
            return None

    def step7_quality_control(
        self, conjectures_data: Dict[str, Any],
        outer_loop_idx: int = 0
    ) -> List[Dict[str, str]]:
        """
        Step 7: Quality control - verify conjectures are self-contained

        Returns:
            List of validated conjecture dicts: [{"conjecture": str, "negation": str}, ...]
        """
        loop_suffix = f" (Loop {outer_loop_idx + 1})" if outer_loop_idx > 0 else ""
        log_print(f"\n{'='*70}")
        log_print(f"STEP 7: QUALITY CONTROL (Self-Contained Check){loop_suffix}")
        log_print(f"{'='*70}")

        conjectures = conjectures_data.get("conjectures", [])
        negations = conjectures_data.get("negations", [])

        if len(conjectures) != len(negations):
            log_print(f"✗ Mismatch: {len(conjectures)} conjectures but {len(negations)} negations")
            return []

        validated = []

        for i, (conj, neg) in enumerate(zip(conjectures, negations)):
            log_print(f"\nChecking conjecture {i+1}/{len(conjectures)}...")

            if self._check_self_contained(conj, neg):
                validated.append({"conjecture": conj, "negation": neg})
                log_print(f"✓ Conjecture {i+1} passed quality control")
            else:
                log_print(f"✗ Conjecture {i+1} failed quality control")

        log_print(f"\nStep 7 complete: {len(validated)}/{len(conjectures)} conjectures validated")
        return validated

    def step8_recursive_verification(
        self, problem: str, validated_conjectures: List[Dict[str, str]],
        outer_loop_idx: int = 0
    ) -> List[Dict[str, str]]:
        """
        Step 8: Recursive Verification (Individual Solve + Individual Grade)

        For each conjecture pair (C, ~C):
        - Solve C (parallel) -> Grade C (parallel)
        - Solve ~C (parallel) -> Grade ~C (parallel)

        Then Step 9: Selection & Conflict Resolution
        """
        loop_suffix = f" (Loop {outer_loop_idx + 1})" if outer_loop_idx > 0 else ""
        log_print(f"\n{'='*70}")
        log_print(f"STEP 8: RECURSIVE VERIFICATION (Individual){loop_suffix}")
        log_print(f"{'='*70}")
        
        tasks = []
        # Prepare tasks for all conjectures and their negations
        for i, conj_dict in enumerate(validated_conjectures):
            # Positive task
            tasks.append({
                "id": f"C{i+1}",
                "statement": conj_dict["conjecture"],
                "is_positive": True
            })
            # Negative task
            tasks.append({
                "id": f"NC{i+1}",
                "statement": conj_dict["negation"],
                "is_positive": False
            })

        log_print(f"\nLaunching {len(tasks)} verification tasks in parallel...")
        
        results = {} # map task_id -> (proof, grade)

        with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
            future_to_task = {
                executor.submit(self._solve_and_grade_single_conjecture, task["statement"], task["id"]): task["id"]
                for task in tasks
            }
            
            for future in as_completed(future_to_task):
                task_id = future_to_task[future]
                try:
                    proof, grade = future.result()
                    results[task_id] = {"proof": proof, "grade": grade}
                except Exception as e:
                    log_print(f"✗ Task {task_id} failed: {e}")
                    results[task_id] = {"proof": "", "grade": 0}

        # Organize for conflict resolution
        positive_results = {}
        negative_results = {}
        
        for task in tasks:
            tid = task["id"]
            res = results.get(tid, {"proof": "", "grade": 0})
            if task["is_positive"]:
                positive_results[tid] = res
            else:
                negative_results[tid] = res

        # Step 9: Conflict Resolution
        return self._resolve_conflicts(validated_conjectures, positive_results, negative_results)

    def _solve_and_grade_single_conjecture(self, statement: str, task_id: str) -> Tuple[str, int]:
        """
        Helper: Solve and grade a single conjecture statement
        Returns: (proof, grade)
        """
        if not HAS_GENAI_SDK:
            return "", 0
            
        api_key = self._get_gemini_api_key()
        if not api_key:
            return "", 0
            
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
                return "", 0

            # Extract Final Blueprint for grading
            clean_proof = self._extract_final_blueprint(proof)

            if not clean_proof:
                log_print(f"[{task_id}] ✗ Failed to extract Final Blueprint, proof is empty after extraction")
                return "", 0

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
            log_print(f"[{task_id}] Grade: {grade}/7")
            
            return proof, grade
            
        except Exception as e:
            log_print(f"[{task_id}] ✗ Error: {e}")
            return "", 0


    # ========================================================================
    # PHASE 3: INTEGRATION & FINAL SOLVING
    # ========================================================================

    def phase3_final_solving(
        self, problem: str, proven_lemmas: List[Dict[str, str]],
        previous_solutions: List[str], previous_feedbacks: List[str], previous_grades: List[int],
        outer_loop_idx: int = 0
    ) -> Tuple[Optional[str], int, List[str], List[int]]:
        """
        Phase 3: Integration & Final Solving

        Steps 10-11:
        10. Final parallel solving with proven lemmas
        11. Final grading loop

        Args:
            problem: The problem statement
            proven_lemmas: List of proven lemmas to use
            previous_solutions: All previous solutions from Phase 1 and previous Phase 3 iterations
            previous_feedbacks: All previous grader feedbacks corresponding to previous_solutions
            previous_grades: All previous grades corresponding to previous_solutions
            outer_loop_idx: Current outer loop iteration index (0-based)

        Returns:
            (best_solution, max_grade, all_solutions, all_grades, all_feedbacks) tuple
            - best_solution: The highest-graded solution
            - max_grade: The maximum grade achieved
            - all_solutions: All solutions generated (for use in next iteration)
            - all_grades: All grades (for use in next iteration)
            - all_feedbacks: All grader feedbacks (for use in next iteration)
        """
        loop_suffix = f" (Loop {outer_loop_idx + 1})" if outer_loop_idx > 0 else ""

        # Step 10: Final parallel solving
        log_print(f"\n{'='*70}")
        log_print(f"STEP 10: FINAL PARALLEL SOLVING (With Proven Lemmas){loop_suffix}")
        log_print(f"{'='*70}")

        if proven_lemmas:
            log_print(f"\nUsing {len(proven_lemmas)} proven lemmas:")
            for i, lemma in enumerate(proven_lemmas):
                log_print(f"  Lemma {i+1} (grade {lemma.get('grade', '?')}): {lemma['conjecture'][:100]}...")
        else:
            log_print("\nNo proven lemmas available")

        if previous_solutions:
            log_print(f"\nUsing {len(previous_solutions)} previous solutions for reference")

        _, final_solutions = self._final_parallel_solve(
            problem, proven_lemmas, previous_solutions, previous_feedbacks, previous_grades
        )

        if not final_solutions:
            log_print(f"✗ Step 10 failed{loop_suffix}: No final solutions generated")
            return None, 0, [], [], []

        # Step 11: Final grading loop (similar to Phase 1)
        log_print(f"\n{'='*70}")
        log_print(f"STEP 11: FINAL GRADING LOOP{loop_suffix}")
        log_print(f"{'='*70}")

        feedbacks, grades = self.step2_parallel_grade(problem, final_solutions)

        max_grade = max(grades) if grades else 0
        best_solution = self._get_best_solution(final_solutions, grades)

        log_print(f"\nFinal max grade{loop_suffix}: {max_grade}/7")

        return best_solution, max_grade, final_solutions, grades, feedbacks

    # ========================================================================
    # HELPER METHODS
    # ========================================================================

    def apply_answer_processor_rule1(
        self, solver_session: Any, proof: str
    ) -> Optional[str]:
        """
        Rule 1: Answer-Processor (Per-Solver-Call Protocol)

        MUST be executed immediately after every Solver generation (Steps 1, 4, 8, 10).
        Single pass only (do not loop recursively).

        Args:
            solver_session: The solver chat session to regenerate in
            proof: The proof text to scan

        Returns:
            Improved proof string, or None if failed
        """
        # Check if answer processor is disabled
        if not self.config_manager.execution.get("enable_answer_processor", True):
            log_print("  [Rule 1] Answer-Processor disabled, skipping")
            return proof

        log_print(f"\n{'='*70}")
        log_print("RULE 1: ANSWER-PROCESSOR (Scan & Regenerate)")
        log_print(f"{'='*70}")

        try:
            # Step 1: Scan proof with Gemini-Flash
            from ..utils.config_utils import send_role_based_request

            # Get Answer-Processor system prompt
            answer_processor_system_prompt = self.config_manager.get_role_prompt(
                "answer_processor", "system_prompt"
            )

            scan_prompt = get_template_required(
                "answer_processor_scan",
                self.config_manager,
                proof=proof
            )

            log_print("  Scanning proof for lazy phrases...")
            comments = send_role_based_request(
                answer_processor_system_prompt,
                scan_prompt,
                role="answer_processor",
                config_manager=self.config_manager
            )

            if not comments:
                log_print("  ✗ Answer-Processor scan failed, using original proof")
                return proof

            # Step 2: Conditional Check
            if "NO_ISSUES" in comments.strip():
                log_print("  ✓ NO_ISSUES detected - skipping regeneration")
                return proof

            log_print(f"  ✓ Found issues ({len(comments)} chars of comments)")

            # Step 3: Ask Solver to regenerate
            regenerate_prompt = get_template_required(
                "regenerate_proof",
                self.config_manager,
                comments=comments
            )

            log_print("  Asking solver to regenerate proof...")
            response = solver_session.send_message(regenerate_prompt)

            self._log_api_call(
                step_name="Rule 1 - Regenerate Proof",
                role="solver",
                prompt=regenerate_prompt,
                response=response
            )

            improved_proof = response.text
            log_print(f"  ✓ Proof regenerated ({len(improved_proof)} chars)")

            return improved_proof

        except Exception as e:
            log_print(f"  ✗ Rule 1 (Answer-Processor) failed: {e}")
            import traceback
            traceback.print_exc()
            return proof  # Fallback to original

    def verify_perfect_solution_rule2(
        self, problem: str, solution: str
    ) -> bool:
        """
        Rule 2: 7/7 Verification Rule (formerly Rule 1)

        7/7 solutions must be verified in 2 fresh independent grader sessions

        Returns:
            True if both verifications return 7/7, False otherwise
        """
        log_print(f"\n{'='*70}")
        log_print("RULE 2: DOUBLE VERIFICATION (2 Independent Graders)")
        log_print(f"{'='*70}")

        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return False

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return False

        try:
            # Use persistent client to prevent garbage collection
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Get system prompt
            system_prompt = self.config_manager.get_role_prompt("grader", "system_prompt")

            # Get model and config
            model_id, gen_config = self._get_genai_model_config("grader", system_prompt)

            # Extract Final Blueprint for grading
            clean_solution = self._extract_final_blueprint(solution)

            if not clean_solution:
                log_print(f"  ✗ Failed to extract Final Blueprint, solution is empty after extraction")
                return False

            # Build grade prompt (same for all verifiers)
            grade_prompt = get_template_required(
                "grade_instruction",
                self.config_manager,
                problem=problem,
                solution=clean_solution,
                materials="None"
            )

            def verify_single(verifier_idx: int) -> Tuple[int, int]:
                """Single verifier task for parallel execution"""
                try:
                    log_print(f"\n[Verifier {verifier_idx+1}] Starting...")

                    # Create FRESH grader session
                    grader = client.chats.create(model=model_id, config=gen_config)

                    response = grader.send_message(grade_prompt)

                    self._log_api_call(
                        step_name=f"Rule 2 - Verification {verifier_idx+1}/{self.rule2_verification_count}",
                        role="grader",
                        prompt=grade_prompt,
                        response=response
                    )

                    feedback = response.text if response.text else ""
                    grade = self._extract_grade(feedback)

                    log_print(f"[Verifier {verifier_idx+1}] Score: {grade}/7")
                    return (verifier_idx, grade)
                except Exception as e:
                    log_print(f"[Verifier {verifier_idx+1}] Error: {e}")
                    return (verifier_idx, 0)  # Return 0 on error (fails verification)

            # Execute verifiers in parallel
            verification_scores = [0] * self.rule2_verification_count
            with ThreadPoolExecutor(max_workers=self.rule2_verification_count) as executor:
                futures = {executor.submit(verify_single, i): i for i in range(self.rule2_verification_count)}
                for future in as_completed(futures):
                    idx, grade = future.result()
                    verification_scores[idx] = grade

            # Both must be 7/7
            success = all(score == 7 for score in verification_scores)

            if success:
                log_print(f"\n✓ RULE 2 PASSED: All {self.rule2_verification_count} verifications returned 7/7")
            else:
                log_print(f"\n✗ RULE 2 FAILED: Scores {verification_scores} (need all 7s)")

            return success

        except Exception as e:
            log_print(f"✗ Rule 2 verification failed with error: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _check_self_contained(self, conjecture: str, negation: str) -> bool:
        """Use lightweight model to check if conjecture and negation are self-contained"""
        log_print("  Checking self-containment...")

        # Build check prompt
        check_prompt = get_template_required(
            "self_contained_check",
            self.config_manager,
            conjecture=conjecture,
            negation=negation
        )

        try:
            # Use quality_checker role (lightweight model)
            from ..utils.config_utils import send_role_based_request

            response = send_role_based_request(
                "",  # No system prompt needed
                check_prompt,
                role="quality_checker",
                config_manager=self.config_manager
            )

            if response and "PASS" in response.upper():
                return True
            else:
                log_print(f"  Failed: {response[:200] if response else 'No response'}")
                return False

        except Exception as e:
            log_print(f"  Error checking self-containment: {e}")
            return False

    def _resolve_conflicts(
        self, validated_conjectures: List[Dict[str, str]],
        positive_results: Dict[str, Dict[str, Any]],
        negative_results: Dict[str, Dict[str, Any]]
    ) -> List[Dict[str, str]]:
        """
        Step 9: Selection & Conflict Resolution
        
        Filter: Grade >= threshold
        Conflict: If both C and ~C proven -> discard both (hallucination detection)
        
        Returns:
            List of proven lemmas: [{"conjecture": str, "proof": str, "grade": int}, ...]
        """
        log_print("\nResolving conflicts and selecting proven lemmas...")
        
        proven_lemmas = []
        
        for i, conj_dict in enumerate(validated_conjectures):
            conj_id = f"C{i+1}"
            neg_id = f"NC{i+1}"
            
            # Get results
            pos_res = positive_results.get(conj_id, {"grade": 0, "proof": ""})
            neg_res = negative_results.get(neg_id, {"grade": 0, "proof": ""})
            
            pos_grade = pos_res.get("grade", 0)
            neg_grade = neg_res.get("grade", 0)
            
            log_print(f"\n  {conj_id}: Positive grade {pos_grade}, Negative grade {neg_grade}")
            
            # Check for conflict
            if pos_grade >= self.conjecture_grade_threshold and neg_grade >= self.conjecture_grade_threshold:
                log_print(f"    ✗ CONFLICT DETECTED: Both proven (hallucination) - discarding both")
                continue
                
            # Select proven lemma
            if pos_grade >= self.conjecture_grade_threshold:
                proven_lemmas.append({
                    "conjecture": conj_dict["conjecture"],
                    "proof": pos_res.get("proof", ""),
                    "grade": pos_grade
                })
                log_print(f"    ✓ Positive conjecture proven (grade {pos_grade})")
            elif neg_grade >= self.conjecture_grade_threshold:
                proven_lemmas.append({
                    "conjecture": conj_dict["negation"],
                    "proof": neg_res.get("proof", ""),
                    "grade": neg_grade
                })
                log_print(f"    ✓ Negative conjecture proven (grade {neg_grade})")
            else:
                log_print(f"    ✗ Neither proven (grades {pos_grade}, {neg_grade})")
                
        log_print(f"\nConflict resolution complete: {len(proven_lemmas)} proven lemmas")
        return proven_lemmas
    def _final_parallel_solve(
        self, problem: str, proven_lemmas: List[Dict[str, str]],
        previous_solutions: List[str], previous_feedbacks: List[str], previous_grades: List[int]
    ) -> Tuple[List[Any], List[str]]:
        """
        Step 10: Final parallel solving with proven lemmas

        Constructs different prompts based on lemma grades:
        - Grade 7/7: "You may use them as Lemmas without further proof"
        - Grade 5-6: Provide as reference material only
        
        Also includes the highest scoring previous solution and its feedback.

        Args:
            problem: The problem statement
            proven_lemmas: List of proven lemmas
            previous_solutions: All previous solutions from Phase 1 and previous Phase 3 iterations
            previous_feedbacks: All previous grader feedbacks
            previous_grades: All previous grades
        """
        if not HAS_GENAI_SDK:
            return [], []

        api_key = self._get_gemini_api_key()
        if not api_key:
            return [], []

        try:
            # Use persistent client to prevent garbage collection
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client
            system_prompt = self.config_manager.get_role_prompt("solver", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("solver", system_prompt)

            # Build final solve prompt with lemmas (grade-dependent instruction)
            if proven_lemmas:
                # Separate lemmas by grade
                perfect_lemmas = [l for l in proven_lemmas if l.get('grade', 0) == 7]
                partial_lemmas = [l for l in proven_lemmas if 5 <= l.get('grade', 0) < 7]

                materials_parts = []

                # Perfect lemmas (7/7) - can use without proof
                if perfect_lemmas:
                    materials_parts.append(
                        "**Rigorously Proven Lemmas (Grade 7/7):**\n"
                        "These conjectures have been rigorously proven. You may use them as Lemmas without further proof.\n"
                    )
                    for i, lemma in enumerate(perfect_lemmas, 1):
                        materials_parts.append(
                            f"\n**Lemma {i}:**\n{lemma['conjecture']}\n\n**Proof:**\n{lemma['proof']}\n"
                        )

                # Partial lemmas (5-6) - reference only
                if partial_lemmas:
                    materials_parts.append(
                        "\n**Conjectures with Partial Proofs (Grade 5-6):**\n"
                        "The following conjectures have partial proofs. Use them as reference material.\n"
                    )
                    for i, lemma in enumerate(partial_lemmas, 1):
                        materials_parts.append(
                            f"\n**Conjecture {i}:**\n{lemma['conjecture']}\n\n**Proof Attempt:**\n{lemma['proof']}\n"
                        )

                additional_materials = "".join(materials_parts) if materials_parts else ""
            else:
                additional_materials = ""

            # Add highest scoring previous solution and its feedback
            if previous_solutions and previous_grades:
                # Find the best previous solution
                best_idx = previous_grades.index(max(previous_grades))
                best_solution = previous_solutions[best_idx]
                best_feedback = previous_feedbacks[best_idx] if best_idx < len(previous_feedbacks) else ""
                best_grade = previous_grades[best_idx]
                
                if additional_materials:
                    additional_materials += "\n\n"
                
                additional_materials += (
                    f"**Highest Scoring Previous Solution (Grade {best_grade}/7):**\n"
                    f"The following is the best solution from all previous attempts, along with its grader feedback.\n"
                    f"Use this as reference, but you should aim to improve upon it.\n\n"
                    f"**Previous Solution:**\n{best_solution}\n\n"
                    f"**Grader Feedback:**\n{best_feedback}\n"
                )
                
                log_print(f"\nIncluding best previous solution (grade {best_grade}/7) in Additional Materials")

            if not additional_materials:
                additional_materials = "None"

            # Construct final prompt
            solve_prompt = f"""**The Problem:**
{problem}

**Additional Materials:**
{additional_materials}

Please solve the problem above."""

            def final_solve_single(solver_idx: int) -> Tuple[int, Any, str]:
                """Single final solver task for parallel execution"""
                try:
                    log_print(f"\n[Final Solver {solver_idx+1}] Starting...")

                    chat = client.chats.create(model=model_id, config=gen_config)
                    response = chat.send_message(solve_prompt)

                    self._log_api_call(
                        step_name=f"Step 10 - Final Solver {solver_idx+1}",
                        role="solver",
                        prompt=solve_prompt,
                        response=response
                    )

                    solution = response.text

                    # Apply Rule 1 (Answer-Processor) immediately after final solving
                    solution = self.apply_answer_processor_rule1(chat, solution)

                    log_print(f"[Final Solver {solver_idx+1}] ✓ Generated and refined ({len(solution)} chars)")
                    return (solver_idx, chat, solution)
                except Exception as e:
                    log_print(f"[Final Solver {solver_idx+1}] ✗ Error: {e}")
                    return (solver_idx, None, "")

            # Execute final solvers in parallel
            log_print(f"\nLaunching {self.num_final_parallel_solvers} final solvers in parallel...")
            results = [None] * self.num_final_parallel_solvers

            with ThreadPoolExecutor(max_workers=self.num_final_parallel_solvers) as executor:
                futures = {
                    executor.submit(final_solve_single, i): i
                    for i in range(self.num_final_parallel_solvers)
                }

                for future in as_completed(futures):
                    idx, chat, solution = future.result()
                    results[idx] = (chat, solution)

            # Collect results in order
            sessions = []
            solutions = []
            for i, (chat, solution) in enumerate(results):
                sessions.append(chat)
                solutions.append(solution if solution else "")

            return sessions, solutions

        except Exception as e:
            log_print(f"✗ Final parallel solve failed: {e}")
            return [], []

    def _get_gemini_api_key(self) -> Optional[str]:
        """Get Gemini API key from environment or file"""
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            return api_key

        possible_paths = [
            "gemini.key",
            "gemini_key.txt",
            "../gemini.key",
            "../gemini_key.txt",
            "../../gemini.key",
            "../../gemini_key.txt",
        ]
        for api_key_file in possible_paths:
            try:
                with open(api_key_file, "r") as f:
                    api_key = f.read().strip()
                    if api_key:
                        return api_key
            except FileNotFoundError:
                continue

        return None

    def _get_genai_model_config(
        self, role: str, system_instruction: str = None
    ) -> Tuple[str, "types.GenerateContentConfig"]:
        """Get model name and configuration for a role"""
        if not HAS_GENAI_SDK:
            return "gemini-3-pro-preview", None

        role_config = self.config_manager.roles.get(role, {})
        model_name = role_config.get("model", "gemini-3-pro")

        model_def = self.config_manager.models.get(model_name, {})
        model_id = model_def.get("gemini_model", model_name)

        params = model_def.get("default_params", {}).copy()
        params.update(role_config.get("params", {}))

        config_args = {
            "temperature": params.get("temperature", 0.4),
            "max_output_tokens": params.get("max_tokens", 65536),
        }

        if system_instruction:
            config_args["system_instruction"] = system_instruction

        # Handle thinking config (ThinkingConfig only accepts thinking_budget, not thinking_level)
        thinking_budget = params.get("thinking_budget")

        if thinking_budget:
            config_args["thinking_config"] = types.ThinkingConfig(
                thinking_budget=thinking_budget
            )

        return model_id, types.GenerateContentConfig(**config_args)

    def _log_api_call(self, step_name: str, role: str, prompt: str, response, call_type: str = "generate"):
        """Log API call details to console and JSONL file (thread-safe)"""
        with self._api_call_lock:
            self._api_call_count += 1
            call_number = self._api_call_count

        log_print(f"\n{'='*70}")
        log_print(f"API CALL #{call_number} [{step_name}] - {role}")
        log_print(f"{'='*70}")

        # Log brief summary
        log_print(f"Prompt: {len(prompt)} chars")
        response_text = response.text if response.text else ""
        log_print(f"Response: {len(response_text)} chars")

        usage = None
        if hasattr(response, 'usage_metadata') and response.usage_metadata:
            usage = response.usage_metadata
            log_print(f"\n Token Usage:")
            log_print(f"  Prompt tokens:      {usage.prompt_token_count}")
            log_print(f"  Output tokens:      {usage.candidates_token_count}")
            log_print(f"  Thinking tokens:    {getattr(usage, 'thoughts_token_count', 'N/A')}")
            log_print(f"  Total tokens:       {usage.total_token_count}")
            log_print(f"  Cached tokens:      {usage.cached_content_token_count if usage.cached_content_token_count else 0}")

        # Get model info
        role_config = self.config_manager.roles.get(role, {})
        model_name = role_config.get("model", "gemini-3-pro")
        params = role_config.get("params", {})

        # Build JSON entry and log via centralized logger
        json_entry = {
            "provider": "genai",
            "model": model_name,
            "role": role,
            "step_name": step_name,
            "call_number": call_number,
            "call_type": call_type,
            "request": {
                "prompt": prompt,
                "prompt_length": len(prompt),
                "generation_config": params
            },
            "success": True,
            "response": {
                "text": response_text,
                "text_length": len(response_text)
            }
        }

        # Add usage metadata if available
        if usage:
            json_entry["response"]["usage"] = {
                "promptTokenCount": usage.prompt_token_count,
                "candidatesTokenCount": usage.candidates_token_count,
                "thoughtsTokenCount": getattr(usage, 'thoughts_token_count', None),
                "totalTokenCount": usage.total_token_count,
                "cachedContentTokenCount": usage.cached_content_token_count if usage.cached_content_token_count else 0
            }

        # Use centralized logger (writes immediately, thread-safe)
        api_log_event(json_entry)

        log_print("-"*80 + "\n")

    def _extract_feedback_for_injection(self, feedback: str) -> str:
        """Extract relevant parts of grader feedback for solver injection.

        Based on feedback_mode config:
        - "full": Return entire grader response (default, backward compatible)
        - "areas_only": Only Areas for Improvement section
        - "areas_and_scaffolding": Areas for Improvement + Scaffolding Questions

        Args:
            feedback: Full grader response text

        Returns:
            Extracted feedback based on mode, or full feedback as fallback
        """
        mode = self.config_manager.execution.get("feedback_mode", "full")

        if mode == "full" or not feedback:
            return feedback

        parts = []

        # Extract Areas for Improvement (case-insensitive, flexible formatting)
        # Matches: **Areas for Improvement:** or ### Areas for Improvement or Areas for Improvement:
        areas_patterns = [
            r'\*\*\s*Areas\s+for\s+Improvement\s*:?\s*\*\*\s*(.*?)(?=\*\*\s*Scaffolding|\*\*\s*Final\s+Grade|#+\s*Scaffolding|#+\s*Final|$)',
            r'#+\s*Areas\s+for\s+Improvement\s*:?\s*(.*?)(?=\*\*\s*Scaffolding|\*\*\s*Final\s+Grade|#+\s*Scaffolding|#+\s*Final|$)',
            r'Areas\s+for\s+Improvement\s*:\s*(.*?)(?=Scaffolding\s+Questions|Final\s+Grade|$)',
        ]

        areas_match = None
        for pattern in areas_patterns:
            areas_match = re.search(pattern, feedback, re.DOTALL | re.IGNORECASE)
            if areas_match:
                break

        if areas_match:
            areas_content = areas_match.group(1).strip()
            parts.append(f"**Areas for Improvement:**\n{areas_content}")
            log_print(f"  [Feedback Extraction] Extracted Areas for Improvement ({len(areas_content)} chars)")

        # Extract Scaffolding Questions if mode includes it (case-insensitive, flexible formatting)
        if mode == "areas_and_scaffolding":
            scaffolding_patterns = [
                r'\*\*\s*Scaffolding\s+Questions\s*:?\s*\*\*\s*(.*?)(?=\*\*\s*Final\s+Grade|#+\s*Final|$)',
                r'#+\s*Scaffolding\s+Questions\s*:?\s*(.*?)(?=\*\*\s*Final\s+Grade|#+\s*Final|$)',
                r'Scaffolding\s+Questions\s*:\s*(.*?)(?=Final\s+Grade|$)',
            ]

            scaffolding_match = None
            for pattern in scaffolding_patterns:
                scaffolding_match = re.search(pattern, feedback, re.DOTALL | re.IGNORECASE)
                if scaffolding_match:
                    break

            if scaffolding_match:
                scaffolding_content = scaffolding_match.group(1).strip()
                parts.append(f"\n**Scaffolding Questions:**\n{scaffolding_content}")
                log_print(f"  [Feedback Extraction] Extracted Scaffolding Questions ({len(scaffolding_content)} chars)")

        if parts:
            extracted = "\n".join(parts)
            log_print(f"  [Feedback Extraction] Mode: {mode}, Original: {len(feedback)} chars -> Extracted: {len(extracted)} chars")
            return extracted
        else:
            # Fallback to full feedback if extraction failed
            log_print(f"  [Feedback Extraction] Could not extract sections, using full feedback")
            return feedback

    def _extract_grade(self, text: str) -> int:
        """Extract numerical grade from grading output.

        Handles various LLM output formats:
        - "Final Grade: 7/7" or "Final Grade: 7 / 7"
        - "Final Grade:\n**7 / 7**" (newline between label and score)
        - "**7/7**" or "**7 / 7**"
        - Score on its own line after "Final Grade:" label
        """
        if not text:
            return 0

        # Patterns ordered from most specific to least specific
        # Use [\s\n]* to allow newlines between label and score
        patterns = [
            # "Final Grade:" followed by bold score (possibly on next line, tolerate inner spaces)
            r'Final\s+Grade:[\s\n]*\*\*\s*(\d+)\s*/\s*7\s*\*\*',
            # "Final Grade:" followed by plain score (tolerate spaces)
            r'Final\s+Grade:[\s\n]*\s*(\d+)\s*/\s*7',
            # 'Final:' followed by score (tolerate spaces)
            r'Final:[\s\n]*\s*(\d+)\s*/\s*7',
            # "Grade:" followed by bold score (tolerate spaces)
            r'Grade:[\s\n]*\*\*\s*(\d+)\s*/\s*7\s*\*\*',
            # "Grade:" followed by plain score (tolerate spaces)
            r'Grade:[\s\n]*\s*(\d+)\s*/\s*7',
            # "Score:" followed by score (tolerate spaces)
            r'Score:[\s\n]*\s*(\d+)\s*/\s*7',
            # Standalone bold score (tolerate spaces)
            r'\*\*\s*(\d+)\s*/\s*7\s*\*\*',
            # Fallback: any X/7 pattern (tolerate spaces)
            r'(\d+)\s*/\s*7',
        ]

        for pattern in patterns:
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
            if matches:
                last_match = matches[-1]
                return int(last_match.group(1))

        return 0

    def _extract_final_blueprint(self, raw_solution: str) -> str:
        """Extract 'The Final Blueprint' section from solver output.

        The solver produces output in this format:
        - Part 1: The Process Log (dialectic dialogue, rounds, etc.)
        - Part 2: The Final Synthesis
          - The Architect's Log (Hemingway Style)
          - The Final Blueprint (Reviewer-Ready) <-- We want this

        Returns:
            The clean proof text from "The Final Blueprint" section.
            Falls back to the full solution if pattern not found.
        """
        if not raw_solution:
            log_print(f"  ⚠ Empty raw_solution passed to _extract_final_blueprint")
            return ""

        # Try multiple patterns to find the Final Blueprint section
        # The Final Blueprint is at the END of the solver output, so we extract everything after the header
        patterns = [
            # Pattern 1: "**The Final Blueprint**" or "**Final Blueprint (Reviewer-Ready)**"
            r'\*\*(?:The\s+)?Final\s+Blueprint[^*]*\*\*[:\s]*\n+(.*)',
            # Pattern 2: "### Final Blueprint" or "## The Final Blueprint"
            r'#+\s*(?:The\s+)?Final\s+Blueprint[^:\n]*:?\s*\n+(.*)',
            # Pattern 3: "Final Blueprint:" as plain text header
            r'(?:The\s+)?Final\s+Blueprint\s*(?:\([^)]*\))?\s*:?\s*\n+(.*)',
        ]

        for pattern in patterns:
            match = re.search(pattern, raw_solution, re.IGNORECASE | re.DOTALL)
            if match:
                blueprint = match.group(1).strip()
                if blueprint:
                    log_print(f"  ✓ Extracted Final Blueprint ({len(blueprint)} chars from {len(raw_solution)} chars)")
                    return blueprint

        # Fallback: return full solution if no Final Blueprint found
        log_print(f"  ⚠ No Final Blueprint section found, using full solution ({len(raw_solution)} chars)")
        return raw_solution

    def _parse_conjecture_extraction(self, text: str) -> Optional[Dict[str, Any]]:
        """Parse conjecture extraction output with structured conjecture identification.

        Expected format from LLM:
        **1. List of Conjecture(s)**
        **Conjecture 1 (Title):**
        [Full conjecture text...]

        **Conjecture 2 (Title):**
        [Full conjecture text...]

        **2. Negation of Conjectures**
        **Negation of Conjecture 1:**
        [Full negation text...]

        **3. Rigorous Proof**
        [Proof text...]
        """
        result = {"conjectures": [], "negations": [], "proof": ""}

        # Extract the conjecture section
        conj_section = re.search(
            r'(?:\*\*)?1\.\s*List of Conjecture\(s\)(?:\*\*)?\s*(.*?)(?=(?:\*\*)?2\.\s*Negation|Negation of Conjecture|Rigorous Proof|$)',
            text, re.DOTALL | re.IGNORECASE
        )

        if conj_section:
            conj_text = conj_section.group(1)

            # Parse individual conjectures by looking for "Conjecture N" patterns
            # This handles formats like:
            # - **Conjecture 1 (Title):**
            # - **Conjecture 1:**
            # - Conjecture 1:
            conj_pattern = r'\*?\*?Conjecture\s+(\d+)\s*(?:\([^)]*\))?\s*:?\*?\*?\s*(.*?)(?=\*?\*?Conjecture\s+\d+|$)'
            conj_matches = re.findall(conj_pattern, conj_text, re.DOTALL | re.IGNORECASE)

            if conj_matches:
                # Found numbered conjectures
                for num, content in conj_matches:
                    content = content.strip()
                    if content and len(content) > 30:  # Meaningful content threshold
                        result["conjectures"].append(content)
            else:
                # Fallback: try to find conjectures as paragraphs (for simpler outputs)
                # Split by double newlines and filter
                paragraphs = re.split(r'\n\s*\n', conj_text)
                for para in paragraphs:
                    para = para.strip()
                    # Skip headers and short lines
                    if para and len(para) > 50 and not para.startswith('**') and not para.startswith('#'):
                        result["conjectures"].append(para)

        # Extract negations section
        neg_section = re.search(
            r'(?:\*\*)?(?:2\.\s*)?Negation of Conjecture(?:s)?(?:\*\*)?\s*(.*?)(?=(?:\*\*)?3\.\s*Rigorous Proof|Rigorous Proof|$)',
            text, re.DOTALL | re.IGNORECASE
        )

        if neg_section:
            neg_text = neg_section.group(1)

            # Parse individual negations by looking for "Negation of Conjecture N" patterns
            neg_pattern = r'\*?\*?Negation of Conjecture\s+(\d+)\s*:?\*?\*?\s*(.*?)(?=\*?\*?Negation of Conjecture\s+\d+|$)'
            neg_matches = re.findall(neg_pattern, neg_text, re.DOTALL | re.IGNORECASE)

            if neg_matches:
                for num, content in neg_matches:
                    content = content.strip()
                    if content and len(content) > 30:
                        result["negations"].append(content)
            else:
                # Fallback: same paragraph-based parsing
                paragraphs = re.split(r'\n\s*\n', neg_text)
                for para in paragraphs:
                    para = para.strip()
                    if para and len(para) > 50 and not para.startswith('**') and not para.startswith('#'):
                        result["negations"].append(para)

        # Extract proof
        proof_section = re.search(
            r'(?:\*\*)?(?:3\.\s*)?Rigorous Proof(?:\*\*)?\s*:?\s*(.*)',
            text, re.DOTALL | re.IGNORECASE
        )
        if proof_section:
            result["proof"] = proof_section.group(1).strip()

        # Log parsing results for debugging
        log_print(f"  Parsed {len(result['conjectures'])} conjectures, {len(result['negations'])} negations")

        if result["conjectures"]:
            return result
        return None

    def _parse_conjectures_with_llm(self, raw_text: str) -> Optional[Dict[str, Any]]:
        """Use LLM (conjecture_parser role) to extract structured conjectures from raw text.

        This is more reliable than regex-based parsing for complex outputs.
        Uses a lightweight Flash model for speed.

        Args:
            raw_text: The raw output from conjecture extractor

        Returns:
            Dict with "conjectures", "negations", and "proof" keys, or None on failure
        """
        log_print("  Using LLM parser for conjecture extraction...")

        if not HAS_GENAI_SDK:
            log_print("  ✗ google-genai SDK not installed, falling back to regex")
            return None

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("  ✗ GEMINI_API_KEY not found, falling back to regex")
            return None

        try:
            # Use persistent client to prevent garbage collection
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Get system prompt for conjecture_parser
            system_prompt = self.config_manager.get_role_prompt("conjecture_parser", "system_prompt")

            # Get model and config
            model_id, gen_config = self._get_genai_model_config("conjecture_parser", system_prompt)

            # Build the parsing prompt
            parse_prompt = f"""Parse the following conjecture extraction output and return structured JSON:

---BEGIN DOCUMENT---
{raw_text}
---END DOCUMENT---

Return a JSON object with "conjectures", "negations", and "proof" arrays/strings."""

            # Create chat session and send
            chat = client.chats.create(model=model_id, config=gen_config)
            response = chat.send_message(parse_prompt)

            self._log_api_call(
                step_name="Step 6 - LLM Conjecture Parser",
                role="conjecture_parser",
                prompt=parse_prompt[:500] + "...[truncated]",  # Log truncated prompt
                response=response
            )

            result_text = response.text if response.text else ""

            # Extract JSON from response
            parsed = self._extract_json_from_response(result_text)

            if parsed and "conjectures" in parsed:
                conjectures = parsed.get("conjectures", [])
                negations = parsed.get("negations", [])
                proof = parsed.get("proof", "")

                log_print(f"  ✓ LLM parser extracted {len(conjectures)} conjectures, {len(negations)} negations")

                return {
                    "conjectures": conjectures,
                    "negations": negations,
                    "proof": proof
                }
            else:
                log_print("  ✗ LLM parser returned invalid format")
                return None

        except Exception as e:
            log_print(f"  ✗ LLM parser failed: {e}")
            import traceback
            traceback.print_exc()
            return None

    def _extract_json_from_response(self, text: str) -> Dict[str, str]:
        """Extract JSON from parser response, handling LaTeX escape issues."""
        # Look for JSON block
        json_match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
        json_str = json_match.group(1) if json_match else text
        
        # If we found a ```json block, try to extract complete JSON by matching braces
        # (The regex might stop early if there are ``` markers in the content)
        if json_match:
            json_start_pos = json_match.start() + len('```json')
            # Try to find the complete JSON object by matching braces
            remaining = text[json_start_pos:]
            brace_count = 0
            in_string = False
            escape_next = False
            json_end_pos = -1
            
            for i, char in enumerate(remaining):
                if escape_next:
                    escape_next = False
                    continue
                if char == '\\':
                    escape_next = True
                    continue
                if char == '"' and not escape_next:
                    in_string = not in_string
                if not in_string:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            json_end_pos = i + 1
                            break
            
            if json_end_pos > 0:
                # Extract the complete JSON
                complete_json = remaining[:json_end_pos].strip()
                # Remove any trailing ``` markers
                complete_json = re.sub(r'\s*```\s*$', '', complete_json)
                json_str = complete_json

        def fix_latex_escapes(s):
            """Fix invalid JSON escape sequences common in LaTeX.

            LaTeX uses backslash-brace, backslash-bracket etc. which are invalid JSON escapes.
            Valid JSON escapes are: backslash + one of: " \\ / b f n r t uXXXX
            """
            # Replace \{ with \\{ (and similar) but only if not already escaped
            # Match a single backslash followed by characters that aren't valid JSON escapes
            # Valid JSON escape chars after backslash: " \ / b f n r t u
            result = re.sub(
                r'(?<!\\)\\([^"\\/bfnrtu])',
                r'\\\\\1',
                s
            )
            return result

        json_str = fix_latex_escapes(json_str)

        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            log_print(f"  Warning: Could not parse JSON: {e}")
            # Try one more fix: sometimes there are triple backslashes
            json_str = re.sub(r'\\\\\\([^"\\/bfnrtu])', r'\\\\\1', json_str)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                log_print("  Warning: JSON parsing failed after fixes")
                return {}

    def _get_best_solution(self, solutions: List[str], grades: List[int]) -> str:
        """Get solution with highest grade"""
        if not solutions or not grades:
            return ""

        max_idx = grades.index(max(grades))
        return solutions[max_idx]

    def _get_top_solutions(
        self,
        solutions: List[str],
        grades: List[int],
        feedbacks: Optional[List[str]],
        n: int,
    ) -> Tuple[List[str], List[str]]:
        """Get top N solutions by grade"""
        # Sort by grade (descending)
        sorted_indices = sorted(range(len(grades)), key=lambda i: grades[i], reverse=True)
        top_indices = sorted_indices[:n]

        top_solutions = [solutions[i] for i in top_indices]
        if feedbacks and len(feedbacks) == len(solutions):
            top_feedbacks = [feedbacks[i] for i in top_indices]
        else:
            # If feedbacks are unavailable/misaligned, keep behavior deterministic
            top_feedbacks = ["" for _ in top_indices]

        return top_solutions, top_feedbacks

    def _format_proven_lemmas(self, proven_lemmas: List[Dict[str, str]]) -> str:
        """Format proven lemmas for final solving"""
        if not proven_lemmas:
            return "None"

        formatted = []
        for i, lemma in enumerate(proven_lemmas, 1):
            formatted.append(f"**Lemma {i}:**\n{lemma['conjecture']}\n\n**Proof:**\n{lemma['proof']}\n")

        return "\n".join(formatted)

    def aggregate_feedback(self, conjecture_feedback_map: Dict[str, str]) -> str:
        """
        Aggregate feedback using Markdown structure (Implementation Note B)

        Args:
            conjecture_feedback_map: dict { "C1": "Feedback text...", "C2": "..." }

        Returns:
            Markdown-formatted consolidated feedback
        """
        report = ["# Consolidated Feedback Report\n"]

        for conj_id, feedback in conjecture_feedback_map.items():
            section = f"## Feedback for Conjecture {conj_id}\n{feedback}\n\n---\n"
            report.append(section)

        return "\n".join(report)
