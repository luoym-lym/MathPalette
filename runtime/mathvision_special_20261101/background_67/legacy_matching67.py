from env67 import *
import gc
known={x['path'] for x in read(OWN/'legacy_scoped_full_history_audit.json')}
rows=[]
extras=[]
for rel in (OWN/'legacy_matching_JSON_paths.txt').read_text(encoding='utf-8-sig').splitlines():
    p=(PROJECT/rel).resolve()
    data=p.read_bytes(); row={'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'full_bytes_read':True}
    try:
        if p.suffix=='.jsonl': values=[json.loads(line) for line in data.decode('utf-8-sig').splitlines() if line.strip()]
        else: values=[json.loads(data.decode('utf-8-sig'))]
    except (UnicodeError,ValueError) as exc: row['parse_error']=str(exc)
    else:
        stack=list(values)
        while stack:
            v=stack.pop()
            if isinstance(v,dict):
                if v.get('question_id') in QIDS and isinstance(v.get('answer'),str) and len(v['answer'])>20:
                    if str(p) not in known:
                        extras.append({'path':str(p),'sha256':row['sha256'],'question_id':v['question_id'],'status':v.get('status'),'finish_reason':v.get('finish_reason'),'png_sha256':v.get('png_sha256',v.get('image_sha256')),'full_answer':v['answer']})
                stack.extend(v.values())
            elif isinstance(v,list): stack.extend(v)
        del stack,values
    rows.append(row); del data; gc.collect()
save('legacy_all_matching_JSON_full_read_audit.json',{'at':now(),'files':rows,'additional_full_raw_response_records':extras,'all_extant_matching_paths_only_read_no_restore':True})
with (OWN/'legacy_additional_full_finals.txt').open('x',encoding='utf-8') as f:
    for r in extras: f.write('\nFILE '+r['path']+'\nQUESTION '+r['question_id']+' STATUS '+str(r['status'])+'\n'+r['full_answer']+'\n')
print('ALL_LEGACY_MATCHING_JSON_FULL_READ',len(rows),'additional_raw_responses',len(extras),flush=True)
