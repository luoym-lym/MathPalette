# MathVerse offline candidate review

This package contains 731 unapproved candidates. Agent verification is not user Pass. The existing 142 formal questions are separate and unchanged by packaging.

## Layout and identity

- `index.jsonl`: the only candidate listing. Every file path is relative to the **repository root**, not this folder.
- `items/MV####/candidate.json`: the same complete record for one question. `MV####` is its original MathVerse problem index padded to four digits; `source_key=testmini:<sample_index>` is preserved. `legacy_id` retains its staging identifier.
- Each item contains source PNG, redrawn PNG/SVG, frozen scene, portable `redraw.py`, original author entry `source_redraw.py`, source/adaptation evidence and verification. `source_redraw.py` is byte-identical historical evidence for the old source layout; execute `redraw.py` instead.
- `shared/`: seven isolated renderer families, exact machine protocols and a small dispatcher. Do not replace these with a single stock renderer: arrows, curved regions, polygon holes, ellipse handling and Analytics wrappers differ.
- Deleting a candidate removes only its `items/MV####/` directory and index row. Shared renderer dependencies are intentionally independent of other candidate directories.

## Offline use

Install Python 3.13.9 and the pinned requirements before disconnecting. All question assets and executable rendering inputs are local. No network, source image tracing, CDN or cloud staging path is needed to review or redraw.

From the repository root:

    python -B review_candidates/mathverse/items/MV0001/redraw.py .runtime/example.png
    python -B review_candidates/mathverse/items/MV0001/redraw.py .runtime/example.svg
    python -B review_candidates/mathverse/validate_package.py

Without an output argument, scripts write to `.runtime/mathverse_redraw/`, never the source image, frozen scene or checked-in reference PNG. Default Python or different Matplotlib/FreeType versions can change rasterized text pixels even if geometry is unchanged. Exact pixel verification requires the pinned environment; the source/reference PNG is never silently regenerated to hide differences.

## Answers and evidence

`original_question` and `original_answer` preserve the source. `question`, `answer`, `answer_type`, and optional `choices` describe the candidate. `candidate_answer_value` resolves a candidate choice letter to text; `source_answer_value` resolves original source options where available.

`answer_consistency.status` is `consistent`, `corrected`, or `needs_manual_confirmation`. Normalization evidence and explicit answer corrections are distinguished from uncertain mathematical equivalence. String differences do not establish an incorrect source answer. Per-item provenance retains the complete original derivation, adaptation explanation, visual observations and the original checks' limitations. Verification evidence is agent work, not a user approval.

## Formal import contract

`promotion.prepare(repository_root, candidate_row, formal_id)` is a pure preparation function. It returns `(formal_row, writes, source_notes)` without writing or approving anything. `writes` maps repository-relative paths to bytes; `formal_row` paths and `runtime_dependencies` are branch-relative. The caller must verify a current user Pass and commit the transaction safely.

Formal scripts, class IDs and frozen scene IDs are renamed together. Images keep identical bytes. Necessary renderer dependencies are copied into the formal branch's `dataset_generator/mathverse_renderers/<family>/`; no formal script depends on a candidate folder. Extra solid model construction evidence goes to source notes, while formal scene fields follow the root catalog schema. Runtime dependencies must be included in the formal content fingerprint.

## Rebuilding

`build_package.py /path/to/audited/staging` reconstructs the package from its original audited staging tree. This is a packaging tool, not needed for offline review or reproduction. It does not import candidates into the formal bank and does not create approval records.

Use `validate_package.py --formal` to additionally prepare every candidate with a temporary formal ID in isolated temporary directories and compare all promoted redraws against the reference pixels. This does not add rows, approvals or files to the formal branches. `--output PATH` chooses the runtime validation report.

## Source attribution

See [SOURCES.md](SOURCES.md) for the official dataset, fixed metadata/image revisions and per-item identity mapping.
