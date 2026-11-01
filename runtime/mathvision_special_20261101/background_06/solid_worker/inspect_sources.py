from tools_local import *
import importlib.util
for qid in ASSIGNED:
    row=AD.records[qid];scene=AD.scenes[qid]
    print('\n'+qid)
    print('scene keys',list(scene))
    print('visibility keys',list(scene.get('visibility',{})))
    print('model',json.dumps(scene.get('visibility',{}).get('models',{}),separators=(',',':')))
    p=ROOT/'SolidGeometry'/next(p for p in row['runtime_dependencies'] if p.endswith('/source_redraw.py'))
    print('source_redraw',str(p))
    print(p.read_text(encoding='utf-8-sig'))
if not (TASK.parent/'formal_files_before.json').exists():
    spec=importlib.util.spec_from_file_location('_readonly_inventory',ROOT/'runtime/mathvision_special_20261101/inventory.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    write(TASK.parent/'formal_files_before.json',module.scan())
    write(TASK.parent/'prior_delivery_fingerprints.json',{str(p.relative_to(ROOT)):file_hash(p) for batch in ['batch_01','batch_02','batch_03','batch_04'] for p in (ROOT/'runtime/mathvision_special_20261101'/batch).rglob('*') if p.is_file()})
