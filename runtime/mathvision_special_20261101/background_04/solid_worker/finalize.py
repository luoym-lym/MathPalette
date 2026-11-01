from tools_local import *
import base64
def sha(data):return hashlib.sha256(data).hexdigest()
manual={
 ('Solid170','opposite_to_adjacent_hole_pairs'):{'finals':['D','A'],'notes':['Run1 explicitly concludes Correct Answer D. Its own option geometry descriptions are wrong, but no final A.','Run2 explicitly concludes Option A and ends A; target hit.']},
 ('Solid188','diagonal_feature_correspondence'):{'finals':['A','C'],'notes':['Run1 explicitly concludes Net A and Answer A; target hit.','Run2 rejects A, concludes Net C, and ends correct choice C; target miss. It names green/red/blue but invents common-vertex incidence.']}
}
audits=[];attempts=[]
for (qid,vid),m in manual.items():
    folder=TASK/qid/vid;design_path=folder/'design.json';design=json.loads(design_path.read_text(encoding='utf-8'));image_path=folder/'candidate.png'
    invocation=next((folder/'tests').iterdir());binding=json.loads((invocation/'binding.json').read_text(encoding='utf-8'));request_bytes=(invocation/'request.json').read_bytes();payload=json.loads(request_bytes)
    expected_payload_keys={'model','stream','thinking','messages'}
    assert set(payload)==expected_payload_keys and payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    assert len(payload['messages'])==2 and payload['messages'][0]=={'role':'system','content':binding['system_prompt']}
    content=payload['messages'][1]['content'];assert payload['messages'][1]['role']=='user' and len(content)==2
    assert content[0]=={'type':'text','text':AD.records[qid]['question']}
    assert content[1]['type']=='image_url' and set(content[1])=={'type','image_url'}
    encoded=content[1]['image_url']['url'];assert encoded.startswith('data:image/png;base64,')
    assert base64.b64decode(encoded.split(',',1)[1])==image_path.read_bytes()
    assert binding['image_sha256']==file_hash(image_path) and binding['design_sha256']==file_hash(design_path)
    assert binding['request_body_sha256']==sha(request_bytes)
    assert binding['expected_wrong_answer']==design['expected_wrong_answer']=='A'
    assert (invocation/'design_snapshot.json').read_bytes()==design_path.read_bytes()
    runs=[]
    for i,final in enumerate(m['finals'],1):
        path=invocation/f'run_{i:02d}.json';raw_path=invocation/f'run_{i:02d}_response.json';job=json.loads(path.read_text(encoding='utf-8'))
        assert job['status']=='completed' and job['finish_reason']=='stop' and job['truncated'] is False
        assert job['response_sha256']==file_hash(raw_path)
        assert job['request_body_sha256']==binding['request_body_sha256'] and job['image_sha256']==binding['image_sha256'] and job['design_sha256']==binding['design_sha256']
        runs.append({'run':i,'full_final_answer_manually_read':True,'manual_final_answer':final,'target_hit':final=='A','manual_note':m['notes'][i-1],'answer_text':job['answer'],'job_path':str(path.relative_to(ROOT)),'raw_response_path':str(raw_path.relative_to(ROOT)),'finish_reason':job['finish_reason'],'elapsed_seconds':job['elapsed_seconds']})
    result={'question_id':qid,'variant_id':vid,'expected_wrong_answer':'A','formal_answer':AD.records[qid]['answer'],'runs':runs,'hits':sum(r['target_hit'] for r in runs),'two_completed':True,'decision':'reject_target_not_reached','controls':[],'independent_second_review':'Not requested: candidate failed immutable two-hit gate.','image_sha256':binding['image_sha256'],'design_sha256':binding['design_sha256'],'binding_path':str((invocation/'binding.json').relative_to(ROOT)),'primary_review_path':str((folder/'primary_review_before_calls.json').relative_to(ROOT)),'marker_roles':design['marker_roles'],'mathematical_proof':design['mathematical_proof'],'evidence_paths':sorted(str(p.relative_to(ROOT)) for p in folder.rglob('*') if p.is_file())}
    write(folder/'manual_results.json',result);attempts.append(result)
    audits.append({'question_id':qid,'variant_id':vid,'image_design_snapshot_request_response_bindings_all_match':True,'request_has_only_formal_question_candidate_image_and_existing_system':True,'standard_quicktest3_model_thinking_no_profile_or_timeout_overrides':True,'predeclared_preset_unchanged':True,'two_independent_complete_responses':True,'same_frozen_png_both_calls':True,'no_retries':True,'request_body_sha256':binding['request_body_sha256'],'image_sha256':binding['image_sha256'],'design_sha256':binding['design_sha256'],'evidence_dir':str(invocation.relative_to(ROOT))})
integrity=[]
for qid in ASSIGNED:
    folder=TASK/qid;before=json.loads((folder/'frozen_inputs.json').read_text(encoding='utf-8'));after=AD.frozen_inputs(qid)
    assert before==after
    eligibility_before=json.loads((folder/'eligibility_at_start.json').read_text(encoding='utf-8'));current=eligibility(qid)
    assert current['eligible']
    integrity.append({'question_id':qid,'fresh_at_start':eligibility_before,'still_eligible_at_finish':current,'frozen_inputs_unchanged':True,'frozen_input_snapshot':str((folder/'frozen_inputs.json').relative_to(ROOT)),'all_file_hashes_rechecked':before['files'],'formal_record_unchanged':True,'source_image_scene_projection_visibility_labels_fills_preserved':True,'runtime_original_png_bytes_match_formal':(folder/'original.png').read_bytes()==AD.original_paths[qid].read_bytes()})
write(TASK/'evidence_binding_audit.json',{'all_pass':True,'invocations':audits})
write(TASK/'source_integrity_verification.json',{'all_frozen_inputs_unchanged':True,'questions':integrity,'scope':'Own assessed question files and shared renderer/protocol/schema/config inputs. Root performs whole-workspace prior-evidence audit.'})
prescreens=json.loads((TASK/'prescreen_summary.json').read_text(encoding='utf-8'))
process=json.loads((TASK/'no_live_processes.json').read_text(encoding='utf-8-sig'));assert process['no_live_own_processes']
queue={'created_at':datetime.now(timezone.utc).isoformat(),'candidate_count':0,'candidates':[],'reason':'Both new tested variants have only one immutable target hit out of two complete calls; no candidate qualifies for parent independent review.','no_independent_second_review_claimed':True,'no_delivery_or_Pass_Collect':True}
write(TASK/'second_review_queue.json',queue)
checkpoint={'created_at':datetime.now(timezone.utc).isoformat(),'status':'FINITE_SOLID_WORKER_COMPLETE','stop_reason':'Eight assigned questions assessed. Two purposeful feature-correspondence designs each failed the immutable two-hit gate; six others failed primary legal mechanism/readability screening. No repeat identical-image calls or speculative retries.','all_outputs_under':str(TASK.relative_to(ROOT)),'assigned_question_ids':ASSIGNED,'assessed_question_count':8,'assessed_question_ids':ASSIGNED,'prescreen_only_question_count':6,'prescreens':prescreens['details'],'new_candidate_design_count':2,'tested_question_count':2,'two_complete_call_candidates':2,'completed_calls':4,'failed_calls':0,'aborted_calls':0,'original_control_calls':0,'credible_two_hit_candidates':0,'second_review_queue':str((TASK/'second_review_queue.json').relative_to(ROOT)),'attempts':attempts,'primary_mathematical_visual_marker_reviews_only':True,'independent_second_reviews':0,'new_qualified_deliveries':0,'all_binding_checks_pass':True,'evidence_audit':str((TASK/'evidence_binding_audit.json').relative_to(ROOT)),'source_integrity_verification':str((TASK/'source_integrity_verification.json').relative_to(ROOT)),'formal_library_workbench_env_protocol_approval_recipe_index_changes':False,'previous_exploration_evidence_mutations':False,'Pass_Collect_review_APIs_used':False,'no_live_process_confirmation':process,'native_subagents_started':0,'pending_or_untested_candidates':[],'next_recommendations':['Do not retest either failed identical PNG or combine their individual A hits.','Solid188 local slash matching fails to enforce the triangular endpoint graph; future new questions should bind a measurable or topological feature with fewer projection assumptions.','No reviewed/qualified delivery should be packaged from this worker.'],'chronology_disclosure':str((TASK/'Solid188/diagonal_feature_correspondence/review_chronology_disclosure.json').relative_to(ROOT))}
write(TASK/'checkpoint.json',checkpoint)
print(json.dumps({'assessed':8,'tested_designs':2,'complete_calls':4,'credible_two_hit':0,'all_binding_checks_pass':True,'frozen_inputs_unchanged':True,'no_live_processes':True,'checkpoint':str(TASK/'checkpoint.json')}))
