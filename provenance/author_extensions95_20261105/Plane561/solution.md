# Extension 02: complete solution

**Answer: E — piece E.**

The figure supplies the target squares and all five rigid piece shapes at the same unit scale. Quarter turns are allowed; reflections are forbidden. Every placement must align the unit grids. No unpictured lengths or coordinates are assumed.

For describing the solution only, number columns from the left of the target bounding rectangle and rows from the bottom, starting at 1. The dot is at the centre of column 2, row 3. This numbering is a reference system, not an extra condition.

## Exhaustive construction and exclusion

1. Generate the allowed signed permutation matrices: the four quarter turns, and also the four reflected orientations when flipping is permitted. Remove orientations that produce the same occupied unit squares.
2. For each resulting orientation, align one fixed square with each target square in turn. Keep the placement exactly when every occupied square belongs to the target. Every legal placement appears, because its anchor square must coincide with some target square.
3. Search these placements with one column for each target square and one column for each piece. Choose an uncovered column and try every remaining placement covering it. Delete intersecting placements and recurse. A finished branch is exactly a tiling; conversely every tiling follows one of the tried branches. This proves that no tiling is omitted.
4. An independently ordered search places the five pieces in a fixed order and rejects overlaps. It obtains exactly the same complete set of tilings.

The piece areas are {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 5}, totaling 19, equal to the target area. There are 109 legal single-piece placements and **6 complete tilings**.

| Piece | Distinct allowed orientations | Legal placements | Tilings in which it covers the dot |
| --- | ---: | ---: | ---: |
| A | 2 | 25 | 0 |
| B | 4 | 35 | 0 |
| C | 2 | 12 | 0 |
| D | 4 | 19 | 0 |
| E | 4 | 18 | 6 |

All complete tilings are listed below. Each letter is one unit square of the indicated rigid piece; a period lies outside the target. The top text row corresponds to the top of the figure. These are solution certificates, not markings added to the baseline image.

Tiling 1:

```text
...CC
EECC.
.EDD.
EEDD.
.BAD.
BBA..
```

Tiling 2:

```text
...CC
BBCC.
.BDD.
EEDD.
.EAD.
EEA..
```

Tiling 3:

```text
...CC
EECC.
.EBB.
EEBA.
.DDA.
DDD..
```

Tiling 4:

```text
...CC
EECC.
.EDD.
EEDD.
.BBD.
AAB..
```

Tiling 5:

```text
...CC
EECC.
.EAA.
EEBB.
.DDB.
DDD..
```

Tiling 6:

```text
...AA
EEBB.
.ECB.
EECC.
.DDC.
DDD..
```

In every one of these 6 tilings, the dot square belongs to **E**. Pieces A, B, C, D cover it in zero legal tilings, so all four distractors are excluded.

The dot centre is 0.5 unit from the nearest boundary of its covering piece in the worst case. Its drawn radius is 0.075; the entire dot disk therefore stays at least 0.425 unit from a seam or target boundary. It is never on an edge.

A target can have several tilings while this question has one answer: the requested identity is invariant across all of them. The executable proof and each exact matrix/translation/cell certificate are in `math_check.py` and `math_check.json`.

## Substantive change

New orthogonal polyomino geometry replaces the parent sloping pieces; new target, new dot and explicit lattice motions.
A six-row asymmetric staircase with several side notches.
A domino, a triomino, a skew tetromino, a P pentomino and a U pentomino; turning only.
The other four extensions use different target areas and different shape multisets; this is not a relabeling, whole-image transform or relocation of the dot on one reused puzzle.

## Reproduction

Run the renderer and checker through the campaign `shared/safe_run.py` with this task as `--task`. Within that wrapper the renderer accepts `render.py --output baseline.png --svg`; the checker accepts `math_check.py`. Importing `render.py` does not create an image. The scene contains no answer or approval fields.
