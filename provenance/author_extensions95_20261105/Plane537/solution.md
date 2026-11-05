# Solution

**Answer: E — Pocket E (the midpoint of the bottom rail).**

Here W=12, H=8 and P=(0,2). The unfolded path is (t,2+t), t>0. A corner would require t=12m and 2+12m=8n for integers m,n. The latter equation is impossible modulo 4: its left side is 2 modulo 4 and its right side is 0. Thus none of A, B, C or D is ever reached.

The bottom rail is reached precisely when 2+t=16n. Its positive encounter parameters begin t=14,30,46,... . At t=14, x=14 folds into the width-12 table as x=10, so the first bottom encounter misses E. At t=30, x=30 folds as x=6, exactly the midpoint. This is the first possible bottom-midpoint capture, hence Pocket E is reached first.

For an explicit earlier-event check, the positions are (6,8) at t=6, (12,2) at t=12, (10,0) at t=14, (2,8) at t=22, and (0,6) at t=24. Every one is an ordinary non-pocket rail point. At t=30 the position is (6,0), E. The four corner choices are impossible by the congruence argument, and option F is false because capture occurs in finite time.

The table origin used below is its bottom-left corner. These coordinates merely encode the dimensions and P's location stated in the question. The unit grid is a reference grid, not a set of reflecting walls. The black dot and segment show the incoming motion; the arrow shows the motion after reflection at P. The acute angle is measured against the drawn rail ray, not its normal.

Unfolding a specular reflection continues the ray straight into a reflected copy of the table. A coordinate u folds into an interval of length L by taking r = u mod 2L, then returning r for r ≤ L and 2L−r otherwise. At a pocket, capture takes place immediately; simultaneous arrival at two rails at a corner is one pocket encounter, not an extra reflection. Schematic circle radii do not create extra capture regions. Constant speed and point targets are explicit, so there is no friction-based stopping or finite-radius alternative.

The added midpoint pocket changes the pocket configuration. Although the corners are inaccessible, the ball is captured on its second bottom-rail visit. This requires a first-hit argument rather than merely observing that a corner equation has no solution. Its 3:2 rectangle, quarter-height start and fifth pocket are different from every other draft.
