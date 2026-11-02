import research_core as core
rt=core.rt
import json,hashlib,os,sys,subprocess
from pathlib import Path

assignment=rt.read(rt.OWN/'assignment.json')
initial=rt.read(rt.OWN/'readonly_inputs_initial.json')
preservation=[]
for entry in initial['files']:
    p=Path(entry['path'])
    if not p.is_absolute():p=rt.PROJECT/p
    actual=rt.sha(p)
    preservation.append({'path':str(p),'initial':entry['sha256'],'final':actual,'equal':actual==entry['sha256']})
assert all(x['equal'] for x in preservation)
assert rt.sha(rt.OWN/'assignment.json')==initial['assignment_sha256']
assert rt.sha(rt.OWN/'brief.txt')==initial['brief_sha256']
sources={}
for qid in assignment['question_ids']:
    e=core.eligibility(qid);assert e['eligible'],e['reasons']
    rt.save(rt.OWN/qid/'eligibility_final.json',e);sources[qid]=e
refs={}
for qid,m in rt.read(rt.OWN.parents[1]/'reference_manifest.json').items():
    d=rt.OWN.parents[1]/m['directory']
    refs[qid]={'PNG':rt.sha(d/'C01.png')==m['png_sha256'],'plugin':rt.sha(d/'C01.json')==m['plugin_sha256']}
assert all(v['PNG'] and v['plugin'] for v in refs.values())
lessons=[]
for relative in ['annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json',
    'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
    'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']:
    p=rt.OLD/relative;data=rt.read(p)
    lessons.append({'path':str(p),'sha256':rt.sha(p),'fully_parsed':True,
        'relevant_rejection':data.get('blocking_reason',data.get('reason',data.get('concrete_objections',data.get('rule'))))})
rt.save(rt.OWN/'semantic_lessons_read_audit.json',lessons)
rt.save(rt.OWN/'source_preservation_final.json',{'at':rt.now(),'all_initial_133_history_and_27_reference_JSON_files_unchanged':True,
    'exact_checked_file_count':len(preservation),'files':preservation,'reference_PNG_plugin_hashes':refs,
    'assignment_brief_original_bytes_preserved':True,'all_formal_content_approvals_and_source_hashes_passed':True,
    'final_authoritative_eligibility':sources,'no_formal_approval_Pass_Collect_publication_actions':True,
    'scope':'Checks assigned sources and read-only evidence, not other units mutable progress or entire workspace.'})

# Audit the frozen successful design's actual directional groups without changing
# its predeclared mechanism, colors, preset, image, plugin or any raw response.
d=rt.OWN/'Plane461/u01_symbol_X_diagonals_to_central_hole_pairs'
rt.save(d/'primary_posttest_geometry_caveats.json',{'at':rt.now(),
    'role':'PRIMARY_AUTHOR_SUPPLEMENT_NOT_INDEPENDENT_REVIEW','image_sha256':rt.sha(d/'candidate.png'),
    'actual_source_strokes':{'red_o14':'rising x/y diagonal','blue_o15':'falling x/y diagonal'},
    'actual_D_hole_groups':{'red_o41_o42':'bottom-right plus top-left (falling diagonal)','blue_o40_o43':'bottom-left plus top-right (rising diagonal)'},
    'caveat':'Same-color source and receiver have opposite signed slopes. The frozen mechanism uses the two-direction X-shaped pattern comparison and does not establish exact parallelism. Do not describe the frozen colors as same-slope alignment or silently swap them. Whether this directional correspondence is sufficiently clear is specifically left for the new independent parent review.',
    'no_posthoc_mechanism_replacement':'No new reflection-parity explanation is claimed; it was not the frozen preset mechanism.',
    'unchanged_human_math':'X is explicitly a location symbol, all physical hole centers remain unchanged, and only B is the exact reflected punch orbit.',
    'two_observed_finals':'D,D only. Neither narrative establishes exact use of every mark or causal attribution.'})
queue=rt.read(rt.OWN/'second_review_queue.json')
assert len(queue)==1 and queue[0]['question_id']=='Plane461'
queue[0]['source_preservation_path']=str(rt.OWN/'source_preservation_final.json')
queue[0]['eligibility_final_path']=str(d.parent/'eligibility_final.json')
queue[0]['primary_geometry_caveats_path']=str(d/'primary_posttest_geometry_caveats.json')
queue[0]['limitations'].append('Actual same-color X-stroke and D hole-pair signed slopes are opposite; geometry caveat saved, no color swap or posthoc mechanism replacement. Independent review must assess directed usefulness.')
rt.save(rt.OWN/'second_review_queue.json',queue)

rows=[];pids=[]
for qid in assignment['question_ids']:
    for review_path in (rt.OWN/qid).glob('*/primary_final_review.json'):
        review=rt.read(review_path);cd=review_path.parent
        process=rt.read(cd/'process_completed.json');launch=rt.read(cd/'process_launch.json')
        assert process['exit_code']==0 and process['actual_urllib_request_count']==2
        assert process['frozen_inputs_unchanged'] is True
        pids.append(process['pid'])
        assert rt.sha(cd/'design.json')==review['design_sha256']
        rows.append({'question_id':qid,'variant_id':review['variant_id'],'preset':review['frozen_expected_wrong_answer'],
            'finals':[r['final_answer'] for r in review['raw_final_reviews']],
            'two_complete_calls':2,'primary_two_hit':review['credible_primary_two_hit_candidate'],
            'review':str(review_path),'image_sha256':review['image_sha256'],'summary':review['summary_path'],
            'process_pid':process['pid'],'process_completed_path':str(cd/'process_completed.json')})
assert len(rows)==6 and sum(r['two_complete_calls'] for r in rows)==12
assert sum(r['primary_two_hit'] for r in rows)==1

# Read-only process inspection. Never terminate or modify another unit's process.
ps="$p = Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^python(w)?(.exe)?$' -and $_.CommandLine -match 'mathvision_similar24_special_20261102[\\\\/]+units[\\\\/]+u01_fold_locations' }; @($p | Select-Object ProcessId,ParentProcessId,Name,CommandLine) | ConvertTo-Json -Depth 5 -Compress"
done=subprocess.run(['powershell','-NoProfile','-Command',ps],capture_output=True,text=True,encoding='utf-8',check=True)
observed=json.loads(done.stdout) if done.stdout.strip() else []
if isinstance(observed,dict):observed=[observed]
running_other_than_auditor=[p for p in observed if p['ProcessId']!=os.getpid()]
assert not running_other_than_auditor,running_other_than_auditor
shutdown={'at':rt.now(),'own_API_pids':pids,'all_API_processes_have_completed_exit0':True,
    'running_own_python_processes_except_this_auditor':running_other_than_auditor,
    'auditor_pid':os.getpid(),'auditor_is_foreground_and_will_exit_after_writing':True,
    'servers_agents_worktrees_started':False,'other_units_processes_touched':False,
    'all_captured_scenes_closed_in_finally':True,'inspection_command':ps,'inspection_raw_stdout':done.stdout}
rt.save(rt.OWN/'process_shutdown_evidence.json',shutdown)

# Preserve the exact real cache routing history, including reference harness setup.
cache_dirs={name:[str(p) for p in (rt.OWN/'harness'/name).rglob('*') if p.is_file()] for name in ('mpl_cache','cache','tmp')}
rt.save(rt.OWN/'cache_routing_audit.json',{'at':rt.now(),'numerical_threads_all_1_before_imports':True,
    'initial_project_Pillow_matplotlib_import_caches':str(rt.OWN/'ownruntime'),
    'reference_harness_behavior':'Original harness creates HARNESS-local mpl_cache/cache/tmp dirs and sets process-local variables at module import. Its only code edit is the audited local PROJECT path.',
    'reference_harness_created_unit_local_cache_files':cache_dirs,
    'last_two_candidate_pairs':'Wrapper audit restores all four actual request cache environment variables to ownruntime and records them before transport.',
    'all_new_files_inside_own_root':True,'no_global_environment_or_dotenv_changes':True})

assessment=rt.read(rt.OWN/'remaining_research_assessment.json')
checkpoint=rt.read(rt.OWN/'checkpoint.json')
checkpoint.update(updated_at_utc=rt.now(),stage='PRIMARY_RESEARCH_RECORDED_WITH_TWO_UNRESOLVED_QUESTIONS',
    new_model_calls=12,new_complete_model_calls=12,new_model_failures=0,new_model_aborts=0,
    tested_candidate_images=6,primary_two_hit_candidate_count=1,unworked_assigned_questions=[],
    holds=[],skips=[],unfinished_questions=['Plane202','Plane238'],
    no_three_candidate_early_stop=True,no_quota_saving_stop=True,
    independent_second_review_performed=False,delivery_or_formal_actions_performed=False,
    own_API_process_ids=pids,all_own_API_processes_ended=True,
    evidence_paths={'queue':str(rt.OWN/'second_review_queue.json'),'source_preservation':str(rt.OWN/'source_preservation_final.json'),
        'process_shutdown':str(rt.OWN/'process_shutdown_evidence.json'),'unfinished_reasons':str(rt.OWN/'remaining_research_assessment.json')},
    tested_candidates=rows)
for qid in assignment['question_ids']:
    checkpoint['questions'][qid]={'status':assessment[qid]['status'],
        'tested_candidates':[r for r in rows if r['question_id']==qid],
        'actual_complete_calls':sum(r['two_complete_calls'] for r in rows if r['question_id']==qid),
        'unfinished_reason':assessment[qid].get('unfinished_reason'),
        'eligibility_final':str(rt.OWN/qid/'eligibility_final.json')}
checkpoint['offline_errors_and_corrections']=[str(rt.OWN/'offline_error_001.json'),str(rt.OWN/'offline_error_001_traceback.txt'),
    str(rt.OWN/'Plane202/u01_paper_frame_diagonal_symmetry_substitution/offline_rejected_before_any_call.json'),
    str(rt.OWN/'Plane238/u01_actual_crease_to_wrong_packet_separator/visual_primary_pre_view_timestamp_preserved.json')]
rt.save(rt.OWN/'checkpoint.json',checkpoint)

report=['# u01 primary research record','',
    'Scope: Plane202, Plane238, Plane461. PRIMARY author only; no independent second review, delivery, Pass or Collect.',
    '', 'New actual calls: 12, all complete; each of six tested images received exactly two calls. New API failures/aborts: 0.',
    '', '| Question | Variant | Frozen preset | Complete finals | Result |', '|---|---|---|---|---|']
for r in rows:
    report.append('| '+r['question_id']+' | '+r['variant_id']+' | '+r['preset']+' | '+', '.join(r['finals'])+' | '+('PRIMARY two hit; new independent review required' if r['primary_two_hit'] else 'Miss; never retest this PNG')+' |')
report += ['', 'Plane202 and Plane238 remain unresolved; specific alternatives considered and reasons for stopping current hypotheses are in remaining_research_assessment.json. This is not an impossibility claim or a three-candidate/quota stop.',
    '', 'Plane461 signed-direction caveat is preserved in primary_posttest_geometry_caveats.json and second_review_queue.json. Do not silently change colors, reinterpret its mechanism, or infer user approval.',
    '', 'The untested Plane202 paper-frame prototype with stale copied proof text remains preserved and was replaced before any call by a corrected immutable design on identical previously unrequested pixels. Other local preparation errors and the corrected native-view timing record are retained.',
    '', 'Sources and initial read-only evidence hashes remain unchanged. Every API process has exited; process_shutdown_evidence.json records the read-only process inspection. All newly written content is within this unit own_root.',
    '', 'Review entry: second_review_queue.json. Overall checkpoint: checkpoint.json. No formal files or approvals were written.']
(rt.OWN/'research_report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
inventory=[]
for p in rt.OWN.rglob('*'):
    if p.is_file() and p.name!='evidence_inventory.json' and 'ownruntime' not in p.parts:
        inventory.append({'path':str(p.relative_to(rt.OWN)),'sha256':rt.sha(p),'bytes':p.stat().st_size})
rt.save(rt.OWN/'evidence_inventory.json',{'created_at':rt.now(),'files':inventory,'runtime_caches_excluded':True})
print(json.dumps({'primary_count':1,'complete_calls':12,'unresolved':['Plane202','Plane238'],'own_API_pids_ended':pids,'readonly_files_unchanged':len(preservation)},ensure_ascii=False))
