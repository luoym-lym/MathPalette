import task_env
from task_env import OWN, PROJECT, BASE
import json, hashlib, sys
from datetime import datetime, timezone
from pathlib import Path
from dataset_tools import catalog

def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,v): Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
QIDS=read(BASE/'background_44_assignment.json')['question_ids']

def eligibility(qid):
    row=next(r for r in catalog.rows(PROJECT/'PlaneGeometry/dataset.jsonl') if r['id']==qid)
    app=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    contents=catalog.content(PROJECT,'PlaneGeometry',row)
    computed=catalog.digest(contents)
    root=PROJECT/'PlaneGeometry/special_variant'
    indices={n: [r for r in catalog.rows(root/n) if r.get('question_id',r.get('id'))==qid]
             if (root/n).exists() else [] for n in ['accepted_index.jsonl','collected_index.jsonl']}
    question_records={n:read(root/qid/n) if (root/qid/n).exists() else None for n in ['recipes.json','collection.json']}
    eligible=row['source_dataset']=='MathVision' and app.get('reviewer')=='user' and bool(app.get('instruction')) and computed==app['content_sha256'] and not any(indices.values()) and not any(question_records.values())
    return {'checked_at_utc':datetime.now(timezone.utc).isoformat(),'formal_record':row,
            'approval':app,'computed_content_sha256':computed,'valid_original_approval':computed==app['content_sha256'],
            'accepted_collected_matches':indices,'special_records':question_records,'eligible':eligible,'content':contents}

if __name__=='__main__':
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import load_config, pixel_hash
    from mathvision_adapter import RendererAdapter
    from dataset_tools.mathvision_workbench import png_bytes
    config=load_config()
    config['runtime_dir']=str(OWN/'adapter_runtime')
    config['output_dir']=str(OWN/'adapter_output')
    adapter=RendererAdapter(config)
    save(OWN/'isolation.json',{'environment':{n:__import__('os').environ[n] for n in ['TEMP','TMP','TMPDIR','MPLCONFIGDIR','XDG_CACHE_HOME']},'strict_own_write_guard':True,'bridge':task_env.ISOLATION})
    preservation={}
    old_files={}
    for qid in QIDS:
        folder=OWN/qid; folder.mkdir(exist_ok=True)
        elig=eligibility(qid); save(folder/'eligibility_start.json',elig)
        assert elig['eligible'],qid
        row=elig['formal_record']; save(folder/'formal_record.json',row)
        context=adapter.inspect_question(qid); save(folder/'context.json',context)
        scene=adapter.scene(qid)
        try: noop=png_bytes(scene)
        finally: scene.close()
        (folder/'noop.png').write_bytes(noop)
        assert pixel_hash(noop)==pixel_hash(PROJECT/'PlaneGeometry'/row['image'])
        paths=[PROJECT/'PlaneGeometry'/p for p in elig['content']['files'] if not p.startswith('../')]
        paths += [PROJECT/'dataset_tools/geometry_dataset.py']
        for p in paths: preservation[str(p)]=sha(p)
        matches=[p for p in BASE.rglob('*') if p.is_file() and qid in p.parts and not p.is_relative_to(OWN)]
        old_files[qid]=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in matches]
        for p in matches: preservation[str(p)]=sha(p)
        save(folder/'old_file_inventory.json',old_files[qid])
        print(qid, 'eligible',elig['valid_original_approval'],'objects',len(context['objects']),'historical_files',len(matches),flush=True)
    for p in [PROJECT/'AGENTS.md',PROJECT/'MATHPALETTE_PROTOCOL.md',PROJECT/'PlaneGeometry/REDRAW_PROTOCOL.md',PROJECT/'PlaneGeometry/dataset_generator/protocol.json',PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json',BASE/'background_44_brief.txt',BASE/'background_44_assignment.json']:
        preservation[str(p)]=sha(p)
    for p in (PROJECT/'PlaneGeometry/workbench').glob('*.py'): preservation[str(p)]=sha(p)
    save(OWN/'preservation_start.json',preservation)
    save(OWN/'old_file_inventory.json',old_files)
