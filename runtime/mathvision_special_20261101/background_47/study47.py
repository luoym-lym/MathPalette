from env47 import *
import json
from inspect47 import IDS
from read47 import select_nodes
references=[]
for batch in sorted(ROOT.glob('batch_[0-9][0-9]')):
    if int(batch.name[-2:])>13:continue
    for p in batch.rglob('design.json'):
        if 'primary_history_evidence' in p.parts:continue
        d=json.loads(p.read_text(encoding='utf-8-sig'))
        filtered={k:v for k,v in d.items() if any(s in k.lower() for s in ['mechanism','marker','intent','reason','information','geometry','hypothesis'])}
        references.append({'path':str(p),'sha256':sha(p),'information_fields':filtered})
dump(OWN/'delivered_reference_study.json',references)
print(json.dumps(references,ensure_ascii=False,separators=(',',':')))
p=ROOT/'plane_explore/checkpoint.json'
v=json.loads(p.read_text(encoding='utf-8-sig'))
print('OLD_INITIAL_CHECKPOINT_KEYS',list(v))
for qid in IDS:
    def relevant(x, prefix=''):
        if isinstance(x,dict):
            return {k:vv for k,vv in x.items() if qid in json.dumps(vv,ensure_ascii=False) or k==qid}
        return x
    print(qid,json.dumps(relevant(v),ensure_ascii=False,separators=(',',':'))[:700])
