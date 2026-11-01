from tools09 import *
from fractions import Fraction as F
def wire301():
    meta=read(HERE/'Plane301/context.json');results={}
    def sub(a,b):return a[0]-b[0],a[1]-b[1]
    def cross(a,b):return a[0]*b[1]-a[1]*b[0]
    def dot(a,b):return a[0]*b[0]+a[1]*b[1]
    for k,let in enumerate('ABCDE'):
        segs=[tuple(tuple(F(v) for v in p) for p in o['geometry']['points']) for o in meta['objects'] if o['id'].startswith('wire'+str(k)+'_')]
        a,b=segs[0][0],segs[-1][1];v=sub(b,a);vv=dot(v,v)
        def reflect(p):
            u=sub(p,a);t=2*dot(u,v)/vv
            return a[0]+t*v[0]-u[0],a[1]+t*v[1]-u[1]
        transforms=[('identity',lambda p:p),('half_turn',lambda p:(a[0]+b[0]-p[0],a[1]+b[1]-p[1])),('chord_reflection',reflect),('bisector_reflection',lambda p:(a[0]+b[0]-reflect(p)[0],a[1]+b[1]-reflect(p)[1]))]
        tests=[]
        for name,f in transforms:
            second=[(f(p),f(q)) for p,q in segs];bad=[]
            for i,(p,q) in enumerate(segs):
                for j,(r,s) in enumerate(second):
                    u=sub(q,p);w=sub(s,r);den=cross(u,w);rp=sub(r,p)
                    if den:
                        t=cross(rp,w)/den;z=cross(rp,u)/den
                        if 0<=t<=1 and 0<=z<=1:
                            pt=(p[0]+t*u[0],p[1]+t*u[1])
                            if pt not in [a,b]:bad.append({'segments':[i,j],'kind':'intersection','point':[str(x) for x in pt]})
                    elif cross(rp,u)==0:
                        axis=0 if u[0] else 1
                        lo=max(min(p[axis],q[axis]),min(r[axis],s[axis]));hi=min(max(p[axis],q[axis]),max(r[axis],s[axis]))
                        if hi>lo:bad.append({'segments':[i,j],'kind':'positive_length_overlap'})
                        elif hi==lo:
                            pt=next((pt for pt in [p,q,r,s] if pt[axis]==lo),None)
                            if pt not in [a,b]:bad.append({'segments':[i,j],'kind':'interior_touch'})
            tests.append({'transform':name,'allowed_closed_simple_join':not bad,'invalid_contacts':bad})
        results[let]=tests
    possible=[let for let,t in results.items() if any(x['allowed_closed_simple_join'] for x in t)]
    assert possible==['B'],possible
    write(HERE/'Plane301/primary_math_audit.json',{'unique_answer':'B','method':'Exact rational segment intersections for every Euclidean isometry mapping the two ordered endpoints onto the same endpoint set: identity, halfturn, reflection in chord, reflection in perpendicular bisector. All copies must use one of these because their two endpoints must join both given endpoints. Only shared global endpoints are allowed; any interior intersection/touch or positive-length overlap fails. Includes turn-over/reflection as a permissive superset.','results':results})
def tile398():
    s=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane398.json');groups={}
    for o in s['objects']:
        oid=o['id'];p=[s['points'][x] for x in o['points']];x=min(v[0] for v in p);y=min(v[1] for v in p)
        group='piece1' if oid.startswith('cellpiece1') else 'piece2' if oid.startswith('cellpiece2') else oid[4]
        groups.setdefault(group,{})[(F(str(x)),F(str(y)))]=bool(o.get('semantic_fill',False))
    def norm(d):
        a=min(x for x,y in d);b=min(y for x,y in d);return {(x-a,y-b):v for (x,y),v in d.items()}
    def orient(d):
        out=[]
        for ref in [-1,1]:
            for rot in range(4):
                z={(ref*x,y):v for (x,y),v in d.items()}
                for _ in range(rot):z={(-y,x):v for (x,y),v in z.items()}
                z=norm(z)
                if z not in out:out.append(z)
        return out
    results={}
    for let in 'ABCDE':
        board=norm(groups[let]);ps=[]
        for piece in ['piece1','piece2']:
            poss=[]
            for ori in orient(norm(groups[piece])):
                for dx in range(4):
                    for dy in range(4):
                        t={(x+dx,y+dy):v for (x,y),v in ori.items()}
                        if all(p in board and board[p]==v for p,v in t.items()):poss.append(t)
            ps.append(poss)
        sols=[]
        for a in ps[0]:
            for b in ps[1]:
                if not(set(a)&set(b)) and set(a)|set(b)==set(board):sols.append({'piece1':[[str(x),str(y),v] for (x,y),v in sorted(a.items())],'piece2':[[str(x),str(y),v] for (x,y),v in sorted(b.items())]})
        results[let]={'solution_count':len(sols),'witnesses':sols[:3]}
    assert all(results[x]['solution_count']>0 for x in 'ABCD') and results['E']['solution_count']==0,results
    write(HERE/'Plane398/primary_math_audit.json',{'unique_answer':'E','method':'Recover exact unit-cell positions and semantic black/white fill from frozen scene. Enumerate all8 square-grid isometries and every board translation for each piece; require both spatial and fill match, disjoint interiors and coverage of all16 cells.','results':results})
if __name__=='__main__':
    for name in sys.argv[1:]:globals()[name]()
