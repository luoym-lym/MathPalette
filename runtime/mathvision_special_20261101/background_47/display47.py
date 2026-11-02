from env47 import *
import json
args=sys.argv[1:]
for qid in args:
    dossier=json.loads((OWN/qid/'reading_dossier.json').read_text(encoding='utf-8'))
    for d in dossier:
        name=Path(d['path']).name
        if name in ['scene.json','source.json','execution.json','protocol_review.json']:
            print(json.dumps(d,ensure_ascii=False,separators=(',',':')))
