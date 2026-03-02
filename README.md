# Momus IMO Pipeline

Official implementation of the paper **"Escaping the Cognitive Well: Efficient Competition Math with Off-the-Shelf Models"** ([arXiv:2602.16793](https://arxiv.org/abs/2602.16793)).

This repository contains the Momus inference pipeline for IMO-style proof problems, plus a Huang-Yang baseline agent and reproducible experiment configs.

## Quick Start

### 1. Install

```bash
pip install -e .
```

### 2. Set API key (native Gemini)

```bash
export GEMINI_API_KEY="..."
```

Or place the key in `gemini.key` (also supports legacy `gemini_key.txt`).

### 3. Run one problem (Momus)

```bash
imo-solve imo24SL/A1.md \
  --agent momus \
  --config imo_solver/config/momus_config.yaml \
  --prompts imo_solver/prompts/momus_prompts.yaml
```

### 4. Run in parallel

```bash
imo-parallel imo24SL/A1.md -n 4 \
  --agent momus \
  --config imo_solver/config/momus_config.yaml \
  --prompts imo_solver/prompts/momus_prompts.yaml
```

## Agents

- `momus`: main paper pipeline.
- `huang_yang`: baseline solver pipeline.

## Configs

- `imo_solver/config/momus_config.yaml`: default Momus config.
- `imo_solver/config/huang_yang_config.yaml`: baseline config.
- `imo_solver/config/momus_exp_gemini3_flash_depth3_config.yaml`: Gemini 3 Flash example.
- `imo_solver/config/momus_exp_gemini3_pro_depth3_config.yaml`: Gemini 3 Pro example.
- `imo_solver/config/momus_exp_gemini25pro_native_config.yaml`: Gemini 2.5 Pro native example.
- `imo_solver/config/base_models_config.yaml`: shared native Gemini model definitions.

## Included Dataset

- `proofbench.csv` is included at repository root for ProofBench-based scripts.

## Final Released Results

- Packaged final outputs are in:
  - `release_results/proofbench_momus_final_001_030/`
- Per-problem artifacts include `solution.txt`, solver logs, API logs, metadata, and `proof_autograder_result.json`.
- A provenance table is provided at:
  - `release_results/proofbench_momus_final_001_030/manifest.csv`
- Summary files are under:
  - `release_results/proofbench_momus_final_001_030/summaries/`

## Useful Scripts

```bash
python scripts/run/run_gemini3_single.py --help
python scripts/run/run_momus_parallel_batch.py --help
python scripts/run/run_momus_on_proofbench.py --help
python scripts/run/run_imo_level_batch.py --help
```

## Subdirectory Guides

- `imo_solver/README.md`
- `imo_solver/agents/README.md`
- `imo_solver/config/README.md`
- `imo_solver/prompts/README.md`
- `imo_solver/runners/README.md`
- `imo_solver/utils/README.md`
- `scripts/README.md`
- `scripts/run/README.md`

## Citation

```bibtex
@misc{dang2026escapingcognitivewellefficient,
      title={Escaping the Cognitive Well: Efficient Competition Math with Off-the-Shelf Models},
      author={Xingyu Dang and Rohit Agarwal and Rodrigo Porto and Anirudh Goyal and Liam H Fowl and Sanjeev Arora},
      year={2026},
      eprint={2602.16793},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2602.16793},
}
```
