from bootstrap import *
import runpy
qid=sys.argv[1]
items=read(OWN/'prepared_offline_drafts.json')
item=next(x for x in items if x['question_id']==qid)
sys.argv=['validate_candidate_replay.py','--question',qid,'--candidate',item['directory'],'--output',str(OWN/'replay'/qid)]
runpy.run_path(str(OLD/'validate_candidate_replay.py'),run_name='__main__')
