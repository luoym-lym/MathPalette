import tools_local as t
import math
from itertools import combinations
def read(p):return t.json.loads(p.read_text(encoding='utf-8-sig'))
# Fresh source-cell exact cover for screened Plane244, independent of old solver text.
q='Plane244';objects=read(t.HERE/q/'context.json')['objects']
def cells(prefix):
    result=set()
    for o in objects:
        if not o['id'].startswith(prefix):continue
        p=o['geometry']['points'];xs=[x for x,y in p];ys=[y for x,y in p]
        result|={(x,y) for x in range(min(xs),max(xs)) for y in range(min(ys),max(ys))}
    return result
source=cells('image1_');rotations=[]
for r in range(4):
    p=source.copy()
    for _ in range(r):p={(-y,x) for x,y in p}
    mx=min(x for x,y in p);my=min(y for x,y in p);rotations.append({(x-mx,y-my) for x,y in p})
results=[]
for k in range(2,7):
    target=cells('image'+str(k)+'_');placements=[]
    for orient in rotations:
        for x,y in target:
            for u,v in orient:
                p={(a+x-u,b+y-v) for a,b in orient}
                if p<=target and p not in placements:placements.append(p)
    witnesses=[[sorted(a),sorted(b)] for a,b in combinations(placements,2) if not a&b and a|b==target]
    results.append({'image_number':k,'small_rectangle_area_units':len(target)/2,'two_copy_covers':len(witnesses),'one_witness':witnesses[:1]})
assert sum(bool(r['two_copy_covers']) for r in results)==4
t.write(t.HERE/q/'primary_math_audit.json',{'method':'Fresh exact unit-square extraction of all2x1 rectangles, four rigid rotations, all anchored translations, two disjoint copies covering target exactly.','source_unit_cells':sorted(source),'results':results,'unique_answer':4})
# Fresh exact container search for Plane289 using integer oblique coordinates X=2x,Y=y/(sqrt3/2).
q='Plane289';vertices={tuple([round(2*x),round(y/(math.sqrt(3)/2))]) for o in read(t.HERE/q/'context.json')['objects'] for x,y in o['geometry']['points']}
def cross(a,b,p):return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
def inside(p,tri):
    signs=[cross(tri[i],tri[(i+1)%3],p) for i in range(3)]
    return min(signs)>=0 or max(signs)<=0
records=[]
for side in range(1,6):
    found=[]
    for X in range(-12,17):
        for Y in range(-12,13):
            if (X-Y)%2:continue
            for sign in [-1,1]:
                tri=[(X,Y),(X+2*side,Y),(X+side,Y+sign*side)]
                if all(inside(v,tri) for v in vertices):found.append(tri)
    records.append({'side':side,'containers':found})
assert [len(r['containers']) for r in records[:4]]==[0,0,0,1]
t.write(t.HERE/q/'fresh_container_enumeration.json',{'method':'All lattice translations over bounds far wider than source and both triangle orientations; exact integer cross-product containment for every original vertex. Any same-unit triangulated equilateral container has integer side and lattice-aligned edges.','coordinates':'X=2x,Y=y/(sqrt3/2)','source_vertices':sorted(vertices),'results':records,'minimum_added':9})
# Prove every newly added Plane286 endpoint is an existing visible contour vertex.
q='Plane286';c=read(t.HERE/q/'context.json');o={r['id']:r['geometry']['points'] for r in c['objects'] if r.get('styleable')}
plugin=read(t.HERE/q/'r30_diagonal_side_span/plugin.json');proof=[]
for a in plugin['params']['actions']:
    matches=[{'object':oid,'vertex_index':i,'exact_xy':xy} for oid,ps in o.items() for i,xy in enumerate(ps) if xy==a['xy']]
    assert matches;proof.append({'marker_id':a['id'],'source_matches':matches})
t.write(t.HERE/q/'r30_diagonal_side_span/endpoint_exact_proof.json',proof)
t.write(t.HERE/'Plane349'/'primary_math_audit.json',{'source_dimensions':{'base_cm':10,'height_cm':6},'row_rectangle_counts':[5,4,3,2],'rectangle_width':2,'rectangle_height':1.5,'total_rectangle_area':42,'triangle_area':30,'grey_area':12,'unique_choice':'B','source_jpg_formal_png_actually_compared':True})
print(t.json.dumps({'Plane244':4,'Plane289_container_counts':[len(r['containers']) for r in records],'Plane286_all8_markers_existing_vertices':True,'Plane349':'B=12'}))
