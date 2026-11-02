from tools72 import *
import base64

variants={'Plane335':'r72_congruent_apex_wedge_binding','Plane355':'r72_width_to_fold_measurement_role'}
old_changes=[]
for row in read(HERE/'old_history_inventory.json'):
    p=Path(row['path'])
    if not p.is_file() or sha(p)!=row['sha256']:old_changes.append(str(p))
source60_changes=[]
for path,h in read(HERE/'source_unit60_complete_initial_hashes.json').items():
    p=Path(path)
    if not p.is_file() or sha(p)!=h:source60_changes.append(path)
source_audits={};results=[];evidence=[]
for q in IDS:
    initial=read(HERE/q/'source_hashes_initial.json')
    changes=[p for p,h in initial.items() if not (PROJECT/p).is_file() or sha(PROJECT/p)!=h]
    current=eligibility(q);write(HERE/q/'eligibility_final.json',current)
    source_audits[q]={'all_initial_frozen_sources_hash_exact':not changes,'changed_paths':changes,'current_approval_matches':current['approval_matches_current'],'eligible':current['eligible'],'initial_fingerprint':read(HERE/q/'eligibility_initial.json')['current_content_sha256'],'final_fingerprint':current['current_content_sha256']}
    if q not in variants:
        results.append({'question_id':q,'status':'reasoned_zero_call_skip','new_designs':0,'new_calls':0,'assessment':str(HERE/q/'assessment.json'),'math':str(HERE/q/'unique_math.json')});continue
    d=HERE/q/variants[q];t=next((d/'tests').glob('quicktest3_*'))
    design=read(d/'design.json');binding=read(t/'binding.json');summary=read(t/'summary.json');review=read(d/'manual_final_review.json')
    body=read(t/'request.json')
    assert set(body)=={'model','stream','thinking','messages'}
    assert body['model']=='mimo-v2.6-flash' and body['thinking']=={'type':'disabled'} and body['stream'] is False
    assert len(body['messages'])==2 and body['messages'][0]['role']=='system' and body['messages'][1]['role']=='user'
    assert body['messages'][0]['content']==binding['system_prompt']
    parts=body['messages'][1]['content'];assert len(parts)==2
    assert parts[0]=={'type':'text','text':current['record']['question']}
    png=base64.b64decode(parts[1]['image_url']['url'].split(',',1)[1])
    assert png==(d/'candidate.png').read_bytes()
    assert sha(d/'candidate.png')==binding['image_sha256']==design['candidate_sha256']
    assert sha(d/'design.json')==binding['design_sha256']==sha(t/'design_snapshot.json')
    assert sha(t/'request.json')==binding['request_body_sha256']
    assert binding['expected_wrong_answer']==design['expected_wrong_answer']==read(d/'wrong_preset.json')['expected_wrong_answer']
    assert sha(d/'plugin.json')==design['plugin_sha256']
    assert sha(d/'candidate.png')==sha(d/'repeat.png')==sha(d/'offline_replay.png')
    assert summary['two_completed'] and len(summary['results'])==2
    assert len(list(t.glob('run_*_started.json')))==2
    run_rows=[]
    for i in [1,2]:
        run=read(t/f'run_{i:02d}.json');start=read(t/f'run_{i:02d}_started.json');raw=read(t/f'run_{i:02d}_response.json')
        assert run['status']=='completed' and raw['choices'][0]['finish_reason']=='stop'
        assert run['response_sha256']==sha(t/f'run_{i:02d}_response.json')
        assert run['request_body_sha256']==start['request_body_sha256']==binding['request_body_sha256']
        assert run['image_sha256']==start['image_sha256']==binding['image_sha256']
        assert run['design_sha256']==start['design_sha256']==binding['design_sha256']
        assert raw['choices'][0]['message']['content']==review['complete_model_answers'][i-1]
        run_rows.append({'run':i,'status':run['status'],'started':str(t/f'run_{i:02d}_started.json'),'raw':str(t/f'run_{i:02d}_response.json'),'raw_sha256':sha(t/f'run_{i:02d}_response.json'),'final':review['manual_final_values'][i-1],'preset_hit':review['preset_hits'][i-1]})
    evidence.append({'question_id':q,'variant_id':variants[q],'request_only_formal_question_and_exact_frozen_PNG':True,'no_correct_answer_preset_intent_history_params_sent':True,'model_thinking_system_profile_unchanged':True,'no_token_or_timeout_override':True,'exactly_two_complete_actual_calls':True,'candidate_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'design_sha256':sha(d/'design.json'),'wrong_preset_sha256':sha(d/'wrong_preset.json'),'request_sha256':sha(t/'request.json'),'binding_sha256':sha(t/'binding.json'),'runs':run_rows,'manual_review':str(d/'manual_final_review.json'),'api_finished':read(d/'api_process_finished.json')})
    results.append({'question_id':q,'variant_id':variants[q],'status':'primary_double_hit_pending_NEW_parent_independent_review' if review['both_hit_preset'] else 'complete_first_pair_preset_missed','new_designs':1,'new_calls':2,'preset':design['expected_wrong_answer'],'manual_finals':review['manual_final_values'],'preset_hits':review['preset_hits'],'design':str(d/'design.json'),'evidence_dir':str(t)})
    del body,parts,png,raw;gc.collect()

meta=[]
for row in read(HERE/'initial_snapshot_manifest.json'):
    p=Path(row['source'])
    if p.parent==BASE and p.name in ['continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json']:
        old=Path(row['snapshot']).read_bytes();new=p.read_bytes()
        meta.append({'source':str(p),'original_full_snapshot':row['snapshot'],'original_sha256':row['sha256'],'current_sha256':sha(p),'unchanged':old==new,'exact_old_prefix_of_current':new.startswith(old),'classification':'unchanged' if old==new else ('exact-prefix parent append; diagnostic' if new.startswith(old) else 'parent runtime update; diagnostic only'),'historical_snapshots_never_rewritten':True})
        del old,new;gc.collect()
for p in (BASE/'background_60/readin_snapshots').glob('*'):
    for name in ['continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json']:
        if p.name.startswith(name+'.'):
            old=p.read_bytes();new=(BASE/name).read_bytes()
            meta.append({'source60_original_snapshot':str(p),'old_sha256':sha(p),'current_source':str(BASE/name),'current_sha256':sha(BASE/name),'exact_old_prefix_of_current':new.startswith(old),'classification':'unchanged' if old==new else ('exact-prefix parent append; diagnostic' if new.startswith(old) else 'parent runtime update; diagnostic only'),'historical_snapshot_never_rewritten':True})
            del old,new;gc.collect()
write(HERE/'parent_metadata_diagnostic_final.json',meta)
write(HERE/'source_and_old_evidence_final_audit.json',{'source_audits':source_audits,'old_evidence_files_checked':len(read(HERE/'old_history_inventory.json')),'old_evidence_changes':old_changes,'entire_source60_files_checked':len(read(HERE/'source_unit60_complete_initial_hashes.json')),'source60_changes':source60_changes,'no_frozen_source_evidence_restoration_or_rewrite':True,'scope':'Scoped formal/protocol/helper inputs and named prior evidence; no whole-workspace unchanged claim.'})
assert not old_changes and not source60_changes and all(not a['changed_paths'] and a['current_approval_matches'] and a['eligible'] for a in source_audits.values())
write(HERE/'evidence_binding_audit.json',evidence)
write(HERE/'tool_diagnostics.json',{'allocation_import_render_failures':[],'remote_API_errors':[],'incomplete_or_aborted_calls':[],'nonblocking_audit_command_diagnostics':[{'action':'rg search wrote all_reference_paths.txt within the searched tree','observation':'rg emitted a sharing violation for its own newly written output file. Source search output was preserved; no source file was written. Later explicit per-file JSON/request inventories provide relevant evidence.','external_or_render_failure':False},{'action':'CIM query after Plane335 already exited, piped empty results into JSON writer then attempted Get-Content','observation':'No rows meant no output file was created; Get-Content reported the absent own audit path. The subsequent explicit empty-array process_check_after_335.json records count0. No process was terminated or retried.','external_or_render_failure':False}],'API_retry_count':0,'stalled_process_terminations':0})
queue=[r for r in results if r['status'].startswith('primary_double_hit')]
write(HERE/'second_review_queue.json',{'unit':'background_72','created_at':now(),'primary_candidates':queue,'count':len(queue),'NEW_independent_parent_review_required_before_any_delivery':True,'self_independent_review_or_user_approval':False})
write(HERE/'checkpoint.json',{'unit':'background_72','stage':'material_refinement','finished_at':now(),'scope':IDS,'actual_assessed_question_ids':IDS,'unworked_question_ids':[],'results':results,'new_design_count':2,'actual_candidate_calls':4,'complete_pairs':2,'primary_double_hits':len(queue),'reasoned_zero_call_skips':['Plane365','Plane386'],'finite_stop_reason':'All four assigned IDs assessed, first pairs or reasoned pre-call skips completed.','source_eligibility_and_approval_audit':str(HERE/'source_and_old_evidence_final_audit.json'),'full_manual_finals_and_request_raw_binding_audit':str(HERE/'evidence_binding_audit.json'),'all_history_inventory':str(HERE/'old_history_inventory.json'),'old_actual_raw_binding_audit':str(HERE/'old_actual_request_binding_audit.json'),'historic_exact_new_PNG_request_scan':str(HERE/'historic_exact_PNG_request_scan.json'),'mutable_parent_snapshot_diagnostics':str(HERE/'parent_metadata_diagnostic_final.json'),'semantics_lessons_read':['annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json','cited Plane295/342/242 actual independent objections'],'native_checks':'Actual source JPG, full native formal PNG and both new native candidate PNGs manually viewed; all four no-op baselines pass, both candidates repeat byte-identically and replay exactly in fresh processes.','math_corrections':['Plane365 has three gray exposed components, not merely two; total gray G=1 and white double overlap O=1 prove S=3.','Plane386 static final-packing lower bound strengthens old grid-slide BFS for continuous translations with axis orientations; explicit three-distinct-bar sliding construction saved.'],'errors_and_process_diagnostics':str(HERE/'tool_diagnostics.json'),'own_API_process_finished_records':[str(HERE/q/v/'api_process_finished.json') for q,v in variants.items()],'process_closure':'API calls finished normally; final exact own-PID/command CIM closure snapshot is written after this audit process exits.','no_controls_retests_profile_changes_or_approval_actions':True,'no_formal_Special_env_git_dotruntime_or_prior_unit_writes':True,'all_new_files_only_OWNROOT':str(HERE),'no_nested_agents_threads_worktrees_servers':True,'limitations':['Primary exploration only. No user approval, independent review, Pass, Collect, delivery or publication.','Wrong answers missing their own immutable preset remain misses; no preset changes or outcome relabeling.','No statistical causal gain, original-control correctness or human-study claim.']})
print(json.dumps({'results':results,'primary_candidates':len(queue),'source_and_old_evidence_exact':True},ensure_ascii=False),flush=True)
