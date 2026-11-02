from tools37 import *
notes=read(ROOT/'provenance/source_notes.json')
for q in IDS:
    n=notes[q].get('geometry_notes',{})
    write(TASK/q/'source_geometry_notes.json',n)
    print(q,'MODEL',json.dumps(n.get('additional_model_evidence',{}),ensure_ascii=False))
old_records=[]
report=read(SHARED/'exploration_report.json')
for q in IDS:
    entries=[]
    for d in OLD[q].rglob('design.json'):
        responses=[]
        for p in sorted(d.parent.rglob('run_*_response.json')):
            raw=read(p);responses.append({'path':str(p),'sha256':file_hash(p),'complete_message':raw['choices'][0]['message'],'finish_reason':raw['choices'][0]['finish_reason']})
        reviews={p.name:{'path':str(p),'sha256':file_hash(p),'content':read(p)} for p in d.parent.glob('*review.json')}
        entries.append({'design_path':str(d),'design_sha256':file_hash(d),'design':read(d),'full_raw_responses':responses,'reviews':reviews,'unchanged_outcome':'MISS; never relabeled'})
    qa=next(x for x in ASSIGN['questions'] if x['question_id']==q)
    old_records.append({'question_id':q,'old_attempts':entries,'prior_summary':qa['prior_history_summary'],'independent_review_files':qa['prior_independent_review_files'],'control_reuse':'No existing original control calls for these eight according to historical attempts; no new controls planned','mutable_report_attempts':[a for a in report.get('attempts',[]) if a.get('question_id')==q]})
write(TASK/'old_history_audit.json',{'created_at':now(),'all_original_history_read_only':True,'records':old_records})
batches=[]
for i in range(1,12):
    b=SHARED/f'batch_{i:02d}'
    plugins=[]
    for p in b.rglob('plugin.json'):
        d=read(p)
        if d.get('params',{}).get('actions') is not None:
            plugins.append({'path':str(p),'sha256':file_hash(p),'question_id':d.get('question_id'),'intent':d.get('intent',d.get('description')),'actions':d['params']['actions']})
    # Batch format often uses named plugins under plugins/.
    for p in b.glob('plugins/*.json'):
        d=read(p)
        if 'params' in d and not any(x['path']==str(p) for x in plugins):plugins.append({'path':str(p),'sha256':file_hash(p),'question_id':d.get('question_id'),'intent':d.get('intent',d.get('description')),'actions':d['params'].get('actions')})
    batches.append({'batch':b.name,'plugins':plugins})
write(TASK/'delivered_reference_study.json',{'references':batches,'lesson':'Real partial-feature correspondence, exact ownership and orientation matter. An unchanged failed image is not new evidence. Numerical targets must retain counts and true spatial interfaces; avoid isolated answer salience and hidden-edge invention.'})
print('REFERENCES',json.dumps(batches,ensure_ascii=False))
