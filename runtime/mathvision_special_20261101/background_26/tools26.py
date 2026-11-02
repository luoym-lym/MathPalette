import os, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=HERE.parent
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for var,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[var]=str(p)
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
def owncheck(path):
    if isinstance(path,int) or path is None:return
    if not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):raise PermissionError('background_26 write outside own root: '+str(path))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):owncheck(args[0]);owncheck(args[1])
sys.addaudithook(guard)
import json,hashlib,copy,importlib.util
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools.catalog import content,digest
ASSIGNMENT=json.loads((BASE/'background_26_assignment.json').read_text(encoding='utf-8-sig'))
ASSIGNED=ASSIGNMENT['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def write(path,value):
    path=Path(path);owncheck(path);path.parent.mkdir(parents=True,exist_ok=True)
    def conv(x):
        if hasattr(x,'tolist'):return x.tolist()
        if isinstance(x,Path):return str(x)
        raise TypeError(type(x).__name__)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False,default=conv);f.write('\n')
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def rows(path):return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    br=ROOT/'PlaneGeometry';reasons=[];rec=next((r for r in rows(br/'dataset.jsonl') if r['id']==qid),None)
    paths=[br/'dataset.jsonl',ROOT/'provenance/approvals.json',ROOT/'provenance/source_notes.json']
    ap=read(ROOT/'provenance/approvals.json')['approvals'].get(qid,{})
    if not rec or rec.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    current=digest(content(ROOT,'PlaneGeometry',rec)) if rec else None
    if ap.get('reviewer')!='user' or not ap.get('instruction') or not ap.get('approved_at_utc') or ap.get('content_sha256')!=current:reasons.append('approval_not_current')
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=br/'special_variant'/name;paths.append(p)
        if any(x.get('question_id')==qid and x.get('status')==status for x in rows(p)):reasons.append(name)
    p=br/'special_variant'/qid/'recipes.json';paths.append(p)
    if p.exists():
        d=read(p);entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(x.get('status')=='passed' or x.get('reviewed_at') for x in entries if isinstance(x,dict)):reasons.append('passed_recipe')
    p=br/'special_variant'/qid/'collection.json';paths.append(p)
    if p.exists():
        c=read(p).get('current',{})
        if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collection_or_special_completion')
    for p in BASE.glob('batch_*/manifest.json'):
        paths.append(p)
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered:'+p.parent.name)
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'formal_record':rec,'original_approval':ap,'current_original_content_sha256':current,'approval_fingerprint_matches':current==ap.get('content_sha256'),'authoritative_state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},'diagnostic_runtime_metadata_hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in [BASE/'remaining_questions.jsonl',BASE/'exploration_report.json']}}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output');return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];br=ROOT/'PlaneGeometry'
    paths=[br/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]+list(ad.input_files.values())
    paths += [ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'AGENTS.md',br/'REDRAW_PROTOCOL.md',br/'dataset_generator/protocol.json',br/'workbench/plugin.schema.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all():
    cfg,ad=adapter()
    for qid in ASSIGNED:
        folder=HERE/qid;ck=eligibility(qid)
        if not (folder/'eligibility_start.json').exists():write(folder/'eligibility_start.json',ck)
        if not ck['eligible']:continue
        before=inputs(ad,qid);meta=ad.inspect_question(qid)
        paths={t['id']:t['partial_paths'] for t in meta['canvas']['targets']}
        if (folder/'context.json').exists():assert read(folder/'context.json')==meta
        else:write(folder/'context.json',meta)
        write(folder/'paths_frozen.json',paths);write(folder/'formal_record.json',ad.records[qid]);write(folder/'input_fingerprints.json',before)
        (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes());assert before==inputs(ad,qid)
        print(json.dumps({'qid':qid,'baseline_match':True,'objects':len(meta['objects'])}),flush=True)
def history_inventory():
    found={q:[] for q in ASSIGNED}
    for p in BASE.rglob('design.json'):
        if p.is_relative_to(HERE):continue
        try:d=read(p)
        except (ValueError,OSError):continue
        q=d.get('question_id')
        if q in found:found[q].append(str(p.relative_to(ROOT)))
    write(HERE/'history_inventory.json',found);print(json.dumps(found,ensure_ascii=False,indent=2))
if __name__=='__main__':
    if 'history' in sys.argv:history_inventory()
    else:inspect_all()
