# MathVision review-workbench import validation

Scope: import the final 696 retained MathVision questions as pending candidates on
`review/mathverse-workbench`. The 24 exclusions are ledger records only. No real
Pass/Delete decision was executed by this integration.

## Preserved data

- Original category counts: combinatorial geometry 296, transformation geometry
  160, solid geometry 240. Frozen-scene target protocols: 429 PlaneGeometry and
  267 SolidGeometry.
- Independent audit compared 3,480 primary and 2,641 supplemental artifacts to
  the authoritative final packages, all byte-identical. The 2,243 execution
  inputs match the source bytes; reference PNG/SVG files are not execution inputs.
- All existing formal branch files, `dataset_tools`, approvals, source notes,
  formal index and MathVerse package/history remain unchanged from `de156d1d`.
- All new rows explicitly remain pending and `user_approved=false`. Historical
  scene statuses and Agent verification records are not human approval.

## Checks completed

- New multi-source tests: 7/7 passed, including isolated actual Pass for all five
  source-category/target-protocol combinations, Delete, restart/idempotent replay,
  stale fingerprints, missing source interpreter rollback, and real HTTP routes.
- Source-specific launcher tests: 3/3 passed. `launch_workbench.py --check`
  recognizes the current MathVision environment without claiming MathVerse also
  matches. Both Windows entrypoints honor an explicit `MATHPALETTE_PYTHON`.
- Frontend pure-logic/static tests: 13/13 passed, including source/category
  filters, distinct MV/MVI identities, ambiguous numeric jumps, source options,
  and readable evidence for all 696 MathVision rows.
- Independent read-only API/service audit: all 696 details and 1,392 image hash
  responses passed; all 24 excluded IDs are absent from the queue. Existing
  combined progress remains 852 pending (696 MathVision + 156 MathVerse),
  90 passed and 485 deleted; no real state changed.
- Independent isolated crash recovery passed after approval-file write, candidate
  move and committed transaction. Replaying the same request is safe.
- `python -B dataset_tools/catalog.py check` passed for the unchanged 287 formal
  questions (70 Analytics, 139 PlaneGeometry, 78 SolidGeometry).

## Full frozen reproduction

**Passed: 696/696 questions, 2,088 isolated renders, all exact bytes and pixels.**

The full import validator was run with `--formal --twice`: every candidate was
rendered twice in clean isolated layouts, then prepared with a temporary formal
ID and rendered with no candidate directory. Its finalized machine-readable
report is `review_candidates/mathvision/import_render_validation.json`.

## Limits and honest regression status

The complete pre-existing Python suite was run in the available MathVision
Python 3.12 environment. Existing MathVerse exact-pixel cases do **not** pass
there: its frozen references require its distinct Python 3.13.9 / NumPy 2.5.3 /
Matplotlib 3.11.2 / FreeType 2.14.3 environment. The same failures were established
on the unchanged baseline, and downstream MathVerse transaction-injection tests
stop at that pixel guard before their intended stage. The run reported 24 test
methods, 11 failure subcases, 2 errors, and 2 existing no-pending-solid skips;
all new MathVision tests passed. The extra launcher tests were run separately.
Do not describe this as a fully passing legacy suite or loosen pixel checks to
make it pass. The original MathVerse pins and source assets are unchanged; use
`MATHPALETTE_MATHVERSE_PYTHON` for its dedicated interpreter.

Real Chromium browser testing was not run: the executor denied browser socket
creation, and a scoped escalation failed environment setup. Browser regressions
are included for a capable local environment. Real loopback HTTP and Node logic
checks did run and pass.

Formal MathVision standalone scripts are validated. Existing Special variant
adapters and legacy stock geometry tools were not extended or validated for the
new native semantic rendering extensions; use the formal row's `script` for exact
reproduction. This import does not claim new Special variant compatibility.

New code passes the whitespace check. Historical SVG whitespace is intentionally
preserved with the source bytes, not normalized to satisfy a text-style check.
