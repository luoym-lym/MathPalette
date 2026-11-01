from pathlib import Path
import os,sys,json,hashlib
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
for k,n in {'TEMP':'progress_tmp','TMP':'progress_tmp','MPLCONFIGDIR':'progress_mpl','XDG_CACHE_HOME':'progress_cache'}.items():
    p=HERE/n;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
sys.dont_write_bytecode=True;sys.path.insert(0,str(BASE))
from runtime_isolation import install
install(HERE/'progress_render_tmp')
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
assignment=read(BASE/'background_07_assignment.json')['question_ids'];inventory=read(BASE/'inventory.json');progress=read(BASE/'exploration_report.json')
remaining=[json.loads(s) for s in (BASE/'remaining_questions.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
out={'source':'Read-only diagnostic prior exploration metadata; authoritative current approval/Special files remain decisive.','inventory_counts':{k:{f:v[f] for f in ['mathvision_total','eligible_count']} for k,v in inventory.items()},'assigned_inventory_entries':{q:next((r for v in inventory.values() for r in v['eligible'] if r['id']==q),None) for q in assignment},'assigned_remaining_entries':[r for r in remaining if r['question_id'] in assignment],'assigned_prior_attempts':[r for r in progress['attempts'] if r['question_id'] in assignment],'historical_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [BASE/'inventory.json',BASE/'remaining_questions.jsonl',BASE/'exploration_report.json']},'metadata_not_rewritten':True}
assert not out['assigned_prior_attempts'] and all(r['status']=='not_yet_explored' for r in out['assigned_remaining_entries'])
with (HERE/'prior_progress_readonly.json').open('x',encoding='utf-8') as f:json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'inventory_counts':out['inventory_counts'],'assignment_prior_attempts':len(out['assigned_prior_attempts']),'assignment_fresh_entries':len(out['assigned_remaining_entries'])}))
