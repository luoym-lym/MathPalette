# Data sources

These candidates originate from **MathVerse**, testmini split, **Vision Dominant** version.

- Official project: https://github.com/ZrrSkywalker/MathVerse
- Official metadata snapshot: https://raw.githubusercontent.com/ZrrSkywalker/MathVerse/937b090597aeafb8e82b35d310a4bc5b9e2ea29d/data/testmini.json
- Official image dataset: https://huggingface.co/datasets/AI4Math/MathVerse
- Downloaded image archive: https://huggingface.co/datasets/AI4Math/MathVerse/resolve/3bc86196678bad115a923d2851c6821dbe235939/images.zip

Metadata SHA-256: `e212dd9c54a048b716cd41c14890b505e6f6b4a878fe4d3e43c7911579a59230`.
Image archive SHA-256 (matching the published LFS digest): `40de79d29048e7a8d37e3307cd2ca0f2e94001167e3a395167c4ee4f6fb58f92`.

At initial packaging, the 788 official Vision Dominant problems were matched against the MathVerse problems already in MathPalette. Excluding 57 distinct already-collected parent problems produced 731 candidates. The historical packaging baseline was `558a6e03e651c0738f3a7dbce23c0bfeff8a5c02`. These are historical source/deduplication counts, not current pending or formal totals. Current pending records come from `index.jsonl`, decisions from `review_state.json`, and formal data and rules follow the local `master` branch. Do not restore completed or deleted candidates from the packaging snapshot.

Each candidate preserves the official `problem_index`, `sample_index`, upstream source label, original English question/answer, and original image hash in its provenance. `source_key` uses the sample index (`testmini:<sample_index>`), while the candidate ID uses the parent problem index. Source images are unchanged. Redrawn figures, adapted questions/answers, and verification evidence are MathPalette review materials and are explicitly distinguished from the source records.
