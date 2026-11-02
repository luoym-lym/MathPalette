from bootstrap import *
import subprocess
tracked=read(OWN/'readonly_initial_sha256.json')
changed=[{'path':p,'initial_sha256':h,'current_sha256':sha(p)} for p,h in tracked.items() if sha(p)!=h]
assert not changed
save('readonly_preservation_final.json',{'at_utc':now(),'tracked_file_count':len(tracked),'changed_files':changed,'all_tracked_formal_source_reference_helper_and_old_evidence_hashes_unchanged':True,'scope':'Exactly readonly_initial_sha256.json; parent progress and other unrelated runtime metadata are not called source drift.','source_hashes':tracked})
pairs=[]
for p in sorted((OWN/'Plane213').glob('*/pair_reaped.json')):
    a=read(p);assert a['reaped'] and a['returncode']==0
    finished=read(p.parent/'pair_process_finished.json');assert finished['finished']
    pairs.append({'variant_id':p.parent.name,'API_pid':a['pid'],'reaped':True,'returncode':a['returncode'],'actual_request_attempts':finished['actual_request_attempts']})
own_text=OWN.name.replace("'","''")
ps="$taskUnitNeedle='"+own_text+"'; Get-CimInstance Win32_Process | Where-Object { $_.Name -like 'python*' -and $_.ProcessId -ne "+str(os.getpid())+" -and $_.CommandLine -like ('*'+$taskUnitNeedle+'*') } | Select-Object ProcessId,ParentProcessId,CommandLine | ConvertTo-Json -Depth 3 -Compress"
result=subprocess.run(['powershell','-NoProfile','-NonInteractive','-Command',ps],capture_output=True,text=True,encoding='utf-8',check=True)
other=json.loads(result.stdout) if result.stdout.strip() else []
assert not other,'Owned local process still active; finish it safely before closure.'
save('process_closure_audit.json',{'at_utc':now(),'all_API_pairs':pairs,'all_owned_API_children_reaped':True,'active_owned_API_requests':0,'other_owned_python_processes_excluding_this_short_lived_closer':other,'closer_pid':os.getpid(),'closer_exits_normally_after_writing_audit':True,'servers_subagents_worktrees_started':0,'new_provider_or_model_switches':0,'API_retries':0,'scope':'Owned Python processes carrying the unique u11_plane213_continue unit token, including relative commands; no other task process stopped.'})
ck=read(OWN/'checkpoint.json');ck.update(at_utc=now(),current_eligibility=eligibility(),active_owned_API_requests=0,all_owned_API_pairs_reaped=True,other_owned_local_processes=0,readonly_preservation_final_path=str(OWN/'readonly_preservation_final.json'),process_closure_audit_path=str(OWN/'process_closure_audit.json'))
save('checkpoint.json',ck,replace=True)
manifest={p.relative_to(OWN).as_posix():sha(p) for p in sorted(OWN.rglob('*')) if p.is_file() and p.name!='closing_artifact_sha256.json'}
save('closing_artifact_sha256.json',manifest)
print(json.dumps({'question_id':'Plane213','PRIMARY_candidates':len(read(OWN/'second_review_queue.json')),'completed_API_calls':ck.get('completed_API_calls'),'reaped_pairs':len(pairs),'other_owned_processes':0,'tracked_readonly_files_unchanged':len(tracked)},ensure_ascii=False))
