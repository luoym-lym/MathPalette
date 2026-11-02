from env42 import *
import base64
MANUAL={
'Plane413':('r42_partial_cell_unit_corner_transfer',['5.5','14.5'],[False,False],['First response ends5.5.','Second response earlier states17, then retracts its geometry and ends14.5. Incidental17 is not its final; no24 final.']),
'Plane418':('r42_local_corner_fit_to_area_bound_exact_edge_overlay',['4','5'],[False,True],['First response considers5 extensively but explicitly rejects it and ends4.','Second response falsely fits a T in a1x4 strip and ends5; exactly one target hit.']),
'Plane420':('r42_reflected_corner_triangle_families',['-4','-5 (or absolute5)'],[False,False],['First response counts3 triangles and ends-4.','Second response ends-5 with parenthetical absolute5. Its terminal convention is ambiguous, but neither value is preset1; cannot count as target hit.']),
'Plane470':('r42_parallel_column_endpoint_pairs',['20','18'],[False,False],['First forgets the2 horizontal collinear triples and ends20.','Second subtracts both horizontal rows and ends18; neither final is preset6.']),
'Plane478':('r42_crossed_subrectangle_ladder_binding',['13','5'],[False,False],['First uses an invalid6-region+7-composite enumeration and ends13.','Second misreads square/vertical overlap and ends5. Neither final is preset12.'])}
tested=[]
for q,(v,finals,hits,notes) in MANUAL.items():
    out=HERE/q/v;d=read(out/'design.json');invocations=list((out/'tests').glob('quicktest3_*'));assert len(invocations)==1;ev=invocations[0]
    b=read(ev/'binding.json');summ=read(ev/'summary.json');req=read(ev/'request.json')
    assert b['requested_runs']==2 and summ['two_completed'] and len(summ['results'])==2
    assert file_hash(out/'candidate.png')==b['image_sha256'] and file_hash(out/'design.json')==b['design_sha256']
    assert (ev/'design_snapshot.json').read_bytes()==(out/'design.json').read_bytes()
    assert file_hash(ev/'request.json')==b['request_body_sha256']
    assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'} and req['stream'] is False
    assert set(req)=={'model','stream','thinking','messages'}
    assert req['messages'][0]=={'role':'system','content':b['system_prompt']}
    content=req['messages'][1]['content'];assert len(content)==2 and content[0]=={'type':'text','text':b['question']}
    embedded=base64.b64decode(content[1]['image_url']['url'].split(',',1)[1]);assert embedded==(out/'candidate.png').read_bytes()
    e=eligibility(q);assert e['eligible'] and e['formal_record']['question']==b['question'] and canonical_hash(e['formal_record'])==b['question_record_sha256']
    assert d['expected_wrong_answer']==b['expected_wrong_answer'] and str(d['expected_wrong_answer'])!=str(e['formal_record']['answer'])
    reports=[];rawpaths=[]
    for i in (1,2):
        p=ev/f'run_{i:02d}_response.json';raw=read(p);run=read(ev/f'run_{i:02d}.json');start=read(ev/f'run_{i:02d}_started.json')
        assert raw['model']=='mimo-v2.6-flash' and raw['choices'][0]['finish_reason']=='stop'
        assert run['status']=='completed' and run['http_status']==200 and run['response_sha256']==file_hash(p)
        assert raw['usage']['completion_tokens_details']['reasoning_tokens']==0
        for key in ('request_body_sha256','image_sha256','design_sha256'):assert run[key]==start[key]==b[key]
        assert out.joinpath('design.json').stat().st_mtime<ev.joinpath(f'run_{i:02d}_started.json').stat().st_mtime
        reports.append({'run_index':i,'entire_raw_provider_response_manually_read':True,'full_final_text':raw['choices'][0]['message']['content'],'manually_identified_terminal_answer':finals[i-1],'matches_predeclared_wrong_answer':hits[i-1],'interpretation':notes[i-1],'raw_response_path':str(p),'raw_response_sha256':file_hash(p),'run_record_sha256':file_hash(ev/f'run_{i:02d}.json'),'started_at':start['started_at'],'finished_at':run['finished_at'],'complete_stop_response':True})
        rawpaths.append(str(p))
    manual={'question_id':q,'variant_id':v,'created_at':now(),'expected_wrong_answer':d['expected_wrong_answer'],'formal_correct_answer':e['formal_record']['answer'],'manual_final_answers':finals,'target_hits':sum(hits),'two_predeclared_target_hits':all(hits),'all_raw_full_texts_manually_read':True,'results':reports,'no_incidental_mention_as_final':True,'no_preset_or_image_edited_after_calls':True,'no_retry_or_success_sample_selection':True}
    write(out/'manual_final_review.json',manual)
    frozen_files={str(p.relative_to(out)):file_hash(p) for p in out.rglob('*') if p.is_file() and p.name not in ('context.json','render_check.json')}
    write(out/'frozen_evidence_audit.json',{'question_id':q,'variant_id':v,'created_at':now(),'exact_frozen_binding':b,'candidate_request_png_bytes_identical':True,'only_formal_question_and_candidate_PNG_in_solver_user_input':True,'correct_answer_preset_intent_parameters_original_comparison_absent_from_request':True,'exactly_two_calls_and_complete_stop_responses':True,'unchanged_reference_harness_sha256':file_hash(BASE/'harness/quicktest3_isolated.py'),'own_harness_copy_sha256':file_hash(HERE/'harness/quicktest3_isolated.py'),'preset_design_precedes_both_calls':True,'all_local_frozen_evidence_hashes':frozen_files,'manual_review':manual,'timestamp_limit':'Local file times and storedUTC chronology are internal evidence, not a trusted external timestamp or exhaustive provider invocation ledger.'})
    tested.append({'question_id':q,'variant_id':v,'candidate_directory':str(out),'expected_wrong_answer':d['expected_wrong_answer'],'formal_correct_answer':e['formal_record']['answer'],'manual_final_answers':finals,'target_hits':sum(hits),'two_hits':all(hits),'binding':b,'request_path':str(ev/'request.json'),'raw_response_paths':rawpaths,'manual_review_path':str(out/'manual_final_review.json'),'primary_review_path':str(out/'primary_review.json'),'difference_audit_path':str(out/'design_difference_audit.json'),'exact_evidence_audit_path':str(out/'frozen_evidence_audit.json'),'png_sha256':b['image_sha256'],'design_sha256':b['design_sha256']})
assert not any(t['two_hits'] for t in tested)
old_changes=[];old_count=0;relevant={};broad_changes=[];all_saved={}
for q in ASSIGNED:
    inventory=read(HERE/q/'prior_history_inventory.json')
    for rel,old in inventory['scoped_prior_files'].items():
        old_count+=1;actual=file_hash(ROOT/rel) if (ROOT/rel).exists() else None
        if actual!=old:old_changes.append({'path':rel,'before':old,'current':actual})
    start=read(HERE/q/'input_fingerprints.json');e=read(HERE/q/'eligibility_start.json');r=e['formal_record']
    important={str(Path('PlaneGeometry')/p) for p in [r['image'],r['scene'],r['script'],r['original_image'],*r.get('runtime_dependencies',[])] if p}
    for rel,h in start['files'].items():
        all_saved.setdefault(rel,h)
        if rel in important or rel.startswith(('PlaneGeometry\\workbench\\','dataset_tools\\')) or rel in ('MATHPALETTE_PROTOCOL.md','PlaneGeometry\\REDRAW_PROTOCOL.md','PlaneGeometry\\dataset_generator\\protocol.json'):
            relevant[rel]=h
current_hashes={rel:file_hash(ROOT/rel) if (ROOT/rel).exists() else None for rel in all_saved}
for rel,old in all_saved.items():
    if current_hashes[rel]!=old:broad_changes.append({'path':rel,'before':old,'current':current_hashes[rel],'scope':'relevant_frozen_input' if rel in relevant else 'other_adapter_manifest_input_external_drift'})
relevant_changes=[c for c in broad_changes if c['scope']=='relevant_frozen_input']
assert not old_changes and not relevant_changes,(old_changes,relevant_changes)
current=[eligibility(q) for q in ASSIGNED];assert all(e['eligible'] for e in current)
for e in current:
    assert e['approval']==read(HERE/e['question_id']/'eligibility_start.json')['approval']
    write(HERE/e['question_id']/'eligibility_final.json',e)
source={'created_at':now(),'stage':'material_refinement','all8_currently_eligible_and_original_user_content_fingerprints_valid':True,'current_authoritative_eligibility':current,'prior_scoped_evidence_files_checked':old_count,'prior_evidence_changes':old_changes,'relevant_frozen_source_file_count':len(relevant),'relevant_frozen_source_changes':relevant_changes,'all_adapter_manifest_files_checked':len(all_saved),'other_adapter_manifest_changes':broad_changes,'all_new_explicit_writes_under':str(HERE),'strict_own_directory_guard_before_project_imports':True,'TEMP_TMP_TMPDIR_MPLCONFIGDIR_XDG_CACHE_HOME_inside_own_root':True,'shared_renderers_helpers_harness_not_modified':True,'formal_approval_Pass_Collect_publication_actions':False,'no_whole_workspace_unchanged_claim':True,'external_unrelated_changes_policy':'Preserved; no reset/checkout/revert/cleanup/rebuild or historical metadata fingerprint rewrite.','own_API_process_records':[read(HERE/t['question_id']/t['variant_id']/'api_process_finished.json') for t in tested]}
write(HERE/'source_preservation_audit.json',source)
queue={'unit':'background_42','stage':'material_refinement','created_at':now(),'candidate_count':0,'question_ids':[],'candidates':[],'actual_assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'required_next_action':'No candidate qualifies for independent second review in this finite unit. Any future materially new exact two-hit design must receive a NEW parent independent review.','approval_status':'No independent second review, Pass, Collect, original approval or publication performed.'}
write(HERE/'second_review_queue.json',queue)
checkpoint={'unit':'background_42','stage':'material_refinement','status':'complete_finite_assigned_unit','finished_at':now(),'stop_reason':'All8 assigned questions reasonably exhausted; no external failure and no quota/cost stop.','actual_assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'new_substantive_design_count':5,'new_frozen_tested_PNG_count':5,'local_render_only_failed_drafts':2,'completed_candidate_pairs':5,'actual_API_call_count':10,'complete_stop_response_count':10,'possible_candidate_count':0,'API_errors':0,'API_aborts':0,'API_retries':0,'new_original_control_calls':0,'prior_original_controls':'Global same-question binding scan found none; no original control was repeated or newly required. No causal gain or statistically reliable efficacy claimed.','native_source_JPEG_formal_PNG_and_all5_old_design_PNGs_actually_viewed':True,'all10_old_raw_full_responses_manually_read':True,'all10_new_raw_full_responses_manually_read':True,'fresh_noop_formal_pixel_equality_count':8,'schema_normalized_and_twice_same_bytes_candidate_count':5,'tested_new_designs':tested,'screened_without_new_frozen_design':[read(HERE/q/'refinement_prescreen.json') for q in ['Plane451','Plane459','Plane485']],'local_implementation_failure_evidence':str(HERE/'Plane418/local_render_failures.json'),'source_preservation_audit':str(HERE/'source_preservation_audit.json'),'global_prior_same_question_inventory':str(HERE/'global_prior_same_question_inventory.json'),'second_review_queue':str(HERE/'second_review_queue.json'),'no_original_data_or_prior_evidence_altered':True,'process_status':'All5 ownAPI run wrappers returned normally and saved finish records; external exact PID/command read-only check saved separately before handback. No termination needed.','no_nested_agent_T3_thread_worktree':True,'no_independent_self_review_or_delivery_or_Pass_Collect':True}
write(HERE/'checkpoint.json',checkpoint)
print(json.dumps({'assessed':8,'new_designs':5,'complete_calls':10,'candidates':0,'old_files_checked':old_count,'relevant_source_files':len(relevant),'source_changes':len(relevant_changes),'prior_evidence_changes':len(old_changes)},ensure_ascii=False))
