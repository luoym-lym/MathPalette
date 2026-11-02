from bootstrap import HERE, PROJECT, TASK, renderer_setup
import json, hashlib, sys, gc, base64
from datetime import datetime, timezone
from pathlib import Path

IDS = ['Solid134','Solid165','Solid212','Solid218','Solid222','Solid223','Solid227','Solid235']
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,obj):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8') as f: json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def record(q):
    with (PROJECT/'SolidGeometry/dataset.jsonl').open(encoding='utf-8-sig') as f:
        for line in f:
            r=json.loads(line)
            if r['id']==q:return r
    raise ValueError(q)
def eligible(q,out):
    from dataset_tools.catalog import content,digest
    r=record(q);a=read(PROJECT/'provenance/approvals.json')['approvals'][q]
    c=content(PROJECT,'SolidGeometry',r)
    actual=digest(c)
    idx={}
    for name in ('accepted_index.jsonl','collected_index.jsonl'):
        p=PROJECT/'SolidGeometry/special_variant'/name
        if not p.exists(): p=PROJECT/'SolidGeometry'/name
        entries=[]
        if p.exists():
            with p.open(encoding='utf-8-sig') as f:
                for l in f:
                    if l.strip():
                        row=json.loads(l)
                        if row.get('question_id',row.get('id'))==q:entries.append(row)
        idx[name]={'path':str(p),'sha256':sha(p) if p.exists() else None,'entries':entries}
    specials={}
    for name in ('recipes.json','collection.json'):
        p=PROJECT/'SolidGeometry/special_variant'/q/name
        specials[name]={'exists':p.exists(),'sha256':sha(p) if p.exists() else None}
    valid=(r['source_dataset']=='MathVision' and actual==a['content_sha256'] and a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and not any(x['entries'] for x in idx.values()) and not any(x['exists'] for x in specials.values()))
    audit={'question_id':q,'created_at':datetime.now(timezone.utc).isoformat(),'eligible':valid,'approval':a,'computed_content_sha256':actual,'content':c,'indices':idx,'special_records':specials}
    save(out,audit)
    if not valid:raise ValueError('Eligibility failed '+q)
    return r

def history():
    # Names/directories first; full raw objects are read one at a time and released.
    manifests=[]
    for q in IDS:
        folder=HERE/q;folder.mkdir(exist_ok=True)
        eligible(q,folder/'eligibility_initial.json')
        save(folder/'formal_record.json',record(q))
        files=[]
        for p in TASK.rglob('*'):
            if not p.is_file() or p.is_relative_to(HERE):continue
            if q in p.parts and p.suffix.lower() in ('.json','.png','.jpg','.log','.bin','.py','.txt'):
                files.append({'path':str(p),'sha256':sha(p),'size':p.stat().st_size})
        save(folder/'old_evidence_manifest.json',files)
        with (folder/'old_full_text.txt').open('x',encoding='utf-8') as out:
            for item in files:
                p=Path(item['path'])
                if p.suffix!='.json' or p.name=='request.json':continue
                data=read(p)
                out.write('\nFILE '+str(p)+'\n')
                if p.name.endswith('_response.json'):
                    out.write(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
                elif p.stat().st_size<150000:
                    out.write(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
                else:
                    out.write('large context separately audited, see immutable manifest\n')
                del data
        print(q,len(files),'eligibility verified',flush=True)
        del files;gc.collect()
    sources=[]
    for q in IDS:
        for rel,h in read(HERE/q/'eligibility_initial.json')['content']['files'].items():
            p=(PROJECT/'SolidGeometry'/rel).resolve()
            sources.append({'path':str(p),'sha256':h})
    save(HERE/'source_hashes_initial.json',sources)

def inspect(q):
    renderer_setup()
    from delivery_bridge_adapter import RendererAdapter
    from renderer_adapter import scene_png
    import matplotlib.pyplot as plt
    adapter=RendererAdapter({'dataset_file':str(PROJECT/'SolidGeometry/dataset.jsonl')})
    c=adapter.inspect_question(q)
    save(HERE/q/'context_fresh.json',c)
    s=adapter.scene(q)
    try:
        png,pix=scene_png(s)
        (HERE/q/'noop.png').write_bytes(png)
        save(HERE/q/'noop_check.json',{'pixel_hash':pix,'context_original_pixel_hash':c['original_pixel_sha256'],'matches':pix==c['original_pixel_sha256'],'noop_sha256':sha(HERE/q/'noop.png')})
    finally:s.close();plt.close('all')
    print(q,'native context/no-op saved',flush=True)

if __name__=='__main__':
    if sys.argv[1]=='history':history()
    elif sys.argv[1]=='inspect':inspect(sys.argv[2])
    elif sys.argv[1]=='eligibility':eligible(sys.argv[2],Path(sys.argv[3]))
