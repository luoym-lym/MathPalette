from tools40 import *
def find(x,q):
    if isinstance(x,dict):
        if x.get('question_id')==q or x.get('id')==q:return [x]
        return [r for v in x.values() for r in find(v,q)]
    if isinstance(x,list):return [r for v in x for r in find(v,q)]
    return []
folders=[p for p in BASE.rglob('*') if p.is_dir() and p.name in IDS and not p.is_relative_to(TASK) and not any(s.startswith('batch_') or s=='delivery_supplements' or s=='delivery_validation' or s=='independent_review' for s in p.relative_to(BASE).parts)]
for q in IDS:
    prior=[p for p in folders if p.name==q]
    files={str(p.relative_to(ROOT)):file_hash(p) for f in prior for p in f.rglob('*') if p.is_file()}
    records=[]
    for f in prior:
        for p in f.rglob('*.json'):
            if p.name in ['design.json','plugin.json','primary_review.json','manual_final_review.json','primary_prescreen.json','prescreen.json','independent_review.json'] or p.name.endswith('_response.json'):
                records.append({'path':str(p.relative_to(ROOT)),'content':read(p)})
    cps=[]
    for p in BASE.rglob('checkpoint.json'):
        if p.is_relative_to(TASK):continue
        if any(str(f).startswith(str(p.parent)) for f in prior):
            rows=find(read(p),q)
            cps.append({'path':str(p.relative_to(ROOT)),'rows':rows})
    write(TASK/q/'history_audit.json',{'question_id':q,'folders':[str(f.relative_to(ROOT)) for f in prior],'all_prior_files_sha256':files,'full_records':records,'checkpoint_rows':cps,'read_only':True})
    print(q,'prior folders',[str(f.relative_to(BASE)) for f in prior],'designs',sum(r['path'].endswith('/design.json') for r in records),'raw replies',sum(r['path'].endswith('_response.json') for r in records))
    for r in records:
        if r['path'].endswith('prescreen.json') or r['path'].endswith('design.json') or r['path'].endswith('plugin.json') or r['path'].endswith('manual_final_review.json') or r['path'].endswith('primary_review.json'):
            print(json.dumps(r,ensure_ascii=False))
    for cp in cps:print(json.dumps(cp,ensure_ascii=False))
write(TASK/'history_discovery.json',{'folders':[str(f) for f in folders],'completed_at':now()})
