from pathlib import Path
import os,sys,json,hashlib
from datetime import datetime,timezone
TASK=Path(__file__).resolve().parent
ROOT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k,v in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=TASK/v;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
def own(path):
    if isinstance(path,int) or path is None:return
    p=Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(TASK):raise PermissionError('background_13 write outside own directory blocked: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):own(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):own(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):own(args[0]);own(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
from bridge_adapter import RuntimeBridgeAdapter,PluginRenderer,file_hash,pixel_hash,canonical_hash
AD=RuntimeBridgeAdapter()
ASSIGNED=json.loads((TASK.parent/'background_13_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def write(path,value):
    path=Path(path);own(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(path):
    return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    base=ROOT/'SolidGeometry';reasons=[];files={}
    record=next(r for r in rows(base/'dataset.jsonl') if r['id']==qid)
    from dataset_tools.catalog import content,digest
    ap=ROOT/'provenance/approvals.json';a=json.loads(ap.read_text(encoding='utf-8-sig'))['approvals'].get(qid,{})
    current=digest(content(ROOT,'SolidGeometry',record))
    if a.get('reviewer')!='user' or not a.get('instruction') or current!=a.get('content_sha256'):reasons.append('no matching current user original approval')
    if record.get('source_dataset')!='MathVision':reasons.append('not formal MathVision')
    for p in [ap,base/'dataset.jsonl',base/'special_variant/accepted_index.jsonl',base/'special_variant/collected_index.jsonl']:
        if p.exists():files[str(p.relative_to(ROOT))]=file_hash(p)
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        if any(r.get('question_id')==qid for r in rows(base/'special_variant'/name)):reasons.append(name)
    folder=base/'special_variant'/qid
    for name in ['recipes.json','collection.json']:
        p=folder/name
        if p.exists():
            files[str(p.relative_to(ROOT))]=file_hash(p)
            d=json.loads(p.read_text(encoding='utf-8-sig'))
            if name=='collection.json' and d.get('current'):reasons.append('collection/special completion record')
            if name=='recipes.json':
                es=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
                if isinstance(es,dict):es=list(es.values())
                if any(e.get('status')=='passed' or e.get('reviewed_at') for e in es if isinstance(e,dict)):reasons.append('passed recipe')
    for p in TASK.parent.glob('batch_*/manifest.json'):
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered manifest '+str(p.relative_to(ROOT)))
    rem=TASK.parent/'remaining_questions.jsonl';row=next((r for r in rows(rem) if r['question_id']==qid),None)
    report=TASK.parent/'exploration_report.json';rep=json.loads(report.read_text(encoding='utf-8-sig'))
    historical_attempts=[r for r in rep.get('attempts',[]) if r['question_id']==qid]
    return {'question_id':qid,'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':not reasons,'reasons':reasons,'formal_record_sha256':canonical_hash(record),'approval_content_sha256':current,'approval_matches_current':current==a.get('content_sha256'),'authority_files':files,'remaining_status':row.get('status') if row else None,'historical_attempts':historical_attempts,'diagnostic_hashes':{str(rem.relative_to(ROOT)):file_hash(rem),str(report.relative_to(ROOT)):file_hash(report)},'diagnostic_note':'Mutable historical progress is diagnostic only; current formal, user approval, and Special records establish eligibility.'}
def inspect(qid):
    check=eligibility(qid);folder=TASK/qid;folder.mkdir(exist_ok=False)
    write(folder/'eligibility_at_start.json',check)
    if not check['eligible']:return
    write(folder/'formal_record.json',AD.records[qid]);c=AD.inspect_question(qid)
    write(folder/'context.json',c);write(folder/'source_scene_snapshot.json',AD.scenes[qid]);write(folder/'frozen_inputs.json',AD.frozen_inputs(qid))
    (folder/'original.png').write_bytes(AD.original_paths[qid].read_bytes())
    print(json.dumps({'question_id':qid,'question':AD.records[qid]['question'],'answer':AD.records[qid]['answer'],'objects':len(c['objects']),'snaps':len(c['snap_points']),'baseline_matches_formal':True},ensure_ascii=False),flush=True)
if __name__=='__main__':
    for qid in sys.argv[1:]:inspect(qid)
