from tools_local import *
import importlib.util
q,v=sys.argv[1:3];folder=TASK/q/v
check=eligibility(q);assert check['eligible'],check
write(folder/'eligibility_immediately_before_calls.json',check)
review=json.loads((folder/'primary_review.json').read_text(encoding='utf-8'));assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
p=TASK/'harness/quicktest3_isolated.py';source=TASK.parent/'harness/quicktest3_isolated.py';assert p.read_bytes()==source.read_bytes()
spec=importlib.util.spec_from_file_location('unit15_unchanged_harness',p);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.PROJECT=ROOT;h.RUNTIME=(ROOT/'runtime').resolve()
for var,name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():os.environ[var]=str(TASK/name)
write(folder/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat(),'harness_original_sha256':file_hash(source),'harness_local_sha256':file_hash(p),'relocation':'Byte-identical harness import from own directory; PROJECT/RUNTIME globals restored to true repository root after relocation; no request/solver/settings/function change.'})
r=h.run_tests('SolidGeometry',q,folder/'candidate.png',folder/'design.json',folder/'tests',2)
write(folder/'api_process_finished.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'evidence_dir':r['evidence_dir'],'two_completed':r['two_completed']})
