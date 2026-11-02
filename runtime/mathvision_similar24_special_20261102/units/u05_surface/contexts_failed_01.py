from worker_env import *
from delivery_bridge_adapter import RendererAdapter
from renderer_adapter import scene_png
from workbench_io import load_config, pixel_hash
config=load_config(PROJECT/'SolidGeometry/workbench/config.json')
adapter=RendererAdapter(config)
for qid in ('Solid186','Solid226'):
    folder=OWN/qid
    context=adapter.inspect_question(qid)
    save(folder/'fresh_context.json',context,True)
    scene=adapter.scene(qid)
    try:
        data,ph=scene_png(scene)
        (folder/'no_op.png').write_bytes(data)
        save(folder/'no_op_audit.json',{'pixel':ph,'formal_pixel':pixel_hash(adapter.original_paths[qid]),'matches':ph==pixel_hash(adapter.original_paths[qid]),'png_sha':hashlib.sha256(data).hexdigest(),'context_sha':sha(folder/'fresh_context.json')},True)
    finally: scene.close()
    native=next((PROJECT/'SolidGeometry'/p for p in adapter.records[qid]['runtime_dependencies'] if p.endswith('/scene.json')))
    s=load(native)
    save(folder/'native_scene_snapshot.json',s,True)
    print(json.dumps({'qid':qid,'native_scene':str(native),'solid_models':s.get('solid_models'),
      'projection':s['projection'],'visibility':{k:v for k,v in s['visibility'].items() if k!='edge_checks'},
      'objects':[{**o,'world_endpoints':[s['points'][p] for p in o.get('points',[])]} for o in s['objects']],
      'context_keys':list(context),'snap_points_count':len(context['snap_points'])},ensure_ascii=False),flush=True)
