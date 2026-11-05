# Solution for extension_02

**Answer: A.** The actual pattern is: cell (1,1): diamond with horizontal long axis; cell (1,2): spade with tip left; cell (2,2): club with stem left.

In this solution, board rows are counted from top to bottom and columns from left to right. Local option cells are also indexed from the top-left bounding rectangle; absent cells are not part of the piece.

## A direct matching witness

Rotate the displayed option 270 degrees counterclockwise and translate it to the following cells. Each mark, including its direction, agrees with the grid. Reversing this motion gives the displayed answer from the cut piece.

| Option cell (column, row) | Board cell (row, column) | Mark in displayed option |
| --- | --- | --- |
| (1, 2) | (2, 2) | spade with tip left |
| (2, 2) | (3, 2) | club with stem left |
| (1, 1) | (2, 3) | diamond with horizontal long axis |

## Exhaustive uniqueness check

A legal cut uses whole cells. Once its orientation is fixed, its lower-left bounding cell determines its position. For a transformed template of width w and height h in a W by H board, there are (W-w+1)(H-h+1) positions. The checker evaluates all four quarter-turns. It transforms both cell coordinates and symbol directions, and compares every cell. For a diamond, opposite directions of its long axis are identical; all other quarter-turn directions are distinct. Thus the following search covers every case permitted by the question.

| Option | Positions tested (including orientation) | Exact matches | Minimum mismatching cells |
| --- | ---: | ---: | ---: |
| A | 36 | 1 | 0 |
| B | 36 | 0 | 1 |
| C | 36 | 0 | 1 |
| D | 36 | 0 | 2 |
| E | 36 | 0 | 1 |

Only A has a zero-mismatch placement, and it has exactly one. Every tested placement and its mismatching cells are retained in math_check.json; math_check.py reproduces this enumeration without importing the renderer or using the stored answer to select candidates.

## Why the other choices fail

- **B:** Compared with the matching pattern, at option cell (2, 2), club with stem down replaces club with stem left. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 1 mismatching cell(s).
- **C:** Compared with the matching pattern, at option cell (1, 1), star rotated 90 degrees counterclockwise from top-pointing replaces diamond with horizontal long axis. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 1 mismatching cell(s).
- **D:** Compared with the matching pattern, at option cell (1, 2), club with stem left replaces spade with tip left; at option cell (2, 2), spade with tip left replaces club with stem left. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 2 mismatching cell(s).
- **E:** Compared with the matching pattern, at option cell (1, 1), diamond with vertical long axis replaces diamond with horizontal long axis; at option cell (2, 2), club with stem down replaces club with stem left. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 1 mismatching cell(s).

## Conditions and design

The template, complete board, all five choices, and all mark orientations are visible. The English stem explicitly specifies whole grid cells, rigid movement of marks, rotation, and the turning-over rule. No undisplayed lengths, coordinates, colors, or hidden marks are used.

A bent three-cell corner replaces a straight domino; two perpendicular adjacencies must meet at the same cell.

The other four originals use different free-polyomino shapes (see design.json). These differences persist under rotation and reflection.

This original is staged as unreviewed_original, with no formal question number or user approval.
