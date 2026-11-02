from tools20 import *
import base64

manual={
 ('Plane393','first_flip_outer_feature_binding'):{'finals':['C','D'],'notes':['Complete final explicitly C. It mislocates source/result triangles and omits the correct final half-turn fill arrangement. Preset A is not the final answer.','Complete final explicitly D. It invents diagonal corner fill placements, then describes D as grey top-left/dark bottom-right, which does not accurately describe D. Not preset A.']},
 ('Plane416','cut_and_fold_bevel_binding'):{'finals':['C','C'],'notes':['Complete final C after wrongly asserting eight layers necessarily make an octagonal hole and misdescribing C as an octagon. It explicitly dismisses E colored lines. Not preset E.','Complete final C:C after conflicting fold/triangle/cut descriptions and calling C a diamond. It explicitly rejects E because of its colored edge. Not preset E.']},
 ('Plane431','crest_face_to_sharp_locus_binding'):{'finals':['B','A'],'notes':['Complete final B. It incorrectly transfers sharp polyline corners to the center locus and misdescribes some option features. One target-letter hit only; no paired claim.','Complete final A. It correctly mentions rounded crests but falsely allows circular dips at concave valleys. Not preset B.']},
 ('Plane408','ribbon_identity_top_edge_binding'):{'finals':['E','B'],'notes':['Complete final E:0cm. Its false formula80+maximum+sum(lengths) depends only on the set of ribbons, producing the intended conservation error. One target hit only.','Complete final B:50cm. Its intermediate perimeter arithmetic is wrong and it assumes a degenerate shortest length to recover the answer; correct final letter/value does not establish sound reasoning. Not preset E.']},
 ('Plane431','wheel_circle_to_concave_arc_binding'):{'finals':['C','B'],'notes':['Complete final C. It invents flat valley transitions and misdescribes C peaks as rounded. Not preset A.','Complete final B:B. It gives the correct convex/concave contact rule but assigns it to wrong diagram B instead of E; final letter is B. Not preset A.']}
}
candidate_records=[];binding_audits=[];fullmanual=[]
for (qid,vid),m in manual.items():
    out=HERE/qid/vid;d=json.loads((out/'design.json').read_text(encoding='utf-8'))
    summaries=list((out/'tests').glob('quicktest3_*/summary.json'));assert len(summaries)==1
    sp=summaries[0];s=json.loads(sp.read_text(encoding='utf-8'));ep=sp.parent
    assert s['two_completed'] and s['requested_runs']==2 and len(s['results'])==2
    binding=json.loads((ep/'binding.json').read_text(encoding='utf-8'))
    reqbytes=(ep/'request.json').read_bytes();request=json.loads(reqbytes)
    formal=next(r for r in rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']==qid)
    assert set(request)=={'model','stream','thinking','messages'}
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
    assert request['messages']==[
      {'role':'system','content':s['system_prompt']},
      {'role':'user','content':[{'type':'text','text':formal['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode((out/'candidate.png').read_bytes()).decode('ascii')}}]}
    ]
    assert file_hash(out/'candidate.png')==d['image_sha256']==binding['image_sha256']==s['image_sha256']
    assert file_hash(out/'design.json')==binding['design_sha256']==s['design_sha256']
    assert (ep/'design_snapshot.json').read_bytes()==(out/'design.json').read_bytes()
    assert (out/'candidate.png').read_bytes()==(out/'repeat.png').read_bytes()
    assert file_hash(ep/'request.json')==binding['request_body_sha256']==s['request_body_sha256']
    assert s['question_record_sha256']==canonical_hash(formal)
    assert binding['expected_wrong_answer']==d['expected_wrong_answer']
    assert s['reference_quick_test_sha256']==file_hash(ROOT/'PlaneGeometry/workbench/quick_test.py')
    assert json.loads((out/'api_process_finished.json').read_text(encoding='utf-8'))['two_completed']
    rawchecks=[];reviewruns=[]
    for index,(r,final,note) in enumerate(zip(s['results'],m['finals'],m['notes']),1):
        rp=ep/f'run_{index:02d}_response.json';raw=json.loads(rp.read_bytes())
        assert r['status']=='completed' and r['finish_reason']=='stop'
        assert raw['choices'][0]['message']['content']==r['answer']
        assert r['response_sha256']==file_hash(rp)
        assert r['image_sha256']==binding['image_sha256'] and r['design_sha256']==binding['design_sha256'] and r['request_body_sha256']==binding['request_body_sha256']
        hit=final==str(d['expected_wrong_answer'])
        reviewruns.append({'run_index':index,'entire_final_manually_read':True,'complete_final_text':r['answer'],'final_answer':final,'matches_predeclared_wrong_answer':hit,'manual_notes':note,'raw_response_path':str(rp.relative_to(ROOT)),'raw_response_sha256':file_hash(rp),'finish_reason':r['finish_reason'],'status':r['status']})
        rawchecks.append({'run_index':index,'exact_image_design_request_bindings':True,'raw_response_sha256':file_hash(rp)})
    paired=all(r['matches_predeclared_wrong_answer'] for r in reviewruns)
    assert not paired
    mr={'question_id':qid,'candidate_id':qid+'/'+vid,'review_type':'PRIMARY manual reading only','reviewed_at':now(),'expected_wrong_answer_frozen_before_pair':d['expected_wrong_answer'],'correct_answer':formal['answer'],'both_complete_finals_read_manually':True,'runs':reviewruns,'paired_target_hit':paired,'status':'rejected_preset_pair_not_met','narrative_limit':'Incorrect intermediate geometry/labels retained verbatim; no requirement for identical narratives is imposed and no reasoning error is recast as target hit.','evidence_summary_path':str(sp.relative_to(ROOT))}
    write(out/'manual_finals_review.json',mr);fullmanual.append(mr)
    audit={'candidate_id':qid+'/'+vid,'binding_path':str((ep/'binding.json').relative_to(ROOT)),'summary_path':str(sp.relative_to(ROOT)),'exact_request_only_original_question_and_one_candidate_png':True,'correct_answer_preset_intent_parameters_not_sent':True,'exact_two_real_calls':True,'same_png_and_immutable_design_for_both':True,'no_profile_max_tokens_or_timeout_override':True,'unchanged_harness_sha256':file_hash(BASE/'harness/quicktest3_isolated.py'),'harness_cache_only_redirected_to_own_root':True,'no_retries':True,'repeat_png_byte_identical':True,'raw_checks':rawchecks,'preset_sha256':file_hash(out/'design.json'),'image_sha256':file_hash(out/'candidate.png'),'plugin_sha256':file_hash(out/'plugin.json')}
    binding_audits.append(audit)
    candidate_records.append({'question_id':qid,'candidate_id':qid+'/'+vid,'design_path':str((out/'design.json').relative_to(ROOT)),'plugin_path':str((out/'plugin.json').relative_to(ROOT)),'candidate_png':str((out/'candidate.png').relative_to(ROOT)),'expected_wrong_answer':d['expected_wrong_answer'],'correct_answer':formal['answer'],'manual_final_answers':m['finals'],'two_completed':True,'paired_target_hit':False,'status':'rejected_preset_pair_not_met','binding_path':audit['binding_path'],'evidence_path':str(sp.relative_to(ROOT)),'manual_finals_path':str((out/'manual_finals_review.json').relative_to(ROOT)),'primary_review_path':str((out/'primary_review.json').relative_to(ROOT)),'primary_source_audit_path':str((HERE/qid/'source_primary_audit.json').relative_to(ROOT)),'marker_bindings_path':str((out/'marker_bindings.json').relative_to(ROOT)),'source_inputs_path':str((out/'source_inputs.json').relative_to(ROOT)),'image_sha256':audit['image_sha256'],'design_sha256':audit['preset_sha256']})
write(HERE/'candidate_evidence_audit.json',{'created_at':now(),'candidates':binding_audits,'all_exact_bindings_valid':True})
write(HERE/'complete_manual_finals.json',fullmanual)

source_files={};before_conflicts=[]
for qid in ASSIGNED:
    snap=json.loads((HERE/qid/'input_fingerprints.json').read_text(encoding='utf-8'))
    for p,digest in snap['files'].items():
        if p in source_files and source_files[p]!=digest:before_conflicts.append(p)
        source_files[p]=digest
frozen_changes=[];diagnostic_changes=[]
for relative,digest in source_files.items():
    p=ROOT/relative;actual=file_hash(p) if p.exists() else None
    if actual!=digest:
        item={'path':relative,'before':digest,'now':actual}
        if relative=='provenance/approvals.json':diagnostic_changes.append({**item,'classification':'aggregate approval file; individual current approval checked separately'})
        else:frozen_changes.append(item)
assert not frozen_changes
finaleligibility=[]
for qid in ASSIGNED:
    e=eligibility(qid);assert e['eligible'];write(HERE/qid/'eligibility_final.json',e);finaleligibility.append({'question_id':qid,'eligible':True,'individual_original_fingerprint_matches':e['original_approval_fingerprint_matches']})
other_allocations=[]
for p in BASE.glob('background_*_assignment.json'):
    if p.name=='background_20_assignment.json':continue
    other=json.loads(p.read_text(encoding='utf-8-sig'))
    overlaps=sorted(set(ASSIGNED)&set(other['question_ids']))
    if overlaps:other_allocations.append({'assignment':p.name,'overlaps':overlaps})
assert not other_allocations
write(HERE/'source_preservation_audit.json',{'created_at':now(),'scope':'Individually assigned MathVision original inputs, dependencies and current eligibility; not whole-workspace equality.','distinct_frozen_paths_checked':len(source_files),'frozen_input_changes':frozen_changes,'aggregate_diagnostic_changes':diagnostic_changes,'before_snapshot_conflicts':before_conflicts,'all_current_individual_approvals_and_eligibility_valid':True,'per_question':finaleligibility,'reservation_overlap_with_other_assignments':other_allocations,'python_write_guard':'runtime_isolation installed before project rendering imports plus strict own-root audit hook; harness source unchanged and cache global redirected before module mkdir.','formal_or_review_mutations_performed':False,'external_unrelated_workbench_changes':'Preserved; no restore, reset, clean, whole-workspace hash equality claim, or global summary writes.'})

checkpoint={'unit':'background_20','created_at':now(),'status':'finite_batch_complete','stop_reason':'All20 assigned questions assessed; all saved candidate pairs completed and manually reviewed.','assigned_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'counts':{'assigned_questions':20,'assessed_questions':20,'prescreen_only_questions':16,'designed_questions':4,'saved_designs':5,'complete_candidate_pairs':5,'actual_candidate_API_calls':10,'original_control_calls':0,'credible_paired_hit_possibilities':0,'errors':0,'aborted_calls':0,'retries':0,'untested_saved_candidates':0},'candidates':candidate_records,'prescreen_assessments_path':str((HERE/'assessments.json').relative_to(ROOT)),'source_audit_path':str((HERE/'source_preservation_audit.json').relative_to(ROOT)),'binding_audit_path':str((HERE/'candidate_evidence_audit.json').relative_to(ROOT)),'full_manual_finals_path':str((HERE/'complete_manual_finals.json').relative_to(ROOT)),'process_audit_path':str((HERE/'process_audit.json').relative_to(ROOT)),'second_review_queue_path':str((HERE/'second_review_queue.json').relative_to(ROOT)),'original_controls':{'run':False,'reason':'No candidate reached the predeclared paired target. Controls are not an extra hard gate and none were needed for this negative checkpoint.'},'errors':[],'aborts':[],'controls':[],'limits':['Two calls per design are not a statistical/human/causal study.','No per-marker causal ablation or original controls.','Source and candidate evidence have primary review only. Plane393 annotation-as-card-ink caveat retained.','No candidate is qualified or recommended for delivery; allfive fail their own predeclared pairs.','Parent must start a NEW independent reviewer before any future delivery.'],'next_recommendations':['Do not retry these same question/image/preset tuples or select successes across designs.','All20 allocations are assessed; parent can aggregate this terminal coverage checkpoint.','No review or delivery is proposed.'],'no_live_own_API_processes':True,'process_completion_evidence':'Allfive api_process_finished.json exist, with two_completed true; final PID/command audit in process_audit.json.','formal_library_state_approvals_env_runtime_git_modified_by_this_unit':False,'nested_agents_threads_worktrees_started':False}
write(HERE/'second_review_queue.json',{'unit':'background_20','created_at':now(),'review_type_required':'NEW independent second reviewer started by parent before any delivery','assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'credible_paired_hit_possibilities':[],'candidates':[],'candidate_count':0,'reason':'None of the five predeclared paired targets was met. All raw complete finals and rejected designs remain immutable in checkpoint.','checkpoint':'checkpoint.json','rejected_candidates':candidate_records,'approval_or_publication_performed':False})
assert (HERE/'process_audit.json').exists()
write(HERE/'checkpoint.json',checkpoint)
report='background_20 finite checkpoint\n20 assigned /20 assessed;16 prescreen-only;4 designed questions;5 saved designs.\n5 complete pairs /10 real quicktest3 calls;0 controls, errors, aborts or retries.\n0 credible paired-target candidates; empty second_review_queue.json.\nManual finals: Plane393 A-preset C/D; Plane416 E-preset C/C; Plane431 B-preset B/A; Plane408 E-preset E/B; Plane431 A-preset C/B. No unchanged retests.\nAll presets, exact raw bindings, full manual finals, primary proofs/marker roles/source/visual audits retained.\nAssigned original frozen inputs/current eligibility rechecked; no formal, approval, Pass/Collect, .env, .runtime, .git or global summary writes. Concurrent unrelated changes preserved.\nAllfive own API processes finished; final PID/command audit saved. Primary review only; parent NEW independent reviewer required before any future delivery.\n'
with (HERE/'report.txt').open('x',encoding='utf-8') as f:f.write(report)
print(json.dumps(checkpoint['counts']))
