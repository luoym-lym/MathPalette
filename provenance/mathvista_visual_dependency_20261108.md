# MathVista visual-dependency revision review

## Scope and review status

This revision covers exactly the 61 newly admitted MathVista items
**Ana71–Ana131**. Ana46, the other 957 formal items, all source images,
source notes, shared drawing code, and accepted Special variants are unchanged.
The follow-up removes only Ana121's three formula labels from its frozen scene
and redraw; its curve samples and axes remain identical. The other 60 scenes
and redraws retain their original hashes.

All 61 prompts were revised. Answers changed for 19 items, answer types for 12,
and choice mappings for 18 (including conversions to/from non-choice answers).
The branch dataset, compatibility classes, and root review index agree.

**The user explicitly accepted these revisions and requested direct submission to the workbench.** The later instruction was:

> 不用审核，你就默认我审核过了。
> 如果我觉得有问题我可以自己在工作台里面调整。你的题目修改之后直接提交到工作台

The initial modification request was not treated as content approval. After the
later explicit acceptance, `question_review.py` recorded a new approval for
Ana71–Ana131 using that exact instruction and the current content fingerprints,
then rebuilt the formal index. Prior approval hashes and timestamps remain in the
companion revision manifest, which links to the complete public ledger at the
base commit rather than duplicating historical user instructions. No historical approval dates or individual Special
Pass/Collect actions were fabricated. The production approval gate is unchanged.

The current Analytics workbench reads `Analytics/dataset.jsonl`; the updated
questions, class metadata, and production-generated `question_bank.jsonl` are
now synchronized and approved.

## Changes

- Remove supplied function formulas, values, and coordinates when they made
  the graph redundant.
- Replace intrinsic or unsupported global questions, rather than merely adding
  “shown in the graph.” Examples include polynomial degree, epigraph infinitude,
  improper-integral convergence, and extrapolated equilibrium/periodicity.
- Preserve mathematical work where the image supports it: derivatives and
  secant slopes, limits and continuity, convexity, symmetry, intervals, area,
  integrals, labelled-curve comparison, and extrema.
- Keep all geometric evidence and the existing rendering style. Ana121's
  formula labels are removed so formula OCR cannot replace reading its curves.

Examples:

| Item | Previous shortcut | Revised visual task |
| --- | --- | --- |
| Ana71 | Absolute-value formula gives both derivatives | Compare the slopes of the displayed branch at two inputs |
| Ana89 | A nonempty epigraph is necessarily infinite | Decide whether a specified point belongs to the actual shading |
| Ana111 | The supplied power determines improper-integral divergence | Determine the sign of a finite integral from the plotted region |
| Ana121 | Formula labels permit OCR; the old crossing test has a narrow margin | Count curves above y=1 at x=4, without formula labels |
| Ana131 | Given constants make substitution immediate | Read the intersection-bounded interval where U lies below E |

## Evidence and checks

The companion JSON records every before/after prompt, answer, visual solution,
removed shortcut, and an alternative graph consistent with the same text but
giving a different answer. Every actual PNG was inspected. An independent
review inspected all 61 PNGs/scenes, checked text-only underdetermination and
solved the revised questions from the graph: **61/61 agreed**, with no remaining
text-only uniquely determined answers found. This is a mathematical/content
audit, not an empirical model-ablation score or a claim that guessing or dataset
memorization is impossible. Solutions and counterfactual formulas are audit
metadata only, not solver prompts.

Commands run:

```
python -X utf8 -B dataset_tools/test_mathvista_visual_dependency.py
python -X utf8 -B dataset_tools/test_answer_schema.py
python -X utf8 -B dataset_tools/test_catalog_concurrency.py
python -X utf8 -B dataset_tools/check_mathvista_visual_redraw.py
python -X utf8 -B dataset_tools/catalog.py check
git diff --check
```

- Visual-revision regression tests: **8 passed** in the formal environment. They bind the semantic audit
  to exact question/image hashes, verify all metadata and preserved assets,
  check the 1,018-record index and verify the current explicit reapproval against preserved previous approval records.
- Existing answer-schema tests: **7 passed**.
- Existing catalog-concurrency tests: **3 passed**.
- Renderer code is compared with the pinned Git baseline using the same
  running interpreter for both sources. Literal question metadata is excluded;
  executable expressions assigned to metadata fields are not ignored.
- The production catalog check passes after explicit user reapproval. The original approval gate is unchanged.
- No paid model calls or model-evaluation logs were created.

## AST compatibility correction

The first checker persisted CPython 3.12 `ast.dump` hashes and incorrectly used
them as a cross-version acceptance gate. This was reproduced: 0/61 mismatches
on 3.12.14 versus 61/61 on 3.13.5, whose dump omits empty fields by default.
Both the regression suite and redraw checker now read the immutable Git
baseline and compare its AST with the revised source in the same interpreter.
Legacy per-item AST hashes remain historical audit data only. Missing baseline
history fails visibly, and new regression cases reject changed drawing code
and side-effectful metadata expressions.

## Follow-up question checks

- Ana121: at x=4, the three ordinates are about 2, 1.386, and 0.602. Exactly two
  exceed 1; the minimum decision margin is about 0.386 units (15 pixels).
  All three formula labels are gone. Every curve coordinate is unchanged.
- Ana110 retains the actual condition f(x)>0 and correct answer `(-4, -1)`.
  Ana131 retains U below E and `(-2, 2)`. Both explicitly request interval
  notation; the review's alternative sign/curve-name quotations were not used.
- Ana111's and Ana126's sign options and Ana127's comparison options are lowercase.
  Their answers and mathematics are unchanged.
- These six refinements were independently checked against the actual images
  and recorded under the user's existing explicit task approval. Previous
  approval hashes/timestamps remain in the manifest's approval history.

## Formal workbench environment

The repository freezes Python 3.13.9, NumPy 2.5.3, Matplotlib 3.11.2,
Pillow 12.3.0, and FreeType 2.14.3. All five versions are now installed and
verified in the repository-supported `.venv`. The existing requirements and
saved recipe environments were not changed. Use the launcher's documented
explicit interpreter selection:

```
export MATHPALETTE_PYTHON="$PWD/.venv/bin/python"
export MPLCONFIGDIR="$PWD/.runtime/mplconfig"
export XDG_CACHE_HOME="$PWD/.runtime/cache"
.venv/bin/python -X utf8 -B dataset_tools/test_mathvista_visual_dependency.py
.venv/bin/python -X utf8 -B dataset_tools/check_mathvista_visual_redraw.py --require-published-pixels
```

The explicit override is important on this Linux host because automatic
interpreter discovery resolves virtualenv symlinks to the base executable.
The workbench launcher has independently accepted the override and exact
required versions. No environment or pixel guard was weakened or spoofed.

The earlier Python 3.12 and 3.13.5 runs were diagnostics, not formal-environment
acceptance. Final integration, rendering, replay, and workbench operations use
the complete pinned environment above.

Formal-environment results:

- All **61/61 current redraws match the published PNG pixels exactly**.
- Baseline comparison matches the declared scope: 60 images are identical;
  Ana121 alone differs because its three formula labels were removed.
- Eight visual-revision, seven answer-schema, three catalog-concurrency, and
  seven Analytics Special-case regression tests pass.
- The full isolated integrity suite passes: launcher environment selection,
  approval rejection, Pass/Collect/reopen/delete, index synchronization, and
  cold recovery. Its synthetic review actions do not alter real user records.
- The production catalog check passes with 1,018 questions and 1,132 Special
  variants across all branches.
- Official replay of the 146 accepted Analytics variants: **126 passed; 20
  blocked by an existing Linux path incompatibility**. The affected frozen
  classes use `ROOT/'..\\mathverse_renderers\\runtime.py'`, which Linux treats as
  a literal filename. Affected slots are Ana49 C01–C05, Ana54 C01–C02,
  Ana57 C01–C02, Ana59 C01–C04, Ana60 C01, Ana67 C01–C02, Ana68 C01, and
  Ana70 C01–C03. The eight scripts and 19 relevant dependency/scene/workbench
  files are byte-identical to prior PR head `58675d0a`; the intended normalized
  runtime file exists. This is evidence of a pre-existing platform blocker,
  not a claim that an isolated prior-head replay was run. No saved recipe,
  image, frozen class or environment check was changed to conceal these failures.

## Authorized workbench reopening

Ana72–Ana74 were reopened through the unchanged official workbench flow after
explicit user authorization, using fresh context tokens and the formal
environment. They now appear as **waiting** in the active list; restart
persistence was verified. Active questions changed from 58 to 61, collected
questions from 73 to 70, and each history from zero to one entry.

Each old collection remains verbatim in history with its actual reopening time.
Only the three collection files and collected index changed, plus the new
baseline manifest created by normal workbench initialization. Existing
baselines and all 146 accepted Analytics variants were preserved. Historical
`current.special_case` fields are retained inside the old collection record;
the outer reopened status and runtime state determine active-list membership.
