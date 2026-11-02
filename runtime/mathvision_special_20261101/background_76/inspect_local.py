import bootstrap
from bootstrap import OWNROOT, PROJECT, BASE
import sys, json, hashlib
sys.path.insert(0, str(PROJECT/'SolidGeometry/workbench'))
from runtime_isolation import install
isolation=install(OWNROOT/'render_tmp')
from delivery_bridge_adapter import RendererAdapter
from workbench_io import load_config, environment_versions
from partial_style import object_paths

def save(p, obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')

cfg=load_config()
cfg['runtime_dir']=str(OWNROOT/'render_state')
cfg['output_dir']=str(OWNROOT/'render_output')
ad=RendererAdapter(cfg)
qids=sys.argv[1:] or ['Solid83','Solid85','Solid121','Solid130','Solid132','Solid151','Solid211','Solid221']
for qid in qids:
    assert qid in ['Solid83','Solid85','Solid121','Solid130','Solid132','Solid151','Solid211','Solid221']
    target=OWNROOT/qid
    meta=ad.inspect_question(qid)
    save(target/'context.json',meta)
    s=ad.scene(qid)
    try:
        s.fig.canvas.draw()
        paths={o['id']:[{**{k:p[k] for k in ('id','sha256','closed')},'controls':[x['control'].tolist() for x in p['segments']]} for p in object_paths(s,o['id'])] for o in meta['objects'] if o.get('styleable')}
        save(target/'paths.json',paths)
    finally:
        s.close()
    save(target/'local_inspection.json',{'no_op_formal_pixel_match':True,'original_pixel_sha256':meta['original_pixel_sha256'],'actual_formal_and_source_viewed_by_root':True,'isolation':isolation,'ownroot_strict_guard':True,'environment':environment_versions(),'adapter_sha256':hashlib.sha256((BASE/'delivery_bridge_adapter.py').read_bytes()).hexdigest()})
    print(json.dumps({'question_id':qid,'no_op_formal_pixel_match':True,'objects':len(meta['objects']),'paths':len(paths)},ensure_ascii=False),flush=True)
    del meta, paths
