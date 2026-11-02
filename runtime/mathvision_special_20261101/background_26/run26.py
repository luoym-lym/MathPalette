from tools26 import *
q=sys.argv[1];vid=sys.argv[2];assert q in ASSIGNED
out=HERE/q/vid;d=read(out/'design.json');p=read(out/'primary_review_before_calls.json');assert p['ready_for_exactly_two_calls']
assert d['variant_id']==vid and p['image_sha256']==file_hash(out/'candidate.png') and p['design_sha256']==file_hash(out/'design.json')
ck=eligibility(q);assert ck['eligible'],ck
write(out/'eligibility_before_calls.json',ck)
src=BASE/'harness/quicktest3_isolated.py';dst=HERE/'harness/quicktest3_isolated.py';dst.parent.mkdir(parents=True,exist_ok=True)
if not dst.exists():dst.write_bytes(src.read_bytes())
assert dst.read_bytes()==src.read_bytes()
write(out/'harness_runtime_routing.json',{'source':str(src),'isolated_byte_identical_copy':str(dst),'source_sha256':file_hash(src),'copy_sha256':file_hash(dst),'only_module_global_routing_overrides':{'PROJECT':str(ROOT),'RUNTIME':str(ROOT/'runtime')},'solver_settings_overrides':None,'profile_max_tokens_timeout_retries_overrides':False,'isolation':ISOLATION,'all_generated_paths_guarded_below':str(HERE)})
write(out/'api_process_started.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now(),'own_script':str(Path(__file__).resolve()),'run_count':2})
spec=importlib.util.spec_from_file_location('background26_unchanged_harness',dst);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
h.PROJECT=ROOT;h.RUNTIME=ROOT/'runtime'
try:
    result=h.run_tests('PlaneGeometry',q,out/'candidate.png',out/'design.json',out/'tests',runs=2)
    write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed'],'retries':0})
    print(json.dumps({'question_id':q,'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']}),flush=True)
except BaseException as exc:
    write(out/'api_process_failed.json',{'pid':os.getpid(),'finished_at':now(),'error_type':type(exc).__name__,'error':str(exc),'retries':0});raise
