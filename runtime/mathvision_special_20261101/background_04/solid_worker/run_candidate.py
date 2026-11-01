from tools_local import *
import importlib.util
qid,vid=sys.argv[1:3]
folder=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(folder/'eligibility_immediately_before_calls.json',check)
write(folder/'process_launch.json',{'pid':os.getpid(),'command_arguments':sys.argv,'started_at':datetime.now(timezone.utc).isoformat(),'question_id':qid,'variant_id':vid})
spec=importlib.util.spec_from_file_location('isolated_harness',ROOT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
result=module.run_tests('SolidGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
write(folder/'process_completed.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
