from bootstrap import HERE, TASK, PROJECT
from audit import read, sha, save, IDS
from pathlib import Path
import sys
import json

def prose(value):
    if isinstance(value,dict):
        return {k:prose(v) for k,v in value.items() if not any(w in k.lower() for w in ('hash','sha256','fingerprint','file','coordinate','geometry','source_local','all_choice','timestamps','snapshot','environment'))}
    if isinstance(value,list):
        return [prose(x) for x in value if not isinstance(x,(int,float))]
    return value

mode=sys.argv[1]
if mode=='raw235':
    p=next((TASK/'background_15/Solid235').rglob('run_01_response.json'))
    d=read(p)
    text=d['choices'][0]['message']['content']
    start=int(sys.argv[2])
    print('full content length',len(text),'slice',start,min(start+18000,len(text)))
    print(text[start:start+18000])
elif mode=='reviews':
    for path in ['independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json','independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']:
        p=TASK/path
        d=read(p)
        print(path)
        print('ALL KEYS',list(d))
        print(json.dumps({k:v for k,v in d.items() if k in ('decision','reason','requirement_disposition','human_semantics_disposition','concrete_objections','blocking_reason','semantics','native_visual_review','human_semantics')},ensure_ascii=False,indent=2))
elif mode=='context':
    q=sys.argv[2]
    c=read(HERE/q/'context_fresh.json')
    print('CANVAS',c['canvas'],'VIEW',c['xlim'],c['ylim'])
    for obj in c['objects']:
        print(json.dumps({k:v for k,v in obj.items() if k not in ('partial_paths',)},ensure_ascii=False))
    print('SNAP',json.dumps(c['snap_points'],ensure_ascii=False))
elif mode=='sources':
    q=sys.argv[2]
    r=read(HERE/q/'formal_record.json')
    for rel in [r['scene'],r['script']]+[v for v in r['runtime_dependencies'] if '/items/'+q+'/' in v]:
        p=PROJECT/'SolidGeometry'/rel
        print('SOURCE',p,'SHA256',sha(p))
        print(p.read_text(encoding='utf-8-sig'))
elif mode=='history':
    q=sys.argv[2]
    for entry in read(HERE/q/'history_full_relevant.json'):
        p=Path(entry['path'])
        if p.name.endswith('_response.json') or p.name in ('summary.json','binding.json'):
            continue
        print(entry['path'])
        print(json.dumps(entry['content'],ensure_ascii=False,indent=2))
elif mode=='parent':
    text=(TASK/'continuation_brief.txt').read_text(encoding='utf-8-sig')
    print(text)
