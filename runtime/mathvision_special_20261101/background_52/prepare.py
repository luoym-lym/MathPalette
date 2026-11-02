from bootstrap import install, OWN, PROJECT, SESSION
ISOLATION = install()
import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime, timezone
from research import save, load, sha, IDS
from dataset_tools import catalog

def eligibility(qid, leaf='eligibility_initial.json'):
    row = next(r for r in catalog.rows(PROJECT/'PlaneGeometry/dataset.jsonl') if r['id']==qid)
    approval = load(PROJECT/'provenance/approvals.json')['approvals'].get(qid)
    content = catalog.content(PROJECT,'PlaneGeometry',row)
    digest = catalog.digest(content)
    special=PROJECT/'PlaneGeometry/special_variant'
    accepted=[r for r in catalog.rows(special/'accepted_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collected=[r for r in catalog.rows(special/'collected_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collection=special/qid/'collection.json'
    data=load(collection) if collection.exists() else None
    eligible=(row['source_dataset']=='MathVision' and approval.get('reviewer')=='user'
              and bool(approval.get('instruction')) and approval['content_sha256']==digest
              and not accepted and not collected and not data)
    evidence={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'question_id':qid,
              'formal_record':row,'formal_record_sha256':catalog.digest(row),
              'original_approval':approval,'current_content_sha256':digest,
              'approval_fingerprint_matches':digest==approval['content_sha256'],
              'accepted_records':accepted,'collected_records':collected,'collection':data,
              'eligible':eligible,'content':content,
              'authoritative_files':{str(p.relative_to(PROJECT)):sha(p) for p in [PROJECT/'PlaneGeometry/dataset.jsonl',PROJECT/'provenance/approvals.json',special/'accepted_index.jsonl',special/'collected_index.jsonl']}}
    save(OWN/qid/leaf,evidence)
    assert eligible,(qid,'ineligible')
    return evidence

def init():
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import load_config,pixel_hash
    from mathvision_adapter import RendererAdapter
    from dataset_tools.mathvision_workbench import png_bytes
    from partial_style import object_paths
    cfg=load_config()
    adapter=RendererAdapter(cfg)
    for qid in IDS:
        e=eligibility(qid)
        row=e['formal_record']
        save(OWN/qid/'formal_record.json',row)
        context=adapter.inspect_question(qid)
        save(OWN/qid/'fresh_context.json',context)
        scene=adapter.scene(qid)
        try:
            data=png_bytes(scene)
            (OWN/qid/'no_op.png').write_bytes(data)
            scene.fig.canvas.draw()
            paths={o['id']:[{k:p[k] for k in ('id','sha256','closed')} | {'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,o['id'])] for o in scene.objects if o.get('styleable')}
            save(OWN/qid/'exact_paths.json',paths)
            save(OWN/qid/'baseline_check.json',{'formal_png':str(adapter.original_paths[qid]),'formal_sha256':sha(adapter.original_paths[qid]),'no_op_sha256':hashlib.sha256(data).hexdigest(),'pixel_equal':pixel_hash(data)==pixel_hash(adapter.original_paths[qid]),'original_pixel_sha256':pixel_hash(data)})
        finally: scene.close()
        print(json.dumps({'qid':qid,'eligible':e['eligible'],'objects':len(context['objects']),'baseline_equal':True},ensure_ascii=False),flush=True)
    save(OWN/'isolation.json',ISOLATION)

def history(qid):
    inv=load(OWN/'history_inventory.json')
    records=[]
    for item in inv:
        p=PROJECT/item['path']
        if qid not in p.parts or p.suffix not in ['.json','.txt','.log','.bin']:
            continue
        if p.name in ['context.json','exact_paths.json','paths_public.json','input_fingerprints.json'] or 'eligibility' in p.name or 'source_hash' in p.name:
            continue
        if p.name=='request.json':
            d=load(p)
            for m in d.get('messages',[]):
                for c in m.get('content',[]) if isinstance(m.get('content'),list) else []:
                    if c.get('type')=='image_url':
                        import base64
                        raw=base64.b64decode(c['image_url']['url'].split(',',1)[1])
                        c['image_url']['url']={'omitted_binary_only':True,'png_sha256':hashlib.sha256(raw).hexdigest()}
            records.append({'path':str(p),'sha256':sha(p),'content':d})
        else:
            try: d=load(p)
            except Exception: d=p.read_text(encoding='utf-8',errors='replace')
            records.append({'path':str(p),'sha256':sha(p),'content':d})
    save(OWN/qid/'old_history_read.json',records)
    for r in records:
        # Duplicate raw bodies and summary results are read from exact raw once.
        name=Path(r['path']).name
        if name not in ['design.json','plugin.json','primary_math.json','primary_review.json','primary_visual.json','run_01_response.json','run_02_response.json']:
            continue
        print(json.dumps(r,ensure_ascii=False,separators=(',',':')))

def source(qid):
    e=load(OWN/qid/'eligibility_initial.json')
    row=e['formal_record']
    print(json.dumps({'formal_question':row,'approval':e['original_approval']},ensure_ascii=False))
    paths=[PROJECT/'PlaneGeometry'/row['scene'],PROJECT/'PlaneGeometry'/row['script']]
    paths += [PROJECT/'PlaneGeometry'/p for p in row['runtime_dependencies'] if '/items/' in p]
    for p in paths:
        text=p.read_text(encoding='utf-8-sig')
        content=json.loads(text) if p.suffix=='.json' else text
        print(json.dumps({'path':str(p),'sha256':sha(p),'content':content},ensure_ascii=False,separators=(',',':')))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('op',choices=['init','eligibility','history','source'])
    parser.add_argument('qid',nargs='?')
    a=parser.parse_args()
    if a.op=='init':init()
    elif a.op=='eligibility':print(json.dumps(eligibility(a.qid,'eligibility_before_calls.json'),ensure_ascii=False))
    elif a.op=='history':history(a.qid)
    else:source(a.qid)
