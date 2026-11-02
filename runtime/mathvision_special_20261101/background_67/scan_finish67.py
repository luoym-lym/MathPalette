from env67 import *
import base64
import gc
import re

A=read(OWN/'snapshots/background_67_assignment.json')
items={x['question_id']:x for x in A['questions']}
targets={v['frozen_source_files_sha256']['candidate.png']:q for q,v in items.items()}
aliases={q:[v['variant_id'],v['frozen_source_files_sha256']['candidate.png'],v['frozen_source_files_sha256']['design.json']] for q,v in items.items()}
scanned=set()
for line in (OWN/'whole_task_scan_files.jsonl').open(encoding='utf-8'):
    r=json.loads(line); scanned.add(r['path']); del r
supp=[]
supplement_read_errors=[]
payload=re.compile(rb'data:image/(?:png|jpeg|jpg);base64,([A-Za-z0-9+/=]+)')
for root in (PROJECT/'runtime',PROJECT/'.runtime'):
    if not root.exists(): continue
    for d,dirs,files in os.walk(root):
        dirs[:]=[n for n in dirs if n not in ('__pycache__','.git') and not (Path(d)/n).resolve().is_relative_to(OWN)]
        for n in files:
            p=Path(d)/n
            if str(p) in scanned: continue
            try: row={'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size}
            except OSError as exc:
                supplement_read_errors.append({'path':str(p),'error_type':type(exc).__name__,'error':str(exc)})
                save('supplement_read_errors.json',supplement_read_errors)
                continue
            matches=set()
            if row['sha256'] in targets: matches.add(targets[row['sha256']]); row['exact_png']=True
            # Bound memory while searching all otherwise-unlisted extensions.
            tail=b''
            with p.open('rb') as f:
                for b in iter(lambda:f.read(262144),b''):
                    data=tail+b
                    for q,needles in aliases.items():
                        if any(x.encode() in data for x in needles): matches.add(q)
                    tail=data[-2048:]
                del tail
            if row['bytes']<=8388608:
                data=p.read_bytes()
                embedded=[]
                for m in payload.finditer(data):
                    raw=base64.b64decode(m.group(1),validate=True); h=hashlib.sha256(raw).hexdigest(); del raw
                    if h in targets: matches.add(targets[h]); embedded.append(targets[h])
                if embedded: row['embedded_exact_png_matches']=embedded
                try: value=json.loads(data.decode('utf-8-sig'))
                except (UnicodeError,ValueError): pass
                else:
                    stack=[value]
                    while stack:
                        obj=stack.pop()
                        if isinstance(obj,dict): stack.extend(obj.values())
                        elif isinstance(obj,list): stack.extend(obj)
                        elif isinstance(obj,str) and obj.startswith('data:image/') and ';base64,' in obj:
                            try: raw=base64.b64decode(obj.split(',',1)[1],validate=True)
                            except ValueError:
                                row.setdefault('invalid_data_URL_literals',[]).append(obj)
                            else:
                                h=hashlib.sha256(raw).hexdigest(); del raw
                                if h in targets: matches.add(targets[h]); row['JSON_embedded_exact_png_match']=targets[h]
                    del stack,value
                del data
            else:
                # Large otherwise-unclassified binaries are catalogued explicitly.
                row['large_binary_no_full_JSON_allocation']=True
            if matches: row['matches']=sorted(matches)
            supp.append(row)
            gc.collect()
save('whole_task_supplement_all_extensions.json',{'at':now(),'previous_file_count':len(scanned),'additional_files':supp,'no_extension_filter_in_supplement':True,'matching_additional_files':[x for x in supp if x.get('matches')]})
print('SUPPLEMENT',len(supp),'matches',len([x for x in supp if x.get('matches')]),flush=True)

r=read(OWN/'whole_task_zero_call_scan.json')
direct=[]
diagnostic=[]
for entry in r['matching_directories']:
    for f in entry['files']:
        p=Path(f['path'])
        direct_type=bool(re.search(r'(?:^|__)(?:request|binding|summary)\.json$|(?:^|__)(?:quicktest3_)?run_?\d',p.name))
        # A copied/renamed raw payload or run cannot evade the scan by its filename.
        try: value=read(p)
        except (UnicodeError,ValueError): value=None
        stack=[value]
        while stack:
            value=stack.pop()
            if isinstance(value,dict):
                image_hash=value.get('image_sha256',value.get('png_sha256'))
                if image_hash in targets and any(k in value for k in ('started_at','run_index','run_id','http_status','response_sha256')): direct_type=True
                if 'messages' in value and 'model' in value and (f.get('exact_embedded_matches') or f.get('decoded_JSON_embedded_match')): direct_type=True
                stack.extend(value.values())
            elif isinstance(value,list): stack.extend(value)
        if direct_type:
            direct.append({'directory':str(p.parent),'file':f,'question_ids':entry['matches'],'actual_start_or_response_present':any(re.match(r'run_\d',x.name) for x in p.parent.iterdir() if x.is_file())})
        else: diagnostic.append({'path':str(p),'matched_questions':entry['matches'],'reason':'Not an actual call artifact; direct request/binding/run/summary evidence separately checked.'})
blockers=[x for x in direct]
for m in r['malformed_JSON']:
    if m['matched_questions']: blockers.append({'malformed_matching_evidence':m})
for f in supp:
    if f.get('matches'):
        # Metadata snapshots are exact archived metadata, not API artifacts.
        p=Path(f['path'])
        is_snapshot=p.suffix=='.snapshot' and any(t in p.name for t in ('continuation_brief','exploration_report','remaining_questions','assignment','brief','dispatch'))
        if not is_snapshot: blockers.append({'unknown_matching_supplement':f})
resolved=[]
for failure in r['unreadable']:
    p=Path(failure['path']); data=p.read_bytes(); h=hashlib.sha256(data).hexdigest()
    dst=OWN/'placeholder_report_bytes'/h/p.name; dst.parent.mkdir(parents=True,exist_ok=True)
    if not dst.exists(): dst.write_bytes(data)
    matching=[q for q,needles in aliases.items() if any(x.encode() in data for x in needles)]
    v=json.loads(data.decode('utf-8-sig')); stack=[v]; invalid=[]; exact=[]
    while stack:
        obj=stack.pop()
        if isinstance(obj,dict): stack.extend(obj.values())
        elif isinstance(obj,list): stack.extend(obj)
        elif isinstance(obj,str) and obj.startswith('data:image/') and ';base64,' in obj:
            try: raw=base64.b64decode(obj.split(',',1)[1],validate=True)
            except ValueError: invalid.append(obj)
            else:
                emb=hashlib.sha256(raw).hexdigest(); del raw
                if emb in targets: exact.append(targets[emb])
    diagnostic=bool(invalid) and all(x=='data:image/png;base64,<exact frozen candidate>' for x in invalid) and not matching and not exact
    row={'path':str(p),'sha256':h,'preserved_bytes':str(dst),'full_JSON_read_again':True,'invalid_literals':invalid,'matching_assigned_frozen_identity':matching,'exact_assigned_PNG_payloads':exact,'classification':'unrelated_Plane342_report_explicit_placeholder_not_actual_payload' if diagnostic else 'unresolved_matching_or_unknown_evidence'}
    resolved.append(row)
    if not diagnostic: blockers.append(row)
    del data,v,stack; gc.collect()
save('global_scan_placeholder_diagnostics.json',resolved)
if supplement_read_errors: blockers.append({'unreadable_supplement_files':supplement_read_errors})
report={'at':now(),'whole_task_scan':str(OWN/'whole_task_zero_call_scan.json'),'supplement':str(OWN/'whole_task_supplement_all_extensions.json'),'complete_file_count':len(scanned)+len(supp),'direct_exact_candidate_API_artifacts':direct,'diagnostic_metadata_matches':diagnostic,'blockers':blockers,'all_three_zero_prior_actual_calls_proved':not blockers,'method':'Every task runtime and legacy .runtime file hashed, textual/JSON embedded data decoded in primary scan; all remaining extensions scanned for exact PNG/design hashes and variant identity. Actual request/start/binding/raw/summary linkage distinguished from metadata references. Matching unknowns block reuse. No missing-summary inference.'}
save('zero_call_final_gate.json',report)
print('FINAL_ZERO_GATE',report['all_three_zero_prior_actual_calls_proved'],'direct',len(direct),'blockers',len(blockers),flush=True)
