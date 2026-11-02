from tools28 import *
qid,vid=sys.argv[1:3];folder=TASK/qid/vid
assert qid in ASSIGNED and vid.startswith('r28_')
assert (folder/'pretest_native_visual_review.json').exists()
assert (folder/'design_difference_audit.json').exists()
design=read(folder/'design.json');assert file_hash(folder/'candidate.png')==design['frozen_png_sha256']
if qid=='Solid123':assert (TASK/qid/'primary_unique_math_enumeration.json').exists()
assert not (folder/'tests').exists(),'No unchanged candidate repeat permitted'
check=eligibility(qid);assert check['eligible'],check
write(folder/'eligibility_immediately_before_calls.json',check)
write(folder/'process_launch.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'command_exclusively_own_unit':True})
source=SHARED/'harness/quicktest3_isolated.py'
module=types.ModuleType('r28_isolated_harness');module.__file__=str(TASK/'quicktest3_isolated.py')
exec(compile(source.read_bytes(),str(source),'exec'),module.__dict__)
assert module.PROJECT==ROOT and module.HARNESS==TASK
write(folder/'harness_isolation.json',{'source':str(source),'source_sha256':file_hash(source),'source_modified':False,'virtual_module_file':module.__file__,'project':str(module.PROJECT),'cache_root':str(module.HARNESS),'unit_write_guard':True,'profile_overrides':False,'timeout_overrides':False,'max_token_overrides':False,'retries':False})
result=module.run_tests('SolidGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
write(folder/'process_completed.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
