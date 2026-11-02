from bootstrap import *
import runpy
q=sys.argv[1];e=next(e for e in read(OWN/'first_pair_candidates.json') if e['question_id']==q);d=Path(e['candidate_directory'])
eligibility(q)
gate=read(OWN/'zero_prior_call_gate.json');assert gate['all_target_question_PNG_pairs_have_zero_saved_prior_transport']
assert gate['target_PNG_sha256'][q]==sha(d/'candidate.png')==e['PNG_sha256']
assert read(OWN/'fresh_replay'/q/'replay_verification.json')['png_sha256']==e['PNG_sha256']
assert sha(d/'design.json')==e['design_sha256'] and not (d/'tests').exists()
save(OWN/(q+'_process_started.json'),{'at_utc':now(),'pid':os.getpid(),'expected_wrong':e['expected_wrong_answer'],'PNG_sha256':e['PNG_sha256']})
sys.argv=['quicktest3_isolated.py','--branch','SolidGeometry','--question',q,'--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
save(OWN/(q+'_process_finished.json'),{'at_utc':now(),'pid':os.getpid(),'finished':True})
