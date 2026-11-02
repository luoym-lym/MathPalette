import task_env
from task_env import OWN, PROJECT
import json, hashlib, re
from pathlib import Path
from datetime import datetime, timezone
from dataset_tools.catalog import content, digest
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from workbench_io import pixel_hash, load_config

IDS = ['Plane468','Plane469','Plane472','Plane473','Plane475','Plane476','Plane477','Plane479']
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p, v):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def hashfile(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def eligibility(qid):
    record=next(json.loads(x) for x in (PROJECT/'PlaneGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if json.loads(x)['id']==qid)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    payload=content(PROJECT,'PlaneGeometry',record)
    h=digest(payload)
    special=PROJECT/'PlaneGeometry/special_variant'
    matches={}
    for name in ('accepted_index.jsonl','collected_index.jsonl'):
        p=special/name
        matches[name]=[json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip() and qid in x] if p.exists() else []
    local={name:read(special/qid/name) if (special/qid/name).exists() else None for name in ('collection.json','recipes.json')}
    ok=record['source_dataset']=='MathVision' and approval.get('reviewer')=='user' and bool(approval.get('instruction')) and approval['content_sha256']==h and not any(matches.values()) and not any(local.values())
    return {'checked_at_utc':datetime.now(timezone.utc).isoformat(),'formal_record':record,'approval':approval,'computed_content_sha256':h,'approval_fingerprint_matches':h==approval['content_sha256'],'indices':matches,'local_special':local,'eligible':ok,'source_hashes':payload['files']}

if __name__=='__main__':
    config=load_config()
    adapter=RendererAdapter(config)
    history={}
    preservation={}
    allfiles=[p for p in OWN.parent.rglob('*') if p.is_file() and not p.is_relative_to(OWN)]
    for qid in IDS:
        target=OWN/qid; target.mkdir(exist_ok=True)
        e=eligibility(qid); write(target/'eligibility_initial.json',e)
        assert e['eligible'],qid
        context=adapter.inspect_question(qid)
        write(target/'context.json',context)
        s=adapter.scene(qid)
        try:
            b=png_bytes(s); (target/'noop.png').write_bytes(b)
            assert pixel_hash(b)==pixel_hash(PROJECT/'PlaneGeometry/image'/f'{qid}.png')
        finally: s.close()
        record=e['formal_record']
        for p,h in e['source_hashes'].items(): preservation[str((PROJECT/'PlaneGeometry'/p).resolve())]=h
        roots=sorted({p.parents[len(p.parts)-p.parts.index(qid)-2] if False else p for p in []})
        relevant=[p for p in allfiles if qid in p.parts or (p.name in ('checkpoint.json','exploration_report.json','remaining_questions.jsonl','agent_summary.json') and qid in p.read_text(encoding='utf-8-sig',errors='replace'))]
        entries=[]
        textparts=[]
        for p in relevant:
            preservation[str(p)]=hashfile(p)
            entry={'path':str(p),'sha256':hashfile(p),'bytes':p.stat().st_size}
            if p.suffix in ('.json','.jsonl','.txt','.md') and p.name not in ('request.json','context.json','path_context.json','exact_paths.json','path_fingerprints.json','render_check.json','input_fingerprints.json','frozen_inputs.json'):
                t=p.read_text(encoding='utf-8-sig',errors='replace')
                if qid in p.parts:
                    textparts.append('\nFILE '+str(p)+'\n'+t)
                elif p.suffix=='.json':
                    try:
                        data=json.loads(t)
                        def matching(x):
                            if isinstance(x,dict):
                                if any(x.get(k)==qid for k in ('question_id','id')): return [x]
                                return sum((matching(v) for v in x.values()),[])
                            if isinstance(x,list): return sum((matching(v) for v in x),[])
                            return []
                        textparts.append('\nFILE '+str(p)+' MATCHES\n'+json.dumps(matching(data),ensure_ascii=False,indent=2))
                    except Exception as err: entry['parse_error_preserved']=str(err)
            entries.append(entry)
        history[qid]=entries
        (target/'old_history_reading.txt').write_text('\n'.join(textparts),encoding='utf-8')
        print(qid,'eligible',len(context['objects']),'objects',len(entries),'history files',flush=True)
    write(OWN/'old_history_inventory.json',history)
    write(OWN/'preservation_before.json',preservation)
    write(OWN/'isolation.json',task_env.ISOLATION)
