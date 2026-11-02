from bootstrap import *
import json
import hashlib
from datetime import datetime, timezone
from dataset_tools.catalog import content, digest
IDS=['Solid79','Solid214','Solid216','Solid225','Solid232','Solid233','Solid234','Solid247']
BRANCH='SolidGeometry'
def now(): return datetime.now(timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p): return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).is_file() else []
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f: json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def eligibility(qid):
    assert qid in IDS
    branch=PROJECT/BRANCH
    r=next(r for r in rows(branch/'dataset.jsonl') if r['id']==qid)
    a=read(PROJECT/'provenance/approvals.json')['approvals'].get(qid,{})
    payload=content(PROJECT,BRANCH,r)
    accepted=[r for r in rows(branch/'special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collected=[r for r in rows(branch/'special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    special=branch/'special_variant'/qid
    files=[str(p) for folder,ext in [('plugins','*.json'),('images','*.png')] for p in (special/folder).glob(ext)]
    collection=read(special/'collection.json') if (special/'collection.json').is_file() else None
    recipe=read(special/'recipes.json') if (special/'recipes.json').is_file() else None
    root=next(r for r in rows(PROJECT/'question_bank.jsonl') if r['id']==qid)
    valid=a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and digest(payload)==a.get('content_sha256')
    return dict(checked_at=now(),question_id=qid,record=r,approval=a,current_content_sha256=digest(payload),approval_matches_current=valid,
        accepted=accepted,collected=collected,formal_special_files=files,collection=collection,recipe=recipe,root_special_plugins=root.get('special_plugins'),
        eligible=r['source_dataset']=='MathVision' and valid and not accepted and not collected and not files and not recipe and not (collection and collection.get('current')) and not root.get('special_plugins'),frozen_content=payload)
def frozen_files(r):
    branch=PROJECT/BRANCH
    ps=[branch/p for p in content(PROJECT,BRANCH,r)['files']]
    ps += [PROJECT/'provenance/approvals.json',PROJECT/'AGENTS.md',PROJECT/'MATHPALETTE_PROTOCOL.md',branch/'REDRAW_PROTOCOL.md',branch/'dataset_generator/protocol.json',PROJECT/'dataset_tools/mathvision_workbench.py',BASE/'delivery_bridge_adapter.py',BASE/'runtime_isolation.py',BASE/'harness/quicktest3_isolated.py']
    ps += list((branch/'workbench').glob('*.py'))+[branch/'workbench/plugin.schema.json',branch/'workbench/config.json',branch/'workbench/README.md',branch/'workbench/agent_prompt.md']
    return {str(p.relative_to(PROJECT)).replace('\\','/'):sha(p) for p in ps}
def setup():
    sys.path.insert(0,str(PROJECT/BRANCH/'workbench'))
    from workbench_io import load_config
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    cfg=load_config();cfg['runtime_dir']=str(HERE/'state');cfg['output_dir']=str(HERE/'output')
    return RendererAdapter(cfg),PluginRenderer,cfg
def inspect(qid):
    adapter,_,_=setup()
    from PIL import Image
    from partial_style import object_paths
    from dataset_tools.mathvision_workbench import png_bytes
    d=HERE/qid;d.mkdir(exist_ok=True)
    e=eligibility(qid)
    write(d/('eligibility_bridge.json' if (d/'eligibility_initial.json').exists() else 'eligibility_initial.json'),e);assert e['eligible']
    for name,value in [('formal_record.json',e['record']),('source_hashes_initial.json',frozen_files(e['record']))]:
        if (d/name).exists(): assert read(d/name)==value
        else: write(d/name,value)
    c=adapter.inspect_question(qid);write(d/'context.json',c)
    scene=adapter.scene(qid)
    try:
        (d/'baseline.png').write_bytes(png_bytes(scene))
        with Image.open(PROJECT/BRANCH/e['record']['image']) as a,Image.open(d/'baseline.png') as b:
            assert a.size==b.size==(768,768) and a.convert('RGBA').tobytes()==b.convert('RGBA').tobytes()
        scene.fig.canvas.draw()
        paths={o['id']:[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,o['id'])] for o in c['objects'] if o.get('styleable')}
        write(d/'exact_paths.json',paths)
    finally: scene.close()
    write(d/'baseline_check.json',dict(no_op_pixel_equal=True,baseline_sha256=sha(d/'baseline.png'),formal_sha256=sha(PROJECT/BRANCH/e['record']['image']),isolation=ISOLATION))
    print(qid,'eligible / original approval current / no-op equal / objects',len(c['objects']),flush=True)
if __name__=='__main__':
    for qid in sys.argv[1:]: inspect(qid)
