from worker_env import *
import base64
import gc
ledger=[]
def read_registered(path):
    p=Path(path)
    if not p.is_absolute(): p=PROJECT/p
    value=load(p)
    ledger.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'fully_parsed':True})
    return value

assignment=read_registered(OWN/'assignment.json')
save(OWN/'initial_bytes.json',{'at':now(),'brief':sha(OWN/'brief.txt'),'assignment':sha(OWN/'assignment.json')},True)
save(OWN/'checkpoint.json',{'at':now(),'status':'reading_and_independent_prescreen','assigned':assignment['question_ids'],'calls':0,'questions':{q:{'status':'in_progress'} for q in assignment['question_ids']}})
save(OWN/'second_review_queue.json',[])
save(OWN/'environment.json',environment(),True)
for name,expected in assignment['required_parent_scope_files'].items():
    actual=sha(TASK/name)
    assert actual==expected,(name,actual,expected)
for qid in assignment['question_ids']:
    report=eligibility(qid)
    save(OWN/qid/'eligibility_initial.json',report,True)
    assert report['eligible'],report['checks']
    save(OWN/qid/'formal_record.json',report['record'],True)
    print(qid,'current eligibility PASS',flush=True)

references={}
for qid in load(TASK/'task.json')['references']:
    folder=TASK/'references'/qid
    p=read_registered(folder/'C01.json')
    r=read_registered(folder/'recipes.json')
    ref=read_registered(folder/'reference.json')
    assert sha(folder/'C01.png')==load(TASK/'reference_manifest.json')[qid]['png_sha256']
    assert sha(folder/'C01.json')==load(TASK/'reference_manifest.json')[qid]['plugin_sha256']
    for filename,data in ref['copied_files'].items():
        assert sha(folder/filename)==data['sha256']
    references[qid]={'plugin':p,'recipe':r,'reference':ref}
    print(json.dumps({'reference':qid,'plugin':p,'formal_question':ref['formal_record']['question'],
       'recipe':r,'reference_files':ref['copied_files']},ensure_ascii=False),flush=True)
save(OWN/'reference_read_audit.json',{'at':now(),'all9_native_PNGs_viewed':True,'files':ledger.copy(),'frozen_hashes_match':True},True)

history=load(TASK/'history_index.json')
for qid in assignment['question_ids']:
    item=next(x for x in history['questions'] if x['question_id']==qid)
    save(OWN/qid/'history_index_extract.json',item,True)
    paths=set(item['other_scoped_history_file_references']+item['additional_math_manual_history_references']+item['independent_review_references'])
    for d in item['designs']:
        paths.add(d['design_path']); paths.add(d['plugin_path'])
    excerpts=[]
    for relative in sorted(paths):
        data=read_registered(relative)
        # No base64/context retention. Entire JSON is parsed one at a time.
        if relative.endswith('request.json'):
            payload=base64.b64decode(data['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
            excerpts.append({'path':relative,'payload_keys':list(data),'question':data['messages'][1]['content'][0]['text'],'image_sha256':hashlib.sha256(payload).hexdigest()})
            del payload
        elif relative.endswith(('/context.json','/fresh_context.json')):
            excerpts.append({'path':relative,'keys':list(data),'objects_count':len(data.get('objects',[]))})
        else:
            excerpts.append({'path':relative,'data':data})
        del data
        gc.collect()
    save(OWN/qid/'complete_history_read_extract.json',excerpts,True)
    print(qid,'history files fully parsed',len(paths),'transport groups',len(item['all_saved_transport_groups_for_question']),flush=True)
save(OWN/'read_ledger.json',ledger,True)
