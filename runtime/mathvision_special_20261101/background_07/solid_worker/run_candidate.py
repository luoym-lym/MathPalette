from tools_local import *
import importlib.util
qid,vid=sys.argv[1:3];out=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
write(out/'eligibility_immediately_before_calls.json',check)
review=json.loads((out/'primary_review.json').read_text(encoding='utf-8'));assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
write(out/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat()})
p=ROOT/'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py';spec=importlib.util.spec_from_file_location('quicktest3_isolated_solid07',p);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
for var,name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():os.environ[var]=str(TASK/name)
res=h.run_tests('SolidGeometry',qid,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']})
print(json.dumps({'qid':qid,'variant':vid,'evidence_dir':res['evidence_dir'],'two_completed':res['two_completed']},ensure_ascii=False),flush=True)
