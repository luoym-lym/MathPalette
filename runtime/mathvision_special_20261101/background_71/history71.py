from env71 import *
import base64
import gc

audit=[]
images={}
for q, files in read(OWN/'old_history_manifest.json').items():
    finals=[]
    designs=[]
    records=[]
    for rel in files:
        p=PROJECT/rel
        data=p.read_bytes()
        item={'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'full_byte_read':True}
        if p.suffix.lower() in ('.png','.jpg'):
            images.setdefault(item['sha256'],{'path':str(p),'question_id':q,'sha256':item['sha256']})
        if p.suffix=='.json':
            try: value=json.loads(data.decode('utf-8-sig'))
            except (UnicodeDecodeError,json.JSONDecodeError) as exc: item['parse_error']=str(exc)
            else:
                if p.name.endswith('_response.json'):
                    finals.append({'path':rel,'sha256':item['sha256'],'choices':value.get('choices',[]),'usage':value.get('usage')})
                elif p.name=='request.json':
                    user=value.get('messages',[])[-1].get('content',[])
                    text=[x.get('text') for x in user if x.get('type')=='text']
                    rec=next(json.loads(l) for l in (PROJECT/'SolidGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if json.loads(l)['id']==q)
                    item['exact_formal_question_only']=text==[rec['question']]
                    item['model']=value.get('model'); item['thinking']=value.get('thinking')
                    item['embedded_PNG_sha256']=[]
                    for x in user:
                        if x.get('type')=='image_url':
                            raw=base64.b64decode(x['image_url']['url'].split(',',1)[1],validate=True)
                            item['embedded_PNG_sha256'].append(hashlib.sha256(raw).hexdigest())
                            del raw
                    del user,text,rec
                elif p.name=='binding.json':
                    checks={}
                    for field, hf in [('image_path','image_sha256'),('design_path','design_sha256')]:
                        if field in value:
                            src=Path(value[field]); checks[field]={'exists':src.is_file(),'hash_matches':src.is_file() and sha(src)==value.get(hf)}
                    for name,hf in [('request.json','request_body_sha256'),('design_snapshot.json','design_sha256')]:
                        src=p.parent/name
                        if src.is_file(): checks[name]={'hash_matches':sha(src)==value.get(hf)}
                    item['binding_checks']=checks
                    item['preset']=value.get('expected_wrong_answer')
                elif (p.name in ('design.json','plugin.json','design_difference_audit.json') or any(x in p.name for x in ('review','proof','prescreen'))) and p.stat().st_size<200000:
                    designs.append({'path':rel,'sha256':item['sha256'],'content':value})
                elif p.name.startswith('run_') and not p.name.endswith('_started.json'):
                    records.append({'path':rel,'content':value})
                del value
        audit.append(item)
        del data
        gc.collect()
    save(f'{q}/old_full_raw_responses.json', finals)
    save(f'{q}/old_designs_plugins_reviews.json',designs)
    save(f'{q}/old_run_records.json',records)
    path=OWN/q/'old_full_finals.txt'
    with path.open('w',encoding='utf-8') as out:
        for r in finals:
            out.write('\nFILE '+r['path']+'\n')
            for c in r['choices']:
                out.write('FINISH '+str(c.get('finish_reason'))+'\n'+str(c.get('message',{}).get('content'))+'\n')
    print(q,len(files),'files;',len(finals),'raw responses;',len(designs),'design/review artifacts',flush=True)
    del finals,designs,records
    gc.collect()
save('old_evidence_full_byte_read.json',audit)
save('old_images.json',list(images.values()))

# Complete cited reports and full delivered manifests, one document at a time.
reports=[]
for folder in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding','Plane242_r24_disconnected_gray_arc_assembly','Plane263_v01','Plane192_v03','Solid220_false_face_pair']:
    p=BASE/'independent_review'/folder/'independent_review.json'
    if not p.is_file(): continue
    value=read(p)
    target=OWN/'cited_reports'/folder/'independent_review.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(p.read_bytes())
    reports.append({'path':str(p),'sha256':sha(p),'full_snapshot':str(target),'decision':value.get('decision')})
    del value
    gc.collect()
save('cited_reports.json',reports)
refs=[]
for p in sorted(BASE.glob('batch_*/manifest.json')):
    value=read(p)
    target=OWN/'delivered_references'/p.parent.name/'manifest.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(p.read_bytes())
    refs.append({'path':str(p),'sha256':sha(p),'snapshot':str(target)})
    del value
    gc.collect()
save('delivered_references.json',refs)
print('Cited reports',len(reports),'delivered manifests',len(refs),flush=True)
