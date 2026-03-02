"""
IMO Solver Package
AI agents for solving International Mathematical Olympiad problems
"""

# Import main classes for easy access
from .agents.base_agent import BaseAgent, SolutionStatus
from .agents.huang_yang_agent import HuangYangAgent
from .agents.momus_agent import MomusAgent
from .agents.proof_autograder_agent import ProofAutoGraderAgent

# Import runners
from .runners.parallel_runner import run_parallel
from .runners.test_runner import run_test_suite

# Import utilities
from .utils.config_utils import ConfigManager
from .utils.logger import setup_logging

__all__ = [
    "BaseAgent",
    "SolutionStatus",
    "MomusAgent",
    "HuangYangAgent",
    "ProofAutoGraderAgent",
    "run_parallel",
    "run_test_suite",
    "ConfigManager",
    "setup_logging",
]
