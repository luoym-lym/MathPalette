from tools24 import *
q=sys.argv[1];out=next(p.parent for p in (HERE/q).glob('r24_*/design.json') if (p.parent/'primary_review.json').exists() and read(p.parent/'primary_review.json').get('proceed_to_API') and not (p.parent/'api_process.json').exists())
assert read(out/'primary_review.json')['proceed_to_API']
e=eligibility(q);assert e['eligible'];write(out/'eligibility_immediately_before_calls.json',e)
h=harness()
write(out/'harness_context.json',{'source':str(BASE/'harness/quicktest3_isolated.py'),'source_sha256':file_hash(BASE/'harness/quicktest3_isolated.py'),'copy':h.__file__,'copy_sha256':file_hash(h.__file__),'unchanged_bytes':True,'only_context_rebound':['PROJECT','RUNTIME'],'cache_root':str(h.HARNESS),'profile_timeout_tokens_prompt_unchanged':True})
write(out/'api_process.json',{'pid':os.getpid(),'executable':sys.executable,'args':sys.argv,'started_at':now(),'run_count':2,'automatic_retries':0})
try:
    r=h.run_tests('PlaneGeometry',q,out/'candidate.png',out/'design.json',out/'tests',2)
    write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':r['two_completed'],'evidence_dir':r['evidence_dir'],'process_done':True})
except BaseException as err:
    write(out/'api_process_exception.json',{'pid':os.getpid(),'finished_at':now(),'type':type(err).__name__,'error':str(err),'retry':False})
    raise
