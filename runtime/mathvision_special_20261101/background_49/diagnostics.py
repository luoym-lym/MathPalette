import research_env as env
import json
from inspect_sources import save,sha,QIDS,now

def select(value):
 found=[]
 def walk(x,path):
  if isinstance(x,dict):
   if x.get('question_id',x.get('id')) in QIDS:
    found.append({'json_path':path,'value':x});return
   for k,v in x.items():walk(v,path+[k])
  elif isinstance(x,list):
   for i,v in enumerate(x):walk(v,path+[i])
 walk(value,[])
 return found
out={}
for name in ['inventory.json','remaining_questions.jsonl','exploration_report.json']:
 p=env.SHARED/name
 if not p.exists():out[name]={'exists':False};continue
 raw=p.read_text(encoding='utf-8-sig')
 try:
  data=[json.loads(l) for l in raw.splitlines() if l.strip()] if p.suffix=='.jsonl' else json.loads(raw)
  out[name]={'sha256_at_read':sha(p),'role':'diagnostic mutable runtime metadata; not frozen source or authoritative eligibility','relevant_entries':select(data)}
 except Exception as exc:out[name]={'sha256_at_read':sha(p),'parse_error':str(exc),'old_bytes_unchanged':True}
save(env.ROOT/'current_progress_diagnostics.json',out)
save(env.ROOT/'local_execution_events.json',{'created_at_utc':now(),'events':[{'phase':'initial source inspection before any candidate API call','error':'TypeError: Object of type ndarray is not JSON serializable while serializing object_paths into own Solid80/paths.json','classification':'local offline audit serialization failure; not API failure, not failed/aborted candidate','resolution':'JSON encoder now serializes numpy controls with tolist(); inspection reran under own write guard and all8 no-op checks passed','formal_or_old_evidence_modified':False}],
 'no_historical_parse_failure_repair':True,'relevant_old_parse_failure_count':0})
print(json.dumps({k:{'entries':len(v.get('relevant_entries',[])),'parse_error':v.get('parse_error')} for k,v in out.items()}))
