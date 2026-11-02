import bootstrap
from bootstrap import OWN,ROOT
import sys,json,subprocess,os
from datetime import datetime,timezone
from make_candidates import eligible,save
from workbench_io import file_hash
q=sys.argv[1];base=next((OWN/q).glob('r29_*/design.json')).parent
assert (base/'pretest_native_visual_and_marker_audit.json').is_file()
save(base/'eligibility_at_process_launch.json',eligible(q))
command=[sys.executable,'-X','utf8','-B',str(OWN/'harness/quicktest3_isolated.py'),'--branch','SolidGeometry','--question',q,'--image',str(base/'frozen/candidate.png'),'--design',str(base/'design.json'),'--output',str(base/'tests'),'--runs','2']
with (base/'api_stdout.log').open('xb') as out,(base/'api_stderr.log').open('xb') as err:
    process=subprocess.Popen(command,cwd=ROOT,env=os.environ.copy(),stdout=out,stderr=err)
    launch={'pid':process.pid,'supervisor_pid':os.getpid(),'command':command,'created_at':datetime.now(timezone.utc).isoformat(),'design_sha256':file_hash(base/'design.json'),'image_sha256':file_hash(base/'frozen/candidate.png'),'runs_requested':2,'no_timeout_retry_profile_or_token_overrides':True}
    save(base/'api_process_launch.json',launch)
    print(json.dumps(launch,ensure_ascii=False),flush=True)
    result=process.wait()
save(base/'api_process_completed.json',{'pid':process.pid,'exit_code':result,'finished_at':datetime.now(timezone.utc).isoformat(),'all_own_requests_in_this_pair_finished':True})
print(json.dumps({'question_id':q,'exit_code':result,'stdout':str(base/'api_stdout.log'),'stderr':str(base/'api_stderr.log')},ensure_ascii=False),flush=True)
