The answer is **B**, the planar L tetracube: three cubes in a straight row and a fourth attached at an end.

For this solution only, number unit cells `(x,y,z)` from zero, with x increasing from left to right across the front, y increasing from front to back, and z increasing upward. A coordinate names a cube, not a point. This is a way to describe the visible grid; it is not an additional condition.

There are only two cells not identified by a front, right or top face: `(0,1,0)` and `(1,1,0)`. Count each visible cube once even if two faces of it are shown. The light-grey piece already has four cubes, the dark-grey piece has three, and the white piece has three. Thus the two hidden cells must contain one dark-grey cube and one white cube.

If `(0,1,0)` were dark grey, all its in-box face neighbours would be white or light grey: `(0,0,0)` is light grey, `(0,1,1)` is white, and the other hidden cell would be white. The dark-grey piece would be disconnected. Therefore `(1,1,0)` is dark grey and `(0,1,0)` is white.

The complete white set is `{(0,1,0), (0,1,1), (1,1,1), (2,1,1)}`. It has the L shape in B. The other pieces are connected in this completion, so it exists as well as being forced.

The distractors fail for different geometric reasons:

- A is a square slab, containing a four-cube adjacency cycle.
- C is a T with a cube having three face neighbours.
- D is a planar zigzag, with no straight row of three cubes.
- E is a nonplanar corner, with branches along three independent axes.

The white L has adjacency degrees `1,1,2,2`, is planar and has a collinear triple. `math_check.py` enumerates both size-compatible hidden assignments before testing all pieces for face connectivity. Exactly one survives. It then compares all five options under all 24 proper cubic rotations, allowing translations and excluding reflection. No private hidden coordinates are used to infer the answer.

The filled cuboid, one piece per shade, four cubes per piece, and face connectivity are explicit in the English question. These conditions remove ambiguity about separate pieces having the same shade or gaps in the cuboid. Compared with Solid198, this is a smaller 3 x 2 x 2 cuboid made of three pieces, and the target changes from a zigzag to an L; the visible filling and inference are new.
