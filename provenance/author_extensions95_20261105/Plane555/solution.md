# Solution — Plane236_extension_01

The beam exits at **D** (choice **D**).

For positional descriptions only, count columns from the left and rows from the bottom. Thus (c, r) names a visible dashed-grid crossing, with the outer guide at column 0 / 4 or row 0 / 4. These names introduce no hidden geometric conditions.

A / mirror maps a horizontal or vertical direction (dx, dy) to (dy, dx). A \ mirror maps it to (-dy, -dx). Apply this rule on both sides of every finite mirror, always stopping at the nearest mirror on the current ray.

| Hit | Visible mirror position | Slope | Arrives moving | Leaves moving |
| --- | --- | --- | --- | --- |
| 1 | column 1, row 3 | \ | right | down |
| 2 | column 1, row 2 | \ | down | right |
| 3 | column 3, row 2 | \ | right | down |
| 4 | column 3, row 1 | / | down | left |
| 5 | column 2, row 1 | \ | left | up |
| 6 | column 2, row 3 | / | up | right |
| 7 | column 3, row 3 | / | right | up |

After hit 7, the beam travels up to the top of column 3, which is labeled D. No finite mirror intersects that final ray before the boundary.

The full entry-to-exit path is:

(0, 3) → (1, 3) → (1, 2) → (3, 2) → (3, 1) → (2, 1) → (2, 3) → (3, 3) → (3, 4).

The beam passes straight through the following empty guide crossings: (2, 2), (2, 2). A dashed crossing without a short diagonal mirror does not reflect light.

Every turn above occurs at a finite mirror midpoint, away from its endpoints. At each step there is exactly one nearest collision; no ray grazes a mirror or reaches a corner. The trace terminates without repeating an incoming position-and-direction state. Reversing the exit ray retraces every listed collision back to the incident arrow, which also confirms the two-sided reflection rule.

The other choices fail as follows:

- A labels the bottom of column 1. The complete fixed-mirror trace ends at (3, 4), whereas A is at (1, 0); the final outgoing ray does not reach it.
- B labels the bottom of column 2. The complete fixed-mirror trace ends at (3, 4), whereas B is at (2, 0); the final outgoing ray does not reach it.
- C labels the right end of row 2. The complete fixed-mirror trace ends at (3, 4), whereas C is at (4, 2); the final outgoing ray does not reach it.
- E labels the right end of row 3. The complete fixed-mirror trace ends at (3, 4), whereas E is at (4, 3); the final outgoing ray does not reach it.

The mirrors cannot be moved, removed, or rotated in this question. The incident arrow fixes the initial direction; every mirror and every exit is visible. Therefore deterministic equal-angle reflection gives one path and exactly one of the five displayed choices.

Independent verification uses exact rational ray/segment intersection, evaluates all forward finite-mirror candidates after every hit, and compares the result to a separate grid-cell walker. The renderer is not imported by either mathematical computation.

Substantive change from Plane236: 三行三列、中心交点留空；七次反射经过七个不同镜子，跨过空位后从上边离开。父题是两行三列且重访镜子。

The other four extensions use different fixed mirror networks. A label-independent audit of all ten pairs excludes equality under translation, uniform scaling, rotation, or reflection; see ../structural_audit.json.
