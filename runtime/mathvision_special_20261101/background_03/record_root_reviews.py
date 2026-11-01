from research import *

stalled=HERE/'Solid238/subrange_14_binding/tests/quicktest3_20261101T114434_58d20adf0562'
started=json.loads((stalled/'run_02_started.json').read_text(encoding='utf-8-sig'))
cleanup=json.loads((stalled/'process_cleanup.json').read_text(encoding='utf-8-sig'))
if not (stalled/'run_02_aborted.json').exists():
    elapsed=(datetime.fromisoformat(cleanup['recorded_at'])-datetime.fromisoformat(started['started_at'])).total_seconds()
    write(stalled/'run_02_aborted.json',{
        'question_id':'Solid238','variant_id':'subrange_14_binding','run_index':2,
        'status':'aborted_after_stall','recorded_at':datetime.now(timezone.utc).isoformat(),
        'reason':'No response for more than five minutes; finite checkpoint; no retry.',
        'elapsed_seconds_until_verified_cleanup':elapsed,
        'verified_own_pid':18840,
        'verified_command_line':'"C:\\Users\\lym\\miniconda3\\python.exe" -X utf8 -B runtime/mathvision_special_20261101/background_03/run_root_test.py Solid238 subrange_14_binding',
        'verification_method':'Get-CimInstance PID and exact expected command-line substring checked by abandon_stalled_238.ps1 immediately before Stop-Process; process_cleanup.json confirms absence.',
        'request_started_evidence':'run_02_started.json','request_binding':'binding.json',
        'answer_valid_for_two_hit':False,'local_request_timeout_or_profile_changed':False,'retry':False,
        'audit_note':'The initial PowerShell logging hashtable failed because false lacked its $ prefix. Process identity verification and stop still completed; this explicit abort record was then reconstructed from immutable started evidence and cleanup. No request was rerun.'})

manual=[
    {'question_id':'Solid245','variant':'height_to_slant_pair','preset':'228\\pi',
     'manually_read_final_answers':['256\\pi','256\\pi'],'hits':0,
     'decision':'reject_target_not_reached','math_check':'Unique256pi from R10,r4,h8,L10; both full completions correctly distinguish height and slant.'},
    {'question_id':'Solid246','variant':'whole_width_to_AB_pair','preset':'\\frac{3}{2}\\pi',
     'manually_read_final_answers':['3\\pi/4','3\\pi/4'],'hits':0,
     'decision':'reject_target_not_reached','math_check':'Unique3pi/4 from delta radius3 and anglepi/4. Both outputs mention3pi/2 as B travel only; this incidental intermediate value does NOT count.'},
    {'question_id':'Solid242','variant':'cut_face_membership','preset':'96\\pi',
     'manually_read_final_answers':['96\\pi+120','96\\pi+120'],'hits':0,
     'decision':'reject_target_not_reached','math_check':'Unique96pi+120; both completions include the rectangular cut face despite appearance-only dashed boundary.'},
    {'question_id':'Solid213','variant':'nine_unit_basis_binding','preset':'C',
     'manually_read_final_answers':['A (states computed3sqrt29/5, then explicitly corresponds to A)','D'],
     'hits':0,'decision':'reject_target_not_reached',
     'math_check':'UniqueA=3sqrt33/5 by exact3D line clipping. Both model responses make other projection/layout mistakes but neither final equals predeclaredC. Run1 expression conflicts with the selected A, disclosed rather than normalized into a hit.'},
    {'question_id':'Solid238','variant':'subrange_14_binding','preset':'448',
     'manually_read_final_answers':['1040',None],'hits':0,'decision':'reject_incomplete_and_target_miss',
     'run_statuses':['completed','aborted_after_stall'],
     'math_check':'Unique192: AH=BJ=8, prism axial FE=HJ=8, GJ=GH-HJ=6, volume=(8*6/2)*8. Run1 instead asserts false AB=GH=14 and ends1040. Run2 no answer, PID18840 safely stopped.'}
]
for item in manual:
    folder=HERE/item['question_id']/item['variant']
    item['folder']=str(folder.relative_to(PROJECT))
    item['full_final_answers_manually_read']=True
    item['design_sha256']=sha(folder/'design.json')
    item['image_sha256']=sha(folder/'candidate.png')
    item['all_evidence_paths']=[str(p.relative_to(PROJECT)) for p in sorted(folder.rglob('*')) if p.is_file()]
    item['actual_png_viewed']=True
    item['primary_marker_and_math_review_in']='design.json and primary_prescreen.json'
    item['independent_second_review']='not_requested_for_failed_candidate'
write(HERE/'root_manual_results.json',manual)
write(HERE/'prepared_Solid240/prescreen_rejection.json',{
    'question_id':'Solid240','variant':'bridge_false_hinge_mapping',
    'decision':'rejected_before_API','expected_wrong_answer':'6','correct_answer':'1',
    'reason':'The actual selected spatial line_20 is hidden edge T-H. The visible edge dividing Q and ? is a different uncolored edge; therefore the declared net-Q/6 to spatial-Q/? hinge correspondence is not conveyed.',
    'marker_roles_actually_observed':{'line_13':'net common edge Q/6','line_20':'hidden edge T-H, not Q/? common boundary'},
    'actual_png_viewed':True,'fresh_baseline_schema_determinism_replay':'fresh_validation.json',
    'new_API_calls':0,'preserved_prepared_files':True,'second_review_candidate':False})
source_checks=[]
for folder in [HERE/'prepared_Solid240/fresh_replay',*[HERE/r['question_id']/r['variant'] for r in manual]]:
    report=json.loads((folder/'render_check.json').read_text(encoding='utf-8-sig'))
    changed=[relative for relative,expected in report['frozen_inputs']['files'].items()
             if not (PROJECT/relative).is_file() or sha(PROJECT/relative)!=expected]
    source_checks.append({'question_id':report['question_id'],'report':str((folder/'render_check.json').relative_to(PROJECT)),
                          'frozen_files_checked':len(report['frozen_inputs']['files']),'changed_files':changed})
write(HERE/'root_source_verification.json',source_checks)
print(json.dumps({'root_tested_variants':len(manual),'root_two_hit_candidates':0,
                  'frozen_input_changes':sum(len(r['changed_files']) for r in source_checks)}))
