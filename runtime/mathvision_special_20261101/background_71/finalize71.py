from env71 import *
import base64
import gc
import importlib.util

c=read(OWN/'prepared_candidates.json')[0]
dest=Path(c['path'])
tests=list((dest/'tests').glob('quicktest3_*'))
assert len(tests)==1
test=tests[0]
binding=read(test/'binding.json')
summary=read(test/'summary.json')
assert summary['two_completed'] and binding['requested_runs']==2
assert sha(dest/'candidate.png')==c['image_sha256']==binding['image_sha256']
assert sha(dest/'design.json')==c['design_sha256']==binding['design_sha256']
assert (test/'design_snapshot.json').read_bytes()==(dest/'design.json').read_bytes()
assert sha(test/'request.json')==binding['request_body_sha256']
payload=read(test/'request.json')
rec=read(OWN/'Solid120/formal_record.json')
assert set(payload)=={'model','stream','thinking','messages'}
assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
assert len(payload['messages'])==2
assert payload['messages'][0]=={'role':'system','content':binding['system_prompt']}
parts=payload['messages'][1]['content']
assert len(parts)==2 and parts[0]=={'type':'text','text':rec['question']} and parts[1]['type']=='image_url'
image=base64.b64decode(parts[1]['image_url']['url'].split(',',1)[1],validate=True)
assert image==(dest/'candidate.png').read_bytes()
del image,parts,payload
gc.collect()

manual_finals=['37','43']
manual_reasons=[
    'Full final body manually read: explicitly ends Answer:37. It treats the top row as continuing immediately after32 and miscounts the target as the fifth tick. No final50; preset miss.',
    'Full final body manually read: explicitly ends43. It correctly computes period21 but then mislocates the question above22 instead of27. No final50; preset miss.'
]
runs=[]
for index,(final,reason) in enumerate(zip(manual_finals,manual_reasons),1):
    rawpath=test/f'run_{index:02d}_response.json'
    job=read(test/f'run_{index:02d}.json')
    started=read(test/f'run_{index:02d}_started.json')
    raw=read(rawpath)
    assert len(raw['choices'])==1 and raw['choices'][0]['finish_reason']=='stop'
    assert job['status']=='completed' and sha(rawpath)==job['response_sha256']
    for field in ('image_sha256','design_sha256','request_body_sha256'):
        assert started[field]==job[field]==binding[field]
    body=raw['choices'][0]['message']['content']
    assert body==job['answer']
    runs.append({'run':index,'manual_final_answer':final,'preset_hit':False,'consistent_numeric_final':True,'complete_final_manually_read':True,'complete_final_body':body,'manual_reason':reason,'finish_reason':'stop','raw_path':str(rawpath),'raw_sha256':sha(rawpath),'job_sha256':sha(test/f'run_{index:02d}.json'),'started_sha256':sha(test/f'run_{index:02d}_started.json'),'same_frozen_request_image_design':True})
    del raw,job,started,body
    gc.collect()
assert len(list(test.glob('run_*_started.json')))==2
assert len(list(test.glob('run_*_response.json')))==2
review={'at':now(),'question_id':'Solid120','variant_id':c['variant_id'],'expected_wrong_answer':'50','formal_correct_answer':'48','manual_finals':manual_finals,'runs':runs,'status':'complete_pair_missed_unchanged_preset','preset_hits':0,'credible_primary_doublehit':False,'new_API_calls':2,'completed_calls':2,'retries':0,'third_calls':0,'errors':[],'aborts':[],'binding_hash_exact':True,'only_formal_question_plus_same_frozen_PNG_sent':True,'correct_answer_preset_intent_history_params_not_sent':True,'max_tokens_or_timeout_override':False,'new_original_controls':0,'limits':['Both results are wrong relative to48 but neither equals50; this remains a miss.','No causal improvement, model success rate or mechanism confirmation inferred from this pair.','Primary researcher only; no independent review/approval/delivery.']}
save(dest/'manual_final_review.json',review)
save(dest/'request_binding_audit.json',{'at':now(),'binding_sha256':sha(test/'binding.json'),'request_sha256':sha(test/'request.json'),'design_snapshot_sha256':sha(test/'design_snapshot.json'),'formal_question_exact':True,'embedded_PNG_exact':True,'profile':'quicktest3','model':'mimo-v2.6-flash','thinking':{'type':'disabled'},'existing_system_prompt_exact':True,'two_complete_stop_finals':True,'no_extra_started_call':True,'no_tokens_timeout_profile_override':True})

# Immutable original/source/evidence hashes. Parent runtime metadata is diagnostic.
frozen=[]
metadata=[]
mutable_names={'continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','master_progress.json'}
initial=read(OWN/'readonly_hashes_start.json')
for rel,expected in initial.items():
    path=PROJECT/rel
    if path.name in mutable_names: continue
    actual=sha(path)
    frozen.append({'path':rel,'expected':expected,'actual':actual,'unchanged':actual==expected})
for item in read(OWN/'old_evidence_full_byte_read.json'):
    path=PROJECT/item['path']
    actual=sha(path)
    frozen.append({'path':item['path'],'expected':item['sha256'],'actual':actual,'unchanged':actual==item['sha256']})
assert all(i['unchanged'] for i in frozen)
for snap in read(OWN/'readin_snapshots.json'):
    if not snap['mutable_parent_metadata']: continue
    path=PROJECT/snap['path']
    original=Path(snap['snapshot']).read_bytes()
    assert hashlib.sha256(original).hexdigest()==snap['sha256']
    current=path.read_bytes()
    end=OWN/'parent_metadata_end_snapshots'/path.name
    end.parent.mkdir(parents=True,exist_ok=True)
    end.write_bytes(current)
    metadata.append({'path':str(path),'original_snapshot':snap['snapshot'],'original_sha256':snap['sha256'],'current_full_snapshot':str(end),'current_sha256':hashlib.sha256(current).hexdigest(),'unchanged':current==original,'exact_original_byte_prefix':current.startswith(original),'append_bytes':len(current)-len(original) if current.startswith(original) else None,'classification':'unchanged' if current==original else 'parent_exact_prefix_append_diagnostic' if current.startswith(original) else 'parent_metadata_update_diagnostic','old_snapshot_restored_or_rewritten':False})
    del original,current
    gc.collect()
save('source_and_old_evidence_preservation_final.json',{'at':now(),'frozen_checks':frozen,'frozen_changed':[],'parent_metadata_diagnostics':metadata,'old_metadata_original_snapshots_preserved':True})

assessments=[]
for q in QIDS:
    e=eligibility(q)
    assert e['eligible'] and e['approval_matches']
    save(f'{q}/eligibility_final.json',e)
    if q=='Solid120':
        assessments.append({'question_id':q,'status':'MISS','variant_id':c['variant_id'],'new_calls':2,'predeclared_wrong_answer':'50','manual_finals':manual_finals,'primary_doublehit':False,'manual_review':str(dest/'manual_final_review.json'),'difference_audit':str(dest/'design_difference_audit.json')})
    else:
        assessment=read(OWN/q/'design_difference_audit.json')
        assessments.append({'question_id':q,'status':'reasoned_skip_no_clean_distinct_design','new_designs':0,'new_calls':0,'unworked':False,'reason':assessment['reason'],'difference_audit':str(OWN/q/'design_difference_audit.json')})
    del e
    gc.collect()
closure=read(OWN/'process_closure_audit.json')
assert closure['own_live_requests']==0 and not closure['recorded_API_PID_still_exists'] and not closure['live_own_python_processes']
save('errors_and_incompletes.json',{'local_failures':[],'API_errors':[],'incomplete_responses':[],'aborts':[],'stalled_process_terminations':[],'retries':0,'manual_note':'One completed pair only; no retries/retests/third calls/controls. No source62/63 images were called.'})
save('second_review_queue.json',{'unit':'background_71','at':now(),'primary_candidates':[],'queue':[],'count':0,'reason':'Only new pair37/43 misses the frozen50 preset; other four have reasoned skips. No old scoped pair qualifies under its own preset.','new_independent_review_by_parent_required_before_any_delivery':True,'self_independent_reviews':0,'approvals_Pass_Collect_delivery_actions':0})
save('checkpoint.json',{'unit':'background_71','stage':'material_refinement','status':'finite_scope_assessed_complete','finished_at':now(),'scope':QIDS,'actual_assessed_question_ids':QIDS,'unworked_question_ids':[],'stop_reason':'All exact5 have source/currentapproval/math/native/history assessment and first pair or reasoned skip. No quota-thrift stop.','inherited_Codex_configuration':'unchanged; no provider/model/options override','new_design_count':1,'new_API_attempts':2,'completed_calls':2,'preset_hit_calls':0,'credible_primary_doublehits':0,'reasoned_skips':4,'holds':[],'errors':[],'incompletes':[],'aborts':[],'retries':0,'third_calls':0,'new_original_control_calls':0,'own_live_requests':0,'process_closure':str(OWN/'process_closure_audit.json'),'question_assessments':assessments,'second_review_queue':str(OWN/'second_review_queue.json'),'old_full_raw_and_image_audit':str(OWN/'old_evidence_full_byte_read.json'),'old_manual_outcomes':str(OWN/'old_history_manual_outcomes.json'),'new_image_zero_prior_call_hash_audit':str(OWN/'new_image_prior_call_hash_audit.json'),'source_preservation':str(OWN/'source_and_old_evidence_preservation_final.json'),'no_independent_review_approval_Pass_Collect_publication_delivery_formal_edits':True,'all_new_files_and_process_TEMP_cache_output_exclusively_OWNROOT':str(OWN),'no_nested_agents_threads_worktrees_servers':True,'limitations':['Known filesystem request/PNG evidence cannot rule out undisclosed external calls.','Reasoned skips are finite design assessments, not impossibility proofs.','New pair is wrong twice but misses its own preset; no promotion or relabelling.']})
print('FINAL: exact5 assessed;120 pair37/43 vs frozen50 MISS;4 reasoned skips;0 doublehits;0 live requests.',flush=True)
