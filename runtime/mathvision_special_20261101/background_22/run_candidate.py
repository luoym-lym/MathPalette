"""Run exactly one predeclared pair using the byte-identical existing harness."""
from unit_tools import *
import importlib.util
branch,qid,name=sys.argv[1:]
directory=HERE/qid/name
assert qid in IDS
eligible=eligibility(branch,qid)
write(directory/'eligibility_before_pair.json',eligible)
assert eligible['eligible']
source=BASE/'harness/quicktest3_isolated.py'
copy_path=HERE/'quicktest3_isolated.py'
if not copy_path.exists():copy_path.write_bytes(source.read_bytes())
assert sha(source)==sha(copy_path)
spec=importlib.util.spec_from_file_location('_unit22_unchanged_harness',copy_path)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
write(directory/'pair_process.json',{'pid':os.getpid(),'command':sys.argv,'started_at':now(),'harness_source_sha256':sha(source),'harness_copy_sha256':sha(copy_path),'isolation':ISOLATION})
h.run_tests(branch,qid,directory/'candidate.png',directory/'design.json',directory/'tests',runs=2)
write(directory/'pair_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'normal_completion':True})
