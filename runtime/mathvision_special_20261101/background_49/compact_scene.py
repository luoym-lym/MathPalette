import research_env as env
import json,sys
for q in sys.argv[1:]:
 s=json.loads((env.ROOT/q/'formal_scene.json').read_text(encoding='utf-8'))
 print(q)
 print(json.dumps({k:v for k,v in s.items() if k not in ['objects','visibility']},ensure_ascii=False,separators=(',',':')))
 for o in s['objects']: print(json.dumps(o,ensure_ascii=False,separators=(',',':')))
 native=env.PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'/q/'scene.json'
 n=json.loads(native.read_text(encoding='utf-8'))
 print('NATIVE EXTRA',json.dumps({k:v for k,v in n.items() if k not in s},ensure_ascii=False,separators=(',',':')))
