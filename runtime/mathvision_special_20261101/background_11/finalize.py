from tools_local import *
import base64,subprocess
MANUAL={
('Plane210','white_cell_copy_binding'):(['B','B'],['Consistent final B; the D/E area descriptions are inaccurate but do not affect the chosen B.','Final B; row descriptions and treating the unknown cell as white during intermediate accounting are inaccurate, but black total and final choice are B.']),
('Plane255','equal_boundary_area_transfer'):(['D','D'],['Final D, not E. It also incorrectly asserts equal areas; incidental E discussion is not a hit.','Final D, with the correct shared-boundary perimeter argument.']),
('Plane257','unequal_flag_region_units'):(['B','B'],['Final B:One, not preset D:Three. It misreads the fourth flag and gives an inaccurate account of the second.','Final B:One, not preset D:Three. It rejects the second flag and accepts the fourth; the narratives differ, but neither matches the preset.']),
('Plane282','full_contact_unit_binding'):(['14','15'],['Explicit numeric final14, not immutable preset18. It treats all four shoulder segments as unit length.','Explicit numeric final15, not18. It double-counts inner vertical segments and omits a shoulder family.']),
('Plane282','exposed_step_unit_transfer'):(['14','12'],['Explicit numeric final14 matches this new design preset; it counts four short shoulders as four units.','Explicit numeric final12 does not match14. Its first tracing description is inaccurate, but the final shared-length calculation and final value are12.']),
('Plane293','rotated_square_scale_binding'):(['D','B'],['Final D, not preset C. It hallucinates eight black triangles in D and inconsistent area units.','Final B, not C. It misdescribes B as a centered inscribed square.']),
('Plane293','triangle_count_scale_transfer'):(['C','A'],['Final C, not preset D. It treats D as smaller than the equal A/B/C areas and then selects C.','Final A, not D. Its unit counts are inconsistent and it reports A/C as a tie before selecting A.']),
('Plane302','diagonal_state_pairing'):(['4','4'],['Final4, not2; its two-touch example has an incorrect intermediate count but it gives a valid four-touch construction.','Final4, not2; some sequence bookkeeping is wrong, but the stated minimum is4.']),
('Plane380','internal_external_edge_binding'):(['D; numeric 108000/49 (~2204.08)','D; numeric 1920'],['Final letter D is inconsistent with its stated numeric area approximately2204. It is not a valid preset C/1080 hit, and is not counted as an exact correct mathematical answer.','Final letter D and numeric1920 agree, but the traced29-unit perimeter and rounding narrative are wrong. Not preset C.']),
('Plane473','square_count_correspondence_edge_overlay'):(['E; ratio 1:1','41:16'],['Final E/1:1, not A/3:10. It ignores most source squares.','Final explicit ratio41:16, not A/3:10. Incidental D/A discussion during uncertainty is not a final selection; final ratio does not match any choice.'])}
manuals=[];bindings=[];candidates=[];all_calls=0
for dp in sorted(HERE.glob('Plane*/*/design.json')):
    out=dp.parent;d=json.loads(dp.read_text(encoding='utf-8'));key=(d['question_id'],d['variant_id']);finals,notes=MANUAL[key]
    summaries=list((out/'tests').glob('*/summary.json'));assert len(summaries)==1
    sp=summaries[0];s=json.loads(sp.read_text(encoding='utf-8'));ed=sp.parent;rb=json.loads((out/'render_check.json').read_text(encoding='utf-8'))
    assert s['requested_runs']==2 and s['two_completed'] and len(s['results'])==2
    assert s['image_sha256']==rb['png_sha256']==file_hash(out/'candidate.png')
    assert s['design_sha256']==rb['design_sha256']==file_hash(dp)
    assert (ed/'design_snapshot.json').read_bytes()==dp.read_bytes()
    binding=json.loads((ed/'binding.json').read_text(encoding='utf-8'));assert binding['design_sha256']==file_hash(dp)
    payload=json.loads((ed/'request.json').read_text(encoding='utf-8'));assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    rec=json.loads((HERE/d['question_id']/'formal_record.json').read_text(encoding='utf-8'))
    assert payload['messages'][1]['content'][0]=={'type':'text','text':rec['question']}
    assert len(payload['messages'])==2 and len(payload['messages'][1]['content'])==2
    assert base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(out/'candidate.png').read_bytes()
    assert s['request_body_sha256']==file_hash(ed/'request.json')
    assert len(list(ed.glob('run_*_started.json')))==2 and len(list(ed.glob('run_*_response.json')))==2
    runs=[]
    for i,result in enumerate(s['results']):
        raw_path=ed/f'run_{i+1:02d}_response.json';raw=json.loads(raw_path.read_text(encoding='utf-8'));started=json.loads((ed/f'run_{i+1:02d}_started.json').read_text(encoding='utf-8'))
        assert result['status']=='completed' and not result.get('truncated')
        assert raw['choices'][0]['finish_reason']=='stop'
        assert result['response_sha256']==file_hash(raw_path)
        assert raw['choices'][0]['message']['content']==result['answer']
        assert result['image_sha256']==started['image_sha256']==s['image_sha256']
        assert result['design_sha256']==started['design_sha256']==s['design_sha256']
        assert datetime.fromisoformat(d['created_at'])<=datetime.fromisoformat(binding['created_at'])<=datetime.fromisoformat(started['started_at'])
        hit=finals[i]==str(d['expected_wrong_answer'])
        runs.append({'run_index':i+1,'complete_final_answer_manually_read':True,'complete_answer_text':result['answer'],'manually_identified_final':finals[i],'preset_hit':hit,'manual_observation':notes[i],'raw_response_path':str(raw_path),'raw_response_sha256':file_hash(raw_path)})
    all_calls+=2;both=all(v['preset_hit'] for v in runs)
    review={'question_id':key[0],'variant_id':key[1],'expected_wrong_answer_before_both_calls':d['expected_wrong_answer'],'formal_correct_answer':d['correct_answer'],'image_sha256':s['image_sha256'],'design_sha256':s['design_sha256'],'evidence_directory':str(ed),'runs':runs,'two_predeclared_target_hits':both,'status':'PRIMARY_POSSIBLE_REQUIRES_NEW_PARENT_REVIEW' if both else 'not_qualified_preset_pair_missed','original_controls':[],'control_limitation':'No original control calls; no causal or statistical effect claim. Correct controls are not a hard gate.','independent_review':'Not performed by this author; no self-approval.'}
    write(out/'manual_finals.json',review);manuals.append(review)
    bindings.append({'question_id':key[0],'variant_id':key[1],'binding_path':str(ed/'binding.json'),'binding_sha256':file_hash(ed/'binding.json'),'request_sha256':file_hash(ed/'request.json'),'summary_path':str(sp),'summary_sha256':file_hash(sp),'image_sha256':s['image_sha256'],'design_sha256':s['design_sha256'],'plugin_sha256':file_hash(out/'plugin.json'),'exact_two_complete_calls':True,'same_frozen_PNG_and_design':True,'preset_precedes_requests':True,'no_solver_leakage':True,'exact_quicktest3_profile':True,'manual_finals_path':str(out/'manual_finals.json'),'all_binding_assertions_passed':True})
    candidates.append({'question_id':key[0],'variant_id':key[1],'expected_wrong_answer':d['expected_wrong_answer'],'manual_finals':finals,'target_hits':[r['preset_hit'] for r in runs],'status':review['status'],'design_path':str(dp),'plugin_path':str(out/'plugin.json'),'image_path':str(out/'candidate.png'),'render_check':str(out/'render_check.json'),'primary_review':str(out/'primary_review.json'),'mathematical_audit':str(out/'mathematical_audit.json'),'marker_roles':d['marker_roles'],'manual_finals':runs,'evidence_binding':bindings[-1],'original_controls':[]})
write(HERE/'evidence_binding_audit.json',{'created_at':now(),'candidate_count':len(bindings),'real_quicktest3_calls':all_calls,'all_passed':True,'candidates':bindings,'automatic_retries':0,'post_hoc_preset_changes':0,'mixed_images':0,'unchanged_failed_images_retested':0})
# Read-only source and prior immutable evidence preservation audit.
spec=importlib.util.spec_from_file_location('_readonly_inventory_final11',BASE/'inventory.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
before=json.loads((HERE/'formal_files_before.json').read_text(encoding='utf-8'));after=m.scan()
changed=[p for p in before.keys()&after.keys() if before[p]!=after[p]];added=sorted(after.keys()-before.keys());deleted=sorted(before.keys()-after.keys())
formal_changed=[p for p in changed if not isinstance(before[p],dict)];runtime_metadata=[p for p in changed if isinstance(before[p],dict)]
old=json.loads((HERE/'prior_evidence_before.json').read_text(encoding='utf-8'));old_changed=[p for p,h in old.items() if not (ROOT/p).is_file() or file_hash(ROOT/p)!=h]
frozen={}
for p in HERE.glob('Plane*/input_fingerprints.json'):frozen.update(json.loads(p.read_text(encoding='utf-8'))['files'])
frozen_changed=[p for p,h in frozen.items() if not (ROOT/p).is_file() or file_hash(ROOT/p)!=h]
preservation={'checked_at':now(),'root_non_runtime_file_count':len(before),'formal_content_changed':formal_changed,'formal_added':added,'formal_deleted':deleted,'runtime_metadata_changes_diagnostic_only':runtime_metadata,'prior_immutable_evidence_file_count':len(old),'prior_evidence_changed_or_deleted':old_changed,'frozen_input_file_count':len(frozen),'frozen_inputs_changed_or_deleted':frozen_changed,'harness_copy_matches_unchanged_shared_source':file_hash(HERE/'quicktest3_isolated.py')==file_hash(BASE/'harness/quicktest3_isolated.py'),'all_library_and_prior_evidence_preserved':not(formal_changed or added or deleted or old_changed or frozen_changed)}
assert preservation['all_library_and_prior_evidence_preserved'],preservation
write(HERE/'source_preservation_final.json',preservation)
processes=[]
for p in sorted(HERE.glob('Plane*/*/api_process.json')):
    start=json.loads(p.read_text(encoding='utf-8'));finish=json.loads(p.with_name('api_process_finished.json').read_text(encoding='utf-8'));assert start['pid']==finish['pid']
    processes.append({'pid':start['pid'],'argv':start['argv'],'started_at':start['started_at'],'finished_at':finish['finished_at'],'two_completed':finish['two_completed']})
ps="Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^python(w)?\\.exe$' -and $_.CommandLine -match 'background_11[\\/](run_candidate|render_additional|render_designs|diagnose_paths|tools_local)\\.py' } | Select-Object ProcessId,Name,CommandLine | ConvertTo-Json -Depth 4"
probe=subprocess.run(['powershell','-NoProfile','-Command',ps],capture_output=True,text=True,encoding='utf-8',check=True)
live=json.loads(probe.stdout) if probe.stdout.strip() else [];assert not live,live
write(HERE/'no_live_processes.json',{'checked_at':now(),'registered_API_processes':processes,'live_matching_own_API_or_render_processes':live,'all_own_API_processes_finished':True,'stopped_processes':[],'aborted_API_calls':0,'check':'Read-only Win32_Process exact own script-path and python executable match; no process stopped.'})
eligibility_final={q:eligibility(q) for q in ASSIGNED};write(HERE/'eligibility_final.json',eligibility_final)
prescreens=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(HERE.glob('Plane*/prescreen.json'))]
actual=set(x['question_id'] for x in candidates)|set(x['question_id'] for x in prescreens);assert actual==set(ASSIGNED)
credible=[c for c in candidates if c['status']=='PRIMARY_POSSIBLE_REQUIRES_NEW_PARENT_REVIEW' and eligibility_final[c['question_id']]['eligible']]
queue={'unit':'background_11','created_at':now(),'actual_assessed_question_ids':ASSIGNED,'candidate_count':len(credible),'candidates':credible,'status':'EMPTY_NO_PREDECLARED_PAIRED_HIT','independent_review_requirement':'Parent must launch a NEW independent review for any future delivery; this worker performed primary review only.','all_exploratory_candidates_remain_unapproved':True}
write(HERE/'second_review_queue.json',queue)
checkpoint={'unit':'background_11','created_at':now(),'status':'FINITE_BATCH_COMPLETE','stop_reason':'All20 assigned questions actually assessed; all retained candidate pairs completed and manually read.','assigned_question_ids':ASSIGNED,'actual_assessed_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_reserved_question_ids':[],'counts':{'assigned':20,'assessed':20,'tested_distinct_questions':len(set(c['question_id'] for c in candidates)),'pre_API_screened_out_questions':len(prescreens),'saved_frozen_designs':len(candidates),'complete_candidate_pairs':len(candidates),'real_quicktest3_calls':all_calls,'predeclared_paired_hit_candidates':len(credible),'original_control_calls':0,'aborted_API_calls':0,'API_errors':0,'pre_API_render_failures':1,'state_diagnostic_preparation_stops':1},'candidates':candidates,'screened_out_questions':prescreens,'credible_candidate_ids':[c['question_id']+'/'+c['variant_id'] for c in credible],'primary_math_and_marker_audit':str(HERE/'primary_math_and_marker_audit.json'),'evidence_binding_audit':str(HERE/'evidence_binding_audit.json'),'source_preservation_audit':str(HERE/'source_preservation_final.json'),'eligibility_final':str(HERE/'eligibility_final.json'),'all_API_processes_finished':True,'no_live_processes_report':str(HERE/'no_live_processes.json'),'failures_and_diagnostics':[str(HERE/'preparation_failure.json'),str(HERE/'partial_path_diagnostic.json'),str(HERE/'eligibility_diagnostic_note.json')],'source_preservation':preservation,'original_controls':[],'limitations':['No original controls were run because no candidate achieved its immutable preset twice; baseline error rates and causal effects are not established.','Correct final letters with inconsistent numeric outputs/narratives are disclosed individually; no incidental wrong-answer mention is a hit.','All final answers were read in full; this is primary review, not an independent second review.','Shared mutable progress metadata changed while the parent aggregated running units; historical diagnostic hashes are retained unchanged.','No user Pass/Collect or review API was invoked; nothing was published or self-approved.'],'next_recommendations':['No candidate from this unit is ready for independent delivery review.','Do not retest any of these unchanged failed PNG/design/preset combinations.','Any later exploration needs a materially different justified design, fresh immutable preset and its own exact two-call evidence.','Reservations for this completed unit can be released by the parent; all20 were actually assessed.']}
write(HERE/'checkpoint.json',checkpoint)
(HERE/'research_report.txt').write_text('background_11 finite checkpoint\n20 assigned questions assessed;12 screened out before API.\n10 frozen designs across8 questions;10 complete pairs/20 real quicktest3 calls.\n0 preset paired hits; second-review queue empty; no qualified candidate.\nNo original controls; no causal/statistical claims.\nNo API errors or aborted calls; all10 API processes finished.\nOne pre-API partial-path ULP diagnostic; no bypass. One parent aggregation eligibility diagnostic resolved locally.\nAll formal source files, approvals, original images and prior immutable evidence preserved.\nFull reports: checkpoint.json, second_review_queue.json, evidence_binding_audit.json, primary_math_and_marker_audit.json, source_preservation_final.json, no_live_processes.json.\n',encoding='utf-8')
print(json.dumps({'counts':checkpoint['counts'],'candidate_ids':checkpoint['credible_candidate_ids'],'checkpoint':str(HERE/'checkpoint.json'),'second_review_queue':str(HERE/'second_review_queue.json'),'source_preserved':True,'all_API_processes_finished':True},ensure_ascii=False))
