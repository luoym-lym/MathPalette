import bootstrap
from bootstrap import OWN,ROOT,HISTORY
import sys,json
qid=sys.argv[1]
manifest=json.loads((OWN/qid/'old_evidence_manifest.json').read_text(encoding='utf-8'))
selected=[]
for entry in manifest:
    p=ROOT/entry['path'];n=p.name
    if n in ('design.json','plugin.json') or n.endswith('_response.json') or ('review' in n or 'audit' in n) and n.endswith('.json'):
        selected.append((p,json.dumps(json.loads(p.read_text(encoding='utf-8-sig')),ensure_ascii=False,separators=(',',':'))))
for checkpoint in HISTORY.glob('background_*/checkpoint.json'):
    if checkpoint.is_relative_to(OWN):continue
    data=json.loads(checkpoint.read_text(encoding='utf-8-sig'))
    for k in ('assessments','question_assessments','questions','results'):
        v=data.get(k,[])
        if isinstance(v,dict):v=[{'question_id':key,**value} for key,value in v.items() if isinstance(value,dict)]
        for item in v:
            if isinstance(item,dict) and item.get('question_id')==qid:selected.append((checkpoint,json.dumps(item,ensure_ascii=False,separators=(',',':'))))
out='\n'.join(str(p.relative_to(ROOT))+'\n'+t for p,t in selected)
(OWN/qid/'old_full_text_read.txt').write_text(out,encoding='utf-8')
print(out)
