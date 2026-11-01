import os,sys,json,hashlib,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for k,n in {'TEMP':'audit_tmp','TMP':'audit_tmp','MPLCONFIGDIR':'audit_mpl','XDG_CACHE_HOME':'audit_cache'}.items():
    p=HERE/n;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parent))
from runtime_isolation import install
install(HERE/'audit_render_tmp')
spec=importlib.util.spec_from_file_location('_unit07_inventory',HERE.parent/'inventory.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def save(p,v):
    with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
if sys.argv[1]=='before':
    found=m.scan();save(HERE/'formal_files_before.json',found)
    prior={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in HERE.parent.rglob('*') if p.is_file() and not p.is_relative_to(HERE)}
    save(HERE/'prior_runtime_fingerprints.json',prior)
    print(json.dumps({'formal_file_count':len(found),'prior_runtime_files':len(prior)}))
else:
    before=json.loads((HERE/'formal_files_before.json').read_text(encoding='utf-8'));after=m.scan()
    prior=json.loads((HERE/'prior_runtime_fingerprints.json').read_text(encoding='utf-8'))
    changes={'formal_changed':[p for p in before.keys()&after.keys() if before[p]!=after[p]],'formal_deleted':sorted(before.keys()-after.keys()),'formal_added':sorted(after.keys()-before.keys()),'prior_runtime_changed_or_deleted':[p for p,h in prior.items() if not (ROOT/p).is_file() or hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]}
    save(HERE/'source_preservation_final.json',{'formal_file_count':len(before),'prior_runtime_file_count':len(prior),**changes,'no_formal_or_prior_evidence_changes':not any(changes.values())})
    print(json.dumps(changes))
