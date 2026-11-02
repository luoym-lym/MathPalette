from env50 import *
from dataset_tools.catalog import read
from fractions import Fraction as F
import math
out={}
g={tuple(v) for v in read(OWN/'Plane176/math_proof.json')['gray_cells']}
def perimeter(cells):return sum((x+dx,y+dy) not in cells for x,y in cells for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
assert len(g)==9 and perimeter(g)==20
rounds=[];current=set(g)
while True:
    nxt={(x,y) for x in range(8) for y in range(8) if (x,y) not in current and sum((x+dx,y+dy) in current for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])>=2}
    if not nxt:break
    previous=perimeter(current);current|=nxt;rounds.append({'new_cells':sorted(nxt),'number':len(nxt),'perimeter_before':previous,'perimeter_after':perimeter(current)})
assert len(current)==25 and perimeter(current)==20
out['Plane176']={'gray_count':9,'initial_perimeter':20,'iterative_rounds':rounds,'extra_cells':16,'not_solver_input':True}
# Explicit folded centers after unfolding a45degree billiard ray.
def fold(x,w):
    z=x%(2*w);return z if z<=w else 2*w-z
hits=[]
for t in [4,8,10,16]:hits.append({'time':t,'wall_hit':[fold(t,8),fold(2+t,6)]})
assert hits[-1]['wall_hit']==[0,6]
out['Plane177']={'wall_hits':hits,'first_corner_time':16,'pocket':'C'}
alpha=F(70);L=180+alpha;R=360-alpha
left=2*L-R;right=2*R-L
assert left==210 and right==330 and right-left==120
out['Plane180']={'alpha':70,'first_arm_directions':[int(L),int(R)],'reflected_final_directions':[int(left),int(right)],'beta':int(right-left),'source_supplement':110}
M=[F(17,2),F(4)];N=[F(15,2),F(0)];Dp=[F(32,17),F(128,17)];A=[F(0),F(4)]
pts=[A,N,M,Dp];area=abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(pts,pts[1:]+pts[:1])))/2
assert area==32
out['Plane181']={'exact_M':[str(x) for x in M],'exact_N':[str(x) for x in N],'exact_Dprime':[str(x) for x in Dp],'exact_quadrilateral_area':str(area),'triangle_areas':[17,15],'wrong_copied_base_areas':[15,15]}
# Track the actual marked material vertex around12corner pivots, without drawing extra positions.
vertices=[[1.,0.],[1.,1.],[1+math.sqrt(3)/2,.5]];start=[v[:] for v in vertices];events=[]
corners=[[1.,1.],[0.,1.],[0.,0.],[1.,0.]]
co,si=math.cos(7*math.pi/6),math.sin(7*math.pi/6)
for k in range(12):
    pivot=corners[k%4];radius=math.dist(vertices[2],pivot)
    assert abs(radius)<1e-9 or abs(radius-1)<1e-9
    nv=[]
    for x,y in vertices:
        dx,dy=x-pivot[0],y-pivot[1];nv.append([pivot[0]+co*dx-si*dy,pivot[1]+si*dx+co*dy])
    vertices=nv
    events.append({'pivot_number':k+1,'pivot_xy':pivot,'marked_radius':0 if radius<1e-9 else 1,'marked_vertex_after':vertices[2],'all_labeled_vertices_back':all(math.dist(a,b)<1e-9 for a,b in zip(vertices,start))})
assert sum(e['marked_radius'] for e in events)==8 and events[-1]['all_labeled_vertices_back'] and not any(e['all_labeled_vertices_back'] for e in events[:-1])
out['Plane182']={'pivot_events_not_drawn':events,'zero_radius_events':4,'unit_radius_events':8,'turn_per_event':'7pi/6','length':'28pi/3','one_lap_marked_length':'7pi/2','first_joint_return_pivot':12}
assert F(360)/(180-(360-2*108))==10
out['Plane183']={'pentagon_interior':108,'pentagon_exterior':72,'hole_interior':144,'ring_advance':36,'plates':10,'wrong_advance':72,'wrong_count':5}
s=read(OWN/'Plane197/formal_scene_snapshot.json');p=[o for o in s['objects'] if o['id'].startswith('path')];lengths=[math.dist(*o['points']) for o in p]
assert len(p)==9 and all(abs(x-(6 if k%2==0 else 4))<1e-10 for k,x in enumerate(lengths))
out['Plane197']={'black_path_lengths':lengths,'black_path_length_sum':sum(lengths),'five_long_four_short':True}
dump(OWN/'mathematical_calculation_checks.json',out)
print(json.dumps({q:{k:v for k,v in data.items() if k not in ['pivot_events_not_drawn','iterative_rounds']} for q,data in out.items()},ensure_ascii=False))
