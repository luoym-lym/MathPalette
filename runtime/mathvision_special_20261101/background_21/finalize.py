from tools import *
import base64,io
from PIL import Image
def sha(b):return hashlib.sha256(b).hexdigest()
manual={
'Plane461':{'finals':['C','D'],'notes':[
'Read the COMPLETE final. It explicitly concludes C after reversing left/right folding incorrectly and describing four outer-corner holes. The trailing list A:A through E:E is a copied options list, not five chosen answers. The explicit narrative final is C, matching the predeclared C for this run only.',
'Read the COMPLETE final. It describes the punch as the exact geometric center despite its actual top-edge y position, derives a central cluster, and explicitly gives Answer D. It does not select C. The predeclared C pair therefore fails.'], 'outcome':'failed_preset_pair'},
'Plane474':{'finals':['C','D'],'notes':[
'Read the COMPLETE final. It explicitly concludes Answer C after inventing a1x1 gap in the staircase, then miscounting the leftover area. The frozen third figure has no such gap and can be tiled. Incidental mentions of D or piece lengths are not final selections. It does not match preset D.',
'Read the COMPLETE final. It calls D a square, claims cutting the five-bar would be required to make a3-wide row, and explicitly gives Final Answer D. This one run matches predeclared D but is mathematically false. The pair fails because run1 selects C.'], 'outcome':'failed_preset_pair'},
'Plane475':{'finals':['3','8'],'notes':[
'Read the COMPLETE final. It counts only the three right-triangle-like types and explicitly concludes3 noncongruent triangles. It also calls a1-by2 right triangle obtuse. It omits5 valid SSS classes. It does not match predeclared7.',
'Read the COMPLETE final. It explicitly concludes Final Answer8, the formal answer. The supporting reasoning is flawed: it counts collinear triples as shapes, assigns inconsistent squared sides, and says6 spanning types while naming5. A correct final value is recorded as correct-final-only, without treating its proof as valid. It does not match predeclared7.'], 'outcome':'failed_preset_pair'}
}
vids={'Plane461':'punch_to_outer_corner_correspondence','Plane474':'four_bar_to_three_wide_edge_binding','Plane475':'equal_base_height_triangle_class_merge'}
binding_audits=[];candidates=[];completed_calls=0;errors=[]
for qid,vid in vids.items():
    folder=HERE/qid/vid;design=json.loads((folder/'design.json').read_text(encoding='utf-8'));plugin=json.loads((folder/'plugin.json').read_text(encoding='utf-8'));record=json.loads((HERE/qid/'formal_record.json').read_text(encoding='utf-8'))
    invs=list((folder/'tests').glob('quicktest3_*'));assert len(invs)==1
    inv=invs[0];binding=json.loads((inv/'binding.json').read_text(encoding='utf-8'));summary=json.loads((inv/'summary.json').read_text(encoding='utf-8'))
    imagebytes=(folder/'candidate.png').read_bytes();designbytes=(folder/'design.json').read_bytes();requestbytes=(inv/'request.json').read_bytes();request=json.loads(requestbytes)
    assert binding['requested_runs']==2 and binding['expected_wrong_answer']==design['expected_wrong_answer']
    assert binding['image_sha256']==sha(imagebytes) and binding['design_sha256']==sha(designbytes)
    assert (inv/'design_snapshot.json').read_bytes()==designbytes
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert set(request)=={'model','stream','thinking','messages'}
    assert len(request['messages'])==2 and request['messages'][0]['role']=='system' and request['messages'][1]['role']=='user'
    user=request['messages'][1]['content'];assert len(user)==2 and user[0]=={'type':'text','text':record['question']}
    assert base64.b64decode(user[1]['image_url']['url'].split(',',1)[1])==imagebytes
    assert sha(requestbytes)==binding['request_body_sha256']
    assert summary['two_completed'] and len(summary['results'])==2
    reviews=[]
    for i,final in enumerate(manual[qid]['finals'],1):
        r=json.loads((inv/f'run_{i:02d}.json').read_text(encoding='utf-8'));raw=(inv/f'run_{i:02d}_response.json').read_bytes();rawjson=json.loads(raw)
        assert r['status']=='completed' and not r['truncated'] and r['finish_reason']=='stop'
        assert r['response_sha256']==sha(raw) and r['image_sha256']==sha(imagebytes) and r['design_sha256']==sha(designbytes) and r['request_body_sha256']==sha(requestbytes)
        assert rawjson['choices'][0]['message']['content']==r['answer']
        reviews.append({'run_index':i,'complete_final_read_manually':True,'complete_final':r['answer'],'manually_extracted_final_answer':final,'matches_predeclared_wrong_answer':final==str(design['expected_wrong_answer']),'matches_formal_final_answer':final==str(record['answer']),'interpretation':manual[qid]['notes'][i-1],'raw_response_path':str(inv/f'run_{i:02d}_response.json'),'raw_response_sha256':sha(raw),'run_record_sha256':file_hash(inv/f'run_{i:02d}.json')})
        completed_calls+=1
    paired=all(r['matches_predeclared_wrong_answer'] for r in reviews);assert not paired
    write(folder/'manual_final_review.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':design['expected_wrong_answer'],'correct_answer':record['answer'],'both_complete_finals_read_manually':True,'reviews':reviews,'two_completed':True,'two_preset_hits':False,'status':manual[qid]['outcome'],'no_retries_or_posthoc_preset_changes':True,'reviewed_at':now()})
    audit={'question_id':qid,'variant_id':vid,'invocation_count':1,'actual_completed_calls':2,'same_exact_png_both_calls':True,'immutable_predeclared_design_snapshot_equal':True,'request_contains_only_original_question_and_candidate_png_plus_existing_system_prompt':True,'profile_model_thinking_exact':True,'no_output_or_timeout_override':True,'raw_bindings_all_verified':True,'png_sha256':sha(imagebytes),'design_sha256':sha(designbytes),'plugin_sha256':file_hash(folder/'plugin.json'),'request_sha256':sha(requestbytes),'baseline_pixel_match':True,'normalized_schema_and_byte_identical_repeat_draw_verified':True,'evidence_directory':str(inv)}
    binding_audits.append(audit)
    candidates.append({'question_id':qid,'variant_id':vid,'status':'failed_preset_pair','expected_wrong_answer':design['expected_wrong_answer'],'correct_answer':record['answer'],'manual_final_answers':manual[qid]['finals'],'complete_pair':True,'preset_hit_count':sum(r['matches_predeclared_wrong_answer'] for r in reviews),'credible_paired_hit_possibility':False,'candidate_directory':str(folder),'design_path':str(folder/'design.json'),'plugin_path':str(folder/'plugin.json'),'image_path':str(folder/'candidate.png'),'render_check_path':str(folder/'render_check.json'),'math_proof_path':str(folder/'math_proof.json'),'primary_review_path':str(folder/'primary_review.json'),'marker_roles':design['marker_roles'],'human_semantics':design['human_semantics'],'source_audit_path':str(HERE/qid/'source_primary_audit.json'),'manual_final_review_path':str(folder/'manual_final_review.json'),'raw_binding_path':str(inv/'binding.json'),'raw_summary_path':str(inv/'summary.json'),'full_manual_finals':reviews,'controls':[],'errors':[],'aborts':[],'requires_no_unchanged_retest':True})
write(HERE/'evidence_binding_audit.json',{'created_at':now(),'all_pass':True,'candidates':binding_audits,'actual_calls':completed_calls,'errors':[],'aborts':[],'unchanged_candidate_retests':0})
# Authoritative per-question preservation. Broad adapter manifest includes the
# entire branch and is retained as diagnostic history, never a whole-workspace gate.
preservation=[];broad_before={};broad_differences=[]
for qid in ASSIGNED:
    folder=HERE/qid;start=json.loads((folder/'eligibility_start.json').read_text(encoding='utf-8'));end=eligibility(qid);write(folder/'eligibility_end.json',end)
    src=json.loads((folder/'source_primary_audit.json').read_text(encoding='utf-8'));changed=[]
    for rel,digest in src['source_files'].items():
        p=ROOT/rel
        if not p.exists() or file_hash(p)!=digest:changed.append(rel)
    current=next(r for r in rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']==qid)
    assert not changed and canonical_hash(current)==src['formal_record_sha256'] and end['eligible']
    assert end['approval']==start['approval']
    preservation.append({'question_id':qid,'current_eligible':True,'formal_record_unchanged':True,'frozen_individual_inputs_unchanged':True,'approval_record_unchanged_and_valid':True,'source_changed_paths':changed,'source_audit_path':str(folder/'source_primary_audit.json'),'eligibility_end_path':str(folder/'eligibility_end.json')})
    old=json.loads((folder/'input_fingerprints.json').read_text(encoding='utf-8'))['files']
    for rel,digest in old.items():broad_before.setdefault(rel,digest)
for rel,digest in broad_before.items():
    p=ROOT/rel
    if not p.exists() or file_hash(p)!=digest:broad_differences.append({'path':rel,'historical_sha256':digest,'current_sha256':file_hash(p) if p.exists() else None,'classification':'broad_adapter_manifest_diagnostic_not_assigned_question_input','action':'preserved; no restoration performed'})
write(HERE/'source_preservation_audit.json',{'created_at':now(),'per_question_audits':preservation,'all_assigned_frozen_inputs_and_current_approvals_unchanged':True,'broad_adapter_manifest_diagnostic_changes':broad_differences,'whole_workspace_unchanged_claim':False,'own_filesystem_write_guard_scope':str(HERE),'formal_state_or_review_API_actions':[],'unrelated_concurrent_changes':'Preserved. No rollback or whole-workspace equality requirement.','protected_env_git_runtime':'No task writes; .env read only by existing harness credential loader.'})
write(HERE/'Plane474'/'four_bar_to_three_wide_edge_binding'/'primary_math_supplement.json',{'note':'Clarification of unit-grid search completeness; immutable design and evidence unchanged.','axis_alignment':'Any finite tiling of the connected rectilinear target by rectangles has a connected positive-edge contact graph. Along each contact, one side of each rectangle is parallel; their perpendicular companion sides therefore share the same two orientations. A rectangle on the outside boundary is axis aligned, which propagates through the graph.','integer_alignment':'For axis-aligned bars with integer side lengths, a generic horizontal line starts at an integer-coordinate target boundary and crosses integer-width rectangles, so all crossed vertical edges have integer x. Applying the same argument vertically gives integer y. Hence each placement belongs to the enumerated grid placements.','B_obstruction':'No horizontal or vertical run contains5 cells, so the1-by5 bar cannot be placed; all four other boards have saved exact-cover placements.'})
queue={'unit':'background_21','created_at':now(),'assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'credible_paired_hit_possibilities':[],'candidates':[],'count':0,'all_tested_candidates':candidates,'parent_action':'No candidate qualifies for delivery. If any future materially new candidate qualifies, parent must start a NEW independent reviewer before delivery; this unit did primary review only.','approval_status':'No approval, publication, Pass, Collect or formal review API action.'}
write(HERE/'second_review_queue.json',queue)
checkpoint={'unit':'background_21','status':'completed_finite_batch','stop_reason':'all_20_assigned_questions_assessed','created_at':now(),'assigned_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'assessed_count':20,'screened_without_design_count':17,'saved_design_count':3,'complete_candidate_pair_count':3,'actual_api_call_count':completed_calls,'original_control_call_count':0,'credible_paired_hit_possibility_count':0,'candidate_records':candidates,'prescreen_records':[{'question_id':q,'path':str(HERE/q/'primary_prescreen.json')} for q in ASSIGNED],'source_preservation_audit_path':str(HERE/'source_preservation_audit.json'),'evidence_binding_audit_path':str(HERE/'evidence_binding_audit.json'),'second_review_queue_path':str(HERE/'second_review_queue.json'),'controls':[],'errors':errors,'aborts':[],'retries':0,'formal_changes':[],'Pass_Collect_or_review_API_actions':[],'independent_second_review_performed':False,'limitations':['No original control calls; model errors cannot be causally attributed to the annotation from these pairs alone.','No human study, statistical success estimate, or per-marker causal ablation.','All three exact candidate pairs failed their predeclared wrong answer; do not retest unchanged inputs or reinterpret one-hit outcomes as successes.','Plane474 original PNG has no printed option letters; left-to-right order is used, unchanged.','Small Plane461 figures and Plane475 unmarked auxiliary-line crossing were reviewed at native size and remain presentation limitations.'],'next_recommendation':'Return finite checkpoint to parent; do not reallocate unassigned fresh scope or deliver these failed candidates.','no_live_process_confirmation_path':str(HERE/'no_live_processes.json'),'all_own_api_processes_completed':all((HERE/q/v/'process_completed.json').exists() for q,v in vids.items())}
assert checkpoint['all_own_api_processes_completed']
write(HERE/'checkpoint.json',checkpoint)
print(json.dumps({'assessed':20,'designs':3,'complete_pairs':3,'actual_calls':completed_calls,'credible_pairs':0,'broad_manifest_diagnostic_changes':len(broad_differences),'source_audits_pass':True},ensure_ascii=False))
