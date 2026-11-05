# Answer: C — piece C is left out.

All four selected pieces must place their two full straight sides on the exterior. If their common straight-side length is L, the eight outside segments have total length 8L, so the square has side 2L. Each piece therefore occupies a different corner. At each corner there are exactly two possible orientations, including turning the piece over.

To compare the contours, call the distinct wavy edge shapes P, Q, R, S as needed. A shape includes its lobe count, depths and positions; for this first necessary test we ignore which lobe points outward. These names are explanation labels, not extra marks or conditions in the question.

- P: the right wavy edge of piece A.
- Q: the top wavy edge of piece A.
- R: the right wavy edge of piece B.
- S: the top wavy edge of piece C.

| Piece | Two wavy edge shapes |
| --- | --- |
| A | P, Q |
| B | R, P |
| C | P, S |
| D | S, R |
| E | Q, S |

Every internal edge must be paired with exactly one edge of the same shape and opposite traversal. Thus each shape must occur an even number of times. The four pieces also have to form one connected cycle; this excludes an isolated set of edge shapes. These tests alone are not used as a sufficiency proof.

The following actual arrangement supplies sufficiency. Start with each piece exactly as drawn. If indicated, turn it over by reflecting left to right first; then rotate counterclockwise by the stated angle. Move its full-straight-side corner to the specified square corner.

| Square position | Piece | Turn over first? | Counterclockwise rotation |
| --- | --- | --- | --- |
| Bottom left | A | No | 0° |
| Bottom right | B | No | 90° |
| Top right | D | No | 180° |
| Top left | E | No | 270° |

[Exact vector drawing of this square assembly](solution_assembly.svg).

The four internal joins are: A–E, A–B, D–E, B–D. On each join, every cubic segment has exactly the same four control points in reversed order on the neighboring piece. Hence the entire curves coincide, not just their endpoints or their number of bumps. All other edges lie on the square boundary.

There are no unintended crossings: every wavy edge stays strictly inside its 45° cone about its straight base segment, except at the endpoints. This follows from the exact control-point inequalities checked in math_check.py and the convex-hull property of cubic Bézier curves. The cones of neighboring internal joins are disjoint except at the center. Consequently the four matching outlines bound four disjoint interiors and leave no gap inside the square.

The other possible omitted pieces fail as follows:

| Omitted piece | Why it fails |
| --- | --- |
| A | Edge shape Q, S occurs an odd number of times, so at least one internal edge has no partner. |
| B | Edge shape R, S occurs an odd number of times, so at least one internal edge has no partner. |
| D | Edge shape P, R occurs an odd number of times, so at least one internal edge has no partner. |
| E | Edge shape P, Q occurs an odd number of times, so at least one internal edge has no partner. |

For a complete independent check, the verifier tries all five omissions, all 24 corner assignments for each omission, and both permitted orientations at every corner: 5 × 24 × 2⁴ = 1,920 cases. It compares the exact curve geometry and derives the remaining letter before reading the saved answer. The resulting counts are:

| Omitted piece | Valid placements |
| --- | --- |
| A | 0 |
| B | 0 |
| C | 8 |
| D | 0 |
| E | 0 |

Therefore the unique unused piece is **C**. Multiple symmetric arrangements of the same four pieces do not create another answer.

Every piece has exactly area L², calculated by exact integration of its cubic outline; every four-piece selection has area 4L². Area alone cannot eliminate any option.

The public question explicitly permits rotations and turning over, forbids cutting/resizing, and puts both full straight sides on the outside. The search covers all these motions and uses no hidden arrangement rule. Construction coordinates in the certificate are for reproducibility, not additional given data.

与父题的实质差异：All five pieces have exactly equal area, unlike the parent single-cap profiles; balanced multi-lobe cubic contours force exact edge matching.

与另外四题的差异：四种轮廓构成四环；干扰块连接对角的两种边缘。两瓣宽波、浅波、偏峰波及四瓣波必须逐一匹配。

Status: unreviewed_original. This mathematical verification is not a user approval, Special Pass or Collect.
