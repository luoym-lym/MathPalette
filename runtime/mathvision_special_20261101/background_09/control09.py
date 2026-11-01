from tools09 import *
qid='Plane391';vid='whole_square_frame_to_triangle';out=HERE/qid/vid/'original_control'
ck=eligibility(qid);assert ck['eligible']
out.mkdir(parents=True,exist_ok=False)
image=HERE/qid/'original.png';r=read(HERE/qid/'formal_record.json')
assert image.read_bytes()==(ROOT/'PlaneGeometry'/r['image']).read_bytes()
write(out/'design.json',{'question_id':qid,'variant_id':vid+'_original_control','expected_wrong_answer':'8','role':'separate_original_control','created_at':now(),'description':'Unmodified exact formal original PNG. Separate post-candidate control, wrong-target preset inherited from candidate before these two calls; no selection or retesting of the candidate. Correct controls are not a hard gate.'})
write(out/'eligibility_before_calls.json',ck)
write(out/'api_process.json',{'pid':os.getpid(),'argv':sys.argv,'started_at':now()})
h=harness();res=h.run_tests('PlaneGeometry',qid,image,out/'design.json',out/'tests',2)
write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),'two_completed':res['two_completed'],'evidence_dir':res['evidence_dir']})
