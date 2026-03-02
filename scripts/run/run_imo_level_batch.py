#!/usr/bin/env python3
"""
Run Momus Agent on IMO-level problems in parallel.

Usage:
    python run_imo_level_batch.py --start 1 --end 10 --workers 5
    python run_imo_level_batch.py --start 1 --end 5 --workers 3 --output-dir imo_level_experiments/imo_level_run1
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
IMO_LEVEL_CSV = REPO_ROOT / "imo_level_dataset.csv"
DEFAULT_CONFIG = "imo_solver/config/momus_exp_gemini3_flash_depth3_config.yaml"
DEFAULT_PROMPTS = "imo_solver/prompts/momus_prompts.yaml"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "output/imo_level_results"


def load_imo_level_problems(csv_path: str, start_idx: int = 1, end_idx: int = 10) -> list:
    """Load problems from imo_level_dataset.csv by index (1-based)."""
    problems = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            num = int(row['Problem_Number'])
            problems.append({
                'problem_id': f"IMO-Level-{num:03d}",
                'problem': row['Problem'],
                'solution': row['Solution'],
                'rubric': row['Rubric'],
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
    log_print(f"IMO-Level Batch Run: {problem_id}")
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

        metadata_file = output_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(result, f, indent=2)

    return result


def main():
    parser = argparse.ArgumentParser(description="Run Momus Agent on IMO-level problems in parallel")
    parser.add_argument("--start", "-s", type=int, default=1,
                        help="Start problem index (1-based, default: 1)")
    parser.add_argument("--end", "-e", type=int, default=10,
                        help="End problem index (inclusive, default: 10)")
    parser.add_argument("--workers", "-w", type=int, default=5,
                        help="Number of parallel workers (default: 5)")
    parser.add_argument("--config", "-c", default=DEFAULT_CONFIG,
                        help=f"Path to config file (default: {DEFAULT_CONFIG})")
    parser.add_argument("--prompts", "-p", default=DEFAULT_PROMPTS,
                        help=f"Path to prompts file (default: {DEFAULT_PROMPTS})")
    parser.add_argument("--output-dir", "-o", default=str(DEFAULT_OUTPUT_DIR),
                        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("--csv", default=str(IMO_LEVEL_CSV),
                        help=f"Path to CSV file (default: {IMO_LEVEL_CSV})")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        raise FileNotFoundError(
            f"CSV file not found: {csv_path}. Pass --csv <path-to-imo_level_dataset.csv>."
        )

    print(f"{'='*80}")
    print(f"IMO-LEVEL Momus PARALLEL BATCH RUN")
    print(f"{'='*80}")
    print(f"Problems: IMO-Level-{args.start:03d} to IMO-Level-{args.end:03d}")
    print(f"Workers: {args.workers}")
    print(f"Config: {args.config}")
    print(f"Output: {args.output_dir}")
    print(f"{'='*80}")

    # Load problems
    problems = load_imo_level_problems(str(csv_path), args.start, args.end)
    print(f"\nLoaded {len(problems)} problems:")
    for p in problems:
        print(f"  - {p['problem_id']}")

    if not problems:
        print("No problems found!")
        return 1

    # Create output dir
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)

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
        future_to_problem = {
            executor.submit(run_single_problem, task_arg): task_arg[0]['problem_id']
            for task_arg in task_args
        }

        for future in as_completed(future_to_problem):
            problem_id = future_to_problem[future]
            try:
                result = future.result()
                results.append(result)
                status_sym = "+" if result['solved'] else "x"
                print(f"[{len(results)}/{len(problems)}] {status_sym} {problem_id}: {result['status']} ({result['duration_seconds']:.1f}s)")
            except Exception as e:
                print(f"[{len(results)+1}/{len(problems)}] x {problem_id}: EXCEPTION - {e}")
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
    results.sort(key=lambda x: x['problem_id'])
    for r in results:
        status_sym = "+" if r['solved'] else "x"
        duration = r.get('duration_seconds', 0)
        print(f"  {status_sym} {r['problem_id']}: {r['status']} ({duration:.1f}s)")

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
