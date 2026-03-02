# Agents

Pipeline implementations used by this repository.

## Key Files

- `momus_agent.py`: top-level Momus pipeline (recommended default).
- `momus_core_agent.py`: core multi-stage logic.
- `momus_base_agent.py`: base loop with conjecture handling.
- `momus_post_enhancement_agent.py`: optional enhancement pass.
- `huang_yang_agent.py`: baseline solver.
- `proof_autograder_agent.py`: IMO-style 0-7 proof grader (`<points>N out of 7</points>`).
- `base_agent.py`: shared agent interface and lifecycle.

## Typical Selection

- Paper runs: `momus`
- Baseline runs: `huang_yang`
