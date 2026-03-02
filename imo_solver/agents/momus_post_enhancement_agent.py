"""
Momus Post-Enhancement Agent

Refines near-perfect (6/7) solutions to achieve perfect scores (7/7).

Pipeline:
1. Collect 6/7 solutions + grader feedback
2. Parallel proof rewriting (2 rewriters) with conjecture extraction
3. Verify all extracted conjectures (prove/disprove)
4. Filter validated rewritten proofs (keep only if all conjectures proven)
5. Enhanced final solving with proven lemmas + disproven claims + validated rewrites

Design Philosophy:
- Target specific identified gaps rather than regenerating from scratch
- Explicitly prove missing intermediate claims
- Provide both positive (proven lemmas) and negative (disproven claims) information
- Only use validated approaches (all dependencies proven)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

from .momus_core_agent import MomusCoreAgent, SolutionStatus
from ..utils.logger import log_print
from ..utils.config_utils import get_template_required

# Try to import genai SDK (same as core agent)
try:
    from google import genai
    from google.genai import types
    HAS_GENAI_SDK = True
except ImportError:
    HAS_GENAI_SDK = False
    genai = None
    types = None


@dataclass
class RewriterOutput:
    """Output from a proof rewriter"""
    rewriter_id: str  # "rewriter_A" | "rewriter_B"
    approach: str  # "conjecture-based" | "direct-rewrite"
    identified_gaps: List[str]
    conjectures: List[Dict[str, str]]  # [{"statement": ..., "negation": ...}, ...]
    rewritten_proof: str
    raw_output: str


@dataclass
class ConjectureVerification:
    """Result of verifying a conjecture"""
    conjecture_id: str
    statement: str
    negation: str
    proof_of_conjecture: str
    proof_of_negation: str
    grade_conjecture: int
    grade_negation: int
    classification: str  # "proven" | "disproven" | "conflicting" | "unresolved"
    rewriter_source: str


class MomusPostEnhancementAgent(MomusCoreAgent):
    """
    Post-enhancement agent for refining 6/7 solutions to 7/7.

    Inherits from MomusCoreAgent to reuse:
    - Solver/grader infrastructure
    - Rule 1 (Answer Processor)
    - Gemini client management
    """

    def __init__(
        self,
        config_path: str = "imo_solver/config/momus_config.yaml",
        prompts_path: str = "imo_solver/prompts/momus_prompts.yaml",
        base_models_path: Optional[str] = None,
        log_file: str = "logs/momus_post_enhancement.log",
    ):
        """
        Initialize post-enhancement agent.

        Reuses Momus roles and prompts directly:
        - conjecture_extractor: For Step 2 (proof rewriting with gaps)
        - solver: For Step 3 (proving conjectures) and Step 5 (final solving)
        - grader: For grading all proofs
        - answer_processor: For Rule 1 verification (inherited)
        - conjecture_parser: For parsing conjecture extractor output
        """
        super().__init__(
            config_path=config_path,
            prompts_path=prompts_path,
            base_models_path=base_models_path,
            log_file=log_file,
        )

        # Post-enhancement specific settings
        self.num_rewriters = self.config_manager.execution.get("num_rewriters", 2)
        self.min_solutions_at_target = self.config_manager.execution.get("min_solutions_at_target", 3)
        self.target_grade = self.config_manager.execution.get("target_grade", 6)
        self.conjecture_proven_threshold = self.config_manager.execution.get("conjecture_proven_threshold", 6)
        self.num_final_solvers = self.config_manager.execution.get("num_final_solvers", 3)

        log_print(f"\n{'='*80}")
        log_print("MOMUS POST-ENHANCEMENT AGENT INITIALIZED")
        log_print(f"{'='*80}")
        log_print(f"Trigger: >={self.min_solutions_at_target} solutions at {self.target_grade}/7")
        log_print(f"Rewriters: {self.num_rewriters}")
        log_print(f"Final solvers: {self.num_final_solvers}")

    def should_trigger(
        self, problem: str, candidate_solution: str
    ) -> Tuple[bool, List[str]]:
        """
        Check if post-enhancement should be triggered by doing 3 independent gradings.

        Args:
            problem: The problem statement
            candidate_solution: The candidate solution to verify

        Returns:
            (should_trigger, feedbacks) tuple
            - should_trigger: True if NOT all grades are 7/7 (solution needs improvement)
            - feedbacks: List of 3 grader feedbacks (empty if not triggered)
        """
        log_print(f"\n{'='*80}")
        log_print(f"POST-ENHANCEMENT ELIGIBILITY CHECK")
        log_print(f"{'='*80}")
        log_print(f"Running {self.min_solutions_at_target} independent gradings...")

        grades = []
        feedbacks = []

        for i in range(self.min_solutions_at_target):
            log_print(f"\n[Independent Grading {i+1}/{self.min_solutions_at_target}]")
            grade, feedback = self._grade_single_with_feedback(
                problem, candidate_solution, materials="",
                step_name=f"Independent Grading {i+1}"
            )
            grades.append(grade)
            feedbacks.append(feedback)
            log_print(f"  Grade: {grade}/7")

        # Trigger if NOT all grades are 7/7 (solution can potentially be improved)
        all_perfect = all(g == 7 for g in grades)

        if not all_perfect:
            log_print(f"\n{'='*80}")
            log_print(f"✓ POST-ENHANCEMENT TRIGGERED")
            log_print(f"{'='*80}")
            log_print(f"Grades: {grades}")
            log_print(f"Not all grades are 7/7 - solution can potentially be improved")
            log_print(f"Proceeding with enhancement pipeline...")
            return (True, feedbacks)
        else:
            log_print(f"\n{'='*80}")
            log_print(f"✗ POST-ENHANCEMENT NOT TRIGGERED")
            log_print(f"{'='*80}")
            log_print(f"All {self.min_solutions_at_target} independent grades = 7/7")
            log_print(f"Solution is already perfect - no enhancement needed")
            return (False, [])

    def run_enhancement(
        self,
        problem: str,
        candidate_solution: str,
        feedbacks: Optional[List[str]] = None,
    ) -> Tuple[SolutionStatus, str]:
        """
        Run the full post-enhancement pipeline on a single candidate solution.

        Args:
            problem: Original problem statement
            candidate_solution: Single solution to enhance (should be 6/7 quality)
            feedbacks: Optional pre-computed feedbacks from should_trigger()
                      If None, will run independent grading first

        Returns:
            (status, best_solution) tuple
        """
        # Step 0: Verify eligibility if feedbacks not provided
        if feedbacks is None:
            should_enhance, feedbacks = self.should_trigger(problem, candidate_solution)
            if not should_enhance:
                log_print("✗ Solution not eligible for post-enhancement")
                return (SolutionStatus.UNSOLVED, candidate_solution)

        # Step 1: Use the single candidate solution as material
        # (treating it as if we have multiple 6/7 solutions for backward compatibility)
        target_solutions = [candidate_solution]
        target_feedbacks = feedbacks

        # Step 2: Parallel proof rewriting
        rewriter_outputs = self._step2_parallel_rewriting(
            problem, target_solutions, target_feedbacks
        )

        if not rewriter_outputs:
            log_print("✗ Step 2 failed: No rewriter outputs")
            return (SolutionStatus.UNSOLVED, "")

        # Step 3: Conjecture verification
        verifications = self._step3_verify_conjectures(problem, rewriter_outputs)

        # Step 4: Filter validated rewrites
        validated_rewrites = self._step4_filter_rewrites(rewriter_outputs, verifications)

        # Step 5: Enhanced final solving
        final_solution, final_grade = self._step5_enhanced_solving(
            problem, verifications, validated_rewrites
        )

        if final_grade == 7:
            log_print("\n✓ POST-ENHANCEMENT SUCCESS: Achieved 7/7")
            return (SolutionStatus.SOLVED, final_solution)

        if final_grade > self.target_grade:
            log_print(f"\n✓ POST-ENHANCEMENT IMPROVED: {self.target_grade}/7 → {final_grade}/7")
            return (SolutionStatus.UNSOLVED, final_solution)

        log_print(f"\n✗ POST-ENHANCEMENT DID NOT IMPROVE: Still at {final_grade}/7")
        return (SolutionStatus.UNSOLVED, final_solution)

    def _step2_parallel_rewriting(
        self, problem: str, solutions: List[str], feedbacks: List[str]
    ) -> List[RewriterOutput]:
        """
        Step 2: Parallel conjecture extraction (reusing base pipeline conjecture_extractor).

        Launch N extractors in parallel, each analyzes all 6/7 solutions.
        """
        log_print(f"\n{'='*70}")
        log_print(f"STEP 2: PARALLEL CONJECTURE EXTRACTION")
        log_print(f"{'='*70}")

        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return []

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return []

        try:
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Use base pipeline's conjecture_extractor role
            system_prompt = self.config_manager.get_role_prompt("conjecture_extractor", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("conjecture_extractor", system_prompt)

            # Prepare inputs
            solutions_text = "\n\n".join([
                f"=== Solution {i+1} (Grade {self.target_grade}/7) ===\n{sol}"
                for i, sol in enumerate(solutions)
            ])
            feedback_text = "\n\n".join([
                f"=== Feedback for Solution {i+1} ===\n{fb}"
                for i, fb in enumerate(feedbacks)
            ])

            def rewrite_single(rewriter_idx: int) -> Tuple[int, Optional[RewriterOutput]]:
                try:
                    rewriter_id = chr(65 + rewriter_idx)  # A, B, C, ...
                    log_print(f"\n[Rewriter {rewriter_id}] Starting...")

                    chat = client.chats.create(model=model_id, config=gen_config)

                    # Build prompt using base pipeline's conjecture_extraction template
                    extraction_prompt = get_template_required(
                        "conjecture_extraction",
                        self.config_manager,
                        problem=problem,
                        solutions=solutions_text,
                        grader_reports=feedback_text,
                        materials="",  # No additional materials for initial extraction
                    )

                    response = chat.send_message(extraction_prompt)
                    self._log_api_call(
                        step_name=f"Step 2 - Conjecture Extractor {rewriter_id}",
                        role="conjecture_extractor",
                        prompt=extraction_prompt,
                        response=response,
                    )

                    raw_output = response.text
                    if not raw_output:
                        log_print(f"[Rewriter {rewriter_id}] ✗ Empty response")
                        return (rewriter_idx, None)

                    # Parse output
                    parsed = self._parse_rewriter_output(raw_output, f"rewriter_{rewriter_id}")
                    if parsed:
                        num_conj = len(parsed.conjectures)
                        log_print(f"[Rewriter {rewriter_id}] ✓ Parsed: {parsed.approach}, {num_conj} conjectures")
                        return (rewriter_idx, parsed)

                    log_print(f"[Rewriter {rewriter_id}] ✗ Failed to parse output")
                    return (rewriter_idx, None)

                except Exception as e:
                    log_print(f"[Rewriter {chr(65 + rewriter_idx)}] ✗ Error: {e}")
                    import traceback
                    traceback.print_exc()
                    return (rewriter_idx, None)

            log_print(f"\nLaunching {self.num_rewriters} rewriters in parallel...")
            outputs: List[Optional[RewriterOutput]] = [None] * self.num_rewriters

            with ThreadPoolExecutor(max_workers=self.num_rewriters) as executor:
                futures = {
                    executor.submit(rewrite_single, i): i
                    for i in range(self.num_rewriters)
                }
                for future in as_completed(futures):
                    idx, output = future.result()
                    outputs[idx] = output

            valid_outputs = [o for o in outputs if o is not None]
            log_print(f"\nStep 2 complete: {len(valid_outputs)}/{self.num_rewriters} rewriters succeeded")
            return valid_outputs

        except Exception as e:
            log_print(f"✗ Step 2 failed with error: {e}")
            import traceback
            traceback.print_exc()
            return []

    def _parse_conjectures_with_parser(self, text: str) -> Optional[Dict[str, Any]]:
        """Wrapper around inherited _parse_conjectures_with_llm for consistency"""
        return self._parse_conjectures_with_llm(text)

    def _parse_rewriter_output(
        self, text: str, rewriter_id: str
    ) -> Optional[RewriterOutput]:
        """
        Parse base pipeline conjecture extractor output.

        base pipeline format:
        Part 1: The Grading Log (critique process)
        Part 2: Completed Proof with Conjectures
          1. List of Conjecture(s)
          2. Negation of Conjectures
          3. Rigorous Proof
        """
        # Use base pipeline's conjecture_parser to extract structured data
        try:
            parsed_data = self._parse_conjectures_with_parser(text)
            if not parsed_data:
                log_print(f"  ⚠ Failed to parse {rewriter_id} output with conjecture_parser")
                return None

            conjectures_list = parsed_data.get("conjectures", [])
            negations_list = parsed_data.get("negations", [])
            proof = parsed_data.get("proof", "")

            if not proof:
                log_print(f"  ⚠ No proof found in {rewriter_id} output")
                return None

            # Convert to our format
            conjectures = []
            for i, (conj, neg) in enumerate(zip(conjectures_list, negations_list)):
                conjectures.append({
                    "conjecture_num": str(i + 1),
                    "statement": conj,
                    "negation": neg,
                })

            # base pipeline always uses conjecture-based approach
            approach = "conjecture-based" if conjectures else "direct-rewrite"

            return RewriterOutput(
                rewriter_id=rewriter_id,
                approach=approach,
                identified_gaps=[],  # base pipeline doesn't explicitly separate gaps
                conjectures=conjectures,
                rewritten_proof=proof,
                raw_output=text,
            )

        except Exception as e:
            log_print(f"  ✗ Error parsing {rewriter_id} output: {e}")
            import traceback
            traceback.print_exc()
            return None

    def _step3_verify_conjectures(
        self, problem: str, rewriter_outputs: List[RewriterOutput]
    ) -> List[ConjectureVerification]:
        """
        Step 3: Verify all extracted conjectures (prove/disprove).

        For each conjecture C:
        - Solve C
        - Solve ¬C
        - Grade both
        - Classify as proven/disproven/unresolved
        """
        log_print(f"\n{'='*70}")
        log_print(f"STEP 3: CONJECTURE VERIFICATION")
        log_print(f"{'='*70}")

        # Collect all conjectures
        all_conjectures = []
        for output in rewriter_outputs:
            for conj_dict in output.conjectures:
                conj_id = f"{output.rewriter_id}_C{conj_dict['conjecture_num']}"
                all_conjectures.append({
                    "id": conj_id,
                    "statement": conj_dict["statement"],
                    "negation": conj_dict["negation"],
                    "rewriter_source": output.rewriter_id,
                })

        if not all_conjectures:
            log_print("No conjectures to verify (all rewriters used direct rewrites)")
            return []

        log_print(f"Verifying {len(all_conjectures)} conjecture(s)...")

        # Verify each conjecture
        verifications = []
        for conj in all_conjectures:
            log_print(f"\n--- Verifying {conj['id']} ---")

            # Prove C
            proof_C, grade_C = self._solve_and_grade_single_conjecture(
                conj["statement"], f"Prove_{conj['id']}"
            )
            log_print(f"  Prove C: Grade {grade_C}/7")

            # Prove ¬C
            proof_neg_C, grade_neg_C = self._solve_and_grade_single_conjecture(
                conj["negation"], f"Prove_NOT_{conj['id']}"
            )
            log_print(f"  Prove ¬C: Grade {grade_neg_C}/7")

            # Classify
            if grade_C >= self.conjecture_proven_threshold and grade_neg_C >= self.conjecture_proven_threshold:
                classification = "conflicting"  # Momus: Both proven (hallucination)
            elif grade_C >= self.conjecture_proven_threshold and grade_neg_C < self.conjecture_proven_threshold:
                classification = "proven"
            elif grade_neg_C >= self.conjecture_proven_threshold and grade_C < self.conjecture_proven_threshold:
                classification = "disproven"
            else:
                classification = "unresolved"

            log_print(f"  Classification: {classification.upper()}")

            verifications.append(ConjectureVerification(
                conjecture_id=conj["id"],
                statement=conj["statement"],
                negation=conj["negation"],
                proof_of_conjecture=proof_C,
                proof_of_negation=proof_neg_C,
                grade_conjecture=grade_C,
                grade_negation=grade_neg_C,
                classification=classification,
                rewriter_source=conj["rewriter_source"],
            ))

        # Summary
        proven_count = sum(1 for v in verifications if v.classification == "proven")
        disproven_count = sum(1 for v in verifications if v.classification == "disproven")
        conflicting_count = sum(1 for v in verifications if v.classification == "conflicting")
        unresolved_count = sum(1 for v in verifications if v.classification == "unresolved")

        log_print(f"\nStep 3 complete:")
        log_print(f"  Proven: {proven_count}")
        log_print(f"  Disproven: {disproven_count}")
        log_print(f"  Conflicting: {conflicting_count} (Momus: will be included as 'Student's attempted solution')")
        log_print(f"  Unresolved: {unresolved_count}")

        return verifications

    def _step4_filter_rewrites(
        self, rewriter_outputs: List[RewriterOutput], verifications: List[ConjectureVerification]
    ) -> List[RewriterOutput]:
        """
        Step 4: Filter validated rewritten proofs.

        Keep rewrite if:
        - No conjectures (direct rewrite), OR
        - ALL conjectures are PROVEN

        Discard if:
        - ANY conjecture is disproven or unresolved
        """
        log_print(f"\n{'='*70}")
        log_print(f"STEP 4: FILTER VALIDATED REWRITES")
        log_print(f"{'='*70}")

        validated = []

        for output in rewriter_outputs:
            log_print(f"\n[{output.rewriter_id}] Checking validation...")

            if not output.conjectures:
                log_print(f"  ✓ KEEP: Direct rewrite (no conjectures)")
                validated.append(output)
                continue

            # Check all conjectures
            all_proven = True
            for conj_dict in output.conjectures:
                conj_id = f"{output.rewriter_id}_C{conj_dict['conjecture_num']}"
                # Find verification
                verif = next((v for v in verifications if v.conjecture_id == conj_id), None)
                if not verif or verif.classification != "proven":
                    all_proven = False
                    status = verif.classification if verif else "not_found"
                    log_print(f"  Conjecture {conj_dict['conjecture_num']}: {status}")

            if all_proven:
                log_print(f"  ✓ KEEP: All conjectures proven")
                validated.append(output)
            else:
                log_print(f"  ✗ DISCARD: Some conjectures not proven (proof is nonsense)")

        log_print(f"\nStep 4 complete: {len(validated)}/{len(rewriter_outputs)} rewrites validated")
        return validated

    def _solve_single(
        self, problem: str, materials: str, step_name: str
    ) -> str:
        """
        Generate a single solution using the solver role.

        Args:
            problem: Problem statement (or prompt)
            materials: Additional materials
            step_name: Step name for logging

        Returns:
            Solution text (or empty string on failure)
        """
        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return ""

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return ""

        try:
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Get solver config
            solver_sys = self.config_manager.get_role_prompt("solver", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("solver", solver_sys)

            # Build solve prompt
            solve_prompt = get_template_required(
                "solve_instruction",
                self.config_manager,
                problem=problem,
                materials=materials if materials else "None",
            )

            # Solve
            solver_chat = client.chats.create(model=model_id, config=gen_config)
            response = solver_chat.send_message(solve_prompt)

            self._log_api_call(
                step_name=step_name,
                role="solver",
                prompt=solve_prompt,
                response=response,
            )

            proof = response.text

            # Apply Rule 1 (Answer Processor)
            proof = self.apply_answer_processor_rule1(solver_chat, proof)

            if not proof:
                log_print(f"  ✗ Empty proof after Rule 1")
                return ""

            # Extract Final Blueprint
            clean_proof = self._extract_final_blueprint(proof)

            if not clean_proof:
                log_print(f"  ✗ Failed to extract Final Blueprint")
                return ""

            return clean_proof

        except Exception as e:
            log_print(f"  ✗ Error in solving: {e}")
            import traceback
            traceback.print_exc()
            return ""

    def _grade_solution(
        self, problem: str, solution: str, step_name: str
    ) -> int:
        """
        Grade a solution and return the grade (0-7).

        Args:
            problem: Problem statement
            solution: Solution to grade
            step_name: Step name for logging

        Returns:
            Grade (0-7)
        """
        if not HAS_GENAI_SDK:
            log_print("✗ google-genai SDK not installed")
            return 0

        api_key = self._get_gemini_api_key()
        if not api_key:
            log_print("✗ GEMINI_API_KEY not found")
            return 0

        try:
            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            # Get grader config
            grader_sys = self.config_manager.get_role_prompt("grader", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("grader", grader_sys)

            # Build grade prompt
            grade_prompt = get_template_required(
                "grade_instruction",
                self.config_manager,
                problem=problem,
                solution=solution,
                materials="None",
            )

            # Grade
            grader_chat = client.chats.create(model=model_id, config=gen_config)
            response = grader_chat.send_message(grade_prompt)

            self._log_api_call(
                step_name=step_name,
                role="grader",
                prompt=grade_prompt,
                response=response,
            )

            # Extract grade
            grade = self._extract_grade(response.text)
            return grade

        except Exception as e:
            log_print(f"  ✗ Error in grading: {e}")
            import traceback
            traceback.print_exc()
            return 0

    def _solve_and_grade_single_conjecture(
        self, conjecture: str, label: str
    ) -> Tuple[str, int]:
        """
        Solve and grade a single conjecture using core pipeline's infrastructure.

        Returns:
            (proof, grade) tuple
        """
        # Use inherited method from MomusCoreAgent
        # This method already does both solving and grading
        return super()._solve_and_grade_single_conjecture(conjecture, label)

    def _step5_enhanced_solving(
        self,
        problem: str,
        verifications: List[ConjectureVerification],
        validated_rewrites: List[RewriterOutput],
    ) -> Tuple[str, int]:
        """
        Step 5: Enhanced final solving with proven lemmas + disproven claims.

        Provides solvers with:
        - Proven lemmas (conjectures with grade >= threshold)
        - Disproven claims (negations proven, showing false paths)
        - Validated rewritten proofs (reference approaches)
        """
        log_print(f"\n{'='*70}")
        log_print(f"STEP 5: ENHANCED FINAL SOLVING")
        log_print(f"{'='*70}")

        # Build materials sections
        proven_lemmas_section = self._build_proven_lemmas_section(verifications)
        disproven_claims_section = self._build_disproven_claims_section(verifications)
        conflicting_attempts_section = self._build_conflicting_attempts_section(verifications)
        validated_rewrites_section = self._build_validated_rewrites_section(validated_rewrites)

        # Build full prompt
        final_prompt = get_template_required(
            "post_enhancement_final_solve",
            self.config_manager,
            problem=problem,
            proven_lemmas_section=proven_lemmas_section,
            disproven_claims_section=disproven_claims_section,
            validated_rewrites_section=validated_rewrites_section,
        )
        
        # Momus: Append conflicting attempts section if present
        if conflicting_attempts_section:
            final_prompt += "\n\n" + conflicting_attempts_section

        log_print(f"\nMaterials summary:")
        log_print(f"  Proven lemmas: {len([v for v in verifications if v.classification == 'proven'])}")
        log_print(f"  Disproven claims: {len([v for v in verifications if v.classification == 'disproven'])}")
        log_print(f"  Conflicting attempts: {len([v for v in verifications if v.classification == 'conflicting'])}")
        log_print(f"  Validated rewrites: {len(validated_rewrites)}")

        # Solve in parallel
        log_print(f"\nLaunching {self.num_final_solvers} parallel solvers...")

        solutions = []
        grades = []

        def solve_single(idx: int) -> Tuple[int, str, int]:
            try:
                log_print(f"\n[Solver {idx+1}] Starting...")
                solution = self._solve_single(
                    final_prompt, materials="", step_name=f"Step 5 - Final Solver {idx+1}"
                )
                if not solution:
                    log_print(f"[Solver {idx+1}] ✗ No solution")
                    return (idx, "", 0)

                # Grade the solution
                grade = self._grade_solution(
                    problem, solution, step_name=f"Step 5 - Grade Solver {idx+1}"
                )
                log_print(f"[Solver {idx+1}] ✓ Grade: {grade}/7")
                return (idx, solution, grade)

            except Exception as e:
                log_print(f"[Solver {idx+1}] ✗ Error: {e}")
                return (idx, "", 0)

        with ThreadPoolExecutor(max_workers=self.num_final_solvers) as executor:
            futures = [executor.submit(solve_single, i) for i in range(self.num_final_solvers)]
            for future in as_completed(futures):
                _, sol, grade = future.result()
                solutions.append(sol)
                grades.append(grade)

        # Find best solution
        if not grades or max(grades) == 0:
            log_print("\n✗ Step 5 failed: No valid solutions")
            return ("", 0)

        best_idx = grades.index(max(grades))
        best_solution = solutions[best_idx]
        best_grade = grades[best_idx]

        log_print(f"\nStep 5 complete: Best grade = {best_grade}/7")
        return (best_solution, best_grade)

    def _grade_single_with_feedback(
        self, problem: str, solution: str, materials: str, step_name: str
    ) -> Tuple[int, str]:
        """
        Grade a solution and return both grade and full feedback.

        Args:
            problem: Problem statement
            solution: Solution to grade
            materials: Additional materials
            step_name: Step name for logging

        Returns:
            (grade, feedback) tuple where feedback is the full grader response
        """
        # Use inherited _grade_with_retries to get full response
        try:
            # Build grade prompt
            grade_prompt = get_template_required(
                "grade_instruction",
                self.config_manager,
                problem=problem,
                solution=solution,
                materials=materials,
            )

            # Get full grader response (not just grade)
            if not HAS_GENAI_SDK:
                log_print("✗ google-genai SDK not installed")
                return (0, "")

            api_key = self._get_gemini_api_key()
            if not api_key:
                log_print("✗ GEMINI_API_KEY not found")
                return (0, "")

            if self._genai_client is None:
                self._genai_client = genai.Client(api_key=api_key)
            client = self._genai_client

            system_prompt = self.config_manager.get_role_prompt("grader", "system_prompt")
            model_id, gen_config = self._get_genai_model_config("grader", system_prompt)

            chat = client.chats.create(model=model_id, config=gen_config)
            response = chat.send_message(grade_prompt)

            self._log_api_call(
                step_name=step_name,
                role="grader",
                prompt=grade_prompt,
                response=response,
            )

            feedback = response.text
            if not feedback:
                log_print(f"  ⚠ Empty grader response")
                return (0, "")

            # Extract grade from feedback
            grade = self._extract_grade(feedback)
            return (grade, feedback)

        except Exception as e:
            log_print(f"  ✗ Error in grading: {e}")
            import traceback
            traceback.print_exc()
            return (0, "")

    def _build_proven_lemmas_section(self, verifications: List[ConjectureVerification]) -> str:
        """Build section with proven lemmas (base pipeline format)"""
        proven = [v for v in verifications if v.classification == "proven"]
        if not proven:
            return ""

        lemma_items = []
        for i, v in enumerate(proven, 1):
            item = get_template_required(
                "proven_lemma_item",
                self.config_manager,
                index=i,
                statement=v.statement,
                proof=v.proof_of_conjecture,
            )
            lemma_items.append(item)

        return get_template_required(
            "proven_lemmas_section_template",
            self.config_manager,
            threshold=self.conjecture_proven_threshold,
            lemmas="\n\n".join(lemma_items),
        )

    def _build_disproven_claims_section(self, verifications: List[ConjectureVerification]) -> str:
        """Build section with disproven claims (negations proven)"""
        disproven = [v for v in verifications if v.classification == "disproven"]
        if not disproven:
            return ""

        claim_items = []
        for i, v in enumerate(disproven, 1):
            item = get_template_required(
                "disproven_claim_item",
                self.config_manager,
                index=i,
                grade=v.grade_negation,
                false_statement=v.statement,
                negation_proof=v.proof_of_negation,
            )
            claim_items.append(item)

        return get_template_required(
            "disproven_claims_section_template",
            self.config_manager,
            disproven_claims="\n\n".join(claim_items),
        )

    def _build_conflicting_attempts_section(self, verifications: List[ConjectureVerification]) -> str:
        """Build section with conflicting attempts (both C and ¬C proven) as 'Student's attempted solution'"""
        conflicting = [v for v in verifications if v.classification == "conflicting"]
        if not conflicting:
            return ""
        
        conflicting_items = []
        conflicting_items.append(
            "**Student's attempted solution:**\n"
            "The following are attempts where both a statement and its negation were proven. "
            "These are not perfect and should be used with caution as reference material only.\n"
        )
        
        for i, v in enumerate(conflicting, 1):
            conflicting_items.append(
                f"\n**Attempted Solution {i}:**\n"
                f"**Statement:**\n{v.statement}\n\n"
                f"**Proof of Statement (Grade {v.grade_conjecture}/7):**\n{v.proof_of_conjecture}\n\n"
                f"**Negation:**\n{v.negation}\n\n"
                f"**Proof of Negation (Grade {v.grade_negation}/7):**\n{v.proof_of_negation}\n"
            )
        
        return "\n\n".join(conflicting_items)

    def _build_validated_rewrites_section(self, validated_rewrites: List[RewriterOutput]) -> str:
        """Build section with validated rewritten proofs"""
        if not validated_rewrites:
            return ""

        rewrite_items = []
        for i, output in enumerate(validated_rewrites, 1):
            item = get_template_required(
                "validated_rewrite_item",
                self.config_manager,
                index=i,
                rewritten_proof=output.rewritten_proof,
            )
            rewrite_items.append(item)

        return get_template_required(
            "validated_rewrites_section_template",
            self.config_manager,
            rewrites="\n\n".join(rewrite_items),
        )
