from tools39 import *
import base64
manual=read(HERE/'manual_terminal_selections.json');cfg,ad=adapter();results=[];queue=[];allcalls=0;api_pids=[]
for q in ASSIGNED:
    es=eligibility(q);assert es['eligible'];write(HERE/q/'eligibility_final.json',es)
    initial=read(HERE/q/'input_fingerprints.json');current=inputs(ad,q);assert current==initial,(q,'formal input drift')
    if not list((HERE/q).glob('r39_*')):
        results.append(read(HERE/q/'assessment.json'));continue
    out=next((HERE/q).glob('r39_*'));design=read(out/'design.json');preset=str(design['expected_wrong_answer']);pr=read(out/'primary_review.json');rc=read(out/'render_check.json')
    invs=list(out.glob('tests/*/binding.json'));assert len(invs)==1;inv=invs[0].parent;b=read(inv/'binding.json');s=read(inv/'summary.json');req=read(inv/'request.json')
    checks={
      'same_frozen_PNG_byte_sha256':file_hash(out/'candidate.png')==b['image_sha256']==rc['png_sha256']==design['png_sha256'],
      'same_frozen_pixel_sha256':pixel_hash(out/'candidate.png')==b['pixel_sha256']==rc['pixel_sha256']==design['pixel_sha256'],
      'same_frozen_design_byte_sha256':file_hash(out/'design.json')==b['design_sha256']==rc['design_sha256']==file_hash(inv/'design_snapshot.json'),
      'frozen_snapshot_byte_equal':(out/'design.json').read_bytes()==(inv/'design_snapshot.json').read_bytes(),
      'frozen_preset_matches_both':preset==str(b['expected_wrong_answer'])==str(s['expected_wrong_answer']),
      'wrong_preset_is_not_original_answer':preset!=str(ad.records[q]['answer']),
      'exact_current_formal_question':b['question']==ad.records[q]['question']==req['messages'][1]['content'][0]['text'],
      'current_question_record_binding':b['question_record_sha256']==canonical_hash(ad.records[q]),
      'request_body_sha256':file_hash(inv/'request.json')==b['request_body_sha256'],
      'embedded_PNG_matches_frozen_bytes':base64.b64decode(req['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(out/'candidate.png').read_bytes(),
      'exact_system_profile':req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'} and req['messages'][0]=={'role':'system','content':b['system_prompt']},
      'no_token_limit_or_timeout_override':set(req)=={'model','stream','thinking','messages'} and req['stream'] is False,
      'no_intent_answer_or_parameter_leakage':len(req['messages'])==2 and req['messages'][1]['role']=='user' and len(req['messages'][1]['content'])==2 and set(req['messages'][1]['content'][0])=={'type','text'} and set(req['messages'][1]['content'][1])=={'type','image_url'},
      'unchanged_official_quick_test':b['reference_quick_test_sha256']==file_hash(ROOT/'PlaneGeometry/workbench/quick_test.py'),
      'exactly_two_start_files':len(list(inv.glob('run_*_started.json')))==2,
      'exactly_two_raw_responses':len(list(inv.glob('run_*_response.json')))==2,
      'two_complete_records':s['two_completed'] and len(s['results'])==2,
      'predeclared_design_and_difference_chronology':read(out/'design_difference_audit.json')['created_at']<=design['created_at']<b['created_at']<=s['results'][0]['started_at'],
      'no_op_formal_pixel_equality':rc['no_op_formal_pixel_equal'],
      'twice_byte_identical_draw':rc['twice_byte_identical_render'],
      'native_primary_review_before_calls':pr['proceed_to_API'] and pr['reviewed_at']<b['created_at']}
    assert all(checks.values()),(q,checks)
    runreviews=[]
    for k in [1,2]:
        rp=inv/f'run_{k:02d}_response.json';raw=read(rp);rr=read(inv/f'run_{k:02d}.json');msg=raw['choices'][0]['message']['content'];sel=manual[q][k-1]
        check={'status_completed':rr['status']=='completed','HTTP_200':rr['http_status']==200,'finish_stop':rr['finish_reason']==raw['choices'][0]['finish_reason']=='stop','not_truncated':not rr['truncated'],'answer_exact_full_raw':msg==rr['answer'],'response_hash':file_hash(rp)==rr['response_sha256'],'request_binding':rr['request_body_sha256']==b['request_body_sha256'],'image_binding':rr['image_sha256']==b['image_sha256'],'design_binding':rr['design_sha256']==b['design_sha256'],'model_profile':rr['response_model']=='mimo-v2.6-flash','nonthinking':not rr['thinking'] and raw['usage']['completion_tokens_details']['reasoning_tokens']==0}
        assert all(check.values()),(q,k,check)
        final=sel.get('letter') or str(sel['value']);hit=final==preset and not sel.get('contradictory_terminal_letter_value',False)
        runreviews.append({'run_index':k,'manual_final_answer':final,**sel,'preset_hit':hit,'full_raw_final_message':msg,'manually_read_entire_raw_response':True,'incidental_body_mentions_ignored':True,'raw_response_path':str(rp),'raw_response_sha256':file_hash(rp),'run_record_path':str(inv/f'run_{k:02d}.json'),'run_record_sha256':file_hash(inv/f'run_{k:02d}.json'),'started_at':rr['started_at'],'finished_at':rr['finished_at'],'complete_binding_checks':check})
    hits=all(r['preset_hit'] for r in runreviews);allcalls+=2;proc=read(out/'api_process.json');api_pids.append(proc['pid']);assert read(out/'api_process_finished.json')['two_completed']
    ev={'question_id':q,'variant_id':design['variant_id'],'reviewed_at':now(),'role':'Primary manual terminal-answer and evidence-binding audit','expected_wrong_answer':preset,'correct_answer':design['correct_answer'],'results':runreviews,'two_preset_hits':hits,'evidence_binding_checks':checks,'same_frozen_PNG_design_and_preset_both_calls':True,'exactly_two_real_calls':True,'no_retry_or_posthoc_relabel':True,'primary_review':str(out/'primary_review.json'),'delivery_status':'Possible only; parent NEW independent review required' if hits else 'MISS; not a candidate','control_status':'No matching prior original controls found; no new controls requested or run. No causal gain or mechanism confirmation claimed.'}
    write(out/'manual_final_review.json',ev)
    result={'question_id':q,'variant_id':design['variant_id'],'stage':'material_refinement','status':'primary_possibility_requires_NEW_review' if hits else 'tested_new_mechanism_MISS','design_count':1,'actual_calls':2,'expected_wrong_answer':preset,'manual_finals':[x['manual_final_answer'] for x in runreviews],'manual_final_values':[x['value'] for x in runreviews],'two_preset_hits':hits,'material_difference':design['material_difference'],'primary_unique_math_proof':design['primary_unique_math_proof'],'all_mark_roles_and_native_review':str(out/'primary_review.json'),'native_visibility_audit':str(HERE/'native_palette_audit.json'),'design_path':str(out/'design.json'),'candidate_path':str(out/'candidate.png'),'plugin_path':str(out/'plugin.json'),'difference_audit_path':str(out/'design_difference_audit.json'),'raw_evidence_dir':str(inv),'manual_review_path':str(out/'manual_final_review.json'),'current_eligibility':es,'frozen_formal_inputs_unchanged':True,'no_further_cosmetic_retry':'This specific meaningful hypothesis is exhausted by its exact frozen pair. Changing color, width or preset to an observed output would not be a new material mechanism.'}
    write(HERE/q/'assessment.json',result);results.append(result)
    if hits:queue.append(result)
hist=read(HERE/'history_read_audit.json');supp=read(HERE/'history_supplement_read_audit.json');pres={**hist['scoped_preexisting_hashes']}
for it in supp['old_question_JSON_raw_read']+supp['root_and_shared_helper_records']:pres[str(Path(it['path']).relative_to(ROOT))]=it['sha256']
immutable=[];diagnostic=[];drift=[]
for p,h in pres.items():
    f=ROOT/p;actual=file_hash(f) if f.exists() else None
    row={'path':p,'before_sha256':h,'after_sha256':actual,'unchanged':h==actual}
    if f.name in ['continuation_brief.txt','refinement_dispatch_20261102.json','exploration_report.json','remaining_questions.jsonl']:diagnostic.append(row)
    else:immutable.append(row)
    if h!=actual:drift.append(row)
assert not [r for r in immutable if not r['unchanged']],drift
write(HERE/'preservation_final.json',{'created_at':now(),'scoped_old_evidence_and_formal_source_checks':immutable,'all_scoped_immutable_files_unchanged':True,'diagnostic_mutable_runtime_metadata':diagnostic,'current8_formal_input_manifests_exact':True,'strict_own_root_write_guard':True,'no_shared_helper_or_main_ledger_write':True,'no_formal_approval_Pass_Collect_or_delivery':True,'no_whole_workspace_unchanged_claim':True})
write(HERE/'second_review_queue.json',{'created_at':now(),'stage':'material_refinement','unit':'background_39','candidates':queue,'candidate_count':len(queue),'requirement':'Parent must launch NEW independent second review for each possible candidate before any delivery; author did not independently second-review or Pass/Collect.','unqualified_misses_not_queued':True})
write(HERE/'checkpoint.json',{'created_at':now(),'status':'FINITE_BACKGROUND_39_COMPLETE','unit':'background_39','stage':'material_refinement','stop_reason':'All8 assigned refinement questions reasonably exhausted:6 substantive new mechanisms received exact2calls each,2 were skipped after explicit math/feature analysis. No cosmetic repetition or preset fishing.','actual_assessed_question_ids':ASSIGNED,'assessed_question_count':len(ASSIGNED),'unworked_question_ids':[],'new_design_count':6,'new_candidate_call_count':allcalls,'original_control_call_count':0,'completed_real_API_calls':allcalls,'credible_two_hit_possibilities':len(queue),'candidates':queue,'results':results,'API_errors':0,'aborted_calls':0,'retries':0,'local_audit_exception':'One read-only JSON scan encountered historical truncated Plane280 target_paths.failed_partial*.json. Both old raw files were subsequently read, hashed and preserved; the scanner was corrected without any solver retry. See history_supplement_read_audit.json.','historical_truncated_JSON_count':len(supp['historical_malformed_JSON']),'old_result_integrity':'Old Plane276 E72 preset with D60/D60 remains MISS. Old Plane280 A16 was rejected before API and not retested. New Plane276 C48/D60 is MISS againstE72; no posthoc preset changes.','API_process_PIDs':api_pids,'API_process_finished_records_all_complete':True,'no_own_live_API_processes_expected':True,'post_exit_process_audit_path':str(HERE/'process_exit_audit.json'),'own_output_root':str(HERE),'all_writes_and_caches_under_own_root':True,'formal_and_old_evidence_preservation':str(HERE/'preservation_final.json'),'full_history_and_objection_read':str(HERE/'history_supplement_read_audit.json'),'global_prior_binding_scan':str(HERE/'global_prior_binding_scan.json'),'native_math_audit':str(HERE/'supplemental_math_audit.json'),'actual_native_PNG_and_per_marker_review':[r['all_mark_roles_and_native_review'] for r in results if 'all_mark_roles_and_native_review' in r],'second_review_queue_path':str(HERE/'second_review_queue.json'),'no_Pass_Collect_approval_or_delivery_actions':True,'independent_second_review_performed_by_author':False,'source_question_and_presets_immutable':True})
print(json.dumps({'questions':8,'new_designs':6,'complete_real_calls':allcalls,'primary_possibilities':len(queue),'API_errors':0,'aborts':0,'retries':0,'all_scoped_old_and_formal_inputs_unchanged':True,'checkpoint':str(HERE/'checkpoint.json')},ensure_ascii=False))
