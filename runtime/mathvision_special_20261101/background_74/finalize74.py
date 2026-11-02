from audit74 import *
import ast

def main():
    scan=read(HERE/'global_prior_invocation_scan.json')
    assert not any(x['exact'] for x in scan['embedded_images'])
    matching=[]
    malformed=[]
    for x in scan['errors']:
        p=Path(x['path']); raw=p.read_bytes(); needles={}
        for enc in ['utf-8','utf-16-le','utf-16-be']:
            for key,value in [('png_sha',TARGET_SHA),('qid',QID),('variant',VARIANT),('source_key','test:2693')]:
                if value.encode(enc) in raw: needles[key+':'+enc]=True
        # Match the complete exact base64 even in UTF16/escaped slash historical records.
        encoded=base64.b64encode((SOURCE/'candidate.png').read_bytes()).decode('ascii')
        for enc in ['utf-8','utf-16-le','utf-16-be']:
            for value in [encoded,encoded.replace('/','\\/')]:
                if value.encode(enc) in raw: needles['exact_base64:'+enc]=True
        target=HERE/'malformed_preserved'/x['sha256']/p.name
        target.parent.mkdir(parents=True,exist_ok=True)
        if not target.exists(): target.write_bytes(raw)
        malformed.append(dict(path=str(p),sha256=sha(p),snapshot=str(target),raw_matches=needles,error=x['error']))
        if needles: matching.append(malformed[-1])
        del raw,encoded
    write('malformed_raw_match_audit.json',dict(files=malformed,matching=matching,preserved_originals=True,
        note='Malformed source bytes preserved verbatim; raw UTF8/UTF16 exact SHA/ID/variant/source-key and exact/escaped-base64 tested. No repair or overwrite.'))
    # Every relevant actual-invocation-looking artifact is explicitly inventoried.
    transport=[]; exact_files=[]
    for x in scan['matches']:
        p=Path(x['path']); lower=p.name.lower()
        if 'exact_file_bytes' in x['match']: exact_files.append(x)
        if any(k in lower for k in ['binding','request','response','started','summary','incomplete','error','api_process','api_stdout']):
            transport.append(x)
    write('global_zero_call_primary_assessment.json',dict(checked_at=now(),scan=str(HERE/'global_prior_invocation_scan.json'),
        exact_embedded_request_count=0,exact_png_files=exact_files,invocation_named_matching_records=transport,
        malformed_matching_unknown_count=len(matching),
        conclusion='No matching prior actual invocation observed in this available task snapshot. Historical api_process is process-start metadata, not a request-start; the source startup imports failed before transport. This remains a PRIMARY evidence assessment, not authorization to reuse after the new local stop.',
        historical_source_only_zero_call_not_relied_upon=True,
        limits=scan['limits']+['Fresh offline replay and immediately-before-call scan were not completed; no copied inputs or API was authorized by this audit.']))
    # Prove the historical pre-request failure ordering without executing old code.
    ref=BASE/'harness/quicktest3_isolated.py'; old=BASE/'background_57/harness/quicktest3_isolated.py'
    ref_ast=ast.parse(ref.read_text(encoding='utf-8-sig'));old_ast=ast.parse(old.read_text(encoding='utf-8-sig'))
    def functions(tree): return {x.name:ast.dump(x,include_attributes=False) for x in tree.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))}
    assert functions(ref_ast)==functions(old_ast)
    old_text=old.read_text(encoding='utf-8-sig')
    assert old_text.index('from bootstrap import HERE as OWN_ROOT') < old_text.index('def run_tests')
    bootstrap_text=(BASE/'background_57/bootstrap.py').read_text(encoding='utf-8-sig')
    assert 'ISOLATION = install(' in bootstrap_text
    historical_artifacts=[]
    for p in SOURCE.rglob('*'):
        if not p.is_file(): continue
        if p.name in ['binding.json','request.json','summary.json'] or re.search(r'run_\d+.*(?:started|response|incomplete)',p.name): historical_artifacts.append(str(p))
    assert not historical_artifacts
    startup=read(SOURCE/'local_startup_abort_review.json')
    write('historical_startup_transport_order_audit.json',dict(checked_at=now(),original_log_path=str(SOURCE/'api_stdout.log'),
        log_sha256=sha(SOURCE/'api_stdout.log'),process_metadata=read(SOURCE/'api_process.json'),finished=read(SOURCE/'api_process_finished.json'),
        original_review=startup,reference_harness_sha256=sha(ref),old_harness_sha256=sha(old),all_function_ASTs_identical=True,
        ordering='Old relocated harness imports bootstrap before run_tests/main. bootstrap installs runtime_isolation, which imports dataset_tools.mathvision_workbench and numerical plotting libraries. OpenBLAS failure during startup exited before run_tests. Transport occurs only after durable binding.json, request.json, design_snapshot.json and run_N_started.json writes. None exists in the source directory; complete task embedded/request hash scan found no exact request.',
        source_request_artifacts=historical_artifacts,actual_source_calls_observed=0,
        original_startup_not_overwritten=True,new_local_import_error_distinct=True))
    # Fresh duplicate audit over authoritative datasets, without testing other questions.
    initial=read(HERE/'eligibility_initial.json'); formal_sha=sha(PROJECT/'SolidGeometry/image/Solid234.png')
    duplicates=[]; semantic=[]; count=0
    for branch in ['Analytics','PlaneGeometry','SolidGeometry']:
        for r in rows(PROJECT/branch/'dataset.jsonl'):
            count+=1
            if r['id']==QID: continue
            if r.get('image') and sha(PROJECT/branch/r['image'])==formal_sha: duplicates.append(dict(branch=branch,id=r['id']))
            if r.get('source_key')=='test:2693' or r.get('question')==initial['record']['question']:
                semantic.append(dict(branch=branch,id=r['id'],source_dataset=r.get('source_dataset'),source_key=r.get('source_key')))
    write('related_duplicate_audit.json',dict(checked_at=now(),formal_records_read=count,exact_formal_png_duplicates=duplicates,
        same_source_key_or_exact_question_duplicates=semantic,old_assessment=str(BASE/'background_15/Solid234/primary_prescreen.json'),
        old_r15_designs_or_calls_observed=0,old_r57_zero_actual_calls_observed=True,
        scope='Read-only duplicate/source provenance check; no other question tested or redesigned.'))
    # Full reads for all cited old source records and semantic lessons, singly, with digests.
    receipts=[]
    paths=[BASE/'background_57_brief.txt',BASE/'background_57_assignment.json',BASE/'continuation_brief.txt',BASE/'exploration_report.json',BASE/'remaining_questions.jsonl']
    paths+=list((BASE/'background_15'/QID).rglob('*'))+list((BASE/'background_57'/QID).rglob('*'))
    paths+=[BASE/'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',BASE/'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']
    paths += [PROJECT/'SolidGeometry'/p for p in initial['record']['runtime_dependencies']]
    for p in paths:
        if not p.is_file(): continue
        data=p.read_bytes(); item=dict(path=str(p),sha256=hashlib.sha256(data).hexdigest(),size=len(data),complete_read=True)
        if p.suffix in ('.json','.jsonl','.txt','.md','.py','.log'):
            text=data.decode('utf-8-sig')
            if p.suffix=='.json':
                obj=json.loads(text)
                if p.name=='independent_review.json': item['semantic_conclusions']={k:obj[k] for k in ['question_id','decision','reason','concrete_objections','limits'] if k in obj}
                del obj
            elif p.suffix=='.jsonl':
                for line in text.splitlines():
                    if line.strip(): json.loads(line)
            del text
        receipts.append(item); del data
    write('full_read_receipts_final.json',receipts)
    current=eligibility();write('eligibility_final.json',current)
    assert current['eligible']
    assert current['source_hashes']==initial['source_hashes']
    frozen=read(HERE/'source_input_hashes_initial.json');frozen_final={n:sha(SOURCE/n) for n in frozen}
    assert frozen==frozen_final
    write('source_preservation_final.json',dict(checked_at=now(),source_hashes_unchanged=True,source_inputs=frozen_final,
        formal_frozen_content_unchanged=True,approval_current=current['original_approval_current'],source_approval_fingerprint=current['current_content_sha256'],
        ownroot_only_new_files=True,listed_frozen_inputs_copied=False,historical_startup_logs_preserved=True))
    drift=[]
    for x in read(HERE/'parent_metadata_initial.json'):
        old_bytes=Path(x['snapshot']).read_bytes();current_bytes=Path(x['path']).read_bytes()
        state='unchanged' if current_bytes==old_bytes else 'exact_prefix_parent_append' if current_bytes.startswith(old_bytes) else 'mutable_metadata_rewrite_or_nonprefix_update'
        drift.append(dict(path=x['path'],snapshot=x['snapshot'],old_sha256=x['sha256'],new_sha256=hashlib.sha256(current_bytes).hexdigest(),
            old_size=len(old_bytes),new_size=len(current_bytes),classification=state,restored_or_rewritten_by_worker=False))
        del old_bytes,current_bytes
    write('parent_metadata_diagnostic_final.json',drift)
    failure=dict(kind='local_audit_import_path_error',exception='ModuleNotFoundError: No module named audit74',
        evidence=str(HERE/'local_audit_import_failure.log'),process_exit_code=1,api_started=False,
        explanation='The stdin summary command ran from project root without OWNROOT on sys.path. No project/numeric import or network began. This avoidable invocation error is recorded rather than attributed to quota or remote service.',
        disposition='HOLD without API, conservatively following the explicit local import failure stop rule.')
    write('local_failure_stop.json',failure)
    checkpoint=dict(unit='background_74',stage='quota_reset_first_pair_conditional',checked_at=now(),scope=[QID],
        status='HOLD_LOCAL_AUDIT_IMPORT_FAILURE_NO_API',assessed_question_ids=[QID],unworked_question_ids=[],
        frozen_variant_id=VARIANT,frozen_created_at='2026-11-01T20:40:23.746294+00:00',immutable_wrong_answer='D',correct_answer='C',
        new_mechanisms=0,new_designs=0,inputs_copied=0,actual_API_calls=0,complete_pairs=0,candidates=0,remote_API_errors=0,retries=0,
        hold=failure,current_eligibility=str(HERE/'eligibility_final.json'),source_preservation=str(HERE/'source_preservation_final.json'),
        math_native_every_marker_review=str(HERE/'fresh_math_native_every_marker_review.json'),
        math_result='Plane x=3+3z/4 over y^2+z^2<=16; extent0..6 proven by bounds+attaining endpoints; volume48pi~150.796=>C151. Maximum6 substitution96pi~301.593 has unique closest listedD192.',
        actual_source_formal_candidate_native_viewed=True,original_semantic_geometry_fill_text_dimensions_dashes_projection_visibility_preserved=True,
        global_scan=str(HERE/'global_prior_invocation_scan.json'),global_zero_call_primary_assessment=str(HERE/'global_zero_call_primary_assessment.json'),
        global_prior_call_observed=0,malformed_preserved=str(HERE/'malformed_raw_match_audit.json'),historical_transport_order=str(HERE/'historical_startup_transport_order_audit.json'),
        related_duplicate_audit=str(HERE/'related_duplicate_audit.json'),
        fresh_schema_default_noop_repeat_exact_replay='NOT EXECUTED: local audit import failure triggered conservative no-API stop; offline74.py prepared but its offline action never run.',
        frozen_input_copy_gate='NOT PASSED; no listed inputs copied; source oldpaths/date/preset untouched',
        harness_relocation='NOT PERFORMED; no solver harness launched',manual_finals=[],raw_requests=[],bindings=[],design_snapshots=[],
        skips=[],holds=[QID],remaining_gates=['Fresh schema/default normalization, no-op formal pixels, repeat and exact offline replay','Fresh whole-task prior-call scan immediately before any separately authorized future attempt'],
        parent_metadata_diagnostic=str(HERE/'parent_metadata_diagnostic_final.json'),
        all_new_files_temp_cache_logs_under_ownroot=True,failed_stdin_command_guard='Guard import did not begin; no writes were performed by that failed command.',
        owned_API_processes_started=0,owned_API_processes_live=0,process_closure=str(HERE/'process_closure.json'),
        forbidden_actions_performed=False,nested_agents_threads_worktrees_servers=False,
        review_status='PRIMARY assessment only; no independent review/userapproval/originalreview/Pass/Collect/publication/delivery/formal edit',
        inherited_Codex_configuration_unchanged=True,
        limits=['No calls; no hit or causal-effect claim.','No claim about deleted/unseen provider records.','Local orchestration error is avoidable and explicitly preserved; no new post-reset quota failure inferred.'])
    write('checkpoint.json',checkpoint)
    write('second_review_queue.json',dict(unit='background_74',checked_at=now(),candidates=[],count=0,holds=[dict(question_id=QID,variant_id=VARIANT,reason=checkpoint['status'])],
        reason='No API calls or complete pair. Parent must launch a NEW independent delegate review for any future credible double-hit; this worker performs no independent self-review.'))
    print(json.dumps(dict(status=checkpoint['status'],calls=0,candidates=0,live_API_processes=0,matching_malformed=len(matching),current_eligible=current['eligible'],source_inputs_preserved=True)))

if __name__=='__main__': main()
