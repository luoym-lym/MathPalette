from audit import *
import importlib.util

def run(qid,variant):
    assert qid in IDS and variant.startswith('r32_')
    out=ROOT/qid/variant
    assert read(out/'primary_review.json')['proceed_to_API']
    assert read(out/'primary_review.json')['actual_new_native_candidate_viewed']
    assert read(out/'primary_review.json')['candidate_sha256']==sha(out/'candidate.png')
    assert read(out/'primary_review.json')['design_sha256']==sha(out/'design.json')
    assert not (out/'tests').exists(), 'No repeated variant calls'
    e=eligibility(qid); assert e['eligible'],e['reasons']
    save(out/'eligibility_immediately_before_calls.json',e)
    p=ROOT/'harness/quicktest3_isolated.py'
    p.parent.mkdir(parents=True,exist_ok=True)
    original=BASE/'harness/quicktest3_isolated.py'
    if not p.exists(): p.write_bytes(original.read_bytes())
    assert p.read_bytes()==original.read_bytes()
    spec=importlib.util.spec_from_file_location('r32_unchanged_isolated_harness',p)
    h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    h.PROJECT=PROJECT; h.RUNTIME=PROJECT/'runtime'
    process={'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'qid':qid,'variant':variant,'harness_copy_sha256':sha(p),'original_harness_sha256':sha(original),'harness_unchanged':True,'profile_overrides':None,'timeout_overrides':None,'retry':False}
    save(out/'api_process.json',process)
    print(json.dumps(process),flush=True)
    result=h.run_tests('PlaneGeometry',qid,out/'candidate.png',out/'design.json',out/'tests',runs=2)
    save(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir'],'calls':len(result['results']),'normal_return':True})
    print(json.dumps({'finished':True,'qid':qid,'variant':variant,'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']}),flush=True)

if __name__=='__main__': run(*sys.argv[1:])
