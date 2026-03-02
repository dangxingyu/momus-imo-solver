# Configs

All runtime configs for agents and experiments.

## Stable Configs

- `momus_config.yaml`: default Momus config.
- `huang_yang_config.yaml`: baseline config.
- `proof_autograder_config.yaml`: dedicated config for `ProofAutoGraderAgent`.
- `base_models_config.yaml`: shared model registry.

## Example Experiment Configs

- `momus_exp_gemini3_flash_depth3_config.yaml`
- `momus_exp_gemini3_pro_depth3_config.yaml`
- `momus_exp_gemini25pro_native_config.yaml`

## Notes

- Current kept configs are Gemini-native (`provider: gemini`).
- Keep `--config` explicit in command lines for reproducibility.
