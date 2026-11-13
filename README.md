# MathPalette

323 collected questions, 1,140 Special variants, and 1,463 image-text samples. Only normal Collect records are included. Original question IDs, questions, answers, and collection dates are retained.

## Files

- `MathPalette_Dataset/dataset.jsonl`: one record per question.
- `MathPalette_Dataset/samples.jsonl`: one record per model input.
- `MathPalette_Dataset/metadata.json`: dataset counts, branches, sources, and rendering environment.
- `MathPalette_Dataset/SHA256SUMS`: hashes of all formal dataset files except the checksum list itself.
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

Results are individual JSON files in `results/deepseek/`, `results/qwen/`, or `results/minimax/`. The root `results/` directory is tracked by Git and also contains the existing Gemini results in `results/gemini/`. Use `--output-dir PATH` for another run. Received responses are skipped on restart. Each request has a 640-second total deadline. A timeout is recorded and the sample is skipped without retry, including on restart. Other retryable network or service errors retain the limit of three recorded attempts per input across restarts. Use a new output directory after changing the data or model settings.

The published MiniMax snapshot in `results/minimax/` contains one final response for each of the 1,463 sample IDs: 1,462 responses contain both reasoning and an answer; `Plane563_original` retains its original `finish_reason="length"` response with `content=null`. Historical attempts and retry flags have been removed from this final snapshot. The original response fields and token usage are preserved.

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

All formal PNGs were rendered from these classes. Drawing details are in [DRAWING_PROTOCOL.md](DRAWING_PROTOCOL.md); source notices and licenses are in [MathPalette_Dataset/ATTRIBUTION.md](MathPalette_Dataset/ATTRIBUTION.md).

## Dataset schema and integrity

Only normal Collect records (`status="collected"`, `special_case=false`, no pending review) are included. Special slots and counts match the retained Collect record, and original question IDs are preserved.

- `dataset.jsonl`: one question per line (`id`, `source_dataset`, `question`, `answer`, `answer_type`, `choices` where applicable, `branch`, `script`, `approval`, `collection`, `special_variants`, `image`).
- `samples.jsonl`: one model input per line. IDs such as `Ana01_original` and `Ana01_C01` share `question_id`, `question`, `answer`, and `choices`; shared image files do not merge sample identities.
- `answer_type` is `choice`, `number`, `expression`, or `text`. Choice answers use option letters; other answers retain their approved values and units.

```python
import json
from pathlib import Path

root = Path("MathPalette_Dataset")
samples = [json.loads(line) for line in (root / "samples.jsonl").read_text(encoding="utf-8").splitlines()]
sample = samples[0]
print(sample["id"], sample["question"], root / sample["image"])
```

Verify file integrity with:

```sh
(cd MathPalette_Dataset && shasum -a 256 -c SHA256SUMS)
```
