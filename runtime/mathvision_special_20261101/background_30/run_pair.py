import tools_local as t
import importlib.util
qid=t.sys.argv[1];name=t.sys.argv[2];p=t.HERE/qid/name
assert qid in t.ASSIGNED and name.startswith('r30_')
check=t.eligibility(qid);assert check['eligible'],check
t.write(p/'eligibility_at_api.json',check)
review=t.json.loads((p/'primary_visual.json').read_text(encoding='utf-8-sig'))
assert review['native_png_viewed'] and review['human_semantics_acceptable']
assert (p/'design_difference_audit.json').exists()
assert not (p/'tests').exists(),'No unchanged retry permitted'
t.write(p/'api_process.json',{'pid':t.os.getpid(),'command':[t.sys.executable,'-X','utf8','-B',str(t.HERE/'run_pair.py'),qid,name],'started_at':t.now()})
spec=importlib.util.spec_from_file_location('_background30_harness',t.HERE/'quicktest3_isolated.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assert t.file_hash(t.HERE/'quicktest3_isolated.py')==t.file_hash(t.BASE/'harness/quicktest3_isolated.py')
result=m.run_tests('PlaneGeometry',qid,p/'candidate.png',p/'design.json',p/'tests',runs=2)
t.write(p/'api_process_finished.json',{'pid':t.os.getpid(),'finished_at':t.now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']})
print(t.json.dumps({'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed']}),flush=True)
