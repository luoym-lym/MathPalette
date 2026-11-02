from pathlib import Path
import os,sys,json,hashlib,importlib.util
from datetime import datetime,timezone
TASK=Path(__file__).resolve().parent
ROOT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=TASK.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k,n in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    d=TASK/n;d.mkdir(parents=True,exist_ok=True);os.environ[k]=str(d)
def owncheck(p):
    if isinstance(p,int) or p is None:return
    if not Path(os.fsdecode(p)).resolve().is_relative_to(TASK):raise PermissionError('background_38 write outside own scope: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,environment_versions,pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
CONFIG=load_config();CONFIG['runtime_dir']=str(TASK/'state');CONFIG['output_dir']=str(TASK/'output')
AD=RendererAdapter(CONFIG)
ASSIGN=json.loads((BASE/'background_38_assignment.json').read_text(encoding='utf-8-sig'))
QIDS=ASSIGN['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p):return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).is_file() else []
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canon(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def eligibility(q):
    assert q in QIDS
    from dataset_tools.catalog import content,digest
    b=ROOT/'PlaneGeometry';record=AD.records[q];approval=read(ROOT/'provenance/approvals.json')['approvals'][q]
    current=digest(content(ROOT,'PlaneGeometry',record));reasons=[]
    if record['source_dataset']!='MathVision':reasons.append('not MathVision')
    if approval['reviewer']!='user' or not approval['instruction'] or approval['content_sha256']!=current:reasons.append('approval invalid')
    evidence={}
    for f,stat in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=b/'special_variant'/f;evidence[f]=[r for r in rows(p) if r.get('question_id')==q]
        if any(r.get('status')==stat for r in evidence[f]):reasons.append(f)
    for f in ['recipes.json','collection.json']:
        p=b/'special_variant'/q/f;evidence[f]=read(p) if p.is_file() else None
        if p.is_file():reasons.append('existing '+f+' requires manual read')
    manifests=[str(p.relative_to(ROOT)) for p in BASE.glob('batch_*/manifest.json') if q in p.read_text(encoding='utf-8-sig')]
    if manifests:reasons.append('delivered')
    return dict(question_id=q,checked_at=now(),eligible=not reasons,reasons=reasons,formal_record=record,formal_record_sha256=canon(record),approval=approval,current_content_sha256=current,approval_matches_current=current==approval['content_sha256'],special=evidence,delivered_manifests=manifests,mutable_progress_role='diagnostic only; not frozen source')
def paths(q,targets):
    s=AD.scene(q)
    try:
        s.fig.canvas.draw()
        return {t:[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[seg['control'].tolist() for seg in p['segments']]} for p in object_paths(s,t)] for t in targets}
    finally:s.close()
def init():
    if not (TASK/'isolation.json').exists():write(TASK/'isolation.json',dict(root=str(TASK),isolation=ISOLATION,env={k:os.environ[k] for k in ['TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME']},python=sys.version,started_at=now()))
    source=BASE/'harness/quicktest3_isolated.py';dest=TASK/'harness/quicktest3_isolated.py';dest.parent.mkdir(exist_ok=True);dest.write_bytes(source.read_bytes())
    protected={}
    for q in QIDS:
        folder=TASK/q;folder.mkdir(exist_ok=True)
        e=eligibility(q);assert e['eligible'],e
        if not (folder/'eligibility_at_start.json').exists():write(folder/'eligibility_at_start.json',e)
        context=AD.inspect_question(q)
        if not (folder/'context.json').exists():write(folder/'context.json',context)
        if not (folder/'formal_record.json').exists():write(folder/'formal_record.json',AD.records[q])
        if not (folder/'original.png').exists():(folder/'original.png').write_bytes(AD.original_paths[q].read_bytes())
        r=AD.records[q]
        for key in ['image','original_image','scene','script']:
            if r.get(key):p=ROOT/'PlaneGeometry'/r[key];protected[str(p.relative_to(ROOT))]=sha(p)
        for dep in r.get('runtime_dependencies',[]):p=ROOT/'PlaneGeometry'/dep;protected[str(p.relative_to(ROOT))]=sha(p)
        print(q,r['question'],r['answer'],'objects',len(context['objects']),flush=True)
    for p in [ROOT/'provenance/approvals.json',ROOT/'PlaneGeometry/dataset.jsonl',ROOT/'PlaneGeometry/workbench/mathvision_adapter.py',ROOT/'PlaneGeometry/workbench/mathvision_plugins.py',BASE/'harness/quicktest3_isolated.py',BASE/'runtime_isolation.py']:
        protected[str(p.relative_to(ROOT))]=sha(p)
    write(TASK/'protected_sources_before.json',protected)
if __name__=='__main__':init()
