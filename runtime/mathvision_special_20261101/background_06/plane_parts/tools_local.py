import os,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=ROOT/'runtime/mathvision_special_20261101'
for var,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[var]=str(p)
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
import json,hashlib,copy
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
ASSIGNED=['Plane209','Plane218','Plane220','Plane227','Plane231','Plane233']
def now():return datetime.now(timezone.utc).isoformat()
def write(path,value):
    path=Path(path);assert path.resolve().is_relative_to(HERE)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(path):return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    base=ROOT/'PlaneGeometry';reasons=[];dataset=base/'dataset.jsonl';record=next((r for r in rows(dataset) if r['id']==qid),None)
    if not record or record.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    remain=BASE/'remaining_questions.jsonl';entry=next((r for r in rows(remain) if r['question_id']==qid),None)
    if not entry or entry['status']!='not_yet_explored':reasons.append('already_explored_or_absent')
    report=BASE/'exploration_report.json';data=json.loads(report.read_text(encoding='utf-8-sig'))
    if qid in {r['question_id'] for r in data['attempts']}:reasons.append('previous_attempt')
    paths=[dataset,ROOT/'provenance/approvals.json'];diagnostic=[remain,report]
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=base/'special_variant'/name;paths.append(p)
        if any(r.get('question_id')==qid and r.get('status')==status for r in rows(p)):reasons.append(name)
    recipe=base/'special_variant'/qid/'recipes.json';paths.append(recipe)
    if recipe.exists():
        d=json.loads(recipe.read_text(encoding='utf-8-sig'));entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed_recipe')
    collection=base/'special_variant'/qid/'collection.json';paths.append(collection)
    if collection.exists():
        cur=json.loads(collection.read_text(encoding='utf-8-sig')).get('current',{})
        if cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'):reasons.append('collection')
    for manifest in BASE.glob('batch_*/manifest.json'):
        paths.append(manifest)
        if qid in manifest.read_text(encoding='utf-8-sig'):reasons.append('delivery:'+manifest.parent.name)
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'authoritative_state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},'diagnostic_runtime_metadata_hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in diagnostic},'formal_record':record,'remaining_entry':entry}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];base=ROOT/'PlaneGeometry'
    paths=[base/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths+=list(ad.input_files.values())+[ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'provenance/approvals.json',base/'dataset.jsonl',base/'REDRAW_PROTOCOL.md',base/'dataset_generator/protocol.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect(qid):
    check=eligibility(qid);folder=HERE/qid;write(folder/'eligibility_start.json',check)
    if not check['eligible']:print(json.dumps({'qid':qid,'skipped':check['reasons']}),flush=True);return
    cfg,ad=adapter();before=inputs(ad,qid);m=ad.inspect_question(qid)
    write(folder/'context.json',m);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',before)
    (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
    assert before==inputs(ad,qid)
    print(json.dumps({'qid':qid,'question':ad.records[qid]['question'],'answer':ad.records[qid]['answer'],'object_count':len(m['objects']),'snap_point_count':len(m['snap_points']),'baseline_pixel_match':True},ensure_ascii=False),flush=True)
if __name__=='__main__':
    for q in sys.argv[1:]:inspect(q)
