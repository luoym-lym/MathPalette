from tools57 import *
import subprocess
qid=sys.argv[1];assert qid in ['Solid79','Solid234']
assert not (HERE/'external_failure_stop.json').exists()
spec=read(HERE/qid/'spec_r57.json');d=HERE/qid/spec['variant_id']
assert not (d/'api_process.json').exists(),'Already launched; no retry.'
assert read(d/'primary_native_review.json')['proceed_with_exact_frozen_two_calls']
e=eligibility(qid);write(d/'eligibility_immediately_before_calls.json',e);assert e['eligible']
for p,h in read(HERE/qid/'source_hashes_initial.json').items(): assert sha(PROJECT/p)==h,p
design=read(d/'design.json');assert sha(d/'candidate.png')==design['png_sha256'] and sha(d/'plugin.json')==design['plugin_sha256']
cmd=[sys.executable,'-X','utf8','-B',str(HERE/'harness/quicktest3_isolated.py'),'--branch',BRANCH,'--question',qid,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
with (d/'api_stdout.log').open('x',encoding='utf-8') as log:
    p=subprocess.Popen(cmd,cwd=PROJECT,env=os.environ.copy(),stdout=log,stderr=subprocess.STDOUT)
    write(d/'api_process.json',dict(started_at=now(),pid=p.pid,parent_pid=os.getpid(),command=cmd,design_sha256=sha(d/'design.json'),image_sha256=sha(d/'candidate.png'),expected_wrong_answer=design['expected_wrong_answer'],no_timeout_no_retry=True))
    print('START',qid,'own_API_PID',p.pid,flush=True)
    code=p.wait()
write(d/'api_process_finished.json',dict(pid=p.pid,returncode=code,finished_at=now(),wait_reaped=True))
summaries=list((d/'tests').glob('*/summary.json'))
if len(summaries)!=1:
    write(HERE/'external_failure_stop.json',dict(question_id=qid,reason='Harness ended without exactly one summary; no retry',returncode=code,log=str(d/'api_stdout.log')));sys.exit(2)
s=read(summaries[0])
if not s['two_completed']:
    write(HERE/'external_failure_stop.json',dict(question_id=qid,reason='External failure or incomplete request; stop all future API calls without retry.',summary_path=str(summaries[0]),results=s['results']));print('EXTERNAL STOP',str(summaries[0]),flush=True);sys.exit(2)
print('COMPLETE',qid,'two calls',str(summaries[0]),flush=True)
