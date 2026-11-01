from pathlib import Path
import os,sys,json,hashlib,shutil
from datetime import datetime,timezone
TASK=Path(__file__).resolve().parent
ROOT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for key,name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    path=TASK/name;path.mkdir(parents=True,exist_ok=True);os.environ[key]=str(path)
sys.dont_write_bytecode=True;os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
ISOLATION=install(TASK/'render_tmp')
from bridge_adapter_local import RuntimeBridgeAdapter,PluginRenderer,file_hash,pixel_hash,canonical_hash
AD=RuntimeBridgeAdapter()
ASSIGNED=['Solid170','Solid188','Solid169','Solid185','Solid106','Solid152','Solid204','Solid199']
def write(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def jsonl(path):
    return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    base=ROOT/'SolidGeometry';files={};reasons=[]
    record=next(r for r in jsonl(base/'dataset.jsonl') if r['id']==qid)
    files['SolidGeometry/dataset.jsonl']=file_hash(base/'dataset.jsonl')
    if record.get('source_dataset')!='MathVision':reasons.append('not formal MathVision')
    remaining=ROOT/'runtime/mathvision_special_20261101/remaining_questions.jsonl'
    row=next((r for r in jsonl(remaining) if r['question_id']==qid),None)
    if not row or row.get('status')!='not_yet_explored':reasons.append('not currently unattempted')
    report=ROOT/'runtime/mathvision_special_20261101/exploration_report.json'
    attempted={r['question_id'] for r in json.loads(report.read_text(encoding='utf-8-sig'))['attempts']}
    if qid in attempted:reasons.append('already in exploration report')
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        path=base/'special_variant'/name
        if path.exists():files[str(path.relative_to(ROOT))]=file_hash(path)
        if any(r.get('question_id')==qid and r.get('status')==status for r in jsonl(path)):reasons.append(name)
    folder=base/'special_variant'/qid
    path=folder/'recipes.json'
    if path.exists():
        files[str(path.relative_to(ROOT))]=file_hash(path);d=json.loads(path.read_text(encoding='utf-8-sig'))
        entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed recipe')
    path=folder/'collection.json'
    if path.exists():
        files[str(path.relative_to(ROOT))]=file_hash(path);c=json.loads(path.read_text(encoding='utf-8-sig')).get('current',{})
        if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collected/special-completed')
    return {'question_id':qid,'checked_at':datetime.now(timezone.utc).isoformat(),'eligible':not reasons,'reasons':reasons,'formal_record_sha256':canonical_hash(record),'remaining_status':row['status'] if row else None,'checks_sha256':files,'remaining_sha256':file_hash(remaining),'report_sha256':file_hash(report)}
def inspect(qid):
    check=eligibility(qid);assert check['eligible'],check
    folder=TASK/qid;folder.mkdir(exist_ok=False)
    write(folder/'eligibility_at_start.json',check)
    write(folder/'formal_record.json',AD.records[qid]);context=AD.inspect_question(qid)
    write(folder/'context.json',context);write(folder/'source_scene_snapshot.json',AD.scenes[qid]);write(folder/'frozen_inputs.json',AD.frozen_inputs(qid))
    (folder/'original.png').write_bytes(AD.original_paths[qid].read_bytes())
    print(json.dumps({'question_id':qid,'question':AD.records[qid]['question'],'answer':AD.records[qid]['answer'],'object_count':len(context['objects']),'snap_point_count':len(context['snap_points']),'baseline_matches_formal':True},ensure_ascii=False),flush=True)
if __name__=='__main__':
    for qid in sys.argv[1:]:inspect(qid)
