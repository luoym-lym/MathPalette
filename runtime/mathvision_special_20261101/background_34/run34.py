from tools34 import *
import importlib.util
qid,variant=sys.argv[1:3]
folder=UNIT/qid/variant
review=read(folder/'primary_pretest_review.json');assert review['proceed_to_exactly_two_calls']
assert not (folder/'tests').exists(),'Never rerun a candidate, including failed/aborted.'
check=eligibility(qid);assert check['eligible'];write(folder/'eligibility_immediately_before_calls.json',check)
assert source_files(qid)==read(UNIT/qid/'source_fingerprints_start.json')
source=SHARED/'harness/quicktest3_isolated.py';copy_path=UNIT/'quicktest3_isolated.py'
if not copy_path.exists():copy_path.write_bytes(source.read_bytes())
assert source.read_bytes()==copy_path.read_bytes()
write(folder/'api_process.json',{'pid':os.getpid(),'python_executable':sys.executable,'argv':sys.argv,'started_at':now(),'own_unit':str(UNIT),
      'command_line_identity':'python -X utf8 -B '+str(Path(__file__).resolve())+' '+qid+' '+variant})
spec=importlib.util.spec_from_file_location('unchanged_isolated_harness34',copy_path)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
assert module.PROJECT==PROJECT and module.HARNESS==UNIT
write(folder/'harness_isolation.json',{'source':str(source),'source_sha256':sha(source),'isolated_exact_copy':str(copy_path),'copy_sha256':sha(copy_path),
      'harness_bytes_unchanged':True,'project':str(module.PROJECT),'cache_root':str(module.HARNESS),'strict_own_unit_write_guard':True,
      'runtime_isolation':ISOLATION,'profile_token_timeout_overrides':False})
result=module.run_tests(branch_of(qid),qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
write(folder/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
