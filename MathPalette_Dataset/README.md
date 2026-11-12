# MathPalette dataset

323 questions, 1,140 Special variants, and 1,463 image-text samples use 1,456 distinct PNG files. Shared images do not merge sample identities.

Only normal Collect records are included: `status="collected"`, `special_case=false`, and no pending review. Special slots and counts match the retained Collect record. Original question IDs are kept.

## Records

- `dataset.jsonl`: one question per line, including its ID, branch, source, question, answer, answer type, choices where applicable, drawing script, original image, and Special images.
- `approval`: original reviewer and approval date. Historical instruction quotes are omitted.
- `collection`: original Collect date, status, accepted count, and slots.
- `special_variants`: slot IDs, original Pass dates, image paths, and SHA-256 values.
- `samples.jsonl`: one model input per line. IDs such as `Ana01_original` and `Ana01_C01` share the same `question_id`, question, answer, and choices.
- `image_manifest.jsonl`: image hashes, sizes, dimensions, RGBA hashes, and referencing sample IDs.
- `metadata.json`: dataset counts, sources, drawing environment, and artifact hashes.
- `SHA256SUMS`: hashes of all dataset files except the checksum list itself.

Answer types are `choice`, `number`, `expression`, or `text`. Choice answers are option letters; other answers retain their approved values and units.

```python
import json
from pathlib import Path

root = Path("MathPalette_Dataset")
samples = [json.loads(line) for line in (root / "samples.jsonl").read_text(encoding="utf-8").splitlines()]
sample = samples[0]
print(sample["id"], sample["question"], root / sample["image"])
```

## Code

Each file in `questions/` contains one class with original and Special draw methods. All figures use `drawing.py`; temporary output stays outside the formal dataset directory. See the [drawing protocol](../DRAWING_PROTOCOL.md).

The three inference scripts independently load samples, call their model endpoint, and save reasoning and answers. `check_api_key.py` is the only additional API utility. Usage is in the [project README](../README.md).

Verify file integrity from this directory with `shasum -a 256 -c SHA256SUMS`. Source notices and retained licenses are listed in [ATTRIBUTION.md](ATTRIBUTION.md).
