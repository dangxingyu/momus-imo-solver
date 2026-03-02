# Runners

Reusable execution helpers used by CLI.

## Files

- `parallel_runner.py`: run multiple agent instances in parallel.
- `test_runner.py`: run problem sets and record summary metrics.

Most users should call these through CLI commands (`imo-parallel`, `imo-test`).
`imo-test` expects either `--single <file>` or `--problems <dir>` and scans `.txt`/`.md` files.
