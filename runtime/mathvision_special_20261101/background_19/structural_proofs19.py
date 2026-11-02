from tools19 import *
from itertools import combinations
from collections import deque
rects=((0,2,1,3),(1,4,3,1),(1,3,3,1),(4,2,1,3),(1,0,1,3),(2,1,3,1),(2,0,3,1))
def cells(r):
    x,y,w,h=r
    return {(a,b) for a in range(x,x+w) for b in range(y,y+h)}
board={(x,y) for x in range(5) for y in range(5)}
def vacancy(state):
    free=board-set().union(*(cells(r) for r in state))
    return next(([(x+i*dx,y+i*dy) for i in range(3)] for x,y in sorted(free) for dx,dy in ((1,0),(0,1)) if all((x+i*dx,y+i*dy) in free for i in range(3))),None)
def solve(subset):
    queue=deque([rects]);seen={rects};paths={rects:[]}
    while queue:
        st=queue.popleft();gap=vacancy(st)
        if gap:return {'found':True,'states':len(seen),'moves':paths[st],'final':st,'empty_bar_cells':gap}
        for i in subset:
            x,y,w,h=st[i];others=set().union(*(cells(r) for j,r in enumerate(st) if j!=i))
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                r=(x+dx,y+dy,w,h)
                if cells(r)<=board and not cells(r)&others:
                    nxt=st[:i]+(r,)+st[i+1:]
                    if nxt not in seen:
                        seen.add(nxt);queue.append(nxt);paths[nxt]=paths[st]+[{'bar':i+1,'from':[x,y],'to':[x+dx,y+dy]}]
    return {'found':False,'states':len(seen)}
attempts=[];witness=None
for k in range(4):
    for subset in combinations(range(7),k):
        r=solve(subset);attempts.append({'movable_bars':[i+1 for i in subset],**r})
        if r['found']:witness={'minimum_distinct_bars':k,'subset':[i+1 for i in subset],**r};break
    if witness:break
assert witness['minimum_distinct_bars']==3
write(HERE/'sliding_bar_proof.json',{'method':'Exhaustive BFS of integer translations with fixed orientation; minimizes number of distinct bars allowed to move. Includes every zero/one/two-bar subset; permits both horizontal and vertical slides when clear. Original 1x3 bar geometry is fixed.','native_rectangles':rects,'attempts':attempts,'witness':witness,'applies_to':['Plane330','Plane386'],'limitation':'Grid translation model; intended unit-bar sliding puzzle. Continuous translations cannot create a new grid-sized corridor without passing these contact alignments.'})
ships={(0,3),(1,0),(1,1)}
forbidden={(x,y) for x,y in board if any(abs(x-a)<=1 and abs(y-b)<=1 for a,b in ships)}
placements=[sorted({(x+i*dx,y+i*dy) for i in range(3)}) for x,y in board for dx,dy in ((1,0),(0,1)) if {(x+i*dx,y+i*dy) for i in range(3)}<=board-forbidden]
assert len(placements)==8
write(HERE/'Plane389'/'primary_enumeration.json',{'coordinates':'zero-based x from left, y from bottom','occupied_cells':sorted(ships),'forbidden_cells_including_boundary_contact':sorted(forbidden),'legal_3x1_placements':sorted(placements),'answer':8})
print(json.dumps({'sliding_minimum':3,'ship_placements':8}),flush=True)
