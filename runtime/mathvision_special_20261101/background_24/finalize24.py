from tools24 import *
import base64
from html.parser import HTMLParser
def rel(p):return str(Path(p).relative_to(ROOT))
def bindings(out):
    d=read(out/'design.json');ev=next((out/'tests').glob('quicktest3_*'));b=read(ev/'binding.json');req=read(ev/'request.json');summary=read(ev/'summary.json');manual=read(out/'manual_final_review.json')
    record=eligibility(d['question_id'])['formal_record'];image=(out/'candidate.png').read_bytes();snap=read(ev/'design_snapshot.json')
    assert d==snap and b['design_sha256']==file_hash(out/'design.json')==file_hash(ev/'design_snapshot.json')
    assert b['image_sha256']==file_hash(out/'candidate.png') and b['pixel_sha256']==pixel_hash(image)
    assert b['question']==record['question'] and b['expected_wrong_answer']==d['expected_wrong_answer']
    assert b['question_record_sha256']==canonical_hash(record)
    assert b['request_body_sha256']==file_hash(ev/'request.json') and req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'}
    assert set(req)=={'model','stream','thinking','messages'} and req['stream'] is False
    assert req['messages'][0]=={'role':'system','content':b['system_prompt']}
    assert req['messages'][1]['role']=='user' and len(req['messages'][1]['content'])==2
    assert req['messages'][1]['content'][0]=={'type':'text','text':record['question']}
    assert base64.b64decode(req['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==image
    assert summary['two_completed'] and len(summary['results'])==2 and len(list(ev.glob('run_*_response.json')))==2
    for i,r in enumerate(manual['runs'],1):
        raw=ev/f'run_{i:02d}_response.json';job=read(ev/f'run_{i:02d}.json');rr=read(raw)
        assert r['complete_final_text']==rr['choices'][0]['message']['content'] and r['raw_response_sha256']==file_hash(raw)==job['response_sha256']
        assert rr['choices'][0]['finish_reason']=='stop' and job['status']=='completed'
        assert job['image_sha256']==b['image_sha256'] and job['design_sha256']==b['design_sha256'] and job['request_body_sha256']==b['request_body_sha256']
    assert read(out/'api_process_finished.json')['two_completed']
    return {'question_id':d['question_id'],'variant_id':d['variant_id'],'candidate_directory':rel(out),'design_path':rel(out/'design.json'),'png_path':rel(out/'candidate.png'),'png_sha256':b['image_sha256'],'pixel_sha256':b['pixel_sha256'],'design_sha256':b['design_sha256'],'expected_wrong_answer':d['expected_wrong_answer'],'manual_final_answers':manual['manual_final_answers'],'correct_answer':d['correct_answer'],'two_predeclared_target_hits':manual['two_predeclared_target_hits'],'exact_request_path':rel(ev/'request.json'),'raw_binding_path':rel(ev/'binding.json'),'request_body_sha256':b['request_body_sha256'],'full_frozen_binding':b,'complete_manual_review':manual,'raw_response_paths':[rel(ev/f'run_{i:02d}_response.json') for i in [1,2]],'all_frozen_request_design_image_raw_final_bindings_verified':True,'difference_audit':read(out/'design_difference_audit.json'),'primary_review':read(out/'primary_review.json'),'render_check_path':rel(out/'render_check.json'),'math_proof_path':rel(out.parent/'primary_math_audit.json'),'path_fingerprints_path':rel(out/'path_fingerprints.json')}
current={q:eligibility(q) for q in ASSIGNED};assert all(v['eligible'] for v in current.values())
old_changes=[];old_count=0;old_source_hash_comparisons=[]
for q in ASSIGNED:
    inv=read(HERE/q/'prior_history_inventory.json')
    for p,h in inv['all_same_question_file_hashes'].items():
        old_count+=1;actual=file_hash(ROOT/p) if (ROOT/p).exists() else None
        if actual!=h:old_changes.append({'path':p,'before':h,'after':actual})
assert not old_changes,old_changes
source_changes=[];source_files={};metadata=[]
for q in ASSIGNED:
    start=read(HERE/q/'eligibility_start.json');before=read(HERE/q/'input_fingerprints.json')
    for p,h in before['files'].items():
        actual=file_hash(ROOT/p);source_files[p]={'before':h,'current':actual}
        if actual!=h:
            source_changes.append({'path':p,'before':h,'current':actual,'classification':'shared_authoritative_aggregate_external_drift' if p in ['PlaneGeometry/dataset.jsonl','provenance/approvals.json'] else 'FROZEN_SOURCE_DRIFT'})
    for p,h in start['diagnostic_runtime_metadata_hashes'].items():
        actual=file_hash(ROOT/p);metadata.append({'question_id':q,'path':p,'old':h,'current':actual,'changed':actual!=h,'classification':'mutable_runtime_progress_diagnostic_only_not_a_frozen_source','historical_snapshot_untouched':True})
    write(HERE/q/'eligibility_end.json',current[q])
assert not [v for v in source_changes if v['classification']=='FROZEN_SOURCE_DRIFT']
processes=read(HERE/'api_process_exit_audit.json');assert processes['live_own_api_processes']==0
all_designs=sorted(HERE.glob('Plane*/r24_*/design.json'));tested=[p.parent for p in all_designs if (p.parent/'api_process_finished.json').exists()]
audits=[bindings(p) for p in tested];assert len(audits)==5
queued=[a for a in audits if a['two_predeclared_target_hits']];assert [a['question_id'] for a in queued]==['Plane242']
write(HERE/'evidence_binding_audit.json',{'stage':'material_refinement','checked_at':now(),'assessed_question_ids':ASSIGNED,'new_tested_candidate_count':len(audits),'actual_completed_calls':10,'all_request_bindings_verified':True,'candidates':audits,'live_own_api_processes':0,'retries':0,'aborts':0,'errors':0})
write(HERE/'source_preservation_audit.json',{'stage':'material_refinement','checked_at':now(),'current_eligibility':current,'all8_still_eligible_and_approved':True,'fresh_noop_formal_pixel_matches':8,'frozen_source_files_checked':source_files,'observed_source_hash_changes':source_changes,'prior_runtime_evidence_file_count':old_count,'prior_runtime_evidence_changes':old_changes,'mutable_progress_drift':metadata,'no_claim_that_entire_workspace_is_unchanged':True,'external_unrelated_workbench_changes':'Preserved. No restore, state edit, checkout or cleanup performed. Only task-root writes were permitted by Python own-directory guard.','all_write_paths_under':str(HERE),'formal_library_approval_state_pass_collect_publication_API_actions':False,'unchanged_shared_harness_sha256':file_hash(BASE/'harness/quicktest3_isolated.py'),'unchanged_own_harness_copy_sha256':file_hash(HERE/'harness/quicktest3_isolated.py')})
write(HERE/'failures_and_aborts.json',{'stage':'material_refinement','API_errors':[],'API_aborts':[],'API_retries':0,'live_own_API_processes':0,'untested_rejections':[{'question_id':'Plane225','variant_id':'r24_original_animal_heading_retention','reason':'p0 selected accessory ears/fins rather than intended main asymmetric bodies; native visual rejection before calls. Preserved and replaced with a distinct variant targeting actual14segment bodypaths; no palette/width/preset swap.','evidence':rel(HERE/'Plane225/r24_original_animal_heading_retention/primary_review.json')}],'local_pre_API_implementation_failures':[{'script':rel(HERE/'tiling24.py'),'initial_error':'ValueError: Both input arrays must be (arrays of) 3-dimensional vectors, but they are 2 and 2 dimensional instead.','cause':'NumPy2.5 cross no longer accepts2D vectors.','fix':'Use explicit2D determinant a0*b1-a1*b0.','scope':'Primary geometry proof implementation only; no rendering or solver evidence existed for Plane248 when fixed.','API_calls_affected':0}],'failed_pairs':[{'question_id':a['question_id'],'variant_id':a['variant_id'],'preset':a['expected_wrong_answer'],'manual_finals':a['manual_final_answers']} for a in audits if not a['two_predeclared_target_hits']]})
queue={'stage':'material_refinement','created_at':now(),'candidate_count':len(queued),'question_ids':[a['question_id'] for a in queued],'actual_assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'candidates':queued,'required_next_action':'Parent must create a NEW independent second-review task for each queued exact variant. Primary author has not independently second-reviewed or delivered anything.','approval_status':'UNREVIEWED; no Pass/Collect/publication','controls':'No new originalcontrols; none found for these assigned IDs in prior same-question evidence. No causal attribution.','source_preservation_audit':rel(HERE/'source_preservation_audit.json')}
write(HERE/'second_review_queue.json',queue)
design_summaries=[]
for p in all_designs:
    out=p.parent;d=read(p);r=read(out/'primary_review.json')
    design_summaries.append({'question_id':d['question_id'],'variant_id':d['variant_id'],'directory':rel(out),'expected_wrong_answer':d['expected_wrong_answer'],'difference':read(out/'design_difference_audit.json'),'primary_review_status':r.get('status','PRIMARY_VISUAL_MATH_PRECHECK_PASSED'),'tested':out in tested,'completed_calls':2 if out in tested else 0})
write(HERE/'checkpoint.json',{'unit':'background_24','stage':'material_refinement','finished_at':now(),'status':'FINITE_COMPLETE','stop_reason':'All8 assigned completed questions assessed with reasonable materially different hypotheses; no unworked assignment remains.','assigned_question_ids':ASSIGNED,'actual_assessed_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'screened_without_new_design':['Plane220','Plane231','Plane301'],'new_design_records':len(all_designs),'untested_native_visual_rejected_designs':1,'complete_candidate_pairs':len(audits),'actual_completed_API_calls':10,'original_control_calls':0,'API_errors':0,'aborted_calls':0,'automatic_retries':0,'credible_primary_candidates':len(queued),'credible_question_ids':[a['question_id'] for a in queued],'independent_second_review_completed':False,'all_eventual_deliveries_require_parent_NEW_second_review':True,'new_designs':design_summaries,'assessments':[read(HERE/q/'refinement_assessment.json') for q in ASSIGNED],'manual_final_reviews':[a['complete_manual_review'] for a in audits],'evidence_binding_audit':rel(HERE/'evidence_binding_audit.json'),'source_current_eligibility_audit':rel(HERE/'source_preservation_audit.json'),'failures_aborts':rel(HERE/'failures_and_aborts.json'),'process_exit_audit':rel(HERE/'api_process_exit_audit.json'),'second_review_queue':rel(HERE/'second_review_queue.json'),'all_own_API_processes_ended':True,'files_scope':str(HERE),'formal_state_and_historical_evidence_modified':False,'limits':'Two observations per frozen PNG; no statistical, human or per-marker causal inference. Narratives differ and contain errors. No controls repeated. Entire workspace immutability is not claimed; unrelated concurrent changes preserved.'})
print(json.dumps({'assessed':8,'new_designs':len(all_designs),'pairs':len(audits),'completed_calls':10,'credible':[a['question_id'] for a in queued],'old_evidence_files_unchanged':old_count,'frozen_source_changes':source_changes,'live_own_API':0,'checkpoint':str(HERE/'checkpoint.json'),'queue':str(HERE/'second_review_queue.json')},ensure_ascii=False))
