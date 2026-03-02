# Run Scripts

Command-line scripts for larger experiment runs.

## Included Scripts

- `run_gemini3_single.py`: one problem, one run.
- `run_momus_parallel_batch.py`: parallel ProofBench Advanced batch (ProofBench / IMO-Bench).
- `run_momus_on_proofbench.py`: sequential ProofBench Advanced run (ProofBench / IMO-Bench).
- `run_imo_level_batch.py`: IMO-level CSV batch run.
- `grade_proofbench.py`: compatibility entry point for ProofBench grading.
- `grade_proofbench_with_proofautograder.py`: grade saved `solution.txt` files against ProofBench references using `ProofAutoGrader` from IMO-Bench ([imobench.github.io](https://imobench.github.io/)).

Run `--help` on each script to see arguments.
