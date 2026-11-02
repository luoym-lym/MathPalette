from bootstrap import *
import runpy,traceback
qid='Solid226'
item=next(x for x in read(OWN/'prepared_offline_drafts.json') if x['question_id']==qid)
canonical=OLD/'validate_candidate_replay.py'
frozen=read(TASK/'readonly_source_sha256.json')
assert sha(canonical)==frozen['runtime/mathvision_special_20261101/validate_candidate_replay.py']
sys.argv=['validate_candidate_replay.py','--question',qid,'--candidate',item['directory'],'--output',str(OWN/'replay'/qid)]
captured=[]
def trace(frame,event,arg):
 if event=='line' and frame.f_code.co_filename==str(canonical) and frame.f_lineno in (25,26,27):
  l=frame.f_locals;g=frame.f_globals
  captured.append({'line':frame.f_lineno,'argv':list(sys.argv),'source':str(l.get('source')),'output':str(l.get('output')),'runtime':str(g.get('RUNTIME')),'source_within':l['source'].is_relative_to(g['RUNTIME']),'output_within':l['output'].is_relative_to(g['RUNTIME'])})
 return trace
sys.settrace(trace)
try:
 runpy.run_path(str(canonical),run_name='__main__')
 outcome='complete'
except BaseException:
 outcome='error';error=traceback.format_exc();raise
finally:
 sys.settrace(None)
 save(OWN/'replay_preflight_diagnostic226.json',{'at_utc':now(),'canonical_sha_matches_frozen':True,'records':captured,'outcome':outcome,'error':locals().get('error'),'no_source_or_geometry_or_guard_change':True,'new_API_calls':0})
