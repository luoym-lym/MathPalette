import env
from env import OWN
from prepare import read,dump,sha,eligibility
import sys,os,json,runpy
from datetime import datetime,timezone

if __name__=='__main__':
    qid,name=sys.argv[1:3];root=OWN/qid/name
    assert qid in ['Plane400','Plane401','Plane402','Plane405','Plane407','Plane409','Plane410','Plane412']
    assert not list((root/'tests').glob('*/binding.json')),'Never repeat an invocation'
    primary=read(root/'primary_review.json');assert primary['ready_for_exactly_two_calls']
    design=read(root/'design.json');checks=read(root/'render_check.json')
    assert sha(root/'candidate.png')==design['image_sha256']==checks['candidate_sha256']
    e=eligibility(qid);assert e['eligible'];dump(root/'eligibility_immediately_before_calls.json',e)
    dump(root/'api_process.json',{'pid':os.getpid(),'executable':sys.executable,'command_args':sys.argv,'created_at':datetime.now(timezone.utc).isoformat(),'cwd':os.getcwd(),'profile_unchanged':True})
    sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',qid,'--image',str(root/'candidate.png'),'--design',str(root/'design.json'),'--output',str(root/'tests'),'--runs','2']
    try:
        runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
    finally:
        dump(root/'api_process_finished.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'note':'Harness returned or raised; process is exiting. No retry.'})
