from tools33 import *
import importlib.util
q,vid=sys.argv[1:3];out=HERE/q/vid
assert q in ASSIGNED and vid.startswith('r33_')
check=eligibility(q);assert check['eligible'];write(out/'eligibility_immediately_before_calls.json',check)
review=read(out/'primary_review.json');assert review['actual_native_candidate_png_viewed'] and review['proceed_to_API']
d=read(out/'design.json');assert d['image_sha256']==file_hash(out/'candidate.png') and d['plugin_sha256']==file_hash(out/'plugin.json')
assert not (out/'tests').exists(),'No unchanged repeat permitted'
write(out/'api_process.json',{'pid':os.getpid(),'parent_pid':os.getppid(),'executable':sys.executable,'argv':sys.argv,'started_at':now()})
p=BASE/'harness/quicktest3_isolated.py';spec=importlib.util.spec_from_file_location('quicktest3_background33',p);h=importlib.util.module_from_spec(spec)
cache_root=HERE/'harness_runtime';cache_root.mkdir(exist_ok=True)
line=next(i for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1) if s.startswith('for variable, directory in'))
def route(frame,event,arg):
    if frame.f_code.co_filename==str(p) and event=='line' and frame.f_lineno==line:frame.f_globals['HARNESS']=cache_root
    return route
sys.settrace(route)
try:spec.loader.exec_module(h)
finally:sys.settrace(None)
assert h.PROJECT==ROOT and h.HARNESS==cache_root
write(out/'harness_routing.json',{'source_path':str(p),'source_sha256':file_hash(p),'source_unchanged':True,'cache_only_global_redirect':str(cache_root),'profile_overrides':False,'request_logic_overrides':False,'max_tokens_override':False,'local_timeout_override':False,'automatic_retry':False})
res=h.run_tests(BRANCH,q,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']})
print(json.dumps({'qid':q,'variant':vid,'two_completed':res['two_completed'],'evidence_dir':res['evidence_dir']}),flush=True)
