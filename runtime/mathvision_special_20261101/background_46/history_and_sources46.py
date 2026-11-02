from tools46 import *
assert not (OWN/'external_failure_stop.json').exists()
def find(v,q):
    if isinstance(v,dict):
        if v.get('question_id')==q or v.get('id')==q:return [v]
        return [r for x in v.values() for r in find(x,q)]
    if isinstance(v,list):return [r for x in v for r in find(x,q)]
    return []
folders=[p for p in TASK.rglob('*') if p.is_dir() and p.name in IDS and not p.is_relative_to(OWN)]
for q in IDS:
    directory=OWN/q;directory.mkdir(parents=True,exist_ok=True);prior=[p for p in folders if p.name==q];records=[];hashes={}
    for f in prior:
        for p in f.rglob('*'):
            if not p.is_file():continue
            hashes[str(p)]=sha(p)
            if p.suffix=='.json':
                value=read(p)
                if p.name in ['design.json','plugin.json','primary_review.json','manual_final_review.json','primary_prescreen.json','prescreen.json','assessment.json','untested_checkpoint.json'] or p.name.endswith('_response.json'):
                    records.append({'path':str(p),'sha256':sha(p),'full_content':value})
    cps=[]
    for p in TASK.rglob('checkpoint.json'):
        if p.is_relative_to(OWN):continue
        rows=find(read(p),q)
        if rows:cps.append({'path':str(p),'sha256':sha(p),'full_question_rows':rows})
    save(directory/'full_old_history_read_46.json',{'question_id':q,'all_prior_folders':[str(p) for p in prior],'all_prior_files_sha256':hashes,'full_old_records':records,'full_checkpoint_rows':cps,'old_source_controls_reused_no_new_calls':True})
    print(q,'old folders',[str(p.relative_to(TASK)) for p in prior],'records',len(records),flush=True)
    if q not in ['Solid104','Solid141','Solid189']:continue
    assert not (OWN/'external_failure_stop.json').exists()
    e=eligibility(q);save(directory/'eligibility_46.json',e);assert e['eligible']
    ctx=AD.inspect_question(q);save(directory/'context_46.json',ctx)
    save(directory/'formal_record_46.json',AD.records[q])
    save(directory/'source_scene_46.json',read(AD.branch/AD.records[q]['scene']))
    native=next(p for p in AD.records[q]['runtime_dependencies'] if p.endswith('/scene.json'))
    save(directory/'native_scene_46.json',read(AD.branch/native))
    s=AD.scene(q)
    try:
        b,ph=scene_png(s);assert ph==pixel_hash(AD.original_paths[q]);(directory/'noop_46.png').write_bytes(b)
    finally:s.close()
    print(q,'current source/noop/eligibility inspected',flush=True)
