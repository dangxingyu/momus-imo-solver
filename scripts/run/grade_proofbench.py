#!/usr/bin/env python3
"""
Compatibility wrapper for ProofBench grading.

Delegates to grade_proofbench_with_proofautograder.py.
"""

from grade_proofbench_with_proofautograder import main


if __name__ == "__main__":
    raise SystemExit(main())
