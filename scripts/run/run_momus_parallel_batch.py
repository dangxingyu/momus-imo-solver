#!/usr/bin/env python3
"""
Run Momus Agent on multiple ProofBench problems in parallel.

Usage:
    python run_momus_parallel_batch.py --start 1 --end 10 --workers 3
    python run_momus_parallel_batch.py --start 1 --end 30 --workers 4

Examples:
    # Run first 10 Advanced problems with 3 parallel workers
    python run_momus_parallel_batch.py --start 1 --end 10 --workers 3

    # Run all 30 Advanced problems
    python run_momus_parallel_batch.py --start 1 --end 30 --workers 4
"""

import argparse
import csv
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

REPO_ROOT = Path(__file__).resolve().parents[2]
PROOFBENCH_CSV = REPO_ROOT / "proofbench.csv"
DEFAULT_CONFIG = "imo_solver/config/momus_config.yaml"
DEFAULT_PROMPTS = "imo_solver/prompts/momus_prompts.yaml"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "output/proofbench_momus_parallel_results/advanced"


def load_advanced_problems(start_idx: int, end_idx: int) -> list:
    """Load Advanced problems from proofbench.csv by index (1-based)."""
    if not PROOFBENCH_CSV.exists():
        raise FileNotFoundError(f"Missing proofbench CSV: {PROOFBENCH_CSV}")

    problems = []
    with open(PROOFBENCH_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            problem_id = row['Problem ID']
            # Filter for Advanced problems only
            if problem_id.startswith('PB-Advanced-'):
                problems.append({
                    'problem_id': problem_id,
                    'problem': row['Problem'],
                    'solution': row['Solution'],
                    'guidelines': row['Grading guidelines'],
                })

    # Sort by problem number
    problems.sort(key=lambda x: int(x['problem_id'].split('-')[-1]))

    # Select range (1-based indexing)
    selected = problems[start_idx - 1:end_idx]
    return selected


def run_single_problem(args_tuple):
    """Run Momus agent on a single problem. Called by ProcessPoolExecutor."""
    problem_data, config_path, prompts_path, output_base = args_tuple
    problem_id = problem_data['problem_id']

    # Import inside the function for multiprocessing
    from imo_solver.agents import MomusAgent
    from imo_solver.utils.logger import setup_logging, log_print

    # Create output directory
    output_dir = Path(output_base) / problem_id
    output_dir.mkdir(parents=True, exist_ok=True)

    # Setup logging
    log_file = output_dir / f"{problem_id}.log"
    setup_logging(str(log_file))

    start_time = datetime.now()
    log_print(f"\n{'='*80}")
    log_print(f"Momus Batch Run: {problem_id}")
    log_print(f"Config: {config_path}")
    log_print(f"Started: {start_time.isoformat()}")
    log_print(f"{'='*80}")

    result = {
        'problem_id': problem_id,
        'config_path': config_path,
        'start_time': start_time.isoformat(),
        'status': 'ERROR',
        'solved': False,
        'error': None,
        'duration_seconds': 0,
    }

    try:
        # Initialize and run agent
        agent = MomusAgent(
            config_path=config_path,
            prompts_path=prompts_path,
            log_file=str(log_file)
        )

        log_print(f"\nRunning Momus Agent on {problem_id}...")
        log_print(f"Problem:\n{problem_data['problem']}\n")

        status, solution = agent.run(problem_data['problem'])

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        result['status'] = str(status)
        result['solved'] = 'SOLVED' in str(status)
        result['end_time'] = end_time.isoformat()
        result['duration_seconds'] = duration

        log_print(f"\n{'='*80}")
        log_print(f"RESULT: {status}")
        log_print(f"Duration: {duration:.1f}s")
        log_print(f"{'='*80}")

        # Save solution
        if solution:
            solution_file = output_dir / "solution.txt"
            with open(solution_file, 'w', encoding='utf-8') as f:
                f.write(solution)

        # Save metadata
        metadata_file = output_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(result, f, indent=2)

    except Exception as e:
        import traceback
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        result['error'] = str(e)
        result['end_time'] = end_time.isoformat()
        result['duration_seconds'] = duration

        log_print(f"\n{'='*80}")
        log_print(f"ERROR: {e}")
        log_print(f"{'='*80}")
        traceback.print_exc()

        # Save error metadata
        metadata_file = output_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(result, f, indent=2)

    return result


def main():
    parser = argparse.ArgumentParser(description="Run Momus Agent on multiple problems in parallel")
    parser.add_argument("--start", "-s", type=int, default=1,
                        help="Start problem index (1-based, default: 1)")
    parser.add_argument("--end", "-e", type=int, default=10,
                        help="End problem index (inclusive, default: 10)")
    parser.add_argument("--workers", "-w", type=int, default=3,
                        help="Number of parallel workers (default: 3, recommended: 3-4)")
    parser.add_argument("--config", "-c", default=DEFAULT_CONFIG,
                        help=f"Path to config file (default: {DEFAULT_CONFIG})")
    parser.add_argument("--prompts", "-p", default=DEFAULT_PROMPTS,
                        help=f"Path to prompts file (default: {DEFAULT_PROMPTS})")
    parser.add_argument("--output-dir", "-o", default=str(DEFAULT_OUTPUT_DIR),
                        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})")
    args = parser.parse_args()

    print(f"{'='*80}")
    print(f"Momus PARALLEL BATCH RUN")
    print(f"{'='*80}")
    print(f"Problems: PB-Advanced-{args.start:03d} to PB-Advanced-{args.end:03d}")
    print(f"Workers: {args.workers}")
    print(f"Config: {args.config}")
    print(f"Output: {args.output_dir}")
    print(f"{'='*80}")

    # Load problems
    problems = load_advanced_problems(args.start, args.end)
    print(f"\nLoaded {len(problems)} problems:")
    for p in problems:
        print(f"  - {p['problem_id']}")

    if not problems:
        print("No problems found!")
        return 1

    # Prepare arguments for each problem
    task_args = [
        (problem, args.config, args.prompts, args.output_dir)
        for problem in problems
    ]

    # Run in parallel
    print(f"\n{'='*80}")
    print(f"Starting parallel execution with {args.workers} workers...")
    print(f"{'='*80}\n")

    batch_start = datetime.now()
    results = []

    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        # Submit all tasks
        future_to_problem = {
            executor.submit(run_single_problem, task_arg): task_arg[0]['problem_id']
            for task_arg in task_args
        }

        # Collect results as they complete
        for future in as_completed(future_to_problem):
            problem_id = future_to_problem[future]
            try:
                result = future.result()
                results.append(result)
                status_emoji = "✓" if result['solved'] else "✗"
                print(f"[{len(results)}/{len(problems)}] {status_emoji} {problem_id}: {result['status']} ({result['duration_seconds']:.1f}s)")
            except Exception as e:
                print(f"[{len(results)+1}/{len(problems)}] ✗ {problem_id}: EXCEPTION - {e}")
                results.append({
                    'problem_id': problem_id,
                    'status': 'EXCEPTION',
                    'solved': False,
                    'error': str(e),
                })

    batch_end = datetime.now()
    batch_duration = (batch_end - batch_start).total_seconds()

    # Summary
    print(f"\n{'='*80}")
    print(f"BATCH COMPLETE")
    print(f"{'='*80}")

    solved = sum(1 for r in results if r['solved'])
    total = len(results)

    print(f"Total: {total} problems")
    print(f"Solved: {solved} ({100*solved/total:.1f}%)")
    print(f"Failed: {total - solved}")
    print(f"Total duration: {batch_duration:.1f}s ({batch_duration/60:.1f} min)")
    print(f"Avg per problem: {batch_duration/total:.1f}s")

    print(f"\nResults by problem:")
    # Sort results by problem_id
    results.sort(key=lambda x: x['problem_id'])
    for r in results:
        status_emoji = "✓" if r['solved'] else "✗"
        duration = r.get('duration_seconds', 0)
        print(f"  {status_emoji} {r['problem_id']}: {r['status']} ({duration:.1f}s)")

    # Save batch summary
    summary_file = Path(args.output_dir) / f"batch_summary_{args.start}-{args.end}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    summary = {
        'start_idx': args.start,
        'end_idx': args.end,
        'config': args.config,
        'workers': args.workers,
        'batch_start': batch_start.isoformat(),
        'batch_end': batch_end.isoformat(),
        'batch_duration_seconds': batch_duration,
        'total': total,
        'solved': solved,
        'results': results,
    }
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to: {summary_file}")

    return 0 if solved == total else 1


if __name__ == "__main__":
    sys.exit(main())
