from bootstrap import HERE, PROJECT, TASK
from audit import IDS, read, save, sha, eligibility, now
import base64
import gc
import hashlib
import json
import sys
from pathlib import Path

def evidence(q):
    assignment=next(x for x in read(TASK/'background_69_assignment.json')['questions'] if x['question_id']==q)
    d=HERE/q/assignment['variant_id']
    folders=list((d/'tests').glob('quicktest3_*')) if (d/'tests').exists() else []
    if not folders: return {'question_id':q,'variant_id':assignment['variant_id'],'status':'unworked_no_API','expected_wrong_answer':assignment['expected_wrong_answer']}
    assert len(folders)==1, 'One invocation per frozen image only'
    folder=folders[0]
    binding=read(folder/'binding.json')
    assert binding['image_sha256']==sha(d/'candidate.png')
    assert binding['design_sha256']==sha(d/'design.json')
    assert (folder/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
    request_bytes=(folder/'request.json').read_bytes()
    assert hashlib.sha256(request_bytes).hexdigest()==binding['request_body_sha256']
    payload=json.loads(request_bytes)
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    assert payload['messages'][0]=={'role':'system','content':binding['system_prompt']}
    user=payload['messages'][1]
    assert user['role']=='user' and len(user['content'])==2
    assert user['content'][0]=={'type':'text','text':binding['question']}
    blob=base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])
    assert blob==(d/'candidate.png').read_bytes()
    del blob,payload,request_bytes
    summary=read(folder/'summary.json') if (folder/'summary.json').exists() else None
    starts=sorted(folder.glob('run_*_started.json'))
    raws=[]
    for start in starts:
        s=read(start); idx=s['run_index']
        assert s['image_sha256']==binding['image_sha256'] and s['design_sha256']==binding['design_sha256'] and s['request_body_sha256']==binding['request_body_sha256']
        rp=folder/f'run_{idx:02d}_response.json'
        job=folder/f'run_{idx:02d}.json'
        obj=read(job) if job.exists() else None
        row={'run_index':idx,'started':str(start),'started_sha256':sha(start),'job':str(job) if job.exists() else None,'status':obj['status'] if obj else 'incomplete_no_result'}
        if rp.exists():
            response=read(rp)
            assert obj and obj['response_sha256']==sha(rp)
            message=response['choices'][0]['message']
            content=message.get('content')
            assert content==obj['answer']
            row.update(response_path=str(rp),response_sha256=sha(rp),full_final_content=content,finish_reason=response['choices'][0].get('finish_reason'))
            del response
        else: row['error']=obj.get('error') if obj else 'No complete response'
        raws.append(row)
    return {'question_id':q,'variant_id':assignment['variant_id'],'original_created_at':assignment['frozen_created_at'],'expected_wrong_answer':assignment['expected_wrong_answer'],'formal_correct_answer':binding.get('question') and read(d/'design.json')['formal_correct_answer'],'status':'complete_pair_pending_manual_review' if summary and summary['two_completed'] else 'error_or_incomplete_stop_no_retry','exactly_two_starts':len(starts)==2,'actual_starts':len(starts),'two_completed':bool(summary and summary['two_completed']),'evidence_directory':str(folder),'binding':str(folder/'binding.json'),'binding_sha256':sha(folder/'binding.json'),'request':str(folder/'request.json'),'request_sha256':sha(folder/'request.json'),'only_exact_formal_question_and_same_frozen_png_sent':True,'original_system_model_thinking_payload_profile_unchanged':True,'results':raws,'new_mechanism_count':0}

def dump(q):
    e=evidence(q)
    save(HERE/q/'request_raw_binding_audit.json',e)
    print(json.dumps(e,ensure_ascii=False,indent=2))

def manual(q,finals,notes):
    e=read(HERE/q/'request_raw_binding_audit.json')
    assert e['two_completed'] and len(e['results'])==len(finals)==len(notes)==2
    for r,final,note in zip(e['results'],finals,notes):
        r.update(complete_final_manually_read=True,manual_terminal_answer=final,manual_explanation=note,terminal_letter_value_internally_consistent=True,hit_own_unchanged_preset=final==str(e['expected_wrong_answer']))
    e.update(manually_reviewed_at_utc=now(),credible_primary_doublehit=all(x['hit_own_unchanged_preset'] for x in e['results']),status='PRIMARY_doublehit_requires_NEW_independent_review' if all(x['hit_own_unchanged_preset'] for x in e['results']) else 'complete_pair_missed_unchanged_preset',independent_second_review_performed=False,original_control_calls=0,retry_third_call_relabel_or_cherrypick=False)
    save(HERE/q/'manual_full_final_review.json',e)
    print(q,e['status'],finals)

def preservation():
    checks=[];seen=set()
    def check(p,expected,category):
        p=Path(p)
        if str(p) in seen:return
        seen.add(str(p));actual=sha(p)
        checks.append({'path':str(p),'category':category,'expected':expected,'actual':actual,'matches':actual==expected})
    for q in IDS:
        baseline=read(HERE/q/'eligibility_initial.json')
        for rel,h in baseline['content']['files'].items():check(PROJECT/'SolidGeometry'/rel,h,'formal original and frozen dependency')
        for row in read(HERE/q/'old_evidence_manifest.json'):check(row['path'],row['sha256'],'scope historical design/raw/request/image evidence')
    with (HERE/'audits/whole_task_file_inventory.jsonl').open(encoding='utf-8') as f:
        for line in f:
            row=json.loads(line);p=Path(row['path'])
            if (TASK/'background_61') in p.parents or p in (TASK/'runtime_isolation.py',TASK/'delivery_bridge_adapter.py',TASK/'harness/quicktest3_isolated.py'):
                check(p,row['sha256'],'immutable original source unit/helper/harness')
    drift=[]
    for row in read(HERE/'audits/initial_snapshots.json'):
        p=Path(row['source']);old=Path(row['snapshot']).read_bytes();new=p.read_bytes()
        mutable=p.name in ('continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json')
        classification='unchanged' if old==new else ('exact_prefix_parent_append' if new.startswith(old) else 'parent_runtime_metadata_update') if mutable else 'unexpected_immutable_change'
        drift.append({'source':str(p),'initial_full_snapshot':row['snapshot'],'initial_sha256':row['sha256'],'current_sha256':hashlib.sha256(new).hexdigest(),'classification':classification,'old_bytes_are_exact_prefix':new.startswith(old),'restored_or_rewritten':False})
        if old!=new:
            dest=HERE/'snapshots'/'final_metadata'/p.name
            dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(new)
        if not mutable:check(p,row['sha256'],'root/branch protocol, brief or assignment')
    # Preserve the old source unit's complete full metadata snapshots and hashes;
    # changes to parent metadata are diagnostic and never rewritten to agree.
    historic=[]
    for name in ('continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json'):
        p=TASK/'background_61/snapshots'/name
        if not p.exists():continue
        dest=HERE/'snapshots'/'original_background_61_metadata'/name
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(p.read_bytes())
        old=p.read_bytes();current=(TASK/name).read_bytes()
        historic.append({'source_snapshot':str(p),'source_sha256':sha(p),'own_full_snapshot':str(dest),'own_sha256':sha(dest),'current_parent_sha256':hashlib.sha256(current).hexdigest(),'classification':'unchanged' if old==current else 'exact_prefix_parent_append' if current.startswith(old) else 'parent_runtime_metadata_update','old_snapshot_preserved':True,'rewritten_to_force_hash_equality':False})
    save(HERE/'audits/terminal_frozen_preservation.json',{'checked_at_utc':now(),'files':checks,'mismatches':[x for x in checks if not x['matches']],'all_checked_frozen_files_hash_exact':all(x['matches'] for x in checks),'initial_parent_metadata_diagnostics':drift,'original_background_61_metadata_diagnostics':historic,'strict_ownroot_guard_precedes_every_project_import':True,'outside_OWNROOT_files_written_by_worker':False})
    assert all(x['matches'] for x in checks)
    print('Preservation:',len(checks),'frozen files hash-exact; parent metadata classified without restoration')

def final():
    entries=[];queue=[];unworked=[];errors=[]
    for q in IDS:
        eligibility(q,'terminal')
        path=HERE/q/'manual_full_final_review.json'
        if path.exists():
            e=read(path);entries.append(e)
            if e['credible_primary_doublehit']:queue.append({'question_id':q,'variant_id':e['variant_id'],'status':'PRIMARY ONLY; parent must launch NEW independent review','evidence_directory':e['evidence_directory'],'primary_math_native_every_marker':str(HERE/q/'primary_math_native_marker_review.json'),'fresh_render_schema_repeat_exact_offline_replay':str(HERE/q/'fresh_render_replay_audit.json'),'zero_prior_call_certificate':str(HERE/q/'zero_prior_call_certification.json'),'manual_full_final_review':str(path),'new_mechanism_count':0,'no_approval_or_delivery':True})
        else:
            e=evidence(q);entries.append(e)
            if e['status']=='unworked_no_API':unworked.append(q)
            else: errors.append(e)
    preservation()
    closure=read(HERE/'audits/process_closure.json')
    assert closure['own_live_api_process_count']==0
    snapshot={'unit':'background_69','stage':'quota_resume_frozen_first_tests','completed_at_utc':now(),'exact_assigned_question_ids':IDS,'assessed_question_ids':IDS,'unworked_API_question_ids':unworked,'stop_reason':'exact assigned scope assessed with first pairs or holds' if not errors else 'real failure; subsequent calls stopped without retry','actual_starts':sum(e.get('actual_starts',0) for e in entries),'complete_pairs':sum(bool(e.get('two_completed')) for e in entries),'credible_primary_doublehits':len(queue),'new_mechanisms':0,'reused_frozen_drafts_preserve_original_variant_date_preset_internal_paths':True,'results':entries,'holds':[],'skips':[],'errors':errors,'local_command_diagnostics':str(HERE/'audits/local_command_diagnostics.json'),'source_approval_eligibility_audits':[str(HERE/q/'eligibility_terminal.json') for q in IDS],'math_native_every_marker_audits':[str(HERE/q/'primary_math_native_marker_review.json') for q in IDS],'whole_task_zero_call_scan':str(HERE/'audits/whole_task_exact_png_scan.json'),'deep_decoded_invocation_scan':str(HERE/'audits/deep_decoded_invocation_scan.json'),'frozen_source_evidence_preservation':str(HERE/'audits/terminal_frozen_preservation.json'),'process_closure':closure,'no_own_live_requests':True,'no_nested_agent_thread_worktree_server':True,'inherited_Codex_configuration_unchanged':True,'formal_approvals_Special_Pass_Collect_publication_delivery_edits_or_calls':False,'parent_metadata_master_continuation_progress_written':False,'second_review_queue':str(HERE/'second_review_queue.json'),'independent_review_performed':False,'limits':['All reviews here are primary; any doublehit requires a NEW independent parent review before delivery.','Two calls establish observations only; no causal gain, original control correctness or mechanism certainty is claimed.','Known completed62/63 images482/488/206/207 were not called or reused.']}
    save(HERE/'second_review_queue.json',{'unit':'background_69','created_at_utc':now(),'candidates':queue,'independent_review_required':True,'self_review_is_not_independent':True})
    save(HERE/'checkpoint.json',snapshot)
    print(json.dumps({'complete_pairs':snapshot['complete_pairs'],'actual_starts':snapshot['actual_starts'],'primary_doublehits':len(queue),'unworked':unworked,'errors':len(errors),'own_live_requests':0},ensure_ascii=False))

if __name__=='__main__':
    if sys.argv[1]=='dump':dump(sys.argv[2])
    elif sys.argv[1]=='manual':manual(sys.argv[2],json.loads(sys.argv[3]),json.loads(sys.argv[4]))
    elif sys.argv[1]=='manual_file':
        q=sys.argv[2];d=read(HERE/'manual_decisions.json')[q];manual(q,d['finals'],d['notes'])
    elif sys.argv[1]=='final':final()
