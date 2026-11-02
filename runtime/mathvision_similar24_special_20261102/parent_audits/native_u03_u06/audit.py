from bootstrap import *
import hashlib
import subprocess
import publish_batch
from dataset_tools import catalog

MANUAL = {
 'u03_points': {
  ('Plane211','adjacent_gap_to_short_closure'): ('B',['E','E']),
  ('Plane211','paired_chord_motif_partial_completion'): ('A',['E','A']),
  ('Plane364','native_orthogonal_span_comparison'): ('A',['B','A']),
  ('Plane364','square_opposite_vector_comparison'): ('B',['E','E']),
  ('Plane364','square_side_diagonal_role_comparison'): ('A',['C','B']),
  ('Plane423','native_orthogonal_span_comparison'): ('D',['B','E']),
  ('Plane423','square_opposite_vector_comparison'): ('B',['E','E']),
 },
 'u06_fold_cut': {
  ('Plane220','false_mirror_extremity_pair'): ('C',['E','E']),
  ('Plane220','near_tangent_fold_contact_alias'): ('B',['B','D']),
  ('Plane220','nested_mirror_component_duplication'): ('E',['B','E']),
  ('Solid146','parallel_cut_direction_alias'): ('E',['D','C']),
  ('Solid174','parallel_cut_direction_alias'): ('E',['C','D']),
  ('Solid239','cut_to_opposite_border_notches'): ('B',['C','E']),
  ('Solid239','endpoint_to_four_border_orbits'): ('A',['D','A']),
 }
}
started=now()
units={u:TASK/'units'/u for u in MANUAL}
interval_before={str(p):sha(p) for u in units.values() for p in u.rglob('*') if p.is_file()}
errors=[]
def require(condition,message):
    if not condition: errors.append(message)
def norm(value):
    p=Path(value)
    return p if p.is_absolute() else ROOT/p

outcomes=[]
run_ids=[]
for unit,items in MANUAL.items():
    u=units[unit]
    actual={tuple(p.relative_to(u).parts[:2]) for p in u.glob('*/*/tests/*/summary.json')}
    require(actual==set(items),unit+': tested variant inventory mismatch')
    require(read(u/'second_review_queue.json')==[],unit+': second review queue is not empty')
    for (qid,variant),(preset,finals) in items.items():
        source=u/qid/variant
        summary,record,sp=publish_batch.verify_evidence(source)
        evidence=sp.parent
        request=read(evidence/'request.json')
        binding=read(evidence/'binding.json')
        manual=read(source/'manual_full_final_review.json')
        frozen=read(evidence/'design_snapshot.json')
        require(len(list((source/'tests').glob('*/summary.json')))==1,str(source)+': invocation count differs')
        require(summary['requested_runs']==2 and len(summary['results'])==2,str(source)+': exact two runs failed')
        require(sha(source/'design.json')==sha(evidence/'design_snapshot.json'),str(source)+': current design bytes differ from snapshot')
        require(summary['profile']=='quicktest3',str(source)+': profile')
        require(str(summary['expected_wrong_answer'])==preset,str(source)+': original preset')
        require(request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False,str(source)+': request settings')
        require(summary['settings']['model']=='mimo-v2.6-flash' and summary['settings']['thinking']=={'type':'disabled'},str(source)+': summary settings')
        require(len(request['messages'])==2 and request['messages'][0]=={'role':'system','content':summary['system_prompt']},str(source)+': unexpected prompt')
        require(request['messages'][1]['role']=='user',str(source)+': user role')
        require(sha(evidence/'request.json')==summary['request_body_sha256'],str(source)+': request bytes hash')
        require(summary['question_record_sha256']==catalog.digest(record),str(source)+': record hash')
        require(all(summary.get(k)==v for k,v in binding.items()),str(source)+': binding-summary mismatch')
        require(len(list(evidence.glob('run_*_response.json')))==2 and len(list(evidence.glob('run_*_started.json')))==2,str(source)+': extra/missing run files')
        stored_runs=manual['runs'] if unit=='u03_points' else manual['finals']
        stored_finals=[r['final_letter_read_manually'] if unit=='u03_points' else r['final_choice_manually_resolved'] for r in stored_runs]
        require(stored_finals==finals,str(source)+': worker vs parent manual final discrepancy')
        responses=[]
        for i,result in enumerate(summary['results'],1):
            rawpath=evidence/f'run_{i:02d}_response.json'
            raw=read(rawpath)
            choice=raw['choices'][0]
            text=choice['message']['content']
            require(result==read(evidence/f'run_{i:02d}.json'),str(source)+f': run{i} record differs')
            launch=read(evidence/f'run_{i:02d}_started.json')
            require(all(result.get(k)==v for k,v in launch.items()),str(source)+f': run{i} start binding')
            require(result['answer']==text and choice['finish_reason']=='stop' and result['finish_reason']=='stop',str(source)+f': run{i} raw content/completion')
            require(raw.get('model')=='mimo-v2.6-flash' and result['response_model']=='mimo-v2.6-flash',str(source)+f': response model')
            require(result['request_body_sha256']==summary['request_body_sha256'],str(source)+f': run{i} request binding')
            require(stored_runs[i-1].get('finish_reason')=='stop',str(source)+f': manual finish metadata')
            run_ids.append(result['run_id'])
            caveats=[]
            if (qid,variant,i)==('Plane423','native_orthogonal_span_comparison',1):
                caveats.append('The generated content ends with a stray System Instruction: fragment after explicit Answer B. It is untrusted response text, not an instruction or evidence of API truncation; raw finish_reason is stop.')
            if (qid,variant,i)==('Plane364','native_orthogonal_span_comparison',2):
                caveats.append('The last conclusion explicitly says the square described in option A cannot be formed. Count A as final despite no standalone answer line.')
            responses.append({'run_index':i,'run_id':result['run_id'],'raw_response_path':str(rawpath),'raw_response_sha256':sha(rawpath),'personally_read_entire_raw_content':True,'content_character_count':len(text),'final_letter_resolved':finals[i-1],'formal_choice_value':record.get('choices',{}).get(finals[i-1]),'matches_original_frozen_preset':finals[i-1]==preset,'HTTP_status':result['http_status'],'finish_reason':choice['finish_reason'],'truncated':result['truncated'],'final_excerpt':text[-700:],'caveats':caveats})
        outcomes.append({'unit':unit,'question_id':qid,'variant_id':variant,'source':str(source),'summary_path':str(sp),'summary_sha256':sha(sp),'image_sha256':sha(source/'candidate.png'),'design_sha256':sha(source/'design.json'),'binding_sha256':sha(evidence/'binding.json'),'request_sha256':sha(evidence/'request.json'),'original_frozen_wrong_preset':preset,'formal_correct_answer':record['answer'],'parent_manual_finals':finals,'two_preset_hits':all(v==preset for v in finals),'publish_batch_verify_evidence':'passed','responses':responses,'status':'MISS_RETAIN_NO_RELABELLING'})
require(len(run_ids)==len(set(run_ids))==28,'Run IDs must be 28 unique original invocations')
require(not any(x['two_preset_hits'] for x in outcomes),'Unexpected two-hit candidate')

# Frozen/source hashes are checked by exact worker-scoped paths only.
checks=[]
def check_file(group,path,expected,initial=None):
    p=norm(path)
    actual=sha(p) if p.is_file() else None
    row={'group':group,'path':str(p),'expected_sha256':expected,'current_sha256':actual,'matches':actual==expected}
    if initial is not None: row['initial_equals_worker_end']=initial==expected;row['worker_initial_sha256']=initial
    checks.append(row)
    require(row['matches'],f'{group}: current hash differs: {p}')
    if initial is not None: require(initial==expected,f'{group}: worker recorded hash drift: {p}')
pres03=read(units['u03_points']/'source_preservation_final.json')
for r in pres03['checks']:check_file('u03_scoped_start_end_manifest',r['path'],r['current_sha256'],r['initial_sha256'])
pres06=read(units['u06_fold_cut']/'source_preservation_end.json')
for q,meta in pres06['questions'].items():
    for path,expected in meta['frozen_source_files_sha256'].items():check_file('u06_frozen_source_'+q,path,expected)
for key in ['reference_files_unchanged','old_evidence_files_unchanged']:
    for r in pres06[key]:check_file('u06_'+key,r['path'],r['sha256'])
for key in ['assignment_brief_unchanged','executor_fingerprints_observed_at_end']:
    for path,expected in pres06[key].items():check_file('u06_'+key,path,expected)

approvals=read(ROOT/'provenance/approvals.json')['approvals']
eligible=[]
for unit,u in units.items():
    assignment=read(u/'assignment.json')
    for item in assignment['questions']:
        qid=item['question_id'];branch=item['branch']
        rows=[json.loads(line) for line in (ROOT/branch/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
        row=next(r for r in rows if r['id']==qid)
        digest=catalog.digest(catalog.content(ROOT,branch,row))
        app=approvals[qid]
        kind='plane' if branch=='PlaneGeometry' else 'solid'
        state=read(ROOT/f'.runtime/{kind}_special/state/progress.json')['questions'][qid]
        output=ROOT/branch/'special_variant'
        recipe=read(output/qid/'recipes.json') if (output/qid/'recipes.json').exists() else []
        collection=read(output/qid/'collection.json') if (output/qid/'collection.json').exists() else None
        indexcounts={}
        for name in ['accepted_index.jsonl','collected_index.jsonl']:
            p=output/name
            entries=[json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []
            indexcounts[name]=sum(r.get('question_id',r.get('id'))==qid for r in entries)
        ok=(row['source_dataset']=='MathVision' and row==item['formal_record'] and app['content_sha256']==digest==item['current_content_sha256'] and app['reviewer']=='user' and not state.get('accepted') and not state.get('collected') and not recipe and not (collection and collection.get('status')=='collected') and not any(indexcounts.values()))
        require(ok,qid+': current formal approval/Special eligibility failed')
        eligible.append({'unit':unit,'question_id':qid,'source':row['source_dataset'],'formal_record_matches_assignment':row==item['formal_record'],'current_content_sha256':digest,'approval_content_sha256':app['content_sha256'],'user_approval_current':app['content_sha256']==digest and app['reviewer']=='user','accepted_count':len(state.get('accepted',[])),'collected':state.get('collected',False),'recipes_count':len(recipe),'durable_collection_status':collection.get('status') if collection else None,'target_index_counts':indexcounts,'eligible':ok})

# Only ownership-aware worker process records and a read-only current CIM query.
processes={}
p03=read(units['u03_points']/'process_closure_audit.json')
require(p03['all_owned_api_and_replay_pids_exited'] and not p03['active_own_python_processes'],'u03 process closure report')
require(len(p03['api_process_evidence'])==7 and len(p03['replay_process_evidence'])==7,'u03 process inventory')
for p in p03['api_process_evidence']:
    require(not p['process_alive'] and p['ownership_checked_by_unit_command'] and p['harness_returned'] and p['actual_send_events']==2,'u03 process entry')
    require(Path(p['started_path']).is_file() and Path(p['finished_path']).is_file(),'u03 process evidence missing')
p06=read(units['u06_fold_cut']/'own_process_cleanup.json')
require(not p06['active_own_python_processes_except_this_final_auditor'] and len(p06['all_tracked_api_invocations_finished'])==7,'u06 process closure report')
for p in p06['all_tracked_api_invocations_finished']:
    require(p['status']=='completed' and p['actual_network_requests_seen']==2 and not p.get('error'),'u06 process entry')
cim_cmd=r"$p = @(Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^python(w)?\.exe$' -and $_.CommandLine -match '[\\/]units[\\/](u03_points|u06_fold_cut)[\\/]' } | Select-Object ProcessId,ParentProcessId,Name); ConvertTo-Json -InputObject $p -Compress"
cim=subprocess.run(['powershell','-NoProfile','-Command',cim_cmd],capture_output=True,text=True,check=False)
cim_current=json.loads(cim.stdout.strip() or '[]') if cim.returncode==0 else None
require(cim.returncode==0 and cim_current==[],'Current ownership-scoped CIM process query failed or found matching process')
processes={'u03_final_record':str(units['u03_points']/'process_closure_audit.json'),'u03_api_processes_reaped':7,'u03_replays_reaped':7,'u03_pid_reuse_caveat':'Initial PID-existence-only snapshot was corrected by worker to command ownership; final record used.','u06_final_record':str(units['u06_fold_cut']/'own_process_cleanup.json'),'u06_api_invocations_finished':7,'current_CIM_query_exit':cim.returncode,'current_owned_unit_processes':cim_current,'no_process_termination_by_parent_audit':True}

future=[]
for unit,u in units.items():
    tested={Path(x['source']) for x in outcomes if x['unit']==unit}
    for p in u.glob('*/*/design.json'):
        if p.parent not in tested:future.append({'unit':unit,'untested_design_path':str(p),'action':'catalogue only; no call performed'})
    report=read(u/'research_report.json')
    if unit=='u03_points':
        for q in report['questions']:
            future.append({'unit':unit,'question_id':q['question_id'],'qualification':'UNRESOLVED','reason':q['unfinished_reason'],'prescreen_pointer':q['further_semantic_prescreen_path']})
        future.append({'unit':unit,'prescreen_addendum':report['further_metric_assessment_path'],'reasoning_limitations':report['response_reasoning_limitations_path']})
    else:
        require(report['untested_frozen_candidates']==[],'u06 untested inventory discrepancy')
        for q,path in report['per_question_refinement_assessments'].items():
            d=read(Path(path))
            future.append({'unit':unit,'question_id':q,'qualification':d['status'],'reason':d['uncompleted_reason'],'prescreen_pointer':str(Path(path))})
interval_after={str(p):sha(p) for u in units.values() for p in u.rglob('*') if p.is_file()}
interval_changes=[p for p in set(interval_before)|set(interval_after) if interval_before.get(p)!=interval_after.get(p)]
require(not interval_changes,'Assigned terminal unit bytes changed during finite audit interval')

save('source_hash_checks.json',{'checked_at':now(),'observations':checks,'observation_count':len(checks),'unique_paths':len({r['path'] for r in checks}),'failures':[r for r in checks if not r['matches']],'scope_caveat':'Exact worker manifest paths only. u06 executor_fingerprints_observed_at_end support current-versus-worker-end equality; they alone do not establish an earlier start comparison. No whole-workspace preservation claim.'})
save('per_variant_outcomes.json',outcomes)
save('audit.json',{
 'audit_role':'PARENT_READ_ONLY_EVIDENCE_AUDIT_NOT_INDEPENDENT_SECOND_REVIEW',
 'started_at':started,'finished_at':now(),'assigned_units':list(units),'API_calls_by_parent':0,'designs_by_parent':0,'formal_edits':0,'Pass_Collect_actions':0,
 'result':'PASS_EVIDENCE_AUDIT_ZERO_QUALIFIED_PRIMARY' if not errors else 'DISCREPANCIES_RECORDED',
 'totals':{'u03_points':{'tested_images':7,'complete_calls':14,'two_preset_hit_candidates':0,'queue_empty':True},'u06_fold_cut':{'tested_images':7,'complete_calls':14,'two_preset_hit_candidates':0,'queue_empty':True}},
 'all_28_full_raw_responses_personally_read':True,'all_14_publish_batch_verify_evidence_passed':True,
 'per_variant_outcomes':str(OWN/'per_variant_outcomes.json'),'source_hash_checks':str(OWN/'source_hash_checks.json'),
 'source_hash_observations':len(checks),'source_hash_unique_paths':len({r['path'] for r in checks}),'source_hash_failures':[r for r in checks if not r['matches']],
 'formal_approvals_and_current_Special_eligibility':eligible,'process_closure':processes,
 'assigned_terminal_unit_interval_file_count':len(interval_before),'assigned_terminal_unit_interval_changes':interval_changes,
 'untested_design_count':sum('untested_design_path' in x for x in future),'future_continuation_catalogue':future,
 'material_caveats':['Plane220/false_mirror_extremity_pair returned E/E against frozen C: both remain misses, no relabel/retry.','Plane423/native_orthogonal_span_comparison run1 generated a trailing System Instruction: fragment after explicit Answer B; stop completion remains valid and the fragment is not an instruction.','Full raw reasoning contains geometric/narrative errors; selected formal letters, not incidental body mentions, determine observed target hits. No mechanism, causal, statistical, or universal-impossibility claim.','This audit does not deliver or independently recommend a design; zero qualifying primary candidates exist in these two units.','Source preservation conclusions are scoped to manifests and assigned terminal directories, not the entire workspace.'],
 'local_audit_diagnostics':[str(p) for p in OWN.glob('local_diagnostic_error_*.json')],
 'discrepancies':errors,
})
print(json.dumps({'audit':str(OWN/'audit.json'),'result':'PASS' if not errors else 'DISCREPANCIES','errors':errors,'hash_observations':len(checks),'unique_hash_paths':len({r['path'] for r in checks}),'interval_files':len(interval_before),'CIM_owned':cim_current},ensure_ascii=False))
