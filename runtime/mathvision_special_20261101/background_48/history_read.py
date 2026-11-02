import task_env
from task_env import OWN
from prepare import read
from pathlib import Path
import sys, json
qid=sys.argv[1]
mode=sys.argv[2] if len(sys.argv)>2 else 'raw'
for e in read(OWN/'old_history_inventory.json')[qid]:
    p=Path(e['path'])
    if qid not in p.parts: continue
    if mode=='raw' and p.name.endswith('_response.json'):
        print('FULL RAW ANSWER',p)
        raw=p.read_bytes()
        try:
            d=json.loads(raw); c=d['choices'][0]
            t=c['message']['content']; print('finish_reason',c['finish_reason'],'content chars',len(t))
            start=int(sys.argv[3]) if len(sys.argv)>3 else 0
            end=int(sys.argv[4]) if len(sys.argv)>4 else len(t)
            print(t[start:end])
        except Exception as err: print('HISTORICAL PARSE FAILURE PRESERVED',str(err),'bytes',len(raw))
    elif mode=='old' and (p.name in ('design.json','plugin.json','primary_review.json','primary_visual_review.json','primary_prescreen.json','prescreen_assessment.json','math_proof.json','mathematical_audit.json') or 'assess' in p.name):
        print('FULL OLD',p); print(p.read_text(encoding='utf-8-sig'))
