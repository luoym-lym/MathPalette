from env54 import *
from fractions import Fraction as F
import base64
import math
from dataset_tools import catalog

QIDS=read(BASE/'background_54_assignment.json')['question_ids']
manual={
'Plane251':{'finals':['22','59'],'values':['22','59'],'mechanism_observation':'Neither run uses the matched side2 triangle as a unit. Run1 invents8 base units and rectangular decomposition; run2 invents9 base units and subtracts spurious corner counts. Both wrong, both MISS preset5.625.'},
'Plane291':{'finals':['D','B'],'values':['1/2','3/8'],'mechanism_observation':'Run1 treats all gray as one half-rectangle below a diagonal, not the predeclared full-height-to-half-height substitution. Run2 explicitly uses correct1/2 height and returnsB3/8. One hit, NOT two; do not promote or relabel oldv02.'},
'Plane345':{'finals':['C','C'],'values':['76cm','76cm'],'mechanism_observation':'Both finals correctly derive2L=5s, s4, H18, W20 and perimeter76. Both MISS predeclaredE90; nine-unit-edge perimeter hypothesis not observed.'},
'Plane346':{'finals':['D','E'],'values':['24cm x16cm','30cm x20cm'],'mechanism_observation':'Both rejectC because20:12 does not match the explicitly given6:4 grid ratio. First returnsD despite a wrong approximate area; second returns exact choiceE dimensions after a false3.43-cell decomposition. Intended internal-line count error not observed. Run2 final states30x20 rather than a terminal letter; its exact value consistently maps toE, notC.'}}

def polygon_area(coords):
    return abs(sum(F(str(x))*F(str(coords[(i+1)%len(coords)][1]))-F(str(y))*F(str(coords[(i+1)%len(coords)][0])) for i,(x,y) in enumerate(coords)))/2

crosschecks={}
for q in ['Plane293','Plane350']:
    scene=read(OWN/q/'source_scene_snapshot.json')
    shapes={}
    for o in scene['objects']:
        if o.get('semantic_fill'):
            xy=[scene['points'][p] if isinstance(p,str) else p for p in o['points']]
            shapes[o['id']]=str(polygon_area(xy))
    crosschecks[q]=shapes
assert sorted(crosschecks['Plane350'].values())==['1','1','1','1','2','2']
assert sum(F(v) for k,v in crosschecks['Plane293'].items() if k.startswith('black0_'))==1
for panel in range(4):assert sum(F(v) for k,v in crosschecks['Plane293'].items() if k.startswith(f'black{panel}_'))==1
assert [F(16)-F(10),F(14)-F(6),F(17)-F(8),F(13)-F(9)]==[6,8,9,4]
save('exact_geometry_crosschecks.json',{'rational_polygon_areas':crosschecks,'Plane343_radii':{'A':10,'B':6,'C':8,'D':9,'E':4},'Plane346_analytic_grid_area':'(16+pi)-(4+pi)=12','Plane251_exact_area_in_unit_triangles':'(5/2)*(4+5)/2/(1/2)=45/2'})

enum=read(OWN/'Plane351/lattice_enumeration.json')
points=[[-2,0],[-1,-1],[0,-2],[0,-1],[1,-2],[2,-2]]
partial=[(0,1),(1,2),(2,3),(3,4),(4,2),(4,5)]
edges={frozenset((tuple(a),tuple(b))) for a,b in enum['edges']}
assert all(frozenset((tuple(points[a]),tuple(points[b]))) in edges for a,b in partial)
save('Plane351/actual_partial_edge_membership.json',{'exact_axial_map':'x=4+q+r/2, y=sqrt3+r*sqrt3/2','P0_to_P5_axial':points,'partial_edge_indices':partial,'each_actual_partial_stick_is_one_of_42':True,'visible_sticks_remain6':'Only original gapped segments, no new sticks or dots.'})

current={q:eligibility(q) for q in QIDS}
assert all(e['eligible'] for e in current.values())
save('current_eligibility_final.json',current)
assessments=[];newpairs=[];queue=[];all_calls=0
for q in QIDS:
    maths=read(OWN/q/'mathematical_audit.json')
    candidates=list((OWN/q).glob('r54_*/design.json'))
    a={'question_id':q,'assessed_at':now(),'mathematical_audit':str(OWN/q/'mathematical_audit.json'),'actual_formal_png_and_source_jpg_native_viewed':True,'formal_answer':current[q]['formal_record']['answer'],'current_original_approval_matches':True,'source_scene_snapshot_sha256':sha(OWN/q/'source_scene_snapshot.json'),'fresh_context_sha256':sha(OWN/q/'context.json'),'baseline':read(OWN/q/'baseline.json')}
    if not candidates:
        a.update(status='assessed_skip_no_clear_material_new_binding',concrete_reason=maths['skip'],API_calls=0)
    else:
        assert len(candidates)==1
        root=candidates[0].parent;design=read(candidates[0]);summaries=list((root/'tests').glob('*/summary.json'))
        assert len(summaries)==1
        summary=read(summaries[0]);evidence=summaries[0].parent
        binding=read(evidence/'binding.json');request=read(evidence/'request.json')
        image_data=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
        assert summary['two_completed'] and len(summary['results'])==2
        assert len(list(evidence.glob('run_*_started.json')))==2
        assert image_data==(root/'candidate.png').read_bytes()
        assert sha(evidence/'request.json')==binding['request_body_sha256']
        assert sha(evidence/'design_snapshot.json')==sha(root/'design.json')==binding['design_sha256']
        assert sha(root/'candidate.png')==binding['image_sha256']==design['image_sha256']
        assert (evidence/'design_snapshot.json').read_bytes()==(root/'design.json').read_bytes()
        assert request['messages'][1]['content'][0]['text']==current[q]['formal_record']['question']==binding['question']
        assert len(request['messages'])==2 and len(request['messages'][1]['content'])==2
        assert set(request)=={'model','stream','thinking','messages'}
        assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
        assert request['messages'][0]=={'role':'system','content':binding['system_prompt']}
        assert catalog.digest(current[q]['formal_record'])==binding['question_record_sha256']
        assert binding['expected_wrong_answer']==design['expected_wrong_answer']
        assert read(root/'api_process_finished.json')['harness_returned_or_raised']
        manual_runs=[]
        for i,expected_final in enumerate(manual[q]['finals'],1):
            rawpath=evidence/f'run_{i:02d}_response.json';raw=read(rawpath);job=read(evidence/f'run_{i:02d}.json')
            assert job['status']=='completed' and sha(rawpath)==job['response_sha256']
            assert job['request_body_sha256']==binding['request_body_sha256']
            assert raw['choices'][0]['finish_reason']=='stop'
            manual_runs.append({'run_index':i,'status':'completed','full_final_response':raw['choices'][0]['message']['content'],'full_raw_response_path':str(rawpath),'response_sha256':sha(rawpath),'manually_read_complete':True,'terminal_answer':expected_final,'terminal_value':manual[q]['values'][i-1],'hits_immutable_preset':str(expected_final)==str(design['expected_wrong_answer']),'request_body_sha256':job['request_body_sha256'],'image_sha256':binding['image_sha256'],'design_sha256':binding['design_sha256'],'finish_reason':raw['choices'][0]['finish_reason']})
        twohit=all(x['hits_immutable_preset'] for x in manual_runs)
        finals={'question_id':q,'variant_id':design['variant_id'],'read_at':now(),'role':'Primary manual full-response reading; no independent review','expected_wrong_answer':design['expected_wrong_answer'],'honest_final_answers':manual[q]['finals'],'two_hits':twohit,'observed_mechanism_and_limits':manual[q]['mechanism_observation'],'runs':manual_runs,'original_controls':'No previous controls found for these4 questions; none newly called. No causal/incremental claim.'}
        save(root/'manual_finals.json',finals)
        evidence_files=[p for p in evidence.iterdir() if p.is_file()]
        b={'question_id':q,'variant_id':design['variant_id'],'expected_wrong_answer':design['expected_wrong_answer'],'manual_finals':manual[q]['finals'],'two_completed':True,'two_hits':twohit,'evidence_path':str(evidence),'binding_sha256':sha(evidence/'binding.json'),'image_path':str(root/'candidate.png'),'image_sha256':sha(root/'candidate.png'),'pixel_sha256':design['pixel_sha256'],'design_path':str(root/'design.json'),'design_sha256':sha(root/'design.json'),'plugin_path':str(root/'plugin.json'),'plugin_sha256':sha(root/'plugin.json'),'difference_audit_path':str(root/'design_difference_audit.json'),'difference_audit_sha256':sha(root/'design_difference_audit.json'),'primary_review_path':str(root/'primary_review.json'),'manual_finals_path':str(root/'manual_finals.json'),'complete_evidence_file_hashes':{str(p):sha(p) for p in evidence_files},'all_frozen_bindings_passed':True,'solver_only_formal_question_plus_png':True,'original_model_profile_system_thinking_disabled_and_no_token_timeout_overrides':True,'full_manual_finals':manual_runs}
        save(root/'evidence_binding_audit.json',b)
        newpairs.append(b);all_calls+=2
        a.update(status='tested_new_material_candidate_preset_miss' if not twohit else 'primary_twohit_requires_NEW_parent_review',API_calls=2,variant_id=design['variant_id'],new_vs_old=read(root/'design_difference_audit.json')['material_difference'],preset=design['expected_wrong_answer'],manual_finals=manual[q]['finals'],two_hits=twohit,primary_review=str(root/'primary_review.json'),evidence_binding_audit=str(root/'evidence_binding_audit.json'))
        if twohit:queue.append(b)
    save(OWN/q/'assessment.json',a);assessments.append(a)
assert all_calls==8 and not queue
save('evidence_binding_audit.json',{'checked_at':now(),'new_pairs':newpairs,'all8_actual_calls_completed':True,'API_errors':0,'API_aborts':0,'API_retries':0,'original_control_calls':0,'local_pre_request_launch_failure':str(OWN/'local_launch_failure_01.json')})

# Mutable progress files are diagnostic context. Read all their current UTF8
# bytes, retain exact selected rows/attempts, and do not rewrite old snapshots.
metadata={}
for name in ['inventory.json','exploration_report.json','remaining_questions.jsonl']:
    p=BASE/name
    data=catalog.rows(p) if p.suffix=='.jsonl' else read(p)
    if name=='inventory.json':
        plane=data['PlaneGeometry'];selected={}
        for group in ['eligible','excluded']:
            val=plane[group]
            if isinstance(val,list):selected[group]=[x for x in val if isinstance(x,dict) and x.get('question_id',x.get('id')) in QIDS]
            elif isinstance(val,dict):selected[group]={k:v for k,v in val.items() if k in QIDS}
        data=selected
    elif name=='exploration_report.json':
        data=[x for x in data['attempts'] if x.get('question_id',x.get('id')) in QIDS]
    else:data=[x for x in data if x.get('question_id',x.get('id')) in QIDS]
    metadata[name]={'current_sha256':sha(p),'selected_scope_context':data,'classification':'Mutable runtime diagnostic metadata; not a frozen original; historical hashes remain unmodified.'}
save('mutable_metadata_context.json',metadata)

start=read(OWN/'readonly_hashes_start.json')
after={p:sha(PROJECT/p) if (PROJECT/p).is_file() else None for p in start}
changed={p:{'before':old,'after':after[p]} for p,old in start.items() if old!=after[p]}
save('readonly_hashes_final.json',after)
preservation={'checked_at':now(),'tracked_readonly_file_count':len(start),'changed_or_missing_readonly_files':changed,'all_scoped_frozen_formal_source_old_evidence_and_existing_batches_unchanged':not changed,'per_question_current_approval_fingerprints':{q:e['current_content_sha256'] for q,e in current.items()},'formal_state_current_hashes':current[QIDS[0]]['authoritative_hashes'],'own_write_scope':str(OWN),'write_guard_before_project_imports':True,'no_entire_workspace_unchanged_claim':True,'no_git_env_formal_approval_or_Pass_Collect_write':True,'all_new_explicit_file_cache_temp_log_request_paths_inside_own_root':True}
save('source_preservation_final.json',preservation)
assert not changed,changed
save('second_review_queue.json',{'stage':'material_refinement','unit':'background_54','created_at':now(),'candidates':queue,'count':len(queue),'held_candidates':[],'reason_empty':'No new candidate hit its own immutable preset in both complete calls. Old4 pairs also remain misses.','parent_instruction':'Only parent may create a NEW independent review for a qualifying new pair. No independent approval, delivery, Pass or Collect performed.'})

checkpoint={'unit':'background_54','stage':'material_refinement','status':'completed_assigned_scope','completed_at':now(),'branch':'PlaneGeometry','assigned_question_ids':QIDS,'actual_assessed_question_ids':QIDS,'unworked_question_ids':[],'assessed_question_count':8,'new_candidate_count':4,'new_complete_candidate_pairs':4,'actual_API_calls':8,'original_control_calls':0,'API_errors':0,'API_aborts':0,'API_retries':0,'credible_new_twohit_possibilities':0,'stop_reason':'All8 assigned refinement questions assessed with independent math/native/source/history checks;4 clear new targeted candidates received exactly2 real calls each and4 concrete skips.','old_vs_new':{'old_Plane291':{'v01':{'preset':'D','finals':['A','B'],'two_hits':False},'v02':{'preset':'A','finals':['B','D'],'two_hits':False}},'old_Plane293':{'rotated_square_scale_binding':{'preset':'C','finals':['D','B'],'two_hits':False},'triangle_count_scale_transfer':{'preset':'D','finals':['C','A'],'two_hits':False}},'others':'Prior screening only, no saved variant/API. RelatedPlane405 andPlane395 old screenings fully retained.','new':[{k:x[k] for k in ['question_id','variant_id','expected_wrong_answer','manual_finals','two_hits']} for x in newpairs]},'assessments':assessments,'new_pair_bindings':newpairs,'history_audit':str(OWN/'history_audit.json'),'old_history_manifest':str(OWN/'old_history_manifest.json'),'current_eligibility':str(OWN/'current_eligibility_final.json'),'source_and_old_evidence_hashes':str(OWN/'readonly_hashes_final.json'),'source_preservation':preservation,'second_review_queue':str(OWN/'second_review_queue.json'),'new_semantic_review':'Original semantic gray/black/colored membership, labels, number of sticks, source topology and2D view preserved. No invented circle/radius, puzzle piece, relation symbol, gridpoint, legend or question rewrite. Plane350 color-target ambiguity avoided by skipping.','primary_math_and_native_each_marker_reviews':'Everyquestion/mathematical_audit.json; testedquestions/r54_*/primary_review.json plus frozen per-marker design roles and path_fingerprints. Formal and source JPGs plus4old and4new candidate PNGs actually viewed.','failures':[read(OWN/'local_launch_failure_01.json'),read(OWN/'read_query_failure_02.json')],'failure_limits':'The OpenBLAS failure occurred BEFORE any API request/binding/started evidence; subsequent invocation is the first and only actual API pair for that frozen candidate. The metadata query failure was read-only. All exact raw provider responses and immutable evidence remain saved.','process_closure':'All4 API wrapper processes returned and their PTY sessions reported exit0. External final own-PID/command check recorded in process_closure_final.json.','process_closure_path':str(OWN/'process_closure_final.json'),'local_OPENBLAS_NUM_THREADS':os.environ.get('OPENBLAS_NUM_THREADS'),'solver_profile_unchanged':True,'harness_routing_audit':str(OWN/'harness_routing_audit.json'),'no_approval_delivery_Pass_Collect_or_formal_change':True,'parent_NEW_independent_review_required':True}
save('checkpoint.json',checkpoint)
save('artifact_hashes_final.json',{str(p.relative_to(OWN)):sha(p) for p in OWN.rglob('*') if p.is_file() and p.name not in ['artifact_hashes_final.json','process_closure_final.json']})
print(json.dumps({'assessed':8,'new_pairs':4,'actual_calls':8,'new_twohit':0,'old_readonly_files_verified':len(start),'changed_readonly_files':len(changed),'checkpoint_sha256':sha(OWN/'checkpoint.json'),'source_hash_manifest_sha256':sha(OWN/'readonly_hashes_final.json'),'evidence_audit_sha256':sha(OWN/'evidence_binding_audit.json')},ensure_ascii=False),flush=True)
