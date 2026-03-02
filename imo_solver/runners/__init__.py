"""
Runners for executing IMO solver agents
"""

from .parallel_runner import run_parallel
from .test_runner import run_test_suite

__all__ = ["run_parallel", "run_test_suite"]
