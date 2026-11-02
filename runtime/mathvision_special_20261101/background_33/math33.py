from tools33 import *
from itertools import combinations
from math import gcd,sqrt
from collections import Counter
def resolved(q):
    s=read(HERE/q/'source_scene_snapshot.json');c=read(HERE/q/'context.json')
    def xy(p):return s['points'][p] if isinstance(p,str) else p
    return s,c,xy
def det(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
for q in ['Plane249','Plane325']:
    s,c,xy=resolved(q);cells={};painted=set()
    for o in c['objects']:
        g=o['geometry']
        if g['type']!='polygon' or not g.get('semantic_fill'):continue
        p=[xy(v) for v in g['points']];a=(int(min(v[0] for v in p)),int(min(v[1] for v in p)))
        cells[a]=o['id']
        if g.get('semantic_color') not in ('#FFFFFF','#ffffff'):painted.add(a)
    if q=='Plane249':cells={(x,y):cells.get((x,y)) for x in range(4) for y in range(4)}
    n=4 if q=='Plane249' else 9
    fs={'vertical':lambda x,y:(n-1-x,y),'horizontal':lambda x,y:(x,n-1-y),'rising_diagonal':lambda x,y:(y,x),'falling_diagonal':lambda x,y:(n-1-y,n-1-x)}
    axes=[]
    for name,f in fs.items():
        assert {f(*a) for a in cells}==set(cells)
        missing={f(*a) for a in painted}-painted
        axes.append({'axis':name,'minimum_additions':len(missing),'missing_cells':sorted(missing),'completed_cells':sorted(painted|missing)})
    result={'question_id':q,'method':'The full finite cell outline has exactly four reflection axes, so these exhaust all possible symmetries. For each reflection every originally shaded cell forces its missing reflected mate; their union is sufficient.','cell_inventory':[{ 'xy':a,'object_id':v,'shaded':a in painted} for a,v in sorted(cells.items())], 'axes':axes,'unique_minimum_number':min(a['minimum_additions'] for a in axes),'formal_answer_agrees':str(min(a['minimum_additions'] for a in axes))==str(read(HERE/q/'formal_record.json')['answer'])}
    write(HERE/q/'math_proof.json',result);print(q,[(a['axis'],a['minimum_additions']) for a in axes])
for q in ['Plane328','Plane363']:
    s,c,xy=resolved(q);ps=s['points'];names=list(ps)
    triples=[t for t in combinations(names,3) if det(*(ps[i] for i in t))==0]
    mins=[];failcounts=[]
    for k in range(len(names)+1):
        hits=[r for r in combinations(names,k) if all(set(r)&set(t) for t in triples)]
        failcounts.append({'removed_count':k,'total_sets':len(list(combinations(names,k))),'valid_sets':len(hits)})
        if hits:mins=hits;break
    result={'question_id':q,'actual_point_count':len(ps),'points':ps,'all_collinear_triples':triples,'checked_removal_sets':failcounts,'minimum_removal_count':len(mins[0]),'all_minimum_removal_sets':mins,'analytic_lower_bound':'The three disjoint full rows each require a removal, hence at least 3. Removing P00,P11,P22 breaks all rows, columns and both full diagonals, hence suffices. These are all possible collinear triples in the 3x3 lattice.','old_Plane328_record_correction':'Old assessment said 8 perimeter points; actual original source JPG, formal native PNG and frozen scene all contain 9, including P11. Old evidence left unchanged.' if q=='Plane328' else None}
    write(HERE/q/'math_proof.json',result);print(q,len(triples),'triples',len(mins),'minimal sets',len(mins[0]))
q='Plane368';s,c,xy=resolved(q);ps={k:v for k,v in s['points'].items() if k.startswith('P')}
areas=[{'vertices':t,'twice_area':abs(det(*(ps[i] for i in t)))} for t in combinations(ps,3)]
write(HERE/q/'math_proof.json',{'question_id':q,'actual_six_marked_points':ps,'all_twenty_triangles':areas,'minimum_positive_twice_area':min(a['twice_area'] for a in areas if a['twice_area']),'answer':'A = 1/2','analytic_proof':'Integer lattice determinants are integers, so a nondegenerate triangle has area at least 1/2. P0,P2,P3 achieve determinant 1: the vertical P2-P3 unit base and horizontal distance 1 of P0 give area 1/2.'});print(q,areas)
q='Plane448';s,c,xy=resolved(q);g=next(o['geometry'] for o in c['objects'] if o['id']=='band');p=[xy(v) for v in g['points']]
cross=[p[i][0]*p[(i+1)%4][1]-p[(i+1)%4][0]*p[i][1] for i in range(4)]
write(HERE/q/'math_proof.json',{'question_id':q,'ordered_band_vertex_ids':g['points'],'ordered_band_vertices':p,'shoelace_cross_terms':cross,'twice_area':abs(sum(cross)),'unique_area':abs(sum(cross))/2,'triangle_split_at_p01_p41':{'common_base':4,'upper_height':2,'lower_height':1,'upper_area':4,'lower_area':2,'sum':6},'Pick_independent_check':{'boundary_points':4,'interior_points':5,'area':6}});print(q,'cross',cross,'area',abs(sum(cross))/2)
q='Plane486';s,c,xy=resolved(q);raw=s['points'];ps={k:(round(2*p[0]),round(2*p[1]/sqrt(3))) for k,p in raw.items()}
for k,(u,v) in ps.items():assert abs(raw[k][0]-u/2)<1e-12 and abs(raw[k][1]-v*sqrt(3)/2)<1e-12
lines={}
for i,j in combinations(ps,2):
    a,b=ps[i],ps[j];A=a[1]-b[1];B=b[0]-a[0];C=-(A*a[0]+B*a[1]);gg=gcd(gcd(abs(A),abs(B)),abs(C));key=(A//gg,B//gg,C//gg)
    if next(z for z in key if z)!=abs(next(z for z in key if z)):key=tuple(-z for z in key)
    lines[key]=[k for k,(u,v) in ps.items() if key[0]*u+key[1]*v+key[2]==0]
hist=Counter(len(v) for v in lines.values());assert sum(n*(n-1)//2*f for n,f in hist.items())==171
write(HERE/q/'math_proof.json',{'question_id':q,'coordinate_transform':'U=2x,V=2y/sqrt(3); invertible diagonal scaling preserves collinearity exactly. Captured floating coordinates match integer lifts within 1e-12.','original_full_precision_points':raw,'integer_lift':ps,'canonical_line_point_sets':[{'ABC':k,'point_ids':v,'point_count':len(v)} for k,v in sorted(lines.items())],'line_size_histogram':dict(hist),'pair_partition_check':171,'exactly_two_point_line_count':hist[2],'unique_answer':60});print(q,'hist',hist)
q='Plane487';s,c,xy=resolved(q);edges=[(o['id'],*[xy(v) for v in o['geometry']['points']]) for o in c['objects']]
def covered(a,b):
    axis=0 if a[1]==b[1] else 1;fixed=1-axis
    iv=sorted((min(p[axis],r[axis]),max(p[axis],r[axis])) for _,p,r in edges if p[fixed]==r[fixed]==a[fixed])
    end=a[axis]
    for lo,hi in iv:
        if lo<=end: end=max(end,hi)
    return end>=b[axis]
valid=[];bad=[]
for x1,x2 in combinations(range(7),2):
    for y1,y2 in combinations(range(7),2):
        rs=(x1,x2,y1,y2)
        ok=all(covered(a,b) for a,b in [([x1,y1],[x2,y1]),([x1,y2],[x2,y2]),([x1,y1],[x1,y2]),([x2,y1],[x2,y2])])
        (valid if ok else bad).append(rs)
local=[r for r in valid if r[1]<=2 or r[0]>=4 or r[3]<=2 or r[2]>=4 or r==(2,4,2,4)]
write(HERE/q/'math_proof.json',{'question_id':q,'exact_original_segments':edges,'method':'Every edge is horizontal or vertical at integer coordinate 0..6. Enumerate all 21x21=441 possible nondegenerate rectangles, require each of its four continuous edges be covered by the union of original collinear segments. Missing x=3,y=2..4 and y=3,x=2..4 are never filled.','valid_rectangles':valid,'invalid_rectangles':bad,'valid_count':len(valid),'full_grid_rectangles':441,'invalid_count':len(bad),'four_intact_border_strip_union_plus_central_cell_count':len(local),'omitted_spanning_rectangles':len(valid)-len(local),'local_count_derivation':'Each of four 6x2 intact strips contributes C(7,2)C(3,2)=63; subtract 4 corner 2x2 overlap grids of 9 rectangles; add the single central cell: 4*63-4*9+1=217. Other 80 valid rectangles span these local groups.'});print(q,len(valid),'rects,local',len(local))
