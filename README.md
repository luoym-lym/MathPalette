# MathPalette

323 collected questions, 1,140 Special variants, and 1,463 image-text samples. Only normal Collect records are included. Original question IDs, questions, answers, and collection dates are retained.

## Files

- `MathPalette_Dataset/dataset.jsonl`: one record per question.
- `MathPalette_Dataset/samples.jsonl`: one record per model input.
- `MathPalette_Dataset/images/`: 1,456 distinct PNG files shared by the samples.
- `MathPalette_Dataset/questions/`: one Python class per question, including its Special drawings.
- `MathPalette_Dataset/drawing.py`: shared drawing tools.
- `MathPalette_Dataset/infer_deepseek.py`: direct DeepSeek API calls.
- `MathPalette_Dataset/infer_qwen38_max_0902.py`: direct Qwen API calls.
- `MathPalette_Dataset/check_api_key.py`: a small authentication check.

## Install

Use Python 3.13.9 for exact drawing reproduction. The inference scripts require Python 3.11 or newer.

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Keep the existing project `.env`. The scripts read `DEEPSEEK_API_KEY` and `QWEN_38_MAX_0902_API_KEY`; environment variables take priority.

## Run inference

```sh
.venv/bin/python MathPalette_Dataset/infer_deepseek.py --limit 1
.venv/bin/python MathPalette_Dataset/infer_qwen38_max_0902.py --limit 1
```

Remove `--limit 1` to process all samples. Each script reads a PNG and its question, sends a non-streaming request, and saves the returned `reasoning_content`, `content`, usage, and finish reason. No grading or answer-based retry is performed.

DeepSeek uses `deepseek-flash` with thinking enabled and effort `max`. Qwen uses `qwen3.8-max-0902` with thinking enabled and effort `xhigh` at `https://maas.qianwenaiapi.com/compatible-mode/v1`. Neither script sends an output token limit. Both use the same English MathVision instruction followed by the original question, without a system message.

Results are individual JSON files in `results/deepseek/` or `results/qwen/`. The root `results/` directory and its result files are included in Git version control. Use `--output-dir PATH` for another run. Received responses are skipped on restart. Each input has at most three recorded attempts, including earlier runs; each request has a 240-second total deadline. Use a new output directory after changing the data or model settings.

Missing reasoning or answer content is saved as missing, reported in the terminal, and stops the run. Returned reasoning and answers are stored without translation or rewriting. A local timeout does not confirm that the provider stopped computing or billing.

Optional authentication check, without model inference:

```sh
.venv/bin/python MathPalette_Dataset/check_api_key.py deepseek
.venv/bin/python MathPalette_Dataset/check_api_key.py qwen
```

The check uses `GET /models`. A gateway that does not implement that route may reject it even when its chat endpoint is available. It does not test image support or reasoning output.

## Draw a question

```sh
.venv/bin/python MathPalette_Dataset/questions/Ana01.py .runtime/Ana01.png
.venv/bin/python MathPalette_Dataset/questions/Plane25.py .runtime/Plane25_C01.png --variant C01
```

All formal PNGs were rendered from these classes. Drawing details are in [DRAWING_PROTOCOL.md](DRAWING_PROTOCOL.md); data fields and licenses are described in the [dataset README](MathPalette_Dataset/README.md) and [attribution notice](MathPalette_Dataset/ATTRIBUTION.md).
