import task_env
from task_env import OWN, PROJECT
from prepare import read
import json,sys
for q in sys.argv[1:]:
    s=read(PROJECT/'PlaneGeometry/dataset_generator/scenes'/f'{q}.json')
    n=read(PROJECT/f'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/{q}/scene.json')
    print(q,json.dumps(s,ensure_ascii=False,separators=(',',':')))
    print('NATIVE DIFFERENCES',json.dumps({k:v for k,v in n.items() if v!=s.get(k)},ensure_ascii=False,separators=(',',':')))
    c=read(OWN/q/'context.json')
    print('CANVAS KEYS',list(c['canvas']))
    for t in c['canvas'].get('targets',[]):
        print('TARGET',t.get('id'),t.get('object_id'),[(p.get('id'),p.get('closed'),p.get('sha256'),len(p.get('samples',[]))) for p in t.get('partial_paths',[])])
