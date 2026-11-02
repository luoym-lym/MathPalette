from tools40 import *
import importlib.util
q,v=sys.argv[1:3];assert q in IDS;d=TASK/q/v
e=eligibility(q);assert e['eligible'],e
write(d/'eligibility_immediately_before_calls.json',e)
review=read(d/'primary_review.json');assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
assert file_hash(d/'candidate.png')==read(d/'design.json')['candidate_png_sha256']
local=TASK/'harness/quicktest3_isolated.py';source=BASE/'harness/quicktest3_isolated.py'
local.parent.mkdir(exist_ok=True)
if not local.exists():local.write_bytes(source.read_bytes())
assert local.read_bytes()==source.read_bytes()
spec=importlib.util.spec_from_file_location('unchanged_unit40_harness',local);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.PROJECT=ROOT;h.RUNTIME=(ROOT/'runtime').resolve()
for key,name in {'TEMP':'temp','TMP':'temp','TMPDIR':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():os.environ[key]=str(TASK/name)
write(d/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'harness_original_sha256':file_hash(source),'harness_local_sha256':file_hash(local),'relocation':'Byte-identical existing harness under own root; restored PROJECT/RUNTIME to real workspace after location-only relocation. Solver/request/profile/systemprompt/thinking/token/timeout/retry behavior unchanged.'})
r=h.run_tests('SolidGeometry',q,d/'candidate.png',d/'design.json',d/'tests',2)
write(d/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':r['two_completed'],'evidence_dir':r['evidence_dir']})
