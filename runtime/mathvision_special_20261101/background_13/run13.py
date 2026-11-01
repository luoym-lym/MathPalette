from tools13 import *
import importlib.util
qid,vid=sys.argv[1:3];folder=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(folder/'eligibility_before_calls.json',check)
write(folder/'process_launch.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat()})
local=TASK/'harness/quicktest3_isolated.py';shared=TASK.parent/'harness/quicktest3_isolated.py'
assert local.read_bytes()==shared.read_bytes(),'Harness copy must remain unchanged'
spec=importlib.util.spec_from_file_location('qt13',local);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# The exact unchanged harness is copied one level deeper for private caches.
# Set only its path globals to the real project/runtime after the import.
m.PROJECT=ROOT;m.RUNTIME=(ROOT/'runtime').resolve()
write(folder/'harness_routing.json',{'shared_sha256':file_hash(shared),'local_sha256':file_hash(local),'byte_identical':True,'path_globals_overridden':['PROJECT','RUNTIME'],'model_request_or_test_logic_changed':False,'isolation':ISOLATION})
r=m.run_tests('SolidGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
write(folder/'process_completed.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'two_completed':r['two_completed'],'evidence_dir':r['evidence_dir']})
