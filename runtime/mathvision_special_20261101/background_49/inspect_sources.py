import research_env as env
from pathlib import Path
import json
import hashlib
import sys
from datetime import datetime, timezone
from dataset_tools.catalog import content, digest, read, rows

ROOT, PROJECT, SHARED = env.ROOT, env.PROJECT, env.SHARED
QIDS = ['Solid80','Solid89','Solid90','Solid107','Solid159','Solid163','Solid171','Solid172']
def now(): return datetime.now(timezone.utc).isoformat()
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def save(path,value):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False,default=lambda x:x.tolist() if hasattr(x,'tolist') else str(x))+'\n',encoding='utf-8')
def eligibility(qid):
    row=next(r for r in rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']==qid)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'].get(qid,{})
    calculated=digest(content(PROJECT,'SolidGeometry',row))
    out=PROJECT/'SolidGeometry/special_variant'
    indices={}
    for name in ['accepted_index.jsonl','collected_index.jsonl']:
        path=out/name
        indices[name]=[r for r in rows(path) if r.get('question_id',r.get('id'))==qid] if path.exists() else []
    special={name:read(out/qid/name) if (out/qid/name).exists() else None for name in ['recipes.json','collection.json']}
    approved=bool(approval.get('reviewer')=='user' and approval.get('instruction') and approval.get('approved_at_utc') and calculated==approval.get('content_sha256'))
    excluded=bool(any(indices.values()) or special['recipes.json'] or (special['collection.json'] and special['collection.json'].get('status')!='reopened'))
    return {'checked_at_utc':now(),'formal_record':row,'approval':approval,'computed_current_content_sha256':calculated,
            'current_approval_valid':approved,'authoritative_special_indices':indices,'question_special_records':special,
            'eligible': row['source_dataset']=='MathVision' and approved and not excluded}

def prepare():
    sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
    from delivery_bridge_adapter import RendererAdapter
    from renderer_adapter import scene_png
    from partial_style import object_paths
    from workbench_io import load_config
    from PIL import Image
    config=load_config()
    adapter=RendererAdapter(config)
    preservation={}
    history={'created_at_utc':now(),'questions':{},'parse_failures':[]}
    allpaths=list(SHARED.rglob('*'))
    for qid in QIDS:
        directory=ROOT/qid; directory.mkdir(exist_ok=True)
        e=eligibility(qid); save(directory/'eligibility_start.json',e)
        assert e['eligible'],qid
        r=e['formal_record']
        current=content(PROJECT,'SolidGeometry',r)
        save(directory/'input_fingerprints.json',current)
        save(directory/'formal_record.json',r)
        save(directory/'formal_scene.json',read(PROJECT/'SolidGeometry'/r['scene']))
        preservation.update({str((PROJECT/'SolidGeometry'/p).resolve()):h for p,h in current['files'].items()})
        ctx=adapter.inspect_question(qid); save(directory/'context.json',ctx)
        scene=adapter.scene(qid)
        try:
            data,pixels=scene_png(scene)
            (directory/'noop.png').write_bytes(data)
            scene.fig.canvas.draw()
            paths={o['id']:object_paths(scene,o['id']) for o in scene.objects if o.get('styleable')}
            save(directory/'paths.json',paths)
            save(directory/'baseline_check.json',{'noop_pixel_sha256':pixels,'formal_pixel_sha256':ctx['original_pixel_sha256'],
                 'noop_matches_formal':pixels==ctx['original_pixel_sha256'],'noop_sha256':hashlib.sha256(data).hexdigest(),
                 'formal_png_sha256':sha(PROJECT/'SolidGeometry'/r['image']),'source_jpg_sha256':sha(PROJECT/'SolidGeometry'/r['original_image'])})
        finally: scene.close()
        oldfiles=[p for p in allpaths if p.is_file() and not p.is_relative_to(ROOT) and qid in p.relative_to(SHARED).parts]
        entries=[]
        for p in oldfiles:
            stat=p.stat(); h=sha(p); preservation[str(p)]=h
            item={'path':str(p),'sha256':h,'bytes':stat.st_size}
            if p.suffix=='.json':
                try: item['parsed']=json.loads(p.read_text(encoding='utf-8-sig'))
                except Exception as exc:
                    item['parse_failure']=str(exc); history['parse_failures'].append(item.copy())
            entries.append(item)
        history['questions'][qid]=entries
        print(qid, 'eligible',e['eligible'],'objects',len(ctx['objects']),'old_files',len(entries),flush=True)
    for p in [PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json',PROJECT/'SolidGeometry/dataset.jsonl',
              SHARED/'delivery_bridge_adapter.py',SHARED/'runtime_isolation.py',SHARED/'harness/quicktest3_isolated.py']:
        preservation[str(p)]=sha(p)
    for p in (PROJECT/'SolidGeometry/workbench').glob('*'):
        if p.is_file(): preservation[str(p)]=sha(p)
    save(ROOT/'preservation_before.json',preservation)
    save(ROOT/'old_evidence_full_index.json',history)
    print('history parse failures',len(history['parse_failures']))

if __name__=='__main__': prepare()
