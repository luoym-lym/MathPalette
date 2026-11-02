from env47 import *
import json
import subprocess
from datetime import datetime,timezone
from inspect47 import eligibility

def main():
    qid=sys.argv[1]
    root=next((OWN/qid).glob('r47_*'))
    assert not (OWN/'EXTERNAL_FAILURE_STOP.json').exists(),'External failure already occurred; no further calls permitted.'
    assert not (root/'api_process.json').exists(),'Already invoked; never retry this exact image.'
    review=json.loads((root/'primary_review.json').read_text(encoding='utf-8'))
    assert review['primary_pre_call_disposition']=='credible_to_test'
    audit=eligibility(qid);assert audit['eligible']
    dump(root/'eligibility_immediately_before_calls.json',audit)
    d=json.loads((root/'design.json').read_text(encoding='utf-8'))
    assert sha(root/'candidate.png')==d['image_sha256'] and sha(root/'plugin.json')==d['plugin_sha256']
    cmd=[sys.executable,'-X','utf8','-B',str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',qid,'--image',str(root/'candidate.png'),'--design',str(root/'design.json'),'--output',str(root/'tests'),'--runs','2']
    began=datetime.now(timezone.utc).isoformat()
    logpath=root/'api_stdout.log'
    with logpath.open('xb') as log:
        process=subprocess.Popen(cmd,cwd=str(PROJECT),env=os.environ.copy(),stdout=log,stderr=subprocess.STDOUT)
        dump(root/'api_process.json',{'pid':process.pid,'parent_pid':os.getpid(),'command':cmd,'started_at':began,'stdout_log':str(logpath),'no_timeout_token_profile_overrides':True,'runs_requested':2})
        print(json.dumps({'qid':qid,'api_pid':process.pid,'parent_pid':os.getpid(),'log':str(logpath)},ensure_ascii=False),flush=True)
        code=process.wait()
    summaries=list((root/'tests').glob('*/summary.json'))
    status='error_or_incomplete'
    if len(summaries)==1:
        summary=json.loads(summaries[0].read_text(encoding='utf-8'))
        if summary['two_completed']:status='two_completed'
    dump(root/'api_process_finished.json',{'pid':process.pid,'exit_code':code,'finished_at':datetime.now(timezone.utc).isoformat(),'status':status,'summary_paths':[str(x) for x in summaries],'retries':0})
    if status!='two_completed':
        dump(OWN/'EXTERNAL_FAILURE_STOP.json',{'qid':qid,'status':status,'exit_code':code,'stdout_log':str(logpath),'summary_paths':[str(x) for x in summaries],'automatic_retry':False})
    print(json.dumps({'qid':qid,'status':status,'exit_code':code,'summary_paths':[str(x) for x in summaries]},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
