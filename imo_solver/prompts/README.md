# Prompts

Prompt templates mapped to agent roles.

## Files

- `momus_prompts.yaml`: prompts for Momus pipeline roles.
- `huang_yang_prompts.yaml`: prompts for the Huang-Yang pipeline from previous work ([arXiv:2507.15855](https://arxiv.org/abs/2507.15855)).
- `proof_autograder_prompts.yaml`: dedicated prompts/templates for `ProofAutoGraderAgent` from IMO-Bench ([imobench.github.io](https://imobench.github.io/)).

## Notes

- Pair prompts with matching config family (`momus_*` with Momus config, etc.).
- Keep prompt path explicit via `--prompts` in all runs.
