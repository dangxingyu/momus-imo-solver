# Agents

Pipeline implementations used by this repository.

## Key Files

- `momus_agent.py`: top-level Momus pipeline (recommended default).
- `momus_core_agent.py`: core multi-stage logic.
- `momus_base_agent.py`: base loop with conjecture handling.
- `momus_post_enhancement_agent.py`: optional enhancement pass.
- `huang_yang_agent.py`: Huang-Yang pipeline from previous work ([arXiv:2507.15855](https://arxiv.org/abs/2507.15855)).
- `proof_autograder_agent.py`: ProofAutoGrader from IMO-Bench ([imobench.github.io](https://imobench.github.io/)) with IMO-style 0-7 grading (`<points>N out of 7</points>`).
- `base_agent.py`: shared agent interface and lifecycle.

## Typical Selection

- Paper runs: `momus`
- Previous-work pipeline runs: `huang_yang`
- Proof grading runs: `proof_autograder`
