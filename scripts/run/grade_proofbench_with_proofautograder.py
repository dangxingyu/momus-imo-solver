#!/usr/bin/env python3
"""
Grade ProofBench Advanced outputs with ProofAutoGraderAgent.

Expected input layout:
  <results-dir>/PB-Advanced-XXX/solution.txt

For each graded problem, this script writes:
  <results-dir>/PB-Advanced-XXX/proof_autograder_result.json

And a run summary JSON in <results-dir>.
"""

import argparse
import csv
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from imo_solver.agents import ProofAutoGraderAgent
from imo_solver.utils.logger import setup_logging, log_print


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PROOFBENCH_CSV = REPO_ROOT / "proofbench.csv"
DEFAULT_RESULTS_DIR = (
    REPO_ROOT / "output/proofbench_momus_parallel_results/gemini3_flash_resume_16_30_timeoutfix"
)
DEFAULT_CONFIG = "imo_solver/config/proof_autograder_config.yaml"
DEFAULT_PROMPTS = "imo_solver/prompts/proof_autograder_prompts.yaml"


def problem_index(problem_id: str) -> int:
    """Return numeric suffix from PB-Advanced-XXX."""
    try:
        return int(problem_id.split("-")[-1])
    except Exception:
        return -1


def load_proofbench_rows(csv_path: Path) -> Dict[str, Dict[str, str]]:
    """Load PB-Advanced rows keyed by Problem ID."""
    if not csv_path.exists():
        raise FileNotFoundError(f"Missing proofbench CSV: {csv_path}")

    rows: Dict[str, Dict[str, str]] = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            problem_id = row.get("Problem ID", "").strip()
            if problem_id.startswith("PB-Advanced-"):
                rows[problem_id] = row
    return rows


def collect_problem_ids(results_dir: Path, start: int, end: int) -> List[str]:
    """Collect PB-Advanced IDs from result directories in [start, end]."""
    ids: List[str] = []
    for d in sorted(results_dir.glob("PB-Advanced-*")):
        if not d.is_dir():
            continue
        idx = problem_index(d.name)
        if start <= idx <= end:
            ids.append(d.name)
    return sorted(ids, key=problem_index)


def load_existing_result(result_path: Path) -> Optional[Dict]:
    """Load an existing per-problem grade result if present/valid."""
    if not result_path.exists():
        return None
    try:
        with open(result_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def to_summary_record(problem_result: Dict, result_path: Path) -> Dict:
    """Return compact per-problem data for run-level summary JSON."""
    return {
        "problem_id": problem_result.get("problem_id"),
        "status": problem_result.get("status"),
        "points": problem_result.get("points"),
        "points_text": problem_result.get("points_text"),
        "normalized_score": problem_result.get("normalized_score"),
        "passed": problem_result.get("passed", False),
        "parse_source": problem_result.get("parse_source"),
        "usage": problem_result.get("usage"),
        "result_file": str(result_path),
        "solution_file": problem_result.get("solution_file"),
        "graded_at": problem_result.get("graded_at"),
    }


def write_json(path: Path, payload: Dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Grade ProofBench outputs with ProofAutoGraderAgent"
    )
    parser.add_argument(
        "--results-dir",
        default=str(DEFAULT_RESULTS_DIR),
        help=f"Directory with PB-Advanced-XXX subdirs (default: {DEFAULT_RESULTS_DIR})",
    )
    parser.add_argument(
        "--proofbench-csv",
        default=str(DEFAULT_PROOFBENCH_CSV),
        help=f"Path to proofbench.csv (default: {DEFAULT_PROOFBENCH_CSV})",
    )
    parser.add_argument("--start", type=int, default=1, help="Start index (default: 1)")
    parser.add_argument("--end", type=int, default=30, help="End index (default: 30)")
    parser.add_argument(
        "--solution-filename",
        default="solution.txt",
        help="Solution file name inside each problem dir (default: solution.txt)",
    )
    parser.add_argument(
        "--output-file",
        default=None,
        help="Optional summary output JSON path (default: auto in results-dir)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Re-grade even if proof_autograder_result.json already exists",
    )
    parser.add_argument(
        "--config",
        default=DEFAULT_CONFIG,
        help=f"Roles config for grader model selection (default: {DEFAULT_CONFIG})",
    )
    parser.add_argument(
        "--prompts",
        default=DEFAULT_PROMPTS,
        help=f"Prompts file (default: {DEFAULT_PROMPTS})",
    )
    parser.add_argument(
        "--base-models",
        default=None,
        help="Optional base models file path",
    )
    args = parser.parse_args()

    results_dir = Path(args.results_dir).resolve()
    csv_path = Path(args.proofbench_csv).resolve()

    if not results_dir.exists():
        raise FileNotFoundError(f"Results directory not found: {results_dir}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = results_dir / f"proof_autograder_run_{args.start:03d}_{args.end:03d}_{timestamp}.log"
    setup_logging(str(log_path), force_new=True)

    summary_path = (
        Path(args.output_file).resolve()
        if args.output_file
        else results_dir
        / f"proof_autograder_summary_{args.start:03d}_{args.end:03d}_{timestamp}.json"
    )

    log_print("=" * 80)
    log_print("PROOFAUTOGRADER: PROOFBENCH BATCH GRADING")
    log_print("=" * 80)
    log_print(f"Results dir:   {results_dir}")
    log_print(f"ProofBench CSV:{csv_path}")
    log_print(f"Range:         {args.start:03d}-{args.end:03d}")
    log_print(f"Log file:      {log_path}")
    log_print(f"Summary file:  {summary_path}")

    rows = load_proofbench_rows(csv_path)
    problem_ids = collect_problem_ids(results_dir, args.start, args.end)
    if not problem_ids:
        log_print("No problem directories found in requested range.")
        return 1

    log_print(f"\nFound {len(problem_ids)} problem directories to inspect.")

    grader = ProofAutoGraderAgent(
        config_path=args.config,
        prompts_path=args.prompts,
        base_models_path=args.base_models,
        log_file=str(log_path),
    )

    graded_results: List[Dict] = []
    skipped_missing_solution: List[str] = []
    skipped_missing_problem_row: List[str] = []
    skipped_existing: List[str] = []

    for i, problem_id in enumerate(problem_ids, 1):
        log_print(f"\n[{i}/{len(problem_ids)}] {problem_id}")

        row = rows.get(problem_id)
        if not row:
            log_print("  - skipped: problem not found in proofbench.csv")
            skipped_missing_problem_row.append(problem_id)
            continue

        problem_dir = results_dir / problem_id
        solution_path = problem_dir / args.solution_filename
        result_path = problem_dir / "proof_autograder_result.json"

        if not solution_path.exists():
            log_print(f"  - skipped: missing {args.solution_filename}")
            skipped_missing_solution.append(problem_id)
            continue

        if result_path.exists() and not args.overwrite:
            existing = load_existing_result(result_path)
            if existing is not None:
                log_print("  - skipped: existing proof_autograder_result.json")
                skipped_existing.append(problem_id)
                graded_results.append(to_summary_record(existing, result_path))
                continue

        with open(solution_path, "r", encoding="utf-8") as f:
            proposed_solution = f.read()

        grade = grader.grade_submission(
            problem_statement=row.get("Problem", ""),
            ground_truth_solution=row.get("Solution", ""),
            grading_guidelines=row.get("Grading guidelines", ""),
            proposed_solution=proposed_solution,
        )

        problem_result = {
            "problem_id": problem_id,
            "status": "graded" if grade.get("points") is not None else "parse_failed",
            "points": grade.get("points"),
            "points_text": grade.get("points_text"),
            "normalized_score": grade.get("normalized_score"),
            "passed": grade.get("passed", False),
            "parse_source": grade.get("parse_source"),
            "usage": grade.get("usage"),
            "reasoning": grade.get("reasoning"),
            "raw_response": grade.get("raw_response"),
            "solution_file": str(solution_path),
            "graded_at": datetime.now().isoformat(),
        }

        write_json(result_path, problem_result)
        graded_results.append(to_summary_record(problem_result, result_path))

        points = problem_result.get("points")
        if points is None:
            log_print("  - result: parse_failed")
        else:
            log_print(f"  - result: {points}/7 (passed={problem_result['passed']})")

    scored = [r for r in graded_results if isinstance(r.get("points"), int)]
    pass_count = sum(1 for r in scored if r.get("passed"))
    avg_points = (sum(r["points"] for r in scored) / len(scored)) if scored else None

    summary = {
        "results_dir": str(results_dir),
        "proofbench_csv": str(csv_path),
        "config": args.config,
        "prompts": args.prompts,
        "base_models": args.base_models,
        "range": {"start": args.start, "end": args.end},
        "total_problem_dirs": len(problem_ids),
        "graded_records": len(graded_results),
        "scored_records": len(scored),
        "pass_count_ge_6": pass_count,
        "avg_points": avg_points,
        "skipped_missing_solution": skipped_missing_solution,
        "skipped_missing_problem_row": skipped_missing_problem_row,
        "skipped_existing": skipped_existing,
        "results": graded_results,
        "generated_at": datetime.now().isoformat(),
    }

    write_json(summary_path, summary)

    log_print("\n" + "=" * 80)
    log_print("GRADING COMPLETE")
    log_print("=" * 80)
    log_print(f"Graded records:      {len(graded_results)}")
    log_print(f"Scored records:      {len(scored)}")
    log_print(f"Pass count (>=6/7):  {pass_count}")
    log_print(f"Average points:      {avg_points if avg_points is not None else 'N/A'}")
    log_print(f"Summary:             {summary_path}")
    log_print(f"Run log:             {log_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
