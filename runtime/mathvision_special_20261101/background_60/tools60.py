from bootstrap import *
import gc
import hashlib
import json
from datetime import datetime, timezone

IDS = ['Plane271','Plane335','Plane355','Plane365','Plane367','Plane386','Plane387','Plane449']
RELATED = ['Plane186','Plane394','Plane330','Plane260']
BRANCH = 'PlaneGeometry'
def now(): return datetime.now(timezone.utc).isoformat()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p):
    if Path(p).is_file():
        with Path(p).open(encoding='utf-8-sig') as f:
            for line in f:
                if line.strip(): yield json.loads(line)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:
        json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def eligibility(qid):
    from dataset_tools.catalog import content, digest
    assert qid in IDS
    b=PROJECT/BRANCH
    r=next(r for r in rows(b/'dataset.jsonl') if r['id']==qid)
    a=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    c=content(PROJECT,BRANCH,r)
    accepted=[r for r in rows(b/'special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collected=[r for r in rows(b/'special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    special=b/'special_variant'/qid
    recipe=read(special/'recipes.json') if (special/'recipes.json').is_file() else None
    collection=read(special/'collection.json') if (special/'collection.json').is_file() else None
    files=[str(p) for leaf,glob in [('images','*.png'),('plugins','*.json')] for p in (special/leaf).glob(glob)]
    root=next(r for r in rows(PROJECT/'question_bank.jsonl') if r['id']==qid)
    valid=a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and digest(c)==a.get('content_sha256')
    return dict(question_id=qid,checked_at=now(),record=r,approval=a,current_content_sha256=digest(c),approval_matches_current=valid,
        accepted=accepted,collected=collected,recipe=recipe,collection=collection,formal_special_files=files,root_special_plugins=root.get('special_plugins'),
        authoritative_hashes={str(p.relative_to(PROJECT)):sha(p) for p in [b/'dataset.jsonl',PROJECT/'provenance/approvals.json',b/'special_variant/accepted_index.jsonl',b/'special_variant/collected_index.jsonl']},
        eligible=r['source_dataset']=='MathVision' and valid and not accepted and not collected and not recipe and not files and not (collection and collection.get('current')) and not root.get('special_plugins'),frozen_content=c)
def frozen_files(r):
    from dataset_tools.catalog import content
    b=PROJECT/BRANCH
    paths=[b/p for p in content(PROJECT,BRANCH,r)['files']]
    paths += [PROJECT/'AGENTS.md',PROJECT/'MATHPALETTE_PROTOCOL.md',b/'REDRAW_PROTOCOL.md',PROJECT/'provenance/approvals.json',PROJECT/'dataset_tools/mathvision_workbench.py',BASE/'runtime_isolation.py',BASE/'harness/quicktest3_isolated.py']
    paths += list((b/'workbench').glob('*.py'))+[b/'workbench/plugin.schema.json',b/'workbench/config.json',b/'workbench/README.md',b/'workbench/agent_prompt.md']
    return {str(p.resolve().relative_to(PROJECT)).replace('\\','/'):sha(p) for p in paths}
def setup():
    sys.path.insert(0,str(PROJECT/BRANCH/'workbench'))
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    cfg=load_config();cfg['runtime_dir']=str(HERE/'state');cfg['output_dir']=str(HERE/'output')
    return RendererAdapter(cfg),PluginRenderer,cfg
def inspect(qid):
    adapter,_,_=setup()
    from partial_style import object_paths
    from dataset_tools.mathvision_workbench import png_bytes
    from workbench_io import pixel_hash
    d=HERE/qid;d.mkdir(exist_ok=True)
    e=eligibility(qid);write(d/'eligibility_initial.json',e);assert e['eligible']
    write(d/'formal_record.json',e['record']);write(d/'source_hashes_initial.json',frozen_files(e['record']))
    c=adapter.inspect_question(qid);write(d/'context.json',c)
    s=adapter.scene(qid)
    try:
        data=png_bytes(s);(d/'baseline.png').write_bytes(data)
        assert pixel_hash(data)==pixel_hash(PROJECT/BRANCH/e['record']['image'])
        paths={o['id']:[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[seg['control'].tolist() for seg in p['segments']]} for p in object_paths(s,o['id'])] for o in c['objects'] if o.get('styleable')}
        write(d/'exact_paths.json',paths)
    finally: s.close()
    write(d/'baseline_check.json',dict(no_op_pixel_equal=True,baseline_sha256=sha(d/'baseline.png'),formal_sha256=sha(PROJECT/BRANCH/e['record']['image']),isolation=ISOLATION))
    import matplotlib.pyplot as plt
    plt.close('all');del s,c,adapter,data;gc.collect()
    print(qid,'current approval / eligible / native no-op equal',flush=True)
if __name__=='__main__':
    for qid in sys.argv[1:]: inspect(qid)
