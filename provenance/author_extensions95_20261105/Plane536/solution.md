# Solution

**Answer: D — Pocket D (the bottom-left corner).**

Here W=10, H=6 and P=(2,6). The outgoing arrow points southeast at 45°, so the unfolded path is (2+t,6−t), t>0. At a corner the vertical coordinate is a multiple of 6, hence t=6k for a positive integer k. The horizontal condition is 2+6k=10m, equivalently 1+3k=5m. Therefore k≡3 (mod 5), and the least positive solution is k=3. At t=18 the unfolded position is (20,−12), which folds to (0,0), Pocket D.

The preceding boundary encounters, in order, are t=6 at (8,0), t=8 at (10,2), and t=12 at (6,6). None is a pocket. At t=18 the left and bottom rails are reached together at D and capture occurs immediately. Therefore A, B and C cannot be the first pocket, and the infinite-motion option E is false.

The table origin used below is its bottom-left corner. These coordinates merely encode the dimensions and P's location stated in the question. The unit grid is a reference grid, not a set of reflecting walls. The black dot and segment show the incoming motion; the arrow shows the motion after reflection at P. The acute angle is measured against the drawn rail ray, not its normal.

Unfolding a specular reflection continues the ray straight into a reflected copy of the table. A coordinate u folds into an interval of length L by taking r = u mod 2L, then returning r for r ≤ L and 2L−r otherwise. At a pocket, capture takes place immediately; simultaneous arrival at two rails at a corner is one pocket encounter, not an extra reflection. Schematic circle radii do not create extra capture regions. Constant speed and point targets are explicit, so there is no friction-based stopping or finite-radius alternative.

This draft changes the aspect ratio to 5:3, uses a non-midpoint top-rail start, and sends the reflected ball southeast. The reflection order bottom/right/top differs from the parent and from the left-rail drafts; this is not a rotation or scaling of their geometry.
