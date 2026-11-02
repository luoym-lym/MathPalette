from tools import *
qid,name=sys.argv[1:3];d=TASK/qid/name
e=eligibility(qid);assert e['eligible'],e
assert read(d/'primary_visual_review.json')['legal_and_readable']
write(d/'eligibility_immediately_before_calls.json',e)
write(d/'process_launch.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat()})
source=SHARED/'harness/quicktest3_isolated.py';module=types.ModuleType('isolated_harness')
module.__file__=str(TASK/'quicktest3_isolated.py')
exec(compile(source.read_bytes(),str(source),'exec'),module.__dict__)
assert module.PROJECT==ROOT and module.HARNESS==TASK
write(d/'harness_isolation.json',{'source':str(source),'sha256':file_hash(source),'source_modified':False,'virtual_file':module.__file__,'project':str(module.PROJECT),'cache_root':str(module.HARNESS),'unit_write_guard':True})
result=module.run_tests(BRANCH,qid,d/'candidate.png',d/'design.json',d/'tests',runs=2)
write(d/'process_completed.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
