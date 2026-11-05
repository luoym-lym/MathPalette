# Solution for extension_05

**Answer: D.** The actual pattern is: cell (2,1): club with stem up; cell (3,1): diamond with horizontal long axis; cell (1,2): diamond with horizontal long axis; cell (2,2): spade with tip down.

In this solution, board rows are counted from top to bottom and columns from left to right. Local option cells are also indexed from the top-left bounding rectangle; absent cells are not part of the piece.

## A direct matching witness

Reflect the displayed option left-to-right, then rotate the displayed option 90 degrees counterclockwise and translate it to the following cells. Each mark, including its direction, agrees with the grid. Reversing this motion gives the displayed answer from the cut piece.

| Option cell (column, row) | Board cell (row, column) | Mark in displayed option |
| --- | --- | --- |
| (1, 2) | (2, 4) | diamond with horizontal long axis |
| (2, 2) | (3, 4) | spade with tip down |
| (2, 1) | (3, 3) | club with stem up |
| (3, 1) | (4, 3) | diamond with horizontal long axis |

## Exhaustive uniqueness check

A legal cut uses whole cells. Once its orientation is fixed, its lower-left bounding cell determines its position. For a transformed template of width w and height h in a W by H board, there are (W-w+1)(H-h+1) positions. The checker evaluates all four quarter-turns and both reflection states. It transforms both cell coordinates and symbol directions, and compares every cell. For a diamond, opposite directions of its long axis are identical; all other quarter-turn directions are distinct. Thus the following search covers every case permitted by the question.

| Option | Positions tested (including orientation) | Exact matches | Minimum mismatching cells |
| --- | ---: | ---: | ---: |
| A | 96 | 0 | 1 |
| B | 96 | 0 | 1 |
| C | 96 | 0 | 2 |
| D | 96 | 1 | 0 |
| E | 96 | 0 | 2 |

Only D has a zero-mismatch placement, and it has exactly one. Every tested placement and its mismatching cells are retained in math_check.json; math_check.py reproduces this enumeration without importing the renderer or using the stored answer to select candidates.

## Why the other choices fail

- **A:** Compared with the matching pattern, at option cell (1, 2), diamond with vertical long axis replaces diamond with horizontal long axis. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 1 mismatching cell(s).
- **B:** Compared with the matching pattern, at option cell (1, 2), club with stem right replaces diamond with horizontal long axis. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 1 mismatching cell(s).
- **C:** Compared with the matching pattern, at option cell (2, 1), diamond with horizontal long axis replaces club with stem up; at option cell (1, 2), club with stem up replaces diamond with horizontal long axis. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 2 mismatching cell(s).
- **E:** Compared with the matching pattern, at option cell (3, 1), diamond with vertical long axis replaces diamond with horizontal long axis; at option cell (2, 2), spade with tip right replaces spade with tip down. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 2 mismatching cell(s).

The correct option has no match among rotations alone. The reflected match uses the explicitly stated transparency and turning-over rule.

## Conditions and design

The template, complete board, all five choices, and all mark orientations are visible. The English stem explicitly specifies whole grid cells, rigid movement of marks, rotation, and the turning-over rule. No undisplayed lengths, coordinates, colors, or hidden marks are used.

A staggered four-cell chain on a transparent sheet permits turning over. The sole valid choice actually requires reflection, so the extra rule changes the solution.

The other four originals use different free-polyomino shapes (see design.json). These differences persist under rotation and reflection.

This original is staged as unreviewed_original, with no formal question number or user approval.
