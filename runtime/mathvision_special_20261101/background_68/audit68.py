from common68 import *
import base64
import re
import shutil
import zipfile

assignment = read(BASE/'background_68_assignment.json')
targets = {q['question_id']: q for q in assignment['questions']}

def initial():
    snapshot_results = []
    for row in read(HERE/'initial_snapshot_manifest.json'):
        assert sha(row['snapshot']) == row['sha256']
        snapshot_results.append(dict(source=row['source'], snapshot=row['snapshot'], sha256=row['sha256'], verified=True))
    source_assignment = read(BASE/'background_60_assignment.json')
    original_manifest = read(BASE/'background_60/initial_snapshot_manifest.json')
    metadata = []
    mutable = {'continuation_brief.txt', 'exploration_report.json', 'remaining_questions.jsonl', 'refinement_dispatch_20261102.json'}
    for row in original_manifest:
        p = Path(row['source']); old = Path(row['snapshot'])
        assert sha(old) == row['sha256']
        new = sha(p)
        exact = new == row['sha256']
        prefix = False
        if not exact:
            with old.open('rb') as a, p.open('rb') as b:
                prefix = True
                for block in iter(lambda:a.read(1024*1024), b''):
                    if b.read(len(block)) != block:
                        prefix = False; break
        metadata.append(dict(source=str(p), original_snapshot=str(old), original_sha256=row['sha256'], current_sha256=new,
            exact=exact, exact_old_prefix=prefix, classification=('immutable_exact' if exact else 'mutable_parent_exact_prefix_append' if p.name in mutable and prefix else 'mutable_parent_update' if p.name in mutable else 'IMMUTABLE_MISMATCH')))
        assert exact or p.name in mutable
    for qid, q in targets.items():
        d = HERE/qid; d.mkdir(exist_ok=True)
        oldq = next(x for x in source_assignment['questions'] if x['question_id']==qid)
        assert oldq == q['source_assignment_question']
        e = eligibility(qid); write(d/'eligibility_initial.json', e)
        checks = []
        for name, expected in q['frozen_source_files_sha256'].items():
            p = Path(q['source_directory'])/name
            checks.append(dict(path=str(p), expected=expected, actual=sha(p), equal=sha(p)==expected))
        for role, row in oldq['source_inputs'].items():
            checks.append(dict(role=role, path=row['path'], expected=row['sha256'], actual=sha(row['path']), equal=sha(row['path'])==row['sha256']))
        assert e['eligible'] and e['record'] == q['formal_record'] and all(x['equal'] for x in checks)
        frozen={}
        for rel in e['frozen_content']['files']:
            p=PROJECT/BRANCH/rel
            frozen[str(p)] = sha(p)
        for p in [PROJECT/'AGENTS.md', PROJECT/'MATHPALETTE_PROTOCOL.md', PROJECT/BRANCH/'REDRAW_PROTOCOL.md', BASE/'runtime_isolation.py', BASE/'harness/quicktest3_isolated.py', PROJECT/'dataset_tools/catalog.py', PROJECT/'dataset_tools/mathvision_workbench.py'] + list((PROJECT/BRANCH/'workbench').glob('*.py')) + [PROJECT/BRANCH/'workbench/plugin.schema.json', PROJECT/BRANCH/'workbench/config.json']:
            frozen[str(p)] = sha(p)
        write(d/'source_binding_audit.json', dict(checked_at=now(), source60_question_equals_full_read68_nested_question=True, checks=checks, frozen_dependencies=frozen))
        print(qid, 'approval/source/frozen inputs verified', flush=True)
    write(HERE/'initial_snapshot_verification.json', snapshot_results)
    write(HERE/'parent_metadata_classification.json', metadata)

def scan():
    """Whole task, including malformed JSON, embedded images, archives and all units.

    Per-file JSON and image contexts are released immediately. The raw search is
    streaming, including base64 needles, so invalid JSON never drops evidence.
    """
    hashes = {qid:q['frozen_source_files_sha256']['candidate.png'] for qid,q in targets.items()}
    image_b64 = {}
    needles = {}
    for qid,q in targets.items():
        image_b64[qid] = base64.b64encode((Path(q['source_directory'])/'candidate.png').read_bytes())
        needles[qid] = [hashes[qid].encode(), q['variant_id'].encode(), image_b64[qid]]
    overlap = max(len(n) for ns in needles.values() for n in ns)+128
    manifest = HERE/'whole_task_files_initial.jsonl'
    matches=[]; malformed=[]; invocations=[]; decoded_count=0; count=0; png_count=0; archive_count=0
    def raw_matches(p):
        result={}
        with p.open('rb') as f:
            carry=b''
            for block in iter(lambda:f.read(1024*1024), b''):
                combined=carry+block
                for qid,ns in needles.items():
                    found=[label for label,n in zip(('png_sha','variant_id','exact_embedded_base64'),ns) if n in combined]
                    if found: result[qid]=sorted(set(result.get(qid,[])+found))
                carry=combined[-overlap:]
        return result
    def walk_strings(obj):
        if isinstance(obj,str): yield obj
        elif isinstance(obj,list):
            for value in obj: yield from walk_strings(value)
        elif isinstance(obj,dict):
            for value in obj.values(): yield from walk_strings(value)
    def decoded_matches(obj):
        nonlocal decoded_count
        result=[]
        for string in walk_strings(obj):
            if 'data:image/png;base64,' not in string: continue
            for encoded in re.findall(r'data:image/png;base64,([A-Za-z0-9+/=\r\n]+)', string):
                try:
                    blob=base64.b64decode(encoded, validate=False); h=hashlib.sha256(blob).hexdigest(); decoded_count+=1
                    result.append(dict(decoded_sha256=h, matched_question_ids=[q for q,v in hashes.items() if v==h]))
                    del blob
                except (ValueError,TypeError) as err:
                    result.append(dict(error=type(err).__name__))
        return result
    with manifest.open('x',encoding='utf-8',newline='\n') as out:
        for parent, dirs, files in os.walk(BASE):
            pdir=Path(parent)
            if pdir==HERE:
                dirs[:]=[]; continue
            dirs.sort()
            for name in sorted(files):
                p=pdir/name; count+=1
                h=sha(p); size=p.stat().st_size
                row=dict(path=str(p),sha256=h,bytes=size)
                if p.suffix.lower()=='.png':
                    png_count+=1
                    qs=[q for q,v in hashes.items() if h==v]
                    if qs: matches.append(dict(**row,matched_question_ids=qs,kind='exact_png'))
                elif p.suffix.lower()=='.zip':
                    archive_count+=1
                    with zipfile.ZipFile(p) as z:
                        for item in z.infolist():
                            if item.is_dir(): continue
                            with z.open(item) as f:
                                ah=hashlib.sha256()
                                for block in iter(lambda:f.read(1024*1024),b''): ah.update(block)
                            qs=[q for q,v in hashes.items() if ah.hexdigest()==v]
                            if qs: matches.append(dict(**row,archive_member=item.filename,matched_question_ids=qs,kind='archive_exact_png'))
                else:
                    hits=raw_matches(p)
                    dec=[]; valid=None; key_fields={}
                    if p.suffix.lower() in ('.json','.jsonl','.snapshot'):
                        try:
                            if p.suffix.lower()=='.jsonl' or p.name.startswith('remaining_questions.jsonl.'):
                                with p.open(encoding='utf-8-sig') as f:
                                    for line in f:
                                        if line.strip():
                                            obj=json.loads(line); dec.extend(decoded_matches(obj)); del obj
                            else:
                                obj=read(p); dec=decoded_matches(obj)
                                if isinstance(obj,dict):
                                    key_fields={k:obj[k] for k in ('question_id','image_path','image_sha256','design_sha256','request_body_sha256','status','error','error_code','two_completed','requested_runs') if k in obj}
                                del obj
                            valid=True
                        except (json.JSONDecodeError,UnicodeError) as err:
                            valid=False
                            malformed.append(dict(**row,error=str(err),raw_matches=hits))
                    dec_hits={qid for d in dec for qid in d.get('matched_question_ids',[])}
                    qs=sorted(set(hits)|dec_hits)
                    if qs: matches.append(dict(**row,matched_question_ids=qs,kind='raw_or_json_reference',raw_matches=hits,decoded_images=dec,json_valid=valid,key_fields=key_fields))
                    is_call = bool(re.search(r'(?:binding|request|summary|run_\d+.*|.*response.*|.*started.*|.*incomplete.*|.*abort.*|.*error.*)\.(?:json|bin|log|txt)$',name,re.I))
                    if is_call:
                        invocations.append(dict(**row,matched_question_ids=qs,key_fields=key_fields,json_valid=valid,decoded_images=dec,
                            siblings=[x.name for x in p.parent.iterdir() if x.is_file() and re.search(r'(run_|binding|request|summary|response|error|abort|started|incomplete)',x.name,re.I)]))
                out.write(json.dumps(row,ensure_ascii=False)+'\n')
                if count%5000==0: print('scanned files',count,flush=True)
    # Every candidate reference in a call-shaped file requires human classification.
    matching_calls=[r for r in invocations if r['matched_question_ids']]
    write(HERE/'whole_task_zero_call_scan.json',dict(checked_at=now(),scope=str(BASE),exclude_only_own_new_output=True,files=count,png_files=png_count,archive_files=archive_count,decoded_embedded_pngs=decoded_count,
        candidate_png_sha256=hashes,matches=matches,matching_call_evidence=matching_calls,malformed_json=malformed,
        conclusion='PENDING manual classification of every matching call-shaped record; missing summaries never imply zero calls',manifest=str(manifest)))
    write(HERE/'whole_task_invocation_inventory.json', invocations)
    print(json.dumps(dict(files=count,pngs=png_count,decoded_embedded_pngs=decoded_count,matching_call_evidence=len(matching_calls),malformed_json=len(malformed)),ensure_ascii=False),flush=True)

if __name__=='__main__':
    {'initial':initial,'scan':scan}[sys.argv[1]]()
