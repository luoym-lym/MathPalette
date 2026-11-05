# Solution — Plane236_extension_04

The beam exits at **E** (choice **E**).

For positional descriptions only, count columns from the left and rows from the bottom. Thus (c, r) names a visible dashed-grid crossing, with the outer guide at column 0 / 4 or row 0 / 5. These names introduce no hidden geometric conditions.

A / mirror maps a horizontal or vertical direction (dx, dy) to (dy, dx). A \ mirror maps it to (-dy, -dx). Apply this rule on both sides of every finite mirror, always stopping at the nearest mirror on the current ray.

| Hit | Visible mirror position | Slope | Arrives moving | Leaves moving |
| --- | --- | --- | --- | --- |
| 1 | column 3, row 2 | / | left | down |
| 2 | column 3, row 1 | / | down | left |
| 3 | column 2, row 1 | \ | left | up |
| 4 | column 2, row 2 | / | up | right |
| 5 | column 3, row 2 (again, from the other side) | / | right | up |
| 6 | column 3, row 3 | \ | up | left |
| 7 | column 2, row 3 | \ | left | up |
| 8 | column 2, row 4 | \ | up | left |
| 9 | column 1, row 4 | \ | left | up |

After hit 9, the beam travels up to the top of column 1, which is labeled E. No finite mirror intersects that final ray before the boundary.

The full entry-to-exit path is:

(4, 2) → (3, 2) → (3, 1) → (2, 1) → (2, 2) → (3, 2) → (3, 3) → (2, 3) → (2, 4) → (1, 4) → (1, 5).

Every turn above occurs at a finite mirror midpoint, away from its endpoints. At each step there is exactly one nearest collision; no ray grazes a mirror or reaches a corner. The trace terminates without repeating an incoming position-and-direction state. Reversing the exit ray retraces every listed collision back to the incident arrow, which also confirms the two-sided reflection rule.

The other choices fail as follows:

- A labels the left end of row 2. The complete fixed-mirror trace ends at (1, 5), whereas A is at (0, 2); the final outgoing ray does not reach it.
- B labels the bottom of column 2. The complete fixed-mirror trace ends at (1, 5), whereas B is at (2, 0); the final outgoing ray does not reach it.
- C labels the top of column 3. The complete fixed-mirror trace ends at (1, 5), whereas C is at (3, 5); the final outgoing ray does not reach it.
- D labels the left end of row 4. The complete fixed-mirror trace ends at (1, 5), whereas D is at (0, 4); the final outgoing ray does not reach it.

The mirrors cannot be moved, removed, or rotated in this question. The incident arrow fixes the initial direction; every mirror and every exit is visible. Therefore deterministic equal-angle reflection gives one path and exactly one of the five displayed choices.

Independent verification uses exact rational ray/segment intersection, evaluates all forward finite-mirror candidates after every hit, and compares the result to a separate grid-cell walker. The renderer is not imported by either mathematical computation.

Substantive change from Plane236: 四行三列、左下两个交点无镜；从右边第二行进入，九次反射重访第三列第二行镜，再经上部两行从左上方出口离开。

The other four extensions use different fixed mirror networks. A label-independent audit of all ten pairs excludes equality under translation, uniform scaling, rotation, or reflection; see ../structural_audit.json.
