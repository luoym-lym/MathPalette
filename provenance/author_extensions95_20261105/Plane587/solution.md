Use the grid corner as origin for calculation only. The shared endpoint is A=C=(5,1)=X. The other endpoints are B=(9,9) and D=(1,9); both segments have squared length 80.

For A→C and B→D, the shared endpoint is fixed, so the centre must be X. The direction vectors (4,8) and (−4,8) have cos θ=3/5 and sin θ=4/5. A rotation by θ≈53.130102° counterclockwise about X maps the segments.

For A→D and B→C, cos θ=−3/5 and sin θ=−4/5, so θ≈233.130102°. The centre must be equidistant from A, B and D, the circumcentre of this isosceles triangle. Equidistance from B and D gives x=5. Setting (y−1)²=4²+(y−9)² gives y=6, so the second centre is T=(5,6). Both endpoint mappings hold exactly.

Therefore **A: X and T**. Y=(5,5) and Z=(5,9) are neither centre; being on the symmetry axis alone is insufficient. All other options omit a valid centre or include an invalid one.

Exhaustiveness and uniqueness: a nonzero segment has two endpoints, so any rotation mapping it onto the other segment must use one of the two endpoint bijections checked above. Each nonidentity rotation matrix has exactly one fixed point. A zero-angle nonzero translation has none. There is no other centre or endpoint case. Angles are measured counterclockwise from the first segment to the second in the calculation; reversing the mapping gives the same centres. The square grid, endpoint locations and point markers supply every condition used; the solution does not rely on undisplayed coordinate axes or private extra constraints.

相对父题的实质变化：两段构成共端点的V形，夹角不是直角；一个旋转中心就是给定端点，另一个是三角形外心，检验程序须处理零半径。
原题状态：unreviewed_original；来源 Author Designed。数学核验和看图不代表用户批准。
