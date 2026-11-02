from bootstrap import *
import runpy
d=OWN/'Plane213/user233_boundary_spine_foot_transfer_v1'
eligibility()
gate=read(OWN/'prelaunch_gate.json')
assert gate['same_question_exact_PNG_zero_prior_actual_calls_proved']
assert gate['PNG_sha256']==sha(d/'candidate.png') and gate['design_sha256']==sha(d/'design.json')
assert not (d/'tests').exists()
save(OWN/'pair_process_started.json',{'at_utc':now(),'pid':os.getpid(),'question_id':'Plane213','preset':'C','PNG_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json')})
sys.argv=['quicktest3_isolated.py','--branch','PlaneGeometry','--question','Plane213','--image',str(d/'candidate.png'),'--design',str(d/'design.json'),'--output',str(d/'tests'),'--runs','2']
runpy.run_path(str(OWN/'harness/quicktest3_isolated.py'),run_name='__main__')
save(OWN/'pair_process_finished.json',{'at_utc':now(),'pid':os.getpid(),'command_finished':True})
