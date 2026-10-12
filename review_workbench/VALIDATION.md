# MathVerse original review: validation record

Validation date: 2026-10-11 (UTC). This is a local review application, not a hosted service. All destructive test actions were executed in isolated repository copies. The publishable worktree retains all **731 unapproved candidates** and the original **142 formal questions**; its formal datasets, source notes, approvals and root catalog remain byte-identical to the user baseline.

## Candidate coverage

- Official Vision Dominant pool: 788; 57 already collected parent problems excluded; 731 distinct candidates remain.
- Rendering branches: 436 PlaneGeometry, 178 Analytics, 117 SolidGeometry.
- All 731 retain original source images, English source/current questions and answers, redraw PNG/SVG, frozen inputs, code, adaptation notes and independent verification evidence.
- Candidate and promoted scripts reproduce all 731 images with exact RGB pixel equality in the pinned environment. Formal promotion was independently tested without the review directory present.
- All 731 pass formal answer/schema/path checks. 37 option-label formatting inconsistencies found during integration were normalized without changing option values, order or correct answers; pre-normalization text is retained in provenance.
- Answer-consistency labels resolve choice letters to values. Uncertain expression equivalence is shown for manual confirmation rather than automatically declared equal.

## Real cloud-browser testing

Three rounds were performed with Chromium on the cloud Linux desktop and the actual HTTP backend, using two independent test copies and final resource refreshes. This was not merely an HTML screenshot or a mocked backend.

1. Initial display: full source/redraw images, source zoom at 150% and close, scrolling question/choices/answer/verification/adaptation panels, Pass busy feedback and next-question transition, Delete confirmation/cancellation and actual deletion.
2. Interrupted and repeated flows: refresh persistence; passed/deleted history with disabled actions; source/branch navigation; empty search and recovery; stale-content fingerprint rejection followed by reload; stopped server and same-request retry after restart; rapid double-click Pass; navigation while a previous Pass is pending; last item in a pending filter; final history item in the all-status filter.
3. Final code: previously malformed-choice candidate MV0339 successfully promoted to Plane72 in a fresh copy; Solid MV0635 promoted to Solid26; refreshing during its in-flight Pass recovered the saved result without another import. Full formal catalog validation passed after the browser mutations.

Filesystem checks confirmed that deleting a test candidate removed its own directory while preserving other candidates and shared resources. A failed stale-content action did not add a formal question. The browser showed immediate pending/disabled states, and successful operations advanced or showed durable history as appropriate. No application-origin console errors were found in the final round; cloud-browser extension diagnostics were separate from this application.

## Automated and independent checks

- 11 backend tests: seven renderer families, full formal validation, unchanged old approvals, dependency/image tamper rejection, invalid existing formal content rejection, external edits during rendering, recovery, concurrent numbering, idempotency and HTTP protections.
- Independent hard-exit fault injection at nine transaction points: restart restored exact pre-operation file bytes for uncommitted operations; committed decisions remained committed.
- Concurrent processes assigned distinct formal IDs. Same request IDs replayed one result. Conflicting IDs and stale fingerprints were rejected.
- Same-origin/Host/custom-header enforcement rejected four invalid HTTP write classes without modifying candidates.
- Delete scope comparison changed only the selected item plus the candidate index and minimal decision state; no other candidate, formal item or shared dependency was deleted.
- Seven frontend core tests cover all 731 verification/evidence shapes, safe text handling and state helpers. JavaScript syntax and DOM references were checked.
- Existing answer-schema/catalog-lock tests: 9 passed. Existing Plane and Solid workbench suites: 8 and 6 passed. Promotion compatibility suite: 3 passed.
- A separate set of 13 synthetic automated-browser scenarios is supplied for future regression use but was **not executed here** because the sandbox could not launch its own headless browser. The real cloud-browser tests above were executed separately and are not presented as that automated suite.

Final combined Python discovery: **20/20 passed**, followed by **7/7 frontend core tests**. Legacy compatibility additionally passed 90 fail-closed code/dependency negative checks and seven old-progress protection checks.

## Performance observations

Measured on the cloud test machine with the pinned Python environment and 731 candidates:

- Candidate list: approximately 8–15 ms
- Current-item detail: approximately 14–21 ms
- Delete backend: approximately 31–36 ms; one actual browser deletion displayed the next item within 185 ms
- Pass: approximately 2.52–2.67 seconds, including one isolated redraw and complete formal catalog verification

These are measurements, not guarantees for every Windows machine. The implementation avoids all-candidate image hashing/rendering and Git/AST scanning during each decision. Source-note JSON is loaded once per full catalog validation rather than once per formal question; approval and dependency checks still run for every formal item.

## Existing workbench compatibility

Independent testing covered all 873 originals (142 existing plus 731 promoted candidates) through the three native workbench no-op paths with pixel equality. Seven rendering families passed representative Special operations and replay. Both new Analytics families passed all six Base operations with deterministic changed pixels; altered scene/renderer dependencies were detected.

The repository's legacy stock-only geometry helper is deliberately unchanged because its code is part of existing approval fingerprints. Extended-object questions must be reproduced through the formal row's `script`, not that old low-level stock-only helper. The README gives the supported invocation.

Legacy variant compatibility uses an explicit fail-closed version registry rather than rewriting user approvals or recipes. The 184 old Base and 95 old Special variants were replayed with identical pixels. Their existing PNGs and recipe records are preserved; compressed PNG streams may differ without pixel changes. The compatibility code only recognizes the explicitly audited version/dependency combinations and rejects altered dependencies or unknown code versions.

## Boundaries

- Windows launcher/path/locking/publishing branches were reviewed and the interpreter-selection launcher was exercised, including a starting Python with no third-party imports. A native Windows desktop double-click was **not** performed in this Linux cloud environment.
- Passing automated mathematical or rendering checks is not user approval. No genuine candidate was approved or deleted as part of these tests.
- No automatic Git commit, push or merge is performed by the local application. After local review, normal Git tools remain under the user's control.
