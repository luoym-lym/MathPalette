import tools_local as t
import importlib.util
spec=importlib.util.spec_from_file_location('_background16_harness',t.HERE/'quicktest3_isolated.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
qid=t.sys.argv[1];name=t.sys.argv[2];p=t.HERE/qid/name
assert qid in t.ASSIGNED
check=t.eligibility(qid)
if not check['eligible']:raise ValueError(check)
t.write(p/'eligibility_at_api.json',check)
review=t.json.loads((p/'primary_visual.json').read_text())
assert review['native_png_viewed'] and review['human_semantics_acceptable']
branch='PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry'
result=m.run_tests(branch,qid,p/'candidate.png',p/'design.json',p/'tests',runs=2)
print(t.json.dumps({'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed']}),flush=True)
