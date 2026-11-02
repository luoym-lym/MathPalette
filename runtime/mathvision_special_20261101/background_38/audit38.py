from common38 import *
def mentions(d,q):
    if isinstance(d,dict):
        if d.get('question_id',d.get('id'))==q:return [d]
        return [x for v in d.values() for x in mentions(v,q)]
    if isinstance(d,list):return [x for v in d for x in mentions(v,q)]
    return []
history={q:{'designs':[],'bindings':[],'prior_assessments':[]} for q in QIDS}
oldfiles={}
for p in BASE.rglob('design.json'):
    if p.is_relative_to(TASK):continue
    d=read(p);q=d.get('question_id')
    if q in QIDS:
        history[q]['designs'].append({'path':str(p),'sha256':sha(p),'full_design':d,'plugin':read(p.parent/'plugin.json') if (p.parent/'plugin.json').exists() else None})
        for f in p.parent.rglob('*'):
            if f.is_file():oldfiles[str(f.relative_to(ROOT))]=sha(f)
for p in BASE.rglob('binding.json'):
    if p.is_relative_to(TASK):continue
    d=read(p);q=d.get('question_id')
    if q in QIDS:
        entries=[]
        for f in sorted(p.parent.glob('run_*.json')):
            if f.name.endswith('_response.json'):
                v=read(f);entries.append({'path':str(f),'sha256':sha(f),'raw':v})
            elif not f.name.endswith('_started.json'):entries.append({'path':str(f),'sha256':sha(f),'data':read(f)})
        history[q]['bindings'].append({'binding_path':str(p),'sha256':sha(p),'binding':d,'runs':entries})
        for f in p.parent.iterdir():
            if f.is_file():oldfiles[str(f.relative_to(ROOT))]=sha(f)
for folder in ['background_03','background_04','background_11','background_19']:
    p=BASE/folder/'checkpoint.json'
    if p.exists():
        data=read(p)
        for q in QIDS:
            found=mentions(data,q)
            if found:history[q]['prior_assessments'].append({'path':str(p),'sha256':sha(p),'records':found})
for q,h in history.items():
    write(TASK/q/'history_audit.json',h)
    print('\nHISTORY',q,json.dumps(h,ensure_ascii=False),flush=True)
write(TASK/'old_evidence_hashes_before.json',oldfiles)
for q in QIDS:
    c=read(TASK/q/'context.json')
    print('\nCONTEXT',q)
    for o in c['objects']:
        if q=='Plane229' and not o['id'].startswith(('frame','grid')):continue
        print(json.dumps({k:v for k,v in o.items() if k not in ['partial_paths','screen_points','pixel_points']},ensure_ascii=False))
    print('SNAPS',json.dumps(c['snap_points'],ensure_ascii=False))
