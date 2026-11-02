from tools55 import *
from fractions import Fraction as F
from itertools import product, permutations
import numpy as np
import math

def scene(q): return read(PROJECT/BRANCH/eligibility(q)['record']['scene'])

# Signed coordinate-axis junctions; right = incoming tangent cross outward normal.
axes=[np.eye(3,dtype=int)[i]*sgn for i in range(3) for sgn in [1,-1]]
states=[]
for a in axes:
 for b in axes:
  if a@b: continue
  for first_right in [True,False]:
   path=[a,b];right=first_right
   for i in range(1,13):
    if i>1 and np.array_equal(path[-1],a):break
    nxt=(-1 if right else 1)*np.cross(path[-2],path[-1]);path.append(nxt);right=not right
   assert len(path)-1==6
   states.append(dict(start=a.tolist(),first_next=b.tolist(),first_right=first_right,path=[p.tolist() for p in path],first_return=6))
write(HERE/'Solid195/primary_math.json',dict(proof='The only true junctions are the six signed unit axes. For successive junctions p,q the arrival tangent is -p and the outward normal is q; a right turn selects next junction -p cross q, a left turn selects p cross q. The rule alternates. All 48 directed initial states return first at six arcs. Example +x,+y,-z,-x,-y,+z,+x; at return the outgoing direction and next turn phase also reset. Counting only positions therefore does NOT produce a different return time; only counting two-arc procedure cycles instead of arcs gives 3.',all_states=states,correct_answer=6))

s=scene('Solid200');visible={p for p in product(range(3),repeat=3) if p[0]==0 or p[1]==0 or p[2]==2};gray={0:set(),1:set()};faces=[]
for o in s['objects']:
 if o['type']!='face':continue
 view=int(o['id'][4]); pts=np.array([s['points'][p] for p in o['points']],dtype=float);pts[:,2]-=5 if view==0 else 0
 center=pts.mean(axis=0);cell=tuple(min(2,math.floor(v)) for v in center);assert cell in visible
 gray[view].add(cell);faces.append(dict(id=o['id'],view=view,actual_quad=pts.tolist(),cell=cell))
white={i:visible-gray[i] for i in [0,1]};cases=[]
for order in permutations(range(3)):
 for signs in product([-1,1],repeat=3):
  R=np.array([[signs[i] if j==order[i] else 0 for j in range(3)] for i in range(3)])
  if round(np.linalg.det(R))!=1:continue
  transform=lambda cells:{tuple((R@(np.array(c)-1)+1).tolist()) for c in cells}
  g=gray[0]|transform(gray[1]);w=white[0]|transform(white[1]);conflict=g&w
  cases.append(dict(matrix=R.tolist(),conflicts=sorted(conflict),compatible=not conflict,white_union=sorted(w),gray_union=sorted(g),free=sorted(set(product(range(3),repeat=3))-w-g),maximum_gray=27-len(w),duplicated_white=sorted(white[0]&transform(white[1]))))
compatible=[c for c in cases if c['compatible']];assert len(compatible)==1 and compatible[0]['maximum_gray']==9
write(HERE/'Solid200/primary_math.json',dict(method='Read actual gray face quad coordinates, not the source_patterns indexing convention. Every other visible cell is white. Enumerate every proper signed permutation of the two cube frames.',gray_face_audit=faces,local_gray={str(k):sorted(v) for k,v in gray.items()},local_white={str(k):sorted(v) for k,v in white.items()},all_24=cases,compatible=compatible,proof='Only one rotation avoids white/gray contradiction. It forces 18 different white cubes, 5 gray cubes, and leaves 4 cells unconstrained including the center. All four may be gray, attaining 9. The 30 two-view white observations include 12 repeats. Naive duplicate subtraction yields -3, not a credible new preset; omitting only the hidden center would give8 but there is no actual visible source/receiver for that interior cube.'))

write(HERE/'Solid205/primary_math.json',dict(proof='The two sheets unroll to congruent 2*pi*r by h rectangles. Joining the actual vertical cut edges adds their horizontal widths and preserves height: 2*pi*R=4*pi*r, H=h. Hence R=2r and V=pi*(2r)^2*h=4*100=400. Hollow enclosed air is not material conserved by gluing.',correct_answer=400))

s=scene('Solid206');p={k:np.array(v) for k,v in s['points'].items()};ss=6*math.sqrt(2);h=6
assert np.allclose(p['L'],[-ss/2,ss/2,h]) and np.allclose(p['R'],[3*ss/2,ss/2,h])
edgechecks={o['id']:float(np.linalg.norm(p[o['points'][0]]-p[o['points'][1]])) for o in s['objects']}
write(HERE/'Solid206/primary_math.json',dict(proof='The two equal lateral edges from each ridge endpoint put it on the perpendicular bisector plane of the corresponding square side. The four length-s constraints force the ridge parallel to the opposite base sides: otherwise its length is less than 2s (subtracting distance equations gives the lateral components). Up to rigid symmetry, base corners are (0,0,0),(s,0,0),(s,s,0),(0,s,0), ridge L=(-s/2,s/2,h), R=(3s/2,s/2,h). Thus h^2=s^2-s^2/4-s^2/4=s^2/2; h=6. At height t*h, width in x is s*(1+t), in y is s*(1-t), because faces ALRB and DLRC are planar. Area=s^2*(1-t^2); integrate t=0..1: V=(2/3)*s^2*h=288. The equilateral triangular end faces are NOT parallel; their connector lengths are s,s,2s, so they are not the bases of a prism.',world_points={k:p[k].tolist() for k in ['A','B','C','D','L','R']},actual_edge_lengths=edgechecks,height=h,correct_answer=288,prospective_wrong_prism_formula='Using one equilateral end-face area sqrt(3)*s^2/4 and treating the true ridge2s as a perpendicular prism length gives sqrt(3)*s^3/2=216*sqrt(6), about529.0898.'))

s=scene('Solid207');panels={}
for i in range(6):
 keys=[f'f{i}_{k}' for k in range(3 if i%2==0 else 5)];p=[np.array(s['points'][k]) for k in keys];lengths=[float(np.linalg.norm(p[(j+1)%len(p)]-p[j])) for j in range(len(p))];panels[str(i)]=dict(vertices={k:s['points'][k] for k in keys},edge_lengths=lengths)
cut_vertices=list(permutations([0,6,12]));assert len(cut_vertices)==6
write(HERE/'Solid207/primary_math.json',dict(proof='Intersect [0,12]^3 with x+y+z<=18. The cutting face has vertices all permutations of (0,6,12), a regular hexagon with side6sqrt2 and angles120. Each coordinate0 cube face is exactly a 12x12 square minus a 6-by-6 corner right triangle: three A pentagons with cyclic lengths6,12,12,6,6sqrt2. Each coordinate12 face is a right isosceles triangle with legs6: three B triangles. They attach alternately to the six hexagon sides, with the same cyclic net adjacencies and angles as the actual frozen net. Thus the given six panels plus hexagon realize the convex half-cube; fixed convex face metric rigidity excludes another convex folded volume. The map (x,y,z)->(12-x,12-y,12-z) exchanges the two half-cubes and preserves volume, so V=12^3/2=864.',actual_panels=panels,cut_vertices=cut_vertices,correct_answer=864,prospective_scale_error='If a real input half-side6 is incorrectly identified with a full A panel side12, reconstructing the enclosing cube with side6 instead of12 scales the half-cube volume by1/8, giving108. This is a part-to-whole correspondence error; no equal-length condition is added.'))

write(HERE/'Solid208/primary_math.json',dict(proof='Use the actual frozen labeled cube coordinates A=(0,0,0),B=(1,0,0),C=(1,1,0),D=(0,1,0). M=(1/2,0,0),N=(1,1,1/2). Their plane is 2x+y-4z=1. It also meets BF at P=(1,0,1/4); complete section is D-M-P-N, not triangle D-M-N. The small solid has height (2x+y-1)/4 over 0<=x<=1, max(0,1-2x)<=y<=1. The exact two integrals on x=[0,1/2] and[1/2,1] are1/96 and13/96, totaling7/48. Larger=41/48, hence89. Treating P as a midpoint is inconsistent with the given three-point plane; an explicit fake midpoint/equality is forbidden. Merely drawing the true quarter intersection and assigning it the same color as M would not define one geometrically consistent wrong plane or one defensible new wrong volume.',cut_plane=[2,1,-4,-1],section=[[0,1,0],[.5,0,0],[1,0,.25],[1,1,.5]],integrals=['1/96','13/96'],small='7/48',larger='41/48',correct_answer=89))

write(HERE/'Solid209/primary_math.json',dict(proof='Take line ell as x-axis, half wedge angle alpha, centers on the interior bisector of the pictured common wedge. A radius-r sphere tangent to both planes has center distance r*csc(alpha) from ell. The two equal radius36 centers have x separation72, at x=+-36; tangency forces the radius13 center to x=0. Its distance49 to each large center gives36^2+(36-13)^2*csc(alpha)^2=49^2. Hence csc^2(alpha)=1105/529 and cot(alpha)=24/23. A perpendicular cross-section gives distance from ell to a tangency foot on either plane r*cot(alpha)=312/23. gcd312,23=1, so m+n=335. Assuming perpendicular planes would give13 (sum14), but violates the three sphere tangencies:36^2+2*23^2=2354 !=2401. The actual desired foot is neither a silhouette nor an equator point in the frozen projection.',correct_answer=335,foot_distance='312/23',rejected_right_angle='The apparent page angle is not a given right dihedral; there is no readable actual foot-to-ell segment already shown to which a matching marker can bind without drawing hidden construction through the spheres.'))

write(HERE/'Solid210/primary_math.json',dict(proof='Sector radius10 becomes the slant height. Its arc length is(252/360)*2*pi*10=14*pi; base circumference givesR=7. Axis height=sqrt(10^2-7^2)=sqrt51. A,C,E have slant10 and base radii6,7,8; B,D have axis10 and base radii6,7. Thus C alone matches. Treating10 as base radius, or using complementary108degrees to obtain base3, matches no choice. The only naturally offered wrong choice with correct base7 is D via axis/slant confusion, already tested as D preset on the unchanged old source-radius/axis pair and answeredC/C. Adding a true arc/circumference pairing to that failed mechanism is not independently a new wrong geometric hypothesis.',correct_answer='C',base_radius=7,slant=10,height='sqrt51',choices={'A':{'base':6,'slant':10},'B':{'base':6,'height':10},'C':{'base':7,'slant':10},'D':{'base':7,'height':10},'E':{'base':8,'slant':10}}))
print('Eight independent primary math audits saved; no API calls.')
