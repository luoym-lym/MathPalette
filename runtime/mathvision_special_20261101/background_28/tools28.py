from pathlib import Path
import os, sys, json, hashlib, types
from datetime import datetime, timezone
TASK=Path(__file__).resolve().parent
ROOT=TASK.parents[2]
SHARED=TASK.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for key,name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    p=TASK/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
def owncheck(path):
    if isinstance(path,int) or path is None:return
    p=Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(TASK):raise PermissionError('background_28 write outside own directory: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(SHARED));sys.path.insert(0,str(ROOT))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
adapter_source=SHARED/'solid_explore/bridge_adapter.py'
adapter=types.ModuleType('r28_bridge_adapter');adapter.__file__=str(TASK/'bridge_adapter.py')
exec(compile(adapter_source.read_bytes(),str(adapter_source),'exec'),adapter.__dict__)
AD=adapter.RuntimeBridgeAdapter()
file_hash=adapter.file_hash;pixel_hash=adapter.pixel_hash;canonical_hash=adapter.canonical_hash
ASSIGNED=json.loads((SHARED/'background_28_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p):return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []
def write(p,v):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def eligibility(qid):
    assert qid in ASSIGNED
    from dataset_tools.catalog import content,digest
    base=ROOT/'SolidGeometry';record=next(r for r in rows(base/'dataset.jsonl') if r['id']==qid)
    approval=read(ROOT/'provenance/approvals.json')['approvals'].get(qid,{})
    actual=digest(content(ROOT,'SolidGeometry',record));reasons=[];checks={}
    if record['source_dataset']!='MathVision':reasons.append('not MathVision')
    if approval.get('reviewer')!='user' or not approval.get('instruction') or not approval.get('approved_at_utc') or actual!=approval.get('content_sha256'):reasons.append('current original approval mismatch')
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=base/'special_variant'/name
        checks[str(p.relative_to(ROOT))]=file_hash(p) if p.exists() else None
        if any(r.get('question_id')==qid and r.get('status')==status for r in rows(p)):reasons.append(name)
    folder=base/'special_variant'/qid
    for name in ['recipes.json','collection.json']:
        p=folder/name;checks[str(p.relative_to(ROOT))]=file_hash(p) if p.exists() else None
    if (folder/'recipes.json').exists():
        d=read(folder/'recipes.json');entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed recipe')
    if (folder/'collection.json').exists():
        d=read(folder/'collection.json').get('current',{})
        if d.get('status')=='collected' or d.get('collected_at') or d.get('special_case'):reasons.append('collected or special completion')
    for p in SHARED.glob('batch_*/manifest.json'):
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered manifest '+str(p))
    assert qid not in ['Solid197','Plane295','Plane342']
    return {'question_id':qid,'checked_at':now(),'eligible':not reasons,'reasons':reasons,'approval':approval,'approval_current_content_sha256':actual,'approval_matches_current':actual==approval.get('content_sha256'),'formal_record_sha256':canonical_hash(record),'authoritative_special_files':checks,'mutable_progress_hash_is_diagnostic_only':True}

def prepare():
    if not (TASK/'isolation.json').exists():write(TASK/'isolation.json',{'created_at':now(),'guard_before_project_imports':True,'own_root':str(TASK),'runtime_isolation':ISOLATION,'adapter_source':str(adapter_source),'adapter_sha256':file_hash(adapter_source),'unchanged_adapter_source':True,'virtual_file':adapter.__file__})
    report=read(SHARED/'exploration_report.json')
    inventory=read(SHARED/'inventory.json');remaining=rows(SHARED/'remaining_questions.jsonl')
    history={};image_groups={}
    for qid in ASSIGNED:
        folder=TASK/qid;folder.mkdir(exist_ok=True)
        check=eligibility(qid)
        if not (folder/'eligibility_at_start.json').exists():write(folder/'eligibility_at_start.json',check)
        assert check['eligible'],check
        if not (folder/'formal_record.json').exists():write(folder/'formal_record.json',AD.records[qid])
        if not (folder/'source_scene_snapshot.json').exists():write(folder/'source_scene_snapshot.json',AD.scenes[qid])
        write(folder/'frozen_inputs.json',AD.frozen_inputs(qid));context=AD.inspect_question(qid);write(folder/'context.json',context)
        (folder/'original.png').write_bytes(AD.original_paths[qid].read_bytes())
        if AD.records[qid].get('original_image'):(folder/'source_original.jpg').write_bytes((ROOT/'SolidGeometry'/AD.records[qid]['original_image']).read_bytes())
        qdirs=[p for p in SHARED.rglob(qid) if p.is_dir() and not p.is_relative_to(TASK)]
        evidence=[];fulltext={}
        for qdir in qdirs:
            for p in sorted(qdir.rglob('*')):
                if not p.is_file():continue
                rel=str(p.relative_to(ROOT));h=file_hash(p);evidence.append({'path':rel,'sha256':h,'size':p.stat().st_size})
                if p.suffix.lower()=='.png':image_groups.setdefault(h,[]).append(rel)
                if p.suffix.lower() in ['.json','.txt'] and p.name!='request.json' and p.name not in ['context.json','source_scene_snapshot.json']:
                    fulltext[rel]=p.read_text(encoding='utf-8-sig')
        # All raw provider replies included verbatim; request bytes hashed rather than printed.
        history[qid]={'all_question_directories':[str(p.relative_to(ROOT)) for p in qdirs],'all_evidence_files':evidence,'full_text_records':fulltext,'progress_mentions':[a for a in report.get('attempts',[]) if a.get('question_id')==qid],'remaining_rows':[r for r in remaining if r.get('question_id',r.get('id'))==qid]}
        write(folder/'prior_history_full.json',history[qid])
        print(json.dumps({'qid':qid,'baseline_matches_formal':True,'objects':len(context['objects']),'old_dirs':[str(p.relative_to(SHARED)) for p in qdirs],'full_text_count':len(fulltext),'old_files':len(evidence)}),flush=True)
    write(TASK/'prior_history_image_groups.json',image_groups)
    write(TASK/'prior_history_read_manifest.json',{'created_at':now(),'questions':{q:{'history_path':str(TASK/q/'prior_history_full.json'),'history_sha256':file_hash(TASK/q/'prior_history_full.json')} for q in ASSIGNED},'unique_pngs':image_groups,'inventory_file_sha256':file_hash(SHARED/'inventory.json'),'progress_file_sha256':file_hash(SHARED/'exploration_report.json'),'progress_is_mutable_diagnostic_only':True})
if __name__=='__main__':prepare()
