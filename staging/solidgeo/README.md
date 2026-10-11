# Isolated SOLIDGEO review candidates

`candidates.jsonl` is the complete 168-candidate review dataset. It is not a formal dataset and does not allocate `SolidNN` IDs. The 27 excluded source IDs are listed in `manifest.json`; their records, images and scripts are absent.

Each candidate directory contains its unchanged original image, current review PNG, frozen scene, a small reproduction entry point and construction/migration provenance. Shared preview-only helpers reproduce unsupported legacy scenes without importing the historical source bank. Current-compatible scenes use the repository's unchanged SolidGeometry renderer and protocol.

Question/answer content lives in `candidates.jsonl`, including the unmodified source record, canonical current answer, independently audited conclusion/proof, and all choice mappings. Scene JSON contains no duplicated question, answer or user-review state. Source-answer equality is never treated as independent verification.

`pass_eligible` means technical readiness for the user's explicit Pass. `pass_blockers` explains failures precisely. A historical content review, current renderer validation, and a user's approval are separate facts. Target previews are generated in Python 3.13.9, Matplotlib 3.11.2, NumPy 2.5.3 and Pillow 12.3.0. Per-candidate provenance records original and current hashes, changed-pixel metrics, deterministic PNG/SVG checks and actual visual-inspection scope. Historical pixel equality is not assumed.

Payload SHA-256 values bind each reviewed original, preview, scene, script and provenance. The verification content fingerprint binds the reviewed question, canonical answer, answer type and choices. The workbench must revalidate these before Pass and must compare its live import render with the exact displayed preview.

To reproduce one candidate without overwriting the review asset:

```sh
python -B staging/solidgeo/candidates/1748/draw.py .runtime/solidgeo-reproduced/1748.png
```

The preparation entry point is `dataset_tools/prepare_solidgeo_review.py`. It reads the retained source collection and independent audit, refuses incorrect scope or an unpinned environment, and writes only staging. Rebuilding invalidates prior review state and must not be run after decisions exist. Actual visual review is recorded separately with exact image hashes; the recording command itself does not perform an inspection.

See [ATTRIBUTION.md](ATTRIBUTION.md) for upstream attribution and CC BY-NC 4.0 restrictions.
