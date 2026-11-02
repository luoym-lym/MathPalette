from worker_env import *
import base64

ass=load(OWN/'assignment.json')
initial=load(OWN/'initial_bytes.json')
assert sha(OWN/'assignment.json')==initial['assignment'] and sha(OWN/'brief.txt')==initial['brief']
variants={'Solid186':['r05_three_patch_changed_area_binding','r05_face_scale_comparison'],
          'Solid226':['r05_removed_roof_to_new_cut_faces','r05_front_plane_loss']}
additional={
 'Solid186':[
   {'relation':'Exact removed/new 2-by-2 patch correspondence','assessment':'Constructed and tested first design, E=2 new-cut-area-only; full finals C/A, no paired hit.'},
   {'relation':'Complete 3-by-3 face versus real 2-by-2 recessed face','assessment':'Constructed and tested second design, D=4 face-scale substitution; full finals A/A, no paired hit.'},
   {'relation':'Remaining versus original voxel count 19/27','assessment':'9*(19/27)=19/3 litres, no exact listed answer. A volume cue alone does not compare paint surface and is not a credible exact new preset; rounding to 6 would be unsupported.'},
   {'relation':'Omit all three newly exposed cut faces','assessment':'54-12=42 unit faces, yielding 7 litres, absent from choices. Cannot silently round or label this as 6/8.'},
   {'relation':'Only omit the unchanged bottom','assessment':'Both complete and modified solids have the same bottom area 9; both remaining exposed totals would be 45. Ratio still 1; no wrong alternative is generated.'},
   {'relation':'Single 3-to-2 edge length ratio instead of area ratio','assessment':'Would predict 6 litres by a linear-scale mistake, but using only a subset of the same failed 3-to-2 face comparison changes no substantive source/receiver relation. Removing the blue half of the L or relabeling the failed face-scale PNG to C is not a new valid experiment.'},
   {'relation':'Color alternate faces or swap red/blue in the tested comparisons','assessment':'Cosmetic same information, prohibited repeat rather than a new correspondence.'},
   {'relation':'Interpret colors as selecting which faces are painted','assessment':'Changes the explicit entire-surface target or creates ambiguity. Rejected; no paint-subset legend or statement added.'}
 ],
 'Solid226':[
   {'relation':'Historical three-new-face L motifs','assessment':'Old preset E, complete raw finals C and D/1 more. Historical input never retried.'},
   {'relation':'Original missing roof square versus three real new cut faces','assessment':'Constructed first new design with a real removed-source counterpart absent from old test. Preset E=2 more; complete finals D/C, no paired hit.'},
   {'relation':'Original 9-by-3 front plane versus 26-unit notched front plane','assessment':'Constructed second new design. True plane-specific loss 1 supplies frozen B=1 less; complete final answers C/C, no paired hit.'},
   {'relation':'Pair former top with new floor, pair all lost and gained patches','assessment':'All real unit areas cancel exactly. This is useful mathematics but supports C and does not supply a different wrong preset.'},
   {'relation':'Bind full width 1 to cut width 1','assessment':'True equal-thickness cue proves the cut is through the board. It supports C. A hidden rear pocket needed for +1/+2 is inconsistent with the actual width and cut.'},
   {'relation':'Only compare the lost front/back patches to force 2 less','assessment':'The rear lost patch is largely occluded in this projection. An explicit distinct rear-source counterpart would require new unshown lower rear boundaries, while the newly exposed side-wall pair of area 2 must also be accounted for. No simple unambiguous new source/receiver presentation was found; a rear-wall invention or ignoring identical failed information is not accepted.'},
   {'relation':'Draw a surviving rear cavity wall or move the notch to a corner','assessment':'Changes actual 3D geometry or frozen visibility and contradicts a width-1 through notch; rejected before construction.'},
   {'relation':'Recolor/resize old new-face motifs or relabel to previously observed D','assessment':'No new information relation. Cannot retest old or new failed PNGs or change their frozen E/B labels.'}
 ]}
all_results=[];source_checks=[];queue=[]
for qid,ids in variants.items():
    e=eligibility(qid);assert e['eligible']
    save(OWN/qid/'eligibility_final.json',e,True)
    math=load(OWN/qid/'primary_mathematics.json')
    for vid in ids:
        f=OWN/qid/vid;d=load(f/'design.json');a=load(f/'manual_finals_and_binding_audit.json')
        assert not a['qualified_PRIMARY']
        assert sha(f/'design.json')==a['design_sha256']==load(f/'render_gates.json')['design_sha256']
        assert sha(f/'candidate.png')==a['image_sha256']==d['image_sha256']
        assert sha(f/'plugin.json')==a['plugin_sha256']==d['plugin_sha256']
        assert sha(f/'context.json')==d['context_sha256']
        assert sha(f/'candidate.png')==sha(f/'independent_process_replay.png')
        for p,h in load(f/'input_manifest.json')['source_manifest'].items():
            assert sha(PROJECT/p)==h
            source_checks.append({'path':str(PROJECT/p),'sha256':h,'unchanged':True})
        summaries=list((f/'tests').glob('*/summary.json'));assert len(summaries)==1
        s=load(summaries[0]);ev=summaries[0].parent
        assert len(list(ev.glob('run_*_started.json')))==2 and len(list(ev.glob('run_*_response.json')))==2
        assert s['two_completed'] and s['requested_runs']==2
        request=load(ev/'request.json')
        assert request['messages'][1]['content'][0]['text']==e['record']['question']
        image=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
        assert image==(f/'candidate.png').read_bytes();del image
        assert sha(ev/'request.json')==s['request_body_sha256']
        assert (ev/'design_snapshot.json').read_bytes()==(f/'design.json').read_bytes()
        pc=load(f/'process_completed.json');assert pc['harness_main_returned'] and pc['observed_urllib_openings']==2
        for i in (1,2):
            assert load(f/f'eligibility_immediately_before_call_{i:02d}.json')['eligible']
            assert load(f/f'network_guard_{i:02d}.json')['request_body_sha256']==s['request_body_sha256']
        save(f/'primary_review_after_calls.json',{'at':now(),'review_kind':'PRIMARY author review only',
          'question_id':qid,'variant_id':vid,'decision':'paired_preset_miss','qualified_PRIMARY':False,
          'unique_correct_answer':math['unique_answer'],'frozen_wrong_answer':d['expected_wrong_answer'],
          'frozen_wrong_value':d['expected_wrong_value'],'complete_terminal_answers':[{'letter':r['manually_read_final_letter'],'value':r['manually_read_final_value']} for r in a['runs']],
          'math':str(OWN/qid/'primary_mathematics.json'),'marker_roles':str(f/'marker_roles.json'),
          'manual_raw_and_binding_audit':str(f/'manual_finals_and_binding_audit.json'),
          'current_eligibility':str(OWN/qid/'eligibility_final.json'),'reference_migration':str(f/'reference_migration.json'),
          'image_sha256':sha(f/'candidate.png'),'plugin_sha256':sha(f/'plugin.json'),'design_sha256':sha(f/'design.json'),
          'no_further_calls_on_this_PNG':True,'preset_changed':False,'no_independent_second_review_or_user_approval':True,
          'limits':['No causal gain or overall success claim.','Wrong answers outside the frozen preset do not count.','Some narratives use incorrect geometry even when terminal answer is correct.']},True)
        all_results.append({'question_id':qid,'variant_id':vid,'candidate_directory':str(f),
          'preset_letter':d['expected_wrong_answer'],'preset_value':d['expected_wrong_value'],
          'terminal_answers':[{'letter':r['manually_read_final_letter'],'value':r['manually_read_final_value']} for r in a['runs']],
          'summary_path':str(summaries[0]),'audit_path':str(f/'manual_finals_and_binding_audit.json'),
          'image_sha256':sha(f/'candidate.png'),'plugin_sha256':sha(f/'plugin.json'),'design_sha256':sha(f/'design.json'),
          'real_calls':2,'status':'paired_preset_miss','PRIMARY':False})
    reason='Two materially different legal source-to-receiver comparisons were tested and neither produced the frozen wrong answer twice. Remaining screened directions either support the correct answer, yield an unlisted number, change the actual problem, add ambiguous/unshown geometry, or repeat the tested information cosmetically. No further substantive valid comparison is currently identified. This is an unresolved qualification outcome, not a proof that every possible Special is impossible.'
    save(OWN/qid/'further_design_prescreen.json',{'at':now(),'question_id':qid,'considered':additional[qid],
      'decision':'no_further_material_valid_correspondence_currently_identified','reason':reason,
      'no_numeric_candidate_cap_or_quota_stop':True,'no_universal_impossibility_claim':True,'failed_designs_all_preserved':True},True)
    save(OWN/qid/'outcome.json',{'question_id':qid,'research_coverage':'assigned question fully assessed',
      'qualification_status':'UNRESOLVED_NO_TWO_HIT_PRIMARY','reason':reason,'new_real_calls':4,
      'tested_variants':ids,'primary_candidates':[],'correct_answer':math['unique_answer'],
      'complete_math_path':str(OWN/qid/'primary_mathematics.json'),'current_eligibility_path':str(OWN/qid/'eligibility_final.json'),
      'further_prescreen_path':str(OWN/qid/'further_design_prescreen.json'),'no_user_Pass_Collect_or_delivery':True},True)

for item in load(OWN/'read_ledger.json'):
    p=Path(item['path']);actual=sha(p);assert actual==item['sha256'],str(p)
    source_checks.append({'path':str(p),'sha256':actual,'unchanged':True})
for q in load(TASK/'history_index.json')['questions']:
    if q['question_id'] not in variants:continue
    for d in q['designs']:
        p=PROJECT/d['frozen_candidate_png_path'];assert sha(p)==d['frozen_candidate_png_sha256']
        source_checks.append({'path':str(p),'sha256':sha(p),'unchanged':True})
closure=load(OWN/'process_closure_check.json')
assert closure['known_API_process_count']==4 and all(not row['own_API_or_child_processes_remaining'] for row in closure['checks'])
save(OWN/'source_preservation_final.json',{'at':now(),'all_checked_source_and_old_evidence_bytes_unchanged':True,
   'files':source_checks,'own_assignment_and_brief_bytes_unchanged':True,'formal_eligibility_current':True,
   'frozen_designs_plugins_contexts_images_replays_and_requests_match':True,
   'restored_or_repaired_old_files':[],'formal_approvals_or_Pass_Collect_actions':0,
   'all_new_files_under_own_root':str(OWN),'other_units_and_parent_progress_not_modified':True},True)
save(OWN/'terminal_reading_notes.json',{'notes':[
 {'question_id':'Solid186','variant_id':'r05_three_patch_changed_area_binding','run':1,'note':'Full reply computes 6.75 and then chooses nearest C=6. Terminal C/6 is not frozen E/2; no rounding-based preset invented after reading it.'},
 {'question_id':'Solid186','variant_id':'r05_face_scale_comparison','run':1,'note':'Narrative computes 62/6 about 10.33 then selects closest A. Terminal letter A maps to 9 in formal choices; numerical narrative is not a verified solution and does not match D=4.'},
 {'question_id':'Solid226','variant_id':'r05_front_plane_loss','run':1,'note':'Opening says Option D, but full calculation ends explicitly Final Answer C: the same. Terminal answer is C, not opening D, and neither matches frozen B.'}
 ],'all_full_raw_responses_read':True,'only_terminal_letter_and_value_checked_against_immutable_preset':True},True)
save(OWN/'question_identity_audit.json',{'Solid186':{'source_key':'test:1727','target':'entire remaining surface','unique_answer':'A:9 litres',
   'source_warning':'Native scene records source questions 732 and 1727 ask different paint quantities. This unit never substituted the new-cut-faces-only question for the formal 1727 wording or borrowed its responses.',
   'new_cut_faces_12_paint_2_only_a_frozen_wrong_subtask':True},
   'Solid226':{'source_key':'test:2547','target':'complete six-sided surface change','unique_answer':'C:the same','full_width_notch_not_rear_pocket':True}},True)
save(OWN/'second_review_queue.json',queue)
report={'at':now(),'unit_id':'u05_surface','scope':list(variants),'status':'RESEARCH_ASSESSED_QUALIFICATION_UNRESOLVED',
   'PRIMARY_candidates':[],'second_review_queue_count':0,'new_real_API_calls':8,'new_frozen_tested_PNGs':4,
   'each_PNG_exactly_two_calls':True,'complete_nontruncated_responses':8,'API_errors':0,'API_aborts':0,'host_or_source_holds':[],
   'unworked_question_ids':[],'qualification_unresolved_question_ids':list(variants),
   'results':all_results,'local_errors':[{'path':str(OWN/'local_error_01.json'),'kind':'Own diagnostic formatting TypeError; repaired offline, all relevant gates rerun; original saved','model_calls_affected':0}],
   'process_closure_check':str(OWN/'process_closure_check.json'),'all_self_API_processes_ended':True,
   'all_local_render_commands_returned_and_figures_closed':True,'source_preservation':str(OWN/'source_preservation_final.json'),
   'no_user_approval_Pass_Collect_delivery_or_independent_review':True,
   'limitations':['No two-hit PRIMARY in either assigned question.','Research is not a universal impossibility proof.','No control calls, overall rate or causal-effect claims.','Parent must launch a new independent second review for any future qualifying PRIMARY.']}
save(OWN/'research_report.json',report,True)
save(OWN/'checkpoint.json',{'at':now(),'unit_id':'u05_surface','status':report['status'],'assigned':list(variants),
   'real_calls':8,'complete_responses':8,'PRIMARY_candidates':0,'questions':{q:{'status':'UNRESOLVED_NO_TWO_HIT_PRIMARY','outcome_path':str(OWN/q/'outcome.json'),'real_calls':4} for q in variants},
   'errors':[str(OWN/'local_error_01.json')],'API_errors':[],'aborts':[],'holds':[],'skips':[],'unworked':[],
   'qualification_unresolved':list(variants),'second_review_queue':str(OWN/'second_review_queue.json'),
   'research_report':str(OWN/'research_report.json'),'source_preservation':str(OWN/'source_preservation_final.json'),
   'processes_closed':True,'closure_check':str(OWN/'process_closure_check.json')})
# Content manifest excludes itself; checkpoint/queue are stable at handoff.
save(OWN/'handoff_file_sha256.json',{'at':now(),'files':{str(p.relative_to(OWN)):sha(p) for p in OWN.rglob('*') if p.is_file() and 'ownruntime' not in p.parts and p.name!='handoff_file_sha256.json'}},True)
print(json.dumps({'scope':list(variants),'PRIMARY':0,'new_calls':8,'API_errors':0,'aborts':0,'unworked':[],
 'qualification_unresolved':list(variants),'report':str(OWN/'research_report.json')},ensure_ascii=False))
