from unit_env import *
from dataset_tools.mathvision_workbench import png_bytes
from partial_style import object_paths
from workbench_io import pixel_hash, environment_versions

config, adapter, first = adapter_context(QIDS[0])
for qid in QIDS:
    meta = first if qid == QIDS[0] else adapter.inspect_question(qid)
    save(OWN / qid / 'context_v2.json', meta)
    scene = adapter.scene(qid)
    try:
        data = png_bytes(scene)
        (OWN / qid / 'noop_v2.png').write_bytes(data)
        assert pixel_hash(data) == pixel_hash(PROJECT / 'PlaneGeometry' / 'image' / (qid+'.png'))
        scene.fig.canvas.draw()
        paths = {obj['id']:[{k:p[k] for k in ('id','sha256','closed')} for p in object_paths(scene,obj['id'])]
                 for obj in meta['objects'] if obj['styleable']}
        save(OWN / qid / 'paths_v2.json', paths)
    finally:
        scene.close()
    print(qid, 'SNAP',json.dumps(meta['snap_points'],ensure_ascii=False))
    print(qid,'OBJECTS',json.dumps([{k:o[k] for k in ('id','type','styleable') if k in o} for o in meta['objects']],ensure_ascii=False))
save(OWN / 'capture_environment.json',{'created_at':now(),'versions':environment_versions(),
                                     'manifest':adapter.manifest,'isolation':ISOLATION})
