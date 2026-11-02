from common68 import *
import shutil

def main():
    assignment=read(BASE/'background_68_assignment.json')
    closure=read(HERE/'process_closure.json')
    assert closure['own_live_API_process_count']==0
    frozen_checks=[]; outcomes=[]; queue=[]; actual_calls=0; pairs=0
    for q in assignment['questions']:
        qid=q['question_id'];d=HERE/qid;candidate=d/q['variant_id']
        final=eligibility(qid);assert final['eligible'];write(d/'eligibility_final.json',final)
        source_audit=read(d/'source_binding_audit.json')
        for path,h in source_audit['frozen_dependencies'].items():
            actual=sha(path);frozen_checks.append(dict(path=path,sha256_initial=h,sha256_final=actual,equal=actual==h));assert actual==h
        for name,h in q['frozen_source_files_sha256'].items():
            for p in [Path(q['source_directory'])/name,candidate/name]:
                actual=sha(p);frozen_checks.append(dict(path=str(p),sha256_initial=h,sha256_final=actual,equal=actual==h));assert actual==h
        replay=read(d/'offline_replay/replay_verification.json')
        assert replay['matches_tested_png_bytes'] and replay['formal_inputs_unchanged']
        hold=d/'hold_before_API.json'
        if hold.is_file():
            assert not (candidate/'tests').exists() and not (candidate/'api_process_started.json').exists()
            outcome=dict(question_id=qid,variant_id=q['variant_id'],status='HOLD_before_API',actual_calls=0,hold=str(hold),native_reason=read(hold)['blocking_finding'],source_approval_valid=True)
        else:
            review=read(candidate/'manual_final_review.json')
            assert review['two_actual_complete_calls'] and len(review['manual_finals'])==2
            invs=list((candidate/'tests').glob('quicktest3_*'));assert len(invs)==1
            inv=invs[0]
            starts=list(inv.glob('run_*_started.json'));responses=list(inv.glob('run_*_response.json'))
            assert len(starts)==2 and len(responses)==2
            assert not list(inv.glob('*incomplete*')) and not (candidate/'runner_exception.json').exists()
            finished=read(candidate/'api_process_finished.json');assert finished['actual_transport_gates']==2 and finished['runner_status']=='completed'
            actual_calls+=2;pairs+=1
            outcome=dict(question_id=qid,variant_id=q['variant_id'],status=review['status'],actual_calls=2,complete_pair=True,
                expected_wrong_answer=q['expected_wrong_answer'],manual_finals=review['manual_finals'],valid_preset_hits=review['hits'],
                manual_final_review=str(candidate/'manual_final_review.json'),evidence_directory=str(inv),source_approval_valid=True,process_finished=str(candidate/'api_process_finished.json'))
            if review['credible_primary_doublehit']:
                queue.append(dict(question_id=qid,variant_id=q['variant_id'],candidate_directory=str(candidate),expected_wrong_answer=q['expected_wrong_answer'],
                    status='PRIMARY possibility only; parent must launch a NEW independent review before delivery',manual_final_review=str(candidate/'manual_final_review.json'),
                    primary_math=str(d/'primary_math_audit.json'),primary_native_every_marker=str(d/'primary_native_and_marker_review.json'),reuse_provenance=str(candidate/'reuse_provenance.json'),reuse_ready=str(candidate/'reuse_ready.json'),evidence_directory=str(inv)))
        outcome.update(original_created_at=q['frozen_created_at'],original_preset_unchanged=q['expected_wrong_answer'],candidate_png_sha256=sha(candidate/'candidate.png'),design_sha256=sha(candidate/'design.json'),plugin_sha256=sha(candidate/'plugin.json'),
            final_eligibility=str(d/'eligibility_final.json'),source_hashes=str(d/'source_binding_audit.json'),fresh_math=str(d/'primary_math_audit.json'),
            initial_primary_native_marker_review=str(d/'primary_native_and_marker_review.json'),fresh_schema_noop_repeat=str(d/'schema_render_check.json'),exact_offline_replay=str(d/'offline_replay/replay_verification.json'),
            reuse_provenance=str(candidate/'reuse_provenance.json'),global_zero_prior_calls=str(HERE/'zero_call_certification.json'),new_mechanism_count=0)
        outcomes.append(outcome)
    oldchecks=[]
    # Entire old source60 unit is immutable, beyond just its four selected drafts.
    for row in rows(HERE/'whole_task_files_initial.jsonl'):
        p=Path(row['path'])
        if (BASE/'background_60') in p.parents:
            actual=sha(p);oldchecks.append(dict(path=str(p),initial=row['sha256'],final=actual,equal=actual==row['sha256']));assert actual==row['sha256']
    for row in read(HERE/'scoped_old_history_hashes.json'):
        actual=sha(row['path']);assert actual==row['sha256']
        oldchecks.append(dict(path=row['path'],initial=row['sha256'],final=actual,equal=True))
    mutable=[]
    for row in read(HERE/'initial_snapshot_manifest.json'):
        p=Path(row['source']); original=Path(row['snapshot'])
        assert sha(original)==row['sha256']
        current=sha(p);old=original.read_bytes();cur=p.read_bytes()
        prefix=cur.startswith(old)
        if current!=row['sha256']:
            assert p.name in {'continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','master.json'}
            snap=HERE/'final_parent_snapshots'/(p.name+'.'+current+'.snapshot');snap.parent.mkdir(exist_ok=True)
            if not snap.exists():shutil.copyfile(p,snap)
        else:snap=original
        mutable.append(dict(path=str(p),original_full_snapshot=str(original),original_sha256=row['sha256'],final_sha256=current,exact_old_prefix=prefix,
            classification='exact' if current==row['sha256'] else 'parent_exact_prefix_append_diagnostic' if prefix else 'parent_update_diagnostic',final_snapshot=str(snap),old_records_restored_or_rewritten=False))
        del old,cur
    source60snapshots=[]
    for row in read(BASE/'background_60/initial_snapshot_manifest.json'):
        p=Path(row['snapshot']);assert sha(p)==row['sha256']
        dest=HERE/'source60_original_read_snapshots'/p.name;dest.parent.mkdir(exist_ok=True)
        if not dest.exists():shutil.copyfile(p,dest)
        assert sha(dest)==row['sha256'];source60snapshots.append(dict(original_snapshot=str(p),own_copy=str(dest),sha256=row['sha256']))
    write(HERE/'final_preservation_audit.json',dict(checked_at=now(),all_scoped_frozen_source_and_copy_hashes_exact=True,all_entire_source60_unit_and_scoped_old_history_hashes_exact=True,
        frozen_checks=frozen_checks,old_evidence_checks=oldchecks,parent_metadata=mutable,source60_original_snapshots_preserved=source60snapshots,
        scope_limit='Only tracked scoped frozen inputs, source60 unit and old history are asserted unchanged. Other workers and mutable parent metadata are read-only observations; no whole-workspace or actor attribution claim.'))
    write(HERE/'runtime_guard_and_process_audit.json',dict(checked_at=now(),research_agent_configuration='Inherited original Codex/gpt-6.1-sol ultra; no provider/model/options override or alternate provider',
        no_nested_agents_threads_worktrees_or_servers=True,all_new_files_under=str(HERE),python_invocation='python -X utf8 -B',
        ownprocess_thread_environment={k:os.environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},
        ownprocess_cache_environment={k:os.environ[k] for k in ['TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME']},
        strict_ownroot_audit_hook_before_project_numeric_Pillow_imports=True,shared_runtime_isolation=ISOLATION,
        harness_relocation_byte_audit=str(HERE/'harness_relocation_byte_audit.json'),
        each_actual_transport_current_eligibility_and_frozen_source_hash_gate=True,actual_API_calls=actual_calls,complete_pairs=pairs,aborts=0,remote_errors=0,local_allocation_import_render_failures=0,
        retries=0,third_calls=0,connectivity_pings=0,remote_profile_token_timeout_overrides=0,original_controls=0,
        all_owned_render_and_audit_processes_completed=True,all_owned_API_processes_finished=True,owned_live_API_requests=0,exact_PID_command_CIM_closure=closure,
        figures_closed_by_scene_finalizers_or_process_exit=True,formal_Special_approvals_env_git_and_old_source_mutations=0,
        no_user_approval_original_review_Pass_Collect_publication_or_delivery=True))
    write(HERE/'second_review_queue.json',queue)
    write(HERE/'checkpoint.json',dict(unit='background_68',stage='quota_resume_frozen_first_tests',status='completed_assigned_scope_first_pairs_or_holds',finished_at=now(),
        question_ids=IDS,actual_assessed_question_ids=IDS,unworked_question_ids=[],tested_question_ids=[r['question_id'] for r in outcomes if r['actual_calls']],
        held_question_ids=[r['question_id'] for r in outcomes if not r['actual_calls']],actual_API_calls=actual_calls,complete_pairs=pairs,credible_primary_doublehit_possibilities=len(queue),new_mechanism_count=0,
        outcomes=outcomes,stop_reason='Exact four assigned questions assessed: first pairs for eligible frozen drafts, or concrete native HOLD. No quota-thrift, control-correctness or causal-gain stop.',
        tested_frozen_images_exhausted_do_not_retake=[dict(question_id=r['question_id'],png_sha256=r['candidate_png_sha256'],evidence_directory=r['evidence_directory']) for r in outcomes if r['actual_calls']],
        skips=[],errors=[],aborts=[],retries=0,third_calls=0,no_relabel_or_cherrypick=True,
        old_history_manual_review=str(HERE/'manual_old_history_review.json'),all_old_full_raws=str(HERE/'scoped_old_full_finals_read.json'),
        global_zero_prior_call_audit=str(HERE/'whole_task_zero_call_scan.json'),zero_call_certification=str(HERE/'zero_call_certification.json'),archives_and_malformed_audit=str(HERE/'archive_and_malformed_supplement.json'),
        old_parse_flags='99 initial decoder/parser flags include UTF-16 JSON, non-JSON protocol snapshots and malformed old JSON mirrors. Exact bytes preserved, all raw/decoded matching evidence negative; no old record repaired.',
        parent_metadata_classification=str(HERE/'parent_metadata_classification.json'),final_preservation=str(HERE/'final_preservation_audit.json'),runtime_and_process_audit=str(HERE/'runtime_guard_and_process_audit.json'),
        second_review_queue=str(HERE/'second_review_queue.json'),owned_live_API_requests=0,
        independent_review_status='No self-independent review. Any PRIMARY possibility would require a NEW parent-commissioned independent review before delivery.',
        formal_edits=0,approval_Pass_Collect_publication_delivery_actions=0,
        limitations=['Two observations per tested frozen image only; no causal gain or mechanism confirmation asserted.','Plane271 run2 mentionsD only as a forced possibility but insists30 cm; inconsistent withD=15 and not a hit.','Plane367 initial native pass was superseded by a closer native line-class distinction HOLD; initial observations and all frozen bytes remain preserved.','checkpoint_final_pair_in_progress.json is provisional historical progress and can lag atomic raw-response writes; this final checkpoint and immutable request/start/raw bindings establish the completed state.']))
    artifacts={str(p.relative_to(HERE)):sha(p) for p in HERE.rglob('*') if p.is_file() and p.name not in ('own_artifact_hashes.json','finalize.log')}
    write(HERE/'own_artifact_hashes.json',artifacts)
    print(json.dumps(dict(assessed=4,complete_pairs=pairs,actual_calls=actual_calls,held=[r['question_id'] for r in outcomes if not r['actual_calls']],primary_candidates=len(queue),own_live_API_requests=0,checkpoint=str(HERE/'checkpoint.json')),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
