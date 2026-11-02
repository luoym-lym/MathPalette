from common23 import *
from datetime import datetime,timezone
import importlib.util
qid=sys.argv[1];vid=sys.argv[2];d=OUT/qid/vid
e=eligibility(qid);assert e['eligible'];write(d/'eligibility_before_calls.json',e)
assert read(d/'primary_review.json')['proceed_to_API']
assert not (d/'api_process.json').exists(),'Never rerun unchanged candidate'
write(d/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat()})
p=BASE/'harness/quicktest3_isolated.py'
spec=importlib.util.spec_from_file_location('quicktest3_r23',p);h=importlib.util.module_from_spec(spec)
cache=OUT/'harness_runtime';cache.mkdir(exist_ok=True)
line=next(i for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1) if s.startswith('for variable, directory in'))
def route(frame,event,arg):
    if frame.f_code.co_filename==str(p) and event=='line' and frame.f_lineno==line:frame.f_globals['HARNESS']=cache
    return route
sys.settrace(route)
try:spec.loader.exec_module(h)
finally:sys.settrace(None)
assert h.PROJECT==ROOT and h.HARNESS==cache
write(d/'harness_runtime_routing.json',{'harness_source':str(p),'source_sha256':sha(p),'source_executed_unchanged':True,'cache_only_global_redirect':str(cache),'profile_or_request_or_timeout_overrides':False})
r=h.run_tests(e['branch'],qid,d/'candidate.png',d/'design.json',d/'tests',2)
write(d/'api_process_finished.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'evidence_dir':r['evidence_dir'],'two_completed':r['two_completed']})
print(json.dumps({'qid':qid,'variant':vid,'two_completed':r['two_completed'],'evidence_dir':r['evidence_dir']}),flush=True)
