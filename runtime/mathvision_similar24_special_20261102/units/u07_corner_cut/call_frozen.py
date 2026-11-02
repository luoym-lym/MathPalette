from worker_env import *
import argparse
import runpy
import re

p=argparse.ArgumentParser();p.add_argument('question',choices=['Plane194','Plane245']);p.add_argument('variant');a=p.parse_args()
qid=a.question
assert re.fullmatch(r'r0[23]_[a-z_]+',a.variant)
directory=OWN/qid/a.variant
assert read(directory/'primary_review.json')['proceed_to_exact_two_calls']
replay=read(directory/'independent_process_replay.json')
assert replay['exact_candidate_bytes_equal'] and replay['source_still_eligible']['eligible']
design=read(directory/'design.json');assert design['question_id']==qid
frozen={'image':sha(directory/'candidate.png'),'plugin':sha(directory/'plugin.json'),'design':sha(directory/'design.json')}
assert frozen['image']==design['image_sha256'] and frozen['plugin']==design['plugin_sha256']
assert replay['design_sha256']==frozen['design']
for prior in OWN.rglob('api_process.json'):
    assert (prior.parent/'api_process_finished.json').exists(),'Prior own API process not finished'
for prior in OWN.rglob('summary.json'):
    if '/tests/' in prior.as_posix():
        assert all(x['status']=='completed' for x in read(prior)['results']),'Earlier API failure prohibits later calls'
for prior in OWN.rglob('design.json'):
    if prior.parent==directory:continue
    assert read(prior).get('image_sha256')!=frozen['image'],'Exact prior PNG must not be retested'
global_history=read(TASK/'history_index.json')
for h in global_history['questions']:
    for d in h.get('designs',[]):
        assert d.get('frozen_candidate_png_sha256')!=frozen['image'],'Exact old PNG must not be retested'
write(directory/'global_prior_png_audit.json',{'at':now(),'history_index_sha256':sha(TASK/'history_index.json'),
       'exact_old_or_own_candidate_png_collisions':[],'previous_started_runs_this_candidate':0,
       'prior_tests_not_counted_for_this_pair':True},True)
write(directory/'api_process.json',{'started_at':now(),'pid':os.getpid(),'argv':sys.argv,'script_sha256':sha(Path(__file__)),
      'runs':2,'frozen':frozen,'no_provider_or_model_change':True},True)
e=eligibility(qid);assert e['eligible'];write(directory/'eligibility_immediately_before_calls.json',e,True)
counter=0
def each_actual_request(event,args):
    global counter
    if event!='urllib.Request':return
    counter+=1
    assert counter<=2,'Third request forbidden'
    assert str(args[0])=='https://token-plan-cn.xiaomimimo.com/v1/chat/completions'
    e=eligibility(qid);assert e['eligible']
    assert frozen=={'image':sha(directory/'candidate.png'),'plugin':sha(directory/'plugin.json'),'design':sha(directory/'design.json')}
    data=args[1];body=json.loads(data);content=body['messages'][1]['content']
    assert content[0]=={'type':'text','text':e['formal_record']['question']}
    assert len(content)==2 and len(body['messages'])==2
    import base64
    assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==(directory/'candidate.png').read_bytes()
    assert body['model']=='mimo-v2.6-flash' and body['thinking']=={'type':'disabled'} and body['stream'] is False
    assert set(body)=={'model','stream','thinking','messages'}
    write(directory/f'eligibility_at_actual_request_{counter:02d}.json',{'checked_at':now(),'request_number':counter,
       'request_body_sha256':hashlib.sha256(data).hexdigest(),'exact_formal_text_and_frozen_PNG_only':True,'eligibility':e},True)
    checkpoint=read(OWN/'checkpoint.json');checkpoint['updated_at']=now()
    checkpoint['status']='running_original_quicktest3_exact_pair'
    checkpoint['new_API_calls']=len(list(OWN.rglob('run_*_started.json')))
    checkpoint['questions'][qid]={'status':'pair_running','variant_id':a.variant,'candidate_directory':str(directory),
      'expected_wrong_answer':design['expected_wrong_answer'],'current_pair_requests_started':counter}
    write(OWN/'checkpoint.json',checkpoint)
sys.addaudithook(each_actual_request)
sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',qid,
          '--image',str(directory/'candidate.png'),'--design',str(directory/'design.json'),
          '--output',str(directory/'tests'),'--runs','2']
error=None
try:runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
except BaseException as exc:
    error={'type':type(exc).__name__,'message':str(exc)}
    raise
finally:
    write(directory/'api_process_finished.json',{'finished_at':now(),'pid':os.getpid(),'actual_urllib_requests':counter,
      'exception':error,'runner_returned':error is None,'no_child_processes_started':True},True)
