# Solution for extension_01

**Answer: C.** The actual pattern is: cell (1,1): star rotated 180 degrees counterclockwise from top-pointing; cell (2,1): heart with tip up; cell (3,1): club with stem down.

In this solution, board rows are counted from top to bottom and columns from left to right. Local option cells are also indexed from the top-left bounding rectangle; absent cells are not part of the piece.

## A direct matching witness

Rotate the displayed option 90 degrees counterclockwise and translate it to the following cells. Each mark, including its direction, agrees with the grid. Reversing this motion gives the displayed answer from the cut piece.

| Option cell (column, row) | Board cell (row, column) | Mark in displayed option |
| --- | --- | --- |
| (1, 1) | (4, 3) | star rotated 180 degrees counterclockwise from top-pointing |
| (2, 1) | (3, 3) | heart with tip up |
| (3, 1) | (2, 3) | club with stem down |

## Exhaustive uniqueness check

A legal cut uses whole cells. Once its orientation is fixed, its lower-left bounding cell determines its position. For a transformed template of width w and height h in a W by H board, there are (W-w+1)(H-h+1) positions. The checker evaluates all four quarter-turns. It transforms both cell coordinates and symbol directions, and compares every cell. For a diamond, opposite directions of its long axis are identical; all other quarter-turn directions are distinct. Thus the following search covers every case permitted by the question.

| Option | Positions tested (including orientation) | Exact matches | Minimum mismatching cells |
| --- | ---: | ---: | ---: |
| A | 44 | 0 | 1 |
| B | 44 | 0 | 1 |
| C | 44 | 1 | 0 |
| D | 44 | 0 | 2 |
| E | 44 | 0 | 2 |

Only C has a zero-mismatch placement, and it has exactly one. Every tested placement and its mismatching cells are retained in math_check.json; math_check.py reproduces this enumeration without importing the renderer or using the stored answer to select candidates.

## Why the other choices fail

- **A:** Compared with the matching pattern, at option cell (1, 1), star rotated 270 degrees counterclockwise from top-pointing replaces star rotated 180 degrees counterclockwise from top-pointing. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 1 mismatching cell(s).
- **B:** Compared with the matching pattern, at option cell (3, 1), star rotated 0 degrees counterclockwise from top-pointing replaces club with stem down. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 1 mismatching cell(s).
- **D:** Compared with the matching pattern, at option cell (1, 1), club with stem down replaces star rotated 180 degrees counterclockwise from top-pointing; at option cell (3, 1), star rotated 180 degrees counterclockwise from top-pointing replaces club with stem down. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 2 mismatching cell(s).
- **E:** Compared with the matching pattern, at option cell (2, 1), heart with tip left replaces heart with tip up; at option cell (3, 1), club with stem right replaces club with stem down. The exhaustive search finds no occurrence of this choice anywhere on the board; even its best placement has 2 mismatching cell(s).

## Conditions and design

The template, complete board, all five choices, and all mark orientations are visible. The English stem explicitly specifies whole grid cells, rigid movement of marks, rotation, and the turning-over rule. No undisplayed lengths, coordinates, colors, or hidden marks are used.

A three-cell straight run replaces the parent domino: both consecutive adjacencies and three simultaneous mark orientations must agree.

The other four originals use different free-polyomino shapes (see design.json). These differences persist under rotation and reflection.

This original is staged as unreviewed_original, with no formal question number or user approval.
