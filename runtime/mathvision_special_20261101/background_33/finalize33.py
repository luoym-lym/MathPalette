from tools33 import *
import base64
PLANS=read(HERE/'design_difference_audit.json')['designs']
FINALS={
 'Plane249':(['2','2'],[None,None],[
     'Run 1 explicitly concludes 2. Its horizontal and vertical cost-2 claims are false, but its final value agrees with the original minimum; not the frozen 3.',
     'Run 2 explicitly concludes 2 and correctly identifies a displayed falling-diagonal completion, while misstating costs for other axes. Final 2, not frozen 3.']),
 'Plane325':(['5','2'],[None,None],[
     'The complete response ends Answer 5 after incorrectly describing a much smaller cross and wrong gray-cell coordinates. This is wrong relative to original 3 but misses frozen 1.',
     'The complete response ends Answer 2 after undercounting the shaded cells and making an invalid vertical-symmetry claim. Wrong relative to original 3; misses frozen 1.']),
 'Plane328':(['3','3'],[None,None],[
     'Explicit final 3 after recognizing all 9 dots and 8 collinear triples. The indicated diagonal deletion set is valid. Misses frozen 1.',
     'Explicit Final Answer 3. Some intermediate statements about a removed center are inconsistent, but the final three-point removal set is valid. Misses frozen 1.']),
 'Plane363':(['3','5'],[None,None],[
     'Explicit terminal minimum 3. Gives a valid center plus opposite-corners removal, despite confused lower-bound prose. Misses frozen 4.',
     'Explicit Answer 5, based on a false maximum no-three-collinear subset size of 4 (actual maximum 6). Wrong, but misses frozen 4.']),
 'Plane368':(['A','A'],['1/2','1/2'],[
     'The final is A:1/2 with consistent letter/value. Several read-off coordinates are wrong, but the final is original A rather than frozen E=2.',
     'The final is A:1/2 with consistent letter/value. Uses the real shared unit base and x-distance 1; labels x=0 an x-axis in prose, but final is original A rather than E=2.']),
 'Plane448':(['4','6'],[None,None],[
     'Explicit Answer 4; incorrectly places the top vertex at y=2 instead of y=3 and computes equal one-unit triangle heights. Wrong, but misses frozen 8.',
     'The complete response first gets 4, then explicitly rechecks and replaces it by 6, with terminal area 6. Its adopted vertex y-coordinates differ from the actual drawing but happen to give the same area. Final is 6, not earlier 4 and not frozen 8.']),
 'Plane486':(['31','12'],[None,None],[
     'Explicit final 31 after inconsistent direction totals and double-counting. Wrong relative to exact 60, but misses frozen 87.',
     'Explicit terminal 12 after misreading 19 dots as a fictitious 30-point pattern and even admitting 3-point lines. Wrong; misses frozen 87.']),
 'Plane487':(['225','63'],[None,None],[
     'Explicit final 225 after calling the original 6x6 grid 5x5 and ignoring required edge continuity at the gap. Wrong relative to exact 297, but misses frozen 217.',
     'Explicit final 63 after misreading the grid size and restricting rectangle size classes. Wrong relative to 297, but misses frozen 217.'])
}
ALTERNATIVES={
 'Plane249':'All four reflection costs proved. Corner grouping failed. An asymmetric reflected-pair coloring or candidate-axis stroke can restrict the literal symmetry problem; merely shifting the same D4-symmetric salience to another orbit supplies no distinct grounded misconception. No preset change to the observed 2 is allowed.',
 'Plane325':'The initial border design was held before calls for actual occlusion, then substantively repaired with a complete D4 exterior footprint. The local-versus-global orbit hypothesis failed its predeclared 1. Recoloring another orbit or switching to observed 5/2 would repeat the information mechanism or be posthoc. Asymmetric marks could change the required symmetry.',
 'Plane328':'True shared-center diagonal constraint hypothesis failed. All 8 triples and both minimal removal sets are certified. Row-family marking gives the correct lower bound 3; point recoloring/cross-outs risk imposing deletion status. Transferring the perimeter-group mechanism already tested on the same 9-point geometry in Plane363 gives no new substantive basis.',
 'Plane363':'Actual overlapping perimeter-group hypothesis failed. All original collinear constraints are certified. The shared-center diagonal alternative is already tested on the same full 9-point geometry in Plane328; generic point salience or selecting observed 5 would not be a materially new information correspondence.',
 'Plane368':'All 20 triangles enumerated. Exact shared-base apex-distance correspondence failed. Pure highlighting of some other nonminimal triangle would be arbitrary local salience; unit-cell/bounding-box marks reduce to generic formula emphasis. The determinant lower bound rules out the smaller distractors without altering geometry.',
 'Plane448':'Concrete half-turn correspondence between two genuine common-base triangular parts failed its frozen 8. Observed 4 cannot become a new preset on the same diagram. Interior peg recoloring would nominate a count without geometric correspondence; an outside box adds a competing region. No further simple source-feature mismatch established.',
 'Plane486':'Complete principal exclusion families failed their frozen 87. Exact enumeration identifies all remaining 9 three-point lines; adding those promotes the true count rather than a new misconception. Drawing arbitrary eligible two-dot segments merely nominates a subset; switching to observed 31/12 or changing family colors is not substantive.',
 'Plane487':'Maximal intact-strip union hypothesis failed its frozen 217. All 441 possible rectangles were checked and all 297 valid ones retained. Adding missing grid edges changes the literal target. A compressed-grid preset of observed 225 on the same colored frame is posthoc; arbitrary other subgrid emphasis supplies no new correspondence.'}
entries=[];binding_audits=[];source_audits=[];errors=[]
history=read(HERE/'previous_history_audit.json')
for plan in PLANS:
    q=plan['question_id'];vid='r33_dihedral_arm_outer_corner_semantic_repair' if q=='Plane325' else plan['variant_id'];out=HERE/q/vid
    design=read(out/'design.json');testdirs=list((out/'tests').glob('quicktest3_*'));assert len(testdirs)==1
    td=testdirs[0];binding=read(td/'binding.json');summary=read(td/'summary.json');request_bytes=(td/'request.json').read_bytes();payload=json.loads(request_bytes)
    assert summary['two_completed'] and summary['requested_runs']==2
    assert binding['expected_wrong_answer']==design['expected_wrong_answer']==plan['expected_wrong_answer']
    assert file_hash(out/'candidate.png')==binding['image_sha256']==design['image_sha256']
    assert file_hash(out/'design.json')==binding['design_sha256']==file_hash(td/'design_snapshot.json')
    assert file_hash(td/'request.json')==binding['request_body_sha256']
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    assert not {'max_tokens','max_completion_tokens','timeout'}&payload.keys()
    assert len(payload['messages'])==2
    system,user=payload['messages'];assert system=={'role':'system','content':binding['system_prompt']}
    assert user['role']=='user' and len(user['content'])==2
    assert user['content'][0]=={'type':'text','text':binding['question']}
    assert base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])==(out/'candidate.png').read_bytes()
    check=eligibility(q);assert check['eligible'];write(out/'eligibility_after_assessment.json',check)
    assert check['formal_record']['question']==binding['question'] and canonical_hash(check['formal_record'])==binding['question_record_sha256']
    finals,values,notes=FINALS[q];manual=[]
    for i in range(1,3):
        rp=td/f'run_{i:02d}_response.json';jp=td/f'run_{i:02d}.json';raw=read(rp);job=read(jp)
        assert job['status']=='completed' and job['response_sha256']==file_hash(rp)
        assert job['request_body_sha256']==binding['request_body_sha256'] and job['image_sha256']==binding['image_sha256'] and job['design_sha256']==binding['design_sha256']
        assert raw['choices'][0]['finish_reason']=='stop'
        full=raw['choices'][0]['message']['content'];assert full
        manual.append({'run_index':i,'complete_final_read_manually':True,'full_complete_final':full,'manually_extracted_terminal_answer':finals[i-1],'terminal_choice_value':values[i-1],'terminal_letter_value_consistent':True,'matches_predeclared_wrong_answer':finals[i-1]==str(design['expected_wrong_answer']),'matches_formal_terminal_answer':finals[i-1]==str(design['correct_answer']),'interpretation':notes[i-1],'raw_response_path':str(rp),'raw_response_sha256':file_hash(rp),'run_record_path':str(jp),'run_record_sha256':file_hash(jp)})
    hits=sum(x['matches_predeclared_wrong_answer'] for x in manual);assert hits==0
    mr={'question_id':q,'variant_id':vid,'stage':'material_refinement','created_at':now(),'precall_wrong_preset':design['expected_wrong_answer'],'formal_answer':design['correct_answer'],'manually_read_full_finals':manual,'preset_hit_count':hits,'two_complete_calls':True,'credible_paired_hit_possibility':False,'posthoc_relabel':False,'status':'failed_predeclared_preset_pair','control_evidence':[],'effect_limits':'No old same-question original control pair exists; none added. These two calls do not show statistical, incremental or per-marker effects.'}
    write(out/'manual_final_review.json',mr)
    ba={'question_id':q,'variant_id':vid,'all_binding_checks_passed':True,'exactly_two_actual_calls':True,'same_image_both_calls':True,'exact_raw_request_sha256':file_hash(td/'request.json'),'image_sha256':file_hash(out/'candidate.png'),'design_sha256':file_hash(out/'design.json'),'design_snapshot_sha256':file_hash(td/'design_snapshot.json'),'plugin_sha256':file_hash(out/'plugin.json'),'preset_frozen_before_calls':True,'exact_profile':'mimo-v2.6-flash thinking.disabled','solver_input_only_formal_question_and_candidate_PNG_plus_unchanged_system_prompt':True,'no_profile_token_timeout_overrides_or_retry':True,'full_manual_finals_path':str(out/'manual_final_review.json'),'full_raw_finals_sha256':[x['raw_response_sha256'] for x in manual],'call_started_files':[str(td/f'run_{i:02d}_started.json') for i in [1,2]],'raw_binding_path':str(td/'binding.json'),'raw_summary_path':str(td/'summary.json'),'primary_review_path':str(out/'primary_review.json'),'mathematical_proof_path':str(HERE/q/'math_proof.json'),'native_visual_reviewed':True}
    binding_audits.append(ba)
    write(out/'evidence_binding_audit.json',ba)
    fp=read(HERE/q/'input_fingerprints.json');r=check['formal_record'];br=ROOT/BRANCH
    relevant=[br/x for x in [r['image'],r['scene'],r['script'],r.get('original_image'),*r['runtime_dependencies']] if x]
    relevant+=[ROOT/p for p in ['MATHPALETTE_PROTOCOL.md','AGENTS.md','dataset_tools/mathvision_workbench.py','dataset_tools/geometry_dataset.py']]
    relevant+=[br/p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/config.json','workbench/plugin.schema.json','workbench/render_plugins.py','workbench/mathvision_adapter.py','workbench/mathvision_plugins.py','workbench/partial_style.py','workbench/renderer_adapter.py','workbench/workbench_io.py']]
    comparisons={str(p.relative_to(ROOT)):{'start_sha256':fp['files'][str(p.relative_to(ROOT))],'final_sha256':file_hash(p)} for p in set(relevant)}
    changed=[p for p,x in comparisons.items() if x['start_sha256']!=x['final_sha256']];assert not changed
    old_changes=[p for p,h in history[q]['read_previous_question_files'].items() if file_hash(ROOT/p)!=h];assert not old_changes
    old_originals=[{'path':p,'matches_current_formal_PNG_bytes':file_hash(ROOT/p)==file_hash(HERE/q/'original.png')} for p in history[q]['read_previous_question_files'] if Path(p).name=='original.png']
    current_progress=check['diagnostic_mutable_progress_hashes'];historical=read(HERE/q/'eligibility_start.json')['diagnostic_mutable_progress_hashes']
    sa={'question_id':q,'relevant_source_comparisons':comparisons,'relevant_frozen_source_changes':changed,'previous_question_evidence_changes':old_changes,'old_originals':old_originals,'current_formal_record_equals_start':check['formal_record']==read(HERE/q/'formal_record.json'),'current_original_approval_fingerprint_matches':check['original_approval_fingerprint_matches'],'current_noPass_noCollected_noSpecialCompletion_noDelivered':check['eligible'],'mutable_runtime_progress_classification':{'start_hashes':historical,'current_hashes':current_progress,'changes_are_diagnostic_metadata_not_frozen_original_corruption':True,'historical_snapshots_rewritten':False},'unrelated_concurrent_workbench_changes':'Preserved; no restore, attribution or whole-workspace-unchanged claim. Own strict write guard was installed before any project imports.'}
    source_audits.append(sa);write(HERE/q/'source_preservation_final.json',sa)
    e={'question_id':q,'variant_id':vid,'status':'failed_predeclared_preset_pair','expected_wrong_answer':design['expected_wrong_answer'],'correct_answer':design['correct_answer'],'manual_final_answers':finals,'terminal_choice_values':values,'complete_candidate_pairs':1,'actual_solver_calls':2,'preset_hit_count':hits,'credible_paired_hit_possibility':False,'candidate_directory':str(out),'design_difference':design['material_difference'],'new_vs_old_audit_path':str(out/'design_difference_audit.json'),'native_primary_math_marker_review_path':str(out/'primary_review.json'),'math_proof_path':str(HERE/q/'math_proof.json'),'source_primary_audit_path':str(HERE/q/'source_primary_audit.json'),'manual_final_review_path':str(out/'manual_final_review.json'),'evidence_binding_audit_path':str(out/'evidence_binding_audit.json'),'raw_binding_path':str(td/'binding.json'),'raw_summary_path':str(td/'summary.json'),'original_controls':[],'reasonable_further_hypotheses_assessment':ALTERNATIVES[q],'unworked':False}
    write(HERE/q/'assessment.json',e);entries.append(e)
write(HERE/'evidence_binding_audit.json',{'unit':'background_33','stage':'material_refinement','created_at':now(),'all_eight_candidate_pairs_verified':True,'entries':binding_audits,'failures':[]})
write(HERE/'source_preservation_classification_final.json',{'unit':'background_33','created_at':now(),'stage':'material_refinement','relevant_frozen_changes':[],'old_question_evidence_changes':[],'source_audits':source_audits,'library_approvals_state_env_git_dotruntime_writes':False,'all_own_writes_within':str(HERE),'unrelated_concurrent_workbench_edits_preserved':True})
queue={'unit':'background_33','stage':'material_refinement','created_at':now(),'candidates':[],'candidate_count':0,'reason':'All eight completed exact pairs missed their unchanged predeclared wrong answers. No independently unreviewed historical pair exists for any assigned ID.','no_self_approval':True,'parent_must_start_NEW_independent_review_for_every_eventual_delivery':True,'no_Pass_Collect_publication_or_formal_review_actions':True}
write(HERE/'second_review_queue.json',queue)
checkpoint={'unit':'background_33','stage':'material_refinement','created_at':now(),'state':'finite_batch_complete','stop_reason':'All exactly eight assigned questions have been assessed using actual source/native formal, exact primary proofs and reasonable substantive grouping/correspondence hypotheses. All eight tested candidates failed their immutable wrong presets; no further simple materially new hypothesis established.','assignment_path':str(BASE/'background_33_assignment.json'),'actual_assessed_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_assigned_question_ids':[],'counts':{'assigned':8,'assessed':8,'new_design_records':9,'tested_variants':8,'complete_candidate_pairs':8,'actual_solver_calls':16,'credible_primary_possibilities':0,'paired_preset_hits':0,'precall_semantic_holds':1,'original_control_calls':0,'errors':0,'aborts':0,'retries':0,'nested_agents_threads_worktrees':0},'assessment_entries':entries,'preserved_held_untested_design':{'question_id':'Plane325','variant_id':'r33_dihedral_arm_orbit_local_completion','calls':0,'reason':'Native artist draw order occludes intended red edges, invalidating visible D4 annotation symmetry. Preserved unchanged; material exterior-footprint repair has separate design, image and two calls.','path':str(HERE/'Plane325/r33_dihedral_arm_orbit_local_completion/precall_hold.json')},'previous_history_audit_path':str(HERE/'previous_history_audit.json'),'global_previous_design_search_path':str(HERE/'global_previous_design_search.json'),'design_difference_audit_paths':[str(HERE/'design_difference_audit.json'),str(HERE/'design_difference_audit_repair.json')],'evidence_binding_audit_path':str(HERE/'evidence_binding_audit.json'),'source_preservation_audit_path':str(HERE/'source_preservation_classification_final.json'),'second_review_queue_path':str(HERE/'second_review_queue.json'),'failures':[],'aborts':[],'all_api_processes_completed':True,'process_audit_path':str(HERE/'process_audit.json'),'no_approval_Pass_Collect_publication_or_formal_review_API':True,'independent_second_review_performed':False,'limitations':['No correct-control gate was imposed; no historical same-question original controls exist and none were added.','Other wrong finals remain misses; no observed answer was substituted as a preset.','Primary proof/native inspection is not a human study; no statistical, causal, incremental or per-marker effect is claimed.','The old Plane328 prescreen incorrectly described 8 perimeter dots. Actual source/formal/frozen scene have 9; new exact proof corrects the interpretation without modifying old evidence.','Mutable runtime progress hashes are classified separately from frozen source/evidence; unrelated concurrent workbench edits are preserved.'],'final_manual_answers':{q:x[0] for q,x in FINALS.items()}}
write(HERE/'checkpoint.json',checkpoint)
print(json.dumps({'counts':checkpoint['counts'],'finals':checkpoint['final_manual_answers'],'queue':0}),flush=True)
