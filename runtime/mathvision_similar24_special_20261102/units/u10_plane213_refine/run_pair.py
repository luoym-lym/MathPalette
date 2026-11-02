from bootstrap import *
import runpy
d=OWN/'Plane213/user233_exterior_concave_corner_to_B_v2';eligibility();g=read(OWN/'prelaunch_gate.json')
assert g['same_question_exact_PNG_zero_prior_actual_calls_proved'] and g['PNG_sha256']==sha(d/'candidate.png') and g['design_sha256']==sha(d/'design.json')
assert not (d/'tests').exists()
save(OWN/'pair_process_started.json',{'at_utc':now(),'pid':os.getpid(),'question_id':'Plane213','preset':'B','PNG_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json')})
sys.argv=['quicktest3_isolated.py','--branch','PlaneGeometry','--question','Plane213','--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
save(OWN/'pair_process_finished.json',{'at_utc':now(),'pid':os.getpid(),'finished':True})
