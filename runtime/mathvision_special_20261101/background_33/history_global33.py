from tools33 import *
matches={q:[] for q in ASSIGNED};count=0
for p in BASE.rglob('design.json'):
    if p.is_relative_to(HERE):continue
    d=read(p);count+=1;q=d.get('question_id',d.get('id'))
    if q in matches:matches[q].append({'path':str(p.relative_to(ROOT)),'sha256':file_hash(p),'full_design':d})
report=read(BASE/'exploration_report.json')
selected=[]
def walk(v,path=''):
    if isinstance(v,dict):
        if v.get('question_id',v.get('id')) in ASSIGNED:selected.append({'json_path':path,'entry':v})
        else:
            for k,x in v.items():
                if k in ASSIGNED:selected.append({'json_path':path+'/'+k,'entry':x})
                else:walk(x,path+'/'+k)
    elif isinstance(v,list):
        for i,x in enumerate(v):walk(x,path+'/'+str(i))
walk(report)
result={'created_at':now(),'all_prior_design_jsons_scanned':count,'matches':matches,'mutable_progress_entries_read':selected,'mutable_progress_sha256':file_hash(BASE/'exploration_report.json'),'progress_metadata_only':True,'all_old_candidates_need_full_evidence_if_found':True}
write(HERE/'global_previous_design_search.json',result)
print(json.dumps({'scanned':count,'matches':{q:len(v) for q,v in matches.items()},'report_entries':selected},ensure_ascii=False),flush=True)
