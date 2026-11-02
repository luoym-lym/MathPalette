from env67 import *
import gc

assert (OWN/'local_failure_checkpoint.json').exists()
assert not (OWN/'copied_frozen_candidates.json').exists()
A=read(OWN/'snapshots/background_67_assignment.json')
failure=read(OWN/'local_failure_checkpoint.json')
source=PROJECT/'SolidGeometry/workbench/partial_style.py'
source_text=source.read_text(encoding='utf-8-sig')
assert "'dash': (float(dash[0]), tuple(dash[1]) if dash[1] is not None else None)" in source_text
diagnostic={'at':now(),'failed_assertion':'paths == json.loads(frozen_paths.json)','actual_exception':failure,'scope_of_failure':'Isolated verification script comparison before candidate render/copy/API. Not a demonstrated source hash change or geometry change.','concrete_comparison_defect':{'unchanged_library_source':str(source),'sha256':sha(source),'source_returns':'style.dash is a tuple, with an optional nested tuple.','saved_JSON_returns':'JSON arrays load as lists.','plain_Python_tuple_list_equality':(0.0,None)==[0.0,None],'consequence':'The direct dict comparison can fail solely because fresh tuples are compared to archived JSON lists. It cannot justify claiming frozen geometry drift.','remaining_unverified':'Complete path equality after representation normalization was NOT rerun. No candidate render, separate replay, copy or remote pair was attempted after the failure.'},'stop_rule_followed':True,'no_failure_flag_removed_or_overridden':True,'no_source_or_frozen_input_edited':True}
save('preflight_comparison_diagnostic.json',diagnostic)

checks=[]
for path,expected in read(OWN/'immutable_initial_hashes.json').items():
    actual=sha(path); checks.append({'path':path,'expected':expected,'actual':actual,'matches':actual==expected,'kind':'approved_source_or_selected_frozen_source'})
for r in read(OWN/'protocol_read_log.json'):
    actual=sha(r['path']); checks.append({'path':r['path'],'expected':r['sha256'],'actual':actual,'matches':actual==r['sha256'],'kind':'protocol'})
for auditfile in ('scoped_old_full_history_audit.json','legacy_scoped_full_history_audit.json'):
    for r in read(OWN/auditfile):
        actual=sha(r['path']); checks.append({'path':r['path'],'expected':r['sha256'],'actual':actual,'matches':actual==r['sha256'],'kind':'old_raw_design_source_evidence'})
save('immutable_source_and_old_raw_end_hash_audit.json',{'at':now(),'all_match':all(r['matches'] for r in checks),'checks':checks,'parent_mutable_metadata_classified_separately':True})
assert all(r['matches'] for r in checks)

metadata=[]
for manifest in (BASE/'background_59/readin_metadata_snapshots.json',OWN/'snapshots/initial_manifest.json'):
    for r in read(manifest):
        p=Path(r['path']); old=Path(r['snapshot'])
        if not p.exists() or not old.exists(): continue
        original=old.read_bytes(); current=p.read_bytes(); h=hashlib.sha256(current).hexdigest()
        dst=OWN/'metadata_final_snapshots'/h/p.name; dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists(): dst.write_bytes(current)
        mutable=p.name in ('continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json')
        classification='unchanged' if original==current else 'exact_prefix_parent_append_diagnostic' if mutable and current.startswith(original) else 'parent_metadata_update_diagnostic' if mutable else 'immutable_changed'
        metadata.append({'source':str(p),'original_full_snapshot':str(old),'original_sha256':hashlib.sha256(original).hexdigest(),'original_bytes':len(original),'final_full_snapshot':str(dst),'final_sha256':h,'final_bytes':len(current),'classification':classification,'append_bytes':len(current)-len(original) if current.startswith(original) else None,'source_never_restored_or_rewritten':True})
        del original,current; gc.collect()
save('parent_metadata_final_diagnostic.json',metadata)
assert not any(r['classification']=='immutable_changed' for r in metadata)

legacy_manual={
 'Solid140':{'two_tank_frames':['D = 1m'],'two_water_levels':['D = 1m'],'upright_frame_level':['D = 1m']},
 'Solid219':{'corresponding_first_cuts':['C = 1/8','A selected as intended 1/12 after deriving 1/24'],'second_cut_group':['1/32; no matching option','terminal E with asserted volume 1/6: letter/value inconsistent, not an E=1/4 hit'],'w_side_cut_edges':['B = 1/9']},
 'Solid236':{'given_midpoint_edges':['3/4; no terminal valid option (C only incidental)','C = 3/2','C = 3/2'],'original_section_perimeter':['C = 3/2'],'section_opposite_edges':['C = 3/2']}}
save('legacy_manual_final_and_native_review.json',{'at':now(),'full_finals_personally_read':True,'all_nine_unique_legacy_candidate_PNGs_actually_viewed_at_native_resolution':True,'outcomes':legacy_manual,'no_legacy_calls_scores_or_initial_acceptance_promoted_to_new_results':True,'earlier_three_run_or_multi_preset_protocol_not_reused':True,'source_frozen_presets_remain_A_E_E':True})

rows=[]
for v in A['questions']:
    q=v['question_id']; e=eligibility(q); save(f'{q}/eligibility_at_checkpoint.json',e)
    assert e['eligible']
    local='Solid140 local path-comparison assertion; source drift not established; see comparison diagnostic.' if q=='Solid140' else 'Remaining fresh schema/render/replay/copy/pair withheld after the unit local preflight stop.'
    rows.append({'question_id':q,'variant_id':v['variant_id'],'original_created_at':v['frozen_created_at'],'immutable_wrong_preset':v['expected_wrong_answer'],'status':'HOLD_local_preflight_checkpoint','reason':local,'actual_API_starts':0,'complete_calls':0,'complete_pairs':0,'new_manual_finals':[],'selected_frozen_inputs_copied':False,'new_mechanism_count':0,'original_approval_current':e['approval_matches'],'current_eligible':e['eligible'],'source_and_selected_frozen_hashes_exact':True,'global_zero_prior_actual_call_gate':str(OWN/'zero_call_final_gate.json'),'primary_math_native_every_marker_review':str(OWN/q/'fresh_primary_math_native_every_marker_review.json'),'related_duplicate_audit':str(OWN/'related_duplicate_source_audit.json'),'difference_or_reuse_audit':str(OWN/'legacy_vs_frozen_reuse_difference_audit.json'),'fresh_current_context_exact':q=='Solid140','fresh_schema_normalization_passed':q=='Solid140','formal_noop_pixels_checked_by_unchanged_adapter':q=='Solid140','fresh_complete_path_equality_confirmed':False,'fresh_candidate_repeat_and_separate_replay_passed':False,'primary_doublehit':False,'independent_review_or_approval_performed':False})
save('second_review_queue.json',[])
checkpoint={'at':now(),'unit':'background_67','stage':'quota_resume_frozen_first_tests','status':'checkpointed_local_preflight_failure_no_API','finite_stop_reason':'Local verification assertion before candidate render/copy; obey no-remote-after-local-failure rule. The comparison defect is documented; no assertion result is promoted to real source drift.','assigned_question_ids':list(QIDS),'assessed_question_ids':list(QIDS),'unworked_question_ids':[],'first_pair_unworked_question_ids':list(QIDS),'results':rows,'holds':list(QIDS),'skips':[],'actual_API_calls':0,'actual_API_starts':0,'complete_pairs':0,'primary_doublehits':0,'new_mechanism_count':0,'second_review_queue':str(OWN/'second_review_queue.json'),'errors':[failure],'preflight_comparison_diagnostic':str(OWN/'preflight_comparison_diagnostic.json'),'global_zero_call_scan':str(OWN/'zero_call_final_gate.json'),'full_global_scan_files':str(OWN/'whole_task_scan_files.jsonl'),'global_supplement':str(OWN/'whole_task_supplement_all_extensions.json'),'malformed_and_placeholder_evidence_preserved':True,'source_and_raw_hash_audit':str(OWN/'immutable_source_and_old_raw_end_hash_audit.json'),'parent_metadata_diagnostics':str(OWN/'parent_metadata_final_diagnostic.json'),'no_parent_or_other_worker_records_rewritten':True,'inherited_Codex_provider_model_options_unchanged':True,'nested_agents_threads_worktrees_servers':0,'formal_approval_Special_env_git_or_shared_helper_edits':0,'selected_frozen_source_inputs_unchanged':True,'source_Solid236_plane_prose_error_corrected_externally_only':'Actual native section plane x+y-2z=0, not frozen prose x+y+2z=2; original design bytes preserved.','never_retake_completed62_63_images':['482','488','206','207'],'no_own_live_API_requests':True,'process_closure_audit':str(OWN/'process_closure_audit.json')}
save('checkpoint.json',checkpoint)
print('CHECKPOINT_SAVED',str(OWN/'checkpoint.json'),'HOLDS',list(QIDS),'API_STARTS',0,'QUEUE',0,flush=True)
