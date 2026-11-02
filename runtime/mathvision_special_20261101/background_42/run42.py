from env42 import *
import argparse
p=argparse.ArgumentParser();p.add_argument('--question',required=True);p.add_argument('--variant',required=True);args=p.parse_args()
q=args.question;out=HERE/q/args.variant;assert q in ASSIGNED
assert read(out/'primary_review.json')['passes_primary_quality']
assert not (out/'tests').exists(),'No retry of unchanged image'
e=eligibility(q);assert e['eligible'];write(out/'eligibility_immediately_before_calls.json',e)
check=read(out/'render_check.json');assert file_hash(out/'candidate.png')==check['png_sha256'] and file_hash(out/'design.json')==check['design_sha256']
assert inputs(adapter()[1],q)==check['input_fingerprints']
src=BASE/'harness/quicktest3_isolated.py';dst=HERE/'harness/quicktest3_isolated.py';dst.parent.mkdir(exist_ok=True)
if not dst.exists():dst.write_bytes(src.read_bytes())
assert dst.read_bytes()==src.read_bytes()
spec=importlib.util.spec_from_file_location('unchanged_background42_harness',dst);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.PROJECT=ROOT;h.RUNTIME=ROOT/'runtime'
write(out/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'copied_harness_sha256':file_hash(dst),'reference_harness_sha256':file_hash(src),'only_in_memory_path_constants_adjusted_for_deeper_own_copy':True,'runs':2,'no_settings_timeout_token_limit_retry_changes':True})
result=h.run_tests('PlaneGeometry',q,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed']})
print(json.dumps({'question_id':q,'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed']},ensure_ascii=False))
