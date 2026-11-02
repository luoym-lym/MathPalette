from bootstrap import *
import runpy
q=sys.argv[1];e=next(e for e in read(OWN/'first_pair_candidates.json') if e['question_id']==q)
sys.argv=['validate_candidate_replay.py','--question',q,'--candidate',e['candidate_directory'],'--output',str(OWN/'fresh_replay'/q)]
runpy.run_path(str(OLD/'validate_candidate_replay.py'),run_name='__main__')
