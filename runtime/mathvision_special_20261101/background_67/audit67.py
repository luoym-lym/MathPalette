from env67 import *
import base64
import gc
import re
import shutil

A=read(OWN/'snapshots/background_67_assignment.json')
items={v['question_id']:v for v in A['questions']}
targets={v['frozen_source_files_sha256']['candidate.png']:q for q,v in items.items()}
aliases={q:{v['variant_id'],v['source_directory'],v['source_directory'].replace('\\','/'),v['frozen_source_files_sha256']['design.json'],v['frozen_source_files_sha256']['candidate.png']} for q,v in items.items()}
protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/dataset_generator/protocol.json','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json']
readlog=[]
for rel in protocols:
    p=PROJECT/rel; txt=p.read_text(encoding='utf-8-sig')
    readlog.append({'path':str(p),'sha256':sha(p),'characters':len(txt),'full_utf8_read':True})
save('protocol_read_log.json',readlog)
save('isolation.json',{'at':now(),'pid':os.getpid(),'ownroot':str(OWN),'guard_before_project_imports':True,'environment':{n:os.environ[n] for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')}})
old=read(BASE/'background_59_assignment.json')
print('ORIGINAL_ASSIGNMENT_KEYS',list(old),flush=True)
original_questions=old.get('questions',[])
comparisons={}
for q,v in items.items():
    prior=next(x for x in original_questions if x['question_id']==q)
    comparisons[q]={'original_assignment_question_equals_full_inherited_question':prior==v['source_assignment_question'],'original_question_keys':list(prior)}
save('original_assignment_full_read.json',{'path':str(BASE/'background_59_assignment.json'),'sha256':sha(BASE/'background_59_assignment.json'),'full_utf8_json_read':True,'scope_restricted_to':list(QIDS),'comparison':comparisons,'non_question_metadata':{k:v for k,v in old.items() if k!='questions'}})
del old,original_questions
hashes={}
for q,v in items.items():
    e=eligibility(q); save(f'{q}/eligibility_initial.json',e)
    assert e['eligible'],e['reasons']
    checks={}
    for name,expected in v['frozen_source_files_sha256'].items():
        p=Path(v['source_directory'])/name
        actual=sha(p); checks[name]={'expected':expected,'actual':actual,'match':actual==expected}; hashes[str(p)]=actual
    assert all(c['match'] for c in checks.values()),q
    save(f'{q}/frozen_source_hash_gate.json',checks)
    for rel,expected in e['content_snapshot']['files'].items():
        p=PROJECT/'SolidGeometry'/rel
        assert sha(p)==expected,(q,rel)
        hashes[str(p)]=expected
    print(q,'CURRENT_ELIGIBLE_APPROVAL_AND_FROZEN_HASHES_PASS',flush=True)
    del e,checks
save('immutable_initial_hashes.json',hashes)

# Read cited reports one at a time; keep complete source reports unchanged.
refs=['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly','Plane263_v01','Plane192_v03','Solid220_false_face_pair']
refout=[]
for rel in ['annotation_semantics_lessons_20261102.json','annotation_semantics_lesson_plane242_r24_20261102.json']:
    value=read(BASE/rel); refout.append({'path':str(BASE/rel),'sha256':sha(BASE/rel),'full_JSON_read':True,'content':value})
for folder in refs:
    p=BASE/'independent_review'/folder/'independent_review.json'
    if not p.exists(): continue
    v=read(p)
    relevant={k:v[k] for k in ('decision','reason','rationale','issues','strict_conclusion','blocking_reason','requirement_disposition','limitations','remaining_issue','targeted_information','action_necessity','marker_necessity') if k in v}
    refout.append({'path':str(p),'sha256':sha(p),'full_JSON_read':True,'assessment_sections':relevant})
    del v
save('cited_independent_objections_read.json',refout)
del refout

# Read scoped full old history, preserving malformed bytes. Never retain payloads across files.
manifest=read(BASE/'background_59/old_history_manifest.json')
hist=[]
for q in QIDS:
    out=OWN/q/'old_full_finals.txt'
    with out.open('x',encoding='utf-8') as f:
        for rel in manifest[q]:
            p=PROJECT/rel
            data=p.read_bytes()
            row={'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'fully_read':True}
            if p.suffix.lower()=='.json':
                try: v=json.loads(data.decode('utf-8-sig'))
                except (UnicodeError,ValueError) as exc:
                    row['parse_error']=str(exc)
                    dst=OWN/'malformed_history'/row['sha256']/p.name; dst.parent.mkdir(parents=True,exist_ok=True); dst.write_bytes(data); row['preserved_bytes']=str(dst)
                else:
                    if p.name.endswith('_response.json') and isinstance(v,dict):
                        f.write('\nFILE '+str(p)+'\n')
                        for c in v.get('choices',[]):
                            f.write('FINISH '+str(c.get('finish_reason'))+'\n'+str(c.get('message',{}).get('content'))+'\n')
                    del v
            hist.append(row); del data; gc.collect()
    print(q,'FULL_OLD_HISTORY',sum(1 for x in hist if q in x['path']),flush=True)
save('scoped_old_full_history_audit.json',hist)
del hist,manifest

# Whole-task scan including legacy workbench runtime. Data is processed one file at a time.
roots=[PROJECT/'runtime',PROJECT/'.runtime']
directory_matches={}
png_matches=[]
malformed=[]
file_count=0
max_bytes=0
unreadable=[]
payload_re=re.compile(rb'data:image/(?:png|jpeg|jpg);base64,([A-Za-z0-9+/=]+)')
text_ext={'.json','.jsonl','.txt','.log','.bin','.py','.md','.yaml','.yml','.csv'}
with (OWN/'whole_task_scan_files.jsonl').open('x',encoding='utf-8') as out:
    for root in roots:
        if not root.exists(): continue
        for directory,dirs,files in os.walk(root):
            dirs[:]=[d for d in dirs if d not in ('__pycache__','.git') and not (Path(directory)/d).resolve().is_relative_to(OWN)]
            for name in files:
                p=Path(directory)/name
                if p.suffix.lower() not in text_ext|{'.png','.jpg','.jpeg'}: continue
                file_count+=1
                try:
                    digest=sha(p); size=p.stat().st_size; max_bytes=max(max_bytes,size)
                    row={'path':str(p),'sha256':digest,'bytes':size}
                    if p.suffix.lower() in ('.png','.jpg','.jpeg'):
                        if digest in targets:
                            row['target_exact_png']=targets[digest]; png_matches.append(row.copy())
                    else:
                        data=p.read_bytes()
                        decoded=[]
                        for m in payload_re.finditer(data):
                            raw=base64.b64decode(m.group(1),validate=True)
                            embedded=hashlib.sha256(raw).hexdigest()
                            if embedded in targets: decoded.append({'question_id':targets[embedded],'embedded_png_sha256':embedded})
                            del raw
                        matches=set(x['question_id'] for x in decoded)
                        for q,needles in aliases.items():
                            if any(s.encode('utf-8') in data for s in needles): matches.add(q)
                        if decoded: row['exact_embedded_matches']=decoded
                        if matches:
                            row['matched_questions']=sorted(matches)
                            entry=directory_matches.setdefault(str(p.parent),{'matches':set(),'files':[]})
                            entry['matches'].update(matches); entry['files'].append(row.copy())
                        if p.suffix.lower()=='.json':
                            try: value=json.loads(data.decode('utf-8-sig'))
                            except (UnicodeError,ValueError) as exc:
                                err={'path':str(p),'sha256':digest,'bytes':size,'error':str(exc),'matched_questions':sorted(matches)}
                                malformed.append(err); row['malformed']=True
                                # Preserve every malformed JSON; old source bytes stay untouched.
                                dst=OWN/'malformed_global'/digest/p.name; dst.parent.mkdir(parents=True,exist_ok=True)
                                if not dst.exists(): dst.write_bytes(data)
                            else:
                                # Detect JSON-escaped slashes in embedded data too.
                                stack=[value]
                                while stack:
                                    obj=stack.pop()
                                    if isinstance(obj,dict): stack.extend(obj.values())
                                    elif isinstance(obj,list): stack.extend(obj)
                                    elif isinstance(obj,str) and obj.startswith('data:image/') and ';base64,' in obj:
                                        raw=base64.b64decode(obj.split(',',1)[1],validate=True); emb=hashlib.sha256(raw).hexdigest(); del raw
                                        if emb in targets:
                                            q=targets[emb]; entry=directory_matches.setdefault(str(p.parent),{'matches':set(),'files':[]}); entry['matches'].add(q)
                                            if not any(x['path']==str(p) for x in entry['files']): entry['files'].append({**row,'decoded_JSON_embedded_match':q})
                                del value,stack
                        del data,decoded
                    out.write(json.dumps(row,ensure_ascii=False)+'\n')
                except (OSError,ValueError) as exc:
                    unreadable.append({'path':str(p),'error':str(exc)})
                if file_count%250==0: print('SCAN',file_count,flush=True)
                gc.collect()
invocations=[]
unknown=[]
for d,entry in directory_matches.items():
    p=Path(d)
    names=[x.name for x in p.iterdir() if x.is_file()]
    evidence=[n for n in names if re.match(r'run_\d',n) or n in ('request.json','binding.json','summary.json') or any(t in n.lower() for t in ('started','response','incomplete','abort'))]
    # Match directories by path identity too, regardless of which local file carries it.
    own_source=any(p==Path(v['source_directory']) for v in items.values())
    if evidence:
        record={'directory':d,'question_ids':sorted(entry['matches']),'evidence_files':evidence,'matching_files':entry['files']}
        if any(re.match(r'run_\d',n) or any(t in n.lower() for t in ('started','response','incomplete','abort')) for n in evidence):
            invocations.append(record)
        elif not own_source:
            unknown.append(record)
report={'at':now(),'scope':list(QIDS),'roots':[str(r) for r in roots],'excluded_only_ownroot_and_pycache_git':True,'file_count':file_count,'maximum_single_input_bytes':max_bytes,'exact_png_matches':png_matches,'matching_directories':[{**v,'directory':k,'matches':sorted(v['matches'])} for k,v in directory_matches.items()],'actual_or_possible_invocations':invocations,'request_only_unknown_evidence':unknown,'malformed_JSON':malformed,'unreadable':unreadable,'scope_zero_prior_calls_proved':not invocations and not unknown and not unreadable and not any(x['matched_questions'] for x in malformed)}
save('whole_task_zero_call_scan.json',report)
print('ZERO_CALL_SCAN',json.dumps({k:report[k] for k in ('file_count','maximum_single_input_bytes','scope_zero_prior_calls_proved')}),'invocations',len(invocations),'unknown',len(unknown),'malformed',len(malformed),'unreadable',len(unreadable),flush=True)
