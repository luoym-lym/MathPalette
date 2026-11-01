import os, sys, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
os.environ['MPLCONFIGDIR']=str(HERE/'mplcache')
os.environ['TEMP']=os.environ['TMP']=str(HERE/'tmp')
(HERE/'tmp').mkdir(exist_ok=True)
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
sys.path.insert(0,str(ROOT))
from workbench_io import load_config
from mathvision_adapter import RendererAdapter
from runtime_bridge import isolate_native_temporary_files
isolate_native_temporary_files(HERE/'render_tmp')
config=load_config()
config['runtime_dir']=str(HERE/'render_runtime')
config['output_dir']=str(HERE/'render_output')
adapter=RendererAdapter(config)
ids=['Plane273','Plane287','Plane268','Plane255','Plane254','Plane282','Plane283','Plane236','Plane240','Plane249','Plane291','Plane230']
summary=[]
for qid in ids:
    try:
        meta=adapter.inspect_question(qid)
        (HERE/(qid+'_context.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
        summary.append({'id':qid,'objects':[{'id':o['id'],'kind':o['kind'],'geometry':o.get('geometry')} for o in meta['objects']], 'snap_points':meta['snap_points']})
        print(qid,'OK',flush=True)
    except Exception as exc: print(qid,type(exc).__name__,str(exc),flush=True)
(HERE/'probe_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
