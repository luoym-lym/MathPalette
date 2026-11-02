import task_env
from task_env import OWN,PROJECT
from inspect_sources import read,save,sha,eligibility
import os,sys,runpy
from datetime import datetime,timezone

qid,variant=sys.argv[1:]
assert qid in ['Plane415','Plane421','Plane441']
folder=OWN/qid/variant
review=read(folder/'primary_review_before_calls.json')
assert review['proceed_to_exactly_two_real_calls']
assert sha(folder/'design.json')==review['design_sha256']
assert sha(folder/'candidate.png')==review['png_sha256']
assert sha(folder/'plugin.json')==review['plugin_sha256']
e=eligibility(qid);assert e['eligible'];save(folder/'eligibility_immediately_before_calls.json',e)
record={'pid':os.getpid(),'command_line_argv':[sys.executable,'-X','utf8','-B',*sys.argv],
        'cwd':os.getcwd(),'started_at_utc':datetime.now(timezone.utc).isoformat(),
        'question_id':qid,'variant_id':variant,'expected_runs':2,'no_retry':True,
        'design_sha256':sha(folder/'design.json'),'image_sha256':sha(folder/'candidate.png'),
        'harness_path':str(OWN/'harness/quicktest3_isolated.py'),'harness_sha256':sha(OWN/'harness/quicktest3_isolated.py')}
save(folder/'api_process.json',record)
print('OWN_API_PROCESS',os.getpid(),qid,variant,flush=True)
sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',qid,
          '--image',str(folder/'candidate.png'),'--design',str(folder/'design.json'),'--output',str(folder/'tests'),'--runs','2']
try:
    runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
except BaseException as e:
    save(folder/'api_process_finished.json',{'pid':os.getpid(),'finished_at_utc':datetime.now(timezone.utc).isoformat(),'status':'launcher_exception','error_type':type(e).__name__,'error':str(e)})
    raise
else:
    save(folder/'api_process_finished.json',{'pid':os.getpid(),'finished_at_utc':datetime.now(timezone.utc).isoformat(),'status':'harness_returned'})
