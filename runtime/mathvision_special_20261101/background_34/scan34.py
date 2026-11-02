from tools34 import *

history={qid: {'designs':[], 'question_directories':[], 'checkpoints':[]} for qid in IDS}
for path in SHARED.rglob('design.json'):
    if path.is_relative_to(UNIT): continue
    value=read(path)
    qid=value.get('question_id')
    if qid in history: history[qid]['designs'].append(str(path.relative_to(PROJECT)))
for path in SHARED.rglob('*'):
    if path.is_relative_to(UNIT): continue
    if path.is_dir() and path.name in IDS:
        history[path.name]['question_directories'].append(str(path.relative_to(PROJECT)))
for path in SHARED.glob('background_*/checkpoint.json'):
    if path.is_relative_to(UNIT): continue
    value=read(path)
    serialized=json.dumps(value,ensure_ascii=False)
    for qid in IDS:
        if qid in serialized:
            history[qid]['checkpoints'].append({'path':str(path.relative_to(PROJECT)),'sha256':sha(path)})
write(UNIT/'history_inventory.json',history)
for qid in IDS:
    result=eligibility(qid)
    write(UNIT/qid/'eligibility_start.json',result)
    write(UNIT/qid/'formal_record.json',record(qid))
    write(UNIT/qid/'source_fingerprints_start.json',source_files(qid))
    print(json.dumps({'question_id':qid,'eligibility':result['checks'],'source':record(qid),'history':history[qid]},ensure_ascii=False))
frozen={}
for qid,data in history.items():
    paths=[PROJECT/p for p in data['question_directories']]
    for directory in paths:
        for path in directory.rglob('*'):
            if path.is_file(): frozen[str(path.relative_to(PROJECT))]=sha(path)
    for cp in data['checkpoints']: frozen[cp['path']]=cp['sha256']
write(UNIT/'prior_evidence_hashes_start.json',frozen)
progress={name:sha(SHARED/name) for name in ('inventory.json','remaining_questions.jsonl','exploration_report.json','refinement_dispatch_20261102.json')}
write(UNIT/'mutable_progress_hashes_start.json',{'classification':'diagnostic mutable runtime metadata; not frozen source','hashes':progress})

for qid,data in history.items():
    print('\nHISTORY '+qid)
    for d in data['designs']:
        directory=(PROJECT/d).parent
        for path in sorted(directory.rglob('*.json')):
            if path.name=='request.json':
                request=read(path)
                print(json.dumps({'request':str(path.relative_to(PROJECT)),'keys':list(request),'sha256':sha(path),'messages_without_embedded_image':[{**m,'content':[v for v in m['content'] if v['type']=='text']} if isinstance(m.get('content'),list) else m for m in request['messages']]},ensure_ascii=False))
            elif path.name not in ('context.json','render_check.json','path_fingerprints.json','binding.json','summary.json','design_snapshot.json'):
                print(str(path.relative_to(PROJECT)))
                print(path.read_text(encoding='utf-8-sig'))

def relevant_nodes(value,qid):
    if isinstance(value,dict):
        if value.get('question_id',value.get('id'))==qid:
            yield value; return
        if qid in value:
            yield {qid:value[qid]}
        for key,item in value.items():
            if key!=qid: yield from relevant_nodes(item,qid)
    elif isinstance(value,list):
        for item in value: yield from relevant_nodes(item,qid)
for qid,data in history.items():
    for cp in data['checkpoints']:
        value=read(PROJECT/cp['path'])
        nodes=list(relevant_nodes(value,qid))
        write(UNIT/qid/(Path(cp['path']).parent.name+'_prior_prescreen.json'),{'checkpoint':cp,'nodes':nodes})
        print(json.dumps({'question_id':qid,'checkpoint':cp,'relevant_nodes':nodes},ensure_ascii=False))

for qid,variant in [('Plane295','inner_ear_shoulder_correspondence'),('Plane342','quarterturn_wedge_edge_binding')]:
    path=SHARED/'independent_review'/(qid+'_'+variant)/'independent_review.json'
    value=read(path)
    print('REJECTION REPORT '+qid+' TOP KEYS '+str(list(value)))
    substantive={k:v for k,v in value.items() if not any(t in k.lower() for t in ('hash','fingerprint','preservation','supporting','binding','source_audit','evidence'))}
    print(json.dumps(substantive,ensure_ascii=False,indent=2))
    write(UNIT/('semantic_lesson_'+qid+'_report_read.json'),{'path':str(path.relative_to(PROJECT)),'sha256':sha(path),'all_keys':list(value),'substantive':substantive,'full_json_loaded':True})
