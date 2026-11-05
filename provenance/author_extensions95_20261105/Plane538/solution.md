# Solution

**Answer: C — Pocket C (the top-left corner).**

Here W=10, H=8 and P=(4,0). The outgoing arrow points northeast. Since tan θ=1/2 relative to the bottom rail, its horizontal and vertical velocity components are in ratio 2:1. Use the unfolded parametrization (4+2t,t), t>0; t is a travel parameter, not a time measured in a specified unit.

A corner requires t=8n and 4+16n=10m. Reducing modulo 10 gives 6n≡6 (mod 10), or n≡1 (mod 5). The least positive n is 1. At t=8 the unfolded position is (20,8), which folds to (0,8), Pocket C.

The only earlier boundary encounter is t=3 at (10,3) on the right rail, away from both right-hand corner pockets. The next boundary event simultaneously reaches the top and left rails at C, where capture precedes reflection. Thus A, B and D are not the first pocket, and option E is false.

The table origin used below is its bottom-left corner. These coordinates merely encode the dimensions and P's location stated in the question. The unit grid is a reference grid, not a set of reflecting walls. The black dot and segment show the incoming motion; the arrow shows the motion after reflection at P. The acute angle is measured against the drawn rail ray, not its normal.

Unfolding a specular reflection continues the ray straight into a reflected copy of the table. A coordinate u folds into an interval of length L by taking r = u mod 2L, then returning r for r ≤ L and 2L−r otherwise. At a pocket, capture takes place immediately; simultaneous arrival at two rails at a corner is one pocket encounter, not an extra reflection. Schematic circle radii do not create extra capture regions. Constant speed and point targets are explicit, so there is no friction-based stopping or finite-radius alternative.

The aspect ratio is 5:4, P is on the bottom rail 4 units from the left, and the given direction has slope 1/2 instead of 1. These changes alter the geometry beyond a reflection or rotation of a 45° draft. The θ symbol in the figure is fully specified by tan θ=1/2 in the question.
