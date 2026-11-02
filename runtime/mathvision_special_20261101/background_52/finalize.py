from audit_io import install,OWN,PROJECT,SESSION,load,save,sha,IDS
install()
import json,sys,hashlib,base64
from datetime import datetime,timezone

ongoing='--ongoing' in sys.argv
cases=[];bindings=[];started=0;completed=0;aborted=0;possible=[];untested=[];incomplete=[]
for qid in IDS:
    eligibility=load(OWN/qid/'eligibility_final.json')
    case={'question_id':qid,'source_record':str(OWN/qid/'formal_record.json'),'original_approval_and_current_eligibility':str(OWN/qid/'eligibility_final.json'),'approval_content_sha256':eligibility['current_content_sha256'],'fresh_exact_context':str(OWN/qid/'fresh_context.json'),'exact_native_paths':str(OWN/qid/'exact_paths.json'),'baseline':str(OWN/qid/'baseline_check.json'),'primary_unique_math_or_counterexample':str(OWN/qid/'primary_math_proof.json'),'old_history':str(OWN/qid/'old_history_read.json') if (OWN/qid/'old_history_read.json').exists() else None,'designs':[]}
    for f in sorted((OWN/qid).glob('r52_*')):
        d=load(f/'design.json')
        primary=load(f/'primary_review_before_calls.json')
        assert primary['design_sha256']==sha(f/'design.json') and primary['image_sha256']==sha(f/'candidate.png')
        assert sha(f/'candidate.png')==sha(f/'repeat.png')==d['image_sha256']
        design={'variant_id':d['variant_id'],'wrong_preset_unchanged':d['expected_wrong_answer'],'design_path':str(f/'design.json'),'design_sha256':sha(f/'design.json'),'plugin_path':str(f/'plugin.json'),'plugin_sha256':sha(f/'plugin.json'),'image_path':str(f/'candidate.png'),'image_sha256':sha(f/'candidate.png'),'difference_audit':str(f/'design_difference_audit.json'),'primary_math_marker_native_review':str(f/'primary_review_before_calls.json'),'native_preservation':str(f/'native_preservation_audit.json'),'offline_replay':str(f/'post_test_offline_replay.json'),'schema_noop_repeats':str(f/'render_check.json'),'possible_primary_two_hit':False,'calls_started':0,'calls_completed':0}
        tests=list((f/'tests').glob('*/binding.json')) if (f/'tests').exists() else []
        if not tests:
            design['status']='FROZEN_UNTESTED_due_to_external_stop' if not ongoing else 'frozen_not_called_yet'
            untested.append(qid)
        else:
            assert len(tests)==1
            p=tests[0];b=load(p);test=p.parent
            assert sha(f/'design.json')==b['design_sha256']==sha(test/'design_snapshot.json')
            assert sha(f/'candidate.png')==b['image_sha256']
            request=load(test/'request.json')
            assert sha(test/'request.json')==b['request_body_sha256']
            assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
            assert set(request)=={'model','stream','thinking','messages'}
            assert request['messages'][0]['content']==b['system_prompt']
            text,image=request['messages'][1]['content']
            assert text=={'type':'text','text':eligibility['formal_record']['question']}
            assert base64.b64decode(image['image_url']['url'].split(',',1)[1])==(f/'candidate.png').read_bytes()
            run_starts=sorted(test.glob('run_*_started.json'));run_jobs=[p for p in [test/'run_01.json',test/'run_02.json'] if p.exists()]
            started+=len(run_starts);design['calls_started']=len(run_starts)
            design['calls_completed']=sum(load(p)['status']=='completed' for p in run_jobs);completed+=design['calls_completed']
            evidence={'question_id':qid,'variant_id':d['variant_id'],'binding_path':str(p),'binding_sha256':sha(p),'request_path':str(test/'request.json'),'request_sha256':sha(test/'request.json'),'design_path':str(f/'design.json'),'design_sha256':sha(f/'design.json'),'image_path':str(f/'candidate.png'),'image_sha256':sha(f/'candidate.png'),'frozen_expected_wrong_answer':b['expected_wrong_answer'],'raw_and_partial_artifacts':[{ 'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(test.iterdir()) if p.is_file()]}
            if (f/'manual_final_review.json').exists():
                review=load(f/'manual_final_review.json')
                design.update(status=review['status'],manual_final_answers=review['manual_final_answers'],manual_full_finals_path=str(f/'manual_final_review.json'),possible_primary_two_hit=review['possible_primary_two_hit'])
                if review['possible_primary_two_hit']:possible.append({**design,'question_id':qid})
            else:
                incomplete.append(qid)
                bodies=[]
                for raw in sorted(test.glob('run_*_response.json')):
                    body=load(raw)['choices'][0]
                    bodies.append({'path':str(raw),'sha256':sha(raw),'finish_reason':body['finish_reason'],'complete_body':body['message']['content'],'manually_read_terminal_answer':'8' if qid=='Plane483' and raw.name=='run_01_response.json' else None,'matches_frozen_preset':False if qid=='Plane483' and raw.name=='run_01_response.json' else None})
                abort=(f/'manual_abort_record.json')
                design['status']='ABORTED_STALLED_SECOND_CALL' if abort.exists() else 'IN_PROGRESS_SECOND_CALL'
                design['manual_final_answers']=['8',None] if qid=='Plane483' else []
                if abort.exists():aborted+=1
                save(f/'partial_pair_review.json',{'question_id':qid,'variant_id':d['variant_id'],'frozen_wrong_preset':d['expected_wrong_answer'],'status':design['status'],'primary_only':True,'complete_responses':bodies,'missing_response_is_not_no_call':True,'started_call_count':len(run_starts),'completed_call_count':design['calls_completed'],'manual_abort_record':str(abort) if abort.exists() else None,'no_retry_or_preset_relabel':True,'possible_candidate':False,'reason':'The saved first full final is8, not frozen5; the second request has a started record but no completed final. No old/new or cross-image combination is allowed.'})
                design['partial_review']=str(f/'partial_pair_review.json')
            bindings.append(evidence)
        case['designs'].append(design)
    if (OWN/qid/'skip_assessment.json').exists():case['skip']=load(OWN/qid/'skip_assessment.json')
    cases.append(case)

errors={'local_failures':[{'type':'TypeError: ndarray not JSON serializable','location':'initial prepare.py exact_paths snapshot','effect':'Local snapshot initialization stopped before any API call. Saved controls as full-precision lists and re-ran initialization; no source mutation or solver retry.'},{'type':'AssertionError from comparing replaced style-artist registry','location':'native_preservation.py original first audit','evidence':str(OWN/'Plane480/r52_unit_side_to_two_unit_triangle_bases/native_snapshot_difference.json'),'resolution':'Full original artist handles, semantic fill membership, labels and viewport subsequently match; all5 native audits and replay byte checks pass. Frozen designs/PNGs unmodified.'}],'external_failure':load(OWN/'external_failure.json') if (OWN/'external_failure.json').exists() else None,'API_retries':0,'preset_relabels':0,'old_failed_or_aborted_image_retries':0}
save(OWN/'exceptions.json',errors)

status='in_progress_waiting_on_Plane483_second_request' if ongoing else 'checkpoint_external_host_failure' if errors['external_failure'] else 'finite_unit_complete'
checkpoint={'unit':'background_52','stage':'material_refinement','status':status,'updated_at_utc':datetime.now(timezone.utc).isoformat(),'question_ids':IDS,'actual_assessed_question_ids':IDS,'unworked_question_ids':[],'untested_frozen_design_question_ids':untested,'incomplete_pair_question_ids':incomplete,'new_design_count':sum(len(c['designs']) for c in cases),'calls_started':started,'calls_completed':completed,'calls_aborted':aborted,'complete_two_call_pairs':sum(len(c['designs']) and (OWN/c['question_id']/c['designs'][0]['variant_id']/'manual_final_review.json').exists() for c in cases),'new_credible_possible_candidate_count':len(possible),'cases':cases,'frozen_request_design_image_response_bindings':bindings,'source_preservation':str(OWN/'source_preservation_final.json'),'old_evidence_preservation':str(OWN/'old_evidence_preservation_final.json'),'protocols':str(OWN/'protocol_read_receipt.json'),'harness_isolation_audit':str(OWN/'harness_isolation_audit.json'),'exceptions':str(OWN/'exceptions.json'),'process_status':'See process_closure.json; no API process may remain at final handoff.' if not ongoing else 'Plane483 second request still active, new requests paused.','limits':['Primary research only, not independently second-reviewed or delivered.','Only unchanged original formalquestion and candidatePNG entered each solver request.','No original controls existed for these exact8 question histories; none were repeated or added.','No original-image gain, statistical reliability, human population result or causal ablation is asserted.'],'no_approval_Pass_Collect_publication':True,'all_new_writes_only_own_root':str(OWN)}
save(OWN/'checkpoint.json',checkpoint)
save(OWN/'second_review_queue.json',{'unit':'background_52','stage':'material_refinement','updated_at_utc':datetime.now(timezone.utc).isoformat(),'possible_candidates':possible,'count':len(possible),'requires_NEW_independent_parent_review':True,'self_second_review_performed':False,'approval_Pass_Collect_publication_performed':False,'checkpoint':str(OWN/'checkpoint.json'),'untested_frozen_designs_are_not_candidates':untested})
print(json.dumps({k:checkpoint[k] for k in ['status','actual_assessed_question_ids','new_design_count','calls_started','calls_completed','calls_aborted','complete_two_call_pairs','new_credible_possible_candidate_count','untested_frozen_design_question_ids']},ensure_ascii=False))
