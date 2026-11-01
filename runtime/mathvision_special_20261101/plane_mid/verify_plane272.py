import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
scene=json.loads((ROOT/'PlaneGeometry/dataset_generator/scenes/Plane272.json').read_text(encoding='utf-8'))
shape={(min(p[0] for p in o['points']),min(p[1] for p in o['points'])) for o in scene['objects'] if o['id'].startswith('tile')}
def norm(points):
    a=min(x for x,y in points);b=min(y for x,y in points)
    return frozenset((x-a,y-b) for x,y in points)
orientations=set()
for r in range(4):
    orientations.add(norm(shape));shape={(-y,x) for x,y in shape}
assert all(abs(sum((-1)**int(x+y) for x,y in o))==2 for o in orientations)
board={(x,y) for x in range(4) for y in range(4)}
placements=[]
for o in orientations:
    width=max(x for x,y in o)+1;height=max(y for x,y in o)+1
    for dx in range(4-width+1):
        for dy in range(4-height+1): placements.append(frozenset((x+dx,y+dy) for x,y in o))
def search(remaining):
    if not remaining:return []
    p=min(remaining)
    for s in placements:
        if p in s and s<=remaining:
            result=search(remaining-s)
            if result is not None:return [s]+result
    return None
solution=search(board)
assert solution and len(solution)==4
report={'question_id':'Plane272','formal_answer':4,'area_upper_bound':5,
        'five_tile_impossibility':'The 5x4 board has 10 black and 10 white cells. Every T tetromino covers 3 of one checkerboard color and 1 of the other. Five tiles would give an odd sum of five values +2/-2; this cannot be zero. Thus five cannot tile the board.',
        'four_tile_construction':'Four Ts tile the left 4x4 sub-board; the rightmost column remains empty.',
        'four_tile_solution':[[list(p) for p in sorted(s)] for s in solution],
        'appearance_preserved':'Only the four original tile polygon outlines were colored; their gray fills and all board cells are unchanged.'}
(HERE/'Plane272/v01/geometry_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print('Verified 4 via checkerboard obstruction for 5 and explicit 4x4 tiling.')
