#!/usr/bin/env python3
"""
Run Gemini 3 experiments on a single problem.
"""

import os
import sys
import argparse
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from imo_solver.agents import MomusAgent, SolutionStatus
from imo_solver.utils.logger import setup_logging, log_print


def main():
    parser = argparse.ArgumentParser(description="Run Gemini 3 Momus on a single problem")
    parser.add_argument("--config", required=True, help="Path to config YAML")
    parser.add_argument("--prompts", required=True, help="Path to prompts YAML")
    parser.add_argument("--problem", required=True, help="Path to problem file")
    parser.add_argument("--output", required=True, help="Output directory")
    parser.add_argument("--log", required=True, help="Log file path")

    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.output, exist_ok=True)

    # Setup logging
    setup_logging(args.log)

    # Load problem
    with open(args.problem, 'r') as f:
        problem_text = f.read().strip()

    log_print("="*80)
    log_print(f"GEMINI 3 EXPERIMENT")
    log_print("="*80)
    log_print(f"Config: {args.config}")
    log_print(f"Problem: {args.problem}")
    log_print(f"Output: {args.output}")
    log_print("")
    log_print(f"Problem text: {problem_text[:200]}...")

    # Initialize agent
    log_print("\nInitializing Momus agent...")
    agent = MomusAgent(
        config_path=args.config,
        prompts_path=args.prompts,
        base_models_path="imo_solver/config/base_models_config.yaml",
        log_file=args.log,
    )

    # Run agent
    log_print("\n" + "="*80)
    log_print("STARTING Momus PIPELINE")
    log_print("="*80)

    status, solution = agent.run(problem_text, max_runs=3)

    # Save results
    log_print("\n" + "="*80)
    log_print("EXPERIMENT COMPLETE")
    log_print("="*80)
    log_print(f"Status: {status}")

    if status == SolutionStatus.SOLVED and solution:
        solution_file = os.path.join(args.output, "solution.txt")
        with open(solution_file, 'w') as f:
            f.write(solution)
        log_print(f"\n✓ Solution saved to: {solution_file}")
    elif solution:
        solution_file = os.path.join(args.output, "attempted_solution.txt")
        with open(solution_file, 'w') as f:
            f.write(solution)
        log_print(f"\n⚠ Attempted solution saved to: {solution_file}")
    else:
        log_print("\n✗ No solution generated")

    # Return exit code
    if status == SolutionStatus.SOLVED:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
