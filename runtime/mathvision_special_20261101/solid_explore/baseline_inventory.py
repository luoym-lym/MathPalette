from pathlib import Path
import os,sys,json,time
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(OUT/'mpl_cache');sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import load_config
from renderer_adapter import RendererAdapter
cfg=load_config();cfg['runtime_dir']=str(OUT/'state');cfg['output_dir']=str(OUT/'outputs');adapter=RendererAdapter(cfg)
eligible=[json.loads(line) for line in (ROOT/'runtime/mathvision_special_20261101/SolidGeometry_eligible.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
results=[];began=time.monotonic()
for index,record in enumerate(eligible):
    qid=record.get('id',record.get('question_id'))
    try:
        meta=adapter.inspect_question(qid)
        result={'question_id':qid,'baseline_matches_formal':True,'pixel_sha256':meta['original_pixel_sha256'],'object_count':len(meta['objects']),'snap_point_count':len(meta['snap_points'])}
    except Exception as error:result={'question_id':qid,'baseline_matches_formal':False,'error':str(error)}
    results.append(result)
    if (index+1)%10==0:print(json.dumps({'processed':index+1,'total':len(eligible),'elapsed_seconds':round(time.monotonic()-began,1)},ensure_ascii=False),flush=True)
summary={'total':len(results),'baseline_ok':sum(r['baseline_matches_formal'] for r in results),'baseline_failed':sum(not r['baseline_matches_formal'] for r in results),'elapsed_seconds':round(time.monotonic()-began,1),'results':results,'note':'Read-only no-operation redraw checks only; formal files not changed. Failed baselines were not bypassed.'}
(OUT/'baseline_inventory.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='results'},ensure_ascii=False),flush=True)
