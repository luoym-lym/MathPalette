from bootstrap import *
import base64
import gc
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone

QID = 'Solid234'
VARIANT = 'r57_maximum_generator_to_cut_trace'
SOURCE = BASE / 'background_57' / QID / VARIANT
TARGET_SHA = 'dee9beb6b5301c5eeae99d778451259b1a0feb9b75aa3338c26297f639afc821'

def now(): return datetime.now(timezone.utc).isoformat()
def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1048576), b''): h.update(b)
    return h.hexdigest()
def read(path):
    with Path(path).open('r', encoding='utf-8-sig') as f: return json.load(f)
def write(path, value):
    p = HERE / path
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False); f.write('\n')
def rows(path):
    if Path(path).is_file():
        with Path(path).open('r', encoding='utf-8-sig') as f:
            for line in f:
                if line.strip(): yield json.loads(line)

def eligibility():
    from dataset_tools.catalog import content, digest
    branch = PROJECT / 'SolidGeometry'
    r = next(r for r in rows(branch/'dataset.jsonl') if r['id'] == QID)
    a = read(PROJECT/'provenance/approvals.json')['approvals'].get(QID, {})
    payload = content(PROJECT, 'SolidGeometry', r)
    root = next(r for r in rows(PROJECT/'question_bank.jsonl') if r['id'] == QID)
    sp = branch/'special_variant'/QID
    accepted = [r for r in rows(branch/'special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))==QID]
    collected = [r for r in rows(branch/'special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))==QID]
    special_files = [str(p) for p in sp.rglob('*') if p.is_file()] if sp.exists() else []
    valid = a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and digest(payload)==a.get('content_sha256')
    return dict(checked_at=now(), record=r, approval=a, current_content_sha256=digest(payload),
        original_approval_current=bool(valid), frozen_content=payload, accepted=accepted, collected=collected,
        special_files=special_files, root_special_plugins=root.get('special_plugins'),
        source_hashes={p:sha(branch/p) for p in payload['files']},
        eligible=r['source_dataset']=='MathVision' and bool(valid) and not accepted and not collected and not special_files and not root.get('special_plugins'))

def initial():
    e = eligibility(); write('eligibility_initial.json', e)
    assert e['eligible'], 'Current original approval/source/Special eligibility failed'
    assignment = read(BASE/'background_74_assignment.json')['questions'][0]
    hashes = {n:sha(SOURCE/n) for n in assignment['frozen_source_files_sha256']}
    assert hashes == assignment['frozen_source_files_sha256'], 'Frozen source changed'
    write('source_input_hashes_initial.json', hashes)
    paths = [BASE/'continuation_brief.txt',BASE/'exploration_report.json',BASE/'remaining_questions.jsonl']
    paths += list(BASE.glob('*master*'))
    manifest=[]
    for p in paths:
        if not p.is_file(): continue
        data=p.read_bytes(); target=HERE/'parent_metadata_snapshots'/p.name
        target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(data)
        manifest.append(dict(path=str(p),snapshot=str(target),sha256=hashlib.sha256(data).hexdigest(),size=len(data)))
        del data
    write('parent_metadata_initial.json', manifest)
    receipts=[]
    refs = [PROJECT/'AGENTS.md', PROJECT/'MATHPALETTE_PROTOCOL.md', PROJECT/'SolidGeometry/REDRAW_PROTOCOL.md',
        PROJECT/'SolidGeometry/dataset_generator/protocol.json', PROJECT/'SolidGeometry/workbench/README.md',
        PROJECT/'SolidGeometry/workbench/agent_prompt.md', PROJECT/'SolidGeometry/workbench/plugin.schema.json',
        BASE/'background_74_brief.txt',BASE/'background_74_assignment.json',BASE/'background_64_brief.txt',BASE/'background_64_assignment.json',
        BASE/'annotation_semantics_lessons_20261102.json', BASE/'annotation_semantics_lesson_plane242_r24_20261102.json']
    refs += list((BASE/'background_57').glob('*.json'))
    refs += list((BASE/'background_57'/QID).glob('*.*')) + list(SOURCE.glob('*.*'))
    refs += [BASE/'independent_review/Plane295_inner_ear_shoulder_correspondence/independent_review.json',
             BASE/'independent_review/Plane342_quarterturn_wedge_edge_binding/independent_review.json']
    for p in refs:
        if not p.is_file():
            receipts.append(dict(path=str(p),missing=True));continue
        h=sha(p); parsed=None
        if p.suffix.lower() in ('.json','.txt','.md','.py','.log'):
            text=p.read_text(encoding='utf-8-sig')
            if p.suffix=='.json': parsed=json.loads(text)
            receipts.append(dict(path=str(p),sha256=h,size=p.stat().st_size,complete_utf8_read=True,top_keys=list(parsed) if isinstance(parsed,dict) else None))
            del text, parsed
        else: receipts.append(dict(path=str(p),sha256=h,size=p.stat().st_size))
    write('full_read_receipts_initial.json', receipts)
    print(json.dumps(dict(eligible=e['eligible'],content_sha256=e['current_content_sha256'],frozen_hashes_equal=True,receipts=len(receipts))))

def strings(o):
    if isinstance(o,str): yield o
    elif isinstance(o,dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o,list):
        for v in o: yield from strings(v)

def scan():
    started=now(); matches=[]; errors=[]; embedded=[]; inventory_count=0; total_bytes=0; json_count=0; archive_count=0
    needles = {'png_sha':TARGET_SHA.encode(),'qid':QID.encode(),'variant':VARIANT.encode(),
               'source_key':b'test:2693'}
    candidate_b64=base64.b64encode((SOURCE/'candidate.png').read_bytes())
    needles['exact_b64']=candidate_b64
    def inspect_stream(label, stream, size):
        nonlocal inventory_count,total_bytes,json_count
        inventory_count+=1; total_bytes+=size
        h=hashlib.sha256(); found=set(); tail=b''
        while True:
            b=stream.read(1048576)
            if not b: break
            h.update(b); both=tail+b
            for key,n in needles.items():
                if n in both: found.add(key)
            tail=both[-(len(candidate_b64)+128):]
        digest=h.hexdigest()
        if digest==TARGET_SHA: found.add('exact_file_bytes')
        if found: matches.append(dict(path=label,sha256=digest,size=size,match=sorted(found)))
        return found,digest
    listing=[]
    for directory, dirs, files in os.walk(BASE):
        dirs[:]=sorted(d for d in dirs if (Path(directory)/d).resolve()!=HERE)
        for name in sorted(files): listing.append(Path(directory)/name)
    inv=HERE/'global_file_inventory.jsonl'
    with inv.open('x',encoding='utf-8',newline='\n') as out:
        for i,p in enumerate(listing):
            try:
                size=p.stat().st_size
                with p.open('rb') as stream: found,digest=inspect_stream(str(p),stream,size)
                out.write(json.dumps(dict(path=str(p),size=size,sha256=digest),ensure_ascii=False)+'\n')
                if p.suffix.lower() in ('.json','.jsonl') or 'request' in p.name.lower():
                    # Parse one file at a time; malformed bytes are never repaired.
                    try:
                        if p.suffix.lower()=='.jsonl': objects=rows(p)
                        else: objects=iter([read(p)])
                        for obj in objects:
                            json_count+=1
                            for s in strings(obj):
                                if 'data:image/' not in s or ';base64,' not in s: continue
                                for match in re.finditer(r'data:image/[^;\s]+;base64,([A-Za-z0-9+/=\r\n]+)',s):
                                    raw=base64.b64decode(match.group(1),validate=False)
                                    ih=hashlib.sha256(raw).hexdigest()
                                    embedded.append(dict(path=str(p),image_sha256=ih,exact=ih==TARGET_SHA,size=len(raw)))
                                    del raw
                            del obj
                        del objects
                    except (json.JSONDecodeError,UnicodeError,ValueError) as ex:
                        errors.append(dict(path=str(p),sha256=digest,matching=sorted(found),error_type=type(ex).__name__,error=str(ex)[:400],preserved=True))
                        # Raw matching survives malformed JSON and must block if transport association is unknown.
                if p.suffix.lower()=='.zip':
                    archive_count+=1
                    with zipfile.ZipFile(p) as z:
                        for info in z.infolist():
                            if info.is_dir(): continue
                            with z.open(info) as f: inspect_stream(str(p)+'!'+info.filename,f,info.file_size)
                if i%2000==0: print('scanned',i,'files',flush=True)
            except (MemoryError,ImportError): raise
            except Exception as ex:
                errors.append(dict(path=str(p),matching=['unknown'],error_type=type(ex).__name__,error=str(ex)[:400]))
            gc.collect() if i%500==0 else None
    del candidate_b64
    report=dict(started_at=started,finished_at=now(),root=str(BASE),excluded_only=str(HERE),file_and_archive_member_count=inventory_count,
        total_bytes=total_bytes,parsed_json_records=json_count,archives=archive_count,method='All files streamed SHA256 plus exact SHA/variant/QID/source-key/base64 search; each JSON decoded singly, all embedded image data decoded and hashed; ZIP members streamed; malformed originals preserved.',
        matches=matches,embedded_images=embedded,errors=errors,
        limits=['Only currently available on-disk task evidence; no claim about deleted/unseen provider records.','Concurrent other-worker files can appear after inventory; a fresh exact invocation scan is required immediately before calls.'],
        classification='PENDING manual matching invocation and related duplicate review; scan alone does not authorize copying or API')
    write('global_prior_invocation_scan.json',report)
    print(json.dumps(dict(files=inventory_count,matches=len(matches),embedded=len(embedded),exact_embedded=sum(x['exact'] for x in embedded),errors=len(errors))))

if __name__=='__main__':
    if sys.argv[1]=='initial': initial()
    elif sys.argv[1]=='scan': scan()
