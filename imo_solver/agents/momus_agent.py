"""
Momus Agent: base pipeline + Integrated Post-Enhancement

Key improvements over base pipeline:
1. Configurable Rule 2 verification count (default: 3 instead of 2)
2. Integrated post-enhancement for near-perfect solutions
3. Automatic fallback enhancement if final solution is not perfect (all N grades = 7/7)

Pipeline:
- Same as base pipeline (Phases 1-3)
- Modified Rule 2: N consecutive 7/7 grades (configurable)
- Post-Enhancement: If final solution doesn't get all 7/7 in N independent grades,
  automatically run enhancement pipeline to improve it
"""

from typing import Optional, Tuple, List
from .momus_base_agent import MomusBaseAgent
from .momus_post_enhancement_agent import MomusPostEnhancementAgent
from .base_agent import SolutionStatus
from ..utils.logger import log_print


class MomusAgent(MomusBaseAgent):
    """
    Momus agent with integrated post-enhancement.

    Inherits base pipeline's full pipeline and adds:
    - Configurable Rule 2 verification count
    - Automatic post-enhancement for imperfect solutions
    """

    def __init__(
        self,
        config_path: str = "imo_solver/config/momus_config.yaml",
        prompts_path: str = "imo_solver/prompts/momus_prompts.yaml",
        base_models_path: Optional[str] = None,
        log_file: Optional[str] = None,
    ):
        """Initialize Momus agent."""
        super().__init__(config_path, prompts_path, base_models_path, log_file)

        # Momus-specific settings
        self.rule2_verification_count = self.config_manager.execution.get(
            "rule2_verification_count", 3
        )
        self.post_enhancement_trigger_count = self.config_manager.execution.get(
            "post_enhancement_trigger_count", 3
        )
        self.enable_post_enhancement = self.config_manager.execution.get(
            "enable_post_enhancement", True
        )
        self.post_enhancement_min_grade = self.config_manager.execution.get(
            "post_enhancement_min_grade", 0
        )

        # Initialize post-enhancement agent (lazy, only if needed)
        self._post_enhancement_agent = None

        log_print("\n" + "="*80)
        log_print("MOMUS AGENT INITIALIZED")
        log_print("="*80)
        log_print(f"Rule 2 verifications: {self.rule2_verification_count} (improved from base pipeline)")
        log_print(f"Post-enhancement enabled: {self.enable_post_enhancement}")
        if self.enable_post_enhancement:
            log_print(f"Post-enhancement trigger: {self.post_enhancement_trigger_count} independent grades")
            log_print(f"Post-enhancement min grade: {self.post_enhancement_min_grade}/7")
        log_print("="*80)

    def run(
        self, problem: str, max_runs: int = 3, **kwargs
    ) -> Tuple[SolutionStatus, Optional[str]]:
        """
        Run Momus pipeline with integrated post-enhancement.

        Args:
            problem: Problem statement
            max_runs: Maximum outer loops (base pipeline pipeline)
            **kwargs: Additional arguments

        Returns:
            (SolutionStatus, solution_text) tuple
        """
        log_print("\n" + "="*80)
        log_print("MOMUS PIPELINE START")
        log_print("="*80)

        # Phase 1-3: Run base pipeline pipeline
        log_print("\n>>> PHASE 1-3: Running base pipeline Base Pipeline")
        status, final_solution = super().run(problem, max_runs, **kwargs)

        # Check if base pipeline produced a solution
        if not final_solution:
            log_print("\n>>> base pipeline pipeline did not produce any solution text")
            return (status, None)

        log_print("\n" + "="*80)
        log_print("base pipeline PIPELINE COMPLETE - CHECKING POST-ENHANCEMENT")
        log_print("="*80)

        # Check if post-enhancement is enabled
        if not self.enable_post_enhancement:
            log_print("Post-enhancement disabled - returning base pipeline result")
            return (status, final_solution)

        # Phase 4: Post-enhancement check and execution
        log_print(f"\n>>> PHASE 4: Post-Enhancement Check")
        log_print(f"Running {self.post_enhancement_trigger_count} independent evaluations...")

        # Check if solution needs enhancement
        should_enhance, original_feedbacks, original_grades = self._check_post_enhancement_trigger(
            problem, final_solution
        )

        if not should_enhance:
            log_print("\n✓ Solution is perfect (all grades 7/7) - no enhancement needed")
            return (status, final_solution)

        # Run post-enhancement
        log_print(f"\n>>> Solution is imperfect - running post-enhancement pipeline")
        enhanced_status, enhanced_solution = self._run_post_enhancement(
            problem, final_solution, original_feedbacks
        )

        # Grade enhanced solution to compare with original
        if enhanced_status == SolutionStatus.SOLVED and enhanced_solution:
            log_print(f"\n>>> Comparing original vs enhanced solution quality")

            # Extract Final Blueprint for grading (consistent with base pipeline internal grading)
            clean_enhanced = self._extract_final_blueprint(enhanced_solution)
            if not clean_enhanced:
                log_print("  ✗ Failed to extract Final Blueprint from enhanced solution, using full solution")
                clean_enhanced = enhanced_solution

            # Grade enhanced solution N times
            enhanced_grades = []
            for i in range(self.post_enhancement_trigger_count):
                log_print(f"\n[Enhanced Grade {i+1}/{self.post_enhancement_trigger_count}]")

                grade_prompt = self.config_manager.get_template(
                    "grade_instruction",
                    problem=problem,
                    solution=clean_enhanced,
                    materials="None",
                )

                try:
                    from google import genai

                    api_key = self._get_gemini_api_key()
                    if not api_key:
                        log_print("✗ GEMINI_API_KEY not found")
                        break

                    if self._genai_client is None:
                        self._genai_client = genai.Client(api_key=api_key)
                    client = self._genai_client

                    system_prompt = self.config_manager.get_role_prompt("grader", "system_prompt")
                    model_id, gen_config = self._get_genai_model_config("grader", system_prompt)

                    chat = client.chats.create(model=model_id, config=gen_config)
                    response = chat.send_message(grade_prompt)

                    self._log_api_call(
                        step_name=f"Enhanced Solution Grade {i+1}",
                        role="grader",
                        prompt=grade_prompt,
                        response=response,
                    )

                    grade = self._extract_grade(response.text)
                    enhanced_grades.append(grade)
                    log_print(f"  Grade: {grade}/7")

                except Exception as e:
                    log_print(f"  ✗ Error in grading: {e}")
                    break

            # Compare average scores
            if enhanced_grades:
                original_avg = sum(original_grades) / len(original_grades)
                enhanced_avg = sum(enhanced_grades) / len(enhanced_grades)

                log_print("\n" + "="*80)
                log_print("SOLUTION COMPARISON")
                log_print("="*80)
                log_print(f"Original solution average: {original_avg:.2f}/7 (grades: {original_grades})")
                log_print(f"Enhanced solution average: {enhanced_avg:.2f}/7 (grades: {enhanced_grades})")

                if enhanced_avg > original_avg:
                    log_print(f"\n✓ Using ENHANCED solution (improvement: +{enhanced_avg - original_avg:.2f})")
                    log_print("="*80)
                    return (SolutionStatus.SOLVED, enhanced_solution)
                elif enhanced_avg == original_avg:
                    # Tie: always prefer enhanced (already invested in enhancement)
                    log_print(f"\n✓ Using ENHANCED solution (same avg: {enhanced_avg:.2f}/7)")
                    log_print("="*80)
                    return (SolutionStatus.SOLVED, enhanced_solution)
                else:
                    log_print(f"\n→ Using ORIGINAL solution (better by {original_avg - enhanced_avg:.2f})")
                    log_print("="*80)
                    return (status, final_solution)

        log_print("\n" + "="*80)
        log_print("⚠ MOMUS PIPELINE COMPLETE - POST-ENHANCEMENT DID NOT IMPROVE")
        log_print("="*80)
        log_print("Returning original base pipeline solution")
        return (status, final_solution)

    def _check_post_enhancement_trigger(
        self, problem: str, solution: str
    ) -> Tuple[bool, List[str], List[int]]:
        """
        Check if post-enhancement should be triggered.

        Runs N independent grades. If NOT all are 7/7, trigger enhancement.

        Args:
            problem: Problem statement
            solution: Candidate solution

        Returns:
            (should_trigger, feedbacks, grades) tuple
        """
        log_print(f"\nRunning {self.post_enhancement_trigger_count} independent grades...")

        # Extract Final Blueprint for grading (consistent with base pipeline internal grading)
        clean_solution = self._extract_final_blueprint(solution)
        if not clean_solution:
            log_print("  ✗ Failed to extract Final Blueprint, using full solution")
            clean_solution = solution

        grades = []
        feedbacks = []

        for i in range(self.post_enhancement_trigger_count):
            log_print(f"\n[Independent Grade {i+1}/{self.post_enhancement_trigger_count}]")

            # Use base pipeline's grading infrastructure
            grade_prompt = self.config_manager.get_template(
                "grade_instruction",
                problem=problem,
                solution=clean_solution,
                materials="None",
            )

            try:
                from google import genai
                from google.genai import types

                api_key = self._get_gemini_api_key()
                if not api_key:
                    log_print("✗ GEMINI_API_KEY not found")
                    return (False, [], [])

                if self._genai_client is None:
                    self._genai_client = genai.Client(api_key=api_key)
                client = self._genai_client

                system_prompt = self.config_manager.get_role_prompt("grader", "system_prompt")
                model_id, gen_config = self._get_genai_model_config("grader", system_prompt)

                chat = client.chats.create(model=model_id, config=gen_config)
                response = chat.send_message(grade_prompt)

                self._log_api_call(
                    step_name=f"Post-Enhancement Check - Grade {i+1}",
                    role="grader",
                    prompt=grade_prompt,
                    response=response,
                )

                feedback = response.text
                grade = self._extract_grade(feedback)

                grades.append(grade)
                feedbacks.append(feedback)
                log_print(f"  Grade: {grade}/7")

            except Exception as e:
                log_print(f"  ✗ Error in grading: {e}")
                return (False, [], [])

        # Check if all grades are perfect
        all_perfect = all(g == 7 for g in grades)
        avg_grade = sum(grades) / len(grades)

        if all_perfect:
            log_print(f"\n✗ POST-ENHANCEMENT NOT TRIGGERED")
            log_print(f"All {self.post_enhancement_trigger_count} grades = 7/7")
            log_print(f"Solution is already perfect")
            return (False, [], grades)

        # Check if solution meets minimum grade threshold
        if avg_grade < self.post_enhancement_min_grade:
            log_print(f"\n✗ POST-ENHANCEMENT NOT TRIGGERED")
            log_print(f"Grades: {grades} (avg: {avg_grade:.2f}/7)")
            log_print(f"Average grade {avg_grade:.2f} < threshold {self.post_enhancement_min_grade}")
            log_print(f"Solution quality too low for enhancement")
            return (False, [], grades)

        # Trigger enhancement
        log_print(f"\n✓ POST-ENHANCEMENT TRIGGERED")
        log_print(f"Grades: {grades} (avg: {avg_grade:.2f}/7)")
        log_print(f"Not all grades are 7/7 - solution can be improved")
        return (True, feedbacks, grades)

    def _run_post_enhancement(
        self, problem: str, candidate_solution: str, feedbacks: List[str]
    ) -> Tuple[SolutionStatus, str]:
        """
        Run post-enhancement pipeline.

        Args:
            problem: Problem statement
            candidate_solution: Solution to enhance
            feedbacks: Pre-computed feedbacks from trigger check

        Returns:
            (status, enhanced_solution) tuple
        """
        log_print("\n" + "="*80)
        log_print("POST-ENHANCEMENT PIPELINE")
        log_print("="*80)

        # Lazy initialization of post-enhancement agent
        if self._post_enhancement_agent is None:
            log_print("Initializing post-enhancement agent...")
            self._post_enhancement_agent = MomusPostEnhancementAgent(
                config_path=self.config_path,
                prompts_path=self.prompts_path,
                base_models_path=self.base_models_path,
                log_file=self.log_file,
            )

        # Run enhancement (skip trigger check since we already did it)
        return self._post_enhancement_agent.run_enhancement(
            problem=problem,
            candidate_solution=candidate_solution,
            feedbacks=feedbacks,
        )
