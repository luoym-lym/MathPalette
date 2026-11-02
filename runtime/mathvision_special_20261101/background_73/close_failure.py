from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,stamp,eligibility,IDS
from prepare import SPECS
from pathlib import Path
import json,hashlib,base64,gc

def hold235():
    q='Solid235'
    d=HERE/q/SPECS[q]['id']
    summaries=list((d/'tests').rglob('summary.json'))
    assert len(summaries)==1
    p=summaries[0].parent
    summary=read(summaries[0])
    binding=read(p/'binding.json')
    assert summary['two_completed'] is False
    assert [v['status'] for v in summary['results']]==['completed','error']
    request_bytes=(p/'request.json').read_bytes()
    assert hashlib.sha256(request_bytes).hexdigest()==binding['request_body_sha256']
    payload=json.loads(request_bytes)
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    assert payload['messages'][0]=={'role':'system','content':binding['system_prompt']}
    assert payload['messages'][1]['content'][0]=={'type':'text','text':read(HERE/q/'formal_record.json')['question']}
    assert len(payload['messages'])==2 and len(payload['messages'][1]['content'])==2
    image=base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
    assert image==(d/'candidate.png').read_bytes()
    del payload,image,request_bytes
    assert sha(d/'candidate.png')==binding['image_sha256']
    assert sha(d/'design.json')==binding['design_sha256']==sha(p/'design_snapshot.json')
    assert binding['expected_wrong_answer']=='B'
    assert sha(PROJECT/'SolidGeometry/workbench/quick_test.py')==binding['reference_quick_test_sha256']
    first=read(p/'run_01_response.json')
    first_job=read(p/'run_01.json')
    error=read(p/'run_02.json')
    assert first['choices'][0]['finish_reason']=='stop' and first_job['status']=='completed'
    assert sha(p/'run_01_response.json')==first_job['response_sha256']
    assert error['error_code']=='incomplete_http_response'
    partial=p/'run_02_incomplete_response.bin'
    binary=partial.read_bytes()
    assert len(binary)==179 and sha(partial)==error['partial_response_sha256']
    assert set(binary)<=set(b'\r\n \t')
    print('Partial bytes:',len(binary),'all whitespace, no final answer')
    assert len(list(p.glob('run_*_started.json')))==2 and len(list(p.glob('run_*_response.json')))==1
    for index in (1,2):
        started=read(p/f'run_{index:02d}_started.json')
        assert started['request_body_sha256']==binding['request_body_sha256'] and started['image_sha256']==binding['image_sha256'] and started['design_sha256']==binding['design_sha256']
    assert len(read(d/'api_process_finished.json')['actual_network_request_gates'])==2
    result={'question_id':q,'variant_id':SPECS[q]['id'],'time':stamp(),'review_kind':'PRIMARY complete-first-final and true transport failure audit only','preset_frozen_before_both_requests':'B','formal_correct_answer':'E','actual_requests':2,'complete_responses':1,'full_first_response':first['choices'][0]['message']['content'],'first_response_manually_read':True,'first_terminal_answer':'A (6)','first_letter_value_consistent':True,'first_matches_preset':False,'second_response_status':'error_incomplete_http_response','second_final_answer':None,'second_raw_partial_path':str(partial),'second_raw_partial_sha256':sha(partial),'second_partial_byte_length':len(binary),'second_partial_only_whitespace':True,'second_elapsed_seconds':error['elapsed_seconds'],'error_job':error,'both_request_start_bindings_exact':True,'solver_only_formal_question_same_frozen_PNG_existing_system_prompt':True,'remote_model_thinking_profile_max_tokens_timeout_credential_logic_unchanged':True,'harness_had_no_local_timeout':True,'automatic_transport_failure_no_manual_termination':True,'incomplete_pair':True,'credible_primary_doublehit':False,'status':'hold_incomplete_pair_after_transport_failure','do_not_retry_this_frozen_image_or_relabel_prior_answers':True,'new_independent_review_queue_eligible':False,'independent_review_userapproval_Pass_Collect_delivery':False}
    save(d/'manual_final_review.json',result)

def finish():
    hold235()
    source=[]
    for item in read(HERE/'frozen_sources_initial.json')+read(HERE/'helper_hashes_before_render.json'):
        p=Path(item['path'])
        actual=sha(p)
        source.append({'path':str(p),'initial_sha256':item['sha256'],'final_sha256':actual,'matches':actual==item['sha256']})
    old=[]
    for q in IDS:
        eligibility(q,'eligibility_final.json')
        for item in read(HERE/q/'old_evidence_manifest.json'):
            actual=sha(Path(item['path']))
            old.append({'path':item['path'],'initial_sha256':item['sha256'],'final_sha256':actual,'matches':actual==item['sha256']})
    assert all(e['matches'] for e in source+old)
    save(HERE/'frozen_source_helper_old_evidence_final_hash_audit.json',{'time':stamp(),'frozen_sources_and_helpers':source,'scoped_old_evidence':old,'all_hash_exact':True,'scope_limited_preservation_claim':True})
    parent=[]
    mutable={'continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json'}
    for item in read(HERE/'snapshot_manifest_initial.json'):
        p=Path(item['path'])
        original=Path(item['snapshot']).read_bytes()
        current=p.read_bytes()
        assert hashlib.sha256(original).hexdigest()==item['sha256']
        same=original==current
        diagnostic=p.name in mutable
        if not diagnostic:assert same,str(p)
        parent.append({'path':str(p),'original_snapshot':item['snapshot'],'original_sha256':item['sha256'],'current_sha256':hashlib.sha256(current).hexdigest(),'original_snapshot_hash_exact':True,'same':same,'exact_old_prefix_of_current':current.startswith(original),'mutable_parent_metadata':diagnostic,'classification':'unchanged' if same else ('diagnostic_exact_prefix_parent_append' if diagnostic and current.startswith(original) else 'diagnostic_parent_metadata_update'),'no_original_record_snapshot_hash_restored_or_rewritten':True})
        del original,current
        gc.collect()
    save(HERE/'parent_metadata_snapshot_final_classification.json',parent)
    results=[]
    for q in IDS:
        if q not in SPECS:
            results.append({'question_id':q,'status':'reasoned_skip','new_designs':0,'actual_new_requests':0,'evidence':str(HERE/q/'primary_math_native_and_skip.json')})
        else:
            d=HERE/q/SPECS[q]['id']
            manual=read(d/'manual_final_review.json')
            results.append({'question_id':q,'variant_id':SPECS[q]['id'],'status':manual.get('status','complete_pair_missed_immutable_preset'),'immutable_wrong_preset':SPECS[q]['preset'],'manual_terminal_answers':manual.get('manual_terminal_answers',['A (6)',None]),'actual_new_requests':2,'complete_responses':1 if q=='Solid235' else 2,'remote_transport_errors':1 if q=='Solid235' else 0,'primary_doublehit':False,'candidate':str(d/'candidate.png'),'candidate_sha256':sha(d/'candidate.png'),'design':str(d/'design.json'),'design_sha256':sha(d/'design.json'),'plugin':str(d/'plugin.json'),'difference_audit':str(d/'design_difference_audit.json'),'primary_review':str(d/'primary_review.json'),'full_manual_final_failure_audit':str(d/'manual_final_review.json'),'fresh_exact_replay':str(d/'offline_replay_audit.json'),'current_eligibility':str(HERE/q/'eligibility_final.json')})
    closure=read(HERE/'process_closure.json')
    assert closure['own_python_processes_remaining']==[]
    queue={'unit':'background_73','time':stamp(),'count':0,'candidates':[],'reason':'Solid227 B/B missed presetC; Solid235 firstA missed presetB, secondHTTP response incomplete; remaining two reasoned skips.','requires_parent_NEW_independent_review_before_any_delivery':True,'independent_review_not_self_performed':True}
    save(HERE/'second_review_queue.json',queue)
    checkpoint={
      'unit':'background_73','stage':'material_refinement','time':stamp(),'continuation_of':'background_61',
      'OWNROOT':str(HERE),'exact_scope':IDS,'assessed_question_ids':IDS,'unworked_question_ids':[],
      'finite_stop':'All four listed questions assessed as first-pair-or-hold; real incomplete HTTP transport failure on last request triggered no-more-calls stop.',
      'new_design_count':2,'actual_new_API_requests':4,'complete_new_responses':3,'completed_new_pairs':1,
      'incomplete_new_pairs':1,'new_primary_doublehits':0,'results':results,
      'source_current_original_approval_math_native_everymarker_design_difference_checks_complete':True,
      'eligibility_rechecked_before_each_actual_request':True,
      'full_old_raw_finals_manually_read_and_old_misses_not_relabelled':True,
      'global_request_and_objection_scan':str(HERE/'global_old_call_and_objection_scan_v2.json'),
      'global_frozen_image_prior_request_scan':str(HERE/'frozen_images_zero_prior_request_audit.json'),
      'frozen_source_helper_old_evidence_final_hash_audit':str(HERE/'frozen_source_helper_old_evidence_final_hash_audit.json'),
      'parent_metadata_final_classification':str(HERE/'parent_metadata_snapshot_final_classification.json'),
      'old_parent_full_snapshots_hashes_preserved':True,'actual_source_design_PNG_request_raw_bindings_hash_exact':True,
      'new_calls_on482_488_206_207':0,'original_controls_run':0,'control_correct_or_causal_gain_hardgate_imposed':False,
      'remote_errors':[{'question_id':'Solid235','run':2,'error':'IncompleteRead(179 bytes read)','elapsed_seconds':900.673,'raw_partial_bytes':179,'raw_partial_only_whitespace':True,'complete_final_answer':None}],
      'external_stop_record':str(HERE/'EXTERNAL_STOP.json'),'no_requests_after_external_error':True,
      'incomplete_remote_requests':1,'manually_aborted_requests':0,'manual_process_terminations':0,'retries':0,'third_calls':0,
      'local_allocation_import_render_failures':[],
      'local_readonly_audit_script_issues':[str(p) for p in sorted(HERE.glob('local_script_error_*.json'))]+[str(HERE/'scan_v1_limitation.json')],
      'early_dimension_statement_correction':str(HERE/'Solid227/primary_math_native.json'),
      'pre_API_counter_scope_clarification':str(HERE/'pre_API_call_count_field_clarification.json'),
      'all_new_files_TEMP_caches_logs_tests_inside_OWNROOT':True,'strict_writeguard_before_project_imports':True,
      'ownprocess_only_OPENBLAS_OMP_MKL_NUMEXPR_THREADS_1':True,
      'remote_model_thinking_system_profile_max_tokens_timeout_credentials_logic_changed':False,
      'original_harness_single_local_PROJECT_line_relocation_only':str(HERE/'harness_byte_diff_audit.json'),
      'no_nested_agents_threads_worktrees_servers_or_scope_expansion':True,
      'own_live_requests':0,'process_closure':str(HERE/'process_closure.json'),
      'independent_second_review_userapproval_originalreview_Pass_Collect_publication_delivery_formal_edits':False,
      'important_hold':'Solid235 frozen image has received its two actual starts and a true second transport failure. Do not retry/relabel it as untested or form a pair with other images.'
    }
    save(HERE/'checkpoint.json',checkpoint)
    artifacts=[{'path':str(p),'sha256':sha(p),'size':p.stat().st_size} for p in HERE.rglob('*') if p.is_file() and p.name!='final_artifact_manifest.json']
    save(HERE/'final_artifact_manifest.json',{'time':stamp(),'files':artifacts,'self_excluded':True})
    print('FINAL:4 actual requests,3 complete responses,1 incomplete transport failure;0 doublehits;0 own live requests')

if __name__=='__main__':finish()
