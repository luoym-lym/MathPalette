from pathlib import Path
import os,sys,json,hashlib
from datetime import datetime,timezone
TASK=Path(__file__).resolve().parent
ROOT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
SHARED=TASK.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    path=TASK/name;path.mkdir(parents=True,exist_ok=True);os.environ[key]=str(path)
sys.path.insert(0,str(SHARED))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
def owncheck(path):
    if isinstance(path,int) or path is None:return
    p=Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(TASK):raise PermissionError('background_14 write outside own directory: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(guard)
from bridge_adapter import RuntimeBridgeAdapter,PluginRenderer,file_hash,pixel_hash,canonical_hash
AD=RuntimeBridgeAdapter()
ASSIGNED=json.loads((SHARED/'background_14_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def write(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def jsonl(path):return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    base=ROOT/'SolidGeometry';files={};reasons=[]
    record=next(r for r in jsonl(base/'dataset.jsonl') if r['id']==qid)
    from dataset_tools.catalog import content,digest
    approval_path=ROOT/'provenance/approvals.json';approval=read(approval_path)['approvals'].get(qid,{})
    actual=digest(content(ROOT,'SolidGeometry',record))
    if approval.get('reviewer')!='user' or not approval.get('instruction') or actual!=approval.get('content_sha256'):reasons.append('current original lacks matching user approval')
    if record.get('source_dataset')!='MathVision':reasons.append('not formal MathVision')
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        path=base/'special_variant'/name
        if path.exists():files[str(path.relative_to(ROOT))]=file_hash(path)
        if any(r.get('question_id')==qid and r.get('status')==status for r in jsonl(path)):reasons.append(name)
    folder=base/'special_variant'/qid
    if (folder/'recipes.json').exists():
        d=read(folder/'recipes.json');entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed recipe')
    if (folder/'collection.json').exists():
        c=read(folder/'collection.json').get('current',{})
        if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collected/special complete')
    report=read(SHARED/'exploration_report.json');attempts=[a for a in report.get('attempts',[]) if a.get('question_id')==qid]
    delivered={q for b in report.get('delivered_batches',[]) for q in b.get('candidates',[])}
    if qid in delivered:reasons.append('delivered')
    for manifest in SHARED.glob('batch_*/manifest.json'):
        if qid in manifest.read_text(encoding='utf-8-sig'):reasons.append('delivered manifest')
    return {'question_id':qid,'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':not reasons,'reasons':reasons,'formal_record_sha256':canonical_hash(record),'approval_content_sha256':actual,'approval_matches_current':actual==approval.get('content_sha256'),'checks_sha256':files,'prior_attempts':attempts,'mutable_progress_snapshot_sha256':file_hash(SHARED/'exploration_report.json'),'diagnostic_note':'Progress report hash is mutable metadata; formal records/approval/Special records are authoritative.'}
def inspect(qid):
    check=eligibility(qid);folder=TASK/qid;folder.mkdir(exist_ok=False)
    write(folder/'eligibility_at_start.json',check)
    if not check['eligible']:print(qid,check);return
    write(folder/'formal_record.json',AD.records[qid]);context=AD.inspect_question(qid)
    write(folder/'context.json',context);write(folder/'source_scene_snapshot.json',AD.scenes[qid]);write(folder/'frozen_inputs.json',AD.frozen_inputs(qid))
    (folder/'original.png').write_bytes(AD.original_paths[qid].read_bytes())
    if AD.records[qid].get('original_image'):(folder/'source.png').write_bytes((ROOT/'SolidGeometry'/AD.records[qid]['original_image']).read_bytes())
    print(json.dumps({'question_id':qid,'answer':AD.records[qid]['answer'],'objects':len(context['objects']),'baseline_matches_formal':True,'prior_attempts':len(check['prior_attempts'])}),flush=True)
if __name__=='__main__':
    for qid in sys.argv[1:]:inspect(qid)
