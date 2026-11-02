from env42 import *
from itertools import combinations
from fractions import Fraction as F
def scene(q):return read(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/q/'scene.json')
def segments(sc):
    out=[]
    for ob in sc['objects']:
        if ob['type'] not in ('polygon','segment'):continue
        ps=[tuple(F(str(c)) for c in sc['points'][p]) for p in ob['points']]
        out+=list(zip(ps,ps[1:]+ps[:1])) if ob['type']=='polygon' else [(ps[0],ps[1])]
    return out
def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def covered(a,b,segs):
    k=0 if b[0]!=a[0] else 1;lo,hi=sorted([a[k],b[k]]);intervals=[]
    for c,d in segs:
        if cross(a,b,c)==0 and cross(a,b,d)==0:
            x,y=sorted([c[k],d[k]]);intervals.append((x,y))
    reach=lo
    for x,y in sorted(intervals):
        if x>reach:return False
        if y>=lo:reach=max(reach,y)
        if reach>=hi:return True
    return False
def rectangles(sc):
    seg=segments(sc);xs=sorted({p[0] for s in seg for p in s});ys=sorted({p[1] for s in seg for p in s});out=[]
    for x1,x2 in combinations(xs,2):
        for y1,y2 in combinations(ys,2):
            ps=[(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
            if all(covered(a,b,seg) for a,b in zip(ps,ps[1:]+ps[:1])):out.append([float(x1),float(y1),float(x2),float(y2)])
    return out
def packing(w,h,k):
    base=[(0,0),(1,0),(2,0),(1,1)];rots=[]
    for _ in range(4):
        mx=min(x for x,y in base);my=min(y for x,y in base);rots.append([(x-mx,y-my) for x,y in base]);base=[(-y,x) for x,y in base]
    placements=[]
    for rot in rots:
        for dx in range(w-max(x for x,y in rot)):
            for dy in range(h-max(y for x,y in rot)):
                cells=[(x+dx,y+dy) for x,y in rot];mask=sum(1<<(y*w+x) for x,y in cells);placements.append((mask,cells))
    bycell=[[p for p in placements if p[0]&(1<<i)] for i in range(w*h)];full=(1<<(w*h))-1
    def dfs(used,left):
        if left==0:return []
        free=full^used
        if free.bit_count()<4*left:return None
        cell=(free&-free).bit_length()-1
        for mask,cells in bycell[cell]:
            if not mask&used:
                result=dfs(used|mask,left-1)
                if result is not None:return [cells]+result
        if free.bit_count()>4*left:return dfs(used|(1<<cell),left)
        return None
    result=dfs(0,k);assert result and len(result)==k
    assert len(set(p for r in result for p in r))==4*k
    return result
if __name__=='__main__':
    for q in ASSIGNED:
        sc=scene(q);audit={'question_id':q,'source_scene_read_in_full':True,'created_at':now()}
        if q=='Plane413':
            ps=[sc['points'][p] for p in sc['objects'][0]['points']];area=abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(ps,ps[1:]+ps[:1])))/2
            audit.update(vertices=ps,shoelace_area=area,proof='Frozen gray boundary follows these seven lattice vertices; shoelace gives17 square units, also27 total minus white triangles3+1+3+3. Unit grid and gray area are the targets, not boundary-mark counts.');assert area==17
        elif q in ('Plane418','Plane485'):
            w,h,k=(5,4,4) if q=='Plane418' else (6,6,8)
            audit.update(grid=[w,h],maximum=k,packing_witness=packing(w,h,k),proof='Each T contains4 unit squares and covers3 cells of one checkerboard parity and1 of the other. A full board tiling would use an odd number of Ts (5 or9); the total parity imbalance is twice a sum of an odd number of +1/-1 terms, hence nonzero. Both boards have equal black/white counts. So area upper bound5/9 is unattainable; explicit disjoint packing of4/8 proves maximum. Coordinates are proof-only, never added to displayed board.')
        elif q=='Plane420':
            ts=[]
            for i,j in combinations(range(5),2):ts.append([[i,4-i],[j,4-j],[i,4-j]])
            sq=[[x,y,s] for s in range(1,5) for x in range(4) for y in range(4) if x+y+2*s<=4]
            assert len(ts)==10 and len(sq)==7
            audit.update(triangles=ts,squares=sq,answer=3,proof='The only oblique line is x+y=4. Every triangle chooses two distinct of its5 lattice intersections and the uniquely forced horizontal/vertical right-angle corner, giving C(5,2)=10. Axis-aligned squares satisfy x+y+2s<=4:6 unit squares and1 of side2. Difference10-7=3. Top and right corner side2 triangles each contain3 triangles; restricting to either group misses4 cross-group triangles and wrongly gives |6-7|=1.')
        elif q=='Plane451':
            s={(1,3),(2,1),(4,0)};closure={(x2,y2) for x,y in s for x2 in (x,4-x) for y2 in (y,3-y)}
            audit.update(shaded_cells=sorted(s),symmetry_closure=sorted(closure),additional=len(closure)-3,proof='The full5x4 rectangular grid has only its horizontal and vertical reflection axes; diagonal reflection cannot preserve its outer boundary. The3 shaded cells generate disjoint orbits of4,2,4 cells. Their10-cell closure is necessary and sufficient, so7 additional. Appearance marks must not be interpreted as additional shaded units.')
        elif q=='Plane459':
            audit.update(answer=5,triangles=['ABD','BDE','DEC','BDC','ABC'],not_triangles=['ABED (quadrilateral; AB and BE are not collinear)','ADE (AE absent)','AEC (AE absent)'],proof='D lies on AC and E on BC. Splitting BDC by DE creates BDE/DEC; with ABD, BDC, ABC there are5. Among5 point triples A,D,C and B,E,C are collinear; the other unlisted triples require absent AE. Partial edge pairing cannot turn ABED into a triangle. DE is near parallel to AB in the displayed layout but not an exact parallel given.')
        elif q=='Plane470':
            points=list(sc['points'].items());deg=[];tri=[];onecolumn=[]
            for t in combinations(points,3):
                if cross(*[p[1] for p in t])==0:deg.append([p[0] for p in t])
                else:
                    tri.append([p[0] for p in t])
                    if len({p[1][0] for p in t})==3:onecolumn.append([p[0] for p in t])
            assert len(tri)==18 and len(onecolumn)==6
            audit.update(collinear_triples=deg,all_triangles=tri,one_per_column_triangles=onecolumn,answer=18,proof='Six distinct dots giveC(6,3)=20 triples. Exactly the two horizontal rows are collinear, leaving18. Choosing one dot from each true vertical pair yields8 triples minus the2 rows=6, omitting12 valid triangles that use both vertices of one column. Three parallel open column segments contain no new vertex or triangle and impose no restriction on the requested choice of dots.')
        elif q=='Plane478':
            rs=rectangles(sc);assert len(rs)==11
            groups={}
            for name,bounds in [('top',[1,2,3,4]),('horizontal',[0,1.5,2.3,2.5]),('vertical',[2,0,2.8,3.3])]:
                x1,y1,x2,y2=bounds;groups[name]=[r for r in rs if x1<=r[0]<r[2]<=x2 and y1<=r[1]<r[3]<=y2]
            audit.update(rectangles=rs,inside_source_families=groups,answer=11,proof='All segments are horizontal/vertical. Enumerate all pairs of native x-levels and y-levels; require all4 sides covered by original collinear segment unions. This gives exactly11 boxes. Every rectangle uses these existing levels, so the list is exhaustive. Colors cannot change the universe or remove crossing edges.')
            print(q,json.dumps(audit,ensure_ascii=False))
        write(HERE/q/'primary_math_audit.json',audit)
