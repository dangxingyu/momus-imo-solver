"""
Test runner for IMO solver test suites
"""

import os
import json
import time
from pathlib import Path
from typing import Dict, Type, Optional

from ..agents.base_agent import BaseAgent, SolutionStatus
from ..agents.huang_yang_agent import HuangYangAgent


def run_single_test(
    problem_file: str,
    agent_class: Type[BaseAgent] = HuangYangAgent,
    log_dir: str = "./logs",
    config_path: str = "imo_solver/config/huang_yang_config.yaml",
    prompts_path: str = "imo_solver/prompts/huang_yang_prompts.yaml",
    base_models_path: Optional[str] = None,
) -> tuple:
    """
    Run agent on single problem

    Returns:
        (problem_name, status, time_taken)
    """
    problem_name = Path(problem_file).stem
    log_file = os.path.join(log_dir, f"{problem_name}.log")

    print(f"  {problem_name:<20} ... ", end="", flush=True)

    # Create agent with new architecture support
    agent = agent_class(
        config_path=config_path,
        prompts_path=prompts_path,
        base_models_path=base_models_path,
        log_file=log_file,
    )

    # Run agent (let it use config file default for max_runs)
    start_time = time.time()
    status = agent.run_from_file(
        problem_file
    )  # No max_runs specified, will use config default
    time_taken = time.time() - start_time

    # Print result
    if status == SolutionStatus.SOLVED:
        print(f"✓ SOLVED ({time_taken:.1f}s)")
    else:
        print(f"✗ {status.value} ({time_taken:.1f}s)")

    return (problem_name, status, time_taken)


def run_test_suite(
    problems_dir: Optional[str] = None,
    agent_class: Type[BaseAgent] = HuangYangAgent,
    log_dir: str = "./logs",
    results_file: str = "./results.json",
    config_path: str = "imo_solver/config/huang_yang_config.yaml",
    prompts_path: str = "imo_solver/prompts/huang_yang_prompts.yaml",
    base_models_path: Optional[str] = None,
) -> Dict:
    """
    Run full test suite

    Returns:
        Dictionary with test results summary
    """
    if not problems_dir:
        raise ValueError("problems_dir is required")

    # Create directories
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(os.path.dirname(results_file) or ".", exist_ok=True)

    # Get problem files
    problem_path = Path(problems_dir)
    problem_files = sorted(list(problem_path.glob("*.txt")) + list(problem_path.glob("*.md")))

    if not problem_files:
        raise ValueError(f"No .txt or .md problem files found in {problems_dir}")

    print("=" * 60)
    print("IMO Agent Test Suite")
    print("=" * 60)
    print(f"Agent: {agent_class.__name__}")
    print(f"Problems: {len(problem_files)}")
    print("-" * 60)

    results = []
    solved = 0
    start_time = time.time()

    # Run tests
    for problem_file in problem_files:
        problem_name, status, time_taken = run_single_test(
            str(problem_file),
            agent_class,
            log_dir,
            config_path,
            prompts_path,
            base_models_path,
        )

        results.append(
            {"problem": problem_name, "status": status.value, "time": time_taken}
        )

        if status == SolutionStatus.SOLVED:
            solved += 1

    total_time = time.time() - start_time

    # Summary
    print("-" * 60)
    print(f"Results: {solved}/{len(problem_files)} solved")
    print(f"Success Rate: {100*solved/len(problem_files):.1f}%")
    print(f"Total Time: {total_time:.1f}s")

    # Save results
    summary = {
        "agent": agent_class.__name__,
        "config_path": config_path,
        "prompts_path": prompts_path,
        "base_models_path": base_models_path,
        "total": len(problem_files),
        "solved": solved,
        "success_rate": solved / len(problem_files) if len(problem_files) > 0 else 0,
        "total_time": total_time,
        "results": results,
    }

    with open(results_file, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nResults saved to: {results_file}")
    print(f"Logs saved to: {log_dir}")

    return summary
