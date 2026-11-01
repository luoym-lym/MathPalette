from tools_local import *
import base64
records=[];audit_candidates=[];queue=[];frozen_files={};source_changes=[];state_drift=[];current_eligibility={}
for q in ASSIGNED:
    current=eligibility(q);assert current['eligible'],current
    current_eligibility[q]=current
    write(HERE/q/'eligibility_end.json',current)
    initial=json.loads((HERE/q/'eligibility_start.json').read_text())
    for p,old in initial['authoritative_state_hashes'].items():
        new=current['authoritative_state_hashes'].get(p)
        if old!=new:state_drift.append({'question_id':q,'path':p,'historical_sha256':old,'current_sha256':new,'classification':'Concurrent authoritative index or state change; current assigned-question eligibility separately rechecked; historical snapshot preserved.'})
    fp=json.loads((HERE/q/'input_fingerprints.json').read_text())
    for p,h in fp['files'].items():
        if p in frozen_files:assert frozen_files[p]==h
        frozen_files[p]=h
    for design_path in sorted((HERE/q).glob('*/design.json')):
        out=design_path.parent;d=json.loads(design_path.read_text());r=json.loads((out/'render_check.json').read_text());pr=json.loads((out/'primary_review.json').read_text())
        assert file_hash(out/'candidate.png')==r['png_sha256'] and pixel_hash(out/'candidate.png')==r['pixel_sha256']
        assert file_hash(out/'plugin.json')==r['plugin_sha256'] and file_hash(design_path)==r['design_sha256']
        assert r['two_byte_identical_redraws'] and r['schema_default_normalized'] and r['baseline_pixel_match']
        raw_dirs=list((out/'tests').glob('quicktest3_*')) if (out/'tests').exists() else []
        rec={'question_id':q,'variant_id':d['variant_id'],'expected_wrong_answer':d['expected_wrong_answer'],'correct_answer':d['correct_answer'],'design_path':str(design_path),'design_sha256':file_hash(design_path),'plugin_path':str(out/'plugin.json'),'plugin_sha256':file_hash(out/'plugin.json'),'image_path':str(out/'candidate.png'),'image_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixel_hash(out/'candidate.png'),'context_path':str(out/'context.json'),'path_fingerprints_path':str(out/'path_fingerprints.json'),'render_check_path':str(out/'render_check.json'),'primary_review_path':str(out/'primary_review.json'),'mathematical_proof_path':str(HERE/q/'mathematical_audit.json'),'marker_roles':d['marker_roles'],'manual_finals':[],'raw_bindings':[],'status':pr.get('status','UNTESTED'),'api_calls':0,'paired_target_hit':False,'approval_status':'PRIMARY ONLY; NO PASS/COLLECT/QUALIFICATION'}
        if raw_dirs:
            assert len(raw_dirs)==1
            e=raw_dirs[0];binding=json.loads((e/'binding.json').read_text());summary=json.loads((e/'summary.json').read_text());manual=json.loads((out/'manual_final_review.json').read_text())
            assert file_hash(design_path)==binding['design_sha256']==file_hash(e/'design_snapshot.json')
            assert file_hash(out/'candidate.png')==binding['image_sha256'] and r['pixel_sha256']==binding['pixel_sha256']
            assert d['expected_wrong_answer']==binding['expected_wrong_answer'] and summary['two_completed']
            assert binding['settings']['model']=='mimo-v2.6-flash' and binding['settings']['thinking']=={'type':'disabled'}
            request=json.loads((e/'request.json').read_text());assert set(request)=={'model','stream','thinking','messages'}
            assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
            assert request['messages'][0]=={'role':'system','content':binding['system_prompt']}
            user=request['messages'][1];assert user['role']=='user' and len(user['content'])==2
            assert user['content'][0]=={'type':'text','text':current['formal_record']['question']}
            encoded=user['content'][1]['image_url']['url'];assert encoded.startswith('data:image/png;base64,') and base64.b64decode(encoded.split(',',1)[1])==(out/'candidate.png').read_bytes()
            assert file_hash(e/'request.json')==binding['request_body_sha256']
            for i in [1,2]:
                run=json.loads((e/f'run_{i:02d}.json').read_text());started=json.loads((e/f'run_{i:02d}_started.json').read_text())
                assert run['status']=='completed' and run['http_status']==200 and not run['truncated'] and run['finish_reason']=='stop'
                assert run['image_sha256']==binding['image_sha256'] and run['design_sha256']==binding['design_sha256'] and run['request_body_sha256']==binding['request_body_sha256']
                assert started['request_body_sha256']==binding['request_body_sha256'] and file_hash(e/f'run_{i:02d}_response.json')==run['response_sha256']
            rec.update({'manual_finals':[v['choice'] for v in manual['actual_manual_finals']],'manual_final_review_path':str(out/'manual_final_review.json'),'paired_target_hit':manual['paired_target_hit'],'api_calls':2,'status':'PRIMARY_PAIRED_HIT_REQUIRES_NEW_INDEPENDENT_REVIEW' if manual['paired_target_hit'] else 'COMPLETE_PAIR_MISS','raw_bindings':[{'evidence_dir':str(e),'binding_path':str(e/'binding.json'),'binding_sha256':file_hash(e/'binding.json'),'files':{p.name:file_hash(p) for p in e.iterdir() if p.is_file()}}]})
            audit_candidates.append({'question_id':q,'variant_id':d['variant_id'],'frozen_design_unchanged':True,'same_png_in_both_actual_calls':True,'request_only_formal_question_and_frozen_image':True,'exact_quicktest3_profile':True,'no_retries_or_profile_overrides':True,'full_manual_final_review':True,'raw_hashes_verified':True})
            if rec['paired_target_hit']:queue.append({**rec,'requires_parent_new_independent_review':True,'qualification_status':'NOT QUALIFIED OR PUBLISHED','review_focus':['Unique original mathematics from fullfrozen geometry','Actual PNG readability and everymarkerrole','Human interpretation ofmarkings, especially cut/partitionsemantics','Fullrawbindingandexplicitmanualfinals','Freshbyte-identicalfrozenpluginreplay'],'original_controls':[],'limits':'Exactlytwoobservations; nooriginalcontrol, statistical orcausalclaim. Modelnarrativesmaycontainerrors.'})
        records.append(rec)
for p,h in frozen_files.items():
    actual=file_hash(ROOT/p) if (ROOT/p).exists() else None
    if actual!=h:source_changes.append({'path':p,'before':h,'after':actual})
assert not source_changes,source_changes
no_live=json.loads((HERE/'no_live_processes.json').read_text(encoding='utf-8-sig'));assert not no_live['live_owned_python_processes']
aud={'created_at':now(),'assessed_question_ids':ASSIGNED,'original_source_files':{'checked_file_count':len(frozen_files),'files':frozen_files,'changed':source_changes,'all_frozen_inputs_unchanged':True},'all_current_approvals_valid':all(c['approval_valid'] for c in current_eligibility.values()),'all_current_eligibility_valid':all(c['eligible'] for c in current_eligibility.values()),'authoritative_global_state_metadata_drift':state_drift,'state_drift_handling':'Globalaccepted/collected index hashes maychange fromconcurrentuserworkbenchactions outside assignedquestions. No historical snapshotrewritten or userchange restored. CurrentquestionIDscheckedagainstnewauthoritativefiles.','candidate_evidence_checks':audit_candidates,'actual_source_and_formal_pngs_viewed':ASSIGNED,'actual_candidate_pngs_viewed':[r['image_path'] for r in records],'own_write_scope':str(HERE),'write_guard':'runtime_isolation.install calledaftercache/TEMP selectionandbeforeprojectrenderimports; write_new JSON helperrestrictsoutputs toownfolder. Harness unchanged, envresetafterimport.','no_live_processes_path':str(HERE/'no_live_processes.json'),'formal_or_workbench_writes':False,'prior_evidence_edits':False}
write(HERE/'source_and_evidence_audit.json',aud)
write(HERE/'second_review_queue.json',{'created_at':now(),'assessed_question_ids':ASSIGNED,'candidates':queue,'requires_parent_new_independent_review':True,'primary_only':True,'no_self_approval_or_publication':True})
checkpoint={'unit':'background_07/plane_worker','completed_at':now(),'status':'COMPLETE_SUBSET_EXHAUSTED' if not queue else 'STOP_ONE_CREDIBLE_NEW_PAIRED_HIT','assigned_question_ids':ASSIGNED,'assessed_question_ids':ASSIGNED,'counts':{'questions_assessed':len(ASSIGNED),'saved_design_records':len(records),'complete_paired_evidence_candidates':sum(r['api_calls']==2 for r in records),'actual_quicktest3_calls':sum(r['api_calls'] for r in records),'credible_new_paired_hit_possibilities':len(queue),'untested_designs':sum(r['api_calls']==0 for r in records),'prescreen_only_questions':2,'errors':0,'aborted_calls':0,'original_control_calls':0},'candidate_records':records,'prescreen_questions':[{'question_id':q,'record_path':str(HERE/q/'prescreen_assessment.json'),'proof_path':str(HERE/q/'mathematical_audit.json')} for q in ['Plane262','Plane265']],'original_controls':[],'failures_and_aborts':{'complete_pair_misses':[{'question_id':r['question_id'],'variant_id':r['variant_id'],'preset':r['expected_wrong_answer'],'finals':r['manual_finals']} for r in records if r['api_calls'] and not r['paired_target_hit']],'untested_visual_rejections':[r for r in records if r['api_calls']==0],'api_errors':[],'aborted_calls':[],'local_diagnostics':['Plane247gridprefix corrected fromfigureN_ topieceN_beforeproofsave, noAPI involved.','Plane262proofcapsulehalfunitorigin correctedbeforeproofsave; exactnormalizationclarification retained.']},'source_and_evidence_audit_path':str(HERE/'source_and_evidence_audit.json'),'second_review_queue_path':str(HERE/'second_review_queue.json'),'no_live_processes_path':str(HERE/'no_live_processes.json'),'no_live_own_processes':True,'new_native_subagents_spawned':0,'no_pass_collect_review_api_or_publication':True,'next_recommendations':['Parent mustlaunchNEWindependentreview for anyqueuedcandidate beforedelivery.','Do notretestanyfailedidenticalimage orchangeitsfrozenpreset.','Plane247trueopenchainmatchescausevariable1-onlyvs1+4inferences; donotclaimrobustnessornewfixedpartition.','Plane239prefix producedB/D; fullcontactpath constraintremains uniqueA.','Plane245diagonal/ghostroletrap returnedcorrectB/B; preservefailure.','UntestedPlane242diameterdraft hasredundantoccludedgreenmark andmustnotbe delivered.','Plane262andPlane265requireanewconcreteinformationmechanism; currentproofsarecompletebutnopartial-outlinequota wasforced.']}
write(HERE/'checkpoint.json',checkpoint)
print(json.dumps({'counts':checkpoint['counts'],'queue_count':len(queue),'frozen_inputs_checked':len(frozen_files),'source_changes':source_changes,'state_metadata_drift_count':len(state_drift),'no_live_own_processes':True},ensure_ascii=False))
