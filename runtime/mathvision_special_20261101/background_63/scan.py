from bootstrap import *
import base64
import gc
import re
import shutil

assignment=read(BASE/'background_63_assignment.json')
targets={q['candidate_png_sha256']:q['question_id'] for q in assignment['questions']}
ids=('Solid206','Solid207')
api_name=re.compile(r'(request|binding|started|response|summary|error|incomplete|abort|process_launch|run_\d+|quick.?test)',re.I)
matches=[];malformed=[];counts={'json_files':0,'api_artifacts':0,'embedded_images':0,'png_files':0}
ledger=HERE/'global_scan_files.jsonl'
def strings(v, path=''):
    if isinstance(v,str): yield path,v
    elif isinstance(v,dict):
        for k,x in v.items(): yield from strings(x,path+'/'+str(k))
    elif isinstance(v,list):
        for i,x in enumerate(v): yield from strings(x,path+'/'+str(i))
with ledger.open('x',encoding='utf-8') as log:
    for parent,dirs,files in os.walk(BASE):
        dirs[:]=[d for d in dirs if Path(parent,d).resolve()!=HERE]
        for name in files:
            p=Path(parent,name)
            if p.suffix.lower() not in ('.json','.jsonl','.png','.bin','.txt','.log'): continue
            rec={'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
            if p.suffix.lower()=='.png':
                counts['png_files']+=1
                if rec['sha256'] in targets:
                    rec['exact_png']=targets[rec['sha256']]; matches.append(dict(rec,kind='png_file'))
            else:
                raw=p.read_bytes()
                text=raw.decode('utf-8-sig',errors='replace')
                api=bool(api_name.search(name)) or '/tests/' in p.as_posix()
                if api: counts['api_artifacts']+=1
                related=any(q in text for q in ids) or any(q in str(p) for q in ids)
                hash_matches=[h for h in targets if h in text]
                if p.suffix.lower() in ('.json','.jsonl'):
                    counts['json_files']+=1
                    try:
                        values=(json.loads(s) for s in text.splitlines() if s.strip()) if p.suffix=='.jsonl' else iter([json.loads(text)])
                        embedded=[]
                        for value in values:
                            for key,s in strings(value):
                                if s.startswith('data:image/') and ';base64,' in s:
                                    b=base64.b64decode(s.split(';base64,',1)[1],validate=True)
                                    h=hashlib.sha256(b).hexdigest();counts['embedded_images']+=1
                                    embedded.append({'key':key,'sha256':h,'bytes':len(b)})
                                    if h in targets: matches.append(dict(rec,kind='embedded_request_image',question_id=targets[h],json_key=key,api_artifact=api))
                                    del b
                            del value
                        if embedded: rec['embedded_images']=embedded
                    except (ValueError,UnicodeError) as e:
                        item=dict(rec,error=str(e),api_artifact=api,related_question=related,exact_hash_mentions=hash_matches)
                        malformed.append(item)
                        dest=HERE/'malformed_evidence'/rec['sha256']/name
                        dest.parent.mkdir(parents=True,exist_ok=True)
                        shutil.copyfile(p,dest)
                        rec['malformed']=True
                if api and (related or hash_matches):
                    rec.update(related_question=related,exact_hash_mentions=hash_matches)
                    if hash_matches: matches.append(dict(rec,kind='api_hash_reference'))
                del raw,text
            log.write(json.dumps(rec,ensure_ascii=False)+'\n')
        gc.collect()
blocking=[m for m in matches if m['kind']=='embedded_request_image' or m['kind']=='api_hash_reference']
unknown=[m for m in malformed if m['related_question'] or m['exact_hash_mentions'] or (m['api_artifact'] and m['bytes'] == 0)]
write(HERE/'global_prior_invocation_scan.json',dict(checked_at=now(),scope=str(BASE),counts=counts,matches=matches,malformed_records=malformed,blocking_exact_or_unknown=blocking+unknown,zero_visible_exact_prior_invocations=not blocking and not unknown,limitations=['On-disk whole-task evidence only; no claim about deleted, unseen or provider-side evidence.','All task directories included except own newly created output directory.'],ledger=str(ledger),ledger_sha256=sha(ledger)))
print(json.dumps(dict(counts=counts,matches=matches,malformed=len(malformed),blockers=len(blocking+unknown)),ensure_ascii=False),flush=True)
