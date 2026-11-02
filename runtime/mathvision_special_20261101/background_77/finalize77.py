from audit77 import *
from publish_batch import verify_evidence
src=HERE/QID/VARIANT
summary,record,sp=verify_evidence(src)
assert summary['requested_runs']==len(summary['results'])==2 and summary['two_completed']
assert str(summary['expected_wrong_answer'])=='D' and record['answer']=='C'
assert sha(src/'design.json')==summary['design_sha256']
assert sha(sp.parent/'request.json')==summary['request_body_sha256']
for i,a in enumerate(summary['results'],1):
    raw=read(sp.parent/f'run_{i:02d}_response.json');body=raw if 'choices' in raw else raw['response']
    assert body['choices'][0]['message']['content']==a['answer']
    assert a['answer'].rstrip().endswith(('B:75','B: 75','**B: 75**.','**B: 75**')) or 'B: 75' in a['answer'][-250:]
finished=read(HERE/'process_finished.json');assert finished['returncode']==0 and finished['process_wait_returned']
provenance=read(src/'reuse_provenance.json')
for name,h in provenance['frozen_source_and_copy_sha256'].items():assert sha(SOURCE/name)==sha(src/name)==h
for rel,h in provenance['old74_hashes_before_parent_testing'].items():assert sha(BASE/'background_74'/rel)==h
current=eligibility();assert current['eligible'] and current['current_content_sha256']==provenance['fresh_eligibility']['current_content_sha256']
write('manual_full_final_review.json',{'reviewed_at':now(),'question_id':QID,'frozen_preset':'D=192','correct_answer':'C=151','full_complete_answers_read':True,'final_answers':['B=75','B=75'],'target_hits':[False,False],'doublehit':False,'narrative_limit':'Run1wronghoof64thenclosest75;run2invalidarcsin integral thenabout61closest75. IncidentalD in hypothetical radius8 case is NOT the final answer. No posthoc relabel toB.','evidence':str(sp),'new_designs':0,'independent_review_required_only_if_future_newcandidate':True})
checkpoint={'unit':'background_77','stage':'parent_local_import_repair_then_original_frozen_FIRSTpair','status':'completed_pair_preset_miss','completed_at':now(),'question_ids':[QID],'actual_assessed_question_ids':[QID],'unworked_question_ids':[],'new_design_count':0,'new_mechanism_count':0,'reused_frozen_drafts_first_test':1,'variant_id':VARIANT,'original_created_at':read(src/'design.json')['created_at'],'expected_wrong_answer':'D','correct_answer':'C','manual_finals':['B','B'],'actual_API_calls':2,'completed_calls':2,'complete_pairs':1,'preset_hits':0,'credible_primary_doublehits':0,'API_errors':0,'aborts':0,'retries':0,'third_calls':0,'controls':0,'exact_PNG_design_plugin_bytes_preserved':True,'fresh_approval_current':True,'old57_and74_hashes_current_exact':True,'root_math_and_native_mark_review':str(HERE/'primary_parent_review.json'),'fresh_schema_and_replay':str(HERE/'offline/replay_verification.json'),'global_prior_call_scan':str(HERE/'global_prior_invocation_scan.json'),'reuse_provenance':str(src/'reuse_provenance.json'),'summary':str(sp),'manual_full_finals':str(HERE/'manual_full_final_review.json'),'local_import_error_fix_record':str(HERE/'repair_scope.json'),'old74_HOLD_and_failure_logs_untouched':True,'all_owned_API_processes_closed':True,'process_closure':finished,'all_new_files_only':str(HERE),'no_formal_approval_Pass_Collect_delivery_or_self_independent_review':True}
write('checkpoint.json',checkpoint)
write('second_review_queue.json',{'unit':'background_77','created_at':now(),'candidates':[],'count':0,'reason':'Both finalB75miss frozenD192. No candidate, no newmechanism, no retest.'})
write('closing_evidence_manifest.json',{'created_at':now(),'files_sha256':{str(p.relative_to(HERE)):sha(p) for p in HERE.rglob('*') if p.is_file()},'source_and_old_inputs_preserved':True,'actual_calls':2,'preset_hits':0,'own_API_closed':True})
print(json.dumps({'question_id':QID,'frozen_preset':'D','finals':['B','B'],'doublehit':False,'actual_calls':2,'closed':True,'old74_HOLD_untouched':True}))
