"""Preserve research evidence, current qualification and process closure for u04."""
import research as r
import subprocess
import os

# A first finalization stopped on a local report-key typo after writing these
# read-only audits. Preserve them; compare every value exactly while retaining
# their original top-level observation timestamp. No model work is resumed.
_original_save=r.save
def final_save(path,value,new=False):
    path=r.Path(path)
    if new and path.exists():
        assert path.name in ('unresolved_assessment.json','eligibility_final.json','readonly_preservation_final.json'),path
        saved=r.read(path)
        comparison=r.json.loads(r.json.dumps(value,ensure_ascii=False))
        for field in ('created_at','checked_at'):
            if field in saved and field in comparison: comparison[field]=saved[field]
        assert saved==comparison,'Existing finalization evidence differs beyond observation timestamp: '+str(path)
        return
    return _original_save(path,value,new=new)
r.save=final_save

assessment={
 'question_id':'Plane490','created_at':r.now(),'role':'PRIMARY research; no independent second review',
 'status':'UNRESOLVED_NO_QUALIFYING_PRIMARY',
 'unique_original_answer':'180; existence by all7 vertex negations and uniqueness by nonzero vertex mean',
 'tested_distinct_hypotheses':[
   {'variant':'a01_shared_boundary_invariance','new_information':'Actual spatially coincident common Z subset, with180-invariant red end walls and blue middle.','frozen_wrong':'0','complete_finals':['180','180'],'outcome':'Failed0/2'},
   {'variant':'a02_corresponding_arrowhead_flank_directions','new_information':'Actual corresponding sloped head-edge direction classes, middle strips; black/gray endpoints retained.','frozen_wrong':'0','complete_finals':['90','90'],'outcome':'Failed0/2; two wrong90 finals cannot be relabeled as0 or promoted.'},
   {'variant':'a03_true_corresponding_notch_right_angles','new_information':'Actual corresponding nonshared concave L notches; small white opening90 versus full rigid180.','frozen_wrong':'90','complete_finals':['180','180'],'outcome':'Failed0/2'}],
 'additional_correspondence_prescreen':[
   {'family':'Parallel same-side shaft matching','decision':'Not pursued','reason':'Old primary objections remain: it discards the head reversal and only repeats a translation/local parallelism cue; no materially new relation beyond tested commonZ and head-flank classes.'},
   {'family':'Pair a source slant to a perpendicular/noncorresponding target wall','decision':'Reject','reason':'The compared parts are not true corresponding equal edges. A false red/blue permutation generally fails to map under the original unique180, creating an intrinsic-edge-color no-solution reading. No new false mapping condition is authorized.'},
   {'family':'Recolor/reverse one whole arrow or overwrite its decisive gray identity','decision':'Reject','reason':'Changes the explicitly designated darker/lighter figures or arrow direction; violates task meaning.'},
   {'family':'CenterC dot, label, isolated angle/option highlight','decision':'Reject','reason':'No specific relational information; only salience. The question has no numeric option to match.'},
   {'family':'New lines joining C to true arrow tips or corresponding vertex dots','decision':'No reliable wrong-angle hypothesis','reason':'Both tip-radius vectors are exact negatives, so direct true correspondence reinforces180. Removing/relocating tips, direction arrows or labels to force a quarterturn is prohibited.'},
   {'family':'Combine all previous marks / change colors widths / retest failed PNG','decision':'Reject','reason':'No new effective information relation, and would risk visual clutter or prohibited retries. Each failed frozen input is retained with its original preset and both finals.'},
   {'family':'A new complete color-preserving corner/side comparison not in the above','decision':'None established in this research','reason':'The rigid mapping and entire directed arrow orientation still force180. I have no further grounded, concise relation with a distinct incorrect pre-test inference; this is not a proof that every possible future annotation must fail.'}],
 'why_research_stops_here':'No further substantive valid new correspondence is currently established. This is not quota saving, a three-candidate cap, a claim of universal impossibility, or acceptance of the second design outside its preset.',
 'remaining_work':'Parent may continue only if a genuinely new valid semantic correspondence is identified, with new frozen input/preset, full offline gates and exactly2 new calls. None of these failed PNGs may be retried.',
 'calls':6,'failed_frozen_candidates':3,'API_errors':0,'aborts':0,
 'human_semantics':'All three are intended as legal true-boundary comparisons with the original unique180 retained, including literal colored-edge mappings. Their failure is the required final-preset gate, not repaired by changing the original answer.',
 'extra_diagnostic':'A03 supplemental unmarked-crop exact-RGBA assertion failed at24 dark-tip antialias pixels; complete exact difference and unchanged executor explanation retained. No pixel patch, rerender retry, source/candidate hash drift, or numerical tolerance introduced.'}
r.save(r.OWN/'Plane490/unresolved_assessment.json',assessment,new=True)

protected={}
for filename in ('initial_read_manifest.json','history_full_read_manifest.json'):
    saved=r.read(r.OWN/filename)
    entries=saved.get('files',saved.get('files_sha256'))
    for relative,digest in entries.items(): protected[relative]=digest
preservation=[]; metadata_changes=[]; drift=[]
for relative,before in sorted(protected.items()):
    after=r.sha(r.PROJECT/relative)
    entry={'path':relative,'before':before,'after':after,'exact_equal':before==after}
    preservation.append(entry)
    if before!=after:
        if relative.replace('\\','/').endswith('/task.json'):
            metadata_changes.append(entry)
        else:
            drift.append(entry)
assert not drift,drift
qualifications={}
for qid in ('Plane321','Plane490'):
    current=r.eligibility(qid); assert current['eligible']
    r.save(r.OWN/qid/'eligibility_final.json',current,new=True)
    qualifications[qid]={'source_dataset':current['record']['source_dataset'],
                        'current_content_sha256':current['recomputed_content_sha256'],
                        'approval_content_sha256':current['approval']['content_sha256'],
                        'eligible':True,'accepted':current['indices']['accepted_index.jsonl'],
                        'collected':current['indices']['collected_index.jsonl'],
                        'recipes':current['recipes'],'collection':current['collection'],
                        'frozen_source_files_sha256':current['source_files_sha256']}
r.save(r.OWN/'readonly_preservation_final.json',{'created_at':r.now(),'protected_files':preservation,
     'protected_file_count':len(preservation),'source_and_history_drift':drift,
     'parent_metadata_changes_not_restored':metadata_changes,'qualifications':qualifications,
     'strict_guard_root':str(r.OWN),'all_new_writes_confined_to_own_root':True,
     'original_env_or_git_edits':False,'formal_approval_Pass_Collect_actions':0},new=True)

calls=[]; invocations=[]; pid_files=[]
for summary_file in sorted(r.OWN.glob('Plane*/*/tests/*/summary.json')):
    directory=summary_file.parent; summary=r.read(summary_file)
    candidate=directory.parent.parent; design=r.read(candidate/'design.json')
    assert r.sha(candidate/'design.json')==summary['design_sha256']
    assert r.sha(candidate/'candidate.png')==summary['image_sha256']
    gate=r.read(candidate/'render_gates.json')
    for name,key in [('plugin.schema.json','schema_sha256'),('mathvision_plugins.py','renderer_sha256'),('mathvision_adapter.py','adapter_sha256')]:
        assert r.sha(r.PROJECT/'PlaneGeometry/workbench'/name)==gate[key]
    assert r.sha(candidate/'plugin.json')==design['plugin_sha256']
    assert r.sha(r.OWN/summary['question_id']/'primary_math_proof.json')==design['proof_sha256']
    assert r.sha(r.PROJECT/'PlaneGeometry/workbench/quick_test.py')==summary['reference_quick_test_sha256']
    assert r.sha(directory/'request.json')==summary['request_body_sha256']
    assert (directory/'design_snapshot.json').read_bytes()==(candidate/'design.json').read_bytes()
    started=list(directory.glob('run_*_started.json'))
    assert len(started)==len(summary['results'])==2
    raw=[]
    for index,run in enumerate(summary['results'],1):
        assert run['status']=='completed' and run['finish_reason']=='stop' and run['http_status']==200 and not run['truncated']
        response=directory/f'run_{index:02d}_response.json'
        assert r.sha(response)==run['response_sha256']
        assert r.read(response)['choices'][0]['message']['content']==run['answer']
        assert r.read(candidate/f'eligibility_before_actual_request_{index:02d}.json')['eligible']
        raw.append({'run_id':run['run_id'],'raw_sha256':run['response_sha256'],'raw_path':str(response)})
        calls.append({'question_id':summary['question_id'],'variant_id':candidate.name,'run_id':run['run_id'],
                      'started_at':run['started_at'],'finished_at':run['finished_at'],'complete':True,
                      'request_body_sha256':summary['request_body_sha256'],'image_sha256':summary['image_sha256'],
                      'design_sha256':summary['design_sha256'],'response_sha256':run['response_sha256']})
    report=r.read(candidate/'manual_final_review.json')
    assert all(x.get('complete_response_read_in_full',x.get('complete_response_manually_read_in_full')) for x in report['responses'])
    invocations.append({'question_id':summary['question_id'],'variant_id':candidate.name,
        'frozen_preset':design['expected_wrong_answer'],
        'final_values':[x['final_value_degrees'] for x in report['responses']],
        'two_hits':report.get('two_complete_preset_hits',report.get('two_complete_hits')),'summary_path':str(summary_file),'raw':raw})
    pid_files.append(candidate/'api_process_started.json')
assert len(calls)==len({x['run_id'] for x in calls})==8
assert not list(r.OWN.glob('Plane*/*/tests/*/run_03*'))
assert not (r.OWN/'api_failure_stop.json').exists()
r.save(r.OWN/'complete_call_ledger.json',{'created_at':r.now(),'new_actual_calls':len(calls),
    'new_complete_responses':len(calls),'invocations':invocations,'calls':calls,
    'historical_calls_not_counted_as_new':8,'new_control_calls':0,'new_third_calls':0,
    'new_API_errors':0,'new_aborts':0,'preset_relabeling':0,'retried_failed_or_aborted_frozen_PNGs':0},new=True)

# This read-only process query starts no API, server or persistent child process.
query="Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^python(w)?\\.exe$' -and $_.CommandLine -like '*u04_angles*' } | Select-Object ProcessId,ParentProcessId,Name,CommandLine | ConvertTo-Json -Depth 3 -Compress"
process=subprocess.run(['powershell','-NoProfile','-Command',query],capture_output=True,text=True,
                       encoding='utf-8',errors='replace',check=True,
                       creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
data=r.json.loads(process.stdout) if process.stdout.strip() else []
if isinstance(data,dict): data=[data]
others=[x for x in data if x['ProcessId']!=os.getpid()]
api_pids=[r.read(p)['pid'] for p in pid_files]
assert not others,others
r.save(r.OWN/'process_closure_audit.json',{'created_at':r.now(),'own_API_PIDs':api_pids,
    'each_API_wrapper_finished_file':[str(p.with_name('api_process_finished.json')) for p in pid_files],
    'all_API_and_render_exec_commands_returned_exit0':True,
    'OS_query':'Read-only Win32_Process scan of python executables whose command contains own unit path',
    'own_python_processes_other_than_this_finalizer':others,
    'remaining_API_or_render_processes':0,'finalizer_pid':os.getpid(),
    'finalizer':'Synchronous artifact finalization only; exits after saving checkpoint/report.',
    'servers_started':0,'subagents_started':0,'worktrees_started':0,
    'other_units_or_old_general_exploration_processes_touched':False},new=True)

queue=r.read(r.OWN/'second_review_queue.json')
assert len(queue)==1 and queue[0]['question_id']=='Plane321'
queue[0]['exact_math_support_path']=str(r.OWN/'Plane321/exact_mathematical_checks.json')
queue[0]['source_preservation_path']=str(r.OWN/'readonly_preservation_final.json')
queue[0]['complete_call_ledger_path']=str(r.OWN/'complete_call_ledger.json')
r.save(r.OWN/'second_review_queue.json',queue)
checkpoint=r.read(r.OWN/'checkpoint.json')
checkpoint['questions']['Plane321'].update(status='PRIMARY_only_pending_fresh_independent_second_review',new_actual_calls=2)
checkpoint['questions']['Plane490'].update(status='UNRESOLVED_no_qualifying_PRIMARY',new_actual_calls=6,
    failed_variants=[x['variant'] for x in assessment['tested_distinct_hypotheses']],
    unfinished_reason=assessment['why_research_stops_here'],
    unresolved_assessment_path=str(r.OWN/'Plane490/unresolved_assessment.json'))
checkpoint.update(updated_at=r.now(),status='research_stopped_with_one_PRIMARY_and_one_unresolved_question',
    new_actual_calls=8,new_completed_responses=8,primary_candidate_count=1,API_errors=0,aborts=0,
    unworked_question_ids=[],unresolved_question_ids=['Plane490'],holds=[],skips=[],formal_actions=0,
    independent_second_review=False,delivery_performed=False,
    process_closure_audit=str(r.OWN/'process_closure_audit.json'),
    source_preservation_audit=str(r.OWN/'readonly_preservation_final.json'),
    complete_call_ledger=str(r.OWN/'complete_call_ledger.json'),
    diagnostics=[str(r.OWN/'offline_error_01.json'),str(r.OWN/'Plane490/a03_true_corresponding_notch_right_angles/semantic_crop_diagnostic.json')],
    limitations=['Plane321 only PRIMARY; parent must create a fresh independent second review.',
                 'Plane490 no qualifying PRIMARY despite three distinct legal correspondence hypotheses; no universal impossibility claimed.',
                 'No third call, retry, after-the-fact preset change, user Pass/Collect or delivery.'])
r.save(r.OWN/'checkpoint.json',checkpoint)
report={'unit_id':'u04_angles','assigned':['Plane321','Plane490'],
    'primary_candidates':[{'question_id':'Plane321','variant_id':'a01_pivot_legs_vs_true_bases',
                          'original':'E=300 degrees','frozen_wrong':'B=120 degrees','two_complete_finals':['B=120','B=120'],
                          'candidate_directory':str(r.OWN/'Plane321/a01_pivot_legs_vs_true_bases')}],
    'unresolved':[assessment],'new_actual_API_calls':8,'completed':8,'API_errors':0,'aborts':0,
    'unworked':[],'formal_actions':0,'independent_second_review_performed':False,'delivery_performed':False,
    'second_review_queue':str(r.OWN/'second_review_queue.json'),'checkpoint':str(r.OWN/'checkpoint.json'),
    'source_preservation':str(r.OWN/'readonly_preservation_final.json'),
    'call_ledger':str(r.OWN/'complete_call_ledger.json'),'process_closure':str(r.OWN/'process_closure_audit.json')}
r.save(r.OWN/'primary_research_report.json',report,new=True)
manifest={str(p.relative_to(r.OWN)):r.sha(p) for p in r.OWN.rglob('*') if p.is_file() and not p.is_relative_to(r.OWN/'ownruntime') and p.name!='artifact_sha256.json'}
r.save(r.OWN/'artifact_sha256.json',{'created_at':r.now(),'files':manifest,'runtime_cache_excluded':True},new=True)
print(r.json.dumps({'primary':['Plane321'],'unresolved':['Plane490'],'new_actual_calls':8,
    'completed':8,'all_protected_sources_unchanged':not drift,'remaining_own_API_or_render_processes':0,
    'queue':str(r.OWN/'second_review_queue.json'),'report':str(r.OWN/'primary_research_report.json')},ensure_ascii=False))
