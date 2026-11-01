from tools_local import *
qid,vid=sys.argv[1:3];out=HERE/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(out/'eligibility_immediately_before_calls.json',check)
primary=json.loads((out/'primary_review.json').read_text(encoding='utf-8'))
assert primary['actual_candidate_png_viewed'] and primary['proceed_to_API']
write(out/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now()})
assert file_hash(HERE/'quicktest3_isolated.py')==file_hash(BASE/'harness/quicktest3_isolated.py')
spec=importlib.util.spec_from_file_location('_unchanged_quicktest11',HERE/'quicktest3_isolated.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
res=h.run_tests('PlaneGeometry',qid,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']})
print(json.dumps({'qid':qid,'variant':vid,'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']},ensure_ascii=False),flush=True)
