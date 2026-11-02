from env54 import *
import runpy

q,name=sys.argv[1:3]
root=OWN/q/name
assert q in read(BASE/'background_54_assignment.json')['question_ids']
assert not list(OWN.glob('**/run_*.json')) or not any(read(p).get('status')=='error' for p in OWN.glob('**/run_*.json') if not p.name.endswith('_started.json')),'External error already occurred: STOP'
assert not list((root/'tests').glob('*/binding.json')),'No repeat calls on frozen candidate'
assert read(root/'primary_review.json')['ready_for_exactly_two_calls']
d=read(root/'design.json')
assert sha(root/'candidate.png')==d['image_sha256']
e=eligibility(q);save(root/'eligibility_immediately_before_calls.json',e);assert e['eligible']
save(root/'api_process.json',{'pid':os.getpid(),'executable':sys.executable,'original_args':sys.argv,'started_at':now(),'cwd':os.getcwd(),'no_profile_effort_token_timeout_overrides':True})
sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',q,'--image',str(root/'candidate.png'),'--design',str(root/'design.json'),'--output',str(root/'tests'),'--runs','2']
try:
    runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
finally:
    save(root/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'harness_returned_or_raised':True,'retry':False})
