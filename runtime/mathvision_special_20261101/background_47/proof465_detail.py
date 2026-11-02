from env47 import *
import json
from fractions import Fraction as F

def clip(poly,axis,bound,above):
    if not poly:return []
    result=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        ina=a[axis]>=bound if above else a[axis]<=bound
        inb=b[axis]>=bound if above else b[axis]<=bound
        if ina:result.append(a)
        if ina!=inb:
            t=(bound-a[axis])/(b[axis]-a[axis])
            result.append(tuple(a[i]+t*(b[i]-a[i]) for i in [0,1]))
    return result

def area(p):
    if not p:return F(0)
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])))/2

s=json.loads((OWN/'Plane465/formal_scene_snapshot.json').read_text(encoding='utf-8'))
o=next(x for x in s['objects'] if x['id']=='gray0')
p=[tuple(F(v) for v in s['points'][n]) for n in o['points']]
cells=[]
for y in range(5,11):
    for x in range(6):
        q=p
        for axis,bound,above in [(0,x,True),(0,x+1,False),(1,y,True),(1,y+1,False)]:q=clip(q,axis,F(bound),above)
        cells.append({'unit_cell_lower_left':[x,y],'gray_area':str(area(q)),'clipped_exact_vertices':[[str(a),str(b)] for a,b in q]})
half=[c['unit_cell_lower_left'] for c in cells if c['gray_area']=='1/2']
full=[c['unit_cell_lower_left'] for c in cells if c['gray_area']=='1']
assert len(full)==12 and len(half)==8 and sum(F(c['gray_area']) for c in cells)==16
assert sorted(half)==sorted([[2,10],[3,10],[0,7],[0,8],[5,7],[5,8],[2,5],[3,5]])
dump(OWN/'Plane465/exact_cell_decomposition.json',{'method':'Exact rational Sutherland-Hodgman intersection of the actual complete gray0 polygon with each of the36 pre-existing unit grid cells. No image editing or new geometric condition.','full_cell_count':len(full),'half_cell_count':len(half),'full_cells':full,'half_cells':half,'total_dark_area':'16','block_area':36,'ratio':'4/9','actual_eight_half_cells_exactly_match_four_frozen_T_marker_groups':True,'all36cells':cells})
print(json.dumps({'full':full,'half':half,'gray_area':16,'ratio':'4/9'},ensure_ascii=False))
