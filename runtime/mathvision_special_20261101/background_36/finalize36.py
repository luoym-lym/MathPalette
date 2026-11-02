from tools_local import *
import base64
variants={'Solid99':('r36_straight_branch_side_seam',['10','3']),'Solid112':('r36_four_tile_cross_course_binding',['8','3']),'Solid117':('r36_lowered_column_unit_corner_binding',['11','3']),'Solid139':('r36_endpoint_elbow_front_L_transfer',['26','12'])}
notes={
'Solid99':['Final explicitly10; numerically correct, despite faulty tower/ground analysis. Not preset11.','Final explicitly3 after lengthy mutually inconsistent reconstruction. Not preset11.'],
'Solid112':['Final explicitly8 after claiming10remaining. Not preset3.','Final explicitly3; matches preset, but reasoning assumes source3x2x2rather than3x3x2. This single numerical hit does not confirm the intended cross-course mechanism.'],
'Solid117':['Final explicitly11 from27-16, misreading column heights. Not preset5.','Final explicitly3 from27-24, misreading column heights. Not preset5.'],
'Solid139':['Final26from a corner count8+3*6. Not preset48; no incidental mention counted.','Final12from invented digit grids/counts. Not preset48.']}
attempts=[];all_source={};old_integrity=[];eligibility_rows=[]
for q in ASSIGNED:
    p=TASK/q
    e=eligibility(q);assert e['eligible'],e
    write(p/'eligibility_at_end.json',e);eligibility_rows.append(e)
    start=json.loads((p/'frozen_inputs.json').read_text(encoding='utf-8'))
    now=AD.frozen_inputs(q)
    assert start==now,(q,'formal inputs or environment changed')
    all_source.update(start['files'])
    history=json.loads((p/'history_audit.json').read_text(encoding='utf-8'))
    for rel,expected in history['all_prior_files_sha256'].items():
        actual=file_hash(ROOT/rel);assert actual==expected,(q,rel)
        old_integrity.append({'path':rel,'sha256':actual,'unchanged':True})
    if q not in variants:continue
    v,finals=variants[q];folder=p/v
    summaries=list((folder/'tests').glob('*/summary.json'));assert len(summaries)==1
    summary_path=summaries[0];s=json.loads(summary_path.read_text(encoding='utf-8'))
    assert s['two_completed'] and len(s['results'])==2
    assert s['image_sha256']==file_hash(folder/'candidate.png')
    assert s['design_sha256']==file_hash(folder/'design.json')
    assert (summary_path.parent/'design_snapshot.json').read_bytes()==(folder/'design.json').read_bytes()
    d=json.loads((folder/'design.json').read_text(encoding='utf-8'))
    assert str(s['expected_wrong_answer'])==str(d['expected_wrong_answer'])
    request=summary_path.parent/'request.json';assert file_hash(request)==s['request_body_sha256']
    body=json.loads(request.read_text(encoding='utf-8'))
    assert body['model']=='mimo-v2.6-flash' and body['thinking']=={'type':'disabled'}
    assert set(body)=={'model','stream','thinking','messages'}
    assert body['messages'][1]['content'][0]=={'type':'text','text':AD.records[q]['question']}
    assert len(body['messages'][1]['content'])==2
    assert base64.b64decode(body['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==(folder/'candidate.png').read_bytes()
    manual=[]
    for i,answer in enumerate(finals,1):
        raw_path=summary_path.parent/f'run_{i:02d}_response.json';raw=json.loads(raw_path.read_text(encoding='utf-8'))
        choice=raw['choices'][0];assert choice['finish_reason']=='stop'
        assert s['results'][i-1]['status']=='completed'
        assert file_hash(raw_path)==s['results'][i-1]['response_sha256']
        text=choice['message']['content']
        manual.append({'run_index':i,'response_path':str(raw_path),'response_sha256':file_hash(raw_path),'complete_raw_assistant_answer_read_manually':text,'final_answer_manual':answer,'finish_reason':'stop','status':'completed','matches_unchanged_preset':answer==str(d['expected_wrong_answer']),'manual_judgment':notes[q][i-1]})
    pair=all(r['matches_unchanged_preset'] for r in manual)
    assert not pair
    review={'question_id':q,'variant_id':v,'review_kind':'primary_manual_final_read_NOT_independent','complete_answers_read':True,'expected_wrong_answer_frozen':d['expected_wrong_answer'],'formal_correct_answer':AD.records[q]['answer'],'runs':manual,'target_hits':sum(r['matches_unchanged_preset'] for r in manual),'two_target_hits':pair,'primary_candidate':False,'history_relabelled':False,'retries':0,'candidate_sha256':s['image_sha256'],'design_sha256':s['design_sha256'],'request_sha256':s['request_body_sha256'],'raw_binding':str(summary_path.parent/'binding.json'),'summary':str(summary_path),'math_visual_marker_review':str(folder/'primary_review.json'),'difference_audit':str(folder/'design_difference_audit.json'),'no_controls_or_incremental_effect_claim':True}
    write(folder/'manual_final_review.json',review)
    attempts.append({'question_id':q,'variant_id':v,'candidate_directory':str(folder),'expected_wrong_answer':d['expected_wrong_answer'],'manual_finals':finals,'target_hits':review['target_hits'],'complete_calls':2,'candidate':False,'evidence_summary':str(summary_path),'manual_final_review':str(folder/'manual_final_review.json'),'design':str(folder/'design.json'),'plugin':str(folder/'plugin.json'),'candidate_png':str(folder/'candidate.png'),'design_difference_audit':str(folder/'design_difference_audit.json'),'render_check':str(folder/'render_check.json'),'marker_path_bindings':str(folder/'marker_path_bindings.json'),'primary_review':str(folder/'primary_review.json'),'frozen_bindings':{'image_sha256':s['image_sha256'],'design_sha256':s['design_sha256'],'request_body_sha256':s['request_body_sha256'],'raw_responses':[r['response_sha256'] for r in manual]}})
    print(q,d['expected_wrong_answer'],'manual finals',finals,'hits',review['target_hits'])
closure=json.loads((TASK/'process_closure_audit.json').read_text(encoding='utf-8-sig'));assert closure['live_own_api_processes']==[]
for entry in closure['own_recorded_api_processes']:
    assert any(json.loads((TASK/q/v/'api_process_finished.json').read_text(encoding='utf-8'))['pid']==entry['pid'] for q,(v,_) in variants.items())
write(TASK/'source_preservation_final.json',{'checked_at':datetime.now(timezone.utc).isoformat(),'current_eligibility_all_eight':True,'each_start_frozen_input_manifest_equals_current':True,'formal_source_file_count':len(all_source),'formal_source_files_sha256':all_source,'old_scoped_evidence_file_count':len(old_integrity),'old_scoped_evidence':old_integrity,'global_runtime_aggregates':'Diagnostic mutable metadata only; historical hashes and other agents files not edited. No claim of global tree immutability.','own_writes_scope':str(TASK),'own_write_guard_installed_before_project_import':True,'guard_source':str(TASK/'tools_local.py'),'formal_special_or_approval_actions':0})
queue={'unit':'background_36','stage':'material_refinement','created_at':datetime.now(timezone.utc).isoformat(),'candidates':[],'candidate_count':0,'reason':'No new frozen PNG obtained exactly two completed target final answers. Solid112 has one hit only. No variant promoted or history relabelled.','required_for_any_future_candidate':'Parent creates a NEW independent second review; no self second-review, Pass, Collect, formal approval or publication.'}
write(TASK/'second_review_queue.json',queue)
checkpoint={'unit':'background_36','stage':'material_refinement','status':'completed_finite_batch','stop_reason':'All eight assigned refinement questions reasonably assessed. Four distinct targeted designs tested; four hypotheses rejected before design/calls with exact geometric reasons.','created_at':datetime.now(timezone.utc).isoformat(),'actual_assessed_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'unworked_question_ids':[],'assessed_count':8,'new_design_count':4,'completed_candidate_pair_count':4,'completed_real_calls':8,'controls_calls':0,'credible_primary_candidate_count':0,'errors':[],'aborts':[],'retries':0,'own_live_api_processes':[],'primary_attempts':attempts,'screened_question_ids':[q for q in ASSIGNED if q not in variants],'question_assessments':{q:str(TASK/q/'assessment.json') for q in ASSIGNED},'per_question_math':{q:str(TASK/q/'primary_math_audit.json') for q in ASSIGNED},'history_audits':{q:str(TASK/q/'history_audit.json') for q in ASSIGNED},'no_old_calls_repeated':'All eight prior scopes contained zero saved designs and zero old response files; full prior screening/checkpoint evidence read and preserved.','controls_reused':[],'controls_note':'Assigned old histories contain no original-control calls. No new control calls or claims of incremental effect.','source_preservation':str(TASK/'source_preservation_final.json'),'process_closure':str(TASK/'process_closure_audit.json'),'second_review_queue':str(TASK/'second_review_queue.json'),'delivered_readonly_reference_audit':str(TASK/'delivered_references_read.json'),'isolation':'TEMP/TMP/MPLCONFIGDIR/XDG_CACHE_HOME under own root; own strict audit guard installed before importing project. Byte-identical local harness, truePROJECT/RUNTIME binding restored. Exact inherited model/thinking/system/credential/profile/timeout/no max tokens.','no_formal_or_shared_writes':True,'approval_pass_collect_publish_actions':0,'independent_review_performed_by_self':False,'limits':['These finite negative results do not prove every legal design impossible.','Wrong finals that miss the frozen preset remain misses.','The one matching Solid112 final uses a different apparent mechanism; no mechanism/causal-effect evidence is claimed.']}
write(TASK/'checkpoint.json',checkpoint)
print('COMPLETED',len(all_source),'formal source hashes;',len(old_integrity),'old evidence hashes;8assessed4newdesigns8completedcalls0candidates0errors0aborts')
