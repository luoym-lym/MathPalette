import os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE = HERE.parent
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
for key, name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name; p.mkdir(parents=True,exist_ok=True); os.environ[key]=str(p)
def own_guard(event,args):
    def check(p):
        if isinstance(p,int) or p is None:return
        p=Path(os.fsdecode(p)).resolve()
        if not p.is_relative_to(HERE):raise PermissionError('background_41 write outside own root: '+str(p))
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(own_guard)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
import json, hashlib, importlib.util, copy
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
ASSIGNED=['Plane427','Plane430','Plane434','Plane436','Plane437','Plane438','Plane440','Plane442']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,v):
    p=Path(p);assert p.resolve().is_relative_to(HERE);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(p):return [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if p.exists() else []
def eligibility(q):
    assert q in ASSIGNED
    b=ROOT/'PlaneGeometry';r=next(r for r in rows(b/'dataset.jsonl') if r['id']==q)
    from dataset_tools.catalog import content,digest
    a=read(ROOT/'provenance/approvals.json')['approvals'][q];c=content(ROOT,'PlaneGeometry',r);d=digest(c)
    valid=a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and d==a.get('content_sha256')
    matches={n:[v for v in rows(b/'special_variant'/n) if v.get('question_id',v.get('id'))==q] for n in ('accepted_index.jsonl','collected_index.jsonl')}
    records={n:read(b/'special_variant'/q/n) if (b/'special_variant'/q/n).exists() else None for n in ('recipes.json','collection.json')}
    delivered=[str(p) for p in BASE.glob('batch_*/manifest.json') if q in p.read_text(encoding='utf-8-sig')]
    eligible=r['source_dataset']=='MathVision' and valid and not any(matches.values()) and not any(records.values()) and not delivered
    return {'question_id':q,'checked_at_utc':now(),'eligible':eligible,'formal_record':r,'approval':a,'computed_current_content_sha256':d,'valid_current_user_approval':valid,'accepted_and_collected_matches':matches,'special_records':records,'delivered_matches':delivered,'frozen_content':c}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'state');cfg['output_dir']=str(HERE/'output');return cfg,RendererAdapter(cfg)
def harness():
    src=BASE/'harness/quicktest3_isolated.py';dst=HERE/'harness/quicktest3_isolated.py';dst.parent.mkdir(exist_ok=True)
    if not dst.exists():dst.write_bytes(src.read_bytes())
    assert dst.read_bytes()==src.read_bytes()
    spec=importlib.util.spec_from_file_location('background41_unchanged_harness',dst);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    h.PROJECT=ROOT;h.RUNTIME=ROOT/'runtime';return h
