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
def _owncheck(path):
    if isinstance(path,int) or path is None:return
    if not Path(os.fsdecode(path)).resolve().is_relative_to(HERE):
        raise PermissionError('background_09 write outside own root: '+str(path))
def _guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):_owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):_owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):_owncheck(args[0]);_owncheck(args[1])
sys.addaudithook(_guard)
import json, hashlib, copy, importlib.util
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
from dataset_tools.catalog import content,digest
ASSIGNMENT=json.loads((BASE/'background_09_assignment.json').read_text(encoding='utf-8-sig'))
ASSIGNED=ASSIGNMENT['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def write(path,value):
    path=Path(path);_owncheck(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def rows(path):return [json.loads(s) for s in Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(path).exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    b=ROOT/'PlaneGeometry';reasons=[];r=next((r for r in rows(b/'dataset.jsonl') if r['id']==qid),None)
    paths=[b/'dataset.jsonl',ROOT/'provenance/approvals.json',ROOT/'provenance/source_notes.json']
    ap=read(ROOT/'provenance/approvals.json')['approvals'].get(qid,{})
    if not r or r.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    current=digest(content(ROOT,'PlaneGeometry',r)) if r else None
    if ap.get('reviewer')!='user' or not ap.get('instruction') or ap.get('content_sha256')!=current:reasons.append('approval_not_current')
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=b/'special_variant'/name;paths.append(p)
        if any(x.get('question_id')==qid and x.get('status')==status for x in rows(p)):reasons.append(name)
    p=b/'special_variant'/qid/'recipes.json';paths.append(p)
    if p.exists():
        d=read(p);entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(x.get('status')=='passed' or x.get('reviewed_at') for x in entries if isinstance(x,dict)):reasons.append('passed_recipe')
    p=b/'special_variant'/qid/'collection.json';paths.append(p)
    if p.exists():
        c=read(p).get('current',{})
        if c.get('status')=='collected' or c.get('collected_at') or c.get('special_case'):reasons.append('collection')
    for p in BASE.glob('batch_*/manifest.json'):
        paths.append(p)
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered:'+p.parent.name)
    remain=BASE/'remaining_questions.jsonl';report=BASE/'exploration_report.json'
    entry=next((x for x in rows(remain) if x['question_id']==qid),None)
    attempts=read(report).get('attempts',[])
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'formal_record':r,'approval_current_fingerprint':current,'approved_at':ap.get('approved_at_utc'),'authoritative_state_hashes':{str(p.relative_to(ROOT)):file_hash(p) if p.exists() else None for p in paths},'diagnostic_runtime_metadata':{'remaining_entry':entry,'previous_attempts':[x for x in attempts if x['question_id']==qid],'hashes':{str(p.relative_to(ROOT)):file_hash(p) for p in [remain,report]}}}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    r=ad.records[qid];b=ROOT/'PlaneGeometry'
    paths=[b/p for p in [r['image'],r['scene'],r['script'],r.get('original_image'),*r.get('runtime_dependencies',[])] if p]
    paths+=list(ad.input_files.values())+[ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'provenance/approvals.json',ROOT/'provenance/source_notes.json',b/'dataset.jsonl',b/'REDRAW_PROTOCOL.md',b/'dataset_generator/protocol.json']
    return {'question_record_sha256':canonical_hash(r),'files':{str(p.relative_to(ROOT)):file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect(qid):
    check=eligibility(qid);out=HERE/qid;write(out/'eligibility_start.json',check)
    if not check['eligible']:print(json.dumps({'qid':qid,'skipped':check['reasons']}),flush=True);return
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid)
    write(out/'context.json',meta);write(out/'formal_record.json',ad.records[qid]);write(out/'input_fingerprints.json',before)
    (out/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
    assert before==inputs(ad,qid)
    print(json.dumps({'qid':qid,'baseline_match':True,'objects':len(meta['objects']),'question':ad.records[qid]['question'],'answer':ad.records[qid]['answer']},ensure_ascii=False),flush=True)
def harness():
    p=HERE/'harness/quicktest3_isolated.py';p.parent.mkdir(parents=True,exist_ok=True)
    source=BASE/'harness/quicktest3_isolated.py'
    if not p.exists():p.write_bytes(source.read_bytes())
    assert p.read_bytes()==source.read_bytes()
    spec=importlib.util.spec_from_file_location('background09_unchanged_harness',p);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    h.PROJECT=ROOT;h.RUNTIME=ROOT/'runtime'
    return h
if __name__=='__main__':
    for q in sys.argv[1:]:inspect(q)
