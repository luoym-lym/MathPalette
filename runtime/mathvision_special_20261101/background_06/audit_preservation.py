from pathlib import Path
import os,sys,json,hashlib,importlib.util
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for key,name in {'TEMP':'audit_tmp','TMP':'audit_tmp','MPLCONFIGDIR':'audit_mpl','XDG_CACHE_HOME':'audit_cache'}.items():
    target=HERE/name;target.mkdir(parents=True,exist_ok=True);os.environ[key]=str(target)
sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parent))
from runtime_isolation import install
install(HERE/'audit_render_tmp')
spec=importlib.util.spec_from_file_location('_readonly_inventory',HERE.parent/'inventory.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
before=json.loads((HERE/'formal_files_before.json').read_text(encoding='utf-8'));after=module.scan()
prior=json.loads((HERE/'prior_delivery_fingerprints.json').read_text(encoding='utf-8'))
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'checked_at':datetime.now(timezone.utc).isoformat(),'formal_baseline_file_count':len(before),'changed':[p for p in before.keys()&after.keys() if before[p]!=after[p]],'deleted':sorted(before.keys()-after.keys()),'added':sorted(after.keys()-before.keys()),'prior_delivered_file_count':len(prior),'prior_delivered_files_changed_or_deleted':[p for p,h in prior.items() if not (ROOT/p).is_file() or digest(ROOT/p)!=h],'method':'Read-only complete SHA256 snapshot outside root runtime/.git; preexisting .runtime metadata-only to preserve isolation. All batch01-04 files have exact SHA256 comparisons. Worker source audits additionally bind formal question/source/rendering inputs and raw test bytes. No prior exploratory evidence path is an output path; shared harness cache directories are diagnostic mutable runtime helpers.','mutable_progress_metadata':['exploration_report.json','remaining_questions.jsonl'],'mutable_progress_policy':'Historical snapshot hashes retained; current eligibility checked against authoritative formal approvals and Special state. These runtime metadata files are not frozen original source files.','no_formal_or_prior_delivery_changes':not any([report_list for report_list in [list(before.keys()-after.keys()),list(after.keys()-before.keys()),[p for p in before.keys()&after.keys() if before[p]!=after[p]],[p for p,h in prior.items() if not (ROOT/p).is_file() or digest(ROOT/p)!=h]]])}
with (HERE/'source_preservation_final.json').open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['method','mutable_progress_policy']}))
