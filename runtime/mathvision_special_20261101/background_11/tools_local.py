import os, sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=HERE.parent
for key,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=HERE/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
def own_guard(event,args):
    def check(p):
        if p is not None and not isinstance(p,int):
            resolved=Path(os.fsdecode(p)).resolve()
            if not resolved.is_relative_to(HERE):raise PermissionError('background_11 write outside own directory: '+str(resolved))
    if event=='open' and args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(own_guard)
import json,hashlib,copy,importlib.util
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,canonical_hash,pixel_hash,file_hash,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths
ASSIGNED=json.loads((BASE/'background_11_assignment.json').read_text(encoding='utf-8-sig'))['question_ids']
def now():return datetime.now(timezone.utc).isoformat()
def write(path,value):
    path=Path(path);assert path.resolve().is_relative_to(HERE)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(path):return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()] if path.exists() else []
def eligibility(qid):
    assert qid in ASSIGNED
    branch=ROOT/'PlaneGeometry';special=branch/'special_variant';reasons=[];dataset=branch/'dataset.jsonl'
    rec=next((r for r in rows(dataset) if r['id']==qid),None)
    if not rec or rec.get('source_dataset')!='MathVision':reasons.append('not_formal_MathVision')
    ap=ROOT/'provenance/approvals.json';approval=json.loads(ap.read_text(encoding='utf-8-sig'))['approvals'].get(qid)
    if not approval or approval.get('reviewer')!='user':reasons.append('missing_original_approval')
    paths=[dataset,ap]
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=special/name;paths.append(p)
        if any(r.get('question_id')==qid and r.get('status')==status for r in rows(p)):reasons.append(name)
    p=special/qid/'recipes.json';paths.append(p)
    if p.exists():
        d=json.loads(p.read_text(encoding='utf-8-sig'));entries=d if isinstance(d,list) else d.get('recipes',d.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(e.get('status')=='passed' or e.get('reviewed_at') for e in entries if isinstance(e,dict)):reasons.append('passed_recipe')
    p=special/qid/'collection.json';paths.append(p)
    if p.exists():
        cur=json.loads(p.read_text(encoding='utf-8-sig')).get('current',{})
        if cur.get('status')=='collected' or cur.get('collected_at') or cur.get('special_case'):reasons.append('collected_or_special_completed')
    for p in BASE.glob('batch_*/manifest.json'):
        paths.append(p)
        if qid in p.read_text(encoding='utf-8-sig'):reasons.append('delivered:'+p.parent.name)
    report=json.loads((BASE/'exploration_report.json').read_text(encoding='utf-8-sig'))
    attempts=[r for r in report['attempts'] if r['question_id']==qid]
    foreign=[r for r in attempts if not str(r.get('candidate','')).replace('\\','/').startswith('background_11/')]
    if foreign:reasons.append('foreign_prior_assessment')
    return {'question_id':qid,'eligible':not reasons,'reasons':reasons,'checked_at':now(),'approval':approval,'own_prior_designs_aggregated_by_parent':[r.get('candidate') for r in attempts if r not in foreign],'authoritative_state_hashes':{p.relative_to(ROOT).as_posix():file_hash(p) if p.exists() else None for p in paths},'diagnostic_runtime_metadata_hashes':{n:file_hash(BASE/n) for n in ['inventory.json','remaining_questions.jsonl','exploration_report.json']}}
def adapter():
    cfg=load_config();cfg['runtime_dir']=str(HERE/'render_state');cfg['output_dir']=str(HERE/'render_output')
    return cfg,RendererAdapter(cfg)
def inputs(ad,qid):
    rec=ad.records[qid];branch=ROOT/'PlaneGeometry'
    paths=list(ad.input_files.values())+[branch/p for p in [rec.get('original_image'),*rec.get('runtime_dependencies',[])] if p]
    paths+=[ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'AGENTS.md',ROOT/'provenance/approvals.json',branch/'workbench/plugin.schema.json',branch/'workbench/config.json',branch/'workbench/render_plugins.py',branch/'workbench/partial_style.py']
    return {'question_record_sha256':canonical_hash(rec),'files':{p.relative_to(ROOT).as_posix():file_hash(p) for p in sorted(set(paths))},'environment':environment_versions()}
def inspect_all():
    cfg,ad=adapter()
    for qid in ASSIGNED:
        out=HERE/qid;check=eligibility(qid);write(out/'eligibility_start.json',check)
        if not check['eligible']:print(qid,check['reasons'],flush=True);continue
        before=inputs(ad,qid);meta=ad.inspect_question(qid)
        write(out/'context.json',meta);write(out/'formal_record.json',ad.records[qid]);write(out/'input_fingerprints.json',before)
        (out/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
        assert before==inputs(ad,qid)
        print(json.dumps({'qid':qid,'baseline_match':True,'objects':len(meta['objects'])}),flush=True)
def snapshot():
    spec=importlib.util.spec_from_file_location('_readonly_inventory11',BASE/'inventory.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    write(HERE/'formal_files_before.json',m.scan())
    old={}
    for pattern in ['batch_*','independent_review','background_03','background_04','background_05','background_06']:
        for d in BASE.glob(pattern):
            if d.is_dir():
                for p in d.rglob('*'):
                    if p.is_file():old[p.relative_to(ROOT).as_posix()]=file_hash(p)
    write(HERE/'prior_evidence_before.json',old)
    (HERE/'quicktest3_isolated.py').write_bytes((BASE/'harness/quicktest3_isolated.py').read_bytes())
    write(HERE/'isolation.json',{'runtime_isolation':ISOLATION,'additional_write_guard':'own directory only','harness_copy_byte_identical':file_hash(HERE/'quicktest3_isolated.py')==file_hash(BASE/'harness/quicktest3_isolated.py')})
if __name__=='__main__':
    if sys.argv[1]=='snapshot':snapshot()
    elif sys.argv[1]=='inspect':inspect_all()
