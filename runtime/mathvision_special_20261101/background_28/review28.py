from tools28 import *
import base64
MANUAL={
'r28_depth_vertices_as_cells':(['21','4'],['Explicit final21; assumes4by4by4 and equal hidden counts. Neither reasoning nor final matches preset8.','Explicit final4 from12-8; wrong visible count. Earlier8 is a visible-count intermediate, not the final hidden-white answer.']),
'r28_interior_section_full_depth':(['18','12'],['Explicit final18 from misread5by5by4dimensions; misses preset24.','Explicit final12, the formal correct result; misses preset24.']),
'r28_L_leg_to_bar_span':(['1','5'],['Explicit final1 after inventing block multiplicities and a new rectangle; intermediate6notfinal. Misses preset15.','Explicit final5 after confused material/visibility counting; misses preset15.']),
'r28_big_face_to_unit_tile':(['1.8','1'],['Explicit final1.8kg from erroneous9/54=0.15; correctly counts12white unit faces but arithmetic fails. Not18kg.','Explicit final1kg from incorrectly assuming a1cube corner and6white faces; misses preset18.']),
'r28_highest_layer_only':(['6','7'],['Explicit final6 from wrong height rows summing21; not preset5.','Explicit final7, formal correct value. Some individual heights permuted but total20; not preset5.']),
'r28_interface_side_value_transfer':(['15','22'],['Explicit final15 from misread pip counts and same-value opposite faces; not preset25.','Explicit final22 from misread pips and assumed die handedness; not preset25.']),
'r28_small_width_to_rear_depth':(['E','A'],['Explicit finalE=56cm2; discusses16but rejects it for whole-top interpretation. Misses predeclaredD=24.','Explicit finalA=16cm2, formal correct. Narrative face naming is loose, but final letter/value consistent; missesD24.']),
'r28_near_skin_only':(['27','27'],['Explicit final27 from misreading all original dimensions as5. Both-end skin subtraction itself is correct for that imagined cube. It is wrong but misses preset36.','Explicit final27 again from misreading5by5by5; NOT a36hit. Equal wrong finals may not be relabeled after testing.']),
'r28_L_bounding_square':(['21','17'],['Final sentence explicitly21. Earlier15andquestioned15calculation are intermediate alternatives; misses preset3.','Explicit final17 from wrongly4unitLsand2unitbar. Discussed11alternative is not final; misses preset3.'])}

def review(folder):
    d=read(folder/'design.json');vid=d['variant_id'];qid=d['question_id']
    if (folder/'manual_final_review.json').exists():return
    finals,notes=MANUAL[vid]
    summaries=list((folder/'tests').glob('*/summary.json'));assert len(summaries)==1
    sp=summaries[0];s=read(sp);inv=sp.parent;binding=read(inv/'binding.json')
    requestbytes=(inv/'request.json').read_bytes();request=json.loads(requestbytes)
    record=next(r for r in rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id']==qid)
    assert s['two_completed'] and s['requested_runs']==2
    assert s['design_sha256']==file_hash(folder/'design.json')==file_hash(inv/'design_snapshot.json')
    assert s['image_sha256']==file_hash(folder/'candidate.png')==d['frozen_png_sha256']
    assert binding['request_body_sha256']==hashlib.sha256(requestbytes).hexdigest()
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert set(request)=={'model','stream','thinking','messages'}
    assert len(request['messages'])==2
    assert request['messages'][1]['content'][0]=={'type':'text','text':record['question']}
    assert request['messages'][0]['content']==s['system_prompt']
    assert base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(folder/'candidate.png').read_bytes()
    rr=[]
    for i in [1,2]:
        rawp=inv/f'run_{i:02d}_response.json';raw=read(rawp);job=read(inv/f'run_{i:02d}.json')
        assert job['status']=='completed' and raw['choices'][0]['finish_reason']=='stop'
        assert job['response_sha256']==file_hash(rawp)
        content=raw['choices'][0]['message']['content']
        rr.append({'run_index':i,'raw_response_path':str(rawp),'raw_response_sha256':file_hash(rawp),'job_path':str(inv/f'run_{i:02d}.json'),'finish_reason':'stop','complete_final_answer_text':content,'entire_complete_reply_read_manually':True,'manual_final_answer':finals[i-1],'interpretation':notes[i-1],'matches_predeclared_wrong_answer':finals[i-1]==str(d['expected_wrong_answer'])})
    hit=all(r['matches_predeclared_wrong_answer'] for r in rr)
    write(folder/'manual_final_review.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'preset':d['expected_wrong_answer'],'correct_answer':record['answer'],'manual_results':rr,'credible_paired_hit':hit,'preset_changed_after_calls':False,'raw_pair_count':2,'extra_samples_or_retries':0,'note':'Whole complete final manually interpreted. Incidental values are not target hits.'})
    write(folder/'evidence_binding_audit.json',{'question_id':qid,'variant_id':vid,'checked_at':now(),'summary':str(sp),'binding':str(inv/'binding.json'),'request_body':str(inv/'request.json'),'request_body_sha256':file_hash(inv/'request.json'),'design_sha256':file_hash(folder/'design.json'),'design_snapshot_sha256':file_hash(inv/'design_snapshot.json'),'image_sha256':file_hash(folder/'candidate.png'),'raw_responses':[{'path':r['raw_response_path'],'sha256':r['raw_response_sha256']} for r in rr],'question_record_sha256':canonical_hash(record),'two_complete_stop_finals':True,'exact_two_calls_same_frozen_request_image_design':True,'only_formal_question_and_frozen_PNG_in_user_message':True,'model_profile_exact':True,'no_answer_preset_intent_history_or_params_in_solver_input':True,'no_profile_token_timeout_overrides':True,'no_retry':True,'all_binding_checks_passed':True})
    write(folder/'primary_review.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'review_kind':'Primary author math/native visual/per-marker review ONLY','unique_formal_answer':record['answer'],'mathematics':read(TASK/qid/'primary_math_audit.json'),'each_marker':d['each_marker_proof'],'native_visual_review':read(folder/'pretest_native_visual_review.json'),'schema_and_render_report':str(folder/'schema_and_marker_audit.json'),'source_frozen':read(folder/'render_check.json')['frozen_inputs'],'image_sha256':file_hash(folder/'candidate.png'),'design_sha256':file_hash(folder/'design.json'),'full_finals':[r['manual_final_answer'] for r in rr],'predeclared_wrong_answer':d['expected_wrong_answer'],'credible_paired_hit':hit,'controls':'No same-question old original control found in prior history; none newly called.','limits':['No causal/statistical/human-performance claim from two calls.','No independent second review by this author; any future primary candidate needs a NEW parent review.'],'approval_status':'No Pass/Collect/publication/formal review actions.'})
    print(qid,vid,'preset',d['expected_wrong_answer'],'finals',finals,'hit',hit,flush=True)
if __name__=='__main__':
    for p in sorted(TASK.glob('Solid*/r28_*/design.json')):
        if p.parent.name in MANUAL:review(p.parent)
