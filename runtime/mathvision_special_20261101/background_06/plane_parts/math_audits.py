from tools_local import *
import itertools
def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
def grid_cells(meta,prefix):
    edges={edge(*o['geometry']['points']) for o in meta['objects'] if o['id'].startswith(prefix) and o['kind']=='segment'}
    xs=[p[0] for e in edges for p in e];ys=[p[1] for e in edges for p in e]
    cells=set()
    for x in range(int(min(xs)),int(max(xs))):
        for y in range(int(min(ys)),int(max(ys))):
            es=[edge((x,y),(x+1,y)),edge((x+1,y),(x+1,y+1)),edge((x+1,y+1),(x,y+1)),edge((x,y+1),(x,y))]
            if all(e in edges for e in es):cells.add((x,y))
    return cells
def normalize(s):
    a=min(x for x,y in s);b=min(y for x,y in s);return frozenset((x-a,y-b) for x,y in s)
def orientations(s):
    out=set()
    for flip in [-1,1]:
        for rot in range(4):
            t={(flip*x,y) for x,y in s}
            for _ in range(rot):t={(-y,x) for x,y in t}
            out.add(normalize(t))
    return out
def placements(board,s):
    out=set()
    for shape in orientations(s):
        for x in range(-5,6):
            for y in range(-5,6):
                t=frozenset((a+x,b+y) for a,b in shape)
                if t<=board:out.add(t)
    return sorted(out,key=lambda s:sorted(s))
def run(qid):
    meta=json.loads((HERE/qid/'context.json').read_text());board=normalize(grid_cells(meta,'given_'));out={}
    for letter in 'ABCDE':
        shape=normalize(grid_cells(meta,letter+'_'));p=placements(board,shape);solutions=[]
        count=3 if qid=='Plane233' else 2
        for group in itertools.combinations(p,count):
            if sum(map(len,group))==len(set().union(*group)) and (qid!='Plane233' or set().union(*group)==board):solutions.append([sorted(s) for s in group])
        out[letter]={'cells':sorted(shape),'orientation_count':len(orientations(shape)),'placement_count':len(p),'solution_count':len(solutions),'witnesses':solutions[:3]}
    write(HERE/qid/'mathematical_enumeration.json',{'question_id':qid,'created_at':now(),'board_cells':sorted(board),'method':'Exhaustive finite grid placements under all 8 square-grid isometries; choose pairwise-disjoint copies, additionally cover board for Plane233. Every candidate cell is recovered from its four original frozen unit edges.','results':out,'correct_answer':'A','formal_unique_answer_confirmed':(out['A']['solution_count']>0 and all(out[k]['solution_count']==0 for k in 'BCDE')) if qid=='Plane233' else (out['A']['solution_count']==0 and all(out[k]['solution_count']>0 for k in 'BCDE'))})
    print(qid,json.dumps({k:v['solution_count'] for k,v in out.items()}))
if __name__=='__main__':
    for q in sys.argv[1:]:run(q)
