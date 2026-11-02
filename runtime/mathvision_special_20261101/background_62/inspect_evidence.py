from bootstrap import install,OWN,PROJECT,SESSION
install()
import json, hashlib
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p):
    p=Path(p); b=p.read_bytes(); t=b.decode('utf-8-sig'); return b,t
from pathlib import Path
receipts=[]
def inspect(p,full=True):
    b,t=read(p); d=json.loads(t) if str(p).endswith('.json') else None
    receipts.append({'path':str(p),'sha256':sha(b),'bytes':len(b),'full_UTF8_read':True})
    print('\nFILE',p,'bytes',len(b))
    if d is not None:
        if full: print(json.dumps(d,ensure_ascii=False,indent=2))
        else:
            for k,v in d.items():
                print(k, (str(type(v))+':'+str(len(v))) if isinstance(v,(list,dict)) else str(v)[:1500])
    else: print(t)
for n in ['preparation62.json','draft52_untested_first_call_provenance.json']:
    inspect(SESSION/n,False)
for n in ['checkpoint.json','final_qa.json']:
    inspect(SESSION/'background_52'/n,False)
for q in ['Plane482','Plane488']:
    p=SESSION/'background_52'/q
    print('\nFILES',q,[str(f.relative_to(p)) for f in p.rglob('*') if f.is_file()])
    inspect(p/'primary_math_proof.json')
    inspect(p/'old_history_read.json')
(OWN/'initial_read_receipts.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2),encoding='utf-8')
snap=OWN/'parent_initial_snapshots';snap.mkdir(exist_ok=True)
for n in ['continuation_brief.txt','exploration_report.json','remaining_questions.jsonl','refinement_dispatch_20261102.json','launch58_63_20261102.json','background_62_brief.txt','background_62_assignment.json']:
    p=SESSION/n
    if p.exists():
        b,t=read(p); (snap/n).write_bytes(b)
        receipts.append({'path':str(p),'snapshot':str(snap/n),'sha256':sha(b),'bytes':len(b),'full_UTF8_read':True})
(OWN/'initial_read_receipts.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2),encoding='utf-8')
