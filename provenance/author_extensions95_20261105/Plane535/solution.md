# Solution

**Answer: A — Pocket A (the bottom-right corner).**

Here W=9, H=6 and P=(0,3). The outgoing direction is (1,1), so in an unfolded table the position is (t,3+t), t>0. A corner requires t=9m and 3+9m=6n, where m is a positive integer. Dividing by 3 gives 1+3m=2n, so m must be odd. Its least positive value is m=1: t=9, giving unfolded position (9,12). Folding gives (9,0), Pocket A.

Before that corner, the only boundary event is at t=3, position (3,6). It is on the top rail but at no pocket. Thus A is the first pocket. The simultaneous right/bottom encounter at t=9 is absorbed at A immediately. Pockets B, C and D are not visited first, and the finite capture excludes option E.

The table origin used below is its bottom-left corner. These coordinates merely encode the dimensions and P's location stated in the question. The unit grid is a reference grid, not a set of reflecting walls. The black dot and segment show the incoming motion; the arrow shows the motion after reflection at P. The acute angle is measured against the drawn rail ray, not its normal.

Unfolding a specular reflection continues the ray straight into a reflected copy of the table. A coordinate u folds into an interval of length L by taking r = u mod 2L, then returning r for r ≤ L and 2L−r otherwise. At a pocket, capture takes place immediately; simultaneous arrival at two rails at a corner is one pocket encounter, not an extra reflection. Schematic circle radii do not create extra capture regions. Constant speed and point targets are explicit, so there is no friction-based stopping or finite-radius alternative.

Relative to the parent, the aspect ratio changes from 4:3 to 3:2 and P is the left-rail midpoint. The path has one ordinary reflection after P before capture, whereas the parent's first capture is C after three ordinary reflections.
