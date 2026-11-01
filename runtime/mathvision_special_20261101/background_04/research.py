import os,sys,json,hashlib,importlib.util
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=ROOT/'runtime/mathvision_special_20261101'
for key,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target=HERE/name;target.mkdir(parents=True,exist_ok=True);os.environ[key]=str(target)
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(HERE/'render_tmp')
def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f:json.dump(value,f,ensure_ascii=False,indent=2,default=lambda v:v.tolist());f.write('\n')
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def jsonl(path):return [json.loads(l) for l in path.read_text(encoding='utf-8-sig').splitlines() if l.strip()] if path.exists() else []
def eligible(branch,qid):
    base=ROOT/branch;special=base/'special_variant';files={};reasons=[]
    record=next(r for r in jsonl(base/'dataset.jsonl') if r['id']==qid)
    if record['source_dataset']!='MathVision':reasons.append('not MathVision')
    for name,status in [('accepted_index.jsonl','passed'),('collected_index.jsonl','collected')]:
        p=special/name
        if p.exists():files[str(p.relative_to(ROOT))]=digest(p)
        if any(r.get('question_id')==qid and r.get('status')==status for r in jsonl(p)):reasons.append(name)
    p=special/qid/'recipes.json'
    if p.exists():
        files[str(p.relative_to(ROOT))]=digest(p);data=json.loads(p.read_text(encoding='utf-8-sig'))
        entries=data if isinstance(data,list) else data.get('recipes',data.get('variants',[]))
        if isinstance(entries,dict):entries=list(entries.values())
        if any(r.get('status')=='passed' or r.get('reviewed_at') for r in entries if isinstance(r,dict)):reasons.append('passed recipe')
    p=special/qid/'collection.json'
    if p.exists():
        files[str(p.relative_to(ROOT))]=digest(p);current=json.loads(p.read_text(encoding='utf-8-sig')).get('current',{})
        if current.get('status')=='collected' or current.get('collected_at') or current.get('special_case'):reasons.append('collection completed')
    queue=next(r for r in jsonl(BASE/'remaining_questions.jsonl') if r['question_id']==qid)
    if queue['status']!='not_yet_explored':reasons.append('already explored')
    report=json.loads((BASE/'exploration_report.json').read_text(encoding='utf-8-sig'))
    if any(r['question_id']==qid for r in report['attempts']):reasons.append('report already assessed')
    files[str((base/'dataset.jsonl').relative_to(ROOT))]=digest(base/'dataset.jsonl')
    return {'question_id':qid,'branch':branch,'eligible':not reasons,'reasons':reasons,'queue_status':queue['status'],'checked_at':datetime.now(timezone.utc).isoformat(),'input_hashes':files}
def inputs(branch,record):
    rels=[record[k] for k in ['image','scene','script','original_image'] if record.get(k)]+record.get('runtime_dependencies',[])
    paths=[ROOT/branch/p for p in rels]
    paths += [ROOT/'MATHPALETTE_PROTOCOL.md',ROOT/'dataset_tools/mathvision_workbench.py']
    paths += [ROOT/branch/p for p in ['REDRAW_PROTOCOL.md','dataset_generator/protocol.json','workbench/plugin.schema.json','workbench/config.json','workbench/render_plugins.py','workbench/renderer_adapter.py','workbench/partial_style.py','workbench/workbench_io.py']]
    return {p.relative_to(ROOT).as_posix():digest(p) for p in sorted(set(paths))}
def adapter(branch):
    sys.path.insert(0,str(ROOT/branch/'workbench'))
    from workbench_io import load_config
    cfg=load_config();cfg['runtime_dir']=str(HERE/'state'/branch);cfg['output_dir']=str(HERE/'output'/branch)
    if branch=='PlaneGeometry':
        from mathvision_adapter import RendererAdapter
        from mathvision_plugins import PluginRenderer
    else:
        from delivery_bridge_adapter import RendererAdapter
        from render_plugins import PluginRenderer
    return cfg,RendererAdapter(cfg),PluginRenderer
def inspect(branch,qids):
    cfg,ad,PR=adapter(branch)
    for qid in qids:
        check=eligible(branch,qid);assert check['eligible'],check
        folder=HERE/qid;record=ad.records[qid];before=inputs(branch,record)
        context=ad.inspect_question(qid)
        write(folder/'eligibility_before_assessment.json',check);write(folder/'context.json',context);write(folder/'formal_record.json',record);write(folder/'frozen_inputs.json',before)
        (folder/'original.png').write_bytes(ad.original_paths[qid].read_bytes())
        assert inputs(branch,record)==before
        print(json.dumps({'question_id':qid,'question':record['question'],'answer':record['answer'],'objects':context['objects'],'snap_points':context['snap_points'],'source_script':record['script'],'scene':record['scene']},ensure_ascii=False),flush=True)
def audit(action):
    spec=importlib.util.spec_from_file_location('_old_inventory_readonly',BASE/'inventory.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    if action=='before':
        files=mod.scan()
        write(HERE/'formal_files_before.json',files)
        old={}
        for parent,dirs,names in os.walk(BASE):
            if Path(parent)==BASE:dirs[:]=[d for d in dirs if d not in ['background_04','harness']]
            for name in names:
                p=Path(parent)/name;old[p.relative_to(ROOT).as_posix()]=digest(p)
        write(HERE/'previous_evidence_before.json',old)
        print('Baseline files',len(files),'old evidence',len(old))
    else:
        before=json.loads((HERE/'formal_files_before.json').read_text(encoding='utf-8'));after=mod.scan()
        old=json.loads((HERE/'previous_evidence_before.json').read_text(encoding='utf-8'))
        value={'checked_at':datetime.now(timezone.utc).isoformat(),'formal_checked_count':len(before),'formal_changed':[p for p in before.keys()&after.keys() if before[p]!=after[p]],'formal_added':sorted(after.keys()-before.keys()),'formal_deleted':sorted(before.keys()-after.keys()),'previous_evidence_checked_count':len(old),'previous_evidence_changed_or_deleted':[p for p,h in old.items() if not (ROOT/p).is_file() or digest(ROOT/p)!=h]}
        write(HERE/'source_preservation_audit.json',value);print(json.dumps(value,ensure_ascii=False))
if __name__=='__main__':
    if sys.argv[1]=='inspect':inspect(sys.argv[2],sys.argv[3:])
    elif sys.argv[1]=='audit':audit(sys.argv[2])
