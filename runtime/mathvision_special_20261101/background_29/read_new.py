import bootstrap
from bootstrap import OWN
import sys,json
for q in sys.argv[1:]:
    print(q)
    for p in sorted((OWN/q).glob('r29_*/tests/*/run_*_response.json')):
        data=json.loads(p.read_text(encoding='utf-8-sig'))
        print(p)
        print(json.dumps(data,ensure_ascii=False,indent=2))
