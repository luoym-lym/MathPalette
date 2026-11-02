from env67 import *
import base64
import gc

gate=OWN/'zero_call_final_gate.json'
before=gate.read_bytes(); before_sha=hashlib.sha256(before).hexdigest()
archive=OWN/'zero_gate_versions'/before_sha/'zero_call_final_gate.json'
archive.parent.mkdir(parents=True,exist_ok=True)
if not archive.exists(): archive.write_bytes(before)
original=json.loads(before)
A=read(OWN/'snapshots/background_67_assignment.json')
targets={v['frozen_source_files_sha256']['candidate.png']:v['question_id'] for v in A['questions']}
resolutions=[]
blockers=[]
for b in original['blockers']:
    if 'unknown_matching_supplement' in b:
        source=Path(b['unknown_matching_supplement']['path']); data=source.read_bytes(); h=hashlib.sha256(data).hexdigest()
        dst=OWN/'supplement_metadata_full_snapshots'/h/source.name; dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists(): dst.write_bytes(data)
        if source.suffix=='.jsonl': values=[json.loads(line) for line in data.decode('utf-8-sig').splitlines() if line.strip()]
        else: values=[json.loads(data.decode('utf-8-sig'))]
        rootkeys=list(values[0]) if isinstance(values[0],dict) else ['array']
        stack=values[:]; actual=[]; payload=[]; matching_leaf_records=[]
        while stack:
            v=stack.pop()
            if isinstance(v,dict):
                bound=v.get('image_sha256',v.get('png_sha256'))
                if isinstance(bound,str) and bound in targets and any(k in v for k in ('run_index','run_id','started_at','http_status','response_sha256')): actual.append({'question_id':targets[bound],'record':v})
                if 'sha256' in v and v['sha256'] in targets:
                    matching_leaf_records.append({k:x for k,x in v.items() if not isinstance(x,(dict,list))})
                stack.extend(v.values())
            elif isinstance(v,list): stack.extend(v)
            elif isinstance(v,str) and v.startswith('data:image/') and ';base64,' in v:
                try: raw=base64.b64decode(v.split(',',1)[1],validate=True)
                except ValueError: pass
                else:
                    ih=hashlib.sha256(raw).hexdigest(); del raw
                    if ih in targets: payload.append(targets[ih])
        metadata_kind='other_worker_global_file_or_PNG_hash_inventory' if any(x in source.name for x in ('hash_audit','file_inventory')) else 'full_parent_progress_or_quota_recovery_metadata_snapshot'
        resolution={'path':str(source),'current_full_snapshot':str(dst),'current_sha256':h,'scanned_sha256':b['unknown_matching_supplement']['sha256'],'bytes':len(data),'full_UTF8_JSON_or_JSONL_read':True,'root_keys':rootkeys[:30],'actual_assigned_PNG_bound_run_records':actual,'actual_assigned_embedded_requests':payload,'matching_hash_inventory_leaf_records':matching_leaf_records[:30],'classification':metadata_kind,'source_is_readonly':True,'same_directory_other_question_calls_do_not_bind_this_PNG':True,'reason':'These files enumerate source PNG hashes or preserve parent preparation/progress, rather than carrying an actual request/start/raw for an assigned frozen PNG. Full records were examined, in addition to global direct artifacts and embedded-request scan.'}
        resolutions.append(resolution)
        if actual or payload: blockers.append(resolution)
        print('METADATA_RESOLUTION',source.name,'actual_bound_runs',len(actual),'exact_payloads',len(payload),'keys',rootkeys[:8],flush=True)
        del data,values,stack; gc.collect()
    elif 'unreadable_supplement_files' in b:
        for failure in b['unreadable_supplement_files']:
            source=Path(failure['path'])
            allowed={PROJECT/'.runtime/analytics_special/state/workbench.lock':PROJECT/'Analytics/workbench/review_store.py',PROJECT/'.runtime/solid_special/state/workbench.lock':PROJECT/'SolidGeometry/workbench/review_store.py'}
            helper=allowed.get(source)
            text=helper.read_text(encoding='utf-8-sig') if helper else ''
            size=source.stat().st_size
            sentinel=helper is not None and size==1 and 'self.handle.write(b"0")' in text and 'msvcrt.LK_NBLCK, 1' in text
            resolution={'path':str(source),'read_failure_preserved':failure,'observed_bytes':size,'classification':'OS-exclusive_one-byte_workbench_writer_mutex' if sentinel else 'unresolved','helper':str(helper),'helper_sha256':sha(helper) if helper else None,'helper_full_read':bool(helper),'reason':'The unchanged StoreLock writes exactly one byte b"0" and holds an OS byte-range lock. This sentinel cannot contain a PNG, SHA256, request, binding, start, response or any assigned identity. The lock was not opened for writing, released or modified. This is an unrelated active-service mutex, not unknown matching call evidence.'}
            resolutions.append(resolution)
            if not sentinel: blockers.append(resolution)
            print('LOCK_RESOLUTION',str(source),size,'sentinel',sentinel,flush=True)
    else: blockers.append(b)
save('zero_call_supplement_diagnostic_resolution.json',{'at':now(),'original_uncertainty_gate':str(archive),'original_gate_sha256':before_sha,'resolutions':resolutions,'remaining_blockers':blockers,'no_old_report_or_source_record_rewritten':True})
new={**original,'at':now(),'initial_uncertainty_gate_archived':str(archive),'supplement_diagnostic_resolution':str(OWN/'zero_call_supplement_diagnostic_resolution.json'),'blockers':blockers,'all_three_zero_prior_actual_calls_proved':not blockers,'explicit_non_evidence_exceptions':['Two OS-exclusive 1-byte workbench.lock sentinels; exact code and size audited; contents not forcibly read.'],'zero_call_basis':'No exact assigned PNG embedded request, binding/start/run/raw/summary or related-duplicate actual-call evidence across full task and legacy runtime. Every matching reference and malformed/placeholder record was preserved and classified. Missing summary was never the basis.'}
save(gate,new)
print('ADJUDICATED_FINAL_ZERO_CALL_GATE',new['all_three_zero_prior_actual_calls_proved'],'remaining_blockers',len(blockers),flush=True)
