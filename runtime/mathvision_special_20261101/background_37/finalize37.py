from tools37 import *
from review37 import verify
import numpy as np

# Prove why the provisional six-interface design forSolid177 cannot be cleanly drawn.
q='Solid177';s=read(TASK/q/'source_scene_snapshot.json');faces={}
for axis,plane,name in [(0,0,'left'),(0,1,'right'),(1,0,'front'),(1,1,'rear'),(2,0,'bottom'),(2,1,'top')]:
    found=[]
    for o in s['objects']:
        if o.get('type')!='segment':continue
        ps=[s['points'].get(p,p) if isinstance(p,str) else p for p in o['points']];a,b=np.array(ps,float);v=b-a
        if a[axis]!=plane or b[axis]!=plane:continue
        lo,hi=0.,1.
        for k in range(3):
            if k==axis:continue
            if abs(v[k])<1e-14:
                if not 0<=a[k]<=1:lo,hi=1.,0.;break
            else:
                ts=sorted([(0-a[k])/v[k],(1-a[k])/v[k]]);lo=max(lo,ts[0]);hi=min(hi,ts[1])
        if hi-lo>1e-12 and np.linalg.norm(v)*(hi-lo)>1e-12:found.append({'object':o['id'],'positive_interval':[lo,hi],'world_endpoints':[(a+lo*v).tolist(),(a+hi*v).tolist()]})
    faces[name]=found
assert all(not faces[n] for n in ['left','rear','bottom'])
write(TASK/q/'visibility_skip_audit.json',{'created_at':now(),'central_cube':[0,1,0,1,0,1],'actual_visible_edge_intervals_on_each_contact_face_perimeter':faces,'no_positive_length_visible_rim_for_three_interfaces':True,'skip_does_not_replace_hidden_interfaces_with_outer_arm_contours':True})

before=read(TASK/'readonly_history_hashes_before.json');changed=[p for p,h in before.items() if not (ROOT/p).is_file() or file_hash(ROOT/p)!=h]
assert not changed,changed
current=[];assessments=[];entries=[];rawcalls=[];trusted=[];held=[]
for q in IDS:
    e=eligibility(q);assert e['eligible'];current.append(e)
    old=read(TASK/q/'frozen_inputs.json');actual=frozen(q);assert old==actual,(q,'frozen source changed')
    if q=='Solid177':
        assessments.append({'question_id':q,'status':'screened_no_clean_six_contact_encoding','new_design_count':0,'completed_calls':0,'skip_record':str(TASK/q/'prescreen.json'),'visibility_proof':str(TASK/q/'visibility_skip_audit.json'),'eligibility_current':e});continue
    f=next((TASK/q).glob('*/design.json')).parent;d=read(f/'design.json');audit=verify(q,f);manual=read(f/'manual_final_review.json');diff=read(f/'design_difference_audit.json');free=read(f/'pretest_freeze.json');ev=Path(audit['summary_path']).parent
    earliest=min(read(p)['started_at'] for p in ev.glob('run_*_started.json'))
    assert d['created_at']<earliest and diff['created_at']<earliest and free['created_at']<earliest
    assert read(f/'process_completed.json')['two_completed']
    assert not (f/'process_failed.json').exists()
    hits=[r.get('matches_immutable_preset',r.get('matches_predeclared_wrong_answer',False)) for r in manual['manual_results']]
    paired=all(hits);finals=[r['manually_extracted_final'] for r in manual['manual_results']]
    status='credible_primary_two_hit' if q=='Solid126' else ('numeric_two_hit_held_information_targeting' if q=='Solid230' else 'paired_preset_miss')
    entry={'question_id':q,'variant_id':f.name,'candidate_dir':str(f),'correct_answer':AD.records[q]['answer'],'expected_wrong_answer':d['expected_wrong_answer'],'manual_finals':finals,'numeric_twohit':paired,'primary_twohit':q=='Solid126','primary_disposition':status,'raw_evidence_dir':str(ev),'difference_from_old':diff['substantive_difference'],'design_difference_audit':str(f/'design_difference_audit.json'),'evidence_binding_audit':str(f/'evidence_binding_audit.json'),'manual_final_review':str(f/'manual_final_review.json'),'primary_review':str(f/'primary_review.json'),'pretest_visual_review':str(f/'pretest_visual_review.json'),'candidate_png_sha256':file_hash(f/'candidate.png'),'design_sha256':file_hash(f/'design.json'),'plugin_sha256':file_hash(f/'plugin.json'),'primary_math_unique':True,'native_candidate_viewed':True,'schema_normalized_deterministic_baseline_equal':True,'eligibility_current':e,'raw_binding_audit':audit,'new_design_and_difference_frozen_before_both_calls':True,'review_status':'PRIMARY ONLY; no independent review or delivery'}
    if q=='Solid126':
        entry.update(primary_supplement=str(f/'primary_supplement.json'),reviewer_must_check=['Exact frozenPNG/design and both completeAfinals; oldC/A,AremainsMISS.','Actual9x6top/floor openL and3x6end/cutside correspondence: unchanged dimensions and ghostdashstyles.','UniqueBviaLcrosssection69/perimeter40/depth6=>378vs432; no newendcaps.','Each mark informative and true; redcancellationbiasmustnot obscure two9x3end losses.','Fresh authoritative original approval/MathVision/noPass/noCollect/noSpecialCompletion.','No originalcontrolorincrementaleffectclaim; NEWindependent task required before delivery.']);trusted.append(entry)
    elif q=='Solid230':
        entry.update(information_targeting_objection='BOTHcompleteanswers explicitlycountboth1faces. Theyreadunmarkedmiddle-right6as5; frozenidentitymerge hypothesis not observed. Numeric42/42 is valid but cannot be presentedas demonstrated targetedtransfer orincrementaleffect.',pip_pixel_preservation=str(f/'pip_pixel_preservation.json'),review_status='HOLD in primary review for unsupported information targeting; not a credible targeted candidate. Parent may elect NEW independent review, never deliver unchanged without independent recommendation.');held.append(entry)
    entries.append(entry)
    assessments.append({'question_id':q,'status':status,'new_design_count':1,'completed_calls':2,'expected_wrong_answer':d['expected_wrong_answer'],'manual_finals':finals,'matches_preset':hits,'new_vs_old_difference':diff['substantive_difference'],'evidence':entry})
    for i in [1,2]:
        rp=ev/f'run_{i:02d}.json';raw=ev/f'run_{i:02d}_response.json';job=read(rp)
        assert job['status']=='completed'
        rawcalls.append({'question_id':q,'run':i,'job_path':str(rp),'job_sha256':file_hash(rp),'response_path':str(raw),'response_sha256':file_hash(raw),'request_path':str(ev/'request.json'),'request_sha256':file_hash(ev/'request.json'),'binding_path':str(ev/'binding.json'),'binding_sha256':file_hash(ev/'binding.json'),'image_sha256':entry['candidate_png_sha256'],'design_sha256':entry['design_sha256'],'manual_final':finals[i-1],'matches_frozen_preset':hits[i-1]})

assert len(rawcalls)==14 and len(entries)==7 and len(assessments)==8
proc=read(TASK/'no_live_api_processes.json');assert proc['live_own_api_process_count']==0
write(TASK/'source_and_history_audit_final.json',{'created_at':now(),'readonly_history_file_count':len(before),'readonly_history_changes':changed,'all_current_formal_source_dependency_hashes_unchanged':True,'all_eight_current_original_approvals_match':True,'all_eight_current_eligibility_checks':current,'formal_records_frozen_per_question_not_whole_dataset_file':True,'mutable_progress_and_dispatch_are_diagnostic_metadata_only':True,'dedicated_bridge_and_shared_helpers_modified':False,'write_guard_scope':str(TASK),'nested_agents_threads_worktrees':False})
protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json','runtime/mathvision_special_20261101/background_37_brief.txt','runtime/mathvision_special_20261101/background_37_assignment.json','runtime/mathvision_special_20261101/continuation_brief.txt','runtime/mathvision_special_20261101/annotation_semantics_lessons_20261102.json']
write(TASK/'protocol_read_receipt.json',{'created_at':now(),'read_in_full':{p:file_hash(ROOT/p) for p in protocols},'implementation_authorized_by_current_user':True,'preparation_only_assignment_flag_is_descriptive_old_phase':True,'eight_ids_only':IDS})
write(TASK/'second_review_queue.json',{'unit':'background_37','stage':'material_refinement','created_at':now(),'candidate_count':len(trusted),'candidates':trusted,'held_numeric_two_hit_count':len(held),'held_numeric_two_hits':held,'all_numeric_two_hit_count':len(trusted)+len(held),'no_self_approval':True,'no_Pass_Collect_publication_formal_review_API':True,'requires_parent_NEW_independent_review_for_every_eventual_delivery':True,'held_case_cannot_be_silently_promoted':True})
write(TASK/'checkpoint.json',{'unit':'background_37','stage':'material_refinement','completed_at':now(),'status':'terminal','stop_reason':'All8assignedrefinementquestionsreasonablyassessed;7materialnewdesigns/7exactpairscompleted;Solid177cleanlyskippedforocclusion. Noquota/coststop.','assigned_question_ids':IDS,'actual_assessed_question_ids':IDS,'assessed_question_ids':IDS,'actual_assessed_question_count':8,'unworked_question_ids':[],'saved_design_count':7,'completed_paired_evidence_candidate_count':7,'completed_candidate_API_call_count':14,'original_control_completed_call_count':0,'all_completed_API_call_count':14,'aborted_call_count':0,'error_call_count':0,'retry_count':0,'credible_twohit_possibility_count':1,'credible_candidate_ids':['Solid126'],'numeric_twohit_count':2,'held_numeric_twohit_ids':['Solid230'],'primary_candidates_only':True,'second_review_queue':str(TASK/'second_review_queue.json'),'assessments':assessments,'new_design_records':entries,'raw_frozen_request_design_image_response_bindings':rawcalls,'full_manual_finals_in_each_candidate_manual_final_review':True,'original_controls':'Noexistingoriginalcontrolcallsinassigned8history;noadditionalcontrolcalls.Noincrementalcausalclaim.','old_history':str(TASK/'old_history_audit.json'),'history_preservation':str(TASK/'source_and_history_audit_final.json'),'primary_math_audit':str(TASK/'independent_primary_math_audit.json'),'primary_math_audit_is_not_second_review':True,'all_candidates_native_viewed':True,'all_candidates_baseline_pixels_equal_twice_byte_identical_schema_normalized':True,'no_live_api_processes':str(TASK/'no_live_api_processes.json'),'no_own_API_processes_remaining':True,'no_formal_state_env_shared_helper_global_ledger_or_old_evidence_writes':True,'no_nested_agents_threads_worktrees':True,'no_Pass_Collect_approval_or_publication':True,'notes':['Solid230numeric42/42comesfrom6=>5pipmisread,notthefrozenidentitymerge. Retainasholdanddonotrelabelintent.','Genericmathunionhelperground-excludeddiagnosticdoesnotapplytoSolid102orSolid231;fullsurface46/26used.','Solid126oldpresetC/A,AandSolid160oldA/B,BandSolid196old32/64,64remainMISSESforever.']})
write(TASK/'report.json',{'unit':'background_37','assessed':8,'new_designs':7,'completed_real_calls':14,'credible_primary_candidate':'Solid126 / r37_local_area_replacement / presetA / A,A / formalB','held_numeric_pair':'Solid230 / r37_equal_value_face_identity / preset42 /42,42 / formal41; intendedmechanismnotobserved','misses':{e['question_id']:e['manual_finals'] for e in entries if e['question_id'] not in ['Solid126','Solid230']},'skipped':'Solid177 occluded center contacts cannot form6clearcorrespondences','errors':0,'aborts':0,'retries':0,'live_own_API_processes':0,'checkpoint':str(TASK/'checkpoint.json'),'queue':str(TASK/'second_review_queue.json')})
print(json.dumps(read(TASK/'report.json'),ensure_ascii=False))
