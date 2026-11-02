from worker_env import *
import argparse
import runpy

p=argparse.ArgumentParser();p.add_argument('question',choices=['Plane194','Plane245']);a=p.parse_args()
qid=a.question
variant={'Plane194':'r01_fold_axes_to_square_hole','Plane245':'r01_fold_motion_to_square_aperture'}[qid]
directory=OWN/qid/variant
assert read(directory/'primary_review.json')['proceed_to_exact_two_calls']
replay=read(directory/'independent_process_replay.json')
assert replay['exact_candidate_bytes_equal'] and replay['source_still_eligible']['eligible']
design=read(directory/'design.json')
for name,key in [('candidate.png','image_sha256'),('plugin.json','plugin_sha256')]:
    assert sha(directory/name)==design[key]
frozen={'image':sha(directory/'candidate.png'),'plugin':sha(directory/'plugin.json'),'design':sha(directory/'design.json')}
assert replay['design_sha256']==frozen['design']
write(directory/'api_process.json',{'started_at':now(),'pid':os.getpid(),'argv':sys.argv,'runs':2,'frozen':frozen},True)
global_history=read(TASK/'history_index.json')
collisions=[]
for h in global_history['questions']:
    for d in h.get('designs',[]):
        if d.get('frozen_candidate_png_sha256')==frozen['image']:
            collisions.append({'question_id':h['question_id'],'directory':d['directory']})
assert not collisions
write(directory/'global_prior_png_audit.json',{'at':now(),'history_index_sha256':sha(TASK/'history_index.json'),
       'exact_png_collisions':collisions,'previous_started_runs_this_candidate':0,
       'different_formal_question_requests_not_counted':True},True)
write(directory/'eligibility_immediately_before_calls.json',eligibility(qid),True)
counter=0
def each_actual_request(event,args):
    global counter
    if event!='urllib.Request':return
    counter+=1
    assert counter<=2,'Third request forbidden'
    assert str(args[0])=='https://token-plan-cn.xiaomimimo.com/v1/chat/completions'
    e=eligibility(qid);assert e['eligible']
    assert frozen=={'image':sha(directory/'candidate.png'),'plugin':sha(directory/'plugin.json'),'design':sha(directory/'design.json')}
    data=args[1]
    body=json.loads(data)
    content=body['messages'][1]['content']
    assert content[0]=={'type':'text','text':e['formal_record']['question']}
    assert len(content)==2 and len(body['messages'])==2
    import base64
    assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])==(directory/'candidate.png').read_bytes()
    assert body['model']=='mimo-v2.6-flash' and body['thinking']=={'type':'disabled'} and body['stream'] is False
    assert set(body)=={'model','stream','thinking','messages'}
    write(directory/f'eligibility_at_actual_request_{counter:02d}.json',{'checked_at':now(),'request_number':counter,
       'request_body_sha256':hashlib.sha256(data).hexdigest(),'exact_formal_text_and_frozen_PNG_only':True,
       'eligibility':e},True)
sys.addaudithook(each_actual_request)
checkpoint=read(OWN/'checkpoint.json')
checkpoint.update(updated_at=now(),status='running_original_quicktest3_exact_pair')
checkpoint['questions'][qid]={'status':'pair_running','candidate_directory':str(directory),'expected_wrong_answer':design['expected_wrong_answer']}
write(OWN/'checkpoint.json',checkpoint)
sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','PlaneGeometry','--question',qid,
          '--image',str(directory/'candidate.png'),'--design',str(directory/'design.json'),
          '--output',str(directory/'tests'),'--runs','2']
error=None
try:
    runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
except BaseException as exc:
    error={'type':type(exc).__name__,'message':str(exc)}
    raise
finally:
    write(directory/'api_process_finished.json',{'finished_at':now(),'pid':os.getpid(),
       'actual_urllib_requests':counter,'exception':error,'runner_returned':error is None,'no_child_processes_started':True},True)
