import bootstrap75 as boot
from research75 import *
from designs75 import specifications
from assess75 import REASONS
import base64
import gc

def verify_candidate(q):
    d=OWN/q/specifications(q)[0]
    if not (d/'design.json').exists():return {'question_id':q,'status':'not_frozen'}
    design=read(d/'design.json');hashes={}
    for f,k in [('candidate.png','image_sha256'),('plugin.json','plugin_sha256'),('math_proof_snapshot.json','math_proof_sha256'),('design_difference_audit.json','difference_audit_sha256')]:
        hashes[f]={'current':sha((d/f).read_bytes()),'frozen':design[k]};assert hashes[f]['current']==hashes[f]['frozen']
    for f in ['repeat.png','offline_replay.png']:assert (d/f).read_bytes()==(d/'candidate.png').read_bytes()
    result={'question_id':q,'directory':str(d),'frozen_hashes':hashes,'new_design_primary_only':True,'predeclared_wrong_answer':design['expected_wrong_answer'],'old_failed_png_reused':False,'fresh_replay_byte_identity':True,'request_evidence':[]}
    invs=list((d/'tests').glob('quicktest3_*')) if(d/'tests').exists() else []
    for inv in invs:
        binding=read(inv/'binding.json');reqbytes=(inv/'request.json').read_bytes();request=json.loads(reqbytes)
        assert sha(reqbytes)==binding['request_body_sha256']
        assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
        assert set(request)=={'model','stream','thinking','messages'} and request['stream'] is False
        assert request['messages'][0]=={'role':'system','content':binding['system_prompt']}
        contents=request['messages'][1]['content'];assert request['messages'][1]['role']=='user'
        assert len(contents)==2 and contents[0]=={'type':'text','text':binding['question']}
        image_data=base64.b64decode(contents[1]['image_url']['url'].split(',',1)[1]);assert image_data==(d/'candidate.png').read_bytes()
        del image_data,request,reqbytes;gc.collect()
        assert (inv/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
        assert binding['expected_wrong_answer']==design['expected_wrong_answer']
        assert binding['image_sha256']==design['image_sha256']
        assert binding['design_sha256']==sha((d/'design.json').read_bytes())
        assert binding['question']==read(OWN/q/'eligibility_start.json')['formal_record']['question']
        jobs=[]
        for p in sorted(inv.glob('run_*_started.json')):
            start=read(p);assert start['request_body_sha256']==binding['request_body_sha256'];i=start['run_index'];jobp=inv/f'run_{i:02d}.json';rawp=inv/f'run_{i:02d}_response.json'
            job=read(jobp) if jobp.exists() else {'status':'incomplete_no_finished_job'}
            if rawp.exists() and job.get('response_sha256'):assert sha(rawp.read_bytes())==job['response_sha256']
            jobs.append({'start':str(p),'start_sha256':sha(p.read_bytes()),'job':str(jobp) if jobp.exists() else None,'status':job['status'],'raw_response':str(rawp) if rawp.exists() else None,'raw_sha256':sha(rawp.read_bytes()) if rawp.exists() else None})
        result['request_evidence'].append({'invocation':str(inv),'binding':str(inv/'binding.json'),'binding_sha256':sha((inv/'binding.json').read_bytes()),'request_sha256':binding['request_body_sha256'],'exact_question_image_only_payload_verified':True,'original_systemprompt_profile_unchanged':True,'runs':jobs,'started_count':len(jobs),'no_third_call':len(jobs)<=2})
    review=d/'manual_final_review.json'
    if review.exists():result['manual_full_final_review']=read(review)
    else:result['status']='held_no_complete_manually_reviewed_pair'
    partial=d/'partial_manual_final_review.json'
    if partial.exists():result['partial_manual_final_review']=read(partial)
    return result

def main():
    preserve=[];source=[];elig=[];metadata=[]
    for q in IDS:
        e=eligible(q);put(OWN/q/'eligibility_final.json',e);elig.append(e)
        start=read(OWN/q/'eligibility_start.json')
        changes=[]
        for rel,h in start['content_manifest']['files'].items():
            p=(PROJECT/'PlaneGeometry'/rel).resolve();cur=sha(p.read_bytes())
            if cur!=h:changes.append({'path':str(p),'before':h,'current':cur})
        source.append({'question_id':q,'current_fingerprint_matches_user_approval':e['fingerprint_matches'],'current_record_unchanged':start['formal_record']==e['formal_record'],'source_changes':changes,'initial_fingerprint':start['current_original_fingerprint'],'final_fingerprint':e['current_original_fingerprint']})
    old=read(OWN/'old_history_full_read_audit.json')['files']+read(OWN/'delivery_reference_read_audit.json')
    seen=set()
    for row in old:
        p=Path(row['path'])
        if str(p) in seen:continue
        seen.add(str(p));h=sha(p.read_bytes())
        if h!=row['sha256']:preserve.append({'path':str(p),'initial':row['sha256'],'current':h})
    for rel in ['continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','quota_resume74_76_20261102.json']:
        p=BASE/rel;snap=OWN/'snapshots'/str(p.relative_to(PROJECT)).replace('\\','__').replace('/','__');before=snap.read_bytes();current=p.read_bytes()
        classification='identical' if before==current else 'exact_prefix_parent_append' if current.startswith(before) else 'mutable_parent_update_not_exact_prefix'
        metadata.append({'path':str(p),'original_full_snapshot':str(snap),'original_sha256':sha(before),'current_sha256':sha(current),'original_bytes':len(before),'current_bytes':len(current),'classification':classification,'diagnostic_only':True,'restored_or_rewritten':False})
    put(OWN/'preservation_final.json',{'checked_at':now(),'relevant_source':source,'old_evidence_file_count':len(seen),'old_evidence_changes':preserve,'mutable_parent_metadata':metadata,'strict_writeguard_root':str(OWN),'own_formal_Special_approvals_env_git_dotruntime_writes':False,'whole_workspace_unchanged_claim':False,'other_active_workers_readonly_and_untouched':True})
    candidates=[verify_candidate(q) for q in ['Plane317','Plane337','Plane385']]
    put(OWN/'frozen_evidence_final_audit.json',{'checked_at':now(),'candidates':candidates})
    assessments=[]
    for q in IDS:
        a=read(OWN/q/'assessment.json')
        if q in REASONS:
            a.update(REASONS[q]);put(OWN/q/'assessment.json',a)
        assessments.append(a)
    actual=len(list(OWN.glob('Plane*/r75_*/tests/quicktest3_*/run_*_started.json')))
    complete=len(list(OWN.glob('Plane*/r75_*/tests/quicktest3_*/run_*_response.json')))
    doublehits=[c for c in candidates if c.get('manual_full_final_review',{}).get('two_complete_finals_hit_own_preset')]
    cp=read(OWN/'checkpoint.json');cp.update(updated_at=now(),status='finite_scope_completed',actual_assessed_question_ids=IDS,unworked_question_ids=[],primary_assessments=assessments,current_eligibility_paths={q:str(OWN/q/'eligibility_final.json') for q in IDS},math_proofs={q:str(OWN/q/'math_proof.json') for q in IDS},native_audits={q:str(OWN/q/'native_capture_audit.json') for q in IDS},new_frozen_designs=3,reasoned_skips=5,current_API_calls=actual,complete_response_files=complete,complete_candidate_pairs=sum(bool(c.get('manual_full_final_review')) for c in candidates),credible_primary_doublehits=[c['question_id'] for c in doublehits],zero_call_pretest_audit=str(OWN/'global_zero_call_pretest_audit.json'),frozen_bindings_and_full_manual_finals=str(OWN/'frozen_evidence_final_audit.json'),preservation_audit=str(OWN/'preservation_final.json'),holds=[c for c in candidates if c.get('status')=='held_no_complete_manually_reviewed_pair'],process_closure_audit=str(OWN/'process_closure_audit.json'),owned_live_API_requests=0,errors=[{'type':'local_path_audit_serialization','count':2,'recovered':True,'stage':'before rendering or any API','preserved':str(OWN/'local_failures/native_path_serialization'),'never_counted_as_API':True}],primary_text_corrections=[{'question_id':'Plane384','field':'skip narrative shaded-cell count','old':'seven','correct':'eight','saved_math_shaded_coordinates_always_had_eight':True,'formal_or_frozen_design_edits':False}],remote_errors=[read(OWN/'remote_error_stop.json')] if(OWN/'remote_error_stop.json').exists() else [],no_controls_or_connectivity_ping=True,no_retry_or_third_call=True,no_self_independent_review=True,no_delivery_publication_userapproval_Pass_Collect_or_formal_edits=True)
    put(OWN/'checkpoint.json',cp)
    if (OWN/'stop_after_external_stall.json').exists():
        stop=read(OWN/'stop_after_external_stall.json')
        cp.update(status='checkpoint_external_stall_all_eight_assessed',stop_reason='One verified own request was abandoned after sustained no-response; no retries or subsequent model calls.',aborts=[stop],owned_live_API_requests=0,completed_API_calls=complete,started_API_attempts=actual,complete_candidate_pairs=0,untested_frozen_question_ids=['Plane337','Plane385'],incomplete_test_question_ids=['Plane317'],fresh_Codex_quota_failure_observed=False,only_pre_reset_old65_66_quota_failures_inherited=True)
        put(OWN/'checkpoint.json',cp)
    put(OWN/'second_review_queue.json',{'unit':'background_75','updated_at':now(),'primary_candidates':[{'question_id':c['question_id'],'candidate_directory':c['directory'],'review':c.get('manual_full_final_review'),'requires_NEW_parent_independent_delegate':True} for c in doublehits],'primary_only':True,'independent_review_required_before_delivery':True,'no_self_independent_review':True,'no_candidates_delivered':True})
    print(json.dumps({'assessed':8,'designs':3,'skips':5,'actual_API_calls':actual,'complete_raw_responses':complete,'doublehits':[c['question_id'] for c in doublehits],'old_evidence_changes':preserve,'source_changes':[s for s in source if s['source_changes']],'mutable_metadata_classes':{Path(m['path']).name:m['classification'] for m in metadata}},ensure_ascii=False))

if __name__=='__main__':main()
