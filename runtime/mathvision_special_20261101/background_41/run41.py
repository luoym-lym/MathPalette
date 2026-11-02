from env41 import *
q=sys.argv[1];assert q in ASSIGNED
ds=list((HERE/q).glob('r41_*/design.json'));assert len(ds)==1
out=ds[0].parent;assert read(out/'primary_review.json')['proceed_to_API'];assert not (out/'api_process.json').exists()
d=read(ds[0]);assert file_hash(out/'candidate.png')==d['png_sha256'];assert file_hash(out/'plugin.json')==d['plugin_sha256']
e=eligibility(q);assert e['eligible'];write(out/'eligibility_immediately_before_calls.json',e)
h=harness()
write(out/'harness_context.json',{'source':str(BASE/'harness/quicktest3_isolated.py'),'source_sha256':file_hash(BASE/'harness/quicktest3_isolated.py'),'copy':h.__file__,'copy_sha256':file_hash(h.__file__),'unchanged_bytes':True,'only_context_rebound':['PROJECT','RUNTIME'],'cache_root':str(h.HARNESS),'model_profile_systemprompt_thinking_timeout_tokens_API_config_unchanged':True})
write(out/'api_process.json',{'pid':os.getpid(),'executable':sys.executable,'args':sys.argv,'started_at_utc':now(),'runs':2,'automatic_retries':0})
try:
    result=h.run_tests('PlaneGeometry',q,out/'candidate.png',out/'design.json',out/'tests',2)
    write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at_utc':now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir'],'process_done':True})
except BaseException as err:
    write(out/'api_process_exception.json',{'pid':os.getpid(),'finished_at_utc':now(),'type':type(err).__name__,'error':str(err),'retry':False});raise
