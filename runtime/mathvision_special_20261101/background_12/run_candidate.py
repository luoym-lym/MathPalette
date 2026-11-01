from tools_local import *
import importlib.util
qid,vid=sys.argv[1:3];out=HERE/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(out/'eligibility_immediately_before_calls.json',check)
review=read(out/'primary_visual_review.json');assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
write(out/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now()})
p=BASE/'harness/quicktest3_isolated.py';original_mkdir=Path.mkdir
# Import the unchanged shared harness. Its three unconditional cache-directory
# mkdir calls are routed to own equivalents without touching the shared paths.
routes={(p.parent/name).resolve():HERE/('harness_'+name) for name in ['mpl_cache','cache','tmp']}
def routed_mkdir(path,*a,**kw):
    destination=routes.get(path.resolve(),path)
    return original_mkdir(destination,*a,**kw)
try:
    Path.mkdir=routed_mkdir
    spec=importlib.util.spec_from_file_location('quicktest3_isolated_background12',p);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
finally:Path.mkdir=original_mkdir
for var,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():os.environ[var]=str(HERE/name)
res=h.run_tests('PlaneGeometry',qid,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed'],'shared_harness_sha256':file_hash(p),'shared_harness_source_unchanged':True,'cache_mkdir_routing_only':{str(k):str(v) for k,v in routes.items()}})
print(json.dumps({'qid':qid,'variant':vid,'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']},ensure_ascii=False),flush=True)
