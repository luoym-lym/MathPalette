from bootstrap import *
from math_tools import cells,is_exterior
c=read(OWN/'current_context.json');o={x['id']:x for x in c['objects']};src=cells(c,'given_');dst=cells(c,'E_')
groups=[('vertical_span3','#DC2626',['given_35','given_37'],['E_10','E_13'],lambda p:(p[0]+11,p[1]-8)),('horizontal_span3','#2563EB',['given_1','given_19'],['E_1','E_12'],lambda p:(p[0]+13,p[1]-6))]
data=[]
for name,color,source_targets,target_targets,T in groups:
    for st,tt in zip(source_targets,target_targets):
        assert is_exterior(o[st]['geometry']['points'],src) and is_exterior(o[tt]['geometry']['points'],dst)
        assert set(map(T,o[st]['geometry']['points']))==set(map(tuple,o[tt]['geometry']['points']))
    ps=[p for t in source_targets for p in o[t]['geometry']['points']];pt=[p for t in target_targets for p in o[t]['geometry']['points']]
    axis=1 if name.startswith('vertical') else 0
    assert max(p[axis] for p in ps)-min(p[axis] for p in ps)==3
    assert max(p[axis] for p in pt)-min(p[axis] for p in pt)==3
    data.append({'group':name,'color':color,'source_targets':source_targets,'E_targets':target_targets,'source_points':ps,'E_points':pt,'two_unit_end_segments_with_one_unit_black_gap':True})
srow={(x,y) for x,y in src if y==7};scol={(x,y) for x,y in src if x==14}
erow={(x,y) for x,y in dst if y==1};ecol={(x,y) for x,y in dst if x==25}
assert len(srow)==len(scol)==len(erow)==len(ecol)==3 and not srow&scol and len(erow&ecol)==1
save('hypothesis_v9_E_two_span_end_pairs.json',{'at_utc':now(),'question_id':'Plane213','variant_id':'user233_E_independent_three_span_endpairs_v9','wrong_preset':'E','information_groups':data,'specific_true_relations':'The source complete3-cell bottom row and complete3-cell rightmost column are each3 cells long. E complete central3-cell row/column also span3. Two one-unit end fragments with a one-unit existing black gap encode each full span, with exact per-group rigid maps; no internal edge is colored in either diagram.','new_misconception':'Matching the two3-cell one-dimensional spans is mistaken for a matching piece/tiling. The source two compared cell runs are disjoint(6 cells), whereas E row/column overlap in1 cell(5 cells); incidence and3-copy global coverage remain essential. No common two-group spatial map is claimed.','source_run_cells':{'bottom_row':sorted(srow),'rightmost_column':sorted(scol),'intersection':[]},'E_run_cells':{'central_row':sorted(erow),'central_column':sorted(ecol),'intersection':sorted(erow&ecol)},'difference_from_old':'Not the old E connected four-link RURU stair, nor any2×3 B corner,4-unit C/D run or corner inventory. It compares two separately true3-cell extents by their complete end-fragment patterns, with a new overlap/incidence misconception.','concision':'8 exterior unit-edge actions: two ends in each of two groups, on two diagrams. Each end is needed to encode its span; existing middle black gap is deliberately retained in BOTH diagrams.','rejected_internal_line_version':'Coloring full E central row/column boundary chains would style2 interior edges and could appear to impose a1/1/3 cut partition on the candidate. That presentation is rejected before rendering/testing. The proposed end-pair version colors exterior edges only and creates no cut barrier.','current_user_reference':'Current Plane233 paired red/blue existing-boundary comparisons.','requires_native_clarity_fresh_render_replay_zero_prior_gate_immutable_preset_then_exact_two_calls':True,'no_extra_API_calls_in_derivation':0,'current_eligibility':eligibility()})
print(json.dumps({'variant_id':'user233_E_independent_three_span_endpairs_v9','source_runs_overlap':0,'E_runs_overlap':1,'all_proposed_marks_exterior':True,'new_API_calls':0}))
