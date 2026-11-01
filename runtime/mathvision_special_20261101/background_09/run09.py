from tools09 import *
qid,vid=sys.argv[1:3];out=HERE/qid/vid
assert eligibility(qid)['eligible']
review=read(out/'primary_review.json');assert review['actual_candidate_png_viewed'] and review['proceed_to_API']
write(out/'eligibility_immediately_before_calls.json',eligibility(qid))
write(out/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now()})
h=harness()
write(out/'harness_context.json',{'original_path':str(BASE/'harness/quicktest3_isolated.py'),'original_sha256':file_hash(BASE/'harness/quicktest3_isolated.py'),'copy_path':h.__file__,'copy_sha256':file_hash(h.__file__),'unchanged_source_bytes':True,'only_context_globals_rebound':['PROJECT','RUNTIME'],'PROJECT':str(h.PROJECT),'HARNESS':str(h.HARNESS),'own_directory_guard':True})
r=h.run_tests('PlaneGeometry',qid,out/'candidate.png',out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'evidence_dir':r['evidence_dir'],'two_completed':r['two_completed']})
