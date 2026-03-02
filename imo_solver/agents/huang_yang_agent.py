"""
Huang Yang IMO Problem Solver Agent.
"""

from typing import Optional, Tuple

from .base_agent import BaseAgent, SolutionStatus
from ..utils.config_utils import (
    get_role_prompt_required,
    get_template_required,
    send_role_based_request,
)
from ..utils.logger import log_print


class HuangYangAgent(BaseAgent):
    """Huang Yang IMO problem solving agent with verification pipeline."""

    def __init__(
        self,
        config_path: str = "imo_solver/config/huang_yang_config.yaml",
        prompts_path: str = "imo_solver/prompts/huang_yang_prompts.yaml",
        base_models_path: Optional[str] = None,
        log_file: Optional[str] = None,
    ):
        super().__init__(config_path, prompts_path, base_models_path, log_file)

    def run(
        self, problem_statement: str, max_runs: int = None, **kwargs
    ) -> Tuple[SolutionStatus, Optional[str]]:
        """Solve a problem using the Huang Yang verification pipeline."""
        if max_runs is None:
            max_runs = self.config_manager.execution.get("max_runs", 2)

        max_iterations = self.config_manager.execution.get("max_iterations", 30)
        success_threshold = self.config_manager.execution.get("success_threshold", 5)
        failure_threshold = self.config_manager.execution.get("failure_threshold", 10)

        log_print(f"\n{'='*70}")
        log_print("HUANG YANG AGENT - PIPELINE CONFIGURATION")
        log_print(f"{'='*70}")
        log_print(f"Agent Type: {self.__class__.__name__}")
        log_print(f"Config File: {self.config_path}")
        log_print(f"Prompts File: {self.prompts_path}")
        log_print(f"Max runs: {max_runs}")
        log_print(f"Max iterations per run: {max_iterations}")
        log_print(f"Success threshold: {success_threshold}")
        log_print(f"Failure threshold: {failure_threshold}")
        log_print(f"{'='*70}")

        for run in range(max_runs):
            log_print(f"\n{'='*70}")
            log_print(f"RUN {run + 1}/{max_runs}")
            log_print(f"{'='*70}")

            dsol = self.init_explorations(problem_statement)
            if not dsol:
                log_print("Failed to generate initial solution")
                continue

            was_initially_incomplete = not self.check_if_solution_claimed_complete(dsol)

            if was_initially_incomplete:
                log_print(
                    "Solution does not claim to be complete - treating as incomplete and improving"
                )
                dsol = self.improve_solution(problem_statement, dsol)
                if not dsol:
                    log_print("Failed to improve incomplete solution")
                    continue
                log_print("\n[Incomplete solution improved, proceeding to verification]")
            else:
                log_print("\n[Self-improvement phase]")
                dsol = self.improve_solution(problem_statement, dsol)
                if not dsol:
                    log_print("Failed to improve solution")
                    continue

            consecutive_success = 0
            consecutive_failure = 0

            if was_initially_incomplete:
                consecutive_failure = 1
                log_print(
                    "Starting verification loop with +1 failure count due to initial incompleteness"
                )

            for iteration in range(max_iterations):
                log_print(f"\n[Verification iteration {iteration + 1}/{max_iterations}]")

                verification_output = self.verify_solution(problem_statement, dsol)
                if not verification_output:
                    log_print("Verification failed - API error")
                    break

                is_correct = self.analyze_verification_output(verification_output)

                if is_correct:
                    consecutive_success += 1
                    consecutive_failure = 0
                    log_print(
                        f"Solution verified correct ({consecutive_success}/{success_threshold})"
                    )

                    if consecutive_success >= success_threshold:
                        log_print(f"\n{'='*70}")
                        log_print(f"SUCCESS! Found a correct solution in run {run + 1}")
                        log_print(f"{'='*70}")
                        log_print("\n[FINAL SOLUTION]")
                        log_print(dsol)
                        return (SolutionStatus.SOLVED, dsol)
                else:
                    consecutive_success = 0
                    consecutive_failure += 1
                    log_print(
                        f"Solution has issues ({consecutive_failure}/{failure_threshold}), attempting to fix..."
                    )

                    if consecutive_failure >= failure_threshold:
                        log_print("\n[FAILURE THRESHOLD REACHED]")
                        log_print(
                            f"Solution failed verification {failure_threshold} consecutive times"
                        )
                        log_print("Moving to next run...")
                        break

                    dsol = self.improve_solution(
                        problem_statement, dsol, verification_output
                    )
                    if not dsol:
                        log_print("Failed to improve solution based on feedback")
                        break
                    log_print("\n[Solution improved based on verification feedback]")
                    log_print(dsol)

        log_print(f"\n{'='*70}")
        log_print("All runs completed without finding a verified solution")
        log_print(f"{'='*70}")
        return (SolutionStatus.UNSOLVED, None)

    def init_explorations(self, problem_statement: str) -> Optional[str]:
        """Initial exploration and solution generation."""
        question_prompt = get_template_required(
            "initial_problem", self.config_manager, problem_statement=problem_statement
        )
        system_prompt = get_role_prompt_required(
            "prover", "system_prompt", self.config_manager
        )

        log_print("\n" + "=" * 70)
        log_print("STAGE: INITIAL SOLUTION")
        log_print("=" * 70)

        init_dsol = send_role_based_request(
            system_prompt,
            question_prompt,
            role="prover",
            config_manager=self.config_manager,
        )

        if init_dsol:
            log_print("\n[Initial solution generated]")
            log_print(init_dsol)
        else:
            log_print("\n[Failed to generate initial solution]")

        return init_dsol

    def verify_solution(self, problem_statement: str, dsol: str) -> Optional[str]:
        """Verify the solution using verifier role."""
        verifier_system_prompt = get_role_prompt_required(
            "verifier", "system_prompt", self.config_manager
        )
        verification_reminder = get_role_prompt_required(
            "verifier", "reminder_prompt", self.config_manager
        )

        verification_task = get_template_required(
            "verification_task",
            self.config_manager,
            problem_statement=problem_statement,
            dsol=dsol,
            verification_reminder=verification_reminder,
        )

        log_print("\n" + "=" * 70)
        log_print("STAGE: VERIFYING SOLUTION")
        log_print("=" * 70)

        verification_output = send_role_based_request(
            verifier_system_prompt,
            verification_task,
            role="verifier",
            config_manager=self.config_manager,
        )

        if verification_output:
            log_print("\n[Verification complete]")
            if self.config_manager.logging_config.get("log_verification", True):
                log_print(verification_output)
        else:
            log_print("\n[Verification failed]")

        return verification_output

    def check_if_solution_claimed_complete(self, dsol: str) -> bool:
        """Check if the solution claims to be complete."""
        system_prompt = get_role_prompt_required(
            "completeness_checker", "system_prompt", self.config_manager
        )
        question_prompt = get_template_required(
            "completeness_check", self.config_manager, solution=dsol
        )

        response = send_role_based_request(
            system_prompt,
            question_prompt,
            role="completeness_checker",
            config_manager=self.config_manager,
        )

        log_print(f"Completeness checker response: {response}")
        return bool(response and "yes" in response.lower())

    def analyze_verification_output(self, verification_output: str) -> bool:
        """Analyze verification output to determine if solution is correct."""
        system_prompt = get_role_prompt_required(
            "bug_analyzer", "system_prompt", self.config_manager
        )
        question_prompt = get_template_required(
            "bug_report_analysis",
            self.config_manager,
            verification_output=verification_output,
        )

        bug_report = send_role_based_request(
            system_prompt,
            question_prompt,
            role="bug_analyzer",
            config_manager=self.config_manager,
        )

        log_print(f"Bug analyzer response: {bug_report}")
        return bool(bug_report and "yes" in bug_report.lower())

    def improve_solution(
        self,
        problem_statement: str,
        dsol: str,
        verification_output: Optional[str] = None,
    ) -> Optional[str]:
        """Improve solution based on feedback."""
        improver_system_prompt = get_role_prompt_required(
            "improver", "system_prompt", self.config_manager
        )

        if verification_output:
            correction_prompt = get_role_prompt_required(
                "improver", "correction_prompt", self.config_manager
            )
            improver_prompt = get_template_required(
                "correction_task",
                self.config_manager,
                problem_statement=problem_statement,
                dsol=dsol,
                bug_report=verification_output,
                correction_prompt=correction_prompt,
            )
        else:
            improvement_prompt = get_role_prompt_required(
                "improver", "improvement_prompt", self.config_manager
            )
            improver_prompt = get_template_required(
                "improvement_task",
                self.config_manager,
                problem_statement=problem_statement,
                dsol=dsol,
                improvement_prompt=improvement_prompt,
            )

        log_print("\n" + "=" * 70)
        log_print("STAGE: IMPROVING SOLUTION")
        log_print("=" * 70)

        improved_dsol = send_role_based_request(
            improver_system_prompt,
            improver_prompt,
            role="improver",
            config_manager=self.config_manager,
        )

        if improved_dsol:
            log_print("\n[Solution improved]")
        else:
            log_print("\n[Failed to improve solution]")

        return improved_dsol
