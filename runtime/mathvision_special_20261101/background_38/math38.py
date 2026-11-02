from common38 import *
from fractions import Fraction as F
from itertools import combinations
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def area(p):return abs(sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p)))) if p else F(0)
def clip(poly,a,b):
    out=[]
    if not poly:return out
    for p,q in zip(poly,poly[1:]+poly[:1]):
        cp=cross(sub(b,a),sub(p,a));cq=cross(sub(b,a),sub(q,a))
        if cp>=0:out.append(p)
        if (cp>0 and cq<0) or (cp<0 and cq>0):
            t=cp/(cp-cq);out.append(tuple(p[i]+t*(q[i]-p[i]) for i in range(2)))
    return out
ABC=[(F(0),F(1)),(F(4),F(0)),(F(3),F(3))]
cells=[]
for i in range(6):
    for j in range(6-i):
        for orient,verts in [('up',[(i,j),(i+1,j),(i,j+1)]),('down',[(i+1,j),(i+1,j+1),(i,j+1)])]:
            if orient=='down' and i+j>4:continue
            poly=[tuple(map(F,p)) for p in verts]
            for a,b in zip(ABC,ABC[1:]+ABC[:1]):poly=clip(poly,a,b)
            ar=area(poly)
            cells.append(dict(id=f'{orient}_{i}_{j}',vertices=verts,clipped_vertices=[[str(v) for v in p] for p in poly],area=str(ar)))
partials=[c for c in cells if 0<F(c['area'])<1]
groups=[]
for n in range(2,7):
    for combo in combinations(partials,n):
        ar=sum(F(c['area']) for c in combo);err=n-ar
        if err.denominator==1 and 1<=err<=4:groups.append(dict(cells=[c['id'] for c in combo],actual_area=str(ar),counted_as=n,result=str(11+err)))
    if groups:break
out={
'Plane179':dict(method='Skew lattice e1=(1,0), e2=(1/2,sqrt(3)/2); doubled determinant equals unit-small-triangle area.',ABC=[[str(x) for x in p] for p in ABC],area=str(area(ABC)),cell_count=len(cells),full_inside=sum(c['area']=='1' for c in cells),all_cells=cells,small_fragment_groups=groups[:20],proof='A=(0,1),B=(4,0),C=(3,3), determinant (4,-1),(3,2)=11. Gray ABC is unique; lattice and boundaries unchanged.'),
'Plane188':dict(proof='Two disjoint 1x6 vertical stems and a parallelogram with horizontal base1 and perpendicular height6 have area6+6+6=18.',correct='18',wrong='12+2*sqrt(10)',wrong_derivation='Diagonal side vector(2,-6) has length sqrt(40)=2sqrt(10). Substituting it for the perpendicular height gives 12+2sqrt(10), while real parallelogram area is6.'),
'Plane224':dict(proof='Small side1. Their combined width3 is side of middle square. Next square side3+1=4. Top side3+4=7. Whole width7 height7+4=11, area77.',correct='77',wrong='77/9',wrong_derivation='Misbind three-unit span to one-unit base; incorrectly set middle side1, smallest side1/3, lower-right4/3 and top7/3; area (7/3)(11/3)=77/9. Explicit three1 labels refute this unit substitution.'),
'Plane229':dict(proof='A one-square-wide border around n-by-n unit picture uses (n+2)^2-n^2=4n+4 tiles. The32 tiles on7cm imply tile side1cm from4(7/s+1)=32. New n=10 needs44.',correct='44',wrong='48',wrong_derivation='Four12-tile sides include the same four corner squares twice:4*12=48. Subtract4 yields44.'),
'Plane250':dict(proof='Fin5d=25=>d5. Pin5d+4v=37=>v3. Rin5h+6v=38=>h4. Tin3d+4v+2h=15+12+8=35; d^2=h^2+v^2 verifies rectangle consistency.',correct='35',wrong='47',wrong_derivation='Rin up-horizontal-down U spans one tile horizontally but has total3+4+3=10. Transfer that total to each of Tin two horizontal4dm advances yields3*5+4*3+2*10=47.'),
'Plane254':dict(proof='Widths a,b,c,d>0 sum27. Actual segments (a+b)/2 and(c+d)/2 sum13.5, option B.',correct='B',wrong='E',wrong_derivation='Misbind each left center to its right rectangle boundary: center1 a/2 ->a; center3 a+b+c/2->a+b+c. Misread sum=13.5-(a+c)/2=(b+d)/2 depends on division.'),
'Plane256':dict(proof='Let lengths a,a+25,a+50,a+75. Sum individual perimeters invariant. S contact sum a+(a+25)+(a+50)=3a+75. T contact sum(a+25)+(a+25)+a=3a+50. Union perimeter difference=2*(25)=50 independent of a.',correct='50',wrong='25',wrong_derivation='The third-length ribbon right-side interval [a+25,a+50] goes from contact in S to exposed in T and is25 long. Counting just this highlighted exposure misses the matching25 interval of the longest ribbon left side. Other changed exposed intervals sum0; true net50. Only this ONE actual transported edge is marked in both scenes; paper ink interpretation is consistent with the translation of that ribbon.',frozen_example_a=25),
'Plane258':dict(proof='Small sides1 unit=20cm. Square side sequence top1,1,2,3 and lower2,1,1,1,2,3. Ordered black maximal straight lengths1,1,2,2,2,2,2,3,4,1,1 total21 =>420cm, C.',correct='C',wrong='B',wrong_derivation='Endpoint-pair bind actual first1-unit vertical to third2-unit vertical, count third as1. Underestimate one20cm unit:400, B. Black route remains black throughout its segments; endpoint colored nodes do not remove marked route segments.' )}
write(TASK/'math_audit.json',out)
print(json.dumps({q:{k:v for k,v in m.items() if k!='all_cells'} for q,m in out.items()},ensure_ascii=False,indent=2))
