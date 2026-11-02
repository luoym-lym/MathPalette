from bootstrap import *
import subprocess
vid=sys.argv[1];d=OWN/'Plane213'/vid;p=read(d/'pair_process.json');pid=p['pid']
ps='Get-CimInstance Win32_Process -Filter "ProcessId='+str(pid)+'" | Select-Object ProcessId,ParentProcessId,CreationDate,ReadOperationCount,ReadTransferCount,WriteOperationCount,WriteTransferCount,KernelModeTime,UserModeTime,CommandLine | ConvertTo-Json -Depth 3 -Compress'
r=subprocess.run(['powershell','-NoProfile','-NonInteractive','-Command',ps],capture_output=True,text=True,encoding='utf-8',check=True)
proc=json.loads(r.stdout) if r.stdout.strip() else None
if proc:assert 'u11_plane213_continue' in proc['CommandLine'] and vid in proc['CommandLine'] and 'run_pair.py' in proc['CommandLine']
starts=list(d.rglob('run_*_started.json'));completed=[read(f) for f in d.rglob('run_[0-9][0-9].json')]
observation={'at_utc':now(),'verified_owned_process':proc,'actual_request_starts':len(starts),'completed_run_records':len(completed),'statuses':[r['status'] for r in completed],'summary_exists':bool(list(d.rglob('summary.json'))),'new_API_calls_by_this_observation':0,'original_no_timeout_behavior_preserved':True,'no_request_retried_or_terminated':True}
target=d/'pending_process_observations.json';old=read(target) if target.exists() else [];old.append(observation);save(target,old,replace=True)
ck=read(OWN/'checkpoint.json');all_starts=list((OWN/'Plane213').rglob('run_*_started.json'));all_results=[read(f) for f in (OWN/'Plane213').rglob('run_[0-9][0-9].json')]
ck.update(at_utc=now(),actual_API_attempts_including_pending=len(all_starts),actual_completed_responses=len([r for r in all_results if r['status']=='completed']),pending_API_requests=len(all_starts)-len(all_results),status='awaiting_original_pair_response_no_retry',pending_variant_id=vid)
save('checkpoint.json',ck,replace=True)
print(json.dumps(observation,ensure_ascii=False))
