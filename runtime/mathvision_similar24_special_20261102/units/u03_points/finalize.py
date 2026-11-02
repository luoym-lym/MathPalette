from unit_env import *

queue=read(OWN/'second_review_queue.json')
assessments=read(OWN/'further_semantic_prescreen.json')
questions=[]
all_reviews=[]
for qid in QIDS:
    current=eligibility(qid)
    assert current['eligible']
    save(OWN/qid/'eligibility_final.json',current)
    variants=[]
    for path in sorted((OWN/qid).glob('*/design.json')):
        folder=path.parent
        design=read(path)
        review=read(folder/'manual_full_final_review.json')
        summary=read(review['summary_path'])
        replay=read(folder/'independent_replay.json')
        assert replay['exact_replay']
        assert len(summary['results'])==2 and summary['two_completed']
        assert len(list(folder.glob('tests/*/run_*_started.json')))==2
        assert read(folder/'api_process_finished.json')['actual_urllib_send_events']==2
        assert (Path(review['summary_path']).parent/'design_snapshot.json').read_bytes()==path.read_bytes()
        assert sha(path.read_bytes())==review['design_sha256']
        assert sha((folder/'plugin.json').read_bytes())==design['plugin_sha256']
        assert sha((folder/'candidate.png').read_bytes())==design['candidate_sha256']
        assert (folder/'candidate.png').read_bytes()==(folder/'repeat.png').read_bytes()==(folder/'independent_replay.png').read_bytes()
        assert all(r['complete_nontruncated'] for r in review['runs'])
        variants.append({'variant_id':design['variant_id'],'candidate_directory':str(folder),
                         'frozen_wrong_preset':review['frozen_wrong_preset'],
                         'manually_read_final_letters':[r['final_letter_read_manually'] for r in review['runs']],
                         'two_complete_hit':review['two_hit'],'status':review['outcome'],
                         'image_sha256':design['candidate_sha256'],'plugin_sha256':design['plugin_sha256'],
                         'design_sha256':review['design_sha256'],'summary_path':review['summary_path'],
                         'full_manual_review_path':str(folder/'manual_full_final_review.json'),
                         'precall_primary_review_path':str(folder/'primary_review_before_calls.json'),
                         'transfer_path':str(folder/'reference_transfer.json'),'actual_calls':2})
        all_reviews.append(review)
    primary=[v for v in variants if v['two_complete_hit']]
    reason=(None if primary else 'No frozen design achieved two matching complete finals. Additional concise true-information relations were considered; no further credible distinct targeted comparison is currently established without reusing failed inputs, merely moving colors, imposing same-color-only corner restrictions, or adding clutter. This is unresolved qualification, not proof that no future legal Special can work.')
    result={'question_id':qid,'assessed':True,'unworked':False,'current_eligible':current['eligible'],
            'original_unique_correct_answer':'E','mathematical_proof_path':str(OWN/qid/'mathematical_proof.json'),
            'actual_calls':sum(v['actual_calls'] for v in variants),'new_distinct_tested_design_count':len(variants),
            'variants':variants,'PRIMARY_candidates':primary,
            'status':'PRIMARY_ONLY_PARENT_REVIEW_PENDING' if primary else 'QUALIFICATION_UNRESOLVED_NO_TWO_HIT',
            'unfinished_reason':reason,'further_semantic_prescreen_path':str(OWN/'further_semantic_prescreen.json'),
            'count_or_quota_early_stop_used':False,'all_failed_evidence_retained':True}
    save(OWN/qid/'research_result.json',result)
    questions.append(result)

readin=read(OWN/'readin_audit.json')
source_checks=[];metadata_changes=[]
for item in readin['files']:
    path=Path(item['path'])
    current=sha(path.read_bytes())
    result={'path':str(path),'initial_sha256':item['sha256'],'current_sha256':current,'unchanged':current==item['sha256']}
    # Parent progress/brief metadata is not original source and is never restored.
    is_parent_metadata=path.parent==TASK and path.name in ASSIGNMENT['required_parent_scope_files']
    if is_parent_metadata and not result['unchanged']:
        metadata_changes.append(result)
    else:
        source_checks.append(result)
assert all(r['unchanged'] for r in source_checks),'Read-only source or evidence bytes changed'
localization=read(OWN/'harness/localization_audit.json')
assert sha(Path(localization['original_path']).read_bytes())==localization['original_sha256']
assert sha(Path(localization['local_path']).read_bytes())==localization['local_sha256']
save(OWN/'source_preservation_final.json',{'created_at':now(),'checks':source_checks,
     'all_frozen_source_and_old_evidence_bytes_unchanged':True,'parent_metadata_changes_not_source_drift':metadata_changes,
     'original_harness_and_localized_copy_unchanged':True,'strict_own_root_writeguard_used':True,
     'formal_library_approvals_indices_recipes_workbench_state_edits':0,
     'scope_expansion_subagents_servers_worktrees':0,
     'environment_variables_set_only_in_own_process':True})
calls=sum(q['actual_calls'] for q in questions)
assert calls==len(list(OWN.glob('Plane*/**/tests/*/run_*_started.json')))
assert len(queue)==sum(bool(r['two_hit']) for r in all_reviews)
report={'created_at':now(),'unit':'u03_points','scope':QIDS,
        'research_role':'PRIMARY_ONLY_NOT_INDEPENDENT_SECOND_REVIEW',
        'status':'RESEARCH_ASSESSED_ALL_QUALIFICATION_UNRESOLVED' if not queue else 'PRIMARY_QUEUE_READY_FOR_NEW_PARENT_REVIEW',
        'PRIMARY_candidate_count':len(queue),'actual_new_API_calls':calls,
        'complete_nontruncated_responses':calls,'API_errors':[],'aborted_calls':[],
        'offline_errors':[read(OWN/'offline_error_001.json')],
        'visual_audit_metadata_correction':'At initial read-in, readin.py attached the same visual_inspection string to C01.png and original.png records. All nine C01s had actually been viewed before designing. The nine reference original.png images were then viewed separately before finalization. Initial byte-read hashes remain correct; no candidate relied on an unviewed C01. This clarification preserves the overbroad initial label rather than silently rewriting it.',
        'questions':questions,'holds':[],'skips':[],'unworked':[],
        'unfinished':[{'question_id':q['question_id'],'reason':q['unfinished_reason']} for q in questions if q['unfinished_reason']],
        'second_review_queue_path':str(OWN/'second_review_queue.json'),
        'source_preservation_path':str(OWN/'source_preservation_final.json'),
        'process_closure_audit_path':str(OWN/'process_closure_audit.json'),
        'all_failures_raw_requests_responses_and_binding_hashes_retained':True,
        'original_quicktest3_harness_only_local_path_changes':True,
        'same_PNG_exactly_two_calls_per_question_design':True,
        'posthoc_preset_changes_third_calls_or_failed_old_image_retries':0,
        'not_stopped_to_save_quota_or_at_three_candidates':True,
        'no_universal_impossibility_or_causal_gain_or_general_success_rate_claim':True,
        'no_delivery_independent_second_review_user_Pass_Collect_or_approval':True,
        'limitations':['Every qualified PRIMARY would require a brand-new independent parent second review before delivery.',
                       'Unresolved qualification is retained explicitly; it is not completion of the requested 24-question Special set.',
                       'Model explanations sometimes misread coordinates, edge incidence or arithmetic; final-answer agreement alone does not establish the proposed mechanism.']}
save(OWN/'research_report.json',report)
checkpoint={'unit':'u03_points','updated_at':now(),'status':report['status'],
            'question_status':{q['question_id']:q['status'] for q in questions},
            'new_actual_calls':calls,'complete_calls':calls,'PRIMARY_candidates':len(queue),
            'formal_changes':0,'errors':[{'kind':'local_offline_serialization','resolved':True,'path':str(OWN/'offline_error_001.json')}],
            'API_errors':[],'aborted_calls':[],'holds':[],'skips':[],'unworked':[],
            'unfinished':report['unfinished'],'research_report':str(OWN/'research_report.json'),
            'second_review_queue':str(OWN/'second_review_queue.json'),'process_cleanup':'await final OS process check; no API invocation pending'}
save(OWN/'checkpoint.json',checkpoint,replace=True)
print(json.dumps({'PRIMARY_candidates':len(queue),'actual_calls':calls,
                  'per_question':[{k:q[k] for k in ('question_id','actual_calls','new_distinct_tested_design_count','status')} for q in questions],
                  'source_preserved':True},ensure_ascii=False))
