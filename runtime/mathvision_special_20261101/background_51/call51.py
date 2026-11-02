from tools51 import *
import subprocess

qid=sys.argv[1]; assert qid in ['Solid153','Solid183','Solid202']
assert not (HERE/'external_failure_stop.json').exists(), 'External failure already recorded; no further calls.'
spec=read(HERE/qid/'spec_r51.json');d=HERE/qid/spec['name']
assert not (d/'api_process.json').exists(), 'This frozen candidate already launched; no retry.'
e=eligibility(qid); assert e['eligible'];write(d/'eligibility_immediately_before_calls.json',e)
for p,h in read(HERE/qid/'source_hashes_initial.json').items(): assert sha(PROJECT/p)==h,p
design=read(d/'design.json');assert sha(d/'candidate.png')==design['png_sha256']
assert sha(d/'plugin.json')==design['plugin_sha256']
command=[sys.executable,'-X','utf8','-B',str(HERE/'harness/quicktest3_isolated.py'),
    '--branch',BRANCH,'--question',qid,'--image',str(d/'candidate.png'),
    '--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
with (d/'api_stdout.log').open('x',encoding='utf-8') as log:
    process=subprocess.Popen(command,cwd=PROJECT,env=os.environ.copy(),stdout=log,stderr=subprocess.STDOUT)
    write(d/'api_process.json',dict(started_at=now(),pid=process.pid,parent_pid=os.getpid(),command=command,
        expected_wrong_answer=design['expected_wrong_answer'],design_sha256=sha(d/'design.json'),image_sha256=sha(d/'candidate.png'),
        no_timeout_or_retry=True))
    print('START',qid,'own_API_PID',process.pid,flush=True)
    code=process.wait()
write(d/'api_process_finished.json',dict(finished_at=now(),pid=process.pid,returncode=code,wait_reaped=True))
summaries=list((d/'tests').glob('*/summary.json'))
if len(summaries)!=1:
    write(HERE/'external_failure_stop.json',dict(question_id=qid,reason='Harness ended without exactly one summary',returncode=code,stdout_log=str(d/'api_stdout.log')))
    print('STOP: no complete summary; preserve evidence, no retry.',flush=True);sys.exit(2)
summary=read(summaries[0]);errors=[r for r in summary['results'] if r['status']!='completed']
if errors or not summary['two_completed']:
    write(HERE/'external_failure_stop.json',dict(question_id=qid,summary_path=str(summaries[0]),results=summary['results'],reason='First API failure/incomplete call stops all later calls; no retry.'))
    print('STOP: external failure',json.dumps(errors,ensure_ascii=False),flush=True);sys.exit(2)
print('COMPLETE',qid,'two calls',str(summaries[0]),flush=True)
