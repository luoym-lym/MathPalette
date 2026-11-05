Answer: **B — planar L tetracube.**

Use zero-based cube coordinates (x,y,z): x runs left to right on the front face, y runs from front to back, and z runs upward. These coordinates name the unit grid cells already determined by the picture; they are not extra conditions.

There are two unseen cells, (0,1,0) and (1,1,0). The dark piece and the white piece each need one cube; the hatched piece already has four. The white cube must be (1,1,0), because (0,1,0) would not touch any of its three visible cubes. Hence the dark cube is (0,1,0). Together with the three visible bottom-front cubes, this gives a planar three-cube row with a fourth cube attached at an end: an L tetracube.

The dark cells are `[[0, 0, 0], [0, 1, 0], [1, 0, 0], [2, 0, 0]]`. A rotated and translated representation of the same shape is `[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0]]`.

Exhaustive uniqueness certificate: the checker recovers each known cube material from the actual three rendered outer faces. It considers all 9 assignments of materials to the 2 unseen cells. Exactly 2 meet the stated piece volumes; exactly 1 also make every piece face-connected. Thus all admissible internal assemblies, independently of the choices and private construction, give the same dark shape. The complete volume-consistent assignment ledger and all valid assemblies are retained in math_check.json.

Choice check (all 24 proper 3D rotations, with translation normalization):

- A: planar zigzag tetracube — does not match the derived dark set under any of the 24 proper rotations; its pairwise squared cube-center distances differ from the target.
- B: planar L tetracube — matches the derived dark cube set under a proper rotation.
- C: three-axis corner tetracube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [2, 2, 2] differ from the target [1, 2, 3].
- D: planar T tetracube — does not match the derived dark set under any of the 24 proper rotations; its face-adjacency degrees [1, 1, 1, 3] differ from the target [1, 1, 2, 2].
- E: spatial skew-chain tetracube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [2, 2, 2] differ from the target [1, 2, 3].

There is no reliance on a hidden authored coordinate: the hidden model is consulted only after exhaustive solving, to verify that it is one valid witness. The question explicitly requires a filled box, one connected piece per material, equal stated volumes, and proper rotations without reflections. Every cube of every choice has a visible face, and each option has exactly the required number of cubes.

Change from Solid190: 3×2×2 box; 3 pieces of 4 cubes; planar L tetracube; new complete partition and exposed material pattern.
Across this set the targets are L, zigzag, three-axis corner, a spatial five-cube chain, and a spatial six-cube elbow; they are distinct proper-rotation classes.

Status: unreviewed_original. No formal number, Specialvar, Quick Test, Pass, or Collect.
