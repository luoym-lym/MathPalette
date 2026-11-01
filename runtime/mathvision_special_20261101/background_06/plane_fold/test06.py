from tools06 import *
import importlib.util
spec=importlib.util.spec_from_file_location('_unit06_original_quicktest3_harness',BASE/'harness/quicktest3_isolated.py')
harness=importlib.util.module_from_spec(spec);spec.loader.exec_module(harness)
qid,vid=sys.argv[1:3];folder=HERE/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(folder/'eligibility_before_test.json',check)
result=harness.run_tests('PlaneGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
print(json.dumps({'question_id':qid,'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed']},ensure_ascii=False),flush=True)
