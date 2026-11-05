# Plane248_extension_01: complete solution

**Answer: C. Outline C cannot be made from the two displayed pieces without flipping.**

The other four choices are feasible targets, so they are not answers to the question asking for the impossible outline. The number of possible seams in a feasible target does not affect this unique choice.

## Exact interpretation and coordinates

Use the shortest source edge as one unit. The question explicitly states that all corners are right angles, all side lengths are whole units and all outlines have the same scale. Take the lower-left of the bounding box of a displayed piece as (0,0), with x right and y up. For each target use its own bounding box in the same way. A cell (x,y) means the closed square [x,x+1] × [y,y+1]; shared edges have zero area. These coordinates describe the visible outlines and introduce no additional condition.

The source cells are S = {(0,0), (0,1), (0,2), (1,0)}.

| Target | Cells of its exact outline |
| --- | --- |
| A | {(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3)} |
| B | {(0,1), (1,1), (2,1), (2,2), (3,0), (3,1), (4,1), (5,1)} |
| C | {(0,0), (0,1), (0,2), (0,3), (1,1), (1,2), (2,1), (2,2)} |
| D | {(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (1,0), (1,3)} |
| E | {(0,0), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2), (3,2)} |

All targets are simple connected outlines of area 8 square units, twice the piece area. Area alone does not decide the answer.

## Why arbitrary rotations are covered

Take any convex 90-degree corner of the target. Every tile corner is 90 or 270 degrees, so exactly one tile occupies a neighborhood of that corner. Its corner coincides with the target corner, with both incident edges aligned to the target edges. Its rotation is therefore a multiple of 90 degrees, and its translation maps an integer vertex to an integer vertex. After removing this first tile, every boundary segment and vertex of the remaining tile comes from the target or the first tile. They lie on the same integer orthogonal lattice, forcing the second tile also to have a quarter-turn rotation and integer translation. Thus the finite exact cell enumeration covers every permitted continuous rotation/translation.

No quarter-turn restriction has been silently imposed: it follows from the displayed orthogonal geometry and the whole-unit lengths stated in the question. Reflections are excluded throughout this enumeration.

## Certificates for every feasible target

For each tile below, first rotate the original source about its coordinate origin counterclockwise, then translate by t. The two transformed cell sets are disjoint and their union is the complete target. The checker independently verifies these exact equalities.

| Target | First tile: rotation; translation | Second tile: rotation; translation | Total distinct tilings, ignoring tile order |
| --- | --- | --- | --- |
| A | 0°; t=(0,0) | 180°; t=(2,4) | 1 |
| B | 90°; t=(3,1) | 270°; t=(3,2) | 1 |
| D | 0°; t=(0,0) | 0°; t=(0,3) | 1 |
| E | 90°; t=(3,0) | 270°; t=(1,3) | 1 |

These placements establish why each of the four distractor answers is incorrect. Every valid placement certificate, including any alternative seam, is retained in `math_check.json`.

## Exhaustive exclusion of C

Normalize each of the four rotated source shapes so that its lowest x and y cell coordinates are zero. Translate that normalized shape to every integer (dx,dy) in the target bounding box, retaining only placements contained in the target. Remove each retained placement and compare the remaining cell set against all four rotations of S. This enumerates every possible tiling by the preceding proof.

For a compact comparison, a rotation signature is the lexicographically smallest sorted cell set over the four rotations, after translation normalization. Reflection is never included in that signature.

The source rotation signature is {(0,0), (0,1), (0,2), (1,0)}.

All 4 contained placements of a first piece in C are listed below. Each has a different remaining signature from the source.

| First tile rotation | Translation of the original source | Remaining rotation signature | Match? |
| --- | --- | --- | --- |
| 0° | (0,1) | {(0,0), (0,1), (1,0), (2,2)} | No |
| 90° | (3,1) | {(0,0), (0,2), (0,3), (1,2)} | No |
| 270° | (0,2) | {(0,0), (0,1), (0,2), (1,2)} | No |
| 270° | (0,3) | {(0,0), (0,3), (1,1), (2,1)} | No |

There is no possible second piece for any first-piece placement. Thus C, and only C, is impossible. As a diagnostic, the checker also constructs a tiling of this target if reflection is permitted; the no-flipping rule is therefore essential rather than an irrelevant instruction.

## Relation to the parent and status

长臂与单格脚组成的 L 四格；目标包括矩形、长折臂和双凹口轮廓。 父题为含斜边的箭头状拼块；本题使用新的正交手性轮廓及全新目标组合。

The parent task and this task both ask for the unique impossible silhouette formed from two congruent pieces using rotations and translations only. This item uses a different source geometry and new target unions; it is not an option permutation, a rotation or a rescaling of the parent or of another new item.

**Status: unreviewed_original.** No formal question number, user approval, Specialvar, Quick Test, Pass or Collect has been assigned or performed.
