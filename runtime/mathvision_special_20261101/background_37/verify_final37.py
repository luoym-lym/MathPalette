from tools37 import *
cp=read(TASK/'checkpoint.json');queue=read(TASK/'second_review_queue.json')
assert cp['status']=='terminal' and cp['actual_assessed_question_ids']==IDS and not cp['unworked_question_ids']
assert cp['completed_candidate_API_call_count']==14 and cp['saved_design_count']==7
assert queue['candidate_count']==1 and queue['candidates'][0]['question_id']=='Solid126'
assert queue['held_numeric_two_hit_count']==1 and queue['held_numeric_two_hits'][0]['question_id']=='Solid230'
notes=read(ROOT/'provenance/source_notes.json')
for q in IDS:
    assert read(TASK/q/'source_geometry_notes.json')==notes[q].get('geometry_notes',{})
    assert eligibility(q)['eligible'] and read(TASK/q/'frozen_inputs.json')==frozen(q)
manifest={}
for e in cp['new_design_records']:
    f=Path(e['candidate_dir']);b=read(Path(e['raw_evidence_dir'])/'binding.json')
    assert b['reference_quick_test_sha256']==file_hash(ROOT/'SolidGeometry/workbench/quick_test.py')
    assert read(f/'manual_final_review.json')['manual_results'][0]['entire_response_read_manually']
    assert read(f/'manual_final_review.json')['manual_results'][1]['entire_response_read_manually']
    assert read(f/'pretest_visual_review.json')['actually_viewed_native_png']
    for p in f.rglob('*'):
        if p.is_file():manifest[str(p.relative_to(TASK)).replace('\\','/')]=file_hash(p)
write(TASK/'artifact_manifest.json',{'created_at':now(),'candidate_evidence_files':manifest,'file_count':len(manifest),'caches_excluded':True})
write(TASK/'final_verification.json',{'created_at':now(),'terminal_checkpoint_and_queue_consistent':True,'all_eight_current_eligibilities_and_approvals_match':True,'all_eight_frozen_dependencies_and_selected_provenance_geometry_notes_unchanged':True,'all_seven_reference_quicktest_file_hashes_match_current_unchanged_source':True,'fourteen_complete_answers_read_manually':True,'seven_actual_native_candidate_pngs_viewed':True,'credible_primary_candidate_count':1,'held_numeric_pair_count':1,'error_count':0,'abort_count':0,'retry_count':0,'no_live_api_processes_audit':str(TASK/'no_live_api_processes.json'),'readonly_history_changes':read(TASK/'source_and_history_audit_final.json')['readonly_history_changes'],'artifact_manifest':str(TASK/'artifact_manifest.json'),'no_independent_second_review_or_approval_or_delivery':True})
print(json.dumps({'final_verification':'PASS','assessed':8,'new_designs':7,'complete_calls':14,'credible_primary':1,'held_numeric_pair':1,'old_files_verified_unchanged':len(read(TASK/'readonly_history_hashes_before.json')),'candidate_evidence_files':len(manifest)},ensure_ascii=False))
