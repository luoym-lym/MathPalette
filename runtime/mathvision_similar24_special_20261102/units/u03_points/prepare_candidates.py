from unit_env import *
from mathvision_plugins import PluginRenderer
from render_plugins import check_schema
from workbench_io import pixel_hash, environment_versions
from dataset_tools.mathvision_workbench import png_bytes

R, B = '#DC2626', '#2563EB'
def style(target,color):
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}

def grid_spec(qid):
    context = read(OWN/qid/'context_v2.json')
    xy = {p['id']:p['xy'] for p in context['snap_points']}
    pairs = [('P3','P1',R),('P5','P4',R),('P1','P4',B),('P3','P5',B)]
    actions,roles = [],[]
    for i,(a,b,c) in enumerate(pairs):
        actions.append({'type':'add_line','id':f'vector{i+1}','endpoints':[xy[a],xy[b]],
                        'color':c,'linestyle':'solid'})
        roles.append({'action_index':i,'source':{'point_ids':[a,b],'xy':[xy[a],xy[b]]},
                      'recipient':'the other same-colored opposite edge, and the other-colored adjacent edge',
                      'information':('Exact displacement (2,2), shared by the red opposite pair.' if c==R
                                     else 'Exact displacement (2,-2), shared by the blue opposite pair.'),
                      'purpose':'Compare two real equal-length perpendicular direction classes in one permitted square; supplies concrete geometric relations, not an arbitrary option-letter highlight.'})
    return {'question_id':qid,'variant_id':'square_opposite_vector_comparison', 'expected_wrong_answer':'B',
            'expected_wrong_value':('parallelogram with different long sides' if qid=='Plane364' else 'trapezium'),
            'actions':actions,'marker_roles':roles,
            'mechanism':('The red opposite vector pair (2,2) and blue opposite vector pair (2,-2) form the exact permitted tilted square. The predicted error is generalizing this witnessed equal-sided parallelogram to every available parallelogram, falsely excluding unequal adjacent sides (B).' if qid=='Plane364'
                         else 'The two exact opposite vector pairs of the displayed square both give parallel opposite sides. The predicted error is overgeneralizing this concrete two-parallel-pair example to all possible four-point figures, falsely excluding a proper one-parallel-pair trapezium (B).'),
            'human_semantics':'The question quantifies over figures that can be drawn from some of six marked points. The four auxiliary segments connect only original marked points. No new dots, labels, equality ticks, parallel arrows, corner restrictions, or cuts are introduced. Even if the square is read as preprinted colored ink, all six allowed cornerpoints and the existential selection remain unchanged: every exact A-D witness remains drawable over or beside that ink, so E is still unique. This is a displayed example, not a declared exhaustive list of permitted lines. A closed square in a grid is an actual valid figure, not a partition or cutting instruction.',
            'difference_from_old':'All prior Plane364/423 assessments were untested prescreens about generic subsets. This design specifies two exact opposite vector classes, equality of adjacent squared lengths (8), and perpendicularity; the predicted mistake is an example-to-universal inference. It does not hide or recolor any point. No prior candidate PNG/actual request is listed for either question.',
            'remaining_risk':'Author primary semantic judgement only. A fresh parent reviewer must independently determine whether the displayed geometric comparison is sufficiently directed, concise, and unambiguous; model hits cannot settle that gate.'}

spec211 = {'question_id':'Plane211','variant_id':'paired_chord_motif_partial_completion','expected_wrong_answer':'A',
           'expected_wrong_value':'(A)',
           'actions':[style('edge0_0',R),style('edge0_1',B),
                      style('edge1_0',R),style('edge1_1',B),style('edge1_3',R),style('edge1_4',B),
                      style('edge2_0',R),style('edge2_1',B),style('edge5_0',R),style('edge5_1',B)],
           'marker_roles':[
             {'action_index':i,'target':target,'source':source,'recipient':recipient,'information':info,'purpose':purpose}
             for i,(target,source,recipient,info,purpose) in enumerate([
               ('edge0_0','source labels 1-3','all retained result prefix 1-3 chords','actual given first skip-two chord','Define the red chord motif.'),
               ('edge0_1','source labels 3-5','all retained result prefix 3-5 chords','actual given second skip-two chord','Define the blue chord motif.'),
               ('edge1_0','red source 1-3','A labels 1-3','identical labelled prefix chord','Map the first actual source stroke.'),
               ('edge1_1','blue source 3-5','A labels 3-5','identical labelled prefix chord','Map the second actual source stroke.'),
               ('edge1_3','red source skip-two chord','A labels 6-8','a second actual skip-two chord with the same chord length','Promote a repeated true local skip-two motif in A.'),
               ('edge1_4','blue source skip-two chord','A labels 8-1','another actual skip-two chord including a modular wrap','Pair the repeated motif across 9; this is not the old odd-only closure hypothesis.'),
               ('edge2_0','red source 1-3','B labels 1-3','identical existing prefix','Preserve literal color of the given stroke in every result containing that stroke.'),
               ('edge2_1','blue source 3-5','B labels 3-5','identical existing prefix','Preserve literal color of the given stroke in every result containing that stroke.'),
               ('edge5_0','red source 1-3','E labels 1-3','identical existing prefix','Keep the mathematically correct result compatible with literal continuation of the colored source.'),
               ('edge5_1','blue source 3-5','E labels 3-5','identical existing prefix','Keep the mathematically correct result compatible with literal continuation of the colored source.')])],
           'mechanism':'A contains the given two-chord prefix and a second red/blue pair of actual skip-two chords (6-8,8-1). The predicted mistake is accepting these repeated local chord-length motifs as a full completion, overlooking its uncolored adjacent step 5-6 and absent 5-7,7-9,9-2,2-4,4-6 edges. Wrong preset A is frozen before testing. This differs from the old odd-only subgroup B hypothesis.',
           'human_semantics':'All original edges, 54 dot centers, and 54 numeral labels remain. Source strokes 1-3 and 3-5 retain their red/blue colors in A, B, and E, the only panels containing those exact original strokes. Thus even a literal colored-ink continuation has E as its sole graph-valid result. New strokes have no specified color condition. A is graph-invalid because 5 connects to adjacent 6. No parity restriction, new route, deletion, hidden point, or new printed legend is introduced.',
           'difference_from_old':'Old odd_partition_closed_cycle colored only five odd source/B dots red and predicted B; two actual old finals were E. New design contains zero dot overlays, targets A, matches exact ordered source chords, compares their true chord-length motifs with 6-8/8-1 including an even-to-odd wrap, and preserves source ink in all prefix-containing options. This is a new local-motif completeness error, not a recoloring of the old odd-label partition.',
           'remaining_risk':'Two accurate motif matches may be insufficient to distract from the adjacent 5-6 error. No success is assumed. Independent second review belongs to the parent.'}

specs = [spec211,grid_spec('Plane364'),grid_spec('Plane423')]
config, adapter, first = adapter_context('Plane211')
for spec in specs:
    qid,vid = spec['question_id'],spec['variant_id']
    folder = OWN/qid/vid
    folder.mkdir(parents=True,exist_ok=True)
    eligible = eligibility(qid)
    save(folder/'eligibility_before_design.json',eligible)
    assert eligible['eligible']
    meta = first if qid=='Plane211' else adapter.inspect_question(qid)
    # JSON-normalize only tuple/list representation; no numeric tolerance.
    canon = lambda v: json.loads(json.dumps(v,ensure_ascii=False,allow_nan=False))
    assert canon(meta)==read(OWN/qid/'context_v2.json'), 'Real context changed'
    save(folder/'context.json',meta)
    renderer = PluginRenderer(config,adapter,{qid:meta})
    raw = {'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
           'description':'','intent':'','params':{'actions':spec['actions']}}
    check_schema(raw,renderer.schema,renderer.schema)
    normalized = renderer.normalize(raw)
    assert renderer.normalize(normalized)==normalized
    save(folder/'plugin_input.json',raw)
    save(folder/'plugin.json',normalized)
    n1,data1,pix1=renderer.render(normalized,frozen=True)
    n2,data2,pix2=renderer.render(normalized,frozen=True)
    assert n1==n2==normalized and data1==data2 and pix1==pix2
    (folder/'candidate.png').write_bytes(data1)
    (folder/'repeat.png').write_bytes(data2)
    current_schema=(PROJECT/'PlaneGeometry/workbench/plugin.schema.json').read_bytes()
    save(folder/'offline_gates.json',{'created_at':now(),'fresh_schema_sha256':sha(current_schema),
       'schema_validation':True,'default_normalization_idempotent':True,'frozen_render_normalized_exact':True,
       'original_noop_pixel_equal':True,'repeat_PNG_bytes_exact':True,'repeat_pixel_sha256_exact':True,
       'current_context_exact_after_JSON_tuple_list_canonicalization':True,'candidate_sha256':sha(data1),
       'pixel_sha256':pix1,'plugin_sha256':sha((folder/'plugin.json').read_bytes()),
       'environment':environment_versions(),'adapter_manifest':adapter.manifest,
       'independent_process_replay':'pending'})
    # Global history collision audit on exact PNG SHA, including other question IDs.
    hist=read(TASK/'history_index.json')
    matches=[]
    for oldq in hist['questions']:
        for d in oldq['designs']:
            if d.get('frozen_candidate_png_sha256')==sha(data1):
                matches.append({'qid':oldq['question_id'],'directory':d['directory'],
                                'prior_actual_calls':d['unique_started_call_count_from_saved_records'],
                                'do_not_retest':d['do_not_retest_this_frozen_png']})
    assert not matches,'Old candidate reused'
    save(folder/'history_difference_audit.json',{'created_at':now(),'history_index_sha256':sha((TASK/'history_index.json').read_bytes()),
         'exact_global_old_candidate_hash_matches':matches,'same_question_old_designs':next(q['designs'] for q in hist['questions'] if q['question_id']==qid),
         'material_difference':spec['difference_from_old'],
         'same_base_different_question_authorization':('Plane364 and Plane423 share a formal PNG but have different exact formal texts/options; current user explicitly authorized transferring this point/vector comparison. Each must get its own two calls. No failed other-question PNG is used.' if qid!='Plane211' else None)})
    transfer={'primary_reference':'Plane308','current_reference_png_sha256':sha((TASK/'references/Plane308/C01.png').read_bytes()),
              'current_reference_plugin_sha256':sha((TASK/'references/Plane308/C01.json').read_bytes()),
              'observed_current_method':'Actual source odd (1,3,5) red and even (2,4,6) blue, compared with A red/blue triangle contours; not old contiguous 1/2/3 vs 4/5/6 groups.',
              'transfer':'Two colors carry actual geometric source/recipient relations. Here exact chord motifs are compared across source/candidate panels.' if qid=='Plane211'
                         else 'Two colors carry exact point-to-point vector classes and their adjacent/opposite edge relation in a permitted square. Colors carry no extra restriction on which of six points may be used.',
              'other_current_references_inspected':list(read(TASK/'reference_manifest.json')),
              'supporting_open_boundary_method':'Plane233 current L-boundary comparison demonstrates local geometric match is not a global solution. It supplies a general local-to-global mistake type, not a transplanted wrong answer.'}
    save(folder/'reference_transfer.json',transfer)
    proof=read(OWN/qid/'mathematical_proof.json')
    design={**{k:v for k,v in spec.items() if k!='actions'},'created_at':now(),
            'correct_answer':'E','formal_record':eligible['record'],'mathematical_proof':proof,
            'candidate_sha256':sha(data1),'plugin_sha256':sha((folder/'plugin.json').read_bytes()),
            'context_sha256':sha((folder/'context.json').read_bytes()),
            'original_source_approval_content_sha256':eligible['current_content_sha256'],
            'status':'FROZEN_BEFORE_BOTH_CALLS_PRIMARY_ONLY','no_Pass_Collect_or_independent_review':True}
    save(folder/'design.json',design)
    print(json.dumps({'qid':qid,'variant':vid,'candidate':str(folder/'candidate.png'),
                      'image_sha256':sha(data1),'actions':len(normalized['params']['actions']),
                      'predicted':spec['expected_wrong_answer'],'offline_gates':True},ensure_ascii=False),flush=True)
checkpoint=read(OWN/'checkpoint.json')
checkpoint.update(updated_at=now(),status='three_candidates_offline_rendered_visual_and_replay_pending',unworked=[],
                  question_status={q:'candidate_needs_primary_visual_and_independent_replay' for q in QIDS})
save(OWN/'checkpoint.json',checkpoint,replace=True)
