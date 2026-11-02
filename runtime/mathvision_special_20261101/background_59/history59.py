from env59 import *
import base64
import gc

manifest=read(OWN/'old_history_manifest.json')
audit=[]
images={}
for q,files in manifest.items():
    responses=[]
    designs=[]
    records=[]
    for rel in files:
        p=PROJECT/rel
        data=p.read_bytes()
        item={'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'fully_byte_read':True}
        if p.name=='candidate.png': images.setdefault(item['sha256'],{'path':str(p),'question_id':q})
        if p.suffix=='.json':
            try: value=json.loads(data.decode('utf-8-sig'))
            except (UnicodeDecodeError,json.JSONDecodeError) as exc:
                item['parse_error']=str(exc)
            else:
                if p.name.endswith('_response.json'):
                    choices=value.get('choices',[])
                    responses.append({'path':rel,'sha256':item['sha256'],'full_choices':choices,'usage':value.get('usage')})
                elif p.name=='request.json':
                    messages=value.get('messages',[])
                    user=messages[-1]['content'] if messages else []
                    text=[x.get('text') for x in user if x.get('type')=='text']
                    image=[x.get('image_url',{}).get('url','') for x in user if x.get('type')=='image_url']
                    item['request_model']=value.get('model')
                    item['request_thinking']=value.get('thinking')
                    item['request_only_formal_text']=text==[next(json.loads(l)['question'] for l in (PROJECT/'SolidGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if json.loads(l)['id']==q)]
                    item['request_user_types']=[x.get('type') for x in user]
                    item['embedded_PNG_sha256']=[hashlib.sha256(base64.b64decode(s.split(',',1)[1],validate=True)).hexdigest() for s in image]
                    del image,user,messages
                elif p.name=='binding.json':
                    checks={}
                    for field,hashfield in [('image_path','image_sha256'),('design_path','design_sha256')]:
                        if field in value:
                            source=Path(value[field])
                            checks[field]={'path':str(source),'present':source.is_file(),'matches':source.is_file() and sha(source)==value.get(hashfield)}
                    for name,field in [('request.json','request_body_sha256'),('design_snapshot.json','design_sha256')]:
                        source=p.parent/name
                        if source.exists(): checks[name]={'path':str(source),'matches':sha(source)==value.get(field)}
                    item['binding_checks']=checks
                    item['expected_wrong_answer']=value.get('expected_wrong_answer')
                elif p.name=='design.json' or ('review' in p.name or 'prescreen' in p.name or 'proof' in p.name or p.name=='plugin.json') and p.stat().st_size<100000:
                    designs.append({'path':rel,'sha256':item['sha256'],'content':value})
                elif p.name.startswith('run_') and not p.name.endswith('_started.json'):
                    records.append({'path':rel,'content':value})
                del value
        audit.append(item)
        del data
        gc.collect()
    save(f'{q}/old_full_raw_responses.json',responses)
    save(f'{q}/old_designs_plugins_reviews.json',designs)
    save(f'{q}/old_run_records.json',records)
    with (OWN/q/'old_full_finals.txt').open('w',encoding='utf-8') as out:
        for r in responses:
            out.write('\nFILE '+r['path']+'\n')
            for choice in r['full_choices']:
                out.write('FINISH '+str(choice.get('finish_reason'))+'\n')
                out.write(str(choice.get('message',{}).get('content'))+'\n')
    print(q,len(files),'old files',len(responses),'complete raw response artifacts',flush=True)
    del responses,designs,records
    gc.collect()
save('old_evidence_full_byte_read.json',audit)
save('old_native_candidate_images.json',list(images.values()))
