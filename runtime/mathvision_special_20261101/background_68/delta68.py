from common68 import *
import base64
import re

label=sys.argv[1]
baseline={r['path']:r for r in rows(HERE/'whole_task_files_initial.jsonl')}
qs=read(BASE/'background_68_assignment.json')['questions']
hashes={q['question_id']:q['frozen_source_files_sha256']['candidate.png'] for q in qs}
enc={q['question_id']:base64.b64encode((Path(q['source_directory'])/'candidate.png').read_bytes()) for q in qs}
changes=[]; blockers=[]; pngs=[]; checked=0
for parent,dirs,files in os.walk(BASE):
    directory=Path(parent)
    if directory==HERE:dirs[:]=[];continue
    for name in files:
        p=directory/name;checked+=1;h=sha(p);old=baseline.get(str(p))
        if old and old['sha256']==h:continue
        row=dict(path=str(p),old_sha256=old['sha256'] if old else None,current_sha256=h,bytes=p.stat().st_size)
        hits=[]
        if p.suffix.lower()=='.png':
            hits=[q for q,v in hashes.items() if h==v]
            if hits:pngs.append(row)
        else:
            raw=p.read_bytes()
            text=raw.decode('utf-16' if raw[:2] in (b'\xff\xfe',b'\xfe\xff') else 'utf-8-sig',errors='replace')
            hits=[q for q in hashes if hashes[q] in text or enc[q] in raw]
            for encoded in re.findall(r'data:image/png;base64,([A-Za-z0-9+/=\r\n]+)',text.replace('\\/','/')):
                blob=base64.b64decode(encoded);bh=hashlib.sha256(blob).hexdigest();del blob
                hits.extend(q for q,v in hashes.items() if bh==v)
            del raw,text
        row['matched_question_ids']=sorted(set(hits))
        call_name=bool(re.search(r'(binding|request|summary|run_\d+|response|started|incomplete|abort|error)',name,re.I))
        if hits and call_name:blockers.append(row)
        elif hits:row['classification']='Non-call parent progress or another worker inventory/snapshot; diagnostic reference only'
        changes.append(row)
write(HERE/('whole_task_delta_'+label+'.json'),dict(checked_at=now(),checked_files=checked,baseline_manifest_sha256=sha(HERE/'whole_task_files_initial.jsonl'),changed_or_new=changes,matching_call_evidence=blockers,new_exact_candidate_png_copies=pngs,eligible=not blockers and not pngs,exclude_only_ownroot=True))
print(json.dumps(dict(checked_files=checked,new_or_changed=len(changes),matching_call_evidence=len(blockers),new_exact_candidate_pngs=len(pngs)),ensure_ascii=False),flush=True)
assert not blockers and not pngs
