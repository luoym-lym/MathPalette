from worker import *
from itertools import combinations

def normalize(cells):
    x0 = min(x for x,y in cells); y0 = min(y for x,y in cells)
    return {(x-x0,y-y0): v for (x,y),v in cells.items()}

def orientations(cells, reflections=True):
    results = []
    for reflected in ((False, True) if reflections else (False,)):
        for rotation in range(4):
            transformed = {((-x if reflected else x),y):v for (x,y),v in cells.items()}
            for _ in range(rotation):
                transformed = {(-y,x):v for (x,y),v in transformed.items()}
            transformed = normalize(transformed)
            if not any(transformed == r['cells'] for r in results):
                results.append({'reflected': reflected, 'rotation_quarter_turns': rotation, 'cells': transformed})
    return results

def encode(cells):
    return [[x,y,v] for (x,y),v in sorted(cells.items())]

def edge(a,b):
    return tuple(sorted((tuple(a),tuple(b))))

def recover218():
    context = read(OWN / 'Plane218/context.json')
    results = {}
    for prefix in ('given', 'A','B','C','D','E'):
        edges = {edge(*o['geometry']['points']) for o in context['objects'] if o['id'].startswith(prefix+'_')}
        vertices = {p for e in edges for p in e}
        cells = {}
        for x,y in vertices:
            contour = [((x,y),(x+1,y)), ((x+1,y),(x+1,y+1)),
                       ((x+1,y+1),(x,y+1)), ((x,y+1),(x,y))]
            if all(edge(a,b) in edges for a,b in contour): cells[(x,y)] = False
        results[prefix] = normalize(cells)
    return results

def placements(piece, board, reflections=True, match_fill=False):
    output = []
    for oi, orientation in enumerate(orientations(piece, reflections)):
        for dx in range(max(x for x,y in board)+1):
            for dy in range(max(y for x,y in board)+1):
                moved = {(x+dx,y+dy):v for (x,y),v in orientation['cells'].items()}
                if set(moved) <= set(board) and (not match_fill or all(board[p] == v for p,v in moved.items())):
                    output.append({'orientation_index': oi,
                                   'reflected': orientation['reflected'],
                                   'rotation_quarter_turns': orientation['rotation_quarter_turns'],
                                   'translation': [dx,dy], 'cells': moved})
    return output

def enumerate218():
    groups = recover218(); board = groups['given']; results = {}
    assert set(board) == {(x,y) for x in range(4) for y in range(3)}
    for let in 'ABCDE':
        piece = groups[let]; assert len(piece) == 5
        allp = placements(piece, board)
        sols = [(i,j) for i,j in combinations(range(len(allp)),2)
                if not (set(allp[i]['cells']) & set(allp[j]['cells']))]
        rotationp = placements(piece, board, reflections=False)
        rotsols = [(i,j) for i,j in combinations(range(len(rotationp)),2)
                   if not(set(rotationp[i]['cells']) & set(rotationp[j]['cells']))]
        results[let] = {'cells': encode(piece), 'orientation_count': len(orientations(piece)),
                        'placement_count': len(allp), 'unordered_disjoint_pair_count': len(sols),
                        'all_placements': [{**p,'cells':encode(p['cells'])} for p in allp],
                        'all_disjoint_pairs_by_placement_index': sols,
                        'rotation_only_disjoint_pair_count': len(rotsols),
                        'constructive_rotation_only_witness': [encode(rotationp[i]['cells']) for i in rotsols[0]] if rotsols else [],
                        'unused_cell_count_for_each_witness': 2}
        if not sols:
            results[let]['complete_pairwise_intersection_certificate'] = [
                {'pair':[i,j], 'intersection': sorted(set(allp[i]['cells']) & set(allp[j]['cells']))}
                for i,j in combinations(range(len(allp)),2)]
    assert [l for l in 'ABCDE' if results[l]['unordered_disjoint_pair_count'] == 0] == ['A']
    assert all(results[l]['rotation_only_disjoint_pair_count'] for l in 'BCDE')
    report = {'question_id':'Plane218', 'created_at':now(), 'unique_correct_answer':'A',
        'independent_recomputed_not_formal_answer_as_proof':True,
        'actual_original_JPG_and_formal_PNG_viewed':True,
        'interpretation':'The printed candidates are five unit-cell shapes; cut on the displayed square-grid lines. Two identical geometric pieces may be rotated or turned over. They need disjoint interiors, not coverage of all twelve cells. Two cells remain unused.',
        'completeness':'Recover each candidate unit cell independently by testing its four edges in current captured frozen geometry. Enumerate all D4 grid orientations and every integer translation inside the 4 by 3 board, then every unordered pair. A has nonempty intersection in all 28 placement pairs. B-E each have a rotation-only disjoint witness; permitting reflections does not affect the unique exclusion.',
        'board':encode(board), 'results':results,
        'brief_coverage_wording_correction':'Coverage language in the preparation brief is not imposed: 5+5 is 10, not 12. The authoritative formal wording only asks for two identical pieces cut from the grid.'}
    write(OWN / 'Plane218/primary_mathematical_proof.json', report)
    return report

def recover398():
    scene = read(OWN / 'Plane398/frozen_scene_readonly_snapshot.json')
    groups = {}
    for o in scene['objects']:
        oid = o['id']
        if not oid.startswith('cell'): continue
        points = [scene['points'][p] for p in o['points']]
        assert len(set(x for x,y in points)) == 2 and len(set(y for x,y in points)) == 2
        x = min(x for x,y in points); y = min(y for x,y in points)
        group = 'piece1' if oid.startswith('cellpiece1') else 'piece2' if oid.startswith('cellpiece2') else oid[4]
        groups.setdefault(group,{})[(x,y)] = bool(o.get('semantic_fill',False))
    return {g:normalize(c) for g,c in groups.items()}

def enumerate398():
    groups = recover398(); results = {}
    for let in 'ABCDE':
        board = groups[let]; assert set(board) == {(x,y) for x in range(4) for y in range(4)}
        pp = [placements(groups[p],board,match_fill=True) for p in ('piece1','piece2')]
        sols = [(i,j) for i,a in enumerate(pp[0]) for j,b in enumerate(pp[1])
                if not(set(a['cells']) & set(b['cells'])) and set(a['cells']) | set(b['cells']) == set(board)]
        rotation_pp = [placements(groups[p],board,reflections=False,match_fill=True) for p in ('piece1','piece2')]
        rotation_sols = [(i,j) for i,a in enumerate(rotation_pp[0]) for j,b in enumerate(rotation_pp[1])
                         if not(set(a['cells']) & set(b['cells'])) and set(a['cells']) | set(b['cells']) == set(board)]
        results[let] = {'board_cells':encode(board),'full_D4_solution_count':len(sols),
            'all_pattern_matching_placements': {p:[{**a,'cells':encode(a['cells'])} for a in ps]
                for p,ps in zip(('piece1','piece2'),pp)},
            'all_solutions_by_placement_index':sols,
            'rotation_only_solution_count':len(rotation_sols),
            'rotation_only_witness':{p:{**rotation_pp[k][idx], 'cells':encode(rotation_pp[k][idx]['cells'])}
                for k,(p,idx) in enumerate(zip(('piece1','piece2'),rotation_sols[0]))} if rotation_sols else {}}
    assert [l for l in 'ABCDE' if results[l]['full_D4_solution_count'] == 0] == ['E']
    assert all(results[l]['rotation_only_solution_count'] for l in 'ABCD')
    report = {'question_id':'Plane398','created_at':now(),'unique_correct_answer':'E',
        'independent_recomputed_not_formal_answer_as_proof':True,
        'actual_original_JPG_and_formal_PNG_viewed':True,
        'pieces':{p:encode(groups[p]) for p in ('piece1','piece2')},
        'completeness':'The 7-cell L has two arm endpoints at distance 4*sqrt(2), the diameter of the 4x4 target. Any contained isometric copy must carry these endpoints to opposite target corners. Its orientation is therefore a multiple of a quarter-turn or reflection and its position is corner-aligned. The other piece is the complementary 3x3 square. Enumeration of all D4 orientations and all integer translations is exhaustive, even if arbitrary rigid motions were initially contemplated. Match all black and white cells, require disjoint interiors and exactly all 16 cells. A-D each admit a rotation-only witness; E has no witness even with reflections.',
        'results':results}
    write(OWN / 'Plane398/primary_mathematical_proof.json', report)
    return report

if __name__ == '__main__':
    for q, fn in [('Plane218',enumerate218),('Plane398',enumerate398)]:
        report = fn()
        print(json.dumps({'question_id':q,'unique_answer':report['unique_correct_answer'],
              'results':{l:{k:v for k,v in r.items() if k in
                   ('orientation_count','placement_count','unordered_disjoint_pair_count','rotation_only_disjoint_pair_count',
                    'full_D4_solution_count','rotation_only_solution_count','rotation_only_witness')}
                    for l,r in report['results'].items()}},ensure_ascii=False))
