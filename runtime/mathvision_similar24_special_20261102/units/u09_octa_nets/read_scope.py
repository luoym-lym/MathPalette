from own_bootstrap import *

def history_paths(q):
    out=set()
    def walk(z):
        if isinstance(z, dict):
            for k,v in z.items():
                if isinstance(v,str) and v.startswith('runtime/') and (PROJECT/v.split('#')[0]).is_file():
                    out.add(v.split('#')[0])
                walk(v)
        elif isinstance(z,list):
            for v in z:
                walk(v)
        elif isinstance(z,str) and z.startswith('runtime/') and (PROJECT/z.split('#')[0]).is_file():
            out.add(z.split('#')[0])
    walk(q)
    for d in q['designs']:
        p=PROJECT/d['directory']
        if p.is_dir():
            for f in p.rglob('*'):
                if f.is_file():
                    out.add(f.relative_to(PROJECT).as_posix())
    return sorted(out)

if __name__=='__main__':
    assignment=load(OWN/'assignment.json')
    history=load(TASK/'history_index.json')
    selected=[q for q in history['questions'] if q['question_id'] in assignment['question_ids']]
    save(OWN/'history_selected.json',selected,exclusive=True)
    manifest={}
    for q in selected:
        documents=[]
        for rel in history_paths(q):
            p=PROJECT/rel
            manifest[rel]={'sha256':sha(p),'bytes':p.stat().st_size}
            if p.suffix.lower() in ('.json','.jsonl','.txt','.md','.py','.log'):
                # Full text retained in a private read transcript. Request base64 is decoded and audited separately.
                data=p.read_text(encoding='utf-8-sig')
                if p.name=='request.json':
                    import base64
                    req=json.loads(data)
                    for m in req.get('messages',[]):
                        if isinstance(m.get('content'),list):
                            for part in m['content']:
                                if part.get('type')=='image_url':
                                    raw=base64.b64decode(part['image_url']['url'].split(',',1)[1])
                                    part['image_url']['url']={'image_sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'base64_omitted_from_read_transcript':True}
                                    del raw
                    data=json.dumps(req,ensure_ascii=False,indent=2)
                documents.append({'path':rel,'sha256':manifest[rel]['sha256'],'text':data})
                del data
        save(OWN/'reads'/f"{q['question_id']}_full_history.json",documents,exclusive=True)
        print(json.dumps({'question_id':q['question_id'],'full_documents':len(documents),'history_file_count':len(history_paths(q)),
                          'designs':[{'directory':d['directory'],'preset':d['predeclared_wrong_answer'],'calls':d['unique_started_call_count_from_saved_records']} for d in q['designs']],
                          'independent':q['independent_review_references'],'additional_math':q['additional_math_manual_history_references']},ensure_ascii=False))
    refs={}
    for ref in load(TASK/'task.json')['references']:
        p=TASK/'references'/ref
        refs[ref]={}
        for f in ('C01.json','recipes.json','reference.json'):
            refs[ref][f]=load(p/f)
            manifest[(p/f).relative_to(PROJECT).as_posix()]={'sha256':sha(p/f),'bytes':(p/f).stat().st_size}
        manifest[(p/'C01.png').relative_to(PROJECT).as_posix()]={'sha256':sha(p/'C01.png'),'bytes':(p/'C01.png').stat().st_size,'actually_viewed':True}
    save(OWN/'reads/reference_documents.json',refs,exclusive=True)
    save(OWN/'read_source_manifest.json',manifest,exclusive=True)
