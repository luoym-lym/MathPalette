from unit_tools import *
import base64
CONFIGS=[('Plane481','two_strip_overlap_binding',['10','3'],[
    'Read the complete final: ends Final Answer 10. The response uses an inaccurate diamond-plus-square narrative but its declared final is 10; predeclared 12 is not the final.',
    'Read the complete final: ends Answer 3 after treating the center as a one-unit square. This is wrong relative to formal 10 and differs from preset 12.'
]),('Plane482','four_tile_single_window_binding',['C','D'],[
    'Read the complete final: ends C. It speculates about white diamonds, approximate overlaps and an AMC source; these unsupported claims are retained. Final C is not preset B.',
    'Read the complete final: ends Answer D and gives 1/16. It incorrectly uses four favorable arrangements per one window. Final D is not preset B.'
]),('Solid201','two_yes_identity_edge_overlay',['D','D'],[
    'Read the complete final: explicitly concludes D, 2/3, four YES faces. It contradicts the observed maybe while counting; final is internally consistent letter/value D=2/3 and is not preset A.',
    'Read the complete final: ends Answer D and gives 4/6=2/3, with speculative biased-die and maybe-is-YES claims retained. Final D differs from preset A. Two D responses may not be post-hoc relabeled a target hit.'
])]
all_candidates=[];binding_audits=[]
for qid,name,finals,comments in CONFIGS:
    directory=HERE/qid/name
    evidence=list((directory/'tests').glob('quicktest3_*'));assert len(evidence)==1
    evidence=evidence[0];binding=read(evidence/'binding.json');summary=read(evidence/'summary.json')
    design=read(directory/'design.json');plugin=read(directory/'plugin.json')
    assert summary['two_completed'] and binding['requested_runs']==2
    assert binding['design_sha256']==sha(directory/'design.json')==sha(evidence/'design_snapshot.json')
    assert binding['image_sha256']==sha(directory/'candidate.png')==design['image_sha256']
    assert binding['expected_wrong_answer']==design['expected_wrong_answer']
    request=read(evidence/'request.json');record=read(HERE/qid/'formal_record.json')
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert set(request)=={'model','stream','thinking','messages'} and request['stream'] is False
    assert len(request['messages'])==2 and request['messages'][0]['content']==binding['system_prompt']
    body=request['messages'][1]['content'];assert len(body)==2 and body[0]=={'type':'text','text':record['question']}
    payload=base64.b64decode(body[1]['image_url']['url'].split(',',1)[1]);assert hashlib.sha256(payload).hexdigest()==binding['image_sha256']
    assert sha(evidence/'request.json')==binding['request_body_sha256']
    manual=[]
    for i,(final,comment) in enumerate(zip(finals,comments),1):
        p=evidence/f'run_{i:02d}.json';r=read(p)
        assert r['status']=='completed' and r['finish_reason']=='stop' and r['truncated'] is False
        assert r['image_sha256']==binding['image_sha256'] and r['design_sha256']==binding['design_sha256'] and r['request_body_sha256']==binding['request_body_sha256']
        assert r['response_sha256']==sha(evidence/f'run_{i:02d}_response.json')
        raw=read(evidence/f'run_{i:02d}_response.json');assert raw['choices'][0]['message']['content']==r['answer']
        manual.append({'run_index':i,'complete_final_response_manually_read':True,'full_final_response':r['answer'],'manual_final_answer':final,'manual_interpretation':comment,'predeclared_wrong_answer':design['expected_wrong_answer'],'target_hit':False,'raw_run_path':str(p.relative_to(HERE)),'response_path':str((evidence/f'run_{i:02d}_response.json').relative_to(HERE)),'response_sha256':r['response_sha256']})
    review={'question_id':qid,'design_name':name,'reviewed_at':now(),'manual_reader':'background_22 primary designer','independent_second_review':False,'preset':design['expected_wrong_answer'],'formal_answer':record['answer'],'final_answers':finals,'runs':manual,'credible_predeclared_paired_hit':False,'status':'completed_pair_missed_preset','no_retest_or_posthoc_preset_change':True,'controls':[],'limitations':['No original-image control pair was run.','No human performance study or per-marker causal ablation was run.','These outputs do not establish a causal effect of the marks.']}
    write(directory/'manual_finals_review.json',review)
    audit={'question_id':qid,'design':str((directory/'design.json').relative_to(HERE)),'design_sha256':sha(directory/'design.json'),'plugin':str((directory/'plugin.json').relative_to(HERE)),'plugin_sha256':sha(directory/'plugin.json'),'candidate':str((directory/'candidate.png').relative_to(HERE)),'candidate_png_sha256':sha(directory/'candidate.png'),'pixel_sha256':binding['pixel_sha256'],'binding':str((evidence/'binding.json').relative_to(HERE)),'request_body_sha256':binding['request_body_sha256'],'full_finals':str((directory/'manual_finals_review.json').relative_to(HERE)),'two_complete_same_request_same_png_same_preset':True,'exact_request_contains_only_existing_system_prompt_formal_question_candidate_png':True,'profile_model_thinking_unchanged':True,'response_json_and_raw_exact_bindings_verified':True,'immutable_snapshot_matches':True,'preset_created_before_both_calls':design['created_at']<binding['created_at'],'solver_calls':2,'api_errors':0,'api_aborts':0,'automatic_retries':0}
    assert audit['preset_created_before_both_calls']
    binding_audits.append(audit)
    all_candidates.append({'question_id':qid,'design_name':name,'expected_wrong_answer':design['expected_wrong_answer'],'formal_answer':record['answer'],'manual_final_answers':finals,'credible_predeclared_paired_hit':False,'status':review['status'],'evidence':audit,'primary_math_proof':str((HERE/qid/'primary_math.json').relative_to(HERE)),'primary_review':str((directory/'primary_review.json').relative_to(HERE)),'manual_finals_review':str((directory/'manual_finals_review.json').relative_to(HERE))})
source_audit=[]
for qid in IDS:
    branch='PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry'
    initial=read(HERE/qid/'source_hashes_initial.json');current=eligibility(branch,qid)
    differences=[{'path':p,'initial':h,'current':sha(PROJECT/p) if (PROJECT/p).is_file() else None} for p,h in initial.items() if not (PROJECT/p).is_file() or sha(PROJECT/p)!=h]
    first=read(HERE/qid/'eligibility_initial.json')
    entry={'question_id':qid,'branch':branch,'checked_at':now(),'individual_frozen_files_checked':len(initial),'frozen_file_changes_or_missing':differences,'record_unchanged':current['question_record_sha256']==first['question_record_sha256'],'approval_record_unchanged':current['approval']==first['approval'],'currently_eligible':current['eligible'],'current_content_approval_valid':current['approval_current'],'accepted_records':current['accepted_records'],'collected_records':current['collected_records'],'collection':current['collection'],'source_primary_audit':str((HERE/qid/'source_primary_audit.json').relative_to(HERE))}
    assert not differences and entry['record_unchanged'] and entry['approval_record_unchanged'] and current['eligible']
    write(HERE/qid/'eligibility_final.json',current);source_audit.append(entry)
write(HERE/'source_preservation_final.json',{'checked_at':now(),'scope':'Individual assigned MathVision original inputs, current approval and Special eligibility. No whole-workspace equality claim.','questions':source_audit,'all_relevant_frozen_inputs_preserved':True,'writes':'Own unit directory only, guarded after shared runtime_isolation install. All shell/apply_patch writes also explicitly target own unit.','unrelated_author_designed_changes':'Preserved without restores or whole-workspace assertions.','historical_global_runtime_progress_metadata':'Read-only diagnostic metadata; never a frozen-original corruption criterion.'})
inventory=read(BASE/'inventory.json')
membership={q:any(r['id']==q for r in inventory['PlaneGeometry' if q.startswith('Plane') else 'SolidGeometry']['eligible']) for q in IDS}
assert all(membership.values())
write(HERE/'inventory_membership_correction.json',{'checked_at':now(),'correct_inventory_membership':membership,'correction':'allocation_and_history_audit.json originally looked for question_id in inventory eligible rows, which actually use id, producing false diagnostic membership values. That helper error did not affect authoritative eligibility(), original approvals, source hashes or solver calls. Historical audit retained; this correction supersedes only that diagnostic field.'})
write(HERE/'evidence_binding_audit.json',{'checked_at':now(),'harness_shared_source_sha256':sha(BASE/'harness/quicktest3_isolated.py'),'harness_local_copy_sha256':sha(HERE/'quicktest3_isolated.py'),'harness_copy_byte_identical':sha(BASE/'harness/quicktest3_isolated.py')==sha(HERE/'quicktest3_isolated.py'),'candidate_pairs':binding_audits,'all_checks_pass':True})
prescreen={
    'Plane479':{'status':'prescreen_no_clean_hypothesis','reason':'Equal square areas and midpoint text fix a simple area cancellation; no grounded false part correspondence found without adding an artificial internal partition or arbitrary numerator salience. Existing fill/diagonal stay untouched.'},
    'Plane480':{'status':'prescreen_no_clean_hypothesis','reason':'The answer is exact unit-cell area 13. Merely styling cap boundaries/grid lines offers broad salience; proposed wrong totals would need unsupported diagonal-as-unit or false region groupings. No forced design/call.'},
    'Plane484':{'status':'prescreen_source_semantic_hold','reason':'Formal question omits requiring points on and alternating between the rays. Ai=i*u on one ray satisfies the printed constraints for arbitrary n. Diagram suggests alternation but cannot supply a rigorous unique finite maximum without interpretation. No formal change.'},
    'Plane490':{'status':'prescreen_no_clean_hypothesis','reason':'The whole arrow is uniquely a half-turn. A zero-degree false shaft match would merely select shared/parallel shaft segments while discarding arrowhead information; a quarter-turn would pair unrelated long/short edges. Not advanced.'},
    'Solid194':{'status':'prescreen_no_clean_hypothesis','reason':'The illustrated 3-pyramid has no interior balls. Inferring 6 by removing only top/base is a numerical omission; no actual displayed interior feature supports a clean false shell correspondence. Extra stack/shell lines could misrepresent the separated layers.'}
}
processes=read(HERE/'process_audit_final.json');assert not processes
for qid,name,_,_ in CONFIGS:assert (HERE/qid/name/'pair_process_finished.json').is_file()
errors=[{'type':'schema_rejection_pre_render','question_id':'Solid201','path':'Solid201/two_yes_identity_edge_binding/schema_error.json','effect':'Digit-leading native IDs cannot be target values in actual schema. No PNG or API call existed for this implementation. Fixed by legal add_line exact-edge overlays under new directory and unchanged preset A. Original rejected spec retained.'},
        {'type':'diagnostic_inventory_lookup_error','path':'inventory_membership_correction.json','effect':'question_id versus id helper key mismatch; corrected in supplemental audit without changing original evidence or eligibility.'}]
checkpoint={'unit':'background_22','finished_at':now(),'terminal':True,'stop_reason':'All eight assigned questions assessed; all own paired calls complete.','assignment_question_count':8,'assigned_question_ids':IDS,'assessed_question_ids':IDS,'unworked_question_ids':[],'ineligible_skipped_question_ids':[],'rendered_candidate_count':3,'tested_candidate_pairs':3,'actual_api_calls':6,'completed_api_calls':6,'credible_predeclared_paired_hit_count':0,'api_errors':0,'api_aborts':0,'automatic_retries':0,'schema_rejected_pre_render_implementations':1,'schema_rejected_draft_presets':'solid_design_specs.json','prescreened_without_calls':prescreen,'candidates':all_candidates,'second_review_queue':'second_review_queue.json','source_audit':'source_preservation_final.json','binding_audit':'evidence_binding_audit.json','allocation_audit':'allocation_and_history_audit.json','allocation_inventory_correction':'inventory_membership_correction.json','all_presets':['plane_design_specs.json','solid_design_specs.json','solid_design_specs_overlay.json'],'errors':errors,'aborts':[],'original_controls':[],'primary_math_proofs':{q:str((HERE/q/'primary_math.json').relative_to(HERE)) for q in IDS},'source_primary_audits':{q:str((HERE/q/'source_primary_audit.json').relative_to(HERE)) for q in IDS},'no_live_api_processes':True,'process_verification':'process_audit_final.json','processes_terminated':[],'formal_or_approval_writes':False,'Pass_Collect_review_api_actions':False,'independent_second_review_performed':False,'delivery_or_qualification':False,'parent_requirement':'Parent must create a NEW independent second reviewer before any eventual delivery; this queue is empty because no design hit its frozen preset twice.','limitations':['No original controls: causal effect cannot be separated from model baseline error.','No human study, statistical claim, or per-marker causal ablation.','Solid201 D/D is wrong relative to B but cannot count because preset was A.','No post-hoc preset change, selected-success subset, mixed-image evidence or unchanged-image retest.'],'next_recommendations':['Do not retest these unchanged failed images or change their frozen presets.','Any future materially different legal hypothesis needs its own fresh predeclared two-call pair.','Plane484 needs a separate user-authorized source clarification before treating its maximum as uniquely 90; current formal library was left unchanged.'],'artifact_manifest':'artifact_manifest.json','report':'report.md'}
write(HERE/'second_review_queue.json',{'unit':'background_22','created_at':now(),'assessed_question_ids':IDS,'unworked_question_ids':[],'candidates':[],'credible_predeclared_paired_hit_count':0,'reason':'No same-image pair returned the frozen preset twice. Solid201 D/D cannot be converted post hoc from preset A.','requirement':'Any eventual delivery requires a NEW independent reviewer started by parent. No self second-review, no publication, no Pass/Collect.'})
write(HERE/'checkpoint.json',checkpoint)
report='''# background_22 finite checkpoint

All 8 assigned questions were assessed. Three candidate PNGs completed exactly two quicktest3 calls each: 6 complete calls, no API errors, aborts or retries. No credible predeclared paired hit; independent second-review queue is empty. No delivery, approval, Pass or Collect occurred.

| Question / hypothesis | Frozen wrong preset | Complete final answers | Result |
| --- | --- | --- | --- |
| Plane481 two_strip_overlap_binding | 12 | 10 / 3 | Miss |
| Plane482 four_tile_single_window_binding | B | C / D | Miss |
| Solid201 two_yes_identity_edge_overlay | A | D / D | Miss; D/D cannot replace preset A |

Every complete final was read manually and preserved verbatim in the candidate's manual_finals_review.json. request.json binds only the existing solver prompt, exact formal question and candidate PNG. The local harness is byte-identical to the existing isolated harness; model/thinking/request parameters were unchanged.

Fresh actual schema normalization, no-op formal PNG pixel identity, twice byte-identical frozen candidate rendering, full-precision paths, native-size PNG viewing, source JPG inspection, primary unique-answer proofs and per-marker reviews are saved. Solid201 has a fresh 576-rotation-pair proof: exactly one oriented die assignment, three YES faces. Plane482 has exhaustive 4^9 tiling enumeration, probability 1/64. Plane481 has exact polygon and strip-union area 10.

Five questions were screened without calls: Plane479 and Plane480 lacked a clean targeted wrong correspondence; Plane490's proposed local matches discarded the decisive arrowhead; Solid194's shown 3-pyramid has no interior feature to bind; Plane484's printed wording lacks the ray-membership/alternation condition needed for a finite unique maximum. Its formal source remains untouched.

One pre-render Solid201 implementation was rejected by the actual schema because native object IDs begin with digits. Its specification and error remain; the tested version uses allowed 1pt add_line overlays on exact existing snap endpoints. No renderer/schema modification or call retry occurred. A diagnostic inventory lookup used the wrong id key; its supplemental correction records all eight as eligible. Authoritative approval/Special checks were correct throughout.

Final individual source/approval/Special audits passed for all eight questions. No whole-workspace equality is asserted; concurrent unrelated Author-designed changes and mutable global progress were preserved. All task writes stayed under this unit root with cache/TEMP routing and filesystem guards. All own API processes exited normally; final process audit is empty.

No original controls or human/causal ablation studies were run, so these pairs do not establish marker causality. Parent must start a NEW independent second reviewer before any eventual delivery. Do not retest unchanged failed images or revise their presets after seeing these outputs.

See checkpoint.json, evidence_binding_audit.json, source_preservation_final.json, second_review_queue.json and artifact_manifest.json for complete paths and hashes.
'''
(HERE/'report.md').write_text(report,encoding='utf-8',newline='\n')
manifest={str(p.relative_to(HERE)).replace('\\','/'):sha(p) for p in sorted(HERE.rglob('*')) if p.is_file() and not any(x in p.relative_to(HERE).parts for x in ['cache','mpl_cache','temp','tmp','render_tmp'])}
write(HERE/'artifact_manifest.json',{'created_at':now(),'unit_root':str(HERE),'files':manifest,'exclusions':'Ephemeral cache/temp directories; manifest itself is not self-hashed. All raw requests/responses and presets are included.'})
print(json.dumps({'assessed':len(IDS),'pairs':3,'calls':6,'credible':0,'source_audits_pass':True,'binding_audits_pass':True,'no_live_api_processes':True,'manifest_files':len(manifest),'checkpoint':str(HERE/'checkpoint.json'),'second_review_queue':str(HERE/'second_review_queue.json')}))
