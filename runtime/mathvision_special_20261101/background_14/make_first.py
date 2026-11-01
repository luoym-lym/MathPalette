from design_tools import *
q='Solid125';g=[]
for a,b,col,role in [
([0,0,0],[3,0,0],RED,'Full cube front-face horizontal extent, matched to red cavity back-face extent'),
([0,0,0],[0,0,3],RED,'Full cube front-face vertical extent, paired with red cavity vertical extent'),
([6.5,2,3],[8.5,2,3],RED,'White cavity back-plane horizontal extent, false whole-face match to full front face'),
([8.5,2,1],[8.5,2,3],RED,'White cavity back-plane vertical extent; grid visibly remains 2 rather than 3 units'),
([3,0,0],[3,3,0],BLUE,'Full cube right-plane depth extent matched to blue cavity side'),
([3,3,0],[3,3,3],BLUE,'Full cube right-plane height extent matched to blue cavity side'),
([6.5,0,1],[6.5,0,3],BLUE,'Cavity left-plane height extent, blue face correspondence'),
([6.5,0,3],[6.5,2,3],BLUE,'Cavity left-plane depth extent, blue face correspondence'),
([0,0,3],[3,0,3],GREEN,'Full cube top-plane width extent matched to green cavity floor'),
([3,0,3],[3,3,3],GREEN,'Full cube top-plane depth extent matched to green cavity floor'),
([6.5,0,1],[8.5,0,1],GREEN,'White cavity floor width extent, false whole-face match to full top face'),
([8.5,0,1],[8.5,2,1],GREEN,'White cavity floor depth extent, green plane correspondence')]:g.append(segment_group(q,a,b,col,role,2))
save(q,'three_plane_area_binding','4.5',g,'Match each of three white cavity planes to a full cube face by red/blue/green extent pairs; target the wrong substitution of three full faces for three 2-by-2 cut planes, giving 9*3/6=4.5 kg.','The original cube has 6*3^2=54 unit faces. The white planes are three 2-by-2 squares, totaling12. Uniform paint9/54kg per unit area gives2kg. Edge colors express no equal-area condition; 3-versus2 subdivisions remain visible. The boundary pairs are existing edges only.','No new closed contour/cut, no fill changes. Colors pair planes but do not assert equality. All 3x3/2x2 unit grids must remain readable on actual candidate PNG.')
q='Solid147';g=[]
g.append(named(q,['givene20','givene12'],RED,'Two existing edges of the upper visible white square, keyed to upper terminal square of E',2))
g.append(named(q,['givene27','givene33'],BLUE,'Existing outer edges at the lower rear-right white square, keyed to the receding lower branch of E',2))
g.append(named(q,['option4e16','option4e18'],RED,'Corresponding two-edge motif on E upper terminal cube',2))
g.append(named(q,['option4e14','option4e15'],BLUE,'Corresponding lower rear branch edges of E, encouraging false nonplanar rather than hidden planar connectivity',2))
save(q,'white_terminal_tripod_binding','E',g,'Bind the two exposed white terminal features of the cuboid to the upper and receding terminal features of E using red/blue paired existing edges. Wrongly extrapolate a nonplanar tripod from the two visible panels, ignoring the forced hidden row.','The 3x2x2 cuboid has12 cells. The four light cubes and four dark cubes are all fixed by visible material classes. Their complement is white at (0,1,0),(1,1,0),(2,1,0),(1,1,1), a planar T. Its degree sequence is3,1,1,1 and all cells are coplanar, matching D. E also branches atdegree3 but its three arms span3D, hence cannot be a rotation. Color marks change no material fill or connectivity.','Panels are small; actual PNG must show top white versus lower right white and all five options. Existing edge overlays only, no extra cube/partition. Check each chosen stable edge really bounds white rather than dark.')
