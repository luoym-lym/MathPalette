import os, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=HERE.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
def own_guard(event,args):
    def check(p):
        if p is None or isinstance(p,int):return
        if not Path(os.fsdecode(p)).resolve().is_relative_to(HERE):raise PermissionError('background39 outside own root: '+str(p))
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(own_guard)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
import json,hashlib,copy,importlib.util
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools import catalog
ASSIGNED=json.loads((BASE/'background_39_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,v):
    p=Path(p);assert p.resolve().is_relative_to(HERE);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(p):return [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []
def eligibility(q):
    assert q in ASSIGNED
    br=ROOT/'PlaneGeometry';r=next(r for r in rows(br/'dataset.jsonl') if r['id']==q);reasons=[]
    if r.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    a=read(ROOT/'provenance/approvals.json')['approvals'].get(q,{})
    d=catalog.digest(catalog.content(ROOT,'PlaneGeometry',r))
    if a.get('reviewer')!='user' or not a.get('instruction') or not a.get('approved_at_utc') or d!=a.get('content_sha256'):reasons.append('invalid_original_approval')
    paths=[br/'dataset.jsonl',ROOT/'provenance/approvals.json']
    for n in ['accepted_index.jsonl','collected_index.jsonl']:
        p=br/'special_variant'/n;paths.append(p)
        if any(x.get('question_id',x.get('id'))==q for x in rows(p)):reasons.append(n)
    for n in ['recipes.json','collection.json']:
        p=br/'special_variant'/q/n;paths.append(p)
        if p.exists() and read(p):reasons.append('existing_'+n)
    for p in BASE.glob('batch_*/manifest.json'):
        if q in p.read_text(encoding='utf-8-sig'):reasons.append('delivered:'+p.parent.name)
    return {'question_id':q,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'formal_record':r,'original_approval':a,'current_original_content_sha256':d,'original_approval_matches':d==a.get('content_sha256'),'state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths}}
def adapter():
    c=load_config();c['runtime_dir']=str(HERE/'state');c['output_dir']=str(HERE/'output');return c,RendererAdapter(c)
def inputs(ad,q):
    r=ad.records[q];br=ROOT/'PlaneGeometry'
    ps=[br/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    ps+=list(ad.input_files.values())+[ROOT/'AGENTS.md',ROOT/'MATHPALETTE_PROTOCOL.md',br/'REDRAW_PROTOCOL.md',br/'dataset_generator/protocol.json',br/'dataset.jsonl',ROOT/'provenance/approvals.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(ps))},'environment':environment_versions()}
def harness():
    src=BASE/'harness/quicktest3_isolated.py';dst=HERE/'harness/quicktest3_isolated.py';dst.parent.mkdir(exist_ok=True)
    if not dst.exists():dst.write_bytes(src.read_bytes())
    assert src.read_bytes()==dst.read_bytes()
    spec=importlib.util.spec_from_file_location('unchanged_background39_harness',dst);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    h.PROJECT=ROOT;h.RUNTIME=ROOT/'runtime';return h
if __name__=='__main__':
    cfg,ad=adapter()
    for q in ASSIGNED:
        e=eligibility(q);assert e['eligible'],e;write(HERE/q/'eligibility_start.json',e)
        before=inputs(ad,q);m=ad.inspect_question(q)
        write(HERE/q/'context.json',m);write(HERE/q/'formal_record.json',ad.records[q]);write(HERE/q/'input_fingerprints.json',before)
        sc=ad.scene(q)
        try:
            sc.fig.canvas.draw()
            paths={o['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[s['control'].tolist() for s in p['segments']]} for p in object_paths(sc,o['id'])] for o in m['objects']}
        finally:sc.close()
        write(HERE/q/'all_native_paths.json',paths)
        assert before==inputs(ad,q)
        print(q,'eligible; no-op exact;',len(m['objects']),'objects',flush=True)
