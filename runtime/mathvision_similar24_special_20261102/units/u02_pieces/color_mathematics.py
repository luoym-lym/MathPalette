from mathematics import *

BLACK = '#000000'; RED = '#DC2626'; BLUE = '#2563EB'

def gridedges(cells):
    output = {}
    for x,y in cells:
        vs = [(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
        for a,b in zip(vs,vs[1:]+vs[:1]): output[edge(a,b)] = BLACK
    return output

def colored218():
    groups = recover218(); out = {k:gridedges(c) for k,c in groups.items()}
    for e in out['given']:
        if e[0][0] == e[1][0] and e[0][0] in (0,4): out['given'][e] = RED
    for l in 'ABCDE':
        for e in out[l]:
            a,b = e
            yes = ((a[0]==b[0]==0) if l in 'AE' else
                   (a[1]==b[1]==2) if l=='B' else
                   (a[0]==b[0] and (a[0]==0 or a[0]==4)) if l in 'CD' else False)
            if yes: out[l][e] = RED
    return groups,out

def colored398():
    groups = recover398(); out = {k:gridedges(c) for k,c in groups.items()}
    for k in groups:
        for e in out[k]:
            a,b = e
            if k=='piece1': continue
            if k=='A':
                if a[0]==b[0]==4: out[k][e] = RED
                if a[1]==b[1]==4: out[k][e] = BLUE
            else:
                if a[1]==b[1]==4: out[k][e] = RED
                if a[0]==b[0]==0: out[k][e] = BLUE
    return groups,out

def move_edges(piece_edges, placement):
    def f(p):
        x,y=p
        if placement['reflected']: x=-x
        for _ in range(placement['rotation_quarter_turns']): x,y=-y,x
        return x,y
    vertices = {f(p) for e in piece_edges for p in e}
    minx=min(x for x,y in vertices); miny=min(y for x,y in vertices)
    dx,dy=placement['translation']
    def v(p):
        x,y=f(p); return x-minx+dx,y-miny+dy
    return {edge(v(a),v(b)):color for (a,b),color in piece_edges.items()}

def ink_match(piece_edges, placement, board_edges):
    moved = move_edges(piece_edges,placement)
    return all(e in board_edges and board_edges[e]==color for e,color in moved.items())

def edge_encode(edges):
    return [{'endpoints':e,'color':c} for e,c in sorted(edges.items()) if c!=BLACK]

def audit218():
    groups,colors=colored218(); board=groups['given']; result={}
    for l in 'ABCDE':
        ps = [p for p in placements(groups[l],board,reflections=False)
              if ink_match(colors[l],p,colors['given'])]
        pairs=[(i,j) for i,j in combinations(range(len(ps)),2)
               if not(set(ps[i]['cells'])&set(ps[j]['cells']))]
        result[l]={'ink_preserving_placement_count':len(ps),'ink_preserving_disjoint_pair_count':len(pairs),
            'one_witness':[{'transform':{k:v for k,v in ps[i].items() if k!='cells'},
                            'cells':encode(ps[i]['cells']),
                            'transported_colored_edges':edge_encode(move_edges(colors[l],ps[i]))}
                            for i in pairs[0]] if pairs else [],
            'red_units_per_piece':sum(c==RED for c in colors[l].values()),
            'red_units_in_two_pieces':2*sum(c==RED for c in colors[l].values())}
    assert [l for l in 'ABCDE' if result[l]['ink_preserving_disjoint_pair_count']==0]==['A']
    assert [l for l in 'ABCDE' if result[l]['red_units_in_two_pieces']!=6]==['D']
    report={'question_id':'Plane218','created_at':now(),'unique_answer_annotation_reading':'A',
      'unique_answer_color_preserving_material_reading':'A',
      'method':'For every rotation and grid translation, transport every unit edge of the candidate, including all black internal grid edges, and require exact equality with source-grid ink at every covered edge. Then require two disjoint copies. Unused two squares may retain source ink. A has no geometric pair at all; B-E have explicit color-preserving rotation-only pairs.',
      'source_colored_edges':edge_encode(colors['given']),
      'candidate_colored_edges':{l:edge_encode(colors[l]) for l in 'ABCDE'},
      'source_total_red_units':6,'results':result,
      'targeted_wrong_inference':'Only D carries four red units in its two copies versus six on the original board. Treating all source red border as compulsory retained perimeter incorrectly excludes D, because the unused two edge cells retain the other two units. The formal task only cuts two pieces out; it does not use the entire grid.',
      'no_new_condition_needed_for_original_unique_answer':True}
    write(OWN/'Plane218/p03_color_preserving_boundary_proof.json',report)
    return report,colors

def audit398():
    groups,colors=colored398(); results={}
    for l in 'ABCDE':
        board=groups[l]
        pp=[[p for p in placements(groups[k],board,reflections=False,match_fill=True)
             if ink_match(colors[k],p,colors[l])] for k in ('piece1','piece2')]
        sols=[(i,j) for i,a in enumerate(pp[0]) for j,b in enumerate(pp[1])
              if not(set(a['cells'])&set(b['cells'])) and set(a['cells'])|set(b['cells'])==set(board)]
        results[l]={'ink_preserving_solution_count':len(sols),
          'one_witness':{k:{'transform':{n:v for n,v in pp[j][idx].items() if n!='cells'},
                              'cells':encode(pp[j][idx]['cells']),
                              'transported_colored_edges':edge_encode(move_edges(colors[k],pp[j][idx]))}
                         for j,(k,idx) in enumerate(zip(('piece1','piece2'),sols[0]))} if sols else {}}
    assert [l for l in 'ABCDE' if results[l]['ink_preserving_solution_count']==0]==['E']
    report={'question_id':'Plane398','created_at':now(),'unique_answer_annotation_reading':'E',
      'unique_answer_color_preserving_material_reading':'E',
      'method':'Transport all black/white cells and every original unit edge with its exact ink color under all rotations and translations. Require both source pieces to match each target cell/edge, with disjoint coverage of all 16 cells. A-D each retain their original unique rotation-only assembly with every colored edge present in its true image. E was geometrically/pattern-wise impossible and remains impossible.',
      'source_colored_edges':{k:edge_encode(colors[k]) for k in ('piece1','piece2')},
      'target_colored_edges':{l:edge_encode(colors[l]) for l in 'ABCDE'},'results':results,
      'targeted_wrong_inference':'The L top arm is red and its left arm blue. A correctly has red on its right and blue on its top after a clockwise quarter-turn; B-D correctly retain red top/blue left. E has the same local red-top/blue-left four-unit spans as a tempting trial placement, but its black-white cells forbid that placement and every alternative. Rejecting A merely for changing color orientation, while accepting E for local arm-color alignment, is the frozen predicted error.',
      'uncolored_square_piece_preserved':True,'no_new_condition_needed_for_original_unique_answer':True}
    write(OWN/'Plane398/p03_color_preserving_boundary_proof.json',report)
    return report,colors

if __name__=='__main__':
    for q,fn in [('Plane218',audit218),('Plane398',audit398)]:
        report, colors=fn()
        print(json.dumps({'question_id':q,'literal_material_answer':report['unique_answer_color_preserving_material_reading'],
                          'results':{l:{k:v for k,v in r.items() if k!='one_witness'} for l,r in report['results'].items()}},ensure_ascii=False))
