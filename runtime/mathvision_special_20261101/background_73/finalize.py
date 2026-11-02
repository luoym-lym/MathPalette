from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,stamp,eligibility,IDS
from prepare import SPECS
from pathlib import Path
import json,hashlib,base64,sys,gc

def manual(q,answers):
    s=SPECS[q]
    d=HERE/q/s['id']
    paths=list((d/'tests').rglob('summary.json'))
    assert len(paths)==1
    invocation=paths[0].parent
    summary=read(paths[0])
    binding=read(invocation/'binding.json')
    request_bytes=(invocation/'request.json').read_bytes()
    request=json.loads(request_bytes)
    formal=read(HERE/q/'formal_record.json')
    assert hashlib.sha256(request_bytes).hexdigest()==binding['request_body_sha256']
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert set(request)=={'model','stream','thinking','messages'} and request['stream'] is False
    messages=request['messages']
    assert len(messages)==2 and messages[0]=={'role':'system','content':binding['system_prompt']}
    assert messages[1]['role']=='user' and len(messages[1]['content'])==2
    assert messages[1]['content'][0]=={'type':'text','text':formal['question']}
    binary=base64.b64decode(messages[1]['content'][1]['image_url']['url'].split(',',1)[1],validate=True)
    assert binary==(d/'candidate.png').read_bytes()
    del binary,request,messages,request_bytes
    assert sha(d/'candidate.png')==binding['image_sha256']
    assert sha(d/'design.json')==binding['design_sha256']==sha(invocation/'design_snapshot.json')
    assert sha(PROJECT/'SolidGeometry/workbench/quick_test.py')==binding['reference_quick_test_sha256']
    assert len(list(invocation.glob('run_*_started.json')))==2
    assert len(list(invocation.glob('run_*_response.json')))==2
    assert summary['two_completed'] and len(summary['results'])==2
    assert len(read(d/'api_process_finished.json')['actual_network_request_gates'])==2
    finals=[]
    for i,answer in enumerate(answers,1):
        p=invocation/f'run_{i:02d}_response.json'
        raw=read(p)
        job=read(invocation/f'run_{i:02d}.json')
        started=read(invocation/f'run_{i:02d}_started.json')
        assert job['status']=='completed' and raw['choices'][0]['finish_reason']=='stop'
        assert sha(p)==job['response_sha256']
        assert started['image_sha256']==binding['image_sha256'] and started['design_sha256']==binding['design_sha256'] and started['request_body_sha256']==binding['request_body_sha256']
        content=raw['choices'][0]['message']['content']
        finals.append({'run_index':i,'status':job['status'],'finish_reason':raw['choices'][0]['finish_reason'],'raw_response':str(p),'raw_sha256':sha(p),'job':str(invocation/f'run_{i:02d}.json'),'started':str(invocation/f'run_{i:02d}_started.json'),'full_complete_final_manually_read':True,'full_response_content':content,'manual_terminal_answer':answer,'matches_immutable_preset':answer==s['preset'],'final_letter_value_consistent':True})
        del raw,job,started,content
        gc.collect()
    notes=''
    if q=='Solid227':notes='Both terminal answersB are explicit and miss presetC. Run1 uses correct radii; run2 incorrectly calls every radius a diameter but applies that convention uniformly, retains all ratios and terminatesB. Neither incidental mention ofC nor narrative error is a preset hit.'
    save(d/'manual_final_review.json',{'question_id':q,'variant_id':s['id'],'review_kind':'PRIMARY full raw answer reading only','time':stamp(),'expected_wrong_answer_frozen':s['preset'],'formal_correct_answer':formal['answer'],'manual_terminal_answers':answers,'full_finals':finals,'two_actual_complete_requests_same_frozen_question_PNG_design_preset':True,'exactly_two_no_retry_third_call_or_cherrypick':True,'solver_input_only_formal_question_PNG_existing_system':True,'remote_profile_unchanged':True,'payload_binding_verified':True,'notes':notes,'credible_primary_doublehit':all(a==s['preset'] for a in answers),'no_original_control_run_or_required':True,'independent_second_review':False,'no_userapproval_or_delivery':True})
    print(q,'full final review saved',answers,'preset',s['preset'])

def finish():
    hashes=[]
    for e in read(HERE/'frozen_sources_initial.json')+read(HERE/'helper_hashes_before_render.json'):
        p=Path(e['path'])
        actual=sha(p)
        hashes.append({'path':str(p),'initial_sha256':e['sha256'],'final_sha256':actual,'matches':actual==e['sha256']})
    old=[]
    for q in IDS:
        eligibility(q,'eligibility_final.json')
        for e in read(HERE/q/'old_evidence_manifest.json'):
            actual=sha(Path(e['path']))
            old.append({'path':e['path'],'initial_sha256':e['sha256'],'final_sha256':actual,'matches':actual==e['sha256']})
    assert all(e['matches'] for e in hashes+old)
    save(HERE/'frozen_source_helper_old_evidence_final_hash_audit.json',{'time':stamp(),'frozen_source_helpers':hashes,'scoped_old_evidence':old,'all_hash_exact':True,'scope_limited_preservation_claim':True})
    mutable={'continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json'}
    parent=[]
    for e in read(HERE/'snapshot_manifest_initial.json'):
        p=Path(e['path'])
        original=Path(e['snapshot']).read_bytes()
        current=p.read_bytes()
        initial_exact=hashlib.sha256(original).hexdigest()==e['sha256']
        assert initial_exact
        same=current==original
        is_mutable=p.name in mutable
        if not is_mutable:assert same,str(p)
        parent.append({'path':str(p),'original_snapshot':e['snapshot'],'original_sha256':e['sha256'],'current_sha256':hashlib.sha256(current).hexdigest(),'original_snapshot_preserved_exact':True,'same':same,'old_bytes_exact_prefix_of_current':current.startswith(original),'mutable_parent_metadata':is_mutable,'classification':'unchanged' if same else ('diagnostic_exact_prefix_parent_append' if is_mutable and current.startswith(original) else 'diagnostic_parent_metadata_update'),'never_restored_rewritten_or_rehashed_original_snapshot':True})
        del original,current
    save(HERE/'parent_metadata_snapshot_final_classification.json',parent)
    queue=[]
    results=[]
    complete_calls=0
    for q in IDS:
        if q not in SPECS:
            results.append({'question_id':q,'status':'reasoned_skip','evidence':str(HERE/q/'primary_math_native_and_skip.json'),'new_designs':0,'actual_new_calls':0})
            continue
        s=SPECS[q]
        d=HERE/q/s['id']
        m=read(d/'manual_final_review.json')
        complete_calls+=2
        hit=m['credible_primary_doublehit']
        entry={'question_id':q,'variant_id':s['id'],'status':'PRIMARY_doublehit_pending_NEW_independent_review' if hit else 'complete_pair_missed_immutable_preset','preset':s['preset'],'manual_terminal_answers':m['manual_terminal_answers'],'actual_new_calls':2,'candidate':str(d/'candidate.png'),'candidate_sha256':sha(d/'candidate.png'),'design':str(d/'design.json'),'design_sha256':sha(d/'design.json'),'difference_audit':str(d/'design_difference_audit.json'),'manual_final_review':str(d/'manual_final_review.json'),'primary_review':str(d/'primary_review.json'),'replay_audit':str(d/'offline_replay_audit.json'),'current_eligibility':str(HERE/q/'eligibility_final.json'),'independent_second_review_performed':False}
        results.append(entry)
        if hit:queue.append(entry)
    save(HERE/'second_review_queue.json',{'unit':'background_73','time':stamp(),'candidates':queue,'count':len(queue),'status':'PRIMARY only; parent must launch a NEW independent review for each possibility before delivery','no_self_independent_review':True})
    closure=read(HERE/'process_closure.json')
    assert closure['own_python_processes_remaining']==[]
    save(HERE/'checkpoint.json',{'unit':'background_73','stage':'material_refinement','time':stamp(),'continuation_of':'background_61','exact_scope':IDS,'assessed_question_ids':IDS,'unworked_question_ids':[],'finite_stop':'All four listed questions assessed; first pairs completed for each frozen new image, other two reasoned skips.','new_design_count':len(SPECS),'actual_new_API_calls':complete_calls,'completed_new_pairs':2,'new_primary_doublehits':len(queue),'results':results,'source_current_original_approval_math_native_everymarker_design_difference_checks_complete':True,'global_prior_exact_image_request_audit':str(HERE/'frozen_images_zero_prior_request_audit.json'),'old_request_raw_manual_finals_preserved':True,'old_calls_never_relabeled_or_retried':True,'new_calls_on482_488_206_207':0,'source_helper_old_evidence_final_hash_audit':str(HERE/'frozen_source_helper_old_evidence_final_hash_audit.json'),'parent_metadata_classification':str(HERE/'parent_metadata_snapshot_final_classification.json'),'all_new_files_TEMP_caches_logs_tests_inside_OWNROOT':True,'strict_write_guard_before_project_imports':True,'four_thread_limit_env_vars_process_only':True,'remote_model_thinking_system_profile_max_tokens_timeout_credentials_unchanged':True,'remote_errors':[],'incomplete_remote_calls':[],'aborted_requests':[],'retries':0,'local_allocation_import_render_failures':[],'local_script_audit_issues':[str(p) for p in sorted(HERE.glob('local_script_error_*.json'))]+[str(HERE/'scan_v1_limitation.json')],'early_dimension_commentary_correction':str(HERE/'Solid227/primary_math_native.json'),'own_live_requests':0,'process_closure':str(HERE/'process_closure.json'),'independent_second_review_userapproval_originalreview_Pass_Collect_publication_delivery_formal_edits':False})
    artifacts=[]
    for p in HERE.rglob('*'):
        if p.is_file() and p.name!='final_artifact_manifest.json':artifacts.append({'path':str(p),'sha256':sha(p),'size':p.stat().st_size})
    save(HERE/'final_artifact_manifest.json',{'time':stamp(),'files':artifacts,'scope':'Final unit artifacts including raw bindings and snapshots; self excluded.'})
    print('FINAL',complete_calls,'calls;',len(queue),'PRIMARY possibilities; zero live requests')

if __name__=='__main__':
    if sys.argv[1]=='manual':manual(sys.argv[2],sys.argv[3:])
    elif sys.argv[1]=='finish':finish()

