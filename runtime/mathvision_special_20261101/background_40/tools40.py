from pathlib import Path
import os,sys,json,hashlib,copy
from datetime import datetime,timezone
TASK=Path(__file__).resolve().parent
ROOT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=TASK.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'temp','TMP':'temp','TMPDIR':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=TASK/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
def owncheck(path):
    if path is None or isinstance(path,int):return
    if not Path(os.fsdecode(path)).resolve().is_relative_to(TASK):raise PermissionError('Unit40 write outside own root: '+str(path))
def own_guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(own_guard)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from renderer_adapter import scene_png
from workbench_io import load_config,pixel_hash,file_hash,canonical_hash,environment_versions
CONFIG=load_config();CONFIG['runtime_dir']=str(TASK/'state');CONFIG['output_dir']=str(TASK/'output')
AD=RendererAdapter(CONFIG)
ASSIGN=json.loads((BASE/'background_40_assignment.json').read_text(encoding='utf-8-sig'))
IDS=ASSIGN['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(x,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def jl(p):return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []
def eligibility(q):
    assert q in IDS
    from dataset_tools.catalog import content,digest
    record=next(r for r in jl(ROOT/'SolidGeometry/dataset.jsonl') if r['id']==q)
    approval=read(ROOT/'provenance/approvals.json')['approvals'].get(q,{})
    fingerprint=digest(content(ROOT,'SolidGeometry',record));reasons=[];special={}
    if record['source_dataset']!='MathVision':reasons.append('not formal MathVision')
    if approval.get('reviewer')!='user' or not approval.get('instruction') or fingerprint!=approval.get('content_sha256'):reasons.append('approval mismatch')
    for n in ['accepted_index.jsonl','collected_index.jsonl']:
        p=ROOT/'SolidGeometry/special_variant'/n
        rows=[r for r in jl(p) if r.get('question_id')==q];special[n]=rows
        if rows:reasons.append(n+' has current question record')
    for n in ['recipes.json','collection.json']:
        p=ROOT/'SolidGeometry/special_variant'/q/n
        if p.exists():
            special[n]=read(p)
            if n=='recipes.json':
                x=special[n];entries=x if isinstance(x,list) else x.get('recipes',x.get('variants',[]))
                if isinstance(entries,dict):entries=list(entries.values())
                if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries):reasons.append('passed recipe')
            else:
                c=special[n].get('current',{})
                if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collected or special-completed')
    for p in BASE.glob('batch_*/manifest.json'):
        if q in p.read_text(encoding='utf-8-sig'):reasons.append('already delivered '+str(p))
    return {'question_id':q,'checked_at':now(),'eligible':not reasons,'reasons':reasons,'formal_record_sha256':canonical_hash(record),'approval_content_actual':fingerprint,'approval_matches_current':fingerprint==approval.get('content_sha256'),'approval':approval,'authoritative_special_records':special,'mutable_progress_is_diagnostic_only':True}
def frozen(q):
    r=AD.records[q];paths=[r['image'],r['scene'],r['script'],*r.get('runtime_dependencies',[])]
    if r.get('original_image'):paths.append(r['original_image'])
    files={str((AD.branch/p).relative_to(ROOT)):file_hash(AD.branch/p) for p in set(paths)}
    for p in ['dataset_tools/catalog.py','dataset_tools/mathvision_workbench.py','SolidGeometry/workbench/render_plugins.py','SolidGeometry/workbench/plugin.schema.json','SolidGeometry/workbench/partial_style.py','SolidGeometry/workbench/quick_test.py','SolidGeometry/workbench/config.json','runtime/mathvision_special_20261101/delivery_bridge_adapter.py','runtime/mathvision_special_20261101/harness/quicktest3_isolated.py']:
        files[p]=file_hash(ROOT/p)
    return {'record_sha256':canonical_hash(r),'files':files,'environment':environment_versions()}
def inspect(q):
    e=eligibility(q);assert e['eligible'],e
    d=TASK/q;d.mkdir(exist_ok=False)
    write(d/'eligibility_at_start.json',e);write(d/'formal_record.json',AD.records[q]);write(d/'frozen_inputs.json',frozen(q))
    ctx=AD.inspect_question(q);write(d/'context.json',ctx);write(d/'source_scene_snapshot.json',read(AD.branch/AD.records[q]['scene']))
    s=AD.scene(q)
    try:data,pix=scene_png(s)
    finally:s.close()
    (d/'noop.png').write_bytes(data)
    assert pix==pixel_hash(AD.original_paths[q])
    print(q,'eligible; noop pixels match;',len(ctx['objects']),'objects',flush=True)
if __name__=='__main__':
    for q in sys.argv[1:]:inspect(q)
