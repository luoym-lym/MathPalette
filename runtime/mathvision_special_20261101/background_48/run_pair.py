import task_env
from task_env import OWN
from prepare import write,read,eligibility,hashfile
import sys,os,runpy
from datetime import datetime,timezone
q=sys.argv[1];var=sys.argv[2];d=OWN/q/var
assert (d/'primary_review.json').is_file() and read(d/'primary_review.json')['proceed_to_API']
assert not (d/'api_process.json').exists(),'No retry of this frozen candidate'
e=eligibility(q);write(d/'eligibility_immediately_before_calls.json',e);assert e['eligible']
design=read(d/'design.json');assert hashfile(d/'candidate.png')==design['png_sha256']
write(d/'api_process.json',{'pid':os.getpid(),'executable':sys.executable,'argv':sys.argv,'started_at_utc':datetime.now(timezone.utc).isoformat(),'question_id':q,'variant_id':var,'requested_runs':2,'no_retry':True})
sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',q,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
try:
    runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
finally:
    write(d/'api_process_finished.json',{'pid':os.getpid(),'finished_at_utc':datetime.now(timezone.utc).isoformat(),'process_will_exit_after_this_foreground_wrapper':True})
