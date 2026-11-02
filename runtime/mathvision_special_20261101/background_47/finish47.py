from env47 import *
import json
import hashlib
from datetime import datetime,timezone
from inspect47 import IDS,BRANCH,eligibility
from prepare47 import DEFS
from dataset_tools.catalog import digest

def main():
    own_process=json.loads((OWN/'no_live_api_processes.json').read_text(encoding='utf-8-sig'))
    assert own_process['matching_owned_API_process_count']==0
    before=json.loads((OWN/'source_hashes_before.json').read_text(encoding='utf-8'))
    source_comparison=[{'path':p,'before':h,'after':sha(p),'matches':h==sha(p)} for p,h in before.items()]
    old_comparison=[];old_errors=[]
    for qid in IDS:
        for entry in json.loads((OWN/qid/'old_file_manifest.json').read_text(encoding='utf-8')):
            current=sha(entry['path'])
            old_comparison.append({'path':entry['path'],'before':entry['sha256'],'after':current,'matches':current==entry['sha256']})
        dossier=json.loads((OWN/qid/'reading_dossier.json').read_text(encoding='utf-8'))
        old_errors += [d for d in dossier if 'parse_error' in d or 'global_parse_error' in d]
    preservation={'tracked_source_files':source_comparison,'tracked_prior_question_evidence_files':old_comparison,'source_hash_changes':[r for r in source_comparison if not r['matches']],'old_evidence_hash_changes':[r for r in old_comparison if not r['matches']],'strict_guard_blocked_all_writes_outside_own_directory':True,'no_entire_workspace_unchanged_or_actor_attribution_claim':True,'metadata_policy':'Shared mutable progress files are diagnostic runtime metadata; never restored or rewritten. Formal and old evidence files are read-only.','shared_harness_unchanged':sha(ROOT/'harness/quicktest3_isolated.py')==json.loads((OWN/'harness_isolation_audit.json').read_text(encoding='utf-8'))['shared_sha256']}
    dump(OWN/'preservation_final.json',preservation)
    history={
      'Plane452':{'preset':'E','manual_old_finals':['E','D with dimension2x4 inconsistent with formal D=2x7'],'old_two_hits':False,'notes':'First finalE is one preset hit. Second finalD is paired with2x4 and therefore contains an inconsistent letter/value identification. The old pair is not promoted or relabeled.'},
      'Plane456':{'old_designs':0,'old_calls':0,'old_skip':'No concise targeted edge correspondence selected; filling/dissection risk.'},
      'Plane457':{'old_designs':0,'old_calls':0,'old_skip':'No targeted receiver beyond center salience; numeric area condition already sufficient.'},
      'Plane458':{'preset':'D','manual_old_finals':['B','D'],'old_two_hits':False,'notes':'Only one hit; second used wrong B=(4,2),C=(5,3). No old result was reused as a new test.'},
      'Plane460':{'old_designs':0,'old_calls':0,'old_skip':'Matching true protrusion/notch would aid correct cancellation; wrong bounding contour would confuse target.'},
      'Plane462':{'preset':'C','manual_old_finals':['E','E'],'old_two_hits':False,'notes':'Both correct finals miss presetC. First narrative has a peripheral numerical perimeter approximation error; exact comparison stillE.'},
      'Plane463':{'preset':'189','manual_old_finals':['18','24'],'old_two_hits':False,'notes':'Both wrong but neither hits189. No relabel to18 or24; only one small kite exists.'},
      'Plane465':{'old_designs':0,'old_calls':0,'old_skip':'New full fundamental-cell frame could imply tile boundary/crop-as-floor ambiguity.'}
    }
    dump(OWN/'old_history_manual_review.json',{'all_old_candidate_PNGs_opened':True,'all_eight_actual_source_JPGs_and_formal_PNGs_opened':True,'full_old_raw_responses_read_manually':True,'existing_local_binding_inventory':str(OWN/'all_prior_binding_inventory.json'),'question_history':history,'historical_parse_errors':old_errors,'historical_truncated_JSON_policy':'Any truncated bytes stay unchanged and are recorded as called-status unknown unless start/raw evidence establishes calls. No parse failure is treated as no call.','actual_truncated_relevant_files_found':len(old_errors),'no_new_original_control_calls':True})
    results=[];queue=[];assessments=[];calls=0;pairs=0;errors=[];aborts=[];untested=[];incomplete=[]
    for qid in IDS:
        e=eligibility(qid);dump(OWN/qid/'eligibility_final.json',e)
        initial=json.loads((OWN/qid/'eligibility_start.json').read_text(encoding='utf-8'))
        assert e['eligible'] and e['current_content_sha256']==initial['current_content_sha256']
        a={'question_id':qid,'assessed':True,'actual_source_jpg_viewed':True,'native_formal_png_viewed':True,'unique_answer_proof':str(OWN/qid/'math_proof.json'),'current_eligibility_audit':str(OWN/qid/'eligibility_final.json'),'original_approval_content_sha256':e['current_content_sha256'],'old_history_read':str(OWN/qid/'reading_dossier.json')}
        if qid not in DEFS:
            a['status']='screened_no_design';a['reason']=json.loads((OWN/qid/'primary_prescreen.json').read_text(encoding='utf-8'))['reason']
        else:
            root=OWN/qid/DEFS[qid][0]
            starts=list((root/'tests').glob('*/run_*_started.json'))
            calls+=len(starts)
            manualpath=root/'manual_final_review.json'
            if manualpath.exists():
                r=json.loads(manualpath.read_text(encoding='utf-8'))
                summary=json.loads(Path(r['summary_path']).read_text(encoding='utf-8'))
                binding=json.loads(Path(r['binding_path']).read_text(encoding='utf-8'))
                # Supplemental fresh current canonical-record check, independent of narratives.
                assert digest(e['record'])==binding['question_record_sha256']
                assert sha(root/'candidate.png')==r['image_sha256']
                assert sha(root/'design.json')==r['design_sha256']
                assert summary['two_completed'];pairs+=1
                result={'question_id':qid,'variant_id':DEFS[qid][0],'preset':r['preset'],'manual_final_answers':r['manual_final_answers'],'status':r['status'],'preset_hit_count':r['preset_hit_count'],'possible_candidate':r['possible_candidate_for_parent_NEW_independent_review'],'candidate_directory':str(root),'image_path':str(root/'candidate.png'),'image_sha256':r['image_sha256'],'plugin_path':str(root/'plugin.json'),'plugin_sha256':sha(root/'plugin.json'),'design_path':str(root/'design.json'),'design_sha256':r['design_sha256'],'material_difference_audit':str(root/'design_difference_audit.json'),'full_manual_finals':r['full_manual_finals'],'manual_notes':r['manual_notes'],'binding_path':r['binding_path'],'binding_sha256':sha(r['binding_path']),'request_path':r['request_path'],'request_sha256':r['request_sha256'],'summary_path':r['summary_path'],'schema_noop_repeat_audit':str(root/'render_check.json'),'native_preservation_audit':str(root/'native_preservation_audit.json'),'primary_math_visual_marker_review':str(root/'primary_review.json'),'primary_math_proof':str(OWN/qid/'math_proof.json'),'frozen_paths':str(root/'path_fingerprints.json'),'fresh_canonical_formal_record_matches_binding':True,'new_parent_independent_second_review_required':True}
                results.append(result)
                a.update(status=r['status'],variant_id=DEFS[qid][0],final_answers=r['manual_final_answers'],preset=r['preset'],calls=len(starts))
                if result['possible_candidate']:queue.append(result)
            else:
                a.update(status='frozen_prepared_not_called' if not starts else 'called_without_complete_pair',variant_id=DEFS[qid][0],calls=len(starts))
                if not starts:
                    untested.append(qid)
                    a['reason']='No call was issued after the external nonreturning-call stop; frozen design/PNG/native audits retained.'
                else:
                    incomplete.append(qid)
                    if (root/'api_aborted.json').exists():
                        abort_record=json.loads((root/'api_aborted.json').read_text(encoding='utf-8-sig'))
                        aborts.append(abort_record)
                        a['status']='aborted_first_call_without_response_no_retry'
                        a['abort_evidence']=str(root/'api_aborted.json')
                    else:
                        errors.append({'qid':qid,'kind':'no_complete_manual_review','starts':len(starts)})
        assessments.append(a)
    extra_path=OWN/'additional_designs.json'
    extra_designs=json.loads(extra_path.read_text(encoding='utf-8')) if extra_path.exists() else []
    for extra in extra_designs:
        qid=extra['question_id'];root=Path(extra['directory']);definition=extra['definition']
        e=eligibility(qid)
        starts=list((root/'tests').glob('*/run_*_started.json'));calls+=len(starts)
        r=json.loads((root/'manual_final_review.json').read_text(encoding='utf-8'))
        binding=json.loads(Path(r['binding_path']).read_text(encoding='utf-8'))
        assert digest(e['record'])==binding['question_record_sha256']
        assert sha(root/'candidate.png')==r['image_sha256'] and sha(root/'design.json')==r['design_sha256']
        summary=json.loads(Path(r['summary_path']).read_text(encoding='utf-8'));assert summary['two_completed'];pairs+=1
        result={**r,'possible_candidate':r['possible_candidate_for_parent_NEW_independent_review'],'candidate_directory':str(root),'plugin_path':str(root/'plugin.json'),'plugin_sha256':sha(root/'plugin.json'),'material_difference_audit':str(root/'design_difference_audit.json'),'schema_noop_repeat_audit':str(root/'render_check.json'),'native_preservation_audit':str(root/'native_preservation_audit.json'),'primary_math_visual_marker_review':str(root/'primary_review.json'),'primary_math_proof':str(OWN/qid/'math_proof.json'),'frozen_paths':str(root/'path_fingerprints.json'),'new_parent_independent_second_review_required':True}
        results.append(result)
        if result['possible_candidate']:queue.append(result)
        next(a for a in assessments if a['question_id']==qid).setdefault('additional_material_design_evaluations',[]).append({'variant_id':definition[0],'preset':definition[1],'final_answers':r['manual_final_answers'],'status':r['status'],'calls':len(starts),'difference':definition[3]})
    dump(OWN/'assessed_questions.json',assessments)
    dump(OWN/'second_review_queue.json',{'unit':'background_47','stage':'material_refinement','created_at':datetime.now(timezone.utc).isoformat(),'candidate_count':len(queue),'candidates':queue,'parent_must_launch_NEW_independent_review_before_delivery':True,'self_second_review_performed':False,'approval_Pass_Collect_publication_actions':[]})
    checklist={'brief_and_assignment_complete':True,'all_required_root_branch_and_workbench_protocols_read':True,'Plane242_lesson_and_full_independent_report_read':True,'delivered_batches01_to13_studied':str(OWN/'delivered_reference_study.json'),'caches_TMP_and_guard_before_project_imports':str(OWN/'isolation.json'),'fresh_authoritative_approval_and_special_eligibility_per_question':True,'all_source_JPG_native_formal_PNG_current_scenes_inspected':True,'all_old_designs_presets_candidate_PNGs_complete_raws_and_skips_read':str(OWN/'old_history_manual_review.json'),'new_error_rules_and_difference_audits_before_calls':True,'actual_normalization_noop_pixels_repeat_bytes_and_native_marks_reviewed':True,'solver_only_formalquestion_candidatePNG_original_profile':str(OWN/'harness_isolation_audit.json'),'no_new_original_control_calls_or_same_control_repeats':True,'no_retries_or_posthoc_relabels_or_mixed_images':True,'no_extra_geometric_equality_symbols_or_modified_fill_text_point_count':True,'all_own_API_processes_closed':str(OWN/'no_live_api_processes.json'),'all_writes_own_directory_only':str(OWN),'no_formal_or_approval_state_written':True}
    dump(OWN/'requirement_evidence_map.json',checklist)
    external=(OWN/'EXTERNAL_FAILURE_STOP.json').exists()
    checkpoint={'unit':'background_47','stage':'material_refinement','status':'checkpoint_external_nonreturning_call' if external else ('completed_finite_batch' if not errors else 'checkpoint_with_incomplete_work'),'completed_at':datetime.now(timezone.utc).isoformat(),'stop_reason':'external_nonreturning_first_call_aborted_after_exact_own_PID_and_command_verification' if external else ('all_8_assigned_questions_assessed_with_reasonable_meaningful_hypotheses' if not errors else 'external_or_interrupted_failure'),'assigned_question_ids':IDS,'actual_assessed_question_ids':IDS,'assessed_count':len(IDS),'unworked_question_ids':[],'assessment_scope_note':'All8 source/math/history/eligibility assessments are complete; this does not mean all frozen designs received API evaluation. Actual pair/call/untested/interrupted counts are separate.','solver_unworked_question_ids':untested,'solver_incomplete_question_ids':incomplete,'screened_no_design_question_ids':['Plane452','Plane463'],'saved_new_design_count':len(DEFS),'complete_candidate_pair_count':pairs,'actual_API_call_count':calls,'completed_response_count':sum(len(list((OWN/q/d[0]/'tests').glob('*/run_*_response.json'))) for q,d in DEFS.items()),'original_control_call_count':0,'credible_possible_candidate_count':len(queue),'candidate_records':results,'assessments':assessments,'new_vs_old_differences':{q:{'variant_id':d[0],'wrongpreset':d[1],'geometric_rule':d[2],'material_difference':d[3]} for q,d in DEFS.items()},'errors':errors,'aborts':aborts,'retries':0,'offline_QA_exceptions':[str(OWN/'offline_audit_error_01.json')],'offline_QA_resolution':'Exact-palette-only visibility assertion was inappropriate for1pt original black overlap on Plane456; hue-visible pixels and actual native viewing were checked, with frozen PNG unchanged. All later native preservation/visibility audits pass.','historical_relevant_truncated_JSON_count':len(old_errors),'source_and_old_evidence_preservation':str(OWN/'preservation_final.json'),'all_primary_math_marker_native_reviews_complete':True,'all_raw_frozen_bindings_and_full_manual_finals_included':True,'all_own_API_processes_closed':True,'no_live_process_evidence':str(OWN/'no_live_api_processes.json'),'second_review_queue_path':str(OWN/'second_review_queue.json'),'requirement_evidence_map':str(OWN/'requirement_evidence_map.json'),'formal_approval_Pass_Collect_publication_actions':[],'independent_second_review_performed':False,'limitations':['Two observations do not prove a mechanism, causal improvement or statistical gain.','All tested pairs are judged against their own predeclared preset; other repeated wrong values remain misses.','No unchanged failed/aborted image or old original control was called again.','Current source/old evidence hash checks are scoped; no claim that the whole concurrently used workspace stayed unchanged.']}
    checkpoint['saved_new_design_count']=len(DEFS)+len(extra_designs)
    checkpoint['additional_material_differences']=extra_designs
    all_definitions=list(DEFS.items())+[(x['question_id'],x['definition']) for x in extra_designs]
    checkpoint['completed_response_count']=sum(len(list((OWN/q/d[0]/'tests').glob('*/run_*_response.json'))) for q,d in all_definitions)
    prepared=[]
    for qid,definition in all_definitions:
        root=OWN/qid/definition[0]
        prepared.append({'question_id':qid,'variant_id':definition[0],'expected_wrong_answer':definition[1],
                         'frozen_files':{name:{'path':str(root/name),'sha256':sha(root/name)} for name in ['design_difference_audit.json','design.json','plugin.json','candidate.png','repeat.png','context.json','path_fingerprints.json','render_check.json','native_preservation_audit.json','primary_review.json']},
                         'actual_invocation_binding_paths':[str(p) for p in (root/'tests').glob('*/binding.json')],
                         'actual_started_call_paths':[str(p) for p in (root/'tests').glob('*/run_*_started.json')],
                         'API_has_been_called':bool(list((root/'tests').glob('*/run_*_started.json')))})
    checkpoint['all_frozen_prepared_design_records']=prepared
    dump(OWN/'checkpoint.json',checkpoint)
    manifest={str(p.relative_to(OWN)):sha(p) for p in OWN.rglob('*') if p.is_file() and not any(k in p.parts for k in ['tmp','mpl_cache','cache','render_tmp'])}
    dump(OWN/'evidence_manifest.json',manifest)
    print(json.dumps({'assessed':len(IDS),'designs':len(all_definitions),'pairs':pairs,'calls':calls,'possible_candidates':len(queue),'source_hash_changes':len(preservation['source_hash_changes']),'old_hash_changes':len(preservation['old_evidence_hash_changes']),'checkpoint':str(OWN/'checkpoint.json')},ensure_ascii=False))

if __name__=='__main__':main()
