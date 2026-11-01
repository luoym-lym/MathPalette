from tools_b import *
import base64,subprocess
from quick_test import SYSTEM_PROMPT
qid='Plane223';vid='large_spot_ring_correspondence';out=HERE/qid/vid
finals=sys.argv[1:]
before=json.loads((HERE/'extension_before_calls.json').read_text(encoding='utf-8'))
design=json.loads((out/'design.json').read_text(encoding='utf-8'));render=json.loads((out/'render_check.json').read_text(encoding='utf-8'))
assert design['expected_wrong_answer']=='C'
hashes={name:file_hash(out/name) for name in before['frozen_existing_hashes']}
assert hashes==before['frozen_existing_hashes']
previous_differences=[p for p,h in before['original_primary_evidence_hashes'].items() if not(HERE/p).exists() or file_hash(HERE/p)!=h]
assert not previous_differences,previous_differences
evidence_dirs=list((out/'tests').glob('quicktest3_*'));assert len(evidence_dirs)==1
evidence=evidence_dirs[0];summary=json.loads((evidence/'summary.json').read_text(encoding='utf-8'));binding=json.loads((evidence/'binding.json').read_text(encoding='utf-8'))
assert binding['image_sha256']==hashes['candidate.png'] and binding['design_sha256']==hashes['design.json'] and binding['expected_wrong_answer']=='C'
assert (evidence/'design_snapshot.json').read_bytes()==(out/'design.json').read_bytes()
request_bytes=(evidence/'request.json').read_bytes();payload=json.loads(request_bytes)
cfg,ad=adapter();formal=ad.records[qid]
assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
assert set(payload)=={'model','stream','thinking','messages'} and len(payload['messages'])==2
assert payload['messages'][0]=={'role':'system','content':SYSTEM_PROMPT}
assert payload['messages'][1]['content'][0]=={'type':'text','text':formal['question']}
assert len(payload['messages'][1]['content'])==2
assert base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(out/'candidate.png').read_bytes()
assert hashlib.sha256(request_bytes).hexdigest()==binding['request_body_sha256']
completed=[r for r in summary['results'] if r['status']=='completed']
assert len(finals)==len(completed),'Manually supply one reviewed final for every completed response.'
manual=[];index=0
for result in summary['results']:
    selected=None
    if result['status']=='completed':
        selected=finals[index];index+=1
        raw=evidence/f"run_{result['run_index']:02d}_response.json"
        assert file_hash(raw)==result['response_sha256']
        assert result['image_sha256']==hashes['candidate.png'] and result['design_sha256']==hashes['design.json']
    complete=result['status']=='completed' and result.get('finish_reason')=='stop' and not result.get('truncated')
    manual.append({'run_index':result['run_index'],'status':result['status'],'finish_reason':result.get('finish_reason'),'complete_final_manually_read':result['status']=='completed','selected_final_answer':selected,'strict_consistent_target_hit':complete and selected=='C','complete_final_text':result.get('answer'),'result_path':str((evidence/f"run_{result['run_index']:02d}.json").relative_to(ROOT)),'response_sha256':result.get('response_sha256'),'error':result.get('error')})
possible=summary['two_completed'] and len(manual)==2 and all(r['strict_consistent_target_hit'] for r in manual)
status='possible_two_hit_requires_NEW_independent_review' if possible else 'rejected_no_two_consistent_target_finals'
limits=['Original controls were not run; paired outputs do not independently prove causality.','No human performance measurement or per-marker ablation.','No independent second review performed by author; parent must create a NEW task before delivery.']
write(HERE/'extension_manual_final_review.json',{'created_at':now(),'question_id':qid,'variant_id':vid,'expected_wrong_answer':'C','formal_correct_answer':'E','results':manual,'strict_target_hit_count':sum(r['strict_consistent_target_hit'] for r in manual),'status':status,'full_final_read_rule':'Only each complete final selection is counted. Incidental C mentions or contradictory letter/value choices never count.','limits':limits})
current=inputs(ad,qid);assert current==before['fresh_input_fingerprints']
elig=eligibility(qid)
write(HERE/'extension_evidence_audit.json',{'created_at':now(),'fresh_eligibility_end':elig,'source_fingerprints_equal_before_after':True,'source_fingerprints':current,'all_preexisting_primary_evidence_unchanged':True,'original_evidence_files_checked':len(before['original_primary_evidence_hashes']),'preexisting_differences':previous_differences,'original_frozen_candidate_plugin_design_hashes_unchanged':hashes,'one_first_invocation_only':True,'requested_runs':binding['requested_runs'],'raw_request_path':str((evidence/'request.json').relative_to(ROOT)),'raw_binding_path':str((evidence/'binding.json').relative_to(ROOT)),'summary_path':str((evidence/'summary.json').relative_to(ROOT)),'request_body_sha256':binding['request_body_sha256'],'binding_sha256':file_hash(evidence/'binding.json'),'exact_same_frozen_PNG_and_preset_all_runs':True,'only_formal_question_candidate_PNG_and_existing_system_prompt_sent':True,'exact_quicktest3_profile_no_overrides_or_retries':True,'new_complete_pair':summary['two_completed']})
proc=json.loads((out/'api_process.json').read_text(encoding='utf-8'));assert (out/'api_process_finished.json').exists()
old_cleanup=json.loads((HERE/'process_cleanup.json').read_text(encoding='utf-8'));pids=old_cleanup['own_API_pids']+[proc['pid']];ids=','.join(str(v) for v in pids)
command=f"$ids=@({ids}); $rows=@(Get-CimInstance Win32_Process | Where-Object {{ $_.ProcessId -in $ids -or ($_.Name -match '^python(w)?\\.exe$' -and $_.CommandLine -like '*background_05/plane_b/*') }} | Select-Object ProcessId,Name,CommandLine); ConvertTo-Json -InputObject $rows -Depth 3 -Compress"
response=subprocess.run(['powershell','-NoProfile','-Command',command],capture_output=True,text=True,encoding='utf-8',check=True)
live=json.loads(response.stdout.strip() or '[]');live=[live] if isinstance(live,dict) else live
remaining=[r for r in live if r['ProcessId']!=os.getpid()];assert not remaining,remaining
write(HERE/'extension_process_cleanup.json',{'checked_at':now(),'own_API_pids_all_runs':pids,'extension_API_pid':proc['pid'],'own_API_processes_still_live':[],'api_finished_record_present':True,'no_live_requests':True,'remaining_own_worker_processes':remaining,'finalizer_pid_excluded':os.getpid(),'no_other_processes_stopped':True,'no_subagents_spawned':True})
candidate={'question_id':qid,'variant_id':vid,'candidate_root':str(out.relative_to(ROOT)),'expected_wrong_answer':'C','formal_correct_answer':'E','complete_manual_finals':finals,'strict_target_hit_count':sum(r['strict_consistent_target_hit'] for r in manual),'candidate_sha256':hashes['candidate.png'],'design_sha256':hashes['design.json'],'plugin_sha256':hashes['plugin.json'],'primary_review_path':str((out/'primary_review.json').relative_to(ROOT)),'mathematical_proof_path':str((HERE/qid/'rigid_feature_math_audit.json').relative_to(ROOT)),'pre_call_recheck_path':str((HERE/'extension_before_calls.json').relative_to(ROOT)),'manual_final_review_path':str((HERE/'extension_manual_final_review.json').relative_to(ROOT)),'evidence_audit_path':str((HERE/'extension_evidence_audit.json').relative_to(ROOT)),'raw_evidence_directory':str(evidence.relative_to(ROOT)),'status':status,'limitations':limits,'approval':'No Pass/Collect, publication or self independent second review.'}
write(HERE/'extension_second_review_queue.json',{'created_at':now(),'new_possible_count':int(possible),'possible_candidates':[candidate] if possible else [],'rejected_candidates':[] if possible else [candidate],'previous_second_review_queue_preserved':str((HERE/'second_review_queue.json').relative_to(ROOT)),'previous_possible_question_ids':['Plane234'],'review_instruction':'Only a NEW parent independent task may review a possible candidate for delivery. Prior Plane234 remains in original immutable queue; avoid double-counting it.'})
write(HERE/'extension_checkpoint.json',{'created_at':now(),'status':'FINITE_PLANE_B_EXTENSION_COMPLETE','scope':'Exactly the already-frozen never-tested Plane223 draft received its first two-run invocation. No redesign, retargeting, repeat invocation or other question tests.','previous_checkpoint_preserved':str((HERE/'checkpoint.json').relative_to(ROOT)),'question_id':qid,'variant_id':vid,'expected_wrong_answer':'C','manual_finals':finals,'strict_target_hit_count':candidate['strict_target_hit_count'],'new_completed_calls':len(completed),'new_complete_pairs':int(summary['two_completed']),'new_error_calls':sum(r['status']=='error' for r in summary['results']),'new_aborted_calls':0,'new_possible_two_hit_count':int(possible),'new_saved_designs':0,'assessed_question_count_unchanged':6,'saved_design_count_unchanged':3,'cumulative_child_completed_calls':4+len(completed),'cumulative_child_complete_pairs':2+int(summary['two_completed']),'cumulative_child_possible_two_hit_count':1+int(possible),'prior_untested_design_now_tested':True,'candidate':candidate,'extension_queue_path':str((HERE/'extension_second_review_queue.json').relative_to(ROOT)),'evidence_audit_path':str((HERE/'extension_evidence_audit.json').relative_to(ROOT)),'process_cleanup_path':str((HERE/'extension_process_cleanup.json').relative_to(ROOT)),'all_prior_evidence_and_formal_hashes_unchanged':True,'no_live_requests':True,'no_subagents_spawned':True,'no_review_API_Pass_Collect_or_delivery':True,'stop_reason':'Authorized one-pair finite extension exhausted; own API process finished.','limitations':limits})
print(json.dumps({'extension_checkpoint':str(HERE/'extension_checkpoint.json'),'extension_queue':str(HERE/'extension_second_review_queue.json'),'manual_finals':finals,'target_hits':candidate['strict_target_hit_count'],'possible':possible,'no_live_requests':True},ensure_ascii=False),flush=True)
