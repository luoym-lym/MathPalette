from tools_local import *
oldunits={'Solid87':'background_13','Solid99':'background_13','Solid112':'background_14','Solid114':'background_15','Solid116':'background_15','Solid117':'background_15','Solid135':'background_14','Solid139':'background_14'}
for q,u in oldunits.items():
    folder=TASK.parent/u/q
    files={str(p.relative_to(ROOT)):file_hash(p) for p in folder.rglob('*') if p.is_file()}
    relevant=[]
    for p in folder.rglob('*.json'):
        if p.name in ['primary_prescreen.json','prescreen.json','design.json','primary_review.json','manual_final_review.json'] or 'response' in p.name:
            relevant.append({'path':str(p.relative_to(ROOT)),'content':json.loads(p.read_text(encoding='utf-8-sig'))})
    checkpoint=json.loads((TASK.parent/u/'checkpoint.json').read_text(encoding='utf-8-sig'))
    def find(v):
        out=[]
        if isinstance(v,dict):
            if v.get('question_id')==q:out.append(v)
            else:
                for x in v.values():out.extend(find(x))
        elif isinstance(v,list):
            for x in v:out.extend(find(x))
        return out
    record={'question_id':q,'prior_folder':str(folder),'all_prior_files_sha256':files,'full_relevant_records':relevant,'checkpoint_rows':find(checkpoint),'prior_design_count':len(list(folder.rglob('design.json'))),'prior_response_count':len(list(folder.rglob('*response.json'))),'history_readonly':True}
    write(TASK/q/'history_audit.json',record)
    print(q,'old designs',record['prior_design_count'],'old responses',record['prior_response_count'])
for q in ['Solid99','Solid112','Solid117','Solid139']:
    ctx=json.loads((TASK/q/'context.json').read_text(encoding='utf-8'))
    print(q,'first objects',json.dumps(ctx['objects'][:3],ensure_ascii=False))
