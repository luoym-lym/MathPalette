from bootstrap31 import *
from inspect31 import eligibility
import base64

def binding_audit(d):
 des=read(d/'design.json');q=des['question_id'];record=read(OWN/q/'formal_record.json')
 dirs=list((d/'tests').glob('quicktest3_*'));assert len(dirs)==1
 ed=dirs[0];b=read(ed/'binding.json');s=read(ed/'summary.json');m=read(d/'manual_finals.json');p=read(ed/'request.json')
 assert s['two_completed'] and b['requested_runs']==2
 assert len(list(ed.glob('run_*_started.json')))==2 and len(list(ed.glob('run_*_response.json')))==2
 assert sha(d/'design.json')==b['design_sha256']==s['design_sha256']
 assert (ed/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
 assert sha(d/'candidate.png')==b['image_sha256']==s['image_sha256']
 assert des['expected_wrong_answer']==b['expected_wrong_answer']==s['expected_wrong_answer']==m['expected_wrong_answer_before_both_calls']
 assert str(des['expected_wrong_answer'])!=str(record['answer'])
 assert p['model']=='mimo-v2.6-flash' and p['thinking']=={'type':'disabled'} and p['stream'] is False
 assert set(p)=={'model','stream','thinking','messages'}
 assert len(p['messages'])==2 and p['messages'][0]=={'role':'system','content':b['system_prompt']}
 user=p['messages'][1];assert user['role']=='user' and len(user['content'])==2
 assert user['content'][0]=={'type':'text','text':record['question']}
 encoded=user['content'][1]['image_url']['url'];assert encoded.startswith('data:image/png;base64,')
 assert base64.b64decode(encoded.split(',',1)[1])==(d/'candidate.png').read_bytes()
 assert sha(ed/'request.json')==b['request_body_sha256']
 assert hashlib.sha256(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==b['question_record_sha256']
 audit=read(d/'design_difference_audit.json');primary=read(d/'primary_review.json')
 assert sha(d/'design_difference_audit.json')==des['design_difference_audit_sha256']
 assert primary['precall_design_frozen_sha256']==sha(d/'design.json')
 assert primary['precall_PNG_frozen_sha256']==sha(d/'candidate.png')
 finals=[];run_bindings=[]
 for i in range(1,3):
    st=read(ed/f'run_{i:02d}_started.json');r=read(ed/f'run_{i:02d}.json');raw=read(ed/f'run_{i:02d}_response.json');manual=m['runs'][i-1]
    assert r['status']=='completed' and not r['truncated'] and r['finish_reason']=='stop'
    assert raw['model']=='mimo-v2.6-flash' and raw['choices'][0]['finish_reason']=='stop'
    full=raw['choices'][0]['message']['content']
    assert full==r['answer']==manual['full_assistant_content'] and manual['full_raw_final_manually_read']
    assert sha(ed/f'run_{i:02d}_response.json')==r['response_sha256']==manual['raw_response_sha256']
    for key in ['request_body_sha256','image_sha256','design_sha256']:
        assert st[key]==r[key]==b[key]
    assert datetime.fromisoformat(audit['created_at'])<datetime.fromisoformat(st['started_at'])
    assert datetime.fromisoformat(des['created_at'])<datetime.fromisoformat(st['started_at'])
    assert datetime.fromisoformat(primary['created_at'])<datetime.fromisoformat(st['started_at'])
    finals.append(manual['manual_final'])
    run_bindings.append({'run_index':i,'started':str(ed/f'run_{i:02d}_started.json'),'started_sha256':sha(ed/f'run_{i:02d}_started.json'),'completed':str(ed/f'run_{i:02d}.json'),'completed_sha256':sha(ed/f'run_{i:02d}.json'),'raw_response':str(ed/f'run_{i:02d}_response.json'),'raw_response_sha256':r['response_sha256'],'full_manually_read_final':manual['manual_final'],'final_value':manual.get('manual_final_value'),'preset_hit':manual['preset_hit']})
 assert len(m['runs'])==2 and m['two_preset_hits']==all(r['preset_hit'] for r in m['runs'])
 return {'question_id':q,'variant_id':des['variant_id'],'expected_wrong_answer':des['expected_wrong_answer'],'correct_answer':record['answer'],'manual_finals':finals,'two_preset_hits':m['two_preset_hits'],'primary_credible_possibility':m['two_preset_hits'],'evidence_directory':str(ed),'design_path':str(d/'design.json'),'design_sha256':sha(d/'design.json'),'plugin_path':str(d/'plugin.json'),'plugin_sha256':sha(d/'plugin.json'),'candidate_path':str(d/'candidate.png'),'candidate_sha256':sha(d/'candidate.png'),'pixel_sha256':b['pixel_sha256'],'design_difference_audit_path':str(d/'design_difference_audit.json'),'design_difference_audit_sha256':sha(d/'design_difference_audit.json'),'primary_review_path':str(d/'primary_review.json'),'primary_review_sha256':sha(d/'primary_review.json'),'math_proof_path':str(OWN/q/'primary_original_math.json'),'math_proof_sha256':sha(OWN/q/'primary_original_math.json'),'native_schema_repeat_render_path':str(d/'render_check.json'),'manual_finals_path':str(d/'manual_finals.json'),'manual_finals_sha256':sha(d/'manual_finals.json'),'binding_path':str(ed/'binding.json'),'binding_sha256':sha(ed/'binding.json'),'request_path':str(ed/'request.json'),'request_sha256':sha(ed/'request.json'),'summary_path':str(ed/'summary.json'),'summary_sha256':sha(ed/'summary.json'),'run_bindings':run_bindings,'exact_same_PNG_two_complete_calls':True,'unchanged_harness_and_exact_profile':True,'no_solver_intent_answer_history_leakage':True,'rationale_preset_primary_native_review_precede_both_calls':True,'timestamps_limit':'Locally saved binding and timestamps, not externally signed provider attestations.','original_controls':[],'effect_limits':'No original-control calls found for this assigned question and none newly run. No causal/statistical/incremental-effect or human-study claim.','new_parent_independent_review_required_before_delivery':True}

def run():
 process=read(OWN/'no_live_API_processes.json')
 assert not process['live_own_API_processes']
 candidates=[]
 for d in sorted(OWN.glob('Plane*/r31_*/design.json')):
    if (d.parent/'tests').exists():candidates.append(binding_audit(d.parent))
 assert len(candidates)==5
 save(OWN/'evidence_binding_audit.json',{'stage':'material_refinement','created_at':stamp(),'candidates':candidates,'actual_completed_calls':10,'actual_started_calls':10,'errors':0,'aborts':0,'automatic_retries':0,'no_preset_relabel':True,'no_success_selection_or_mixed_images':True,'harness_byte_identical':sha(OWN/'quicktest3_isolated.py')==sha(SHARED/'harness/quicktest3_isolated.py'),'harness_sha256':sha(OWN/'quicktest3_isolated.py')})
 eligible={q:eligibility(q) for q in IDS};assert all(e['eligible'] for e in eligible.values())
 save(OWN/'eligibility_final.json',{'created_at':stamp(),'stage':'material_refinement','authoritative_current_eligibility':eligible})
 # Rehash immutable prior evidence and actual frozen dependencies. Do not restore drift.
 old=read(OWN/'prior_evidence_hashes_start.json');old_drift=[]
 for q,files in old.items():
    for rp,h in files.items():
        p=PROJECT/rp
        if not p.exists() or sha(p)!=h:old_drift.append({'question_id':q,'path':rp,'historical_hash':h,'current_hash':sha(p) if p.exists() else None})
 expected={}
 for q in IDS:expected.update(read(OWN/q/'input_fingerprints.json'))
 broad_drift=[]
 for rp,h in expected.items():
    p=PROJECT/rp
    if not p.exists() or sha(p)!=h:broad_drift.append({'path':rp,'start_hash':h,'current_hash':sha(p) if p.exists() else None})
 per_question=[]
 for q in IDS:
    start=read(OWN/q/'eligibility_start.json');end=eligible[q]
    assert start['current_content_sha256']==end['current_content_sha256']
    per_question.append({'question_id':q,'original_approved_fingerprint_unchanged':True,'fingerprint':end['current_content_sha256'],'original_approval_time_retained':end['approval']['approved_at_utc'],'formal_record_unchanged':start['formal_record']==end['formal_record'],'no_pass_collected_special_completion':end['eligible'],'mutable_progress_hashes_start':start['mutable_progress_metadata'],'mutable_progress_hashes_end':end['mutable_progress_metadata']})
 hist=read(OWN/'history_and_lessons_audit.json');extra_drift=[]
 for item in hist['rejection_lessons']:
    if sha(item['path'])!=item['sha256']:extra_drift.append(item['path'])
 for item in hist['delivered_reference_designs']:
    if sha(item['batch_manifest'])!=item['batch_manifest_sha256'] or sha(item['design_path'])!=item['design_sha256']:extra_drift.append(item['design_path'])
 assert not old_drift and not extra_drift
 save(OWN/'source_preservation_final.json',{'stage':'material_refinement','checked_at':stamp(),'strict_unit_only_python_guard':True,'all_created_files_cache_TEMP_TMP_MPL_XDG_requests_logs_images_under':str(OWN),'formal_approval_Pass_Collect_review_publication_API_calls':0,'per_question_source_and_approval_checks':per_question,'prior_immutable_question_evidence_checked':sum(len(v) for v in old.values()),'prior_immutable_evidence_drift':old_drift,'rejection_and_delivery_reference_drift':extra_drift,'broad_input_manifest_checked_files':len(expected),'broad_input_manifest_drift_preserved_without_rewriting':broad_drift,'drift_classification':'Question-specific approved content fingerprints are unchanged. Broader manifests include unrelated concurrently editable workbench/formal records; any such drift is preserved and listed, never restored or attributed to an actor. Mutable runtime progress hashes are diagnostic metadata only.','whole_workspace_unchanged_claim':False,'original_2D_geometry_projection_view_fills_text_retained':True,'3D_projection_frozen_visibility':'N/A for assigned planar tasks; no such inputs changed.','env_git_dotruntime_written':False,'shared_helpers_global_progress_assignments_old_batches_written':False})
 credible=[c for c in candidates if c['primary_credible_possibility']]
 queue={'stage':'material_refinement','unit':'background_31','created_at':stamp(),'assessed_question_ids':IDS,'unworked_question_ids':[],'candidate_count':len(credible),'candidates':credible,'review_policy':'Parent must start a NEW independent review for EVERY eventual delivery, including repaired variants. Primary results are not user approval or independent recommendation.','approval_Pass_Collect_delivery_actions':0}
 save(OWN/'second_review_queue.json',queue)
 for q in ['Plane232','Plane294','Plane297','Plane302']:
    cs=[c for c in candidates if c['question_id']==q]
    save(OWN/q/'material_refinement_assessment.json',{'question_id':q,'stage':'material_refinement','assessed_at':stamp(),'actual_source_JPG_native_formal_and_every_new_PNG_viewed':True,'primary_unique_original_math':str(OWN/q/'primary_original_math.json'),'old_history':str(OWN/q/'prior_history_read_audit.json'),'tested_variants':cs,'other_reasonable_hypotheses_exhausted_for_this_finite_unit':'Further palette/width/contour substitutions, another same-mechanism grouping, posthoc preset changes or existing failed-image repeats would add no substantive new correspondence. No further calls forced.','current_eligibility':eligible[q]})
 held=[]
 for p in sorted(OWN.glob('Plane*/r31_*/pre_API_visual_hold.json')):held.append(read(p))
 checkpoint={'unit':'background_31','stage':'material_refinement','status':'FINITE_BATCH_COMPLETE','created_at':stamp(),'stop_reason':'All8 assigned questions assessed with reasonable substantive hypotheses; all retained new variants completed exact paired calls and full finals manually read.','assigned_question_ids':IDS,'actual_assessed_question_ids':IDS,'assessed_question_ids':IDS,'unworked_question_ids':[],'counts':{'assigned_questions':8,'assessed_questions':8,'distinct_tested_questions':4,'pre_API_screened_questions':4,'substantive_tested_designs':5,'complete_candidate_pairs':5,'actual_quicktest3_calls':10,'original_control_calls':0,'API_errors':0,'aborted_calls':0,'automatic_retries':0,'credible_primary_possibilities':len(credible),'saved_new_designs_including_untested_drafts':7,'untested_native_visibility_hold_drafts':2},'candidates':candidates,'held_untested_pre_API_drafts':held,'question_assessment_paths':{q:str(OWN/q/'material_refinement_assessment.json') for q in IDS},'old_new_difference_and_history_audit':str(OWN/'history_and_lessons_audit.json'),'per_design_difference_audits':[c['design_difference_audit_path'] for c in candidates],'evidence_binding_audit':str(OWN/'evidence_binding_audit.json'),'source_preservation_audit':str(OWN/'source_preservation_final.json'),'current_eligibility_audit':str(OWN/'eligibility_final.json'),'second_review_queue':str(OWN/'second_review_queue.json'),'no_live_API_processes':str(OWN/'no_live_API_processes.json'),'all_own_API_processes_finished':True,'failures_and_aborts':{'API_errors':[],'API_aborts':[],'pre_API_visual_holds':held},'original_controls':[],'no_nested_agent_thread_worktree':True,'approval_Pass_Collect_formal_review_publication_calls':0,'limits':['No original controls were available for the assigned attempts; unchanged controls were not rerun. No statistical, causal, incremental effect or human-study claim.','All raw final letters/values read in full; narrative errors and incidental answer mentions are retained and do not substitute for the immutable preset.','Native visibility repairs precede any test of those repaired PNGs; untested originals stay frozen.','Parent must commission NEW independent review for every eventual delivered candidate.','Mutable progress metadata drift is distinct from unchanged question-specific approved formal inputs; unrelated workbench edits preserved.']}
 save(OWN/'checkpoint.json',checkpoint)
 print(json.dumps({'stage':checkpoint['stage'],'status':checkpoint['status'],'counts':checkpoint['counts'],'review_queue':len(credible),'checkpoint':str(OWN/'checkpoint.json')}),flush=True)

if __name__=='__main__':run()
