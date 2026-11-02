from common23 import *
branch=sys.argv[1]
sys.path.insert(0,str(ROOT/branch/'workbench'))
from workbench_io import load_config,pixel_hash
if branch=='PlaneGeometry':
    from mathvision_adapter import RendererAdapter
else:
    from delivery_bridge_adapter import RendererAdapter
config=load_config();config['runtime_dir']=str(OUT/'state');config['output_dir']=str(OUT/'output')
ad=RendererAdapter(config)
for qid in sys.argv[2:]:
    audit=eligibility(qid);assert audit['eligible'];write(OUT/qid/'eligibility_fresh_context.json',audit)
    meta=ad.inspect_question(qid);write(OUT/qid/'fresh_context.json',meta)
    from dataset_tools.mathvision_workbench import png_bytes
    scene=ad.scene(qid)
    try:data=png_bytes(scene)
    finally:scene.close()
    (OUT/qid/'noop.png').write_bytes(data)
    assert pixel_hash(data)==pixel_hash(ROOT/branch/audit['formal_record']['image'])
    print(qid)
    for o in meta['objects']:
        if qid=='Plane373':continue
        if qid=='Plane192' and not o['id'].startswith('route'):continue
        if qid=='Plane233' and not o['id'].startswith(('given_','B_')):continue
        print(json.dumps(o,ensure_ascii=False,separators=(',',':')))
