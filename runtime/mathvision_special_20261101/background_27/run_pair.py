from tools27 import *
import importlib.util
qid,vid=sys.argv[1:3];folder=HERE/qid/vid
check=eligibility(qid);assert check['eligible'];write(folder/'eligibility_immediately_before_calls.json',check)
review=json.loads((folder/'primary_visual_review.json').read_text(encoding='utf-8'));assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
write(folder/'api_process_started.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now()})
# Byte-identical copy lets the unchanged harness select caches inside this unit.
# Only the imported module's filesystem root constants are restored in memory.
source=BASE/'harness/quicktest3_isolated.py';dest=HERE/'harness/quicktest3_isolated.py'
dest.parent.mkdir(parents=True,exist_ok=True)
if not dest.exists():dest.write_bytes(source.read_bytes())
assert source.read_bytes()==dest.read_bytes()
spec=importlib.util.spec_from_file_location('_background27_unchanged_quicktest3',dest)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.PROJECT=ROOT;h.RUNTIME=(ROOT/'runtime').resolve()
write(folder/'harness_isolation_audit.json',{'original':str(source),'copy':str(dest),'source_sha256':file_hash(source),'copy_sha256':file_hash(dest),'byte_identical':True,'in_memory_path_constants_restored':['PROJECT','RUNTIME'],'HARNESS':str(h.HARNESS),'model_settings_modified':False,'request_function_modified':False})
res=h.run_tests('PlaneGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',2)
write(folder/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']})
print(json.dumps({'qid':qid,'variant':vid,'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']},ensure_ascii=False),flush=True)

