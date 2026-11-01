import os, sys
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
import json, hashlib
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools import catalog
ASSIGNED=['Plane165','Plane194','Plane195','Plane202','Plane203','Plane204']
def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write('\n')
def rows(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    base=ROOT/'PlaneGeometry';reasons=[]
    dataset=base/'dataset.jsonl';record=next((r for r in rows(dataset) if r['id']==qid),None)
    if not record or record.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    approvals=ROOT/'provenance/approvals.json';approval=json.loads(approvals.read_text(encoding='utf-8-sig'))['approvals'].get(qid,{})
    content_hash=catalog.digest(catalog.content(ROOT,'PlaneGeometry',record))
    if approval.get('reviewer')!='user' or not approval.get('instruction') or approval.get('content_sha256')!=content_hash:reasons.append('current_original_approval_invalid')
    remain=BASE/'remaining_questions.jsonl';entry=next((r for r in rows(remain) if r['question_id']==qid),None)
    if not entry or entry['status']!='not_yet_explored':reasons.append('already_explored_or_absent')
    report=BASE/'exploration_report.json';rd=json.loads(report.read_text(encoding='utf-8-sig'))
    if qid in {r['question_id'] for r in rd['attempts']}:reasons.append('in_previous_attempts')
    paths=[dataset,approvals,remain,report]
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        path=base/'special_variant'/name;paths.append(path)
        if any(r.get('question_id',r.get('id'))==qid and r.get('status') not in ('deleted','rejected') for r in rows(path)):reasons.append(name)
    recipe=base/'special_variant'/qid/'recipes.json';paths.append(recipe)
    if recipe.exists():reasons.append('existing_recipe_requires_skip')
    collection=base/'special_variant'/qid/'collection.json';paths.append(collection)
    if collection.exists():
        current=json.loads(collection.read_text(encoding='utf-8-sig')).get('current',{})
        if current.get('status')=='collected' or current.get('collected_at') or current.get('special_case'):reasons.append('collection')
    delivered=[]
    for manifest in BASE.glob('batch_*/manifest.json'):
        paths.append(manifest)
        if qid in manifest.read_text(encoding='utf-8-sig'):delivered.append(str(manifest.relative_to(ROOT)))
    if delivered:reasons.append('existing_delivery')
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':datetime.now(timezone.utc).isoformat(),'approval':approval,'current_content_sha256':content_hash,'state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},'formal_record':record,'remaining_entry':entry,'existing_delivery_manifests':delivered,'diagnostic_mutable_progress_paths':[str(remain.relative_to(ROOT)),str(report.relative_to(ROOT))]}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    base=ROOT/'PlaneGeometry';r=ad.records[qid]
    paths=[base/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths += [ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'PlaneGeometry/REDRAW_PROTOCOL.md',ROOT/'provenance/approvals.json',base/'dataset.jsonl']
    paths += [base/'workbench'/name for name in ['config.json','plugin.schema.json','mathvision_adapter.py','mathvision_plugins.py','render_plugins.py','partial_style.py','renderer_adapter.py','workbench_io.py','drawing_board.py']]
    paths += [ROOT/'dataset_tools/mathvision_workbench.py',ROOT/'dataset_tools/geometry_dataset.py',base/'dataset_generator/protocol.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all(qids):
    cfg,ad=adapter()
    for qid in qids:
        check=eligibility(qid);folder=HERE/qid;write(folder/'eligibility_start.json',check)
        if not check['eligible']:continue
        before=inputs(ad,qid);m=ad.inspect_question(qid)
        write(folder/'context.json',m);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',before)
        write(folder/'source_scene_snapshot.json',json.loads((ROOT/'PlaneGeometry'/ad.records[qid]['scene']).read_text(encoding='utf-8-sig')))
        (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes());assert before==inputs(ad,qid)
        print(json.dumps({'qid':qid,'question':ad.records[qid]['question'],'answer':ad.records[qid]['answer'],'object_count':len(m['objects']),'snap_point_count':len(m['snap_points']),'baseline_pixel_match':True},ensure_ascii=False),flush=True)
if __name__=='__main__':inspect_all(sys.argv[1:] or ASSIGNED)
