from bootstrap import install,OWN,PROJECT,SESSION
install()
import sys,subprocess,json,os
from datetime import datetime,timezone
from research import save,load,sha
from prepare import eligibility

qid=sys.argv[1]
assert qid in ['Plane480','Plane481','Plane482','Plane483','Plane488']
if (OWN/'external_failure.json').exists():raise RuntimeError('External failure already recorded; further calls prohibited.')
design_path=next((OWN/qid).glob('r52_*/design.json'));folder=design_path.parent
assert not (folder/'tests').exists(),'No repeat of any tested/aborted image.'
e=eligibility(qid,'eligibility_before_calls.json')
initial=load(OWN/qid/'eligibility_initial.json')
assert e['content']==initial['content']
d=load(design_path);review=load(folder/'primary_review_before_calls.json')
assert sha(design_path)==review['design_sha256'] and sha(folder/'candidate.png')==review['image_sha256']==d['image_sha256']
assert review['primary_admissible_for_own_two_calls']
h=load(OWN/'harness_isolation_audit.json')
assert sha(h['isolated_path'])==h['isolated_sha256'] and sha(h['source_path'])==h['source_sha256']
command=[sys.executable,'-X','utf8','-B',str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',qid,'--image',str(folder/'candidate.png'),'--design',str(design_path),'--output',str(folder/'tests'),'--runs','2']
with (folder/'api_stdout.log').open('x',encoding='utf-8') as out,(folder/'api_stderr.log').open('x',encoding='utf-8') as err:
    process=subprocess.Popen(command,cwd=PROJECT,stdout=out,stderr=err,env=os.environ.copy())
    save(folder/'api_process.json',{'pid':process.pid,'parent_pid':os.getpid(),'command':command,'started_at_utc':datetime.now(timezone.utc).isoformat(),'timeout_override':None,'retries':0})
    print(json.dumps({'qid':qid,'pid':process.pid,'command':command},ensure_ascii=False),flush=True)
    code=process.wait()
save(folder/'api_process_finished.json',{'pid':process.pid,'exit_code':code,'finished_at_utc':datetime.now(timezone.utc).isoformat()})
summaries=list((folder/'tests').glob('*/summary.json'))
if code!=0 or len(summaries)!=1:
    save(OWN/'external_failure.json',{'qid':qid,'kind':'harness/process failure or incomplete evidence','exit_code':code,'stdout':str(folder/'api_stdout.log'),'stderr':str(folder/'api_stderr.log'),'retry':False,'manual_abort_record':load(folder/'manual_abort_record.json') if (folder/'manual_abort_record.json').exists() else None})
    raise RuntimeError('Stop: harness incomplete; inspect frozen logs, no retry.')
s=load(summaries[0])
if not s['two_completed']:
    save(OWN/'external_failure.json',{'qid':qid,'kind':'external API error/incomplete pair','summary':str(summaries[0]),'results':s['results'],'retry':False})
print(json.dumps({'qid':qid,'summary':str(summaries[0]),'two_completed':s['two_completed'],'statuses':[r['status'] for r in s['results']]},ensure_ascii=False),flush=True)
