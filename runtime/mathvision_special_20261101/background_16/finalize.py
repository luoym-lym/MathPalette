import tools_local as t
import base64

# These are manual interpretations after reading every complete answer body.
FINALS={
('Plane443','opposite_long_edge_binding'):['5:6','E'],
('Plane278','convex_neck_substitution'):['C','C'],
('Solid157','missing_foot_branch_swap'):['C','A'],
('Solid197','crease_side_binding'):['450','450'],
('Solid178','top_to_front_boundary_binding'):['19','11'],
('Solid151','checkerboard_corner_binding'):['B','C'],
('Solid189','plan_center_height_swap'):['9','32'],
('Solid222','staggered_face_cell_overlap'):['26','14'],
('Plane206','long_leg_whole_profile_binding'):['4','1'],
('Plane489','corner_face_incidence_binding'):['48/125','27/125'],
('Solid197','control_original'):['450','450']}
NOTES={
'Plane443':'Run1 explicitly rejects available choices and concludes5:6; not an A hit. Run2 explicitly finishes4:5,E. Neither is presetA.',
'Plane278':'Both complete finals select C. PresetD cannot be changed after these responses. The runs contain hallucinated piece/color properties, but final C is clear.',
'Solid157':'Run1 final C is correct; run2 final A matches the preset. This is onehit only, not a pair.',
'Solid197':'Both candidate finals explicitly450 despite materially different incorrect calculations. Both separate original controls also explicitly450. The repeated wrong final is real, but an incremental annotation effect has not been shown.',
'Solid178':'The finals are19 and11. Run1 intermediate13 is a claimed new-shell count, not the final; it is not a13 hit.',
'Solid151':'Run1 explicitly B; run2 explicitly C. The incidental C discussion in run1 is not its final. One presetC hit only.',
'Solid189':'Finals9 and32; neither is18. The narratives miscount columns and/or heights.',
'Solid222':'Finals26 and14, neither18. No incidental earlier count is substituted for the final.',
'Plane206':'Finals4 and1, neither3. Run2 reads the red rail as a proposed split: an additional semantic caution is retained even though the original unit-grid geometry and human8-cell counting remain clear.',
'Plane489':'Finals48/125 and27/125, neither53/125. No post-hoc preset or numerator selection.'}
proofs=t.json.loads((t.HERE/'primary_math_proofs.json').read_text())
source_audit={};source_changes=[]
for q in t.ASSIGNED:
    start=t.json.loads((t.HERE/q/'eligibility_start.json').read_text());end=t.eligibility(q)
    original=t.json.loads((t.HERE/q/'input_fingerprints.json').read_text())
    changed=[{'path':p,'before':digest,'after':t.file_hash(t.ROOT/p) if (t.ROOT/p).exists() else None} for p,digest in original['files'].items() if not (t.ROOT/p).exists() or t.file_hash(t.ROOT/p)!=digest]
    b='PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry';rec=next(r for r in t.rows(t.ROOT/b/'dataset.jsonl') if r['id']==q)
    same_record=t.canonical_hash(rec)==original['question_record_sha256']
    copied_original=t.file_hash(t.HERE/q/'original.png')==t.file_hash(t.ROOT/b/rec['image'])
    scene=t.json.loads((t.ROOT/b/rec['scene']).read_text(encoding='utf-8-sig'))
    components={k:t.canonical_hash(scene[k]) for k in ['points','objects','labels','view','projection','visibility','dimensions','distance_markers'] if k in scene}
    audit={'question_id':q,'initial_eligibility':start,'final_eligibility':end,'frozen_source_files_changed':changed,'question_record_unchanged':same_record,'original_approval_record_unchanged':start['approval']==end['approval'],'formal_png_matches_initial_native_viewed_copy':copied_original,'frozen_component_fingerprints':components,'source_native_png_viewed':True,'individual_frozen_inputs_preserved':not changed and same_record and copied_original,'source_classification':'Current formal MathVision record and valid user approval; no Pass, Collect, special completion, or existing delivery. Whole-workspace equality is neither asserted nor used.'}
    source_audit[q]=audit;source_changes+=changed
    assert audit['individual_frozen_inputs_preserved'] and end['eligible'] and audit['original_approval_record_unchanged']
t.write(t.HERE/'source_preservation_final.json',{'created_at':t.now(),'questions':source_audit,'all_individual_inputs_preserved':not source_changes,'external_changes_policy':'Concurrent unrelated Author-designed and aggregate/workbench changes preserved. No restore operation or whole-workspace hash equality claim. Runtime progress metadata hashes are diagnostic snapshots, not frozen original evidence.'})

def binding_audit(q,name,manual):
    p=t.HERE/q/name;design=t.json.loads((p/'design.json').read_text());dirs=list((p/'tests').glob('quicktest3_*'));assert len(dirs)==1
    ev=dirs[0];bind=t.json.loads((ev/'binding.json').read_text());request=(ev/'request.json').read_bytes();req=t.json.loads(request)
    image=(p/'candidate.png').read_bytes();db=(p/'design.json').read_bytes();sha=lambda b:t.hashlib.sha256(b).hexdigest()
    assert bind['image_sha256']==sha(image) and bind['design_sha256']==sha(db) and bind['request_body_sha256']==sha(request)
    assert (ev/'design_snapshot.json').read_bytes()==db and str(bind['expected_wrong_answer'])==str(design['expected_wrong_answer'])
    assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'} and req['stream'] is False
    assert set(req)=={'model','stream','thinking','messages'}
    assert len(req['messages'])==2 and req['messages'][0]=={'role':'system','content':bind['system_prompt']}
    user=req['messages'][1];assert user['role']=='user' and len(user['content'])==2
    record=t.json.loads((t.HERE/q/'formal_record.json').read_text());assert user['content'][0]=={'type':'text','text':record['question']}
    assert user['content'][1]['type']=='image_url' and base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])==image
    assert len(list(ev.glob('run_??_started.json')))==2 and len(list(ev.glob('run_??.json')))==2 and len(list(ev.glob('run_??_response.json')))==2
    entries=[]
    for i,answer in enumerate(manual,1):
        path=ev/f'run_{i:02d}.json';job=t.json.loads(path.read_text());raw=(ev/f'run_{i:02d}_response.json').read_bytes();response=t.json.loads(raw)
        assert job['status']=='completed' and job['response_sha256']==sha(raw)
        assert job['image_sha256']==sha(image) and job['design_sha256']==sha(db) and job['request_body_sha256']==sha(request)
        assert response['choices'][0]['finish_reason']=='stop'
        body=job['answer'];assert isinstance(body,str) and body.strip()
        entries.append({'run_index':i,'manual_final_answer':answer,'manual_hit_on_immutable_preset':answer==str(design['expected_wrong_answer']),'complete_answer_manually_read':True,'full_final_body':body,'answer_body_sha256':sha(body.encode('utf-8')),'raw_job_path':str(path),'raw_response_path':str(ev/f'run_{i:02d}_response.json'),'provider_finish_reason':'stop','status':'completed'})
    result={'question_id':q,'design_id':name,'expected_wrong_answer_frozen_before_calls':design['expected_wrong_answer'],'correct_formal_answer':record['answer'],'binding_path':str(ev/'binding.json'),'request_path':str(ev/'request.json'),'design_path':str(p/'design.json'),'design_sha256':sha(db),'png_sha256':sha(image),'exact_pair_same_png_same_predeclared_preset':True,'harness_sha256':t.file_hash(t.HERE/'quicktest3_isolated.py'),'harness_unchanged':t.file_hash(t.HERE/'quicktest3_isolated.py')==t.file_hash(t.BASE/'harness/quicktest3_isolated.py'),'solver_input_only_original_question_and_candidate_png':True,'request_profile_overrides':False,'exactly_two_calls_no_retry':True,'full_manual_finals':entries,'manual_review_note':NOTES[q],'status':'control' if name=='control_original' else 'primary_paired_hit_possibility' if all(e['manual_hit_on_immutable_preset'] for e in entries) else 'failed_predeclared_pair','independent_second_review_done':False}
    t.write(p/'manual_final_review.json',result)
    return result

allpairs=[binding_audit(q,n,v) for (q,n),v in FINALS.items()]
controls=[p for p in allpairs if p['status']=='control'];candidates=[p for p in allpairs if p['status']!='control'];possibilities=[p for p in candidates if p['status']=='primary_paired_hit_possibility']
assert len(candidates)==10 and len(possibilities)==1 and possibilities[0]['question_id']=='Solid197'
t.write(t.HERE/'evidence_binding_audit.json',{'created_at':t.now(),'all_exact_bindings_verified':True,'candidate_pairs':len(candidates),'control_pairs':len(controls),'calls':2*len(allpairs),'api_errors':0,'aborts':0,'retries':0,'pairs':allpairs})

for p in candidates:
    q=p['question_id'];name=p['design_id'];out=t.HERE/q/name;design=t.json.loads((out/'design.json').read_text());plugin=t.json.loads((out/'plugin.json').read_text());ctx=t.json.loads((t.HERE/q/'context.json').read_text());paths=t.json.loads((t.HERE/q/'paths_public.json').read_text());actions=plugin['params']['actions'];roles=design['marker_roles']
    if q=='Plane206':roles=['Source existing lower edge '+a['target']+' is one of the3 consecutive unit edges defining the input L long leg.' for a in actions[:3]]+roles[1:]
    assert len(roles)==len(actions)
    markers=[]
    for i,(action,role) in enumerate(zip(actions,roles),1):
        entry={'index':i,'normalized_action':action,'role':role,'primary_visual_readable':True,'new_explicit_relation_symbol':False,'original_fill_text_geometry_unchanged':True,'usefulness_review':'One member of the specific partial-feature correspondence described in the predeclared design. Per-marker causal ablation was not performed.'}
        if action['type']=='set_object_style':
            target=next(o for o in ctx['objects'] if o['id']==action['target']);assert target['styleable'];entry['source_object']=target
            entry['actual_paths']=paths[action['target']]
            if 'interval' in action:assert any(x['id']==action['interval']['path_id'] and x['sha256']==action['interval']['path_sha256'] for x in paths[action['target']])
        else:
            assert action['type']=='add_line';entry['endpoint_snap_points']=[[s for s in ctx['snap_points'] if s['xy']==xy] for xy in action['endpoints']];assert all(entry['endpoint_snap_points'])
        markers.append(entry)
    review={'question_id':q,'design_id':name,'reviewer_role':'primary research worker only','native_png_path':str(out/'candidate.png'),'native_visual_review':t.json.loads((out/'primary_visual.json').read_text()),'independent_primary_mathematical_proof':proofs[q],'proof_file':str(t.HERE/'primary_math_proofs.json'),'marker_reviews':markers,'exact_render_check':t.json.loads((out/'render_check.json').read_text()),'source_audit_file':str(t.HERE/'source_preservation_final.json'),'manual_test_review_file':str(out/'manual_final_review.json'),'original_controls':controls if q=='Solid197' else [],'human_semantics_review':'All original objects, text, semantic fills, frozen 3D/projection/visibility and unique answers are preserved. Marks lie on existing boundaries or intervals. No new closed puzzlepiece, cut or shaded unit is introduced. Matching colors are appearance cues, not added mathematical givens.','limitations':['Primary review only; a new independent second-review task is required before any delivery.','Two observed calls are not a statistical reliability estimate.','No human performance experiment or per-marker causal ablation.']+(['The unannotated original also produced450/450; no incremental annotation effect is established.'] if q=='Solid197' else [])+(['One solver described the existing red rail as a split; retain that semantic caution.'] if q=='Plane206' else []),'primary_disposition':p['status'],'approved':False,'published':False}
    t.write(out/'primary_review.json',review)

errors=[
 {'phase':'inspection_setup','questions':['Plane418','Solid151'],'error':'TypeError: Object of type ndarray is not JSON serializable when exporting internal object_paths segments.','resolution':'Preserved both partial invalid paths.json files; saved serializable exact controls/ids/hashes in new paths_public.json files. Renderers and formal inputs not modified. No API had started.'},
 {'phase':'design_setup','question_id':'Solid197','error':'KeyError frontsticker0: semantic fill faces are not styleable paths.','resolution':'Before any candidate/test existed, replaced attempted face-style operation by schema-allowed1pt add_line on exact existing snap-point endpoints. No fill alteration; no failed image or API retry.'},
 {'phase':'primary_proof_setup','question_id':'Solid200','error':'Assertion while reading source_patterns top matrix with an assumed y-major row convention.','resolution':'Used the actual transposed x-major mapping that is internally consistent with side-face cube colors;24-rotation enumeration then finds the unique maximum9. No design/test for this question. Metadata row label is not treated as a geometric input edit.'},
 {'phase':'read_only_view','question_id':'Plane443','error':'A first view call reached this path before the inspection process had created its original.png copy.','resolution':'Viewed the completed native PNG later. No API or output retry occurred.'}]
t.write(t.HERE/'errors_and_aborts.json',{'local_setup_errors':errors,'api_errors':[],'aborted_requests':[],'retries':[],'all_failed_or_diagnostic_files_preserved':True})

queue=[]
for p in possibilities:
    q=p['question_id'];n=p['design_id'];queue.append({'question_id':q,'branch':'SolidGeometry','design_id':n,'status':'NEEDS_NEW_PARENT_INDEPENDENT_SECOND_REVIEW','candidate_png':str(t.HERE/q/n/'candidate.png'),'plugin':str(t.HERE/q/n/'plugin.json'),'immutable_design':str(t.HERE/q/n/'design.json'),'expected_wrong_answer':'450','complete_manual_finals':['450','450'],'formal_correct_answer':'225','primary_review':str(t.HERE/q/n/'primary_review.json'),'manual_finals_and_raw_binding':str(t.HERE/q/n/'manual_final_review.json'),'independent_math_proof':str(t.HERE/'primary_math_proofs.json'),'source_audit':str(t.HERE/'source_preservation_final.json'),'control_finals':['450','450'],'control_evidence':str(t.HERE/'Solid197/control_original/manual_final_review.json'),'control_limitation':'Original also450/450; no measured incremental effect. Correct controls are not an added gate.','independent_review_instructions':'Start a NEW independent reviewer. Inspect actual native PNG and original, exact request/response/design/image bindings, unique225 proof and each of2 edge/crease marks. Review appearance cues and sticker-side/diagonal semantics. Do not treat this queue as approval or delivery.','pass_collect_or_publish_performed':False})
t.write(t.HERE/'second_review_queue.json',{'unit':'background_16','created_at':t.now(),'queue_count':len(queue),'requires_new_independent_reviewer_before_any_delivery':True,'candidates':queue})

assessed=[]
for q in t.ASSIGNED:
    designs=[p for p in candidates if p['question_id']==q]
    screen=t.json.loads((t.HERE/q/'prescreen.json').read_text()) if (t.HERE/q/'prescreen.json').exists() else None
    assert designs or screen
    assessed.append({'question_id':q,'source_audited':True,'native_original_viewed':True,'status':designs[0]['status'] if designs else 'screened_no_clean_hypothesis','design_ids':[p['design_id'] for p in designs],'prescreen':screen,'final_eligible':source_audit[q]['final_eligibility']['eligible']})

api_proc=t.json.loads((t.HERE/'api_processes_final.json').read_text(encoding='utf-8-sig'));assert api_proc['live_own_api_process_count']==0
manifest={}
for p in t.HERE.rglob('*'):
    if p.is_file() and not any(x in ('cache','mpl_cache','tmp','render_tmp','render_state','render_output') for x in p.relative_to(t.HERE).parts):manifest[p.relative_to(t.HERE).as_posix()]=t.file_hash(p)
t.write(t.HERE/'evidence_manifest.json',{'created_at':t.now(),'files':manifest,'preserved_partial_diagnostic_json':['Plane418/paths.json','Solid151/paths.json'],'note':'All original evidence, including local diagnostic failures, retained. Cache/temp files are not formal data.'})
checkpoint={'unit':'background_16','state':'finite_batch_complete_primary_only','created_at':t.now(),'stop_reason':'All20 assigned questions assessed and all planned purposeful candidate pairs completed.','assigned_question_ids':t.ASSIGNED,'assessed_question_ids':[r['question_id'] for r in assessed],'unworked_question_ids':[],'counts':{'assigned':20,'assessed':20,'screened_without_design':10,'candidate_designs_saved':10,'candidate_pairs_complete':10,'candidate_calls_completed':20,'original_control_pairs_complete':1,'original_control_calls_completed':2,'all_api_calls_completed':22,'credible_primary_paired_hit_possibilities':1,'api_errors':0,'aborts':0,'retries':0,'live_own_api_processes':0,'unworked':0,'formal_writes':0,'approvals_pass_collect_or_publications':0},'assessments':assessed,'candidate_pair_evidence':candidates,'original_controls':controls,'source_audit':str(t.HERE/'source_preservation_final.json'),'scope_audit':str(t.HERE/'scope_audit.json'),'primary_math_proofs':str(t.HERE/'primary_math_proofs.json'),'binding_audit':str(t.HERE/'evidence_binding_audit.json'),'evidence_manifest':str(t.HERE/'evidence_manifest.json'),'errors_and_aborts':errors,'api_process_final_verification':api_proc,'second_review_queue':str(t.HERE/'second_review_queue.json'),'second_review_required_before_delivery':True,'next_recommendations':['Parent must start a NEW independent second reviewer for Solid197/crease_side_binding before any delivery.','Disclose original450/450 control and absence of incremental-effect evidence.','No unchanged failed/aborted candidate/image/preset may be retested. Preserve all10 design histories and prescreens.','No reservations are released by this worker; report all20 assessed and no unworked IDs to parent.'],'preservation':'Only own runtime/mathvision_special_20261101/background_16 files/caches/temp created. Strict own-root Python audit guard installed before project work; unchanged harness copy runs in that root. Formal library, approvals, state, .env/.runtime/.git and all previous evidence/helpers/global summaries were not written. Concurrent unrelated changes were preserved, with individual MathVision source verification rather than whole-workspace equality.'}
t.write(t.HERE/'checkpoint.json',checkpoint)
report='background_16 finite primary research checkpoint\n\n20/20 assigned questions assessed; no unworked IDs.\n10 saved candidate designs,10 complete pairs/20 candidate calls;1 original control pair/2 calls.\n22 real quicktest3 calls completed,0 API errors,0 aborts,0 retries,0 live own API processes.\n\nOne primary paired-hit possibility: Solid197/crease_side_binding, preset450, finals450/450, formal225. The separate unannotated original control was also450/450: no incremental annotation effect established. No independent second review or delivery performed. Parent must create a NEW reviewer.\n\nAll20 current formal MathVision approvals and noPass/notCollected/noSpecialCompletion rechecked; individual frozen originals and dependencies unchanged. No formal/state/approval/.env/.runtime/.git or old evidence/global helper changes by this worker.\n\nReports: checkpoint.json; second_review_queue.json; primary_math_proofs.json; source_preservation_final.json; evidence_binding_audit.json; errors_and_aborts.json; evidence_manifest.json. Complete manual final bodies and exact raw bindings are included.\n'
(t.HERE/'research_report.txt').write_text(report,encoding='utf-8')
print(t.json.dumps({'state':checkpoint['state'],'counts':checkpoint['counts'],'checkpoint':str(t.HERE/'checkpoint.json'),'second_review_queue':str(t.HERE/'second_review_queue.json')}))
