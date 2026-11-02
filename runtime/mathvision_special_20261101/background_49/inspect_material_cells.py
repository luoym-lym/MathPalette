import research_env as env
import json
from inspect_sources import save
s=json.loads((env.ROOT/'Solid163/formal_scene.json').read_text(encoding='utf-8'))
n=json.loads((env.PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Solid163/scene.json').read_text(encoding='utf-8'))
print('EXTRAS',list(set(n)-set(s)))
print('MATERIALS',json.dumps(n.get('semantic_materials'),ensure_ascii=False))
print('MODEL',json.dumps(n.get('semantic_models'),ensure_ascii=False))
print('TWO_VIEW',json.dumps(n.get('two_view_verification'),ensure_ascii=False))
faces=[o for o in n['objects'] if o['type']=='face']
print('FACES',json.dumps(faces,ensure_ascii=False,separators=(',',':')))
save(env.ROOT/'Solid163/actual_material_faces.json',faces)
