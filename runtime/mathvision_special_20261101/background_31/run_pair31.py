from bootstrap31 import *
from inspect31 import eligibility
import importlib.util

qid,variant=sys.argv[1:]
assert qid in IDS and variant.startswith('r31_')
d=OWN/qid/variant
primary=read(d/'primary_review.json')
assert primary['proceed_to_exact_two_calls'] and primary['actual_native_PNG_viewed']
assert not list((d/'tests').glob('quicktest3_*'))
assert sha(d/'candidate.png')==primary['precall_PNG_frozen_sha256']
assert sha(d/'design.json')==primary['precall_design_frozen_sha256']
assert (d/'design_difference_audit.json').is_file()
eligible=eligibility(qid);assert eligible['eligible']
save(d/'eligibility_immediately_before_calls.json',eligible)
save(d/'api_process.json',{'started_at':stamp(),'pid':os.getpid(),'parent_pid':os.getppid(),'argv':sys.argv,'unit_root':str(OWN),'image_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json'),'requested_calls':2,'retry':False})
assert sha(OWN/'quicktest3_isolated.py')==sha(SHARED/'harness/quicktest3_isolated.py')
spec=importlib.util.spec_from_file_location('_unit31_unchanged_harness',OWN/'quicktest3_isolated.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
try:
    result=h.run_tests('PlaneGeometry',qid,d/'candidate.png',d/'design.json',d/'tests',runs=2)
    save(d/'api_process_finished.json',{'finished_at':stamp(),'pid':os.getpid(),'two_completed':result['two_completed'],'evidence_directory':result['evidence_dir'],'no_retry':True})
except BaseException as exc:
    save(d/'api_process_exception.json',{'finished_at':stamp(),'pid':os.getpid(),'type':type(exc).__name__,'exception':str(exc),'no_retry':True})
    raise
