from unit_env import *
from mathvision_plugins import PluginRenderer
from render_plugins import check_schema
from workbench_io import environment_versions

R,B='#DC2626','#2563EB'
def interval(context,target,start,end,color):
    path=next(t for t in context['canvas']['targets'] if t['id']==target)['partial_paths'][0]
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5,
            'interval':{'path_id':path['id'],'path_sha256':path['sha256'],
                        'start':start,'end':end,'wrap':False}}
def style(target,color):
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}
config,adapter,first=adapter_context('Plane211')
for qid in QIDS:
    meta=first if qid=='Plane211' else adapter.inspect_question(qid)
    eligibility_now=eligibility(qid)
    assert eligibility_now['eligible']
    if qid=='Plane211':
        vid='adjacent_gap_to_short_closure'
        # The circle path starts at the bottom, passes right at .25 and top at .5.
        # .4-.5 is strictly within the true adjacent source gap between label 1 (50deg) and 9 (90deg).
        # It does not pretend that parameter .4 is the exact location of point 1.
        actions=[interval(meta,f'circle{i}',0.4,0.5,R) for i in range(6)]
        actions += [style(f'edge{i}_{j}',B) for i in (0,1,2,5) for j in (0,1)]
        actions += [style('edge2_4',R)]
        roles=[]
        for i,a in enumerate(actions):
            if i<6:
                roles.append({'action_index':i,'source':'actual adjacent cyclic gap from label 1 toward label 9',
                              'recipient':('B existing short closing chord 9-1' if i==0 else 'same gap in this corresponding result circle'),
                              'information':'The 0.4..0.5 native circle path interval is contained inside the adjacent 1/9 gap; it is not a cut or added chord.',
                              'purpose':('Supply the concrete cyclic-neighbor gap compared with the candidate closing chord.' if i==0
                                         else 'Preserve the exact source circle ink in every result panel, including E, so literal colored-ink continuation stays possible.')})
            elif i<14:
                roles.append({'action_index':i,'source':'actual given 1-3 / 3-5 source prefix',
                              'recipient':a['target'],'information':'These are precisely the given prefix chords, present in source/A/B/E.',
                              'purpose':'Distinguish true given prefix from the red adjacent-gap closure and preserve its blue ink in all prefix-containing panels.'})
            else:
                roles.append({'action_index':i,'source':'red adjacent cyclic 9/1 gap in source',
                              'recipient':'B existing chord from 9 directly to 1','information':'Same pair of endpoint labels on the source circle and B closing chord, but adjacency is not a skip-two edge.',
                              'purpose':'Invite the specific false shortcut from neighboring cyclic labels to premature closure at 1, in contrast to the true next point 2.'})
        expected,value='B','(B)'
        mechanism='The blue lines identify the exact given prefix. The red source arc lies in the actual adjacent 9/1 gap, and the red B short closing chord joins that same pair. The predicted mistake is using a local neighbor-gap-to-chord match to implement return to 1 prematurely. Correct continuation is 9 to 2, because one must skip 1. This targets cyclic closure semantics through an arc/chord relation, not odd-group membership or the failed A paired-motif mapping.'
        human='Nine source points and all result points, labels, circles and edge graphs remain unchanged. Every result circle preserves the same source red interval; every panel containing the given prefix preserves its blue strokes. Even literal colored-circle ink leaves E available and uniquely graph-correct. The red interval stays inside one genuine neighboring-label gap, does not add a spoke or point, and does not assert an extra connection in the source. Native interval .4 starts near angle54deg, not exactly at point1; no exact arc-endpoint equality is claimed.'
        difference='Old B trial marked five odd point centers only. The first new trial compared repeated two-chord motifs in A. This new candidate uses an existing circle interval and the existing B 9-1 chord as a concrete cyclic-gap versus closing-edge correspondence; it has no point grouping and preserves source ink in all panels. It is not a recoloring, linewidth change, filename change, or reuse of either prior PNG.'
    else:
        vid='native_orthogonal_span_comparison'
        actions=[interval(meta,'h5',13/34,29/34,R),interval(meta,'v3',1/6,0.7,B)]
        if qid=='Plane364': actions.append(interval(meta,'h3',5/34,21/34,R))
        roles=[{'action_index':0,'source':'P1=(3,5)','recipient':'P2=(7,5)',
                'information':'An existing horizontal grid interval spans exactly 4 units between original marked points.',
                'purpose':'Compare the horizontal lattice direction and its length to the blue vertical span; not an added side or new allowed-corner rule.'},
               {'action_index':1,'source':'P5=(3,1)','recipient':'P1=(3,5)',
                'information':'An existing vertical grid interval spans exactly 4 units and meets the red interval at the original P1 point.',
                'purpose':'Provide the real orthogonal direction and equal 4-unit span, establishing an axis-based comparison without adding angle ticks or conditions.'}]
        if qid=='Plane364': roles.append({'action_index':2,'source':'P3=(1,3)','recipient':'P4=(5,3)',
                'information':'A second actual horizontal 4-unit span is displaced left by 2 units from the first.',
                'purpose':'Compare alignment of equal horizontal spans: their endpoints do not form any axis-aligned square, while the true tilted square still exists.'})
        expected='A' if qid=='Plane364' else 'D'
        value='square' if qid=='Plane364' else 'obtuse-angled triangle'
        mechanism=('The two red horizontal 4-unit marked-point spans are staggered, and the blue vertical 4-unit marked-point span is between them at x=3. There is no axis-aligned square among all six points. The predicted error is restricting square search to these original lattice directions, missing the exact tilted square whose sides have vectors (2,2) and (2,-2), and answering A.' if qid=='Plane364'
                   else 'The red horizontal and blue vertical equal 4-unit spans meet at P1 and form the two existing grid legs of a right isosceles triangle P5/P1/P2. The predicted mistake is importing this orthogonal grid-leg frame into angle classification generally, recognizing right/acute prototypes but falsely excluding an obtuse triangle (D). The actual set has eight obtuse triples.')
        human='Only color/width of two or three selected intervals on the original grid is modified. No new segment, dot, corner, label, circle, polygon, cut, or fixed point partition is introduced. All six black dots remain visibly distinct. Literal preprinted colored grid lines do not constrain which existing points may be joined: all original exact witnesses and unique E answer remain valid. The segments have actual end coordinates at original marked points; they do not depict extra allowed corners.'
        difference='The first current trial added a true tilted square and compared its two opposite-vector classes. This trial adds no geometry and instead compares exact original horizontal/vertical lattice spans. Its wrong preset and error are different: axis-aligned-only square search for Plane364, and orthogonal-frame angle generalization for Plane423. It does not reuse the same failed PNG or merely change its colors/width.'
    folder=OWN/qid/vid
    folder.mkdir(parents=True,exist_ok=True)
    save(folder/'eligibility_before_design.json',eligibility_now)
    assert json.loads(json.dumps(meta))==read(OWN/qid/'context_v2.json')
    save(folder/'context.json',meta)
    renderer=PluginRenderer(config,adapter,{qid:meta})
    raw={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
         'description':'','intent':'','params':{'actions':actions}}
    check_schema(raw,renderer.schema,renderer.schema)
    plugin=renderer.normalize(raw)
    assert renderer.normalize(plugin)==plugin
    save(folder/'plugin_input.json',raw);save(folder/'plugin.json',plugin)
    p1,d1,x1=renderer.render(plugin,frozen=True)
    p2,d2,x2=renderer.render(plugin,frozen=True)
    assert p1==p2==plugin and d1==d2 and x1==x2
    (folder/'candidate.png').write_bytes(d1);(folder/'repeat.png').write_bytes(d2)
    hist=read(TASK/'history_index.json')
    collision=[]
    for q in hist['questions']:
        for d in q['designs']:
            if d.get('frozen_candidate_png_sha256')==sha(d1):collision.append(d['directory'])
    for path in OWN.glob('Plane*/**/design.json'):
        if read(path).get('candidate_sha256')==sha(d1):collision.append(str(path))
    assert not collision,collision
    save(folder/'history_difference_audit.json',{'created_at':now(),'exact_global_previous_candidate_matches':collision,
         'material_difference':difference,'all_old_history_read_log':str(OWN/'readin_audit.json'),
         'previous_current_failed_designs':[str(p) for p in (OWN/qid).glob('*/manual_full_final_review.json')]})
    transfer={'primary_reference':'Plane308','reference_png_sha256':sha((TASK/'references/Plane308/C01.png').read_bytes()),
              'reference_plugin_sha256':sha((TASK/'references/Plane308/C01.json').read_bytes()),
              'actual_current_reference_viewed':True,
              'migration':'Compare concrete point-to-point/edge relations using two colors; no parity rule or old option is transplanted. Each mark identifies a true cyclic gap or true orthogonal grid span.',
              'supporting_current_reference':'Plane233 open boundary comparison: local relation does not establish a globally valid completion.'}
    save(folder/'reference_transfer.json',transfer)
    design={'created_at':now(),'question_id':qid,'variant_id':vid,'expected_wrong_answer':expected,
            'expected_wrong_value':value,'correct_answer':'E','formal_record':eligibility_now['record'],
            'mathematical_proof':read(OWN/qid/'mathematical_proof.json'),'marker_roles':roles,
            'mechanism':mechanism,'human_semantics':human,'difference_from_old':difference,
            'remaining_risk':'The frame may be insufficiently persuasive; mathematical validity and readable true comparisons do not guarantee model errors. This is PRIMARY author judgement and requires new parent independent review if two-hit.',
            'candidate_sha256':sha(d1),'plugin_sha256':sha((folder/'plugin.json').read_bytes()),
            'context_sha256':sha((folder/'context.json').read_bytes()),
            'status':'FROZEN_BEFORE_BOTH_CALLS_PRIMARY_ONLY'}
    save(folder/'design.json',design)
    save(folder/'offline_gates.json',{'created_at':now(),'fresh_schema_sha256':sha((PROJECT/'PlaneGeometry/workbench/plugin.schema.json').read_bytes()),
         'schema_validation':True,'default_normalization_idempotent':True,'frozen_render_normalized_exact':True,
         'original_noop_pixel_equal':True,'repeat_PNG_bytes_exact':True,'repeat_pixel_sha256_exact':True,
         'current_context_exact_after_JSON_tuple_list_canonicalization':True,'candidate_sha256':sha(d1),
         'pixel_sha256':x1,'plugin_sha256':design['plugin_sha256'],'environment':environment_versions(),
         'adapter_manifest':adapter.manifest,'independent_process_replay':'pending'})
    print(json.dumps({'qid':qid,'vid':vid,'actions':len(actions),'image_sha256':sha(d1),'preset':expected}),flush=True)
checkpoint=read(OWN/'checkpoint.json')
checkpoint.update(updated_at=now(),status='material_refinements_prepared_replay_visual_pending',
                  question_status={q:'new_material_candidate_prepared_after_failed_first_trial' for q in QIDS})
save(OWN/'checkpoint.json',checkpoint,replace=True)
