import itertools
def norm(s):
    x0=min(x for x,y in s);y0=min(y for x,y in s)
    return frozenset((x-x0,y-y0) for x,y in s)
def cells(context,prefix):
    edges=set()
    for o in context['objects']:
        if not o['id'].startswith(prefix):continue
        ps=o['geometry']['points'];assert len(ps)==2 and all(float(v).is_integer() for p in ps for v in p)
        edges.add(frozenset((int(x),int(y)) for x,y in ps))
    xy=[p for edge in edges for p in edge];out=set()
    for x in range(min(p[0] for p in xy),max(p[0] for p in xy)):
        for y in range(min(p[1] for p in xy),max(p[1] for p in xy)):
            v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
            if all(frozenset((v[i],v[(i+1)%4])) in edges for i in range(4)):out.add((x,y))
    return out
def forms(s,flips=(-1,1)):
    out=set()
    for flip in flips:
        t={(flip*x,y) for x,y in s}
        for _ in range(4):out.add(norm(t));t={(-y,x) for x,y in t}
    return out
def search(placements,remaining):
    if not remaining:return 1
    c=min(remaining)
    return sum(search(placements,remaining-p) for p in placements if c in p and p<=remaining)
def prove(context):
    board=norm(cells(context,'given_'));assert len(board)==15
    proof={}
    for letter in 'ABCDE':
        shape=norm(cells(context,letter+'_'));assert len(shape)==5
        ps=set()
        for f in forms(shape):
            for x,y in itertools.product(range(4),repeat=2):
                p=frozenset((x+a,y+b) for a,b in f)
                if p<=board:ps.add(p)
        ps=sorted(ps,key=lambda s:sorted(s))
        tilings=[t for t in itertools.combinations(ps,3) if len(set().union(*t))==15]
        assert search(ps,board)==len(tilings)
        proof[letter]={'cells':sorted(shape),'D4_forms':len(forms(shape)),'all_valid_placements':[sorted(p) for p in ps],'placement_count':len(ps),'unordered_triples_checked':len(list(itertools.combinations(ps,3))),'tiling_count':len(tilings),'witnesses':[[sorted(p) for p in t] for t in tilings]}
    assert [proof[k]['tiling_count'] for k in 'ABCDE']==[2,0,0,0,0]
    return board,proof
def is_exterior(edge,cs):
    edge=frozenset(map(tuple,edge));n=0
    for x,y in cs:
        v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
        n+=any(frozenset((v[i],v[(i+1)%4]))==edge for i in range(4))
    return n==1
