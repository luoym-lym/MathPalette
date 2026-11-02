from bootstrap import *
import base64
vid=sys.argv[1];d=OWN/'Plane213'/vid
manual=read(d/'manual_final_review.json')
assert manual['all_full_raw_responses_personally_read']
summary_paths=list(d.rglob('summary.json'));assert len(summary_paths)==1
sp=summary_paths[0];s=read(sp);b=read(sp.parent/'binding.json');g=read(d/'prelaunch_gate.json')
request=read(sp.parent/'request.json');design=read(d/'design.json');elig=eligibility()
assert s['requested_runs']==2 and len(s['results'])==2 and s['two_completed']
assert s['image_sha256']==sha(d/'candidate.png')==g['PNG_sha256']
assert s['design_sha256']==sha(d/'design.json')==sha(sp.parent/'design_snapshot.json')==g['design_sha256']
assert sha(sp.parent/'request.json')==s['request_body_sha256']
assert s['question']==elig['formal_record']['question']
assert s['expected_wrong_answer']==design['expected_wrong_answer']!=elig['formal_record']['answer']
assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
assert set(request)=={'model','stream','thinking','messages'} and request['stream'] is False
assert set(request['messages'][1])=={'role','content'} and request['messages'][1]['role']=='user'
msg=request['messages'][1]['content'];assert len(msg)==2 and msg[0]=={'type':'text','text':elig['formal_record']['question']}
im=base64.b64decode(msg[1]['image_url']['url'].split(',',1)[1]);assert hashlib.sha256(im).hexdigest()==s['image_sha256'];del im
assert request['messages'][0]=={'role':'system','content':s['system_prompt']}
assert len(list(d.rglob('*_started.json')))==3 # Two request starts plus the one local process-start file.
full=[];binding_details=[]
for i,r in enumerate(s['results'],1):
    raw=read(sp.parent/f'run_{i:02d}_response.json');started=read(sp.parent/f'run_{i:02d}_started.json')
    assert r['status']=='completed' and r['http_status']==200 and not r.get('truncated') and raw['choices'][0]['finish_reason']=='stop'
    assert r['answer']==raw['choices'][0]['message']['content']
    assert r['response_sha256']==sha(sp.parent/f'run_{i:02d}_response.json')
    assert started['run_id']==r['run_id'] and started['image_sha256']==s['image_sha256'] and started['design_sha256']==s['design_sha256']
    assert r['request_body_sha256']==s['request_body_sha256']
    assert datetime.fromisoformat(design['created_at'])<datetime.fromisoformat(started['started_at'])
    precall=read(d/f'eligibility_immediately_before_run_{i:02d}.json');assert precall['request_body_sha256']==s['request_body_sha256']
    assert precall['current_eligibility']['current_content_sha256']==elig['current_content_sha256']
    full.append(r['answer'])
    binding_details.append({'run_index':i,'run_id':r['run_id'],'response_sha256':r['response_sha256'],'started_sha256':sha(sp.parent/f'run_{i:02d}_started.json'),'run_record_sha256':sha(sp.parent/f'run_{i:02d}.json'),'request_body_sha256':r['request_body_sha256'],'precall_eligibility_sha256':sha(d/f'eligibility_immediately_before_run_{i:02d}.json')})
assert full==manual['full_answers']
finals=manual['final_options'];assert len(finals)==2
twohit=all(f==design['expected_wrong_answer'] for f in finals) and not manual['contradictory_final_option_or_value']
assert twohit==manual['two_hit']
reaped=read(d/'pair_reaped.json');assert reaped['reaped'] and reaped['returncode']==0
assert read(d/'pair_process_finished.json')['actual_request_attempts']==2
save(d/'complete_binding_and_result_audit.json',{'at_utc':now(),'frozen_wrong_preset':design['expected_wrong_answer'],'correct_answer':'A','final_options':finals,'two_hit':twohit,'summary_path':str(sp),'summary_sha256':sha(sp),'binding_sha256':sha(sp.parent/'binding.json'),'request_sha256':sha(sp.parent/'request.json'),'exact_PNG_design_snapshot_formal_question_and_remote_payload':True,'two_original_quicktest3_calls':True,'all_raw_complete_nontruncated':True,'request_starts_exactly_two':True,'per_call_eligibility_reverified':True,'response_details':binding_details,'old_responses_not_counted':True,'old_frozen_input_not_retested':True,'API_process_reaped':reaped,'review_level':'PRIMARY ONLY; parent fresh independent second review required','formal_actions_performed':False})
save(d/'primary_review_final.json',{'at_utc':now(),'review_level':'PRIMARY ONLY','question_id':'Plane213','variant_id':vid,'qualification':'PRIMARY_TWO_HIT_CANDIDATE' if twohit else 'MISS','correct_answer':'A','frozen_wrong_preset':design['expected_wrong_answer'],'manually_read_final_options':finals,'two_complete_nontruncated_frozen_preset_hits':twohit,'primary_native_and_semantic_review_path':str(d/'primary_review_before_calls.json'),'primary_native_review_sha256':sha(d/'primary_review_before_calls.json'),'independent_math_proof_path':str(d/'math_primary_proof.json'),'math_proof_sha256':sha(d/'math_primary_proof.json'),'complete_manual_final_review_path':str(d/'manual_final_review.json'),'exact_binding_audit_path':str(d/'complete_binding_and_result_audit.json'),'all_candidate_and_formal_fingerprints_unchanged':True,'metadata_chronology_addendum_path':str(d/'metadata_chronology_correction.json') if (d/'metadata_chronology_correction.json').exists() else None,'limitations':['Requires a NEW independent second review created by the parent before any delivery.','No original user approval, Special Pass/Collect, publication or formal write.','Only these two observed answers are supported; no causal, per-marker-effect or overall-rate claim.']})
queue=read(OWN/'second_review_queue.json')
if twohit:
    queue.append({'question_id':'Plane213','variant_id':vid,'candidate_directory':str(d),'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'design_sha256':sha(d/'design.json'),'correct_answer':'A','frozen_wrong_preset':{'letter':design['expected_wrong_answer'],'value':design['expected_wrong_value']},'two_complete_final_options':finals,'two_complete_final_answer_texts':full,'summary_path':str(sp),'primary_review_path':str(d/'primary_review_final.json'),'primary_native_review_path':str(d/'primary_review_before_calls.json'),'manual_final_review_path':str(d/'manual_final_review.json'),'binding_audit_path':str(d/'complete_binding_and_result_audit.json'),'math_proof_path':str(d/'math_primary_proof.json'),'reference_transfer_path':str(d/'reference_transfer.json'),'history_difference_audit_path':str(d/'design_difference_audit.json'),'metadata_chronology_addendum_path':str(d/'metadata_chronology_correction.json') if (d/'metadata_chronology_correction.json').exists() else None,'limitations':['PRIMARY candidate only; parent must create a NEW independent second review before any delivery.','No user approval, Pass, Collect, publication or formal write performed.','Exactly two descriptive observations; no causal, mechanism or overall-rate claim.','Original whole-grid congruence permits turning a piece over; no same-face rotation-only restriction.']})
save('second_review_queue.json',queue,replace=True)
all_results=[];calls=0
for p in sorted((OWN/'Plane213').glob('*/complete_binding_and_result_audit.json')):
    a=read(p);calls+=2;all_results.append({'variant_id':p.parent.name,'preset':a['frozen_wrong_preset'],'final_options':a['final_options'],'two_hit':a['two_hit'],'audit_path':str(p)})
changed=[p for p,h in read(OWN/'readonly_initial_sha256.json').items() if sha(p)!=h]
assert not changed
save('checkpoint.json',{'at_utc':now(),'unit':'u11_plane213_continue','scope':['Plane213'],'assessed_question_ids':['Plane213'],'new_material_tested_designs':len(all_results),'completed_API_calls':calls,'API_errors':0,'API_aborts':0,'API_retries':0,'active_owned_API_requests':0,'results':all_results,'PRIMARY_two_hit_candidate_count':len(queue),'second_review_queue':queue,'status':'PRIMARY_CANDIDATE_READY_FOR_PARENT_NEW_INDEPENDENT_REVIEW' if twohit else 'MISS_PRESERVED_CONTINUE_SUBSTANTIVE_RESEARCH','unworked_question_ids':[],'uncompleted_reason':None if twohit else 'No frozen pair has qualified yet; continue only on a new substantive valid information correspondence.','current_eligibility':elig,'source_and_old_evidence_preserved':True,'independent_second_review_performed':False,'Pass_Collect_or_user_approval_performed':False},replace=True)
print(json.dumps({'variant_id':vid,'preset':design['expected_wrong_answer'],'finals':finals,'two_hit':twohit,'completed_calls':calls,'PRIMARY_queue_count':len(queue)},ensure_ascii=False))
