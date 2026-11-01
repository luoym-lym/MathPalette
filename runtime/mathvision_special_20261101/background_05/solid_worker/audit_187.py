from tools_local import *
from collections import deque
qid='Solid187'
source_path=next(ROOT/'SolidGeometry'/p for p in AD.records[qid]['runtime_dependencies'] if p.endswith('/scene.json'))
source=json.loads(source_path.read_text(encoding='utf-8-sig'))
def neg(v):return tuple(-x for x in v)
def key(v):return tuple(round(float(x),8) for x in v)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(v,s):return tuple(x*s for x in v)
def fold(cells):
    basis={(1,0):((1,0,0),(0,1,0),(0,0,1))};todo=deque([(1,0)])
    while todo:
        c=todo.popleft();u,v,n=basis[c]
        for (dx,dy),trip in [((1,0),(neg(n),v,u)),((-1,0),(n,v,neg(u))),((0,1),(u,neg(n),v)),((0,-1),(u,n,neg(v)))]:
            d=(c[0]+dx,c[1]+dy)
            if d in cells and d not in basis:basis[d]=trip;todo.append(d)
    return basis
cells={(0,0),(1,0),(2,0),(3,0),(1,1),(1,-1)};basis=fold(cells);results={}
for i,letter in enumerate('ABCDE'):
    offset=7*i
    fills=[o for o in source['objects'] if o['type']=='face' and o['id'].startswith(letter+'material')]
    rects=[(min(p[0] for p in o['points'])-offset,max(p[0] for p in o['points'])-offset,min(p[2] for p in o['points']),max(p[2] for p in o['points'])) for o in fills]
    features=[]
    for cell in sorted(cells):
        cx,cy=cell;xs=sorted({cx,cx+1,*[round(t,10) for r in rects for t in r[:2] if cx<t<cx+1]});ys=sorted({cy,cy+1,*[round(t,10) for r in rects for t in r[2:] if cy<t<cy+1]})
        void=set()
        for ix in range(len(xs)-1):
            for iy in range(len(ys)-1):
                x=(xs[ix]+xs[ix+1])/2;y=(ys[iy]+ys[iy+1])/2
                if not any(a-1e-8<x<b+1e-8 and c-1e-8<y<d+1e-8 for a,b,c,d in rects):void.add((ix,iy))
        while void:
            todo=[void.pop()];component=[]
            while todo:
                tile=todo.pop();component.append(tile)
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    other=(tile[0]+dx,tile[1]+dy)
                    if other in void:void.remove(other);todo.append(other)
            lo_x=min(xs[x] for x,y in component);hi_x=max(xs[x+1] for x,y in component);lo_y=min(ys[y] for x,y in component);hi_y=max(ys[y+1] for x,y in component)
            touches=[]
            if abs(lo_x-cx)<1e-8:touches.append(('left',(0,0),(0,1)))
            if abs(hi_x-cx-1)<1e-8:touches.append(('right',(1,0),(1,1)))
            if abs(lo_y-cy)<1e-8:touches.append(('bottom',(0,0),(1,0)))
            if abs(hi_y-cy-1)<1e-8:touches.append(('top',(0,1),(1,1)))
            u,v,n=basis[cell]
            def project(p):return key(add(mul(n,.5),add(mul(u,p[0]-.5),mul(v,p[1]-.5))))
            edge=sorted([project(p) for p in touches[0][1:]]) if len(touches)==1 else None
            features.append({'face_cell':list(cell),'void_bounds':[lo_x,hi_x,lo_y,hi_y],'touches':[t[0] for t in touches],'folded_cube_edge':edge})
    groups={}
    for f in features:
        e=str(f['folded_cube_edge']);groups.setdefault(e,[]).append(f)
    paired=[v for k,v in groups.items() if k!='None' and len(v)==2]
    valid=False;opposite=False
    if len(paired)==2 and len(features)==4:
        a=paired[0][0]['folded_cube_edge'];b=paired[1][0]['folded_cube_edge']
        midpoint_a=mul(add(a[0],a[1]),.5);midpoint_b=mul(add(b[0],b[1]),.5)
        opposite=key(midpoint_a)==key(neg(midpoint_b));valid=opposite
    results[letter]={'half_notches_or_face_holes':features,'group_sizes':{k:len(v) for k,v in groups.items()},'paired_edge_hole_count':len(paired),'two_opposite_edge_holes':opposite,'matches_target':valid}
assert [k for k,v in results.items() if v['matches_target']]==['C'],results
write(TASK/qid/'folded_notch_audit.json',{'question_id':qid,'correct_unique_answer':'C','method':'Read original material rectangles, find missing face components, fold six face frames exactly, and pair half-notches by full cube-edge identity. Target has two disjoint parallel centrally opposite cube edges. Feature sizes are schematic; no numerical dimensions are given.','nets':results})
for letter,d in results.items():print(letter,d['paired_edge_hole_count'],d['two_opposite_edge_holes'],d['group_sizes'])
