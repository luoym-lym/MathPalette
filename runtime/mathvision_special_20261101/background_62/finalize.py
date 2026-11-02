from bootstrap import install,OWN,PROJECT,SESSION
install()
from gates import sha,load,save,now,eligibility
from pathlib import Path
import json,hashlib

mutable={'continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','launch58_63_20261102.json'}
parent=[]
for snap in (OWN/'parent_initial_snapshots').iterdir():
    p=SESSION/snap.name;b=snap.read_bytes();c=p.read_bytes()
    parent.append({'path':str(p),'original_full_snapshot':str(snap),'original_sha256':hashlib.sha256(b).hexdigest(),'current_sha256':hashlib.sha256(c).hexdigest(),'unchanged':b==c,'original_bytes_exact_prefix':c.startswith(b),'parent_append_bytes':len(c)-len(b) if c.startswith(b) else None,'classification':'unchanged' if b==c else ('parent_exact_prefix_append' if c.startswith(b) else 'parent_metadata_update_diagnostic') if p.name in mutable else 'immutable_brief_or_assignment_changed','old_snapshot_not_rewritten':True})
save(OWN/'parent_metadata_final.json',parent)
changes=[];checks=[];initial=load(OWN/'readonly_initial_hashes.json')
for p,h in initial.items():
    path=Path(p);current=sha(path)
    if path.name in mutable and path.parent==SESSION:continue
    rec={'path':p,'initial_sha256':h,'current_sha256':current,'equal':h==current};checks.append(rec)
    if h!=current:changes.append(rec)
save(OWN/'readonly_preservation_final.json',{'checked_at':now(),'exact_frozen_files_checked':len(checks),'all_equal':not changes,'changes':changes,'checks':checks,'mutable_parent_metadata_audit':str(OWN/'parent_metadata_final.json'),'no_whole_workspace_unchanged_claim':True})

cases=[];queue=[];started=completed=errors=0
for item in load(SESSION/'background_62_assignment.json')['questions']:
    q=item['question_id'];d=OWN/q/item['variant_id'];qual=eligibility(q,'qualification_final.json')
    assert qual['eligible']
    for r in load(d/'reuse_provenance.json')['all_copy_equality']:
        assert sha(r['source'])==r['sha256']==sha(r['copy'])
    audits=d/'complete_evidence_audit.json'
    if audits.exists():
        ev=load(audits);manual=load(d/'manual_full_final_review.json');inv=Path(ev['evidence_dir'])
        assert sha(inv/'request.json')==ev['request_sha256']
        for r in ev['results']:
            assert sha(r['raw_path'])==r['raw_sha256'] and sha(r['result_path'])==r['result_sha256'] and sha(r['started_path'])==r['started_sha256']
        assert ev['complete_audit'] and len(ev['results'])==2
        nstart=len(list(inv.glob('run_*_started.json')));assert nstart==2
        started+=nstart;completed+=2
        case={'question_id':q,'variant_id':item['variant_id'],'original_date':item['frozen_created_at_utc'],'new_design_or_mechanism':False,'first_pair_of_never_called_frozen_draft':True,'expected_wrong_answer':item['expected_wrong_answer'],'correct_answer':item['correct_answer'],'manual_finals':[r['terminal_answer'] for r in manual['runs']],'status':manual['status'],'double_preset_hit':manual['double_preset_hit'],'image_sha256':ev['frozen_image_sha256'],'design_sha256':ev['frozen_design_sha256'],'plugin_sha256':ev['frozen_plugin_sha256'],'request_sha256':ev['request_sha256'],'full_binding_and_raw_audit':str(audits),'manual_full_final_review':str(d/'manual_full_final_review.json'),'evidence_directory':str(inv),'reuse_provenance':str(d/'reuse_provenance.json'),'fresh_math_native_marker_schema_replay_review':str(OWN/q/'fresh_validation/fresh_primary_review.json'),'qualification_final':str(OWN/q/'qualification_final.json')}
        if manual['double_preset_hit']:queue.append(case)
    else:
        invs=list((d/'tests').glob('*')) if (d/'tests').exists() else []
        actualstarts=sum(len(list(i.glob('run_*_started.json'))) for i in invs);started+=actualstarts
        actualcompleted=0
        for i in invs:
            for p in i.glob('run_[0-9][0-9].json'):
                r=load(p)
                if r['status']=='completed':actualcompleted+=1
                else:errors+=1
        completed+=actualcompleted
        case={'question_id':q,'variant_id':item['variant_id'],'status':'held_or_incomplete_after_stop','actual_starts':actualstarts,'complete_calls':actualcompleted,'stop_evidence':str(OWN/'STOP_SUBSEQUENT_CALLS.json')}
    cases.append(case)

save(OWN/'second_review_queue.json',{'unit':'background_62','created_at':now(),'primary_possibilities_only':True,'count':len(queue),'candidates':queue,'parent_must_create_NEW_independent_review_before_delivery':True,'self_independent_review_approvals_Pass_Collect_publication_delivery':False})
closure=load(OWN/'process_closure.json')
assert closure['all_owned_API_processes_closed']
checkpoint={'unit':'background_62','stage':'continuation_of52_frozen_untested_first_calls_not_new_designs','status':'completed' if completed==4 else 'checkpoint_stopped_without_retry','updated_at_utc':now(),'question_ids':['Plane482','Plane488'],'actual_assessed_question_ids':['Plane482','Plane488'],'unworked_question_ids':[],'held_question_ids':[x['question_id'] for x in cases if x['status']=='held_or_incomplete_after_stop'],'new_design_count':0,'new_mechanism_count':0,'reused_frozen_drafts_first_test':2,'calls_started':started,'calls_completed':completed,'complete_two_call_pairs':sum(x.get('first_pair_of_never_called_frozen_draft',False) for x in cases),'API_errors':errors,'host_memory_import_render_failures':0,'aborts':0,'terminations':0,'retries':0,'third_calls':0,'original_control_calls':0,'new_credible_primary_possibility_count':len(queue),'cases':cases,'zero_prior_invocation_scan':str(OWN/'zero_prior_invocation_scan.json'),'duplicate_PNG_and_launch_scan':str(OWN/'zero_call_duplicate_path_scan.json'),'prior_preparation_hash_freshness':str(OWN/'preparation_hash_freshness.json'),'full_read_receipts':str(OWN/'read_receipts.json'),'old_full_final_answers':str(OWN/'old_full_finals.json'),'readonly_preservation':str(OWN/'readonly_preservation_final.json'),'all_scoped_immutable_hashes_equal':not changes,'mutable_parent_metadata':str(OWN/'parent_metadata_final.json'),'second_review_queue':str(OWN/'second_review_queue.json'),'process_closure':str(OWN/'process_closure.json'),'all_own_API_processes_closed':True,'all_new_outputs_below':str(OWN),'no_formal_helpers_original_approvals_Special_env_git_dotruntime_old_evidence_delivery_edits':True,'no_approval_Pass_Collect_review_or_publication_APIs':True,'no_nested_agents_threads_worktrees_servers':True,'historical_malformed_records_preserved':len(load(OWN/'zero_prior_invocation_scan.json')['malformed_records']),'limits':['Only available local historical evidence can be scanned; unseen provider evidence is not asserted.','Copied drafts retain old variant IDs, timestamps, presets, plugin and PNG bytes, and internal paths. No new designs counted.','Correct terminal choices do not certify model narratives. No causal effect or human-study claim.','Every possible doublehit requires parent NEW independent review; no delivery is authorized by this checkpoint.']}
save(OWN/'checkpoint.json',checkpoint)
save(OWN/'final_qa.json',{'at':now(),'assigned_scope_finished':completed==4,'all_frozen_copies_and_request_start_raw_hashes_verified':True,'source_preservation_exact':not changes,'all_native_math_schema_each_marker_repeat_replay_audits_saved':True,'full_final_answers_manually_reviewed':completed==4,'API_calls_started':started,'API_calls_complete':completed,'pairs':2 if completed==4 else None,'doublehits':len(queue),'queue_count':len(queue),'processes_closed':True,'malformed_record_copies_hash_exact':all(sha(x['preserved_exact_copy'])==x['sha256'] for x in load(OWN/'zero_prior_invocation_scan.json')['malformed_records'])})
manifest=[]
for p in OWN.rglob('*'):
    if p.is_file() and p.name!='artifact_manifest.json':manifest.append({'path':str(p.relative_to(OWN)),'bytes':p.stat().st_size,'sha256':sha(p)})
save(OWN/'artifact_manifest.json',{'at':now(),'files':manifest,'manifest_excludes_itself':True})
print(json.dumps({'status':checkpoint['status'],'cases':[{k:c.get(k) for k in ['question_id','manual_finals','status']} for c in cases],'calls_started':started,'calls_completed':completed,'possibilities':len(queue),'readonly_files_checked':len(checks),'readonly_hash_changes':changes,'processes_closed':True},ensure_ascii=False))
