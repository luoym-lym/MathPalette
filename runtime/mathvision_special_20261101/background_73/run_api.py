from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,eligibility,stamp
from prepare import SPECS
from pathlib import Path
import os,sys,runpy,json

q=sys.argv[1]
assert q in SPECS
s=SPECS[q]
d=HERE/q/s['id']
assert not (HERE/'EXTERNAL_STOP.json').exists(),'A previous external failure forbids subsequent calls'
assert not (d/'api_process.json').exists(),'No repeat invocation of a frozen image'
assert read(HERE/'frozen_images_zero_prior_request_audit.json')['new_images_zero_prior_exact_requests']
assert read(d/'primary_review.json')['candidate_sha256']==sha(d/'candidate.png')
assert read(d/'offline_replay_audit.json')['fresh_offline_byte_identity']
assert sha(d/'offline_replay.png')==sha(d/'candidate.png')==read(d/'design.json')['candidate_png_sha256']
eligibility(q,'eligibility_immediately_before_calls.json')
checked=[]
for e in read(HERE/'frozen_sources_initial.json')+read(HERE/'helper_hashes_before_render.json'):
    p=Path(e['path'])
    h=sha(p)
    assert h==e['sha256'],str(p)
    checked.append({'path':str(p),'sha256':h})
for e in read(HERE/q/'old_evidence_manifest.json'):
    assert sha(Path(e['path']))==e['sha256'],e['path']
save(d/'pre_API_frozen_hash_audit.json',{'time':stamp(),'formal_source_and_helper_hashes':checked,'all_scoped_old_evidence_hash_exact':True,'design_sha256':sha(d/'design.json'),'plugin_sha256':sha(d/'plugin.json'),'PNG_sha256':sha(d/'candidate.png'),'remote_calls_before_this_invocation':0,'exactly_two_requested':True})
harness=HERE/'harness/quicktest3_isolated.py'
assert sha(harness)==read(HERE/'harness_byte_diff_audit.json')['relocated_sha256']
argv=[str(harness),'--branch','SolidGeometry','--question',q,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
save(d/'api_process.json',{'pid':os.getpid(),'parent_pid':os.getppid(),'python_executable':sys.executable,'original_argv':sys.argv,'harness_argv':argv,'created_at':stamp(),'only_owned_process':True,'no_third_call_retry_or_profile_override':True})
sys.argv=argv
status='unknown'
actual_request_gates=[]
def before_network(event,args):
    if event!='urllib.Request':return
    # Never serialize event arguments: headers contain the private credential.
    index=len(actual_request_gates)+1
    assert index<=2,'Third actual request forbidden'
    eligibility(q,f'eligibility_before_actual_call_{index:02d}.json')
    for e in read(HERE/'frozen_sources_initial.json')+read(HERE/'helper_hashes_before_render.json'):
        assert sha(Path(e['path']))==e['sha256'],e['path']
    assert sha(d/'candidate.png')==read(d/'design.json')['candidate_png_sha256']
    assert sha(d/'design.json')==read(d/'design_difference_audit.json')['design_sha256']
    actual_request_gates.append({'call':index,'time':stamp(),'fresh_authoritative_eligibility_approval_source_and_design_hashes_pass':True,'credential_event_arguments_not_recorded':True})
    save(d/f'actual_call_{index:02d}_gate.json',actual_request_gates[-1])
sys.addaudithook(before_network)
try:
    namespace=runpy.run_path(str(harness),run_name='__main__')
    summaries=list((d/'tests').rglob('summary.json'))
    assert len(summaries)==1
    summary=read(summaries[0])
    status='two_completed' if summary['two_completed'] else 'incomplete_or_error'
    if status!='two_completed':
        save(HERE/'EXTERNAL_STOP.json',{'time':stamp(),'question_id':q,'summary':str(summaries[0]),'reason':'Original harness did not complete both calls; no retry or subsequent calls allowed','results':summary['results']})
except BaseException as e:
    status='local_or_execution_exception'
    save(d/'execution_exception.json',{'time':stamp(),'type':type(e).__name__,'detail':str(e),'no_retry':True})
    if not (HERE/'EXTERNAL_STOP.json').exists():save(HERE/'EXTERNAL_STOP.json',{'time':stamp(),'question_id':q,'reason':'Execution exception; preserve all starts/raw and stop subsequent calls','exception_type':type(e).__name__})
    raise
finally:
    save(d/'api_process_finished.json',{'pid':os.getpid(),'finished_at':stamp(),'status':status,'actual_network_request_gates':actual_request_gates,'synchronous_process_exiting':True,'no_owned_background_request_process_spawned':True})
