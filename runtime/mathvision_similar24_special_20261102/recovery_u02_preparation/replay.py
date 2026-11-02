from bootstrap import *
import runpy
q=sys.argv[1]
v={'Plane218':'p03_native_outer_boundary_conservation','Plane398':'p03_native_L_arm_transport_all_options'}[q]
sys.argv=[str(OLD/'validate_candidate_replay.py'),'--question',q,'--candidate',str(SOURCE/q/v),'--output',str(OWN/'replay'/q)]
runpy.run_path(str(OLD/'validate_candidate_replay.py'),run_name='__main__')
