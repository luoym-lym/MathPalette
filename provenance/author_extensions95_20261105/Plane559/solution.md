# Solution — Plane236_extension_05

The beam exits at **C** (choice **C**).

For positional descriptions only, count columns from the left and rows from the bottom. Thus (c, r) names a visible dashed-grid crossing, with the outer guide at column 0 / 5 or row 0 / 4. These names introduce no hidden geometric conditions.

A / mirror maps a horizontal or vertical direction (dx, dy) to (dy, dx). A \ mirror maps it to (-dy, -dx). Apply this rule on both sides of every finite mirror, always stopping at the nearest mirror on the current ray.

| Hit | Visible mirror position | Slope | Arrives moving | Leaves moving |
| --- | --- | --- | --- | --- |
| 1 | column 2, row 2 | \ | up | left |
| 2 | column 1, row 2 | \ | left | up |
| 3 | column 1, row 3 | / | up | right |
| 4 | column 2, row 3 | \ | right | down |
| 5 | column 2, row 2 (again, from the other side) | \ | down | right |
| 6 | column 3, row 2 | \ | right | down |
| 7 | column 3, row 1 | \ | down | right |
| 8 | column 4, row 1 | \ | right | down |

After hit 8, the beam travels down to the bottom of column 4, which is labeled C. No finite mirror intersects that final ray before the boundary.

The full entry-to-exit path is:

(2, 0) → (2, 2) → (1, 2) → (1, 3) → (2, 3) → (2, 2) → (3, 2) → (3, 1) → (4, 1) → (4, 0).

The beam passes straight through the following empty guide crossings: (2, 1). A dashed crossing without a short diagonal mirror does not reflect light.

Every turn above occurs at a finite mirror midpoint, away from its endpoints. At each step there is exactly one nearest collision; no ray grazes a mirror or reaches a corner. The trace terminates without repeating an incoming position-and-direction state. Reversing the exit ray retraces every listed collision back to the incident arrow, which also confirms the two-sided reflection rule.

The other choices fail as follows:

- A labels the top of column 2. The complete fixed-mirror trace ends at (4, 0), whereas A is at (2, 4); the final outgoing ray does not reach it.
- B labels the left end of row 2. The complete fixed-mirror trace ends at (4, 0), whereas B is at (0, 2); the final outgoing ray does not reach it.
- D labels the right end of row 1. The complete fixed-mirror trace ends at (4, 0), whereas D is at (5, 1); the final outgoing ray does not reach it.
- E labels the top of column 3. The complete fixed-mirror trace ends at (4, 0), whereas E is at (3, 4); the final outgoing ray does not reach it.

The mirrors cannot be moved, removed, or rotated in this question. The incident arrow fixes the initial direction; every mirror and every exit is visible. Therefore deterministic equal-angle reflection gives one path and exactly one of the five displayed choices.

Independent verification uses exact rational ray/segment intersection, evaluates all forward finite-mirror candidates after every hit, and compares the result to a separate grid-cell walker. The renderer is not imported by either mathematical computation.

Substantive change from Plane236: 三行四列、底行前两个交点无镜；由下边第二列穿过首个空位入射，八次反射重访中央镜，最后沿底行折转并从下边第四列离开。

The other four extensions use different fixed mirror networks. A label-independent audit of all ten pairs excludes equality under translation, uniform scaling, rotation, or reflection; see ../structural_audit.json.
