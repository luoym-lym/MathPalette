from unit_env import *
from itertools import combinations, permutations

def sub(a,b): return [a[0]-b[0],a[1]-b[1]]
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def square(a): return dot(a,a)

for qid in QIDS:
    row = eligibility(qid)
    assert row['eligible']
    scene = read(PROJECT/'PlaneGeometry'/row['record']['scene'])
    if qid == 'Plane211':
        order = [1]
        for i in range(9): order.append((order[-1]+1)%9+1)
        assert order == [1,3,5,7,9,2,4,6,8,1]
        expected = sorted([sorted([a,b]) for a,b in zip(order,order[1:])])
        panels = {}
        for panel,letter in enumerate('ABCDE',1):
            actual = [o for o in scene['objects'] if o['id'].startswith(f'edge{panel}_')]
            edges = sorted([sorted([int(p.split('_')[1]) for p in o['points']]) for o in actual])
            panels[letter] = {'objects':actual,'edges':edges,'matches_full_cycle':edges==expected,
                             'missing_edges':[e for e in expected if e not in edges],
                             'extra_edges':[e for e in edges if e not in expected]}
        assert [l for l,p in panels.items() if p['matches_full_cycle']] == ['E']
        proof = {'question_id':qid,'correct_answer':'E','formal_text':row['record']['question'],
                 'proof_method':'Exact graph edge sets from frozen formal objects, not shape appearance.',
                 'ordered_mod9_cycle':order,'expected_edges':expected,'panels':panels,
                 'uniqueness':'Adding 2 modulo 9 has order 9 since gcd(2,9)=1. All nine vertices must be visited before the return to 1. Only E has precisely all nine required undirected edges. No parity-only closure is valid.'}
    else:
        points = {k:scene['points'][k] for k in ('P0','P1','P2','P3','P4','P5')}
        triangles = []
        for ids in combinations(points,3):
            a,b,c = (points[k] for k in ids)
            area2 = cross(sub(b,a),sub(c,a))
            ds = sorted([square(sub(a,b)),square(sub(a,c)),square(sub(b,c))])
            kind = ('degenerate' if not area2 else 'acute' if ds[2]<ds[0]+ds[1]
                    else 'right' if ds[2]==ds[0]+ds[1] else 'obtuse')
            triangles.append({'vertices':ids,'area2':area2,'squared_lengths_sorted':ds,'type':kind})
        quads = []
        for subset in combinations(points,4):
            # Unique convex cyclic order: fix first vertex and reverse equivalence.
            for tail in permutations(subset[1:]):
                ids = (subset[0],)+tail
                if ids[1]>ids[-1]: continue
                p = [points[k] for k in ids]
                edges = [sub(p[(i+1)%4],p[i]) for i in range(4)]
                turns = [cross(edges[i],edges[(i+1)%4]) for i in range(4)]
                if not (all(t>0 for t in turns) or all(t<0 for t in turns)): continue
                parallel = [cross(edges[0],edges[2])==0,cross(edges[1],edges[3])==0]
                ds = [square(e) for e in edges]
                para = all(parallel)
                is_square = para and len(set(ds))==1 and dot(edges[0],edges[1])==0
                quads.append({'cyclic_vertices':ids,'edges':edges,'edge_squared_lengths':ds,
                              'opposite_pair_parallel':parallel,'square':is_square,
                              'parallelogram':para,'unequal_adjacent_sides_parallelogram':para and ds[0]!=ds[1],
                              'strict_trapezium':sum(parallel)==1})
        assert len(triangles)==20
        if qid=='Plane364':
            witnesses = {'A_square':next(q for q in quads if q['square']),
                         'B_unequal_side_parallelogram':next(q for q in quads if q['unequal_adjacent_sides_parallelogram']),
                         'C_acute_triangle':next(t for t in triangles if t['type']=='acute'),
                         'D_obtuse_triangle':next(t for t in triangles if t['type']=='obtuse')}
        else:
            witnesses = {'A_parallelogram':next(q for q in quads if q['parallelogram']),
                         'B_strict_trapezium':next(q for q in quads if q['strict_trapezium']),
                         'C_right_triangle':next(t for t in triangles if t['type']=='right'),
                         'D_obtuse_triangle':next(t for t in triangles if t['type']=='obtuse')}
        proof = {'question_id':qid,'correct_answer':'E','formal_text':row['record']['question'],
                 'point_coordinates_exact':points,'proof_method':'All 20 unordered triples and every strictly convex cyclic quadruple, with integer cross/dot/squared-distance arithmetic. No numerical tolerance.',
                 'triangles':triangles,'convex_quadrilaterals':quads,'option_witnesses':witnesses,
                 'uniqueness':'Each of A-D has its own exact permitted construction, so no listed type is impossible. The sole correct response is E. Extra colored line segments cannot change the six allowed corners or the existential word can.',
                 'trapezium_definition':'For Plane423 B uses exactly one parallel pair, which is a trapezium under both inclusive and exclusive British definitions.',
                 'count_summary':{'triangle_types':{k:sum(t['type']==k for t in triangles) for k in ('acute','right','obtuse','degenerate')},
                                  'convex_quad_count':len(quads)}}
    save(OWN/qid/'mathematical_proof.json',proof)
    print(qid,json.dumps(proof.get('option_witnesses',proof.get('ordered_mod9_cycle')),ensure_ascii=False))
    if 'count_summary' in proof: print(json.dumps(proof['count_summary']))
