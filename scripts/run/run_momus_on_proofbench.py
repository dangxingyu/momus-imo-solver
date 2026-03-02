#!/usr/bin/env python3
"""
Run Momus Agent on proofbench Advanced problems (001-030).

This script:
1. Loads all PB-Advanced-001 to PB-Advanced-030 problems from proofbench.csv
2. Runs Momus agent on each problem (full base pipeline + post-enhancement pipeline)
3. Saves solutions and metadata
"""

import os
import sys
import csv
import json
import argparse
from pathlib import Path
from typing import Dict

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from imo_solver.agents import MomusAgent, SolutionStatus
from imo_solver.utils.logger import setup_logging, log_print


# Paths
REPO_ROOT = Path(__file__).resolve().parents[2]
PROOFBENCH_CSV = REPO_ROOT / "proofbench.csv"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "output/proofbench_momus_results/advanced"


def load_proofbench_problems() -> Dict[str, str]:
    """
    Load all PB-Advanced problems from proofbench.csv.

    Returns:
        Dict mapping problem_id to problem_text
    """
    problems = {}

    if not PROOFBENCH_CSV.exists():
        raise FileNotFoundError(f"Missing proofbench CSV: {PROOFBENCH_CSV}")

    with open(PROOFBENCH_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            problem_id = row['Problem ID']
            # Filter for Advanced problems only
            if problem_id.startswith('PB-Advanced-'):
                problems[problem_id] = row['Problem']

    return problems


def run_momus_on_problem(problem_id: str, problem_text: str, output_dir: str) -> Dict:
    """
    Run Momus agent on a single problem.

    Args:
        problem_id: Problem ID (e.g., "PB-Advanced-010")
        problem_text: Problem statement
        output_dir: Output directory for results

    Returns:
        Dict with status, solution (if solved), and metadata
    """
    # Setup output directory for this problem
    problem_dir = Path(output_dir) / problem_id
    problem_dir.mkdir(parents=True, exist_ok=True)

    log_file = problem_dir / f"{problem_id}.log"

    log_print("\n" + "="*80)
    log_print(f"RUNNING Momus ON {problem_id}")
    log_print("="*80)
    log_print(f"Problem: {problem_text[:200]}...")

    # Initialize Momus agent
    agent = MomusAgent(
        config_path="imo_solver/config/momus_config.yaml",
        prompts_path="imo_solver/prompts/momus_prompts.yaml",
        log_file=str(log_file),
    )

    # Run agent
    try:
        status, solution = agent.run(problem_text, max_runs=3)

        result = {
            "problem_id": problem_id,
            "status": str(status),
            "solved": status == SolutionStatus.SOLVED,
        }

        # Save solution (regardless of status, for grading)
        if solution:
            solution_file = problem_dir / "solution.txt"
            with open(solution_file, 'w') as f:
                f.write(solution)
            result["solution_file"] = str(solution_file)
        else:
            result["solution_file"] = None

        if status == SolutionStatus.SOLVED:
            log_print(f"\n✓ {problem_id}: SOLVED")
        else:
            log_print(f"\n✗ {problem_id}: NOT SOLVED (but solution saved for grading)")

        # Save metadata
        metadata_file = problem_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(result, f, indent=2)

        log_print(f"Log saved to: {log_file}")
        return result

    except Exception as e:
        log_print(f"\n✗ {problem_id}: ERROR - {e}")
        import traceback
        traceback.print_exc()

        return {
            "problem_id": problem_id,
            "status": "error",
            "solved": False,
            "error": str(e),
        }


def main():
    """Main execution function."""

    # Parse arguments
    parser = argparse.ArgumentParser(description="Run Momus agent on proofbench Advanced problems")
    parser.add_argument("--start", type=int, default=1,
                        help="Start problem number (default: 1)")
    parser.add_argument("--end", type=int, default=30,
                        help="End problem number (default: 30)")
    parser.add_argument("--output-dir", type=str, default=str(DEFAULT_OUTPUT_DIR),
                        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})")
    args = parser.parse_args()

    # Use provided output directory
    output_dir = args.output_dir

    # Setup logging
    os.makedirs(output_dir, exist_ok=True)
    main_log = os.path.join(output_dir, "..", f"run_momus_main_{args.start:03d}_{args.end:03d}.log")
    setup_logging(main_log)

    log_print("="*80)
    log_print("RUNNING Momus AGENT ON PROOFBENCH ADVANCED PROBLEMS")
    log_print("="*80)
    log_print(f"Output directory: {output_dir}")
    log_print(f"Problem range: {args.start:03d} - {args.end:03d}")

    # Load problems
    log_print("\nLoading proofbench problems...")
    all_problems = load_proofbench_problems()
    log_print(f"Total Advanced problems available: {len(all_problems)}")

    # Filter by range
    problems = {
        pid: text for pid, text in all_problems.items()
        if args.start <= int(pid.split('-')[-1]) <= args.end
    }
    log_print(f"Selected problems: {len(problems)}")

    # Run Momus on each problem
    results = []
    skipped = []
    for i, (problem_id, problem_text) in enumerate(sorted(problems.items()), 1):
        log_print(f"\n{'='*80}")
        log_print(f"PROBLEM {i}/{len(problems)}: {problem_id}")
        log_print(f"{'='*80}")

        # Check if already completed (has metadata.json)
        metadata_file = Path(output_dir) / problem_id / "metadata.json"
        if metadata_file.exists():
            log_print(f"⏭ SKIPPING {problem_id} - already completed (metadata.json exists)")
            skipped.append(problem_id)
            # Load existing result
            with open(metadata_file, 'r') as f:
                existing_result = json.load(f)
            results.append(existing_result)
            continue

        result = run_momus_on_problem(problem_id, problem_text, output_dir)
        results.append(result)

    # Save summary
    log_print("\n" + "="*80)
    log_print("RUN COMPLETE - SUMMARY")
    log_print("="*80)

    solved = [r for r in results if r.get("solved", False)]
    errors = [r for r in results if r.get("status") == "error"]

    log_print(f"Total problems: {len(results)}")
    log_print(f"Skipped (already done): {len(skipped)}")
    log_print(f"Solved: {len(solved)}/{len(results)} ({100*len(solved)/len(results):.1f}%)")
    log_print(f"Errors: {len(errors)}")

    log_print("\nPer-problem results:")
    for r in results:
        status_str = "✓ SOLVED" if r.get("solved") else "✗ NOT SOLVED"
        if r.get("status") == "error":
            status_str = f"✗ ERROR: {r.get('error', 'unknown')}"
        log_print(f"  {r['problem_id']}: {status_str}")

    # Save summary JSON
    summary_file = Path(output_dir) / ".." / f"momus_summary_{args.start:03d}_{args.end:03d}.json"
    with open(summary_file, 'w') as f:
        json.dump({
            "total": len(results),
            "skipped": len(skipped),
            "solved": len(solved),
            "errors": len(errors),
            "skipped_ids": skipped,
            "results": results,
        }, f, indent=2)

    log_print(f"\nSummary saved to: {summary_file}")
    log_print(f"Main log: {main_log}")


if __name__ == "__main__":
    main()
