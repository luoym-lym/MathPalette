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
- `MathPalette_Dataset/infer_minimax.py`: direct MiniMax Token Plan API calls.
- `MathPalette_Dataset/check_api_key.py`: a small authentication check.

## Install

Use Python 3.13.9 for exact drawing reproduction. The inference scripts require Python 3.11 or newer.

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Preserve the existing project `.env` credentials. The scripts read `DEEPSEEK_API_KEY`, `QWEN_38_MAX_0902_API_KEY`, and `MINIMAX_API_KEY`; environment variables take priority. The MiniMax Token Plan key may be added to the project `.env` when explicitly requested by the user.

## Run inference

```sh
.venv/bin/python MathPalette_Dataset/infer_deepseek.py --limit 1
.venv/bin/python MathPalette_Dataset/infer_qwen38_max_0902.py --limit 1
.venv/bin/python MathPalette_Dataset/infer_minimax.py --limit 1
```

Remove `--limit 1` to process all samples. Each script processes at most five samples concurrently, reads a PNG and its question, sends a non-streaming request, and saves the returned `reasoning_content`, `content`, usage, and finish reason. No grading or answer-based retry is performed.

DeepSeek uses `deepseek-flash` with thinking enabled and effort `max`. Qwen uses `qwen3.8-max-0902` with thinking enabled and effort `xhigh` at `https://maas.qianwenaiapi.com/compatible-mode/v1`. MiniMax uses `MiniMax-M3.1-Flash` through Token Plan with always-on thinking and the highest effort, `max`, at `https://api.minimax.cn/v1`. Set `MINIMAX_BASE_URL=https://api.minimax.io/v1` for an international account. See the [official OpenAI-compatible API documentation](https://platform.minimax.cn/docs/api-reference/text-openai-api). None of the scripts sends an output token limit. All use the same English MathVision instruction followed by the original question, without a system message.

Results are individual JSON files in `results/deepseek/`, `results/qwen/`, or `results/minimax/`. The root `results/` directory and its result files are local only and ignored by Git. Use `--output-dir PATH` for another run. Received responses are skipped on restart. Each request has a 640-second total deadline. A timeout is recorded and the sample is skipped without retry, including on restart. Other retryable network or service errors retain the limit of three recorded attempts per input across restarts. Use a new output directory after changing the data or model settings.

Missing reasoning or answer content is saved as missing, reported in the terminal, and stops new requests; requests already in flight finish and are saved. Nonretryable provider errors also stop new requests, while a timeout only skips the affected sample. Returned reasoning and answers are stored without translation or rewriting. A local timeout does not confirm that the provider stopped computing or billing.

Optional authentication check, without model inference:

```sh
.venv/bin/python MathPalette_Dataset/check_api_key.py deepseek
.venv/bin/python MathPalette_Dataset/check_api_key.py qwen
.venv/bin/python MathPalette_Dataset/check_api_key.py minimax
```

The check uses `GET /models`. A gateway that does not implement that route may reject it even when its chat endpoint is available. It does not test image support or reasoning output.

## Draw a question

```sh
.venv/bin/python MathPalette_Dataset/questions/Ana01.py .runtime/Ana01.png
.venv/bin/python MathPalette_Dataset/questions/Plane25.py .runtime/Plane25_C01.png --variant C01
```

All formal PNGs were rendered from these classes. Drawing details are in [DRAWING_PROTOCOL.md](DRAWING_PROTOCOL.md); data fields and licenses are described in the [dataset README](MathPalette_Dataset/README.md) and [attribution notice](MathPalette_Dataset/ATTRIBUTION.md).
