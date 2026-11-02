from tools72 import *
from fractions import Fraction as F
from itertools import combinations, product
from collections import deque

def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def intersects_interior(a,b,tri):
    # Exact clipping of the open halfplanes; a nonempty open interval is an interior hit.
    if cross(*tri)<0:tri=list(reversed(tri))
    lo,hi=F(0),F(1)
    for c,d in zip(tri,tri[1:]+tri[:1]):
        u=cross(c,d,a);v=cross(c,d,b);s=v-u
        if s==0:
            if u<=0:return False
        elif s>0:lo=max(lo,-u/s)
        else:hi=min(hi,-u/s)
    return lo<hi

def proof335():
    s=read(PROJECT/BRANCH/'dataset_generator/scenes/Plane335.json')
    p={k:tuple(F(str(v)) for v in xy) for k,xy in s['points'].items()}
    tris=[[p[x] for x in ['0L','0U','0D']],[p[x] for x in ['1L','1U','1D']]]
    pairs=[]
    for a,b in product(['0L','0U','0D'],['1L','1U','1D']):
        hits=[intersects_interior(p[a],p[b],t) for t in tris]
        pairs.append({'left':a,'right':b,'interior_hits':hits,'legal':not any(hits)})
    assert sum(r['legal'] for r in pairs)==4
    write(HERE/'Plane335/unique_math.json',{'method':'Exact rational clipping of all nine segments against each open triangle interior; touching a vertex or lying along a boundary alone does not dissect.','pairs':pairs,'unique_answer':'4','not_from_stored_answer':True})
    print('335',pairs,flush=True)

RECTS=[(0,2,1,3),(1,4,3,1),(1,3,3,1),(4,2,1,3),(1,0,1,3),(2,1,3,1),(2,0,3,1)]
def cells(r):
    x,y,w,h=r;return frozenset((i,j) for i in range(x,x+w) for j in range(y,y+h))
def placements(w,h):return [(x,y,w,h) for x in range(6-w) for y in range(6-h)]
NEW=placements(1,3)+placements(3,1)
def static(sub):
    fixed=set().union(*(cells(r) for i,r in enumerate(RECTS) if i not in sub))
    def rec(k,occupied,placed):
        if k==len(sub):
            for new in NEW:
                if not occupied.intersection(cells(new)):return {'placed':placed,'new':new}
            return None
        i=sub[k];_,_,w,h=RECTS[i]
        for r in placements(w,h):
            c=cells(r)
            if not occupied.intersection(c):
                v=rec(k+1,occupied|c,placed+[{'bar':i,'rect':r}])
                if v:return v
    return rec(0,fixed,[])
def bfs(sub):
    initial=tuple((r[0],r[1]) for r in RECTS)
    queue=deque([initial]);prev={initial:None};move={}
    while queue:
        st=queue.popleft()
        rects=[(x,y,RECTS[i][2],RECTS[i][3]) for i,(x,y) in enumerate(st)]
        occupied=set().union(*(cells(r) for r in rects))
        room=next((r for r in NEW if not occupied.intersection(cells(r))),None)
        if room:
            seq=[];p=st
            while prev[p] is not None:seq.append(move[p]);p=prev[p]
            return {'found':True,'states':len(prev),'moves':seq[::-1],'new_bar':room,'final':rects}
        for i in sub:
            fixed=set().union(*(cells(r) for j,r in enumerate(rects) if j!=i))
            x,y,w,h=rects[i]
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                r=(x+dx,y+dy,w,h)
                if r[0]<0 or r[1]<0 or r[0]+w>5 or r[1]+h>5 or fixed.intersection(cells(r)):continue
                nxt=list(st);nxt[i]=(x+dx,y+dy);nxt=tuple(nxt)
                if nxt not in prev:
                    prev[nxt]=st;move[nxt]={'bar':i,'from':[x,y],'to':[x+dx,y+dy]};queue.append(nxt)
    return {'found':False,'states':len(prev)}

def proof386():
    static_results=[];bfs_results=[]
    for n in range(3):
        for sub in combinations(range(7),n):
            static_results.append({'movable':sub,'witness':static(sub)})
            bfs_results.append({'movable':sub,**bfs(sub)})
    witness=bfs((0,1,2));assert witness['found']
    write(HERE/'Plane386/independent_search.json',{'rectangles_bar_ids_zero_based':RECTS,'static_final_packings_upto_two_moved':static_results,'integer_slide_components_upto_two_moved':bfs_results,'three_bar_witness':witness,'static_relaxation_infeasible':not any(r['witness'] for r in static_results),'integer_bfs_all_upto_two_fail':not any(r['found'] for r in bfs_results)})
    print('386 static possibilities',[(r['movable'],r['witness']) for r in static_results if r['witness']],flush=True)
    print('386 witness',witness,flush=True)

if __name__=='__main__':
    proof335();proof386()
