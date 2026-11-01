from tools_local import *
manual={
 ('Solid111','local_corner_to_wrong_net'):[('B',False,'Clear final B; expected D occurs only as a rejected option in this run.'),('D',True,'Clear final D; one target hit only.')],
 ('Solid187','false_cap_notch_partner'):[('D',False,'Clear final D, expected B explicitly rejected.'),('C',False,'Clear final C; expected B explicitly rejected.')],
 ('Solid144','reflected_three_edge_frame'):[('D',False,'Terminal D is justified as only X, contradictory with D=None of these; not the expected B either.'),('B',False,'Terminal B is repeatedly paired with X/Y or X/Y/Z and acknowledged option mismatch. It does not unambiguously endorse B=X and Z. Do not count as a hit.')],
 ('Solid187','paired_but_adjacent_edge_holes'):[('D',True,'Complete final conclusion explicitly selects D; one target hit.'),('C',False,'Complete final C; no D target hit.')]
}
reviews=[];assessed=[];source_checks=[]
for qid in ASSIGNED:
    initial=json.loads((TASK/qid/'frozen_inputs.json').read_text(encoding='utf-8'))
    final=AD.frozen_inputs(qid);assert initial==final,qid
    check=eligibility(qid);assert check['eligible'],check
    source_checks.append({'question_id':qid,'frozen_inputs_unchanged':True,'original_copy_equals_formal_bytes':(TASK/qid/'original.png').read_bytes()==AD.original_paths[qid].read_bytes(),'eligibility_at_completion':check})
    variants=[]
    for (q,v),runs in manual.items():
        if q!=qid:continue
        folder=TASK/qid/v;test=next((folder/'tests').glob('quicktest3_*'));summary=json.loads((test/'summary.json').read_text(encoding='utf-8'));design=json.loads((folder/'design.json').read_text(encoding='utf-8'))
        assert summary['two_completed']
        entries=[]
        for ix,(letter,hit,note) in enumerate(runs,1):
            job=json.loads((test/f'run_{ix:02d}.json').read_text(encoding='utf-8'))
            assert job['status']=='completed' and not job['truncated'] and job['finish_reason']=='stop'
            entries.append({'run_index':ix,'manual_final_letter':letter,'manual_unambiguous_predeclared_target_hit':hit,'manual_note':note,'complete_final_manually_read':True,'raw_final_path':str(test/f'run_{ix:02d}.json'),'raw_response_path':str(test/f'run_{ix:02d}_response.json'),'response_sha256':job['response_sha256']})
        value={'question_id':qid,'variant_id':v,'status':'tested_rejected_no_two_target_hits','expected_wrong_answer_before_both_calls':design['expected_wrong_answer'],'formal_correct_answer':AD.records[qid]['answer'],'same_frozen_candidate_png_sha256':file_hash(folder/'candidate.png'),'same_immutable_design_sha256':file_hash(folder/'design.json'),'manual_final_letters':[x[0] for x in runs],'unambiguous_target_hits':sum(x[1] for x in runs),'two_target_hits':False,'manual_runs':entries,'design_path':str(folder/'design.json'),'plugin_path':str(folder/'plugin.json'),'candidate_path':str(folder/'candidate.png'),'fresh_context_path':str(folder/'context.json'),'render_check_path':str(folder/'render_check.json'),'primary_review_path':str(folder/'primary_visual_math_review.json'),'binding_path':str(test/'binding.json'),'summary_path':str(test/'summary.json'),'request_path':str(test/'request.json'),'marker_roles':design['marker_roles'],'mechanism':design['mechanism'],'no_retries_or_retargeting':True}
        write(folder/'manual_final_review.json',value);reviews.append(value);variants.append(value)
    screen=TASK/qid/'primary_prescreen.json'
    assessed.append({'question_id':qid,'branch':'SolidGeometry','fresh_formal_noop_pixel_match':True,'actual_original_png_viewed':True,'status':'tested_no_credible_two_hit' if variants else 'prescreen_only_rejected','variant_count':len(variants),'variants':variants,'primary_prescreen_path':str(screen) if screen.exists() else None,'formal_record_path':str(TASK/qid/'formal_record.json'),'source_fingerprints_path':str(TASK/qid/'frozen_inputs.json'),'fresh_context_path':str(TASK/qid/'context.json')})
write(TASK/'manual_final_reviews.json',reviews)
write(TASK/'source_preservation_audit.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'question_count':len(ASSIGNED),'all_frozen_inputs_unchanged':True,'questions':source_checks})
write(TASK/'second_review_queue.json',{'status':'No Solid candidate has two unambiguous target hits','possible_count':0,'possible_candidates':[],'rejected_variants':reviews,'no_independent_second_review_performed':True})
write(TASK/'checkpoint.json',{'created_at':datetime.now(timezone.utc).isoformat(),'status':'FINITE_SOLID_SUBSET_COMPLETE','assigned_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'assessed_question_count':8,'prescreen_only_question_ids':[q['question_id'] for q in assessed if not q['variants']],'saved_candidate_design_count':4,'complete_candidate_pair_tests':4,'completed_candidate_calls':8,'optional_original_control_pair_tests':0,'optional_original_control_completed_calls':0,'total_completed_calls':8,'aborted_or_incomplete_calls':0,'possible_two_hit_count':0,'assessed_questions':assessed,'manual_final_reviews_path':str(TASK/'manual_final_reviews.json'),'source_preservation_audit_path':str(TASK/'source_preservation_audit.json'),'second_review_queue_path':str(TASK/'second_review_queue.json'),'no_live_own_api_processes':True,'process_confirmation':'All four run_candidate.py sessions 35304,61904,63528,81393 exited after both calls; final independent OS process snapshot saved by unit aggregator.','limits':['Solid144 terminal option letters are internally inconsistent with named object sets and are not target hits.','Prescreen-only Solid105 and Solid149 do not have completed independent full uniqueness proofs; no candidates or calls were made for them.','No original controls, per-marker ablations or human performance measurements for Solid experiments.','Primary reviews are not independent second reviews.'],'next_recommendations':['Do not retest any of these four frozen images.','Retain all failed designs and manual contradictions.','Parent must independently review Plane possibilities in separate new tasks; no Solid possibility is queued.'],'approval_status':'No Pass/Collect/review API/publication performed'})
print(json.dumps({'assessed':8,'designs':4,'pairs':4,'calls':8,'possible':0}))
