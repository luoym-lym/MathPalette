from tools09 import *
def wire252():
    meta=read(HERE/'Plane252/context.json');w=[]
    for k in [0,1]:
        w.append([tuple(map(tuple,o['geometry']['points'])) for o in meta['objects'] if o['id'].startswith('wire'+str(k)+'_')])
    def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
    a={edge(*e) for e in w[0]};best=0;wit=[]
    for refl in [1,-1]:
        for rot in range(4):
            def f(p):
                x,y=p;x*=refl
                for _ in range(rot):x,y=-y,x
                return x,y
            b=[(f(x),f(y)) for x,y in w[1]]
            for dx in range(-12,13):
                for dy in range(-12,13):
                    z={edge((x[0]+dx,x[1]+dy),(y[0]+dx,y[1]+dy)) for x,y in b};over=a&z;n=len(over)
                    if n>best:best=n;wit=[]
                    if n==best:wit.append({'reflection':refl,'rotation_quarter_turns':rot,'translation':[dx,dy],'common_edges':sorted(over)})
    assert best==5
    out={'question_id':'Plane252','method':'Enumerate all 8 square-lattice isometries and integer translations -12..12, matching exact unit edges. A positive overlap requires parallel unit edges, hence relative angle a multiple of 90 degrees. For each such orientation, overlap as a function of translation is piecewise linear with integer endpoint breakpoints, so an integer optimum exists. Reflections are included, a superset if turning over is disallowed.','maximum':best,'witnesses':wit,'wire_edges':w}
    write(HERE/'Plane252/primary_math_audit.json',out)
def areas391():
    s=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane391.json');vals={}
    for o in s['objects']:
        if o['type']!='polygon':continue
        p=[s['points'][v] for v in o['points']];area=abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p))))/2;vals[o['id']]=area
    assert sum(vals['piece'+str(i)] for i in range(4))==4
    assert sum(vals['piece'+str(i)] for i in range(4,11))==6
    write(HERE/'Plane391/primary_math_audit.json',{'method':'Shoelace of the unchanged frozen source and assembly polygons. Unit scale fixed by first square area4. Interiors of assembly pieces are disjoint; shared boundaries have zero area.','individual_areas':vals,'source_total':4,'assembly_total':6,'unique_answer':'6'})
def folds348():
    cuts=[0,0.25,0.75,1];widths=[cuts[i+1]-cuts[i] for i in range(3)]
    cells=[{'rectangle':[cuts[x],cuts[y],cuts[x+1],cuts[y+1]],'square':widths[x]==widths[y]} for x in range(3) for y in range(3)]
    assert sum(x['square'] for x in cells)==5
    write(HERE/'Plane348/primary_math_audit.json',{'method':'Normalize original side to1. The first and second folds halve orthogonal dimensions. Cutting at the midpoint of each final folded dimension propagates to 1/4 and3/4 on unfolding. Cuts form3x3 regions with side intervals1/4,1/2,1/4; four corner squares and one central square, four nonsquare rectangles. Dotted folds are not themselves cuts.','cut_positions':cuts,'cells':cells,'unique_answer':'5'})
def tiling213():
    import itertools
    meta=read(HERE/'Plane213/context.json')
    def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
    def cells(prefix):
        es={edge(*o['geometry']['points']) for o in meta['objects'] if o['id'].startswith(prefix) and o['kind']=='segment'}
        pts=[p for e in es for p in e];out=set()
        for x in range(int(min(p[0] for p in pts)),int(max(p[0] for p in pts))):
            for y in range(int(min(p[1] for p in pts)),int(max(p[1] for p in pts))):
                if all(e in es for e in [edge((x,y),(x+1,y)),edge((x+1,y),(x+1,y+1)),edge((x+1,y+1),(x,y+1)),edge((x,y+1),(x,y))]):out.add((x,y))
        return out
    def norm(s):
        x=min(p[0] for p in s);y=min(p[1] for p in s);return frozenset((a-x,b-y) for a,b in s)
    def ori(s):
        out=set()
        for ref in [-1,1]:
            for rot in range(4):
                t={(ref*x,y) for x,y in s}
                for _ in range(rot):t={(-y,x) for x,y in t}
                out.add(norm(t))
        return out
    board=norm(cells('given_'));res={}
    for let in 'ABCDE':
        s=norm(cells(let+'_'));ps=set()
        for z in ori(s):
            for dx in range(4):
                for dy in range(4):
                    p=frozenset((x+dx,y+dy) for x,y in z)
                    if p<=board:ps.add(p)
        sols=[]
        for a,b,c in itertools.combinations(ps,3):
            if not(a&b or a&c or b&c) and a|b|c==board:sols.append([sorted(a),sorted(b),sorted(c)])
        res[let]={'cells':sorted(s),'placements':len(ps),'solution_count':len(sols),'witnesses':sols[:3]}
    assert res['A']['solution_count']>0 and all(res[x]['solution_count']==0 for x in 'BCDE')
    write(HERE/'Plane213/primary_math_audit.json',{'question_id':'Plane213','board_cells':sorted(board),'method':'Exact enumeration of all grid-cell placements under all8 square-lattice isometries, then all disjoint triples. Each cell recovered from4 original unit edges. A finite partition of this polyomino into3 congruent lattice pentominoes is exactly such a triple.','results':res,'unique_answer':'A'})
if __name__=='__main__':
    if sys.argv[1:]==['213']:tiling213()
    elif not sys.argv[1:]:wire252();areas391();folds348()
