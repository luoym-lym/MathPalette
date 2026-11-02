from env70 import *
from design70 import NAMES,directory
import base64
import gc

def compare(manifest):
    changes=[]
    for relative,expected in manifest.items():
        p=PROJECT/relative
        actual=sha(p) if p.is_file() else None
        if actual!=expected:changes.append({'path':relative,'expected_sha256':expected,'current_sha256':actual})
    return changes

core=read(OWN/'readonly_hashes_start.json')
core_changes=compare(core)
source58=read(OWN/'source58_all_files_start.json')
source58_changes=compare(source58)
save('readonly_preservation_final.json',{'checked_at':now(),'scoped_original_old_evidence_and_batches':len(core),
      'changes':core_changes,'all_source58_files':len(source58),'source58_changes':source58_changes,
      'source58_remained_immutable':not source58_changes,'no_restoration_or_rewrites':True})

snapshot_hashes=read(OWN/'initial_snapshot_hashes.json');metadata=[]
for name,old in snapshot_hashes.items():
    saved=OWN/'read_snapshots'/name
    assert sha(saved)==old['snapshot_sha256']
    current=BASE/name
    original_bytes=saved.read_bytes();current_bytes=current.read_bytes()
    record={'name':name,'original_snapshot_sha256':old['snapshot_sha256'],
        'current_sha256':hashlib.sha256(current_bytes).hexdigest(),
        'original_bytes':len(original_bytes),'current_bytes':len(current_bytes),
        'same_bytes':original_bytes==current_bytes,'exact_original_prefix':current_bytes.startswith(original_bytes)}
    mutable=name in ('continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json')
    if not record['same_bytes']:
        target=OWN/'parent_metadata_end_snapshots'/name
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(current_bytes)
        record['append_bytes']=len(current_bytes)-len(original_bytes) if record['exact_original_prefix'] else None
        record['classification']='diagnostic parent-managed runtime update; no restore or overwrite' if mutable else 'frozen_brief_or_selection_drift_requires_attention'
    else:record['classification']='unchanged'
    metadata.append(record)
    del original_bytes,current_bytes
save('parent_metadata_drift_final.json',metadata)

records=[];eligibility_end=[];queue=[];starts_count=0;completed_count=0;api_errors=[]
for qid in QIDS:
    e=eligibility(qid);eligibility_end.append(e)
    save(f'{qid}/eligibility_end.json',e)
    a=read(OWN/qid/'assessment.json')
    record={'question_id':qid,'assessment_path':str(OWN/qid/'assessment.json'),'status':a['status'],
            'eligible_at_finish':e['eligible'],'original_fingerprint_matches':e['original_approval_fingerprint_matches'],
            'math_proof':a['unique_math_independently_checked'],'source_files':a['source_files'],
            'native_context_path':a['native_context'],'original_native_PNGs_viewed':True}
    if qid not in NAMES:
        record.update(reason=a['reason'],API_calls=0,new_designs=0)
        records.append(record);continue
    d=directory(qid);design=read(d/'design.json')
    starts=sorted((d/'tests').glob('**/run_*_started.json'))
    summaries=sorted((d/'tests').glob('**/summary.json'))
    starts_count+=len(starts)
    evidence=[]
    for summary_path in summaries:
        summary=read(summary_path);invocation=summary_path.parent
        binding=read(invocation/'binding.json')
        body=(invocation/'request.json').read_bytes();payload=json.loads(body)
        assert hashlib.sha256(body).hexdigest()==binding['request_body_sha256']
        assert len(payload['messages'])==2
        assert payload['messages'][0]=={'role':'system','content':'Solve the mathematics question using the provided image. Give a clear final answer at the end. For a multiple-choice question, include the option letter in your final answer.'}
        assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
        assert set(payload)=={'model','stream','thinking','messages'}
        content=payload['messages'][1]['content']
        assert payload['messages'][1]['role']=='user' and len(content)==2
        assert content[0]=={'type':'text','text':row(qid)['question']}
        png=base64.b64decode(content[1]['image_url']['url'].split(',',1)[1],validate=True)
        assert png==(d/'candidate.png').read_bytes() and hashlib.sha256(png).hexdigest()==binding['image_sha256']==design['image_sha256']
        assert (invocation/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
        assert sha(d/'design.json')==binding['design_sha256']
        assert sha(d/'plugin.json')==design['plugin_sha256']
        rows=[]
        for result in summary['results']:
            index=result['run_index'];started=read(invocation/f'run_{index:02d}_started.json')
            assert started['request_body_sha256']==binding['request_body_sha256']
            assert started['image_sha256']==binding['image_sha256'] and started['design_sha256']==binding['design_sha256']
            entry={'run':index,'status':result['status'],'run_path':str(invocation/f'run_{index:02d}.json')}
            if result['status']=='completed':
                completed_count+=1
                raw=invocation/f'run_{index:02d}_response.json';response=read(raw)
                assert sha(raw)==result['response_sha256']
                finals=[{'finish_reason':c.get('finish_reason'),'message':c.get('message')} for c in response['choices']]
                entry.update(raw_path=str(raw),raw_sha256=sha(raw),full_final=finals,
                             elapsed_seconds=result['elapsed_seconds'],http_status=result.get('http_status'),
                             transport_complete_not_truncated=all(c['finish_reason']=='stop' for c in finals))
                del response
            else:
                entry.update(error=result.get('error'),http_status=result.get('http_status'))
                api_errors.append({'question_id':qid,**entry})
            rows.append(entry)
        evidence.append({'summary_path':str(summary_path),'binding_path':str(invocation/'binding.json'),
                'request_path':str(invocation/'request.json'),'request_sha256':binding['request_body_sha256'],
                'exact_formal_question_and_same_frozen_PNG_only':True,'pre_call_preset':binding['expected_wrong_answer'],
                'two_completed':summary['two_completed'],'results':rows})
        del png,body,payload,content
        gc.collect()
    manual_path=d/'manual_final_review.json'
    manual=read(manual_path) if manual_path.is_file() else None
    record.update(variant_id=NAMES[qid],new_designs=1,API_calls=len(starts),
        candidate_directory=str(d),image_sha256=sha(d/'candidate.png'),
        plugin_sha256=sha(d/'plugin.json'),design_sha256=sha(d/'design.json'),
        wrongpreset=design['expected_wrong_answer'],evidence=evidence,
        manual_final_review=manual,difference_audit=str(d/'design_difference_audit.json'),
        every_marker_primary_review=str(d/'primary_review.json'),offline_replay=str(d/'offline_replay_check.json'))
    if manual is not None:
        record['status']='primary_doublehit_requires_NEW_independent_review' if manual['credible_primary_doublehit'] else 'complete_first_pair_no_double_preset_hit'
        if manual['credible_primary_doublehit']:
            assert len(starts)==2 and len(evidence)==1 and evidence[0]['two_completed']
            queue.append({'question_id':qid,'variant_id':NAMES[qid],'candidate_directory':str(d),
                'status':'PRIMARY_ONLY_REQUIRES_PARENT_NEW_INDEPENDENT_REVIEW',
                'correct_answer':row(qid)['answer'],'expected_wrong_answer':design['expected_wrong_answer'],
                'manual_final_review':str(manual_path),'image_sha256':sha(d/'candidate.png'),
                'evidence_dir':str(Path(evidence[0]['summary_path']).parent),
                'original_approval_and_source_hashes_current':e['eligible'] and not core_changes,
                'not_approved_Pass_Collect_delivered':True})
    elif not starts:record['status']='held_untested_after_external_or_local_stop'
    else:record['status']='incomplete_or_error_preserved_never_retry_same_image'
    records.append(record)

save('current_eligibility_all_final.json',eligibility_end)
save('new_candidate_request_raw_binding_audit.json',{'checked_at':now(),'records':[r for r in records if r['question_id'] in NAMES],
     'actual_started_calls':starts_count,'completed_calls':completed_count,'API_errors':api_errors,
     'no_answer_preset_intent_history_params_sent':True})
save('second_review_queue.json',queue,replace=True)
checkpoint={'unit':'background_70','stage':'material_refinement','created_at':now(),
 'status':'external_failure_stop' if api_errors else 'finite_scope_assessed_firstpairs_or_holds_complete',
 'own_root':str(OWN),'question_ids':list(QIDS),'actual_assessed_question_ids':list(QIDS),'unworked_question_ids':[],
 'new_designs':2,'API_calls':starts_count,'completed_calls':completed_count,'complete_candidate_pairs':sum(bool(r.get('manual_final_review',{})) for r in records),
 'credible_primary_doublehits':len(queue),'second_review_queue':queue,'records':records,
 'skipped_question_ids':[q for q in QIDS if q not in NAMES],
 'held_or_incomplete_candidates':[r['question_id'] for r in records if r['question_id'] in NAMES and not r.get('manual_final_review')],
 'API_errors':api_errors,'API_retries':0,'third_calls':0,'original_control_calls':0,
 'local_allocation_import_render_failures':[],
 'offline_parser_exception':{'file':str(OWN/'offline_audit_parser_exception_v1.json'),'resolved_by':str(OWN/'embedded_placeholder_classification.json'),'failed_auditor_preserved':True},
 'read_only_frozen_paths':len(core),'frozen_input_changes':core_changes,'source58_changes':source58_changes,
 'parent_metadata_drift':str(OWN/'parent_metadata_drift_final.json'),
 'source_and_current_approval_audits':str(OWN/'current_eligibility_all_final.json'),
 'full_old_history_and_manual_finals':str(OWN/'old_full_manual_final_review.json'),
 'no_nested_agents_threads_worktrees_servers':True,'inherited_agent_configuration_unchanged':True,
 'formal_edits_or_approvals_Pass_Collect_or_publication_or_delivery':False,
 'process_closure':'See process_closure_final.json, written by parent PowerShell after this Python process exits.',
 'limits':['Primary research only; any doublehit needs a NEW independent parent-launched review before delivery.',
           'Two calls are observations, not proof of mechanism, causal improvement or population reliability.',
           'No guarantee about unrecorded external model calls; all saved task evidence was scanned and retained.']}
save('checkpoint.json',checkpoint,replace=True)
print(json.dumps({k:checkpoint[k] for k in ('status','new_designs','API_calls','completed_calls','credible_primary_doublehits','skipped_question_ids')}))
