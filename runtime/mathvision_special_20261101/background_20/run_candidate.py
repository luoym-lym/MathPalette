from tools20 import *
import importlib.util,inspect
qid,vid=sys.argv[1:3];out=HERE/qid/vid
assert eligibility(qid)['eligible']
write(out/'eligibility_before_calls.json',eligibility(qid))
review=json.loads((out/'primary_review.json').read_text(encoding='utf-8'));assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
write(out/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now()})
p=BASE/'harness/quicktest3_isolated.py'
spec=importlib.util.spec_from_file_location('quicktest3_unit20',p);h=importlib.util.module_from_spec(spec)
# Execute the existing harness source unchanged. At module initialization redirect
# only HARNESS (its cache root) before its first mkdir; PROJECT and requests remain
# exactly the reference values. This keeps every write within this unit.
cache_root=HERE/'harness_runtime';cache_root.mkdir(exist_ok=True)
line=next(i for i,s in enumerate(p.read_text(encoding='utf-8').splitlines(),1) if s.startswith('for variable, directory in'))
def route(frame,event,arg):
    if frame.f_code.co_filename==str(p) and event=='line' and frame.f_lineno==line:
        frame.f_globals['HARNESS']=cache_root
    return route
sys.settrace(route)
try:spec.loader.exec_module(h)
finally:sys.settrace(None)
assert h.PROJECT==ROOT and h.HARNESS==cache_root
write(out/'harness_runtime_routing.json',{'source_path':str(p),'source_sha256':file_hash(p),'source_unchanged':True,'cache_only_global_redirect':str(cache_root),'profile_overrides':False,'request_logic_overrides':False})
res=h.run_tests('PlaneGeometry',qid,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']})
print(json.dumps({'qid':qid,'variant':vid,'two_completed':res['two_completed'],'evidence_dir':res['evidence_dir']}),flush=True)
