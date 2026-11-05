Answer: **C — spatial six-cube elbow.**

Use zero-based cube coordinates (x,y,z): x runs left to right on the front face, y runs from front to back, and z runs upward. These coordinates name the unit grid cells already determined by the picture; they are not extra conditions.

The four unseen cells are (0,1,0), (0,1,1), (1,1,0), and (1,1,1). Dark and white each need two cubes; the hatched piece is complete. The visible white cell (2,1,1) can connect to the other white cubes only through (1,1,1), so this cell is white. If white takes (0,1,0) as its second unseen cube, the dark cell (0,1,1) becomes isolated. If white takes (1,1,0), the two remaining dark cubes at x=0 cannot reach the visible dark column. Therefore white takes (0,1,1), and dark takes the two unseen bottom cells. Together with (2,1,0) and the visible front-right column, they form a spatial six-cube elbow.

The dark cells are `[[0, 1, 0], [1, 1, 0], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0]]`. A rotated and translated representation of the same shape is `[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 2], [1, 1, 2], [2, 1, 2]]`.

Exhaustive uniqueness certificate: the checker recovers each known cube material from the actual three rendered outer faces. It considers all 81 assignments of materials to the 4 unseen cells. Exactly 6 meet the stated piece volumes; exactly 1 also make every piece face-connected. Thus all admissible internal assemblies, independently of the choices and private construction, give the same dark shape. The complete volume-consistent assignment ledger and all valid assemblies are retained in math_check.json.

Choice check (all 24 proper 3D rotations, with translation normalization):

- A: planar two-by-three rectangle — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 2, 3] differ from the target [2, 3, 3].
- B: planar long L hexacube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 3, 4] differ from the target [2, 3, 3].
- C: spatial six-cube elbow — matches the derived dark cube set under a proper rotation.
- D: planar staircase hexacube — does not match the derived dark set under any of the 24 proper rotations; its bounding-box extents [1, 3, 4] differ from the target [2, 3, 3].
- E: spatial four-arm hexacube — does not match the derived dark set under any of the 24 proper rotations; its face-adjacency degrees [1, 1, 1, 2, 2, 3] differ from the target [1, 1, 2, 2, 2, 2].

There is no reliance on a hidden authored coordinate: the hidden model is consulted only after exhaustive solving, to verify that it is one valid witness. The question explicitly requires a filled box, one connected piece per material, equal stated volumes, and proper rotations without reflections. Every cube of every choice has a visible face, and each option has exactly the required number of cubes.

Change from Solid190: 3×2×3 box; 3 pieces of 6 cubes; spatial six-cube elbow; new complete partition and exposed material pattern.
Across this set the targets are L, zigzag, three-axis corner, a spatial five-cube chain, and a spatial six-cube elbow; they are distinct proper-rotation classes.

Status: unreviewed_original. No formal number, Specialvar, Quick Test, Pass, or Collect.
