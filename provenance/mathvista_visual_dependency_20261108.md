# MathVista visual-dependency revision review

## Scope and review status

This proposed revision covers exactly the 61 newly admitted MathVista items
**Ana71–Ana131**. Ana46, the other 957 formal items, all source images,
all published redraws, frozen scenes, source notes, shared drawing code, and Special variants
are unchanged.

All 61 prompts were revised. Answers changed for 19 items, answer types for 12,
and choice mappings for 20 (including conversions to/from non-choice answers).
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
- Keep all geometric evidence in the existing images. No new rendering or
  visual style was introduced.

Examples:

| Item | Previous shortcut | Revised visual task |
| --- | --- | --- |
| Ana71 | Absolute-value formula gives both derivatives | Compare the slopes of the displayed branch at two inputs |
| Ana89 | A nonempty epigraph is necessarily infinite | Decide whether a specified point belongs to the actual shading |
| Ana111 | The supplied power determines improper-integral divergence | Determine the sign of a finite integral from the plotted region |
| Ana121 | Logarithm formulas in the options determine derivative order | Count visible intersections with a specified horizontal line |
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

- Visual-revision regression tests: **5 passed**. They bind the semantic audit
  to exact question/image hashes, verify all metadata and preserved assets,
  check the 1,018-record index and verify the current explicit reapproval against preserved previous approval records.
- Existing answer-schema tests: **7 passed**.
- Existing catalog-concurrency tests: **3 passed**.
- All 61 baseline/revised renderers produce identical pixels when run in the
  same available environment. Metadata-excluded renderer ASTs also match.
- The production catalog check passes after explicit user reapproval. The original approval gate is unchanged.
- No paid model calls or model-evaluation logs were created.

## Rendering environment limitation

The repository freezes Python 3.13.9, NumPy 2.5.3, Matplotlib 3.11.2,
Pillow 12.3.0, and FreeType 2.14.3. The available environment was Python 3.12.14,
NumPy 2.3.5, Matplotlib 3.10.8, Pillow 13.0.0, and FreeType 2.6.1.

In that environment, **61/61 before/after renders match each other**, but
**0/61 regenerated images match the published pixels**. This is not reported as
frozen-environment reproducibility. The 61 published PNG files, source images,
and scene files retain their exact baseline hashes. Re-run the committed redraw
checker in the frozen environment to verify published-pixel reproduction.
