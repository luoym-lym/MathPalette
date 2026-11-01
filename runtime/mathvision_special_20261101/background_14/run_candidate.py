from tools import *
import types
qid,vid=sys.argv[1:3];folder=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(folder/'eligibility_immediately_before_calls.json',check)
write(folder/'process_launch.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat()})
source=SHARED/'harness/quicktest3_isolated.py'
module=types.ModuleType('isolated_harness')
# Unchanged harness bytes; virtual __file__ routes its HARNESS caches to this unit
# while keeping PROJECT=parents[3] equal to the actual project root.
module.__file__=str(TASK/'quicktest3_isolated.py')
exec(compile(source.read_bytes(),str(source),'exec'),module.__dict__)
write(folder/'harness_isolation.json',{'source':str(source),'source_sha256':file_hash(source),'source_modified':False,'virtual_module_file':module.__file__,'project':str(module.PROJECT),'cache_root':str(module.HARNESS),'unit_write_guard':True})
result=module.run_tests('SolidGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
write(folder/'process_completed.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
