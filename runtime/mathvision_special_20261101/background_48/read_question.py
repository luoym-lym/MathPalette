import task_env
from task_env import OWN, PROJECT
from prepare import read
import json, sys

for q in sys.argv[1:]:
    print('CURRENT SCENE',q)
    print(json.dumps(read(PROJECT/'PlaneGeometry/dataset_generator/scenes'/f'{q}.json'),ensure_ascii=False,separators=(',',':')))
    print('CURRENT NATIVE SCENE',q)
    native=read(PROJECT/f'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/{q}/scene.json')
    formal=read(PROJECT/'PlaneGeometry/dataset_generator/scenes'/f'{q}.json')
    print(json.dumps({k:v for k,v in native.items() if v!=formal.get(k)},ensure_ascii=False,separators=(',',':')))
    for e in read(OWN/'old_history_inventory.json')[q]:
        from pathlib import Path
        p=Path(e['path'])
        if q not in p.parts: continue
        names=('design.json','plugin.json','math_proof.json','mathematical_audit.json','primary_prescreen.json','prescreen_assessment.json','assessed.json','assessment.json','source_primary_audit.json','primary_review.json','primary_visual_review.json','primary_visual_review.json','manual_final_review.json','manual_finals.json')
        if p.name in names or p.name.endswith('_response.json'):
            print('OLD FULL',p)
            t=p.read_text(encoding='utf-8-sig')
            if p.name=='source_primary_audit.json':
                data=json.loads(t); data.pop('source_files',None); t=json.dumps(data,ensure_ascii=False,indent=2)
            print(t)
