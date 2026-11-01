from tools04 import *
import importlib.util
qid,vid=sys.argv[1:3];folder=HERE/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(folder/'eligibility_immediately_before_calls.json',check)
assert (folder/'primary_review.json').exists(),'Actual image must be viewed and reviewed first'
write(folder/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat()})
path=ROOT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py'
spec=importlib.util.spec_from_file_location('quicktest3_isolated04',path);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
result=h.run_tests('PlaneGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',2)
print(json.dumps({'qid':qid,'variant':vid,'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed']},ensure_ascii=False),flush=True)
