from bootstrap import *
import runpy
vid=sys.argv[1];d=OWN/'Plane213'/vid;g=read(d/'prelaunch_gate.json')
assert not (d/'tests').exists()
assert g['PNG_sha256']==sha(d/'candidate.png') and g['design_sha256']==sha(d/'design.json')
for p,h in g['frozen_candidate_artifact_hashes'].items():assert sha(p)==h
run_counter=0
def precall(event,args):
    global run_counter
    if event!='urllib.Request':return
    run_counter+=1
    assert run_counter<=2
    assert args[0].endswith('/chat/completions')
    # No header/credential is inspected or recorded. This hook changes no network data.
    eligibility_snapshot=eligibility()
    assert sha(d/'candidate.png')==g['PNG_sha256'] and sha(d/'design.json')==g['design_sha256']
    save(d/f'eligibility_immediately_before_run_{run_counter:02d}.json',{'at_utc':now(),'actual_attempt_index':run_counter,'current_eligibility':eligibility_snapshot,'image_sha256':g['PNG_sha256'],'design_sha256':g['design_sha256'],'request_body_sha256':hashlib.sha256(args[1]).hexdigest(),'remote_payload_untouched':True})
    checkpoint=read(OWN/'checkpoint.json')
    checkpoint.update(at_utc=now(),status='frozen_pair_running',current_pair_actual_calls_started=run_counter,active_owned_API_requests=1)
    save('checkpoint.json',checkpoint,replace=True)
sys.addaudithook(precall)
save(d/'pair_process_started.json',{'at_utc':now(),'pid':os.getpid(),'argv':sys.argv,'permitted_actual_calls':2})
checkpoint=read(OWN/'checkpoint.json')
checkpoint.update(at_utc=now(),status='frozen_pair_running',current_pair_actual_calls_started=0,candidate_directory=str(d),second_review_queue=read(OWN/'second_review_queue.json'))
save('checkpoint.json',checkpoint,replace=True)
sys.argv=['quicktest3_isolated.py','--branch','PlaneGeometry','--question','Plane213','--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
save(d/'pair_process_finished.json',{'at_utc':now(),'pid':os.getpid(),'finished':True,'actual_request_attempts':run_counter})
