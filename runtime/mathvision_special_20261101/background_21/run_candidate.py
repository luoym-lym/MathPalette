from tools import *
import types
qid,vid=sys.argv[1:3];folder=HERE/qid/vid
check=eligibility(qid);assert check['eligible'],check
review=json.loads((folder/'primary_review.json').read_text(encoding='utf-8'));assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
write(folder/'eligibility_immediately_before_calls.json',check)
write(folder/'process_launch.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now()})
source=BASE/'harness/quicktest3_isolated.py';module=types.ModuleType('isolated_harness_21')
module.__file__=str(HERE/'quicktest3_isolated.py')
exec(compile(source.read_bytes(),str(source),'exec'),module.__dict__)
assert module.PROJECT==ROOT and module.HARNESS==HERE
write(folder/'harness_isolation.json',{'source':str(source),'source_sha256':file_hash(source),'source_modified':False,'virtual_module_file':module.__file__,'project':str(module.PROJECT),'cache_root':str(module.HARNESS),'unit_write_guard':True,'settings_overrides':None,'retries':0})
result=module.run_tests('PlaneGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
write(folder/'process_completed.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
