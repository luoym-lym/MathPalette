from common68 import *
import base64
import re
import zipfile
import shutil

def strings(obj):
    if isinstance(obj,str): yield obj
    elif isinstance(obj,list):
        for v in obj: yield from strings(v)
    elif isinstance(obj,dict):
        for v in obj.values(): yield from strings(v)

def main():
    a=read(BASE/'background_68_assignment.json')
    target={q['question_id']:q for q in a['questions']}
    hs={q:x['frozen_source_files_sha256']['candidate.png'] for q,x in target.items()}
    encoded={q:base64.b64encode((Path(x['source_directory'])/'candidate.png').read_bytes()).decode() for q,x in target.items()}
    supplement=[]; archive_text_count=0; archive_png_decodes=0
    def examine(text):
        nonlocal archive_png_decodes
        matched={q for q,h in hs.items() if h in text or target[q]['variant_id'] in text or encoded[q] in text}
        for enc in re.findall(r'data:image/png;base64,([A-Za-z0-9+/=\r\n]+)',text.replace('\\/','/')):
            blob=base64.b64decode(enc);h=hashlib.sha256(blob).hexdigest(); del blob
            archive_png_decodes+=1
            matched.update(q for q,w in hs.items() if h==w)
        return sorted(matched)
    for p in BASE.glob('*.zip'):
        with zipfile.ZipFile(p) as z:
            for item in z.infolist():
                if item.is_dir() or not item.filename.lower().endswith(('.json','.jsonl','.txt','.log','.bin')): continue
                archive_text_count+=1
                raw=z.read(item)
                text=raw.decode('utf-16' if raw[:2] in (b'\xff\xfe',b'\xfe\xff') else 'utf-8-sig',errors='replace')
                matches=examine(text)
                if matches: supplement.append(dict(path=str(p),member=item.filename,sha256=hashlib.sha256(raw).hexdigest(),matched_question_ids=matches))
                del raw,text
    scan=read(HERE/'whole_task_zero_call_scan.json')
    malformed=[]
    for row in scan['malformed_json']:
        p=Path(row['path']); raw=p.read_bytes()
        text=raw.decode('utf-16' if raw[:2] in (b'\xff\xfe',b'\xfe\xff') else 'utf-8-sig',errors='replace')
        matches=examine(text)
        parsed=False; note='historical invalid JSON; bytes preserved, raw hash/base64/variant scan negative' if not matches else 'MATCHING UNKNOWN; HOLD'
        try:
            obj=json.loads(text); parsed=True
            for s in strings(obj): matches=sorted(set(matches)|set(examine(s)))
            del obj
            note='valid JSON with UTF-16 BOM; decoded and recursively checked'
        except json.JSONDecodeError:
            if p.suffix=='.snapshot' and not text.lstrip().startswith(('{','[')):
                note='snapshot of non-JSON text/protocol; decoded raw checked'
        d=HERE/'malformed_old_snapshots'/row['sha256']
        if not d.exists(): shutil.copyfile(p,d)
        malformed.append(dict(path=str(p),sha256=sha(p),snapshot=str(d),encoding=('utf-16' if raw[:2] in (b'\xff\xfe',b'\xfe\xff') else 'utf-8-sig'),decoded_json_valid=parsed,matched_question_ids=matches,classification=note))
        del raw,text
    # Preserve a complete per-file audit trail of the scoped old history, including
    # original source60 inputs. No combined image/base64 context is retained.
    history=[]; raws=[]
    for parent,dirs,files in os.walk(BASE):
        directory=Path(parent)
        if directory==HERE: dirs[:]=[];continue
        if not any(q in directory.parts for q in IDS):continue
        for name in sorted(files):
            p=directory/name
            row=dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size)
            if p.suffix.lower()=='.json':
                try:
                    obj=read(p)
                    if name.endswith('_response.json'):
                        assert isinstance(obj,dict)
                        row['finish_reasons']=[x.get('finish_reason') for x in obj.get('choices',[])]
                        row['manual_read_status']='Index only; see subsequent human/agent manual history review'
                        raws.append(dict(**row,full_finals=[x.get('message',{}).get('content') for x in obj.get('choices',[])]))
                    if name in ('design.json','plugin.json','manual_final_review.json','primary_visual_review.json','primary_outcome_review.json','prescreen_rejection.json'):
                        dest=HERE/'old_history_snapshots'/str(p.relative_to(BASE))
                        dest.parent.mkdir(parents=True,exist_ok=True)
                        if not dest.exists(): shutil.copyfile(p,dest)
                    del obj
                except (json.JSONDecodeError,UnicodeError) as err: row['old_parse_error']=str(err)
            history.append(row)
    write(HERE/'archive_and_malformed_supplement.json',dict(checked_at=now(),archive_text_members=archive_text_count,decoded_embedded_images=archive_png_decodes,archive_matches=supplement,malformed_records=malformed,
        all_matching_unknowns_absent=not supplement and not any(r['matched_question_ids'] for r in malformed)))
    write(HERE/'scoped_old_history_hashes.json',history)
    write(HERE/'scoped_old_full_finals_read.json',raws)
    print(json.dumps(dict(archive_text_members=archive_text_count,embedded_images=archive_png_decodes,archive_matches=len(supplement),malformed_records=len(malformed),malformed_matches=sum(bool(r['matched_question_ids']) for r in malformed),scoped_old_raw_responses=len(raws)),ensure_ascii=False),flush=True)
    assert not supplement and not any(r['matched_question_ids'] for r in malformed)
if __name__=='__main__':
    (HERE/'malformed_old_snapshots').mkdir(exist_ok=True)
    main()
