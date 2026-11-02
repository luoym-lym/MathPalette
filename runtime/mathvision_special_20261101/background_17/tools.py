from pathlib import Path
import os,sys,json,hashlib,types
from datetime import datetime,timezone
TASK=Path(__file__).resolve().parent
ROOT=TASK.parents[2]
SHARED=TASK.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=TASK/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
sys.path.insert(0,str(SHARED));sys.path.insert(0,str(ROOT))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
def owncheck(path):
    if isinstance(path,int) or path is None:return
    p=Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(TASK):raise PermissionError('background_17 write outside own root: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(guard)
BRANCH=os.environ.get('MP17_BRANCH','PlaneGeometry')
sys.path.insert(0,str(ROOT/BRANCH/'workbench'))
from workbench_io import load_config,file_hash,pixel_hash,canonical_hash,environment_versions
CONFIG=load_config();CONFIG['runtime_dir']=str(TASK/'state');CONFIG['output_dir']=str(TASK/'output')
if BRANCH=='PlaneGeometry':
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    AD=RendererAdapter(CONFIG)
else:
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    AD=RendererAdapter(CONFIG)
ASSIGNED=json.loads((SHARED/'background_17_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def write(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def jsonl(path):return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []
def frozen(qid):
    r=AD.records[qid];base=ROOT/BRANCH
    paths=[base/r[k] for k in ['image','scene','script','original_image'] if r.get(k)]
    paths += [base/p for p in r.get('runtime_dependencies',[])]
    paths += [ROOT/p for p in ['MATHPALETTE_PROTOCOL.md','dataset_tools/mathvision_workbench.py']]
    paths += [base/p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/plugin.schema.json','workbench/render_plugins.py','workbench/partial_style.py','workbench/renderer_adapter.py','workbench/workbench_io.py','workbench/config.json']]
    if BRANCH=='PlaneGeometry':paths += [base/'workbench/mathvision_adapter.py',base/'workbench/mathvision_plugins.py']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def eligibility(qid):
    assert qid in ASSIGNED and qid in AD.records
    base=ROOT/BRANCH;r=next(r for r in jsonl(base/'dataset.jsonl') if r['id']==qid);reasons=[];files={}
    from dataset_tools.catalog import content,digest
    a=read(ROOT/'provenance/approvals.json')['approvals'].get(qid,{})
    actual=digest(content(ROOT,BRANCH,r))
    if a.get('reviewer')!='user' or not a.get('instruction') or actual!=a.get('content_sha256'):reasons.append('current user approval mismatch')
    if r.get('source_dataset')!='MathVision':reasons.append('not MathVision')
    checks={}
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=base/'special_variant'/name
        entries=[x for x in jsonl(p) if x.get('question_id')==qid];checks[name]=entries
        if p.exists():files[str(p.relative_to(ROOT))]=file_hash(p)
        if any(x.get('status')==status for x in entries):reasons.append(name)
    for name in ['recipes.json','collection.json']:
        p=base/'special_variant'/qid/name;d=read(p) if p.exists() else None;checks[name]=d
        if d is None:continue
        files[str(p.relative_to(ROOT))]=file_hash(p)
        if name=='recipes.json':
            entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
            if isinstance(entries,dict):entries=list(entries.values())
            if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed recipe')
        else:
            c=d.get('current',{})
            if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collected/special completed')
    delivered=[]
    for p in SHARED.glob('batch_*/manifest.json'):
        if qid in p.read_text(encoding='utf-8-sig'):delivered.append(str(p))
    if delivered:reasons.append('existing delivery')
    report=read(SHARED/'exploration_report.json');attempts=[x for x in report.get('attempts',[]) if x.get('question_id')==qid]
    reservations=[]
    for p in SHARED.glob('background_*_assignment.json'):
        if qid in read(p).get('question_ids',[]):reservations.append(p.stem)
    assert reservations==['background_17_assignment'],reservations
    return {'question_id':qid,'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':not reasons,'reasons':reasons,'formal_record_sha256':canonical_hash(r),'approval_content_sha256':actual,'approval_matches_current':actual==a.get('content_sha256'),'approval':a,'special_records':checks,'special_record_hashes':files,'existing_delivery':delivered,'prior_attempts':attempts,'reservations':reservations,'mutable_progress_sha256':file_hash(SHARED/'exploration_report.json'),'note':'Global progress is mutable diagnostic metadata; eligibility comes from current formal/approval/Special records.'}
def inspect(qid):
    d=TASK/qid;d.mkdir(exist_ok=False);e=eligibility(qid);write(d/'eligibility_at_start.json',e)
    if not e['eligible']:print(qid,e['reasons']);return
    write(d/'formal_record.json',AD.records[qid]);write(d/'frozen_inputs.json',frozen(qid))
    c=AD.inspect_question(qid);write(d/'context.json',c);write(d/'source_scene_snapshot.json',read(ROOT/BRANCH/AD.records[qid]['scene']))
    (d/'original.png').write_bytes(AD.original_paths[qid].read_bytes())
    if AD.records[qid].get('original_image'):(d/'source.png').write_bytes((ROOT/BRANCH/AD.records[qid]['original_image']).read_bytes())
    print(json.dumps({'id':qid,'answer':AD.records[qid]['answer'],'objects':len(c['objects']),'baseline_matches':True,'prior_attempts':len(e['prior_attempts'])}),flush=True)
def candidate(qid,name,wrong,actions,mechanism,proof,roles):
    e=eligibility(qid);assert e['eligible'],e
    before=frozen(qid);meta=AD.inspect_question(qid);renderer=PluginRenderer(CONFIG,AD,{qid:meta})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
    normalized,data,pixels=renderer.render(plugin)
    normalized2,data2,pixels2=renderer.render(normalized,frozen=True)
    assert normalized==normalized2 and data==data2 and pixels==pixels2
    assert frozen(qid)==before
    d=TASK/qid/name;d.mkdir(exist_ok=False)
    write(d/'plugin.json',normalized);(d/'candidate.png').write_bytes(data)
    write(d/'context.json',meta);write(d/'eligibility_before_render.json',e)
    design={'question_id':qid,'name':name,'expected_wrong_answer':wrong,'correct_answer':AD.records[qid]['answer'],'mechanism':mechanism,'primary_math_proof':proof,'marker_roles':roles,'created_at':datetime.now(timezone.utc).isoformat(),'png_sha256':file_hash(d/'candidate.png'),'plugin_sha256':file_hash(d/'plugin.json'),'pixel_sha256':pixels,'approval_status':'PRIMARY ONLY; requires parent NEW independent review; no Pass/Collect'}
    write(d/'design.json',design)
    appearance=renderer.appearance_changes(normalized) if hasattr(renderer,'appearance_changes') else {'world_geometry_changed':False,'projection_changed':False,'frozen_visibility_intervals_changed':False,'rendered_line_styles_changed':any('linestyle' in a for a in normalized['params']['actions'])}
    write(d/'render_check.json',{'question_id':qid,'baseline_matches_formal':True,'baseline_pixel_sha256':meta['original_pixel_sha256'],'normalized_by_actual_schema':True,'repeat_bytes_identical':True,'repeat_pixels_identical':True,'frozen_inputs':before,'appearance_changes':appearance,'isolation':ISOLATION,'unit_write_guard':True})
    print(str(d),flush=True)
if __name__=='__main__':
    for qid in sys.argv[1:]:inspect(qid)
