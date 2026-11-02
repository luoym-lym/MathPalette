from bootstrap import *
import runpy
vid=sys.argv[1]
sys.argv=['validate_candidate_replay.py','--question','Plane213','--candidate',str(OWN/'Plane213'/vid),'--output',str(OWN/'replays'/vid)]
runpy.run_path(str(OLD/'validate_candidate_replay.py'),run_name='__main__')
