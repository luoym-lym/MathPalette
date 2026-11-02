from tools import *
from concurrent.futures import ThreadPoolExecutor
JOBS=[('Plane402','exposed_strip_extent_binding'),('Plane409','assembled_base_identity_swap'),('Plane476','ratio_whole_side_denominator'),('Plane378','long_unit_top_strip_omission')]
assert BRANCH=='PlaneGeometry'
source=SHARED/'harness/quicktest3_isolated.py';module=types.ModuleType('isolated_harness')
module.__file__=str(TASK/'quicktest3_isolated.py')
exec(compile(source.read_bytes(),str(source),'exec'),module.__dict__)
assert module.PROJECT==ROOT and module.HARNESS==TASK
def run(job):
    qid,name=job;d=TASK/qid/name
    e=eligibility(qid);assert e['eligible'],e
    assert read(d/'primary_visual_review.json')['legal_and_readable']
    assert read(d/'render_check.json')['repeat_bytes_identical']
    assert not (d/'tests').exists()
    write(d/'eligibility_immediately_before_calls.json',e)
    write(d/'process_launch.json',{'pid':os.getpid(),'argv':sys.argv,'question_id':qid,'started_at':datetime.now(timezone.utc).isoformat(),'one_pair_per_thread':True})
    write(d/'harness_isolation.json',{'source':str(source),'sha256':file_hash(source),'source_modified':False,'virtual_file':module.__file__,'project':str(module.PROJECT),'cache_root':str(module.HARNESS),'unit_write_guard':True})
    result=module.run_tests(BRANCH,qid,d/'candidate.png',d/'design.json',d/'tests',runs=2)
    write(d/'process_completed.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
with ThreadPoolExecutor(max_workers=len(JOBS)) as pool:
    list(pool.map(run,JOBS))
