import bootstrap
from bootstrap import OWN,ROOT,HISTORY
import json,hashlib,itertools,sys
from datetime import datetime,timezone
from bridge_adapter import RuntimeBridgeAdapter
from partial_style import object_paths, describe_paths
from dataset_tools import catalog
from workbench_io import canonical_hash,file_hash
ad=RuntimeBridgeAdapter()
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
def save(p,v):
    data=json.dumps(v,ensure_ascii=False,indent=2)+'\n'
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8') as f:f.write(data)
def native(q):return json.loads((ROOT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/q/'scene.json').read_text(encoding='utf-8-sig'))
def eligible(q):
    r=next(json.loads(l) for l in (ROOT/'SolidGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if json.loads(l)['id']==q)
    notes,_=catalog._source_notes_snapshot(ROOT);ap=json.loads((ROOT/'provenance/approvals.json').read_text(encoding='utf-8-sig'))['approvals'][q]
    assert r['source_dataset']=='MathVision' and catalog.digest(catalog.content(ROOT,'SolidGeometry',r,source_notes=notes))==ap['content_sha256']
    special=ROOT/'SolidGeometry/special_variant'
    indices={}
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p=special/name;rows=[json.loads(l) for l in p.read_text(encoding='utf-8-sig').splitlines() if l.strip()];hits=[x for x in rows if x.get('question_id')==q];assert not hits
        indices[name]={'sha256':file_hash(p),'matching_records':hits}
    assert not (special/q/'recipes.json').exists() and not (special/q/'collection.json').exists()
    return {'checked_at':datetime.now(timezone.utc).isoformat(),'formal_mathvision':True,'noPass':True,'notCollected':True,'noSpecialCompletion':True,'approval_matches':True,'original_approval':ap,'current_record_sha256':canonical_hash(r),'indices':indices}
def rotations():
    for perm in itertools.permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in itertools.product([-1,1],repeat=3):
            if parity*signs[0]*signs[1]*signs[2]==1:yield perm,signs
def norm(c):return tuple(sorted(tuple(p[i]-min(x[i] for x in c) for i in range(3)) for p in c))
def matches(c,d):
    target=norm(d)
    return any(norm([tuple(signs[i]*p[perm[i]] for i in range(3)) for p in c])==target for perm,signs in rotations())
def connected(c):
    c=set(map(tuple,c));seen={next(iter(c))}
    while True:
        nxt=seen|{p for p in c if any(sum(abs(p[i]-q[i]) for i in range(3))==1 for q in seen)}
        if nxt==seen:return seen==c
        seen=nxt
def roll(state,d):
    s=state.copy()
    cyc={'E':('U','L','D','R'),'W':('U','R','D','L'),'N':('U','F','D','B'),'S':('U','B','D','F')}[d]
    for a,b in zip(cyc,cyc[1:]+cyc[:1]):s[a]=state[b]
    return s
def states(start,route):
    out=[start]
    for d in route:out.append(roll(out[-1],d))
    return out
def mathproof(q):
    n=native(q)
    if q=='Solid91':
        route='EEESSSWWWNNN';initial={k:k for k in 'UDFBRL'};ends=[states(initial,route*i)[-1] for i in range(1,4)]
        assert ends[-1]==initial and ends[0]!=initial and ends[1]!=initial
        return {'route':route,'initial':initial,'lap_end_states':ends,'unique_first_return':3,'wrong_rule':'Three successive four-roll groups are assumed identity regardless of changing axes. Actual groups EEES,SSWW,WNNN each mix axes; a count of four alone does not imply identity.'}
    if q=='Solid175':
        start={k:k for k in 'UDFBRL'};ss=states(start,'EENENE');bottom=[s['D'] for s in ss];assert bottom[0]==bottom[5] and len(set(bottom))==6
        return {'cells':n['roll_verification']['position_cells'],'route':'EENENE','exact_states':ss,'bottom_labels':bottom,'unique_pair':[1,6],'unique_correct_choice':'B','wrong_rule':'Consecutive transitions 1->2->3->4->5 total four quarter rolls, but E,E,N,E is not four rolls about one axis. Direction-free period-four shortcut predicts 1/5, choice C.'}
    if q=='Solid191':
        start={'U':3,'D':4,'F':2,'B':5,'R':1,'L':6};ss=states(start,'EESSEEE');wrong=states(start,'EEEEESS');assert ss[-1]['U']==6 and wrong[-1]['U']==1
        return {'route':'EESSEEE','exact_states':ss,'unique_end_top':6,'intermediate_lower_panel_state':ss[1],'wrong_reordered_route':'EEEEESS','wrong_route_states':wrong,'wrong_top':1,'reason':'Five east rolls at separated stages cannot be reordered past the two intervening south rolls.'}
    if q=='Solid150':
        proof=n['dot_count_proof'];assert proof['surface_dots']==105
        return {'cube_centers':proof['cube_centers'],'contacts':[{'central_face_normal':list(v),'outer_cube_center':[0.5+v[0],0.5+v[1],0.5+v[2]]} for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]],'all_dots':7*21,'central_hidden':21,'matching_arm_hidden':21,'visible_surface_total':147-21-21,'opposed_arm_grouping':'Three true opposite arms correspond to three pairs of opposite central faces. Equal glued numbers mean each pair totals7 on the arm side,21 across all6. Central side also totals21. This uses the ordinary opposite-pair convention implicit in the approved diagram problem; the full six central faces sum21 independently.','wrong_rule':'147-3*7=126 subtracts one copy of each matched interface pair; both incident faces actually disappear.','all_contacts_are_frozen_original':True}
    if q=='Solid147':
        pcs=n['piece_cells'];other=pcs['light']+pcs['dark'];box=list(itertools.product(range(3),range(2),range(2)));white=[list(c) for c in box if list(c) not in other];m={chr(65+i):matches(o,white) for i,o in enumerate(pcs['options'])};assert [k for k,v in m.items() if v]==['D']
        return {'visible_other_cells':other,'box':box,'white_complement':white,'proper_rotation_count':24,'option_matches':m,'unique_correct_choice':'D','wrong_shape_A':pcs['options'][0],'new_misconception':'The two exposed white terminals are extrapolated to an end-attached planar L rather than the forced center-attached T. A and C are rotated L forms in the original; marks target the specific A terminal presentation, not a claim that A is a unique geometric alternative.','white_degree_sequence':sorted(sum(sum(abs(a[i]-b[i]) for i in range(3))==1 for b in white) for a in white)}
    if q=='Solid198':
        colors={tuple(x['cube']):x['material'] for x in n['piece_colors']};vis={p:c for p,c in colors.items() if p[1]==0 or p[2]==1 or p[0]==3};hidden=[p for p in colors if p not in vis];all_assignments=[]
        for assignment in itertools.product(['black','dark','gray','white'],repeat=len(hidden)):
            full={**vis,**dict(zip(hidden,assignment))}
            if any(sum(c==m for c in full.values())!=4 for m in ['black','dark','gray','white']):continue
            pcs={m:[list(p) for p,c in full.items() if c==m] for m in ['black','dark','gray','white']}
            valid=all(connected(p) for p in pcs.values());all_assignments.append({'hidden_assignment':list(zip(hidden,assignment)),'connected':{m:connected(p) for m,p in pcs.items()},'valid':valid,'pieces':pcs})
        valid=[a for a in all_assignments if a['valid']];assert len(valid)==1
        white=valid[0]['pieces']['white'];m={k:matches(o,white) for k,o in n['option_cube_sets'].items()};assert [k for k,v in m.items() if v]==['C']
        return {'visible_materials':[{'cube':p,'material':c} for p,c in vis.items()],'hidden_cells':hidden,'all_quota_compatible_assignments':all_assignments,'white':white,'option_matches_24_proper_rotations':m,'unique_correct_choice':'C','wrong_shape_B':n['option_cube_sets']['B'],'new_misconception':'The shared seam and directed front rim of the two visible white cap faces are matched to B. The unseen return leg is then incorrectly completed out of the white plane rather than the forced planar staggered pair. B is a spatial hook; this is neither old D aligned-square completion nor old E separated-end long-row completion.'}
def make(q,variant,preset,groups,new,old):
    directory=OWN/q/variant;ctx=ad.inspect_question(q);objects={x['id']:x for x in ctx['objects']};actions=[];roles=[]
    for targets,color,role in groups:
        for target in targets:
            assert target in objects and objects[target]['styleable']
            a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':2}
            actions.append(a);roles.append({'action_index':len(actions)-1,'target':target,'role':role,'source_geometry':objects[target].get('geometry'),'frozen_visibility':objects[target].get('frozen_visibility')})
    difference={'stage':'material_refinement','question_id':q,'variant_id':variant,'recorded_before_render_and_calls_at':datetime.now(timezone.utc).isoformat(),'old_history_manifest':str(OWN/q/'old_evidence_manifest.json'),'old_full_text':str(OWN/q/'old_full_text_read.txt'),'old_outcomes_and_mechanisms':old,'substantive_new_information_or_misconception':new,'why_not_cosmetic':'Targets and geometric correspondence/grouping change, as enumerated below. The preset is derived from the newly stated error, not selected from old final answers. PNG/hash differences are not the basis of novelty.','new_groups':groups,'preset_before_calls':preset,'old_evidence_readonly':True,'prior_independent_objections_found':[]}
    if not (directory/'design_difference_audit.json').exists():save(directory/'design_difference_audit.json',difference)
    if not (directory/'eligibility_at_render.json').exists():save(directory/'eligibility_at_render.json',eligible(q))
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':new,'intent':new,'params':{'actions':actions}}
    # Adapter intentionally creates its directory atomically; audit exists in the parent, so render into a dedicated frozen subdirectory.
    report=json.loads((directory/'frozen/render_check.json').read_text(encoding='utf-8')) if (directory/'frozen/render_check.json').exists() else ad.render_candidate(plugin,directory/'frozen')
    scene=ad.scene(q)
    try:
        paths={target:describe_paths(scene,target) for target in dict.fromkeys(a['target'] for a in actions)}
    finally:scene.close()
    if (directory/'fresh_target_paths.json').exists():(directory/'fresh_target_paths.json').rename(directory/'fresh_target_paths.incomplete_before_serialization_fix.json')
    save(directory/'fresh_target_paths.json',paths)
    math=mathproof(q);save(directory/'primary_math_audit.json',math)
    design={'stage':'material_refinement','question_id':q,'variant_id':variant,'expected_wrong_answer':preset,'correct_answer':ad.records[q]['answer'],'frozen_before_calls_at':datetime.now(timezone.utc).isoformat(),'new_rationale':new,'design_difference_audit_sha256':file_hash(directory/'design_difference_audit.json'),'candidate_png':str(directory/'frozen/candidate.png'),'candidate_sha256':report['png_sha256'],'plugin_sha256':file_hash(directory/'frozen/plugin.json'),'marker_roles':roles,'mathematics':math,'status':'UNREVIEWED primary only; parent NEW independent review mandatory','human_semantics':'Existing visible original edges only. No added cuts, dots, relation symbols, text, fills, arrows, cube pieces, geometry or projection changes. Every original distinction must be checked on the actual PNG before calls.'}
    save(directory/'design.json',design)
    print(json.dumps({'question_id':q,'variant_id':variant,'preset':preset,'png':str(directory/'frozen/candidate.png'),'sha256':report['png_sha256'],'action_count':len(actions),'baseline_match':report['baseline_matches_formal'],'deterministic':report['deterministic']},ensure_ascii=False),flush=True)

specs={
'Solid175':('r29_four_hinge_axis_collapse','C',[
(['grid1','grid5','grid9','grid10'],RED,'Four consecutive actual shared contact hinges for transitions 1->2,2->3,3->4,4->5. Equal appearance groups quarter-roll count while real hinge-axis changes remain visible.'),
(['grid15','grid16'],BLUE,'The two later actual hinges 5->6 and6->7 distinguish the remainder after the falsely completed four-roll group.')],
'Group the first four consecutive roll hinges as one direction-free period-four cycle, predicting the same bottom at1and5 (C) despite the E,E,N,E axis change.',
'Old false_roll_pair merely colored bottom boundaries1and7 to predictA; complete finalsB/B. New design styles six actual shared transition hinges in chronological groups, rather than endpoint salience.'),
'Solid191':('r29_separated_east_hinge_commutation','1',[
(['panel0grid1part0','panel0diee4','panel0grid5part0','panel0grid14part0','panel0grid17part0','panel0grid20part0'],RED,'Five eastward transition hinges, first two before and last three after the southward pair. The coincident initial grid/die edge is styled consistently, not counted as an extra roll.'),
(['panel0grid7part0','panel0grid10part0'],BLUE,'Two southward transition hinges; visually isolate the intervening operation that the false rule commutes past the red family.')],
'Bind the five eastward roll hinges across separated stages into one family and the two intervening south hinges into another; false reordering EESSEEE -> EEEEESS yields top1.',
'Old top_face_identity_transfer paired top/front face rims across two panels, preset3, complete finals1/2. New design leaves those face rims unmarked and instead encodes separated ground-hinge families; target1 is independently derived from the new reordered rigid-roll sequence, not copied from the old final1.'),
'Solid91':('r29_three_four_hinge_cycles','1',[
(['ground10part0','diee4','ground17part0','ground23part0','ground32part0'],RED,'First four actual chronological hinges E,E,E,S; coincident die/ground initial hinge has two source IDs for one physical line.'),
(['ground29part0','ground27part0','ground20part0','ground14part0'],BLUE,'Next four chronological hinges S,S,W,W; the mixed axis directions stay geometrically visible.'),
(['ground1part0','ground2part0','ground5part0','ground8part0','diee0'],GREEN,'Last four chronological hinges W,N,N,N; coincident terminal footprint edge styled with both source IDs.')],
'Partition the twelve real contact hinges into three chronological groups of four. The error treats each mixed-axis four-roll group as a full orientation cycle, predicting one lap.',
'Old opposed_run_cancellation grouped opposite long boundary runs by parallel axes and predicted1; finals3/1. New groups follow transition order and cross corners, invoking direction-free four-step periodicity rather than cancellation of opposed runs. Outer curbs remain mostly black.'),
'Solid150':('r29_opposed_arm_single_interface_count','126',[
(['crosse11','crosse13','crosse4','crosse7'],RED,'Open two-edge top motifs on the negative-x and positive-x arms identify a true opposite pair of protruding cubes.'),
(['crosse19','crosse22','crosse16','crosse17'],BLUE,'Open motifs on the negative-y foreground arm and the partially visible positive-y back arm identify the second opposite pair without exposing any hidden line.'),
(['crosse25','crosse28','crosse32','crosse33'],GREEN,'Open motifs on upper/lower arms identify the third opposite pair. Three paired arm families correspond to the three opposite-face families of the hidden central die.')],
'Match all six arm cubes into three true opposite-direction pairs, then induce counting one copy of the six matching glue-face values:147-21=126 instead of subtracting both sides of every interface.',
'Old unit13 screened without a candidate because generic emphasis of three visible arms lacked a counterpart. This design explicitly identifies both members of every opposite arm pair, including partial rear/lower features, and states the six-interface one-side accounting error before calls.'),
'Solid147':('r29_end_branch_overhang_completion','A',[
(['givene17','givene12'],RED,'Front and left edges of the exposed upper white face locate the raised terminal in the source.'),
(['givene33','givene35'],BLUE,'Bottom and far vertical edges of the exposed lower-right rear white face locate the second terminal.'),
(['option0e17','option0e19'],RED,'Top/front and receding edges of A raised terminal form the false upper-terminal correspondence.'),
(['option0e0','option0e5'],BLUE,'Bottom and vertical edges of A opposite lower terminal complete a planar end-branch interpretation instead of the forced center-branch T.')],
'Bind the two exposed white terminal motifs to opposite ends of the planar L optionA, confusing an end-attached overhang with the true center-attached T hidden behind the colored front cells.',
'Old white_terminal_tripod_binding mapped source terminal faces to the three-axis tripodE, finalsE/B. New mapping tests planar graph attachment at an end (A) versus the true degree3 central branch(D); it uses new source front/lower exterior sides and entirely different option edges. A was not an old observed final.'),
}

def edge_ids(q,a,b,prefix):
    c=json.loads((OWN/q/'context.json').read_text(encoding='utf-8'))
    def close(x,y):return all(abs(i-j)<1e-11 for i,j in zip(x,y))
    out=[]
    for o in c['objects']:
        p=o.get('geometry',{}).get('points',[])
        if o['id'].startswith(prefix) and o.get('styleable') and len(p)==2 and isinstance(p[0],list) and (close(p[0],a) and close(p[1],b) or close(p[1],a) and close(p[0],b)):out.append(o['id'])
    assert out,(q,a,b,prefix)
    return out
def setup198():
    # Frozen option B is translated +5x,+5.7z; infer exact translation from original geometry, never from raster positions.
    n=native('Solid198');c=json.loads((OWN/'Solid198/context.json').read_text(encoding='utf-8'));be=[o for o in c['objects'] if o['id'].startswith('Be') and o.get('styleable')]
    pts=[p for o in be for p in o['geometry']['points']];offset=[min(p[i] for p in pts) for i in range(3)]
    # B local minimum=(0,0,0), so this is its actual scene translation.
    def bp(p):return [p[i]+offset[i] for i in range(3)]
    groups=[]
    for color,sp,bpair,role in [
        (RED,([11,1,13],[12,1,13]),([0,1,2],[1,1,2]),'Left front rim of source white cap / left front rim of B upper cap'),
        (BLUE,([12,1,13],[13,1,13]),([1,1,2],[2,1,2]),'Right front rim of source white cap / right front rim of B upper cap'),
        (GREEN,([12,1,13],[12,2,13]),([1,1,2],[1,2,2]),'Actual common receding seam between the two white cap faces / corresponding common seam of B')]:
        groups.append((edge_ids('Solid198',*sp,'main'),color,role+'; source feature.'))
        groups.append((edge_ids('Solid198',bp(bpair[0]),bp(bpair[1]),'Be'),color,role+'; false-completion counterpart.'))
    specs['Solid198']=('r29_cap_seam_to_spatial_return','B',groups,
        'Match the common seam and directed two-part front rim of the real white cap to B, then falsely place the hidden return leg out of its plane. The true completion is the planar staggered pair C.',
        'Old E long-row endpoint and D aligned-square completions used outer top L-rims; finalsC/EandD/A, neither an exact pair; a misbound D draft was rejected before calls. New B tests hidden out-of-plane return adjacency and its handed cap seam, with a newly selected common seam/front rim correspondence. B was not an old observed final; no old failed image/preset is repeated.')
if __name__=='__main__':
    if sys.argv[1]=='Solid198':setup198()
    q=sys.argv[1];make(q,*specs[q])
