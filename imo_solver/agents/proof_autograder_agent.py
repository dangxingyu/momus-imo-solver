"""
ProofAutoGrader agent for IMO-style proof grading on a 0-7 scale.
"""

import re
from typing import Any, Dict, Optional, Tuple

from .base_agent import BaseAgent, SolutionStatus
from ..utils.config_utils import (
    get_prompt_required,
    get_template_required,
    send_role_based_request,
)
from ..utils.logger import log_print


POINTS_TAG_RE = re.compile(
    r"<points>\s*([0-7])\s*out\s*of\s*7\s*</points>", re.IGNORECASE
)
POINTS_FALLBACK_RE = re.compile(r"\b([0-7])\s*out\s*of\s*7\b", re.IGNORECASE)


class ProofAutoGraderAgent(BaseAgent):
    """ProofAutoGrader agent (IMO 0-7 grading)."""

    def __init__(
        self,
        config_path: str = "imo_solver/config/proof_autograder_config.yaml",
        prompts_path: str = "imo_solver/prompts/proof_autograder_prompts.yaml",
        base_models_path: Optional[str] = None,
        log_file: Optional[str] = None,
    ):
        super().__init__(config_path, prompts_path, base_models_path, log_file)

    def run(
        self, problem_statement: str, max_runs: int = 1, **kwargs
    ) -> Tuple[SolutionStatus, Optional[str]]:
        """
        BaseAgent-compatible entry point.

        Required kwargs:
            ground_truth_solution: Reference solution text
            grading_guidelines: Per-problem grading criteria
            proposed_solution: Student/model solution to grade
        """
        ground_truth_solution = kwargs.get("ground_truth_solution", "")
        grading_guidelines = kwargs.get("grading_guidelines", "")
        proposed_solution = kwargs.get("proposed_solution", "")

        if not proposed_solution:
            log_print("ProofAutoGraderAgent: proposed_solution is empty")
            return SolutionStatus.ERROR, None

        result = self.grade_submission(
            problem_statement=problem_statement,
            ground_truth_solution=ground_truth_solution,
            grading_guidelines=grading_guidelines,
            proposed_solution=proposed_solution,
        )

        points = result.get("points")
        if points is None:
            return SolutionStatus.ERROR, result.get("raw_response")

        # Keep BaseAgent semantics: "SOLVED" means high-quality proof (>= 6/7).
        status = SolutionStatus.SOLVED if points >= 6 else SolutionStatus.UNSOLVED
        return status, result.get("raw_response")

    def grade_submission(
        self,
        problem_statement: str,
        ground_truth_solution: str,
        grading_guidelines: str,
        proposed_solution: str,
    ) -> Dict[str, Any]:
        """Grade one submission and return parsed scoring info."""
        system_prompt = get_prompt_required(
            "proof_autograder_system_prompt", self.config_manager
        )
        question_prompt = get_template_required(
            "proof_autograder_task",
            self.config_manager,
            problem_statement=problem_statement or "",
            ground_truth_solution=ground_truth_solution or "",
            grading_guidelines=grading_guidelines or "",
            proposed_solution=proposed_solution or "",
        )

        response_text, usage = send_role_based_request(
            system_prompt,
            question_prompt,
            role="grader",
            config_manager=self.config_manager,
            return_usage=True,
        )

        response_text = response_text or ""
        points, parse_source = self._extract_points(response_text)
        reasoning = self._extract_reasoning(response_text)

        result = {
            "points": points,
            "points_text": f"{points} out of 7" if points is not None else None,
            "normalized_score": (points / 7.0) if points is not None else None,
            "passed": (points >= 6) if points is not None else False,
            "parse_source": parse_source,
            "reasoning": reasoning,
            "raw_response": response_text,
            "usage": usage,
        }

        if points is None:
            log_print("ProofAutoGraderAgent: failed to parse <points> tag")
        else:
            log_print(f"ProofAutoGraderAgent: parsed score {points}/7")

        return result

    @staticmethod
    def _extract_points(text: str) -> Tuple[Optional[int], str]:
        """Extract 0-7 score from model output."""
        if not text:
            return None, "missing"

        match = POINTS_TAG_RE.search(text)
        if match:
            return int(match.group(1)), "points_tag"

        fallback = POINTS_FALLBACK_RE.search(text)
        if fallback:
            return int(fallback.group(1)), "fallback_pattern"

        return None, "unparsed"

    @staticmethod
    def _extract_reasoning(text: str) -> str:
        """Return response text before <points> tag when possible."""
        if not text:
            return ""

        match = POINTS_TAG_RE.search(text)
        if match:
            return text[: match.start()].strip()
        return text.strip()
