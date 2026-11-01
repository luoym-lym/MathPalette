from tools_local import *
import importlib.util
MANUAL={
('Solid98','front_row_color_correspondence'):(['D','A'],'Neither full final matches presetB. First miscounts colors; second concludes correctA using an incorrect no-reversal rationale. No hit claimed.'),
('Solid119','white_domino_local_column_binding'):(['D','B'],'First explicitly answersD after arguingD impossible despite a possible-construction question; narrative/task polarity contradict. Second explicitly answersB. Pair fails presetD regardless; no credible hit.'),
('Solid127','reflected_cavity_three_feature_frame'):(['D','E'],'Full finalsD/E. Second notices color-order mismatch onC. No presetC hit.'),
('Solid136','row_to_final_panel_misbinding'):(['C','E'],'Full final1 C with a7,b5,c3, final2 E with a6,b4,c7. No letter/value contradiction in finals; neither is presetD.'),
('Solid137','two_white_domino_local_bindings'):(['C','A'],'Full final1 C:C after accepting marked brick matching; full final2 A after rejectingC. Only one presetC answer.'),
('Solid142','orthogonal_cut_feature_swap'):(['A','A'],'Both complete final answers unambiguouslyA. Both narratives explicitly match red/blue folded cuts to A colored hole families. PresetA fixed before both calls; same immutable image and request body. Correct original remainsC.')}
records=[];queue=[];file_failures=[];total_calls=0
for (q,v),(finals,notes) in MANUAL.items():
    folder=TASK/q/v;design=json.loads((folder/'design.json').read_text());render=json.loads((folder/'render_check.json').read_text())
    invocations=list((folder/'tests').glob('*/summary.json'));assert len(invocations)==1
    summary=json.loads(invocations[0].read_text());binding=json.loads((invocations[0].parent/'binding.json').read_text())
    assert summary['two_completed'] and len(summary['results'])==2
    assert file_hash(folder/'candidate.png')==binding['image_sha256']==render['png_sha256']
    assert file_hash(folder/'design.json')==binding['design_sha256']
    assert file_hash(invocations[0].parent/'request.json')==binding['request_body_sha256']
    assert (invocations[0].parent/'design_snapshot.json').read_bytes()==(folder/'design.json').read_bytes()
    request=json.loads((invocations[0].parent/'request.json').read_text())
    assert set(request)=={'model','stream','thinking','messages'}
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert request['messages'][1]['content'][0]=={'type':'text','text':AD.records[q]['question']}
    import base64
    encoded=request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1]
    assert base64.b64decode(encoded)==(folder/'candidate.png').read_bytes()
    assert AD.frozen_inputs(q)==render['frozen_inputs']
    evidence={'question_id':q,'variant_id':v,'manual_full_final_answers':finals,'preset':design['expected_wrong_answer'],'correct_answer':AD.records[q]['answer'],'full_answers_manually_read':True,'manual_notes':notes,'two_completed':True,'raw_binding_path':str(invocations[0].parent/'binding.json'),'summary_path':str(invocations[0]),'complete_run_paths':[str(invocations[0].parent/f'run_{i:02d}.json') for i in [1,2]],'status':'possible_twohit_pending_new_independent_review' if finals==[design['expected_wrong_answer']]*2 else 'complete_pair_preset_missed','candidate_png_path':str(folder/'candidate.png'),'candidate_sha256':file_hash(folder/'candidate.png'),'plugin_path':str(folder/'plugin.json'),'design_path':str(folder/'design.json'),'math_audit_path':design['math_audit_path'],'marker_roles_path':str(folder/'design.json'),'marker_path_bindings_path':str(folder/'marker_path_bindings.json'),'primary_visual_review_path':str(folder/'primary_visual_review.json'),'render_check_path':str(folder/'render_check.json'),'eligibility_before_calls_path':str(folder/'eligibility_immediately_before_calls.json'),'api_calls':2,'approval_status':'Exploratory only; no Pass/Collect/review API or delivery.'}
    write(folder/'manual_result_review.json',evidence)
    primary={'question_id':q,'variant_id':v,'primary_unique_math_proof':design['primary_math'],'all_marks_have_concrete_roles':True,'roles':design['marker_roles'],'roles_note':'Each adjoining unit edge in a colored rail is necessary to retain the actual two/four-unit feature extent. No arbitrary action-count limit; no per-marker statistical necessity claim.','human_clarity':'Actual source/candidate PNGs reviewed; original geometry, all original semantic fills, dimensions, labels, frozen projection and visibility stay unchanged. Added appearance is not an extra mathematical condition.','source_fingerprint_audit_passed':True,'independent_review':False,'review_disposition':evidence['status'],'next_gate':'A NEW parent-launched independent review task is mandatory before any delivery.'}
    if q=='Solid142':
        control=TASK/q/'original_control';csummary_path=next((control/'tests').glob('*/summary.json'));cs=json.loads(csummary_path.read_text());assert cs['two_completed']
        cb=json.loads((csummary_path.parent/'binding.json').read_text());assert file_hash(control/'original.png')==cb['image_sha256']==file_hash(AD.original_paths[q])
        controls={'finals':['C','C'],'full_answers_manually_read':True,'two_completed':True,'raw_binding_path':str(csummary_path.parent/'binding.json'),'summary_path':str(csummary_path),'note':'Both correct-letter original controls use incorrect narrative details (first broad pattern guessing; second falsely says cut at center and holes touch). C/C controls and A/A candidate support an observed paired-answer difference, without proving marker-level causality, human effects or population rates.'}
        write(control/'manual_result_review.json',controls);primary['original_controls']=controls;evidence['original_controls']=controls
        primary['specific_mark_necessity']='Two source notch traces distinguish actual orthogonal cut features. Red A top/bottom holes and blue A left/right holes encode a swapped notch-to-hole-position mapping. Every colored output contour is one of the four actual output-hole features. No generic A outer-frame highlighting, no new hole, no fill change.'
        queue.append({**evidence,'primary_review_path':str(folder/'primary_review.json'),'limits':['Only two candidate calls and two separate original controls.','Both candidate narratives explicitly used color correspondence, but there is no per-marker ablation or human study.','Original controls C/C have flawed narratives.','Primary review only; no qualification or delivery until NEW independent parent review.']})
    write(folder/'primary_review.json',primary)
    records.append(evidence);total_calls+=2
prescreens=[json.loads((TASK/q/'prescreen_review.json').read_text()) for q in ['Solid121','Solid130']]
all_inputs={};eligibility_checks=[]
for q in ASSIGNED:
    frozen=json.loads((TASK/q/'frozen_inputs.json').read_text());assert AD.frozen_inputs(q)==frozen
    eligibility_checks.append(eligibility(q))
    for rel,expected in frozen['files'].items():
        actual=file_hash(ROOT/rel);all_inputs[rel]=expected
        if actual!=expected:file_failures.append(rel)
write(TASK/'source_and_evidence_audit.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'frozen_source_file_count':len(all_inputs),'source_files_sha256':all_inputs,'changed_source_files':file_failures,'candidate_pairs_bound_to_exact_frozen_request_png_and_design':6,'profile':'mimo-v2.6-flash','thinking':{'type':'disabled'},'no_profiles_limits_timeouts_or_retries_added':True,'current_eligibility':eligibility_checks,'no_live_own_API_processes':'All6candidate and1control launcher processes completed normally; separately verify with system process query before root handback.','mutable_progress_files':'Snapshots are diagnostic runtime metadata; originals use dedicated immutable source fingerprints.'})
write(TASK/'second_review_queue.json',{'question_ids':[r['question_id'] for r in queue],'candidate_count':len(queue),'candidates':queue,'independent_review_status':'Not performed by researcher; parent must start NEW independent task.'})
write(TASK/'checkpoint.json',{'unit':'background_06/solid_worker','created_at':datetime.now(timezone.utc).isoformat(),'assigned_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'question_count_assessed':8,'saved_designs':6,'complete_paired_candidates':6,'candidate_api_calls':total_calls,'original_control_api_calls':2,'aborted_or_error_calls':0,'credible_twohit_possibilities':1,'delivered_or_approved':0,'designs':records,'prescreen_only':prescreens,'rejected_untested_designs':[],'unworked_assignments':[],'source_and_evidence_audit_path':str(TASK/'source_and_evidence_audit.json'),'second_review_queue_path':str(TASK/'second_review_queue.json'),'next_recommendations':['Parent starts NEW independent mathematical/visual/evidence review for Solid142 exact frozen bytes.','Retain every failed image/preset and do not rerun unchanged designs.','Do not publish, Pass or Collect from primary analysis.'],'all_own_API_processes_completed':True})
print(json.dumps({'assessed':8,'designs':6,'paired_candidates':6,'candidate_calls':12,'original_control_calls':2,'possible_twohits':1,'queue':str(TASK/'second_review_queue.json')}))
