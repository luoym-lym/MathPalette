from own_bootstrap import *
from unit_tools import eligibility,snapshot
import runpy
import traceback

directory=Path(sys.argv[1]).resolve()
check_write(directory)
qid=load(directory/'design.json')['question_id']
assert qid=='Solid166'
gate=load(directory/'render_gate.json')
replay=load(directory/'independent_replay_gate.json')
assert gate['candidate_png_sha256']==replay['candidate_png_sha256']==sha(directory/'candidate.png')
assert gate['plugin_sha256']==replay['plugin_sha256']==sha(directory/'plugin.json')
assert gate['design_sha256']==replay['design_sha256']==sha(directory/'design.json')
assert gate['pid']!=replay['pid']
assert load(directory/'primary_visual_review.json')['eligible_for_exact_two_calls']
assert snapshot()==gate['source']==load(OWN/'readonly_execution_source_initial.json')
for rel,v in load(OWN/'read_source_manifest.json').items():
    assert sha(PROJECT/rel)==v['sha256'],rel
history=load(TASK/'history_index.json')
same=[]
for q in history['questions']:
    for d in q.get('designs',[]):
        if d.get('frozen_candidate_png_sha256')==gate['candidate_png_sha256']:
            same.append({'question_id':q['question_id'],'design_path':d['design_path'],'calls':d['unique_started_call_count_from_saved_records']})
assert not same,'Prior PNG collision: stop, audit, do not retest'
# Only one two-run invocation can ever be launched for the frozen candidate.
if (directory/'tests').exists():
    assert not list((directory/'tests').rglob('*started.json')),'A real prior request exists: no repeat'
save(directory/'launch_preflight.json',{'timestamp':now(),'eligibility':eligibility(qid),
   'image_sha256':sha(directory/'candidate.png'),'design_sha256':sha(directory/'design.json'),
   'old_global_saved_hash_collisions':same,'all_read_source_hashes_unchanged':True,
   'renderer_sources_unchanged':True,'schema_noop_repeat_replay_visual_and_preset_passed':True},exclusive=True)
process={'pid':os.getpid(),'script':str(Path(__file__).resolve()),'candidate_directory':str(directory),
         'started_at':now(),'ended_at':None,'network_requests':0,'status':'running','network_gate_records':[]}
save(directory/'own_api_process.json',process,exclusive=True)
network_count=0
def before_network(event,args):
    global network_count
    if event!='urllib.Request':return
    url=args[0]
    if not isinstance(url,str) or not url.endswith('/chat/completions'):return
    network_count+=1
    if network_count>2:
        raise RuntimeError('Exact two network requests exceeded; no third call')
    current=eligibility(qid)
    assert snapshot()==gate['source']
    assert sha(directory/'candidate.png')==gate['candidate_png_sha256']
    assert sha(directory/'design.json')==gate['design_sha256']
    assert sha(directory/'plugin.json')==gate['plugin_sha256']
    evidence=directory/'tests'/f'pre_network_run_{network_count:02d}.json'
    save(evidence,{'request_index':network_count,'timestamp':now(),'eligibility':current,
          'image_sha256':gate['candidate_png_sha256'],'design_sha256':gate['design_sha256'],
          'request_body_sha256':hashlib.sha256(args[1]).hexdigest(),
          'source_frozen':True,'credentials_logged':False},exclusive=True)
    process.update(network_requests=network_count)
    process['network_gate_records'].append(str(evidence))
    save(directory/'own_api_process.json',process)
    cp=load(OWN/'checkpoint.json');cp.update(phase='quicktest3_in_progress',updated_at=now())
    cp['new_actual_calls']=sum(load(p).get('network_requests',0) for p in OWN.rglob('own_api_process.json'))
    cp['questions'][qid].update(status='quicktest3_in_progress',candidate_directory=str(directory),calls=network_count)
    cp['own_processes']=[process]
    save(OWN/'checkpoint.json',cp)

sys.addaudithook(before_network)
sys.argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','SolidGeometry','--question',qid,
          '--image',str(directory/'candidate.png'),'--design',str(directory/'design.json'),
          '--output',str(directory/'tests'),'--runs','2']
try:
    runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
    process['status']='harness_returned'
except BaseException as error:
    process['status']='exception'
    process['exception_type']=type(error).__name__
    # No secret value or request Authorization headers are logged by this wrapper.
    save(directory/'local_wrapper_error.json',{'type':type(error).__name__,'message':str(error),'traceback':traceback.format_exc()},exclusive=True)
    raise
finally:
    process.update(ended_at=now(),network_requests=network_count)
    save(directory/'own_api_process.json',process)
    cp=load(OWN/'checkpoint.json');cp.update(phase='awaiting_manual_full_response_read',updated_at=now())
    cp['new_actual_calls']=sum(load(p).get('network_requests',0) for p in OWN.rglob('own_api_process.json'))
    cp['own_processes']=[load(p) for p in OWN.rglob('own_api_process.json')]
    cp['questions'][qid].update(status='awaiting_manual_full_response_read',calls=network_count)
    save(OWN/'checkpoint.json',cp)
