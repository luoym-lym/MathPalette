Answer: **A — three-axis corner tetracube.**

Use zero-based cube coordinates (x,y,z): x runs left to right on the front face, y runs from front to back, and z runs upward. These coordinates name the unit grid cells already determined by the picture; they are not extra conditions.

The only unseen cells are (0,1,0), (1,1,0), and (2,1,0). White and gray are already complete. Dark needs one cube and the hatched piece needs two. The three visible dark cubes are (2,0,0), (2,0,1), and (3,0,0). Of the unseen cells, only (2,1,0) shares a face with this set. It is therefore dark. One central cube now has three neighbors in three perpendicular directions, giving the spatial corner tetracube. The other two unseen cubes complete the connected hatched piece.

The dark cells are `[[2, 0, 0], [2, 0, 1], [2, 1, 0], [3, 0, 0]]`. A rotated and translated representation of the same shape is `[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]`.

Exhaustive uniqueness certificate: the checker recovers each known cube material from the actual three rendered outer faces. It considers all 64 assignments of materials to the 3 unseen cells. Exactly 3 meet the stated piece volumes; exactly 1 also make every piece face-connected. Thus all admissible internal assemblies, independently of the choices and private construction, give the same dark shape. The complete volume-consistent assignment ledger and all valid assemblies are retained in math_check.json.

Choice check (all 24 proper 3D rotations, with translation normalization):

- A: three-axis corner tetracube — matches the derived dark cube set under a proper rotation.
- B: planar L tetracube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 2, 3] differ from the target [2, 2, 2].
- C: planar zigzag tetracube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 2, 3] differ from the target [2, 2, 2].
- D: planar T tetracube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 2, 3] differ from the target [2, 2, 2].
- E: spatial skew-chain tetracube — does not match the derived dark set under any of the 24 proper rotations; its face-adjacency degrees [1, 1, 2, 2] differ from the target [1, 1, 1, 3].

There is no reliance on a hidden authored coordinate: the hidden model is consulted only after exhaustive solving, to verify that it is one valid witness. The question explicitly requires a filled box, one connected piece per material, equal stated volumes, and proper rotations without reflections. Every cube of every choice has a visible face, and each option has exactly the required number of cubes.

Change from Solid190: 4×2×2 box; 4 pieces of 4 cubes; three-axis corner tetracube; new complete partition and exposed material pattern.
Across this set the targets are L, zigzag, three-axis corner, a spatial five-cube chain, and a spatial six-cube elbow; they are distinct proper-rotation classes.

Status: unreviewed_original. No formal number, Specialvar, Quick Test, Pass, or Collect.
