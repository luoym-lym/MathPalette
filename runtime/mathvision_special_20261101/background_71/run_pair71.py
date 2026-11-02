from env71 import *
import runpy

assert not (OWN/'local_failure.json').exists()
assert not (OWN/'api_process_started.json').exists(), 'Never retry an existing pair process'
ready=read(OWN/'preflight_ready.json')
assert ready['ready_for_exact_runs2']
c=read(OWN/'prepared_candidates.json')[0]
dest=Path(c['path'])
for q in QIDS:
    e=eligibility(q)
    assert e['eligible']
    save(f'{q}/eligibility_immediately_before_pair.json',e)
assert sha(dest/'candidate.png')==c['image_sha256'] and sha(dest/'design.json')==c['design_sha256']
original=(BASE/'harness/quicktest3_isolated.py').read_bytes()
audit=read(OWN/'harness_isolation_audit.json')
assert hashlib.sha256(original).hexdigest()==audit['reference_sha256']
assert sha(OWN/'harness/quicktest3_isolated.py')==audit['own_sha256']
argv=[str(OWN/'harness/quicktest3_isolated.py'),'--branch','SolidGeometry','--question','Solid120','--image',str(dest/'candidate.png'),'--design',str(dest/'design.json'),'--output',str(dest/'tests'),'--runs','2']
save('api_process_started.json',{'at':now(),'pid':os.getpid(),'executable':sys.executable,'launcher_argv':sys.argv[:],'harness_argv':argv,'expected_calls':2,'same_frozen_image':c['image_sha256'],'same_frozen_design':c['design_sha256'],'no_retry':True})
save('checkpoint.json',{'unit':'background_71','stage':'exact_pair_in_progress','scope':QIDS,'assessed_question_ids':QIDS,'unworked_question_ids':[],'reasoned_skips':['Solid138','Solid169','Solid213','Solid215'],'new_design_count':1,'own_API_PID':os.getpid(),'evidence_root':str(dest),'no_retry':True})
sys.argv=argv
try:
    runpy.run_path(argv[0],run_name='__main__')
except BaseException as exc:
    save('pair_launcher_failure.json',{'at':now(),'pid':os.getpid(),'error_type':type(exc).__name__,'error':str(exc),'no_retry':True,'stop_subsequent_calls':True})
    raise
finally:
    save('api_process_finished.json',{'at':now(),'pid':os.getpid(),'harness_returned_or_raised':True,'no_further_requests_by_this_process':True})
