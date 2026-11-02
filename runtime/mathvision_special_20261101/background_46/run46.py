from tools46 import *
import importlib.util
q,v=sys.argv[1:3];assert q in IDS and q not in ['Solid106','Solid152']
assert not (OWN/'external_failure_stop.json').exists(),'Prior external failure: all further calls prohibited'
d=OWN/q/v;assert not (d/'tests').exists(),'Never repeat a started candidate'
e=eligibility(q);save(d/'eligibility_immediately_before_first_calls_46.json',e);assert e['eligible']
rv=read(d/('primary_native_review_46.json' if v.startswith('r40_') else 'primary_review.json'));assert rv['proceed_to_first_pair']
assert sha(d/'candidate.png')==read(d/'design.json')['candidate_png_sha256']
local=OWN/'harness/quicktest3_isolated.py';source=TASK/'harness/quicktest3_isolated.py'
local.parent.mkdir(parents=True,exist_ok=True)
if not local.exists():local.write_bytes(source.read_bytes())
assert local.read_bytes()==source.read_bytes()
spec=importlib.util.spec_from_file_location('unchanged_background46_harness',local);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.PROJECT=PROJECT;h.RUNTIME=(PROJECT/'runtime').resolve()
for key,sub in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():os.environ[key]=str(OWN/sub)
save(d/'api_process_46.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'original_harness_sha256':sha(source),'local_harness_sha256':sha(local),'call_count_requested':2,'no_retry':True,'relocation_only':'Exact unchanged harness copy, PROJECT/RUNTIME restored for own46 location. All solver/model/profile/systemprompt/timeout/token behavior inherited unchanged.'})
result=h.run_tests('SolidGeometry',q,d/'candidate.png',d/'design.json',d/'tests',2)
save(d/'api_process_finished_46.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
if any(x['status']!='completed' for x in result['results']):
    save(OWN/'external_failure_stop.json',{'stopped_at':now(),'question_id':q,'variant_id':v,'evidence_dir':result['evidence_dir'],'results':result['results'],'stop_all_further_calls_and_exploration':True,'retry':False})
