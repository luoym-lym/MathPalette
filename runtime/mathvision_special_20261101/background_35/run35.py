from tools35 import *
import subprocess
q=sys.argv[1];v=sys.argv[2];assert q in ASSIGNED
out=HERE/q/v;d=json.loads((out/'design.json').read_text());primary=json.loads((out/'primary_review.json').read_text())
assert primary['proceed_to_exactly_two_calls'] and primary['actual_native_candidate_png_viewed']
assert file_hash(out/'candidate.png')==d['png_sha256']==primary['image_sha256']
assert file_hash(out/'design.json')==primary['design_sha256']
e=eligibility(q);assert e['eligible'];write(out/'eligibility_immediately_before_calls.json',e)
source_path=BASE/'harness/quicktest3_isolated.py';original=source_path.read_text(encoding='utf-8-sig')
old='PROJECT = Path(__file__).resolve().parents[3]';assert original.count(old)==1
patched=original.replace(old,'PROJECT = Path('+repr(str(ROOT))+')')
assert original[original.index('def timestamp():'):]==patched[patched.index('def timestamp():'):]
code_path=HERE/'harness/quicktest3_isolated.py';code_path.parent.mkdir(parents=True,exist_ok=True)
write(out/'harness_isolation_audit.json',{'reference_harness':str(source_path),'reference_sha256':file_hash(source_path),'bootstrap_only_change':'PROJECT constant set to original project root and __file__ routed to own runtime harness directory, so all default harness caches remain inside background_35. No solver/test function, request, model, profile, max_tokens, timeout or retry logic changed.','unchanged_core_from_def_timestamp_sha256':hashlib.sha256(original[original.index('def timestamp():'):].encode()).hexdigest(),'core_byte_equal':True,'runtime_isolation_installed':ISOLATION,'own_root_guard_installed_before_all_project_imports':True,'solver_inputs_only_formal_question_and_candidate_png':True,'requested_runs':2})
write(out/'process_launch.json',{'pid':os.getpid(),'command':subprocess.list2cmdline([sys.executable,*sys.argv]),'argv':[sys.executable,*sys.argv],'created_at':now(),'own_candidate':str(out),'requested_runs':2})
ns={'__name__':'_unit35_unchanged_isolated_harness','__file__':str(code_path)}
exec(compile(patched,str(code_path),'exec'),ns)
result=ns['run_tests'](BRANCH,q,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'process_completion.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':result['evidence_dir'],'two_completed':result['two_completed'],'results_status':[r['status'] for r in result['results']]})
print(json.dumps({'question_id':q,'two_completed':result['two_completed'],'evidence_dir':result['evidence_dir']}),flush=True)
