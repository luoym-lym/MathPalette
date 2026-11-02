from tools26 import *
names=['exploration_report.json','remaining_questions.jsonl'];items=[]
for q in ASSIGNED:
    a=read(HERE/q/'prior_history_audit.json')
    for rel in a['old_evidence_file_sha256']:
        path=ROOT/rel
        if path.suffix!='.json' or not any(s in path.name for s in ['eligibility','fingerprint','audit','render_check']):continue
        try:obj=read(path)
        except (ValueError,OSError):continue
        def walk(x,keys):
            if isinstance(x,dict):
                for k,v in x.items():
                    if isinstance(v,str) and len(v)==64 and any(n in k for n in names):
                        name=next(n for n in names if n in k);cur=file_hash(BASE/name)
                        items.append({'question_id':q,'historical_evidence_file':rel,'json_key_path':keys+[k],'historical_recorded_sha256':v,'current_sha256':cur,'changed':v!=cur,'classification':'mutable parent runtime progress metadata; not a frozen original or eligibility gate; historical file remains unchanged'})
                    walk(v,keys+[k])
            elif isinstance(x,list):
                for i,v in enumerate(x):walk(v,keys+[i])
        walk(obj,[])
write(HERE/'historical_progress_hash_classification.json',{'created_at':now(),'stage':'material_refinement','records':items,'changed_count':sum(i['changed'] for i in items),'authoritative_current_eligibility_basis':'Formal per-question record, current original approval content fingerprint, accepted/collected indices, per-question recipes/collection and immutable delivered manifests.','no_old_snapshot_rewrite':True})
print(json.dumps({'historical_mutable_hash_entries':len(items),'changed':sum(i['changed'] for i in items)}))
