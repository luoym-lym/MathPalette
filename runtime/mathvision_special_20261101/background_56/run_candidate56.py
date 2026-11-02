from env56 import *
import runpy

qid=sys.argv[1]
candidate=next(r for r in read(OWN/'prepared_candidates.json') if r['question_id']==qid)
dest=Path(candidate['path'])
assert sha(dest/'design.json')==candidate['design_sha256']
assert sha(dest/'candidate.png')==candidate['image_sha256']
review=read(dest/'primary_pretest_review.json')
assert review['actually_viewed_frozen_native_PNG'] and review['primary_all_mark_roles_readable']
e=eligibility(qid)
assert e['eligible'],e['reasons']
save(dest/'eligibility_immediately_before_calls.json',e)
assert not (dest/'api_process.json').exists(), 'Never relaunch an API candidate'
save(dest/'api_process.json',{'started_at':now(),'pid':os.getpid(),'command_argv':sys.argv[:],'python':sys.executable,'profile':'original quicktest3 mimo-v2.6-flash thinking.disabled','runs':2,'design_sha256':sha(dest/'design.json'),'image_sha256':sha(dest/'candidate.png'),'own_strict_guard':True,'no_retry':True})
script=OWN/'harness/quicktest3_isolated.py'
sys.argv=[str(script),'--branch','PlaneGeometry','--question',qid,'--image',str(dest/'candidate.png'),'--design',str(dest/'design.json'),'--output',str(dest/'tests'),'--runs','2']
try:
    runpy.run_path(str(script),run_name='__main__')
except BaseException as err:
    save(dest/'api_process_exception.json',{'at':now(),'pid':os.getpid(),'type':type(err).__name__,'error':str(err),'no_retry':True})
    raise
finally:
    save(dest/'api_process_finished.json',{'at':now(),'pid':os.getpid(),'normal_python_finally_reached':True,'design_still_frozen':sha(dest/'design.json')==candidate['design_sha256'],'image_still_frozen':sha(dest/'candidate.png')==candidate['image_sha256']})
