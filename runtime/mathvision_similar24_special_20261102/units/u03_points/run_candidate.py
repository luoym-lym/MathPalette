from unit_env import *
import runpy
import base64

folder=Path(sys.argv[1]).resolve()
assert folder.is_relative_to(OWN)
assert not (OWN/'API_STOP.json').exists(),'Previous host/API error stops all later calls in this unit'
assert not list(folder.glob('tests/**/run_*_started.json')),'Already started; never retry same candidate'
design=read(folder/'design.json')
qid=design['question_id']
assert qid in QIDS
assert read(folder/'independent_replay.json')['exact_replay']
assert read(folder/'primary_review_before_calls.json')['ready_for_exact_two_calls']
assert sha((folder/'candidate.png').read_bytes())==design['candidate_sha256']
initial_design=sha((folder/'design.json').read_bytes())
initial_plugin=sha((folder/'plugin.json').read_bytes())
save(folder/'api_process_started.json',{'created_at':now(),'pid':os.getpid(),'argv':sys.argv,
     'harness':str(OWN/'harness/quicktest3_isolated.py'),'requested_runs':2,
     'four_numerical_threads':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS')}})

calls=[]
def before_send(event,args):
    if event!='urllib.Request': return
    assert len(calls)<2,'No third actual request'
    current=eligibility(qid)
    assert current['eligible'],'Source or qualification changed immediately before call'
    assert sha((folder/'design.json').read_bytes())==initial_design
    assert sha((folder/'plugin.json').read_bytes())==initial_plugin
    payload=json.loads(args[1])
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'}
    assert payload['messages'][1]['content'][0]=={'type':'text','text':current['record']['question']}
    content=payload['messages'][1]['content']
    assert len(content)==2
    image_bytes=base64.b64decode(content[1]['image_url']['url'].split(',',1)[1])
    assert sha(image_bytes)==design['candidate_sha256']
    audit={'created_at':now(),'call_index':len(calls)+1,'request_body_sha256':sha(args[1]),
           'image_sha256':sha(image_bytes),'design_sha256':initial_design,'eligibility':current,
           'exact_formal_question_and_same_PNG_only':True,'max_tokens_absent':True}
    save(folder/f'eligibility_immediately_before_call_{len(calls)+1}.json',audit)
    calls.append(audit['request_body_sha256'])

sys.addaudithook(before_send)
harness=OWN/'harness/quicktest3_isolated.py'
sys.argv=[str(harness),'--branch','PlaneGeometry','--question',qid,'--image',str(folder/'candidate.png'),
          '--design',str(folder/'design.json'),'--output',str(folder/'tests'),'--runs','2']
error=None
try:
    runpy.run_path(str(harness),run_name='__main__')
    summary_path=next(folder.glob('tests/*/summary.json'))
    summary=read(summary_path)
    if not summary['two_completed']:
        save(OWN/'API_STOP.json',{'created_at':now(),'folder':str(folder),'summary':str(summary_path),
                                'reason':'Actual API/transport failed; all later unit requests stopped'})
except BaseException as exc:
    error=repr(exc)
    save(OWN/'API_STOP.json',{'created_at':now(),'folder':str(folder),'reason':error,
         'actual_urllib_send_events':len(calls),'no_retry':True})
    raise
finally:
    save(folder/'api_process_finished.json',{'created_at':now(),'pid':os.getpid(),
        'actual_urllib_send_events':len(calls),'request_sha256':calls,'error':error,
        'harness_returned_or_raised':True,'subprocesses_started_by_wrapper':0})
