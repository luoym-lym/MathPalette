from tools34 import *
from make34 import SPECS,SKIPS
import base64
import subprocess

# Terminal values are manually transcribed after reading the COMPLETE raw contents.
MANUAL={
 'Plane257':[('B','One','Final B:One in both complete responses. Neither equals presetD:Three. Both narratives misread other flags; the old observedB is not promoted or relabeled.'),('B','One','Final B:One. Numerator transfer to flag1 did not occur in the final. No causal inference from this finite pair.')],
 'Solid184':[('67.5','67.5','Final67.5, not preset45. It incorrectly uses S=x+y+z instead of S=2(x+y+z).'),('54','54','Final54, the unique original answer. Correct sum5S=270; miss preset45.')],
 'Plane336':[('6','6','Final6, original correct. It mislocates the three white triangles at corners in its narrative, but terminal numeric value is6; not preset4.5.'),('6','6','The COMPLETE5796-token content was manually read, including many discarded conflicting region descriptions and intermediate values. The explicit terminal Answer is6. It is not preset4.5; incidental alternative computations are not final-answer evidence. Finish_reason is stop, not truncated.')],
 'Plane340':[('0.75','3/4','Final0.75(or3/4), not preset2. The coordinate setup and dividing-line reasoning are inconsistent, but final value is explicit.'),('1','1','Final1, original correct. Intermediate integration includes wrong partial-region bounds but terminal value remains1, not preset2.')]
}

def binding_audit(qid,spec):
    folder=UNIT/qid/spec['variant_id']
    invocations=list(folder.glob('tests/quicktest3_*'));assert len(invocations)==1
    invocation=invocations[0];binding=read(invocation/'binding.json');request=read(invocation/'request.json')
    design=read(folder/'design.json');snapshot=invocation/'design_snapshot.json'
    assert binding['requested_runs']==2 and binding['expected_wrong_answer']==spec['expected_wrong_answer']
    assert sha(folder/'candidate.png')==binding['image_sha256']==design['frozen_png_sha256']
    assert sha(folder/'design.json')==binding['design_sha256'] and snapshot.read_bytes()==(folder/'design.json').read_bytes()
    assert sha(invocation/'request.json')==binding['request_body_sha256']
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert set(request)=={'model','stream','thinking','messages'} and request['stream'] is False
    assert request['messages'][0]=={'role':'system','content':binding['system_prompt']}
    user=request['messages'][1];assert user['role']=='user' and len(user['content'])==2
    assert user['content'][0]=={'type':'text','text':record(qid)['question']}
    assert base64.b64decode(user['content'][1]['image_url']['url'].split(',',1)[1])==(folder/'candidate.png').read_bytes()
    assert canonical(record(qid))==binding['question_record_sha256']
    assert sha(folder/'plugin.json')==design['normalized_plugin_sha256']
    jobs=[];full_manual=[];aborts=[]
    for index in (1,2):
        started=read(invocation/f'run_{index:02d}_started.json')
        assert all(started[key]==binding[key] for key in ('request_body_sha256','image_sha256','design_sha256'))
        path=invocation/f'run_{index:02d}.json'
        if path.exists():
            job=read(path);assert job['status']=='completed'
            raw_path=invocation/f'run_{index:02d}_response.json';raw=read(raw_path)
            assert raw['choices'][0]['finish_reason']=='stop' and sha(raw_path)==job['response_sha256']
            assert all(job[key]==binding[key] for key in ('request_body_sha256','image_sha256','design_sha256'))
            assert index<=len(MANUAL[qid]),'Read and transcribe newly completed full final before finalizing.'
            value,meaning,observation=MANUAL[qid][index-1]
            full_manual.append({'run_index':index,'status':'completed','finish_reason':'stop','raw_response_path':str(raw_path),
                'raw_response_sha256':sha(raw_path),'run_record_sha256':sha(path),'complete_raw_content':raw['choices'][0]['message']['content'],
                'complete_content_and_terminal_value_manually_read':True,'manual_final':value,'manual_value':meaning,
                'matches_immutable_preset':value==spec['expected_wrong_answer'],'manual_observation':observation})
            jobs.append(job)
        else:
            abort=folder/'aborted_call.json'
            assert abort.exists(),'Running or incomplete call must finish or be safely aborted before checkpoint.'
            aborts.append(read(abort))
    manual={'question_id':qid,'variant_id':spec['variant_id'],'preset':spec['expected_wrong_answer'],'at':now(),
            'image_sha256':binding['image_sha256'],'design_sha256':binding['design_sha256'],'full_manual_finals':full_manual,
            'aborted_or_incomplete':aborts,'credible_two_hit':len(full_manual)==2 and all(x['matches_immutable_preset'] for x in full_manual),
            'preset_never_changed':True,'no_retry_or_larger_set_selection':True}
    assert not manual['credible_two_hit'],'A new primary possibility must be queued and trigger the three-case finite stop.'
    write(folder/'manual_final_review.json',manual)
    evidence_hashes={str(path.relative_to(PROJECT)):sha(path) for path in folder.rglob('*') if path.is_file()}
    audited={'question_id':qid,'variant_id':spec['variant_id'],'at':now(),'checks':{
       'exactly_two_actual_calls_started':True,'same_frozen_png_request_design_both_calls':True,'preset_and_design_snapshot_immutable':True,
       'raw_request_contains_only_original_formal_question_and_candidate_png':True,'exact_unmodified_reference_system_prompt':True,
       'exact_quicktest3_model_thinking':True,'no_profile_max_tokens_localtimeout_override':True,'raw_complete_response_hashes_match':True,
       'formal_record_current_matches_binding':True,'full_manual_terminal_finals_read':True},
       'completed_calls':len(full_manual),'aborted_calls':len(aborts),'completed_pair':len(full_manual)==2,'manual_finals':[x['manual_final'] for x in full_manual],
       'credible_two_hit':False,'binding_path':str(invocation/'binding.json'),'binding_sha256':sha(invocation/'binding.json'),
       'request_path':str(invocation/'request.json'),'request_sha256':sha(invocation/'request.json'),
       'summary_path':str(invocation/'summary.json') if (invocation/'summary.json').exists() else None,
       'manual_final_review_path':str(folder/'manual_final_review.json'),'all_candidate_evidence_files':evidence_hashes}
    write(folder/'evidence_binding_audit.json',audited)
    return {'question_id':qid,'variant_id':spec['variant_id'],'stage':'material_refinement','preset':spec['expected_wrong_answer'],
            'correct_answer':record(qid)['answer'],'complete_manual_finals':[x['manual_final'] for x in full_manual],
            'completed_calls':len(full_manual),'aborted_calls':len(aborts),'status':'paired_preset_miss' if len(full_manual)==2 else 'incomplete_pair_aborted_no_retry',
            'credible_two_hit':False,'difference':spec['old_new_difference'],'new_information_correspondence':spec['mechanism'],
            'candidate_root':str(folder),'immutable_evidence_binding':audited,
            'math_audit':str(UNIT/qid/'primary_math_audit.json'),'per_marker_native_semantic_review':str(folder/'primary_pretest_review.json'),
            'frozen_design':str(folder/'design.json'),'frozen_plugin':str(folder/'plugin.json'),'frozen_png':str(folder/'candidate.png'),
            'full_manual_final_review':str(folder/'manual_final_review.json'),'controls':{'new_calls':0,'existing_invocations_found':[],'limitation':'No original control comparison, no incremental effect established.'},
            'approval_status':'No self approval or delivery. NEW parent independent review required if any future candidate is eventually considered.'}

if __name__=='__main__':
    # A process list from PowerShell is also retained for exact PID/command verification.
    command="Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^python' -and $_.CommandLine -match 'background_34[\\/]run34.py' } | Select-Object ProcessId,Name,CommandLine | ConvertTo-Json -Depth 3"
    observed=subprocess.run(['powershell','-NoProfile','-Command',command],capture_output=True,text=True,encoding='utf-8',check=True)
    assert not observed.stdout.strip(),'Own API process remains active; do not finalize.'
    write(UNIT/'own_api_processes_closed.json',{'at':now(),'process_query':command,'matching_own_run34_processes':[],
          'exit_code':observed.returncode,'raw_stdout':observed.stdout,'raw_stderr':observed.stderr,'all_own_api_processes_closed':True})
    attempts=[binding_audit(qid,spec) for qid,spec in SPECS.items()]
    source_audits={};old_hashes=read(UNIT/'prior_evidence_hashes_start.json')
    old_changes=[{'path':path,'old':digest,'now':sha(PROJECT/path) if (PROJECT/path).exists() else None} for path,digest in old_hashes.items() if not (PROJECT/path).exists() or sha(PROJECT/path)!=digest]
    assert not old_changes
    for qid in IDS:
        check=eligibility(qid);assert check['eligible']
        end=source_files(qid);start=read(UNIT/qid/'source_fingerprints_start.json');changes=[p for p,v in start.items() if end.get(p)!=v]
        assert not changes
        source_audits[qid]={'at':now(),'current_eligibility':check,'relevant_source_files_unchanged':True,'changed_paths':changes,
                           'current_source_files':end,'record_sha256_unchanged':canonical(record(qid))==read(UNIT/qid/'eligibility_start.json')['record_sha256']}
        write(UNIT/qid/'source_and_eligibility_final.json',source_audits[qid])
    progress_start=read(UNIT/'mutable_progress_hashes_start.json')['hashes'];progress_final={name:sha(SHARED/name) for name in progress_start}
    progress_drift={name:{'historical_at_unit_start':v,'current':progress_final[name]} for name,v in progress_start.items() if progress_final[name]!=v}
    preservation={'at':now(),'all_own_file_writes_only_below':str(UNIT),'strict_audit_write_guard_before_project_imports':True,
        'runtime_isolation':ISOLATION,'all_relevant_formal_source_approval_fingerprints_unchanged':True,
        'all_read_prior_evidence_hashes_preserved':True,'old_evidence_changed':old_changes,'old_files_checked':len(old_hashes),
        'mutable_progress_classification':'Diagnostic runtime metadata; current eligibility is separately established from authoritative formal/approval/Special records. No historical hash rewritten.',
        'progress_start':progress_start,'progress_final':progress_final,'mutable_progress_drift':progress_drift,
        'unrelated_concurrent_workbench_edits_preserved':True,'whole_workspace_unchanged_claim':False,
        'formal_approval_Pass_Collect_publication_APIs_called':False,'env_git_dotruntime_writes':False,
        'source_eligibility_audits':{qid:str(UNIT/qid/'source_and_eligibility_final.json') for qid in IDS}}
    write(UNIT/'source_preservation_classification_final.json',preservation)
    assessments=[]
    for qid in IDS:
        if qid in SKIPS:
            assessments.append({'question_id':qid,**SKIPS[qid],'primary_math':str(UNIT/qid/('primary_math_audit_corrected.json' if qid=='Plane338' else 'primary_math_audit.json')),'prescreen_path':str(UNIT/qid/'refinement_prescreen.json')})
        else:
            spec=SPECS[qid]
            assessments.append({'question_id':qid,'decision':'new_material_design_completed_or_aborted_without_retry',
                'variant_id':spec['variant_id'],'old_new_difference':spec['old_new_difference'],'hypothesis':spec['mechanism'],
                'additional_reasonable_hypotheses_exhausted':{
                   'Plane257':'No extra attempt targeting old observedB. Flag3 piece-count would require exposing its black interior midline as an extra counted division; flag5 repeats the old failed unequal-unit mechanism. No new legal mechanism retained.',
                   'Plane336':'Additional rhombus/white triangle outline pairing repeats earlier unsupported equal-region counting; adding area-subdivision lines either supports the correct answer or adds partitions. No second retained design.',
                   'Plane340':'A half-square treatment of both shaded frames gives the already correct1, so it is not a distinct wrong-target hypothesis. Recoloring the same frames to chase0.75 would be output-driven cosmetics and is excluded.',
                   'Solid184':'Contact-seam emphasis alone has no useful source receiver; adding ghost/internal faces changes frozen visibility. The observed67.5 cannot be a new preset without a new geometry-based hypothesis. No extra design retained.'}[qid]})
    queue={'stage':'material_refinement','unit':'background_34','at':now(),'candidates':[],
           'credible_primary_possibilities':0,'note':'No new candidate achieved its own immutable preset twice. No old independently rejected/held variant is promoted. Parent must launch a NEW independent review for every eventual delivery.'}
    write(UNIT/'second_review_queue.json',queue)
    completed=sum(a['completed_calls'] for a in attempts);aborted=sum(a['aborted_calls'] for a in attempts)
    checkpoint={'stage':'material_refinement','unit':'background_34','status':'completed','finished_at':now(),
        'assigned_question_ids':IDS,'actual_assessed_question_ids':IDS,'assessed_question_ids':IDS,'unworked_question_ids':[],
        'question_count':8,'new_design_count':4,'screened_without_new_calls':4,'actual_candidate_calls_started':8,
        'completed_calls':completed,'aborted_calls':aborted,'api_errors':0,'automatic_retries':0,
        'complete_candidate_pairs':sum(a['completed_calls']==2 for a in attempts),'credible_primary_possibilities':0,
        'new_control_calls':0,'stop_reason':'All8 assigned questions assessed; reasonable substantive hypotheses exhausted. All8 actual calls completed normally; no external failure, abort or retry.',
        'assessments':assessments,'attempts':attempts,'second_review_queue':str(UNIT/'second_review_queue.json'),
        'history_inventory':str(UNIT/'history_inventory.json'),'prior_full_history_and_raw_binding_audit':str(UNIT/'history_read_and_binding_audit.json'),
        'delivered12_exclusion_and_readonly_references':str(UNIT/'delivered_reference_and_exclusion_audit.json'),
        'source_preservation':preservation,'failures_or_aborts':[read(UNIT/a['question_id']/a['variant_id']/'aborted_call.json') for a in attempts if a['aborted_calls']],
        'draft_mathematical_erratum':str(UNIT/'Plane338/primary_math_erratum_pretest.json'),
        'dependency_historical_comparison':str(UNIT/'rendering_dependency_historical_comparison.json'),
        'process_closure':str(UNIT/'own_api_processes_closed.json'),'nested_agents_threads_worktrees':0,
        'limits':['Primary math/native-visual/marker assessments are author reviews, not independent second review or human studies.',
                  'No controls run; neither incremental effect nor causal or statistical gain is established.',
                  'All old observed wrong values remain misses to their own original presets; none relabeled.',
                  'Every eventual delivery requires NEW parent independent review. No approvals, Pass, Collect or publication performed.']}
    write(UNIT/'checkpoint.json',checkpoint)
    print(json.dumps({'stage':'material_refinement','assessed':8,'new_designs':4,'calls_started':8,'calls_completed':completed,'calls_aborted':aborted,
                      'complete_pairs':checkpoint['complete_candidate_pairs'],'credible_possibilities':0,'queue':str(UNIT/'second_review_queue.json'),'checkpoint':str(UNIT/'checkpoint.json')},ensure_ascii=False))
