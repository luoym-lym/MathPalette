from tools45 import *
import base64,io
from PIL import Image
import numpy as np
manual={
 'Solid81':{'finals':['C','A'],'notes':['Final C is wrong but misses frozen A. It wrongly claims the remaining row/column in a2x2 slab is disconnected and incorrectly accepts B.','Final A matches frozen A. It wrongly treats the three-cube column as impossible and accepts overlapping dominoes for B; actual A matching is horizontal base+upper vertical pair.']},
 'Solid97':{'finals':['D','B'],'notes':['Final D is explicit; misses frozen B. It misreads left-die pip values, calls a valid die nonstandard and chooses a closest altered option. No values or choice text were changed in the request.','Complete long final B=only2 matches frozen B. Many earlier contradictory trial values are superseded by the consistent terminal B/2. It repeatedly miscounts left top2 as3, then assumes a standard chirality; no mechanism/causality claim is supported.']},
 'Solid108':{'finals':['B','D'],'notes':['Final B misses frozen C. It skips the blank adjacent triangle and invents a two-roll return.','Final D misses frozen C. It skips the blank triangle and assumes a universal four-face rolling cycle. Actual route has6rolls and first return E.']}
}
assessed=[];testresults=[];preserve={};elig=[]
for q in IDS:
    before=read(TASK/q/'frozen_inputs.json');after=frozen(q)
    assert before==after,(q,'source changed')
    e=eligibility(q);assert e['eligible'];write(TASK/q/'eligibility_at_end.json',e);elig.append(e)
    preserve[q]={'all_exact_relevant_source_hashes_match_start':True,'question_record_hash_matches':True,'file_count':len(after['files']),'current_approval_content_sha256':e['current_content_sha256'],'user_approved_at_utc':e['approval']['approved_at_utc'],'baseline_no_op_pixels_equal':True}
    row={'question_id':q,'math_audit':str(TASK/'independent_primary_math_audit.json'),'source_context_audit':str(TASK/q/'source_context_audit.json'),'current_eligible':True}
    if q not in manual:
        row.update(status='assessed_no_clean_new_design',api_calls=0,prescreen=str(TASK/q/'material_refinement_prescreen.json'))
        assessed.append(row);continue
    f=next(p.parent for p in (TASK/q).glob('r45_*/process_completed.json'))
    completed=read(f/'process_completed.json');d=Path(completed['evidence_dir']);binding=read(d/'binding.json');design=read(f/'design.json');plugin=read(f/'plugin.json')
    png=(f/'candidate.png').read_bytes();reqbytes=(d/'request.json').read_bytes();req=read(d/'request.json')
    assert binding['image_sha256']==hashlib.sha256(png).hexdigest()
    assert binding['design_sha256']==file_hash(f/'design.json')==file_hash(d/'design_snapshot.json')
    assert binding['request_body_sha256']==hashlib.sha256(reqbytes).hexdigest()
    assert binding['expected_wrong_answer']==design['expected_wrong_answer']
    assert req['model']=='mimo-v2.6-flash' and req['thinking']=={'type':'disabled'}
    assert set(req)=={'model','stream','thinking','messages'} and req['stream'] is False
    assert req['messages'][0]=={'role':'system','content':binding['system_prompt']}
    user=req['messages'][1];assert user['content'][0]=={'type':'text','text':AD.records[q]['question']}
    assert base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])==png
    assert len(req['messages'])==2 and len(user['content'])==2
    assert len(list(d.glob('run_*_started.json')))==2 and len(list(d.glob('run_*_response.json')))==2
    assert not list(d.glob('*incomplete*'))
    entries=[]
    for i,ans in enumerate(manual[q]['finals'],1):
        p=d/f'run_{i:02d}_response.json';raw=read(p);run=read(d/f'run_{i:02d}.json');start=read(d/f'run_{i:02d}_started.json');msg=raw['choices'][0]['message']['content']
        assert run['status']=='completed' and raw['choices'][0]['finish_reason']=='stop' and run.get('truncated') is False
        assert run['image_sha256']==binding['image_sha256'] and run['design_sha256']==binding['design_sha256'] and run['request_body_sha256']==binding['request_body_sha256']
        assert run['response_sha256']==file_hash(p) and start['run_id']==run['run_id']
        entries.append({'run_index':i,'raw_response_path':str(p),'raw_response_sha256':file_hash(p),'complete_final_text':msg,'entire_response_manually_read':True,'hand_read_final_answer':ans,'hand_read_choice_value':('only2' if q=='Solid97' and ans=='B' else None),'matches_immutable_predeclared_wrong_answer':ans==design['expected_wrong_answer'],'terminal_choice_value_contradiction':False,'narrative_limit':manual[q]['notes'][i-1],'status':run['status'],'finish_reason':raw['choices'][0]['finish_reason'],'elapsed_seconds':run['elapsed_seconds'],'started_at':start['started_at'],'finished_at':run['finished_at']})
    pair=all(x['matches_immutable_predeclared_wrong_answer'] for x in entries)
    assert pair is False
    write(f/'manual_final_review.json',{'question_id':q,'variant_id':design['variant_id'],'frozen_expected_wrong_answer':design['expected_wrong_answer'],'correct_answer':AD.records[q]['answer'],'same_exact_png_both_calls':True,'calls_exactly2':True,'all_manual_final_results':entries,'two_hits':False,'disposition':'complete_pair_preset_missed','no_preset_relabeling_or_repeat':True,'primary_only':True})
    hashes={str(p.relative_to(TASK)):file_hash(p) for p in d.iterdir() if p.is_file()}
    hashes.update({str((f/n).relative_to(TASK)):file_hash(f/n) for n in ['design.json','plugin.json','candidate.png','design_difference_audit.json','context.json','render_check.json','pretest_visual_review.json','pretest_freeze.json','manual_final_review.json']})
    write(f/'evidence_binding_audit.json',{'question_id':q,'variant_id':design['variant_id'],'audited_at':now(),'exact_source_record_and_current_approval_verified':True,'exact_raw_request_question_image_only':True,'no_correct_answer_preset_intent_parameters_or_original_image_sent':True,'unchanged_harness_source':file_hash(SHARED/'harness/quicktest3_isolated.py'),'profile_model_thinking_system_prompt_unchanged':True,'no_timeout_max_tokens_override_no_retry':True,'same_design_png_request_binding_for_both_completed_calls':True,'exactly2starts2complete_responses_no_partial_or_error':True,'pretest_freeze_files_still_match':all(file_hash(f/n)==h for n,h in read(f/'pretest_freeze.json')['files'].items()),'full_manual_finals':manual[q]['finals'],'two_hits':False,'files':hashes,'timestamp_limit':'Local timestamps and hashes establish internal binding chronology, not a provider-side exhaustive invocation ledger or trusted timestamp service.','control_status':'No prior original-control binding found for these assigned IDs; none repeated or newly called. Prior candidate pairs are not controls.','inference_limit':'Two observations do not establish mechanism, causal gain, statistical reliability or per-mark contribution. No gain/identical-narrative requirement is imposed.'})
    primary={'question_id':q,'variant_id':design['variant_id'],'role':'Primary researcher only; not an independent second review','unique_original_math':design['pretest_math_proof'],'marker_roles':design['pretest_marker_roles'],'material_difference':read(f/'design_difference_audit.json'),'native_visual_and_semantic_audit':str(f/'pretest_visual_review.json'),'pip_supplement':str(f/'pip_pixel_preservation.json') if (f/'pip_pixel_preservation.json').exists() else None,'actual_native_png_viewed':True,'legal_normalized_plugin_and_exact_replay':True,'full_manual_finals':manual[q]['finals'],'preset':design['expected_wrong_answer'],'credible_possible_candidate':False,'reason':'Frozen preset was not hit twice; preserve evidence, no promotion or posthoc relabel.','approval_status':'No original approval edit, SpecialPass/Collect, review API or publication.'}
    write(f/'primary_review.json',primary)
    row.update(status='complete_pair_preset_missed',variant_id=design['variant_id'],design_path=str(f/'design.json'),image_path=str(f/'candidate.png'),png_sha256=binding['image_sha256'],preset=design['expected_wrong_answer'],full_hand_read_finals=manual[q]['finals'],api_calls=2,raw_evidence=str(d),primary_review=str(f/'primary_review.json'),binding_audit=str(f/'evidence_binding_audit.json'))
    assessed.append(row);testresults.append(row)

history=read(TASK/'history_inventory_complete.json');changed=[];oldcount=0
for q,files in history.items():
    for entry in files:
        oldcount+=1
        if file_hash(entry['path'])!=entry['sha256']:changed.append(entry['path'])
assert not changed
write(TASK/'source_and_history_audit_final.json',{'checked_at':now(),'source_checks':preserve,'old_evidence_files_verified':oldcount,'old_evidence_hash_changes':changed,'original_approval_fingerprints_all8_match':True,'old_mutable_progress_snapshots_not_treated_as_geometry':True,'no_entire_workspace_unchanged_claim':True,'shared_runtime_helpers_read_only':True,'all_writes_guarded_inside_own_root':True})
write(TASK/'second_review_queue.json',{'unit':'background_45','stage':'material_refinement','created_at':now(),'candidates':[],'held_or_rejected_for_parent_information':[],'reason':'No new design has two complete finals hitting its immutable preset. No independent second review or delivery requested.','approval_status':'No Pass/Collect/formal approval/publication.'})
checkpoint={'unit':'background_45','stage':'material_refinement','status':'complete_assigned8_reasonably_exhausted','created_at':now(),'actual_assessed_question_ids':IDS,'unworked_question_ids':[],'question_count':8,'distinct_new_design_hypotheses':3,'tested_design_count':3,'saved_design_json_count':4,'saved_png_draft_count':4,'rejected_offline_draft_count':1,'actual_api_calls_started':6,'actual_api_calls_completed':6,'complete_same_image_pairs':3,'original_control_calls':0,'credible_possible_candidates':0,'second_review_queue':str(TASK/'second_review_queue.json'),'api_errors':0,'aborts':0,'retries':0,'local_preflight_failures':[{'question_id':'Solid81','type':'offline_guide_clearance_assertion','solver_calls':0,'evidence':str(TASK/'Solid81/r45_external_overlapping_domino_correspondence/preflight_rejection.json')},{'question_id':'Solid81','type':'runner_invoked_after_failed_quality_missing_freeze','solver_calls':0,'harness_not_imported_request_not_created':True}],'delayed_successful_call':{'question_id':'Solid97','run_index':2,'elapsed_seconds':254.406,'status':'completed_stop','no_abort_no_retry':True},'questions':assessed,'old_history_summary':{'Solid84_false_cross_pair':'presetE; full finalsC/C; miss','Solid84_symbol_similarity_capture':'presetA; full finalsE/window(D); miss','Solid98_front_row_color_correspondence':'presetB; full finalsD/A; miss','other6':'Original completed first-pass histories were prescreen-only, not assumed uncalled from missing mutable summaries. Actual question directories and root/worker checkpoints inspected.','old_malformed_or_truncated_json_in_assigned_evidence':[],'old_bytes_preserved':True},'mathematics':str(TASK/'independent_primary_math_audit.json'),'source_qualification_audits':str(TASK/'source_and_history_audit_final.json'),'native_render_checks':'Each tested design: fresh dedicatedMathVision adapter; actual PluginRenderer schema/default normalization; formal no-op pixels; two byte-identical renders; exact fullprecision object/path or anchor hashes; actual nativePNG viewing. Solid97 all16pip raster boxes additionally verified after capturepoint artist registry exposed0 artists.','process_status':'All three foreground run45 invocations returned exit0. External no-live-process check saved separately before handoff.','no_unrequested_hard_gates':'No gain/causal effect, identical narrative or arbitrary marker-count requirement used. Task-specific human physical-color ambiguity remains a gate.','formal_state':'Read only; no approvals/Pass/Collect/publication or shared ledger/helper edits.'}
write(TASK/'checkpoint.json',checkpoint)
print(json.dumps({k:checkpoint[k] for k in ['status','question_count','distinct_new_design_hypotheses','tested_design_count','actual_api_calls_completed','credible_possible_candidates','api_errors','aborts','retries']},ensure_ascii=False))
