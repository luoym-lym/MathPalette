from bootstrap import *
import runpy
d=OWN/'Plane213/user233_boundary_spine_foot_transfer_v1'
sys.argv=['validate_candidate_replay.py','--question','Plane213','--candidate',str(d),'--output',str(OWN/'offline_replay')]
runpy.run_path(str(OLD/'validate_candidate_replay.py'),run_name='__main__')
