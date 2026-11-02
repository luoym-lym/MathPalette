from local_env import *
from api_gate import check_eligibility, check_frozen
import argparse, json, runpy, hashlib, traceback

ap=argparse.ArgumentParser()
ap.add_argument('qid')
ap.add_argument('--runs',type=int,choices=[2],required=True)
ap.add_argument('--variant')
args=ap.parse_args()
qid=args.qid
entries=read_json(OWN/'primary_design_manifest.json')
if (OWN/'supplementary_design_manifest.json').exists(): entries+=read_json(OWN/'supplementary_design_manifest.json')
entry=next(x for x in entries if x['question_id']==qid and (args.variant is None or x['variant_id']==args.variant))
candidate=Path(entry['candidate_directory'])
assert not (OWN/'batch_api_halt.json').exists(), 'Earlier host/API failure ends this batch; no subsequent call'
assert not list(candidate.rglob('run_*_started.json')), 'Already started this frozen candidate; no resume or third call'
assert not (candidate/'api_process.json').exists(), 'Frozen invocation must not be restarted'
design=check_frozen(candidate)
branch=read_json(OWN/qid/'formal_record.json')['id']
branch='SolidGeometry' if qid.startswith('Solid') else 'PlaneGeometry'
ev=check_eligibility(qid,'immediately_before_invocation')
save(candidate/'eligibility_before_invocation.json',ev,True)
assert ev['eligible'],ev['reasons']
harness=OWN/'ownruntime/harness/quicktest3_isolated.py'
prov=read_json(harness.parent/'routing_provenance.json')
assert sha(harness)==prov['routed_sha256'] and sha(OLD/'harness/quicktest3_isolated.py')==prov['source_sha256']
save(candidate/'api_process.json',{'pid':os.getpid(),'started_at':now(),'command':sys.argv,
    'profile':'original quicktest3','requested_runs':2,'source_harness_sha256':prov['source_sha256'],
    'routed_harness_sha256':prov['routed_sha256'],'strict_writeguard':str(OWN),
    'threads':{x:os.environ[x] for x in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']}},True)

requests_seen=0
def before_network(event, audit_args):
    global requests_seen
    if event!='urllib.Request':return
    requests_seen+=1
    assert requests_seen<=2, 'Third request forbidden'
    check_frozen(candidate)
    eligibility=check_eligibility(qid,'before_actual_call_'+str(requests_seen))
    save(candidate/f'eligibility_before_actual_call_{requests_seen:02d}.json',eligibility,True)
    assert eligibility['eligible'],eligibility['reasons']
    # Read only the payload; never persist or print credential-bearing headers.
    fullurl,data,_headers,method=audit_args
    payload=json.loads(data)
    formal=eligibility['formal_record']
    assert payload['messages'][1]['content'][0]=={'type':'text','text':formal['question']}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'}
    assert not any(k in payload for k in ['max_tokens','max_completion_tokens'])
    assert len(payload['messages'])==2 and len(payload['messages'][1]['content'])==2
    bindings=list((candidate/'tests').glob('*/binding.json'));assert len(bindings)==1
    binding=read_json(bindings[0])
    assert hashlib.sha256(data).hexdigest()==binding['request_body_sha256']
    assert binding['image_sha256']==sha(candidate/'candidate.png')
    save(candidate/f'actual_call_{requests_seen:02d}_payload_gate.json',{'checked_at':now(),'pid':os.getpid(),
       'formal_text_exact':True,'frozen_image_and_design_exact':True,'payload_sha256':hashlib.sha256(data).hexdigest(),
       'original_payload_and_profile_unchanged':True,'request_index':requests_seen,'headers_saved':False},True)

sys.addaudithook(before_network)
sys.argv=[str(harness),'--branch',branch,'--question',qid,'--image',str(candidate/'candidate.png'),
          '--design',str(candidate/'design.json'),'--output',str(candidate/'tests'),'--runs','2']
status='unknown';error=None
try:
    runpy.run_path(str(harness),run_name='__main__')
    summaries=list((candidate/'tests').glob('*/summary.json'))
    assert len(summaries)==1
    summary=read_json(summaries[0])
    status='completed' if summary['two_completed'] else 'api_error_or_incomplete'
    if status!='completed':
        save(OWN/'batch_api_halt.json',{'halted_at':now(),'question_id':qid,'reason':status,
             'summary':str(summaries[0]),'no_remaining_candidate_requests':True},True)
except BaseException as exc:
    status='wrapper_or_host_exception'
    error={'type':type(exc).__name__,'message':str(exc),'traceback':traceback.format_exc()}
    if not (OWN/'batch_api_halt.json').exists():
        save(OWN/'batch_api_halt.json',{'halted_at':now(),'question_id':qid,'reason':status,
             'error':error,'requests_seen':requests_seen,'no_remaining_candidate_requests':True},True)
    raise
finally:
    save(candidate/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'status':status,
         'actual_network_requests_seen':requests_seen,'local_child_processes_started':[],'error':error},True)
    cp=read_json(OWN/'checkpoint.json')
    cp['updated_at']=now();cp['phase']='testing_or_reviewing'
    cp['questions'][qid]['status']=status
    cp['questions'][qid]['calls']=len(list((OWN/qid).glob('*/actual_call_*_payload_gate.json')))
    cp['new_actual_calls']=len(list(OWN.glob('*/*/actual_call_*_payload_gate.json')))
    save(OWN/'checkpoint.json',cp)
    print(json.dumps({'question_id':qid,'status':status,'actual_requests':requests_seen,'pid':os.getpid()},ensure_ascii=False),flush=True)
