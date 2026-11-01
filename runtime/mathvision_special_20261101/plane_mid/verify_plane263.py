"""Independent exact cover check for the frozen L pentomino, no model call."""
import json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
context=json.loads((HERE/'Plane263_context.json').read_text(encoding='utf-8'))
shape={(min(p[0] for p in o['geometry']['points']), min(p[1] for p in o['geometry']['points'])) for o in context['objects']}
def norm(points):
    a=min(x for x,y in points);b=min(y for x,y in points)
    return frozenset((x-a,y-b) for x,y in points)
rotations=set()
for flip in (1,-1):
    points={(flip*x,y) for x,y in shape}
    for r in range(4):
        rotations.add(norm(points))
        points={(-y,x) for x,y in points}
def tile(side):
    board={(x,y) for x in range(side) for y in range(side)}
    candidates=[]
    for o in rotations:
        width=max(x for x,y in o)+1;height=max(y for x,y in o)+1
        for dx in range(side-width+1):
            for dy in range(side-height+1):
                candidates.append(frozenset((x+dx,y+dy) for x,y in o))
    by_cell={p:[s for s in candidates if p in s] for p in board}
    calls=0
    def search(remaining):
        nonlocal calls
        calls+=1
        if not remaining:return []
        valid=None
        for p in sorted(remaining):
            moves=[s for s in by_cell[p] if s<=remaining]
            if not moves:return None
            if valid is None or len(moves)<len(valid): valid=moves
        for s in valid:
            result=search(remaining-s)
            if result is not None:return [s]+result
        return None
    result=search(board)
    return result,calls
five,nodes=tile(5)
assert five is None
# Two copies tile a 5-by-2 rectangle; ten such disjoint rectangles tile 10-by-10.
tile_a={(0,0),(1,0),(2,0),(3,0),(0,1)}
tile_b={(4,1),(3,1),(2,1),(1,1),(4,0)}
assert norm(tile_a) in rotations and norm(tile_b) in rotations
assert tile_a.isdisjoint(tile_b)
assert tile_a|tile_b=={(x,y) for x in range(5) for y in range(2)}
copies=[{(x+dx,y+dy) for x,y in t} for dx in (0,5) for dy in (0,2,4,6,8) for t in (tile_a,tile_b)]
assert len(copies)==20 and sum(len(c) for c in copies)==len(set().union(*copies))==100
assert set().union(*copies)=={(x,y) for x in range(10) for y in range(10)}
report={'question_id':'Plane263','area_of_piece':5,'orientation_count_including_reflections':len(rotations),
        'square_5x5_tileable':False,'complete_exact_cover_search_nodes':nodes,
        'square_10x10_explicit_tiling_pieces':20,'formal_answer_verified':20,
        'argument':'Area must be 5n and a perfect square. The first possibility is n=5 for 5x5; exhaustive exact cover rejects it even allowing flips. The next possibility is n=20 for 10x10, constructed explicitly.',
        'tiling_10x10':[[list(p) for p in sorted(c)] for c in copies]}
(HERE/'Plane263/v01/geometry_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='tiling_10x10'},ensure_ascii=False))
