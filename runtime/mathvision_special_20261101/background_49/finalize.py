import research_env as env
import json,base64,hashlib,io
from pathlib import Path
from inspect_sources import save,sha,now,eligibility,QIDS
from PIL import Image

FINALS={'Solid80':['10','10'],'Solid89':['C','C'],'Solid90':['10','sqrt(119)'],'Solid107':['11','11'],
        'Solid159':['-11','10'],'Solid171':['36','36'],'Solid172':['9','17']}
NOTES={
 'Solid80':'Both finals10 explicitly subtract the removed corner and add the three new corners; preset11 missed twice.',
 'Solid89':'Both final C/600g. Run1 temporarily miscounts19 removed, then explicitly corrects to7; final remains unambiguous C/600g. Neither run hitsA/540g.',
 'Solid90':'Run1 final10; run2 finalsqrt119 after wrongly treatingXZ as an edge andZA as the top-face diagonal. Neither is the frozen aggregate target10sqrt2.',
 'Solid107':'Both finals11. Run1 is a full223.081-second,10706-completion-token stop response with many discarded intermediate mistakes; final states5+6=11. No timeout, token limit, retry or abort was introduced. Run2 also ends11.',
 'Solid159':'Run1 final-11 after a contradictory tetrahedron/octahedron analysis. Run2 final10 although its written1+5+1+1+1 expression equals9. Neither is16.5; these wrong outputs are not relabelled.',
 'Solid171':'Both final36. Run1 says every edge is octagon/triangle-shared, which overlooks octagon/octagon old remnants; its total count is nevertheless36. Run2 also obtains36 by12+24. Neither hits20.',
 'Solid172':'Run1 final9 despite inconsistent invented1/4 replacement. Run2 discusses13 and17 as intermediate alternatives, then reads actualT=1/L=5 and finally gives17. Incidental13 is not a preset13 hit.'}

def audit_candidate(q):
 d=next((env.ROOT/q).glob('r49_*')); design=json.loads((d/'design.json').read_text(encoding='utf-8'))
 evdirs=list((d/'tests').iterdir()); assert len(evdirs)==1; ev=evdirs[0]
 binding=json.loads((ev/'binding.json').read_text(encoding='utf-8'))
 requestbytes=(ev/'request.json').read_bytes();request=json.loads(requestbytes)
 e=eligibility(q);assert e['eligible'];save(d/'eligibility_after_calls.json',e)
 assert (ev/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
 assert binding['design_sha256']==sha(d/'design.json') and binding['image_sha256']==sha(d/'candidate.png')
 assert binding['expected_wrong_answer']==design['expected_wrong_answer'] and binding['requested_runs']==2
 assert binding['request_body_sha256']==hashlib.sha256(requestbytes).hexdigest()
 assert set(request)=={'model','stream','thinking','messages'}
 assert request['model']=='mimo-v2.6-flash' and request['stream'] is False and request['thinking']=={'type':'disabled'}
 assert len(request['messages'])==2 and request['messages'][0]=={'role':'system','content':binding['system_prompt']}
 user=request['messages'][1];assert user['role']=='user' and len(user['content'])==2
 assert user['content'][0]=={'type':'text','text':e['formal_record']['question']}
 assert binding['question']==e['formal_record']['question']
 imagebytes=base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])
 assert imagebytes==(d/'candidate.png').read_bytes()
 im=Image.open(io.BytesIO(imagebytes)).convert('RGBA');assert im.size==(768,768) and im.getextrema()[3]==(255,255)
 ph=hashlib.sha256(b'768x768:RGBA:'+im.tobytes()).hexdigest();assert binding['pixel_sha256']==ph
 assert binding['question_record_sha256']==hashlib.sha256(json.dumps(e['formal_record'],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
 summary=json.loads((ev/'summary.json').read_text(encoding='utf-8'));assert summary['two_completed']
 assert len(summary['results'])==2 and len(list(ev.glob('run_*_started.json')))==2 and len(list(ev.glob('run_*_response.json')))==2
 reviews=[]
 for i in [1,2]:
  p=ev/f'run_{i:02d}.json'; r=json.loads(p.read_text(encoding='utf-8'))
  rp=ev/f'run_{i:02d}_response.json'; raw=json.loads(rp.read_text(encoding='utf-8-sig'))
  choice=raw['choices'][0];start=json.loads((ev/f'run_{i:02d}_started.json').read_text(encoding='utf-8'))
  assert r['status']=='completed' and r['http_status']==200 and choice['finish_reason']=='stop'
  assert r['response_sha256']==sha(rp) and raw['model']=='mimo-v2.6-flash'
  assert start['request_body_sha256']==binding['request_body_sha256'] and start['image_sha256']==binding['image_sha256'] and start['design_sha256']==binding['design_sha256']
  assert r['image_sha256']==binding['image_sha256'] and r['design_sha256']==binding['design_sha256']
  assert (d/'design.json').stat().st_mtime< (ev/f'run_{i:02d}_started.json').stat().st_mtime
  reviews.append({'run_index':i,'status':'completed','full_raw_final_text':choice['message']['content'],
   'entire_raw_response_manually_read':True,'manual_terminal_answer':FINALS[q][i-1],'expected_wrong_answer':design['expected_wrong_answer'],
   'matches_predeclared_wrong_answer':False,'raw_response_path':str(rp),'raw_response_sha256':sha(rp),
   'elapsed_seconds':r['elapsed_seconds'],'completion_tokens':raw['usage']['completion_tokens'],'finish_reason':choice['finish_reason'],'manual_notes':NOTES[q]})
 save(d/'manual_final_review.json',{'question_id':q,'variant_id':design['variant_id'],'reviewed_at_utc':now(),'reviews':reviews,
  'two_target_hits':False,'decision':'MISS; no candidate; no relabelling, retry or second-review promotion','mechanism_or_causal_gain_proven':False})
 audit={'question_id':q,'variant_id':design['variant_id'],'frozen_image_design_snapshot_request_raw_response_bindings_valid':True,
  'request_is_exact_formal_question_plus_candidatePNG_and_original_systemprompt':True,'no_solver_answer_preset_intent_history_or_parameters':True,
  'original_model_thinking_profile_no_max_tokens_no_timeout_override':True,'exactly_two_actual_completed_calls_same_PNG':True,
  'design_and_material_difference_audit_predate_both_calls':True,'no_other_same_image_candidate_attempt':True,
  'expected_wrong_answer':design['expected_wrong_answer'],'manual_terminal_answers':FINALS[q],'both_preset_hits':False,
  'evidence_dir':str(ev),'binding_sha256':sha(ev/'binding.json'),'request_sha256':sha(ev/'request.json'),
  'candidate_png_sha256':sha(d/'candidate.png'),'candidate_pixel_sha256':ph,'design_sha256':sha(d/'design.json'),'plugin_sha256':sha(d/'plugin.json'),
  'source_context_binding':{'current_approval_content_sha256':e['computed_current_content_sha256'],'context_sha256':sha(d/'context.json'),'marker_path_bindings_sha256':sha(d/'marker_path_bindings.json')},
  'schema_noop_offline_repeat_and_per_action_visibility_report':str(d/'render_check.json'),'actual_native_primary_semantics_review':str(d/'primary_review.json'),
  'raw_response_hashes':[sha(ev/f'run_{i:02d}_response.json') for i in [1,2]],'manual_full_answers_report':str(d/'manual_final_review.json')}
 save(d/'evidence_binding_audit.json',audit)
 save(env.ROOT/q/'assessment.json',{'question_id':q,'assessed':True,'status':'tested_material_refinement_MISS','variant_id':design['variant_id'],'candidate_directory':str(d),
  'expected_wrong_answer':design['expected_wrong_answer'],'complete_manual_final_answers':FINALS[q],'two_target_hits':False,
  'material_difference':design['material_difference'],'mathematics':str(env.ROOT/q/'primary_math_proof.json'),'notes':NOTES[q],
  'reasonable_finite_assessment_exhausted':True,'no_arbitrary_design_or_marker_cap_used':True,'not_a_claim_that_all_other_variants_are_impossible':True})
 return audit

def main():
 process=json.loads((env.ROOT/'process_audit_final.json').read_text(encoding='utf-8-sig'));assert process['all_own_api_processes_closed']
 candidates=[audit_candidate(q) for q in QIDS if q in FINALS]
 before=json.loads((env.ROOT/'preservation_before.json').read_text(encoding='utf-8'));changes={}
 for p,h in before.items():
  current=sha(p) if Path(p).exists() else None
  if current!=h:changes[p]={'before':h,'after':current}
 save(env.ROOT/'preservation_after.json',{'checked_at_utc':now(),'tracked_readonly_files':len(before),'hash_changes':changes,'all_tracked_readonly_files_unchanged':not changes,
  'strict_own_root_write_guard_installed_before_project_imports':True,'all_new_files_TEMP_TMP_TMPDIR_MPLCONFIGDIR_XDG_CACHE_HOME_under':str(env.ROOT),
  'formal_approval_Pass_Collect_publish_shared_helper_or_global_ledger_mutations':0,'old_evidence_untouched':True,'no_git_history_env_or_runtime_changes':True,
  'scope':'Only explicitly tracked source/implementation/old-question evidence files; no assertion that unrelated concurrent whole workspace is unchanged.'})
 eligibility_reports={q:eligibility(q) for q in QIDS};assert all(e['eligible'] for e in eligibility_reports.values())
 save(env.ROOT/'final_current_eligibility.json',eligibility_reports)
 summary={'unit':'background_49','stage':'material_refinement','status':'terminal','finished_at_utc':now(),
  'assigned_question_ids':QIDS,'actual_assessed_question_ids':QIDS,'unworked_question_ids':[],'question_count':8,
  'saved_material_design_count':7,'tested_design_count':7,'completed_paired_candidate_count':7,'actual_API_call_attempts':14,'completed_API_calls':14,
  'original_control_calls':0,'possible_candidate_count':0,'API_errors':0,'aborted_calls':0,'retries':0,'live_own_API_processes':0,
  'stop_reason':'All8 assigned questions assessed with independent actual-source mathematics, complete old-history review and reasonable distinct information hypotheses. Seven legal primary designs tested once with exactly2 calls each; Solid163 skipped for concrete information/semantic reasons. No arbitrary quota/cost cap or universal impossibility claim.',
  'screened_without_design':['Solid163'],'untested_saved_designs':[],
  'manual_final_answers':FINALS,'all_frozen_binding_audits':candidates,
  'question_assessments':{q:str(env.ROOT/q/'assessment.json') for q in QIDS},
  'mathematics':{q:str(env.ROOT/q/'primary_math_proof.json') for q in QIDS},
  'current_eligibility_original_approval_audit':str(env.ROOT/'final_current_eligibility.json'),
  'original_source_records':str(env.ROOT/'source_records_full.json'),'old_full_evidence_index':str(env.ROOT/'old_evidence_full_index.json'),
  'all_old_bindings_designs_and_existing_controls_scan':str(env.ROOT/'global_old_binding_design_scan.json'),'old_full_manual_final_review':str(env.ROOT/'old_manual_final_review.json'),
  'existing_original_controls':'None found for these8 IDs in readonly global binding scan; no unchanged control rerun and no new control hard gate.',
  'historical_parse_failures':'No parse failure among this scope historical artifacts. All historic bytes remain untouched; no inference of no call from parsing failure.',
  'annotation_semantics_lesson':'Plane242 lesson and complete independent review read. Physical-paper color-transport none reading is case-specific; here numerical graph/weight problems preserve original object/color/count identities. Solid163 abstention preserves black/white counting semantics.',
  'source_preservation':str(env.ROOT/'preservation_after.json'),'own_process_closure':str(env.ROOT/'process_audit_final.json'),
  'local_exception_evidence':str(env.ROOT/'local_execution_events.json'),
  'local_exception_summary':'One initial offline ndarray JSON serialization error resolved before API calls; all required render audits then passed. Read-only shell wildcard/Get-Date compatibility errors did not affect evidence or calls.',
  'slow_complete_calls':'Solid107 run1 completed after223.081s, Solid172 run2 after89.207s; both full stop responses kept, no token/timeout override, retry or abort.',
  'review_queue':str(env.ROOT/'second_review_queue.json'),'no_qualified_delivery_claim':True,'no_self_independent_second_review':True,
  'no_mechanism_causality_statistical_gain_claim':True,'no_formal_approval_Pass_Collect_or_publication':True,'no_nested_agents_T3_threads_or_worktrees':True}
 save(env.ROOT/'checkpoint.json',summary)
 save(env.ROOT/'second_review_queue.json',{'unit':'background_49','stage':'material_refinement','created_at_utc':now(),'candidates':[],
  'possible_candidate_count':0,'reason':'All seven new exact pairs miss their immutable presets; Solid163 has no clean new design. No old one-hit or other double-wrong miss was relabelled.',
  'parent_NEW_independent_second_review_required_for_any_future_possible_candidate':True,'approval_status':'RESEARCH_ONLY; no user Pass/Collect/approval/publication'})
 manifest={str(p):{'sha256':sha(p),'bytes':p.stat().st_size} for p in env.ROOT.rglob('*') if p.is_file() and p.suffix in ['.json','.png','.py','.ps1'] and not any(part in ['render_tmp','temp','cache','mplconfig','mpl_cache','tmp','__pycache__'] for part in p.relative_to(env.ROOT).parts)}
 save(env.ROOT/'evidence_manifest.json',{'created_at_utc':now(),'files':manifest})
 print(json.dumps({'assessed':8,'designs':7,'actual_complete_calls':14,'possible_candidates':0,'API_errors':0,'aborts':0,'retries':0,'readonly_hash_changes':changes,'live_own_API_processes':0,'checkpoint':str(env.ROOT/'checkpoint.json'),'second_review_queue':str(env.ROOT/'second_review_queue.json')},ensure_ascii=False))
if __name__=='__main__':main()
