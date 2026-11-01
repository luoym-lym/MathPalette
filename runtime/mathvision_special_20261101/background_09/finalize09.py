from tools09 import *
import base64
MANUAL={
 ('Plane252','incompatible_local_overlap_sum'):['2','6'],
 ('Plane252','single_U_contiguous_overlap'):['3','6'],
 ('Plane391','right_angle_size_alias'):['16','7'],
 ('Plane391','whole_square_frame_to_triangle'):['8','8'],
 ('Plane348','fold_to_middle_cut_alias'):['16','4'],
 ('Plane415','arc_inventory_perimeter_alias'):['15','20'],
 ('Plane213','open_notch_local_global_binding'):['C','B'],
 ('Plane276','exposed_cut_edge_migration'):['D','D'],
 ('Plane301','terminal_feature_transfer'):['C','B'],
 ('Plane398','wrong_corner_L_transfer'):['D','A'],
}
NOTES={
 ('Plane252','single_U_contiguous_overlap'):'Run1 complete conclusion identifies the maximum as the3-segment U, without a separate numeric Answer line. Classified3 by full manual reading; it is unequivocally not the preset4. Run2 explicitly ends6.',
 ('Plane213','open_notch_local_global_binding'):'Run1 finalC describes a four-cell bar, inconsistent with the actual5-cell L optionC; flagged as unreliable, never a targetB hit. Run2 explicitly endsB and calls the red source path internal U boundaries. This supports the local-to-global hypothesis but also confirms a residual human-semantics risk; there is no paired hit and no queue entry.',
 ('Plane391','whole_square_frame_to_triangle'):'Both complete finals explicitly give8cm2. Their component counts and source decompositions differ and are mathematically false. They are not required to share a causal narrative; no causal or statistical attribution is made. Independent source/assembly shoelace proof confirms6. Five open-frame actions have explicit source-to-assembly roles; source diagonal and triangle sizes remain visible.',
 ('Plane301','terminal_feature_transfer'):'Run1 discusses bothB andC then explicitly selectsC; run2 explicitly selectsB. PresetC is not hit twice.',
 ('Plane415','arc_inventory_perimeter_alias'):'Run1 ends15cm. Run2 ends20cm, but its straight-boundary counts are inaccurate despite matching the formal final. No causal interpretation or correctness of its reasoning is claimed.',
}
def rel(p):return str(Path(p).resolve().relative_to(ROOT)).replace('\\','/')
def checks_for(out,manual):
    ds=read(out/'design.json');rc=read(out/'render_check.json') if (out/'render_check.json').exists() else None
    dirs=list((out/'tests').glob('quicktest3_*'));assert len(dirs)==1
    ev=dirs[0];binding=read(ev/'binding.json');summary=read(ev/'summary.json')
    assert binding['requested_runs']==2 and summary['two_completed']
    designbytes=(out/'design.json').read_bytes();assert (ev/'design_snapshot.json').read_bytes()==designbytes
    assert ds['created_at']<=binding['created_at']
    assert binding['design_sha256']==file_hash(out/'design.json')
    img=Path(binding['image_path']);assert binding['image_sha256']==file_hash(img)
    assert binding['pixel_sha256']==pixel_hash(img)
    requestbytes=(ev/'request.json').read_bytes();assert hashlib.sha256(requestbytes).hexdigest()==binding['request_body_sha256']
    request=json.loads(requestbytes);assert set(request)=={'model','stream','thinking','messages'}
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
    assert request['messages']==[{'role':'system','content':binding['system_prompt']},{'role':'user','content':[{'type':'text','text':binding['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(img.read_bytes()).decode('ascii')}}]}]
    r=next(x for x in rows(ROOT/'PlaneGeometry/dataset.jsonl') if x['id']==ds['question_id'])
    assert binding['question']==r['question'] and binding['question_record_sha256']==canonical_hash(r)
    finals=[];runs=[]
    for i,answer in enumerate(manual,1):
        p=ev/f'run_{i:02d}.json';job=read(p);raw=ev/f'run_{i:02d}_response.json';started=read(ev/f'run_{i:02d}_started.json')
        assert job['status']=='completed' and job['finish_reason']=='stop' and not job['truncated']
        assert job['response_sha256']==file_hash(raw)
        assert job['image_sha256']==binding['image_sha256'] and job['design_sha256']==binding['design_sha256'] and job['request_body_sha256']==binding['request_body_sha256']
        assert binding['created_at']<=started['started_at']
        runs.append({'run_index':i,'manual_final_answer':answer,'complete_final_answer':job['answer'],'manually_read_in_full':True,'preset_hit':answer==str(ds['expected_wrong_answer']),'run_path':rel(p),'run_sha256':file_hash(p),'response_path':rel(raw),'response_sha256':file_hash(raw),'finish_reason':job['finish_reason'],'truncated':job['truncated']})
    checked={'question_id':ds['question_id'],'variant_id':ds['variant_id'],'created_at':now(),'expected_wrong_answer':ds['expected_wrong_answer'],'manual_final_answers':manual,'complete_manual_finals':runs,'two_preset_hits':all(x['preset_hit'] for x in runs),'same_frozen_PNG_and_preset_both_calls':True,'exactly_two_real_calls':True,'no_retry':True,'solver_request_only_formal_question_and_candidate_PNG':True,'settings_exact_quicktest3':True,'no_profile_max_tokens_timeout_overrides':True,'evidence_dir':rel(ev),'binding_path':rel(ev/'binding.json'),'binding_sha256':file_hash(ev/'binding.json'),'request_path':rel(ev/'request.json'),'request_sha256':file_hash(ev/'request.json'),'design_path':rel(out/'design.json'),'design_sha256':file_hash(out/'design.json'),'image_path':rel(img),'image_sha256':file_hash(img),'pixel_sha256':pixel_hash(img),'notes':NOTES.get((ds['question_id'],ds['variant_id']),'Full final answers read manually; no incidental mention treated as a hit.')}
    if rc:
        assert rc['png_sha256']==file_hash(img) and rc['pixel_sha256']==pixel_hash(img)
        assert rc['design_sha256']==file_hash(out/'design.json') and rc['plugin_sha256']==file_hash(out/'plugin.json')
        checked.update(plugin_path=rel(out/'plugin.json'),plugin_sha256=file_hash(out/'plugin.json'),render_check_path=rel(out/'render_check.json'),primary_review_path=rel(out/'primary_review.json'),primary_math_path=rel(HERE/ds['question_id']/'primary_math_audit.json'),path_fingerprints_path=rel(out/'path_fingerprints.json'))
    write(out/'manual_finals_and_binding_audit.json',checked)
    return checked
if __name__=='__main__':
    candidates=[];audits=[]
    for (q,v),manual in MANUAL.items():
        a=checks_for(HERE/q/v,manual);audits.append(a)
        if a['two_preset_hits']:candidates.append(a)
    control=checks_for(HERE/'Plane391/whole_square_frame_to_triangle/original_control',sys.argv[1:3])
    assert len(list(HERE.glob('Plane*/**/run_0?_started.json')))==22
    assert len(list(HERE.glob('Plane*/**/run_0?.json')))==22
    # Source audits use frozen formal/renderer files. Runtime progress snapshots are diagnostic only.
    changed=[];files={};elig=[]
    for q in ASSIGNED:
        start=read(HERE/q/'input_fingerprints.json');end=eligibility(q);elig.append(end)
        for name,dig in start['files'].items():
            actual=file_hash(ROOT/name);files[name]={'frozen_sha256':dig,'current_sha256':actual,'unchanged':actual==dig}
            if actual!=dig:changed.append({'question_id':q,'path':name,'before':dig,'after':actual})
        record=read(HERE/q/'formal_record.json');original=ROOT/'PlaneGeometry'/record['image']
        assert (HERE/q/'original.png').read_bytes()==original.read_bytes()
        assert read(HERE/q/'context.json')['original_pixel_sha256']==pixel_hash(original)
    assert not changed
    write(HERE/'source_and_evidence_audit.json',{'created_at':now(),'formal_and_renderer_files_checked':len(files),'changed_frozen_inputs':changed,'files':files,'current_eligibility':elig,'all20_currently_eligible':all(e['eligible'] for e in elig),'baseline_pixel_matches':20,'diagnostic_runtime_hash_differences_do_not_rewrite_historical_snapshots':True,'shared_harness_byte_identical_to_copy':file_hash(BASE/'harness/quicktest3_isolated.py')==file_hash(HERE/'harness/quicktest3_isolated.py'),'own_directory_python_write_guard_enabled':True,'formal_library_workbench_approval_publication_mutations':False,'candidate_evidence_audits':audits,'original_controls':[control]})
    process=read(HERE/'process_audit.json');assert not process['live_own_python_processes']
    prescreens=read(HERE/'prescreens.json');assessed=[q for q in ASSIGNED if q in {x['question_id'] for x in prescreens}|{x[0] for x in MANUAL}]
    assert assessed==ASSIGNED
    queue=[]
    for a in candidates:
        q=a['question_id'];v=a['variant_id'];out=HERE/q/v;d=read(out/'design.json')
        queue.append({'candidate_id':q+'/'+v,'branch':'PlaneGeometry','question_id':q,'variant_id':v,'expected_wrong_answer':d['expected_wrong_answer'],'formal_correct_answer':read(HERE/q/'formal_record.json')['answer'],'manual_final_answers':a['manual_final_answers'],'status':'POSSIBLE_PRIMARY_ONLY_NEW_PARENT_INDEPENDENT_SECOND_REVIEW_REQUIRED','binding_audit':a,'source_context_path':rel(out/'context.json'),'path_fingerprints_path':rel(out/'path_fingerprints.json'),'marker_roles':d['marker_roles'],'primary_math_proof':d['primary_math_proof'],'primary_math_audit_path':rel(HERE/q/'primary_math_audit.json'),'primary_review_path':rel(out/'primary_review.json'),'primary_post_test_review_path':rel(out/'primary_post_test_review.json'),'original_controls':control,'limitations':['Exactly2 candidate calls, no statistical or per-marker causal estimate.','Model narratives differ and miscount original pieces; both numeric finals explicitly8.','Original controls run separately after candidate and end12/6.5, both incorrect for formal6. Correct controls are not an eligibility gate, but these failures prevent any claim that the marks caused an otherwise-correct solver to fail.','Five open source/assembly frames preserve the original diagonal and all piece boundaries; parent must independently assess the whole-square/triangle area transfer and human clarity.'],'no_self_approval':True})
    write(HERE/'second_review_queue.json',{'unit':'background_09','created_at':now(),'actual_assessed_question_ids':assessed,'candidate_count':len(queue),'candidates':queue,'parent_action':'Launch a NEW independent second-review task before any delivery. This worker performed primary review only.','not_queued':[{'candidate_id':x['question_id']+'/'+x['variant_id'],'reason':'predeclared_wrong_answer_not_hit_twice','manual_final_answers':x['manual_final_answers'],'expected_wrong_answer':x['expected_wrong_answer']} for x in audits if not x['two_preset_hits']]})
    cp={'unit':'background_09','status':'finite_batch_complete','stop_reason':'all20_assigned_questions_assessed','created_at':now(),'assigned_question_ids':ASSIGNED,'actual_assessed_question_ids':assessed,'unworked_reservations':[],'assessed_question_count':len(assessed),'tested_question_ids':list(dict.fromkeys(q for q,v in MANUAL)),'tested_question_count':len({q for q,v in MANUAL}),'saved_design_count':len(MANUAL),'complete_candidate_pairs':len(audits),'candidate_API_call_count':2*len(audits),'original_control_API_call_count':2,'all_API_call_count':2*len(audits)+2,'credible_paired_hit_count':len(queue),'candidate_ids':[x['candidate_id'] for x in queue],'screened_out_question_count':len(prescreens),'prescreens_path':rel(HERE/'prescreens.json'),'design_presets_manual_finals_exact_evidence':audits,'original_controls':[control],'failures':[x for x in audits if not x['two_preset_hits']],'aborts':[],'transport_errors':[],'untested_saved_candidates':[],'source_and_evidence_audit_path':rel(HERE/'source_and_evidence_audit.json'),'second_review_queue_path':rel(HERE/'second_review_queue.json'),'process_audit_path':rel(HERE/'process_audit.json'),'no_live_own_API_processes':True,'new_independent_review_or_publication_performed':False,'formal_Pass_Collect_actions':False,'all_task_outputs_only_own_directory':True,'next_recommendations':['Parent should independently review Plane391/whole_square_frame_to_triangle using exact frozen candidate and raw two-call evidence.','Do not repeat any failed/aborted identical design or alter its preset. All20 assignments are now terminal/assessed; no unworked reservations remain.','Preserve this checkpoint and every failed design/control; no mutable global progress file was written by this worker.']}
    write(HERE/'checkpoint.json',cp)
    print(json.dumps({k:cp[k] for k in ['status','assessed_question_count','saved_design_count','candidate_API_call_count','original_control_API_call_count','credible_paired_hit_count','candidate_ids','no_live_own_API_processes']},ensure_ascii=False))
