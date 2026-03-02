# imo_solver Package

Core Python package for the Momus paper implementation.

## Main Entry Points

- `cli.py`: powers `imo-solve`, `imo-parallel`, `imo-test`.
- `agents/`: solver pipeline implementations.
- `config/`: role/model execution configs.
- `prompts/`: prompt templates.
- `runners/`: parallel and test runners.
- `utils/`: config loading, API routing, logging.

## Quick Usage

```bash
imo-solve imo24SL/A1.md \
  --agent momus \
  --config imo_solver/config/momus_config.yaml \
  --prompts imo_solver/prompts/momus_prompts.yaml
```
