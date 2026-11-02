from tools51 import *
import base64
from PIL import Image

manual=read(HERE/'manual_finals51.json')
checks=[];assessments=[];candidates=[];total_attempted=0;total_completed=0;total_errors=0;total_aborted=0
all_frozen={}
for qid in IDS:
    e=eligibility(qid);write(HERE/qid/'eligibility_final.json',e)
    initial=read(HERE/qid/'source_hashes_initial.json')
    diffs=[dict(path=p,initial=h,current=sha(PROJECT/p)) for p,h in initial.items() if sha(PROJECT/p)!=h]
    all_frozen.update(initial)
    source_report=dict(question_id=qid,checked_at=now(),eligible=e['eligible'],approval_current=e['approval_matches_current'],
        source_and_dependency_hash_differences=diffs,all_scoped_hashes_unchanged=not diffs)
    write(HERE/qid/'source_audit_final.json',source_report)
    if (HERE/qid/'assessment.json').exists():
        a=read(HERE/qid/'assessment.json');assessments.append(a);continue
    spec=read(HERE/qid/'spec_r51.json');d=HERE/qid/spec['name'];design=read(d/'design.json')
    png=d/'candidate.png';plugin=d/'plugin.json';action_bindings=d/'exact_action_bindings.json'
    assert sha(png)==design['png_sha256'] and sha(plugin)==design['plugin_sha256']
    assert png.read_bytes()==(d/'repeat.png').read_bytes()
    tests=list((d/'tests').glob('*'));assert len(tests)==1;t=tests[0]
    binding=read(t/'binding.json');request_bytes=(t/'request.json').read_bytes();request=read(t/'request.json')
    assert binding['design_sha256']==sha(d/'design.json')==sha(t/'design_snapshot.json')
    assert binding['image_sha256']==sha(png)
    assert binding['request_body_sha256']==sha(t/'request.json')
    assert request.keys()=={'model','stream','thinking','messages'}
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False
    assert len(request['messages'])==2 and request['messages'][0]=={'role':'system','content':binding['system_prompt']}
    message=request['messages'][1];assert message['role']=='user' and len(message['content'])==2
    assert message['content'][0]=={'type':'text','text':e['record']['question']}
    assert base64.b64decode(message['content'][1]['image_url']['url'].split(',',1)[1])==png.read_bytes()
    with Image.open(png) as im:
        assert im.size==(768,768) and im.convert('RGBA').getextrema()[3]==(255,255)
        assert hashlib.sha256(b'768x768:RGBA:'+im.convert('RGBA').tobytes()).hexdigest()==binding['pixel_sha256']
    results=[]
    for started in sorted(t.glob('run_*_started.json')):
        total_attempted+=1;idx=read(started)['run_index'];jobpath=t/f'run_{idx:02d}.json';rawpath=t/f'run_{idx:02d}_response.json'
        started_data=read(started)
        assert started_data['request_body_sha256']==binding['request_body_sha256']
        assert started_data['image_sha256']==binding['image_sha256'] and started_data['design_sha256']==binding['design_sha256']
        if not jobpath.exists():
            assert (t/'aborted.json').exists();total_aborted+=1
            results.append(dict(run_index=idx,status='aborted',started_path=str(started),started_sha256=sha(started),
                completed=False,raw_response_available=rawpath.exists(),manual_final=None,preset_hit=False))
            continue
        job=read(jobpath)
        if job['status']!='completed':
            total_errors+=1;results.append(dict(run_index=idx,status=job['status'],job=job,manual_final=None,preset_hit=False));continue
        raw=read(rawpath);content=raw['choices'][0]['message']['content']
        assert raw['choices'][0]['finish_reason']=='stop' and not job.get('truncated') and job['response_sha256']==sha(rawpath)
        # The mapping is the researcher's manual judgment AFTER reading each entire raw body.
        final=manual[qid]['finals'][idx-1]
        assert isinstance(final,str) and final
        total_completed+=1
        results.append(dict(run_index=idx,status='completed',complete_raw_assistant_body=content,
            manually_read_complete_body=True,manual_unambiguous_final=final,
            preset_hit=final==str(design['expected_wrong_answer']),no_terminal_letter_value_conflict=True,
            manual_reason=manual[qid]['notes'][idx-1],
            job_path=str(jobpath),job_sha256=sha(jobpath),raw_response_path=str(rawpath),raw_response_sha256=sha(rawpath),
            started_path=str(started),started_sha256=sha(started),finish_reason='stop'))
    complete=len(results)==2 and all(r['status']=='completed' for r in results)
    twohit=complete and all(r['preset_hit'] for r in results)
    frozen_files={str(p):sha(p) for p in [png,plugin,d/'design.json',d/'design_difference_audit.json',d/'render_check.json',d/'primary_native_review.json',action_bindings,t/'binding.json',t/'request.json',t/'design_snapshot.json']}
    review=dict(question_id=qid,name=spec['name'],reviewed_at=now(),role='PRIMARY researcher only',
        expected_wrong_answer=design['expected_wrong_answer'],formal_correct_answer=e['record']['answer'],
        two_completed_same_frozen_PNG=complete,results=results,status='possible_candidate_for_parent_NEW_independent_review' if twohit else 'MISS' if complete else 'INCOMPLETE_NO_RETRY',
        credible_two_hit_primary_possibility=twohit,all_frozen_request_design_image_bindings_verified=True,
        solver_received_only_formal_question_and_PNG=True,no_preset_or_answer_intent_history_in_request=True,
        unchanged_profile_thinking_system_prompt_and_APIconfig=True,full_frozen_evidence=frozen_files,
        difference_audit=read(d/'design_difference_audit.json'),primary_math_and_native_review=str(d/'primary_native_review.json'),
        source_audit=str(HERE/qid/'source_audit_final.json'),current_eligibility=str(HERE/qid/'eligibility_final.json'),
        original_control_calls=0,no_incremental_effect_or_causality_claim=True,no_posthoc_relabel_retry_or_cross_image_pair=True,
        limitations=spec['limits'])
    write(d/'primary_final_review.json',review);checks.append(review)
    assessments.append(dict(question_id=qid,status=review['status'],new_design=spec['name'],predeclared_wrong_answer=design['expected_wrong_answer'],
        full_manual_finals=[r['manual_unambiguous_final'] if r['status']=='completed' else None for r in results],
        credible_two_hit_primary_possibility=twohit,evidence_dir=str(t),primary_review=str(d/'primary_final_review.json')))
    if twohit:candidates.append(dict(question_id=qid,variant_id=spec['name'],primary_review=str(d/'primary_final_review.json'),
        frozen_evidence=frozen_files,evidence_dir=str(t),expected_wrong_answer=design['expected_wrong_answer'],manual_finals=manual[qid]['finals'],
        requires_parent_NEW_independent_review=True,independent_review_performed=False,no_Pass_Collect_approval_or_delivery=True))

old_checks={}
for manifest in list(HERE.glob('Solid*/history_files.json'))+list((HERE/'related_history').glob('*/history_files.json')):
    hashes=read(manifest);old_checks[str(manifest)]=dict(files=len(hashes),differences=[p for p,h in hashes.items() if sha(p)!=h])
write(HERE/'source_and_old_evidence_preservation_final.json',dict(checked_at=now(),scoped_source_file_count=len(all_frozen),scoped_source_hashes=all_frozen,
    source_differences=[p for p,h in all_frozen.items() if sha(PROJECT/p)!=h],old_evidence_checks=old_checks,
    all_source_and_old_scoped_evidence_hashes_unchanged=all(sha(PROJECT/p)==h for p,h in all_frozen.items()) and all(not x['differences'] for x in old_checks.values()),
    whole_workspace_unchanged_claim=False,unrelated_concurrent_changes_not_restored=True))
write(HERE/'second_review_queue.json',dict(unit='background_51',stage='material_refinement',created_at=now(),
    candidate_count=len(candidates),candidates=candidates,parent_action='Create a NEW independent second-review task for each actual candidate before delivery; primary researcher has not second-reviewed, approved or published.',
    rejected_or_missed_frozen_variants_not_promoted=True))
write(HERE/'checkpoint.json',dict(unit='background_51',stage='material_refinement',finished_at=now(),status='finite_batch_complete',
    stop_reason='All8 assigned questions reasonably assessed; no further images/calls are authorized by this finite unit.' if not (HERE/'external_failure_stop.json').exists() else 'All8 assessed; final API attempt failed/incomplete; no further calls/retry.',
    assigned_question_ids=IDS,actual_assessed_question_ids=IDS,unworked_question_ids=[],assessed_count=8,
    new_design_count=3,prescreen_only_count=5,actual_API_attempts=total_attempted,completed_calls=total_completed,
    external_error_calls=total_errors,aborted_calls=total_aborted,original_control_calls=0,retries=0,
    credible_two_hit_primary_possibility_count=len(candidates),independent_second_reviews_by_this_researcher=0,new_qualified_deliveries=0,
    all_question_assessments=assessments,complete_frozen_bindings_and_full_manual_replies=checks,
    second_review_queue=str(HERE/'second_review_queue.json'),source_preservation=str(HERE/'source_and_old_evidence_preservation_final.json'),
    current_eligibility_audits=[str(HERE/q/'eligibility_final.json') for q in IDS],
    history_corrections=str(HERE/'old_history_manual_outcomes_and_corrections.json'),
    offline_setup_errors=str(HERE/'offline_setup_errors.json'),no_external_retry=True,
    process_closure_audit=str(HERE/'process_check_final.json'),
    all_new_files_TEMP_TMP_MPLCONFIGDIR_XDG_CACHE_HOME_under=str(HERE),
    own_write_guard_installed_before_project_imports=True,
    formal_original_approvals_env_dotruntime_git_shared_helpers_global_ledgers_old_evidence_modified=False,
    no_Pass_Collect_review_approval_publication_API=True,no_nested_agents_threads_worktrees_servers=True,
    limitations=['No causal/statistical improvement is established; no new original controls were run.',
        'Solid182 intended20 depends on the depicted uniform alternating adjacency; generic12-pentagon wording alone does not fix an arbitrary unseen hexagon count, and that case was held before design/calls.',
        'Source vessel geometry is schematic; numeric reconstructed volume integration is a diagnostic, while the original highest-level comparison uses monotonicity and symmetry.']))
print(json.dumps(dict(assessed=8,designs=3,attempted=total_attempted,completed=total_completed,errors=total_errors,aborted=total_aborted,candidates=len(candidates)),ensure_ascii=False))
