"""
Base Agent Class for IMO Problem Solving
Provides a common interface for all agent implementations
"""

import time
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Tuple

from ..utils.config_utils import initialize_config, validate_environment
from ..utils.logger import setup_logging, log_print


class SolutionStatus(Enum):
    """Status of solution attempt"""

    SOLVED = "solved"
    UNSOLVED = "unsolved"
    ERROR = "error"
    TIMEOUT = "timeout"


class BaseAgent(ABC):
    """Base class for all IMO problem solving agents"""

    def __init__(
        self,
        config_path: str = "imo_solver/config/huang_yang_config.yaml",
        prompts_path: str = "imo_solver/prompts/huang_yang_prompts.yaml",
        base_models_path: Optional[str] = None,
        log_file: Optional[str] = None,
    ):
        """
        Initialize agent with configuration

        Args:
            config_path: Path to roles config YAML file (new architecture) or legacy single config file
            prompts_path: Path to prompts YAML file
            base_models_path: Path to base models YAML file (optional, auto-detected if None)
            log_file: Optional log file path
        """
        # Store configuration paths
        self.config_path = config_path
        self.prompts_path = prompts_path
        self.base_models_path = base_models_path
        self.log_file = log_file

        # Setup logging if specified
        if log_file:
            setup_logging(log_file)

        # Validate environment
        validate_environment()

        # Initialize configuration with new two-file architecture support
        self.config_manager = initialize_config(
            config_path, prompts_path, base_models_path
        )
        self.start_time = None

        # Log hyperparameters at initialization
        self._log_hyperparameters()

    @abstractmethod
    def run(
        self, problem_statement: str, max_runs: int = 2, **kwargs
    ) -> Tuple[SolutionStatus, Optional[str]]:
        """
        Run the agent on a problem and return status and solution

        Args:
            problem_statement: The problem text
            max_runs: Maximum solution attempts
            **kwargs: Additional agent-specific parameters

        Returns:
            Tuple of (SolutionStatus, solution_text or None)
        """
        pass

    def run_with_status_only(
        self, problem_text: str, max_runs: int = None
    ) -> SolutionStatus:
        """
        Run the agent on problem text and return status only

        Args:
            problem_text: The problem statement as text
            max_runs: Maximum solution attempts

        Returns:
            SolutionStatus indicating success or failure
        """
        self.start_time = time.time()

        try:
            problem_statement = problem_text.strip()
            log_print(f"\nProblem text (first 100 chars): {problem_statement[:100]}...")

            # Run the agent
            status, _ = self.run(problem_statement, max_runs)

            # Log results
            elapsed = time.time() - self.start_time
            log_print(f"\nExecution time: {elapsed:.2f}s")
            log_print(f"Final status: {status.value}")

            return status

        except Exception as e:
            log_print(f"Error during execution: {e}")
            return SolutionStatus.ERROR

    def run_from_file(self, problem_file: str, max_runs: int = None) -> SolutionStatus:
        """
        Run the agent on a problem file

        Args:
            problem_file: Path to problem file
            max_runs: Maximum solution attempts

        Returns:
            SolutionStatus indicating success or failure
        """
        try:
            with open(problem_file, "r", encoding="utf-8") as f:
                problem_text = f.read().strip()

            log_print(f"Problem file: {problem_file}")
            return self.run_with_status_only(problem_text, max_runs)

        except FileNotFoundError:
            log_print(f"Error: Problem file '{problem_file}' not found")
            return SolutionStatus.ERROR
        except Exception as e:
            log_print(f"Error reading problem file: {e}")
            return SolutionStatus.ERROR

    def get_execution_time(self) -> float:
        """Get execution time in seconds"""
        if self.start_time:
            return time.time() - self.start_time
        return 0.0

    def _log_hyperparameters(self):
        """Log hyperparameters and configuration info at start of each session"""
        if hasattr(self, "log_file") and self.log_file:
            log_print("\n" + "=" * 80)
            log_print("HYPERPARAMETERS & CONFIGURATION")
            log_print("=" * 80)
            log_print(f"Agent Type: {self.__class__.__name__}")
            log_print(f"Config File: {self.config_path}")
            log_print(f"Prompts File: {self.prompts_path}")
            log_print(f"Base Models File: {self.base_models_path or 'Auto-detected'}")
            log_print(f"Log File: {self.log_file}")

            # Log execution settings
            if hasattr(self.config_manager, "execution"):
                execution_config = self.config_manager.execution
                log_print("\nExecution Settings:")
                for key, value in execution_config.items():
                    log_print(f"  {key}: {value}")

            # Log retry settings
            if hasattr(self.config_manager, "retry"):
                retry_config = self.config_manager.retry
                log_print("\nRetry Settings:")
                for key, value in retry_config.items():
                    log_print(f"  {key}: {value}")

            # Log logging settings
            if hasattr(self.config_manager, "logging_config"):
                logging_config = self.config_manager.logging_config
                log_print("\nLogging Settings:")
                for key, value in logging_config.items():
                    log_print(f"  {key}: {value}")

            log_print("=" * 80 + "\n")
