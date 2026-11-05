Answer: **E — spatial bent-chain pentacube.**

Use zero-based cube coordinates (x,y,z): x runs left to right on the front face, y runs from front to back, and z runs upward. These coordinates name the unit grid cells already determined by the picture; they are not extra conditions.

The four unseen cells are (x,1,0) for x=0,1,2,3. White is complete, dark and hatched each need one cube, and gray needs two. The visible dark cube (3,1,1) is separated from the dark front-bottom row; its only possible dark neighbor among the unseen cells is (3,1,0). Hence that cell is dark. Gray must then take (1,1,0) and (2,1,0): choosing either pair containing (0,1,0) leaves gray disconnected from its visible cells. The remaining cell (0,1,0) is hatched. The dark piece is a chain of five cubes with two bends in perpendicular planes.

The dark cells are `[[1, 0, 0], [2, 0, 0], [3, 0, 0], [3, 1, 0], [3, 1, 1]]`. A rotated and translated representation of the same shape is `[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [1, 1, 0]]`.

Exhaustive uniqueness certificate: the checker recovers each known cube material from the actual three rendered outer faces. It considers all 256 assignments of materials to the 4 unseen cells. Exactly 12 meet the stated piece volumes; exactly 1 also make every piece face-connected. Thus all admissible internal assemblies, independently of the choices and private construction, give the same dark shape. The complete volume-consistent assignment ledger and all valid assemblies are retained in math_check.json.

Choice check (all 24 proper 3D rotations, with translation normalization):

- A: planar P pentacube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 2, 3] differ from the target [2, 2, 3].
- B: planar U pentacube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 2, 3] differ from the target [2, 2, 3].
- C: planar long-stem T pentacube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 3, 3] differ from the target [2, 2, 3].
- D: spatial branched pentacube — does not match the derived dark set under any of the 24 proper rotations; its face-adjacency degrees [1, 1, 1, 2, 3] differ from the target [1, 1, 2, 2, 2].
- E: spatial bent-chain pentacube — matches the derived dark cube set under a proper rotation.

There is no reliance on a hidden authored coordinate: the hidden model is consulted only after exhaustive solving, to verify that it is one valid witness. The question explicitly requires a filled box, one connected piece per material, equal stated volumes, and proper rotations without reflections. Every cube of every choice has a visible face, and each option has exactly the required number of cubes.

Change from Solid190: 5×2×2 box; 4 pieces of 5 cubes; spatial bent-chain pentacube; new complete partition and exposed material pattern.
Across this set the targets are L, zigzag, three-axis corner, a spatial five-cube chain, and a spatial six-cube elbow; they are distinct proper-rotation classes.

Status: unreviewed_original. No formal number, Specialvar, Quick Test, Pass, or Collect.
