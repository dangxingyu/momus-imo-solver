# Prompts

Prompt templates mapped to agent roles.

## Files

- `momus_prompts.yaml`: prompts for Momus pipeline roles.
- `huang_yang_prompts.yaml`: prompts for Huang-Yang baseline roles.
- `proof_autograder_prompts.yaml`: dedicated prompts/templates for `ProofAutoGraderAgent`.

## Notes

- Pair prompts with matching config family (`momus_*` with Momus config, etc.).
- Keep prompt path explicit via `--prompts` in all runs.
