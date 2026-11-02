from pathlib import Path
import os, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=HERE.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
def own_guard(event,args):
    def check(p):
        if isinstance(p,int) or p is None:return
        p=Path(os.fsdecode(p)).resolve()
        if not p.is_relative_to(HERE):raise PermissionError('background_42 write outside own root: '+str(p))
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(own_guard)
sys.path.insert(0,str(BASE));sys.path.insert(0,str(ROOT))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
import json, hashlib, importlib.util
from datetime import datetime,timezone
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
ASSIGNED=['Plane413','Plane418','Plane420','Plane451','Plane459','Plane470','Plane478','Plane485']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,v):
    p=Path(p);assert p.resolve().is_relative_to(HERE);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(p):return [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    b=ROOT/'PlaneGeometry';record=next(r for r in rows(b/'dataset.jsonl') if r['id']==qid);reasons=[]
    if record['source_dataset']!='MathVision':reasons.append('not_MathVision')
    from dataset_tools.catalog import content,digest
    a=read(ROOT/'provenance/approvals.json')['approvals'].get(qid,{})
    d=digest(content(ROOT,'PlaneGeometry',record))
    valid=a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and d==a.get('content_sha256')
    if not valid:reasons.append('invalid_approval')
    state={}
    for name in ('accepted_index.jsonl','collected_index.jsonl'):
        p=b/'special_variant'/name;state[str(p.relative_to(ROOT))]=file_hash(p) if p.exists() else None
        if any(r.get('question_id',r.get('id'))==qid for r in rows(p)):reasons.append(name)
    for name in ('recipes.json','collection.json'):
        p=b/'special_variant'/qid/name;state[str(p.relative_to(ROOT))]=file_hash(p) if p.exists() else None
        if p.exists():
            data=read(p)
            if name=='collection.json':
                cur=data.get('current',{})
                if cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'):reasons.append('special_completion')
            else:
                entries=data if isinstance(data,list) else data.get('recipes',data.get('variants',[]))
                if isinstance(entries,dict):entries=list(entries.values())
                if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed_recipe')
    for p in BASE.glob('batch_*/manifest.json'):
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered_'+p.parent.name)
    return {'question_id':qid,'checked_at':now(),'eligible':not reasons,'reasons':reasons,'formal_record':record,'approval':{'valid_current_content':valid,'current_content_sha256':d,'recorded_content_sha256':a.get('content_sha256'),'approved_at_utc':a.get('approved_at_utc'),'instruction':a.get('instruction')},'authoritative_state_hashes':state}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'state');cfg['output_dir']=str(HERE/'output');return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];b=ROOT/'PlaneGeometry'
    paths=[b/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths+=list(ad.input_files.values())+[ROOT/'MATHPALETTE_PROTOCOL.md',b/'REDRAW_PROTOCOL.md',b/'dataset_generator/protocol.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect(qid):
    e=eligibility(qid);write(HERE/qid/'eligibility_start.json',e);assert e['eligible'],e['reasons']
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid)
    write(HERE/qid/'context.json',meta);write(HERE/qid/'input_fingerprints.json',before)
    sc=ad.scene(qid)
    try:
        sc.fig.canvas.draw();paths={o['id']:object_paths(sc,o['id']) for o in meta['objects']}
        from dataset_tools.mathvision_workbench import png_bytes
        data=png_bytes(sc);(HERE/qid/'noop.png').write_bytes(data)
        write(HERE/qid/'exact_paths.json',{oid:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in ps] for oid,ps in paths.items()})
    finally:sc.close()
    assert pixel_hash(data)==meta['original_pixel_sha256'];assert inputs(ad,qid)==before
    print(json.dumps({'qid':qid,'eligible':True,'noop':True,'objects':meta['objects']},ensure_ascii=False),flush=True)
if __name__=='__main__':
    for q in sys.argv[1:]:inspect(q)
