import os,sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for var,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[var]=str(p)
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
ASSIGNED=['Plane197','Plane258','Plane225','Plane238','Plane240','Plane314','Plane332','Plane322']
def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8') as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write('\n')
def rows(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    base=ROOT/'PlaneGeometry';reasons=[];hashes={}
    dataset=base/'dataset.jsonl';record=next((r for r in rows(dataset) if r['id']==qid),None)
    if not record or record.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    remain=ROOT/'runtime/mathvision_special_20261101/remaining_questions.jsonl';entry=next((r for r in rows(remain) if r['question_id']==qid),None)
    if not entry or entry['status']!='not_yet_explored':reasons.append('already_explored_or_absent')
    report=ROOT/'runtime/mathvision_special_20261101/exploration_report.json'
    if qid in {r['question_id'] for r in json.loads(report.read_text(encoding='utf-8-sig'))['attempts']}:reasons.append('in_previous_attempts')
    paths=[dataset,remain,report]
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        path=base/'special_variant'/name;paths.append(path)
        if any(r.get('question_id')==qid and r.get('status')==status for r in rows(path)):reasons.append(name)
    recipe=base/'special_variant'/qid/'recipes.json';paths.append(recipe)
    if recipe.exists():
        d=json.loads(recipe.read_text(encoding='utf-8-sig'));entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('recipes')
    collection=base/'special_variant'/qid/'collection.json';paths.append(collection)
    if collection.exists():
        current=json.loads(collection.read_text(encoding='utf-8-sig')).get('current',{})
        if current.get('status')=='collected' or current.get('collected_at') or current.get('special_case'):reasons.append('collection')
    hashes={str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths}
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':datetime.now(timezone.utc).isoformat(),'state_hashes':hashes,'formal_record':record,'remaining_entry':entry}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];base=ROOT/'PlaneGeometry'
    paths=[base/p for p in [r['image'],r['scene'],r['script'],r['original_image'],*r.get('runtime_dependencies',[])] if p]
    paths+=list(ad.input_files.values())
    return {str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))}
def inspect(qid):
    cfg,ad=adapter();check=eligibility(qid);assert check['eligible'],check
    m=ad.inspect_question(qid);folder=HERE/qid
    write(folder/'eligibility_start.json',check);write(folder/'context.json',m);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',inputs(ad,qid))
    (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
    print(json.dumps({'qid':qid,'question':ad.records[qid]['question'],'answer':ad.records[qid]['answer'],'object_count':len(m['objects']),'snap_point_count':len(m['snap_points'])},ensure_ascii=False),flush=True)
if __name__=='__main__':
    for q in sys.argv[1:]:inspect(q)
