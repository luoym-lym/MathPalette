import bootstrap
from bootstrap import OWN,ROOT,HISTORY
import json,sys
qid=sys.argv[1]
c=json.loads((OWN/qid/'context.json').read_text(encoding='utf-8'))
print('CONTEXT',qid)
for o in c['objects']:
    if o.get('styleable'):print(o['id'],json.dumps(o.get('geometry',{}),separators=(',',':')))
p=ROOT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/qid/'scene.json'
s=json.loads(p.read_text(encoding='utf-8-sig'))
print('SEMANTIC_METADATA',json.dumps({k:v for k,v in s.items() if k not in ['objects','visibility','labels','points','view','constraints']},ensure_ascii=False,separators=(',',':')))
for cp in HISTORY.glob('background_*/checkpoint.json'):
    if cp.is_relative_to(OWN):continue
    def walk(o):
        if isinstance(o,dict):
            if o.get('question_id')==qid and ('assessed' in o or 'decision' in o or 'reason' in o or 'screening' in o):print(str(cp),'ASSESSMENT',json.dumps(o,ensure_ascii=False,separators=(',',':')))
            else:
                for v in o.values():walk(v)
        elif isinstance(o,list):
            for v in o:walk(v)
    walk(json.loads(cp.read_text(encoding='utf-8-sig')))
