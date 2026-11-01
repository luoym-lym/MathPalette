from pathlib import Path
import os,sys,json
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR']=str(OUT/'mpl_cache')
os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from workbench_io import load_config
from renderer_adapter import RendererAdapter
from PIL import Image,ImageDraw
cfg=load_config()
cfg['runtime_dir']=str(OUT/'state')
cfg['output_dir']=str(OUT/'outputs')
adapter=RendererAdapter(cfg)
ids=['Solid165','Solid202','Solid243','Solid244','Solid248','Solid171','Solid223','Solid195','Solid106','Solid169','Solid185','Solid225']
canvas=Image.new('RGB',(4*330,3*355),'white')
draw=ImageDraw.Draw(canvas)
summary=[]
for n,qid in enumerate(ids):
    try:
        meta=adapter.inspect_question(qid)
        (OUT/f'{qid}_context.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
        status='ok'
    except Exception as e:
        status=type(e).__name__+': '+str(e)
    rec=adapter.records[qid]
    summary.append({'id':qid,'question':rec['question'],'answer':rec['answer'],'baseline':status})
    im=Image.open(adapter.original_paths[qid]).convert('RGB').resize((330,330))
    x,y=n%4*330,n//4*355
    canvas.paste(im,(x,y+25)); draw.text((x+8,y+5),qid+' | '+str(rec['answer']),fill='black')
canvas.save(OUT/'original_contact.png')
(OUT/'probe_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))
