from research import *
from freeze import VARIANTS
from prepare_designs import PROOFS,SKIPS
import base64

def audit_candidate(qid,var,manual):
    folder=OWN/qid/var
    invocations=list((folder/'tests').glob('quicktest3_*'))
    assert len(invocations)==1
    inv=invocations[0]
    binding=read(inv/'binding.json');summary=read(inv/'summary.json')
    image=(folder/'candidate.png').read_bytes();design=(folder/'design.json').read_bytes()
    request_bytes=(inv/'request.json').read_bytes();request=json.loads(request_bytes)
    assert hashlib.sha256(image).hexdigest()==binding['image_sha256']
    assert hashlib.sha256(design).hexdigest()==binding['design_sha256']
    assert (inv/'design_snapshot.json').read_bytes()==design
    assert hashlib.sha256(request_bytes).hexdigest()==binding['request_body_sha256']
    assert binding['expected_wrong_answer']==json.loads(design)['expected_wrong_answer']
    assert set(request)=={'model','stream','thinking','messages'}
    assert request['model']=='mimo-v2.6-flash' and request['stream'] is False and request['thinking']=={'type':'disabled'}
    assert len(request['messages'])==2
    current=eligibility(qid,folder/'eligibility_final.json')
    assert current['eligible'] and request['messages'][1]['content'][0]=={'type':'text','text':current['record']['question']}
    assert request['messages'][0]=={'role':'system','content':binding['system_prompt']}
    assert binding['system_prompt']=='Solve the mathematics question using the provided image. Give a clear final answer at the end. For a multiple-choice question, include the option letter in your final answer.'
    assert binding['settings']['api_base']=='https://token-plan-cn.xiaomimimo.com/v1'
    assert len(request['messages'][1]['content'])==2
    assert base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==image
    assert binding['image_path']==str(folder/'candidate.png') and binding['design_path']==str(folder/'design.json')
    assert summary['two_completed'] and len(summary['results'])==2 and len(manual['finals'])==2
    assert len(list(inv.glob('run_*_started.json')))==len(list(inv.glob('run_*_response.json')))==2
    assert not list(inv.glob('*incomplete*')) and not list(inv.glob('*aborted*'))
    rows=[]
    for i in range(1,3):
        run=read(inv/f'run_{i:02d}.json');started=read(inv/f'run_{i:02d}_started.json');raw=read(inv/f'run_{i:02d}_response.json')
        assert run['status']=='completed' and run['http_status']==200 and not run.get('truncated')
        choice=raw['choices'][0]
        assert choice['finish_reason']=='stop' and choice['message']['content']==run['answer']
        assert raw['model']=='mimo-v2.6-flash'
        assert sha(inv/f'run_{i:02d}_response.json')==run['response_sha256']
        assert run['run_id']==started['run_id']
        for field in ['request_body_sha256','image_sha256','design_sha256']:
            assert run[field]==started[field]==binding[field]
        rows.append({'run_index':i,'status':run['status'],'finish_reason':choice['finish_reason'],'full_raw_assistant_content':choice['message']['content'],'manual_terminal_answer':manual['finals'][i-1],'manual_hit_unchanged_preset':manual['hits'][i-1],'contradictory_terminal_answer':False,'raw_response_path':str(inv/f'run_{i:02d}_response.json'),'raw_response_sha256':sha(inv/f'run_{i:02d}_response.json'),'elapsed_seconds':run['elapsed_seconds'],'usage':run['usage']})
    assert current['formal_input_binding']==read(folder/'render_check.json')['formal_binding_before']
    result={'question_id':qid,'variant_id':var,'created_at':now(),'predeclared_wrong_answer':binding['expected_wrong_answer'],'manual_finals':manual['finals'],'runs':rows,'manual_review':manual['review'],'primary_credible_two_hit':all(manual['hits']),'outcome':'MISS' if not all(manual['hits']) else 'POSSIBLE_PENDING_NEW_INDEPENDENT_REVIEW','evidence_directory':str(inv),'exact_same_frozen_image_design_request_both_runs':True,'exact_profile_system_and_formal_question_only':True,'no_timeout_token_profile_override_or_retry':True,'two_completed_exactly':True,'binding_sha256':sha(inv/'binding.json'),'request_sha256':sha(inv/'request.json'),'design_sha256':sha(folder/'design.json'),'plugin_sha256':sha(folder/'plugin.json'),'png_sha256':sha(folder/'candidate.png'),'pixel_sha256':binding['pixel_sha256'],'difference_audit_path':str(folder/'design_difference_audit.json'),'path_binding_path':str(folder/'path_bindings.json'),'math_and_native_review_path':str(folder/'primary_prescreen.json'),'current_original_approval_content_sha256':current['current_content_sha256'],'full_final_answers_manually_read':True,'causal_and_mechanism_limit':'No original-control increment, human prevalence or mechanism-faithfulness established. Hit judgments concern only literal complete finals against the unchanged pre-call preset. No second review was done.'}
    dump(folder/'manual_final_review.json',result)
    return result

def finalize():
    manual=read(OWN/'manual_final_decisions.json')
    assert set(manual)==set(VARIANTS)
    results=[audit_candidate(q,v,manual[q]) for q,v in VARIANTS.items()]
    before=read(OWN/'readonly_snapshot_before_calls.json')
    checks=[{'path':p,'before_sha256':h,'after_sha256':sha(p),'unchanged':sha(p)==h} for p,h in before['files'].items()]
    diagnostic=[]
    for c in checks:
        if c['unchanged']:continue
        assert Path(c['path'])==SHARED/'continuation_brief.txt', 'Unexpected frozen source/evidence drift'
        data=Path(c['path']).read_bytes();rolling=hashlib.sha256();matched=None
        for index,b in enumerate(data):
            rolling.update(bytes([b]))
            if rolling.hexdigest()==c['before_sha256']:
                matched=index+1;break
        assert matched is not None, 'Continuation brief is not a byte-preserving append'
        diagnostic.append(c | {'classification':'Concurrent append-only runtime dispatch metadata, not a frozen question/renderer/evidence input','old_bytes_preserved_as_exact_prefix':True,'verified_original_prefix_bytes':matched,'appended_bytes':len(data)-matched,'appended_text':data[matched:].decode('utf-8'),'old_hash_not_rewritten':True,'file_not_restored_or_edited_by_worker':True})
    immutable=[c for c in checks if Path(c['path'])!=SHARED/'continuation_brief.txt']
    assert all(c['unchanged'] for c in immutable)
    eligibility_end={q:eligibility(q,OWN/q/'eligibility_checkpoint.json')['eligible'] for q in IDS}
    assert all(eligibility_end.values())
    queue=[r for r in results if r['primary_credible_two_hit']]
    dump(OWN/'readonly_preservation_final.json',{'at':now(),'checked_file_count':len(checks),'immutable_unchanged_file_count':len(immutable),'all_scoped_original_history_protocol_helper_files_unchanged':True,'checks':checks,'diagnostic_runtime_metadata_changes':diagnostic,'scope_limit':'No attribution or broad unchanged-workspace claim about unrelated concurrent edits. All own tool mutations and Python write guard were confined to background_53.'})
    dump(OWN/'second_review_queue.json',{'unit':'background_53','stage':'material_refinement','created_at':now(),'candidates':queue,'candidate_count':len(queue),'parent_action':'Only if nonempty, start a NEW independent reviewer; primary worker does not second-review, Pass, Collect, approve originals or deliver.'})
    for r in results:
        q=r['question_id']
        dump(OWN/q/'assessment.json',{'question_id':q,'decision':r['outcome'],'original_unique_solution':PROOFS[q],'variant_id':r['variant_id'],'new_design_count':1,'new_call_count':2,'manual_finals':r['manual_finals'],'expected_wrong_answer':r['predeclared_wrong_answer'],'primary_credible_two_hit':r['primary_credible_two_hit'],'full_review_path':str(OWN/q/r['variant_id']/'manual_final_review.json')})
    checkpoint={'unit':'background_53','stage':'material_refinement','status':'complete_exhausted_assigned8','finished_at':now(),'assigned_question_ids':IDS,'actual_assessed_question_ids':IDS,'assessed_question_ids':IDS,'unworked_question_ids':[],'tested_question_ids':list(VARIANTS),'skipped_question_ids':list(SKIPS),'new_design_count':4,'new_candidate_call_count':8,'new_control_call_count':0,'completed_call_count':8,'error_call_count':0,'aborted_call_count':0,'retry_count':0,'possible_candidate_count':len(queue),'all_new_preset_pair_outcomes':results,'skip_assessments':{q:read(OWN/q/'assessment.json') for q in SKIPS},'Solid245_additional_direction':str(OWN/'Solid245/continued_assessment.json'),'old_history_audit':str(OWN/'old_full_raw_and_request_readthrough.json'),'source_native_read_receipts':str(OWN/'source_native_read_receipts.json'),'full_frozen_source_documents':{q:str(OWN/q/'complete_frozen_source_documents_read.json') for q in IDS},'independent_rejects_readthrough':str(OWN/'complete_independent_reject_readthrough.json'),'qualification_current':eligibility_end,'frozen_original_binding_files':{q:str(OWN/q/'eligibility_checkpoint.json') for q in IDS},'math_audit':str(OWN/'math_calculation_audit.json'),'artist_preservation_audit':str(OWN/'original_artist_preservation_audit.json'),'readonly_final_audit':str(OWN/'readonly_preservation_final.json'),'second_review_queue':str(OWN/'second_review_queue.json'),'offline_exceptions':[str(OWN/'offline_exception_01.json'),str(OWN/'offline_exception_02.json')],'external_API_errors':[],'historical_bad_JSON_in_assigned_history':0,'historical_abort_preserved':'Solid238 old subrange_14_binding second call aborted after verified ownPID18840; that old image/preset was not retried.','process_cleanup':'See process_cleanup_final.json; all API caller processes returned normally; no children spawned.','no_pass_collect_original_approval_delivery_or_self_second_review':True,'limits':['All4 new tested images missed their own immutable presets; no possible candidate is inferred from different wrong finals.','No original-control calls repeated. No causal benefit, human statistical effect or per-mark marginal effect claimed.','Historical15 complete raw responses and1 abort were read and preserved; no missing or invalid response was repaired.']}
    checkpoint['offline_exceptions'].append(str(OWN/'offline_exception_03.json'))
    checkpoint['diagnostic_runtime_metadata_changes']=diagnostic
    checkpoint['immutable_unchanged_file_count']=len(immutable)
    checkpoint['total_preservation_files_checked']=len(checks)
    checkpoint['process_cleanup_evidence']=str(OWN/'process_cleanup_final.json')
    dump(OWN/'checkpoint.json',checkpoint)
    print(json.dumps({'assessed':IDS,'designs':4,'calls':8,'possible':len(queue),'immutable_unchanged_files':len(immutable),'diagnostic_runtime_appends':len(diagnostic)},ensure_ascii=False))

if __name__=='__main__':finalize()
