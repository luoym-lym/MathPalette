import os,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=ROOT/'runtime/mathvision_special_20261101'
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for var,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[var]=str(p)
def own_write_guard(event,args):
    def check(p):
        if p is None or isinstance(p,int):return
        path=Path(os.fsdecode(p)).resolve()
        if not path.is_relative_to(HERE):raise PermissionError('background_27 write outside own directory: '+str(path))
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(own_write_guard)
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
from dataset_tools import catalog
ASSIGNED=json.loads((BASE/'background_27_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
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
    approvals=ROOT/'provenance/approvals.json';approval=json.loads(approvals.read_text(encoding='utf-8-sig'))['approvals'].get(qid,{})
    digest=catalog.digest(catalog.content(ROOT,'PlaneGeometry',record)) if record else None
    if approval.get('reviewer')!='user' or not approval.get('instruction') or approval.get('content_sha256')!=digest:reasons.append('original_approval_invalid')
    paths=[dataset,approvals]
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        p=base/'special_variant'/name;paths.append(p)
        if any(r.get('question_id',r.get('id'))==qid and r.get('status') not in ('deleted','rejected') for r in rows(p)):reasons.append(name)
    for name in ['recipes.json','collection.json']:
        p=base/'special_variant'/qid/name;paths.append(p)
        if p.exists():
            data=json.loads(p.read_text(encoding='utf-8-sig'))
            if name=='recipes.json':
                entries=data if isinstance(data,list) else data.get('recipes',data.get('variants',[]))
                if isinstance(entries,dict):entries=list(entries.values())
                if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed_recipe')
            else:
                cur=data.get('current',{})
                if cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'):reasons.append('collection')
    for p in BASE.glob('batch_*/manifest.json'):
        paths.append(p)
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('existing_delivery')
    diagnostic=[BASE/'remaining_questions.jsonl',BASE/'exploration_report.json']
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'approval':approval,'current_content_sha256':digest,'authoritative_state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},'diagnostic_runtime_metadata_hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in diagnostic},'formal_record':record}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];base=ROOT/'PlaneGeometry'
    paths=[base/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths+=list(ad.input_files.values())+[ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'provenance/approvals.json',base/'dataset.jsonl',base/'REDRAW_PROTOCOL.md',base/'dataset_generator/protocol.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all(qids):
    cfg,ad=adapter()
    for qid in qids:
        folder=HERE/qid;check=eligibility(qid);write(folder/'eligibility_start.json',check)
        if not check['eligible']:print(json.dumps({'qid':qid,'skipped':check['reasons']}),flush=True);continue
        before=inputs(ad,qid);m=ad.inspect_question(qid)
        write(folder/'context.json',m);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',before)
        write(folder/'source_scene_snapshot.json',json.loads((ROOT/'PlaneGeometry'/ad.records[qid]['scene']).read_text(encoding='utf-8-sig')))
        (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes());assert before==inputs(ad,qid)
        print(json.dumps({'qid':qid,'answer':ad.records[qid]['answer'],'objects':len(m['objects']),'baseline_pixel_match':True},ensure_ascii=False),flush=True)
def render(qid,vid,actions,preset,mechanism,proof,roles):
    folder=HERE/qid/vid;check=eligibility(qid);write(folder/'eligibility_before_design.json',check);assert check['eligible']
    cfg,ad=adapter();before=inputs(ad,qid);m=ad.inspect_question(qid);write(folder/'context.json',m)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
    renderer=PluginRenderer(cfg,ad,{qid:m});normalized=renderer.normalize(plugin)
    write(folder/'plugin.json',normalized)
    write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':preset,'created_at':now(),'mechanism':mechanism,'primary_mathematical_proof':proof,'marker_roles':roles,'approval_status':'UNREVIEWED; requires NEW independent parent review'})
    a,data,px=renderer.render(normalized,frozen=True);b,data2,px2=renderer.render(normalized,frozen=True)
    assert data==data2 and px==px2 and before==inputs(ad,qid)
    (folder/'candidate.png').write_bytes(data);(folder/'repeat.png').write_bytes(data2)
    write(folder/'render_check.json',{'no_op_formal_pixel_match':True,'normalized_schema_validated':True,'repeat_byte_identical':True,'image_sha256':hashlib.sha256(data).hexdigest(),'pixel_sha256':px,'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'frozen_inputs':before,'isolation':ISOLATION})
    print(json.dumps({'qid':qid,'variant':vid,'actions':len(actions),'image':str(folder/'candidate.png')},ensure_ascii=False),flush=True)
if __name__=='__main__':inspect_all(sys.argv[1:] or ASSIGNED)

