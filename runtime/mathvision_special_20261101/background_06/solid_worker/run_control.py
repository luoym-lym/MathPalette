from tools_local import *
import importlib.util
q='Solid142';folder=TASK/q/'original_control'
check=eligibility(q);assert check['eligible'],check
write(folder/'eligibility_immediately_before_calls.json',check)
write(folder/'process_launch.json',{'pid':os.getpid(),'command_arguments':sys.argv,'started_at':datetime.now(timezone.utc).isoformat()})
spec=importlib.util.spec_from_file_location('isolated_harness',ROOT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
r=module.run_tests('SolidGeometry',q,folder/'original.png',folder/'design.json',folder/'tests',2)
write(folder/'process_completed.json',{'pid':os.getpid(),'two_completed':r['two_completed'],'evidence_dir':r['evidence_dir'],'finished_at':datetime.now(timezone.utc).isoformat()})
