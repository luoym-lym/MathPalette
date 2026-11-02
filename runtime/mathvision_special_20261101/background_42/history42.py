from env42 import *
def find(value,qid):
    if isinstance(value,dict):
        if value.get('question_id',value.get('id'))==qid:return [value]
        result=[]
        for k,v in value.items():
            if k==qid:result.append({k:v})
            elif isinstance(v,(dict,list)):result+=find(v,qid)
        return result
    if isinstance(value,list):return [item for v in value for item in find(v,qid)]
    return []
allfiles=list(BASE.rglob('*'))
for q in ASSIGNED:
    scoped=[p for p in allfiles if p.is_file() and not p.is_relative_to(HERE) and q in p.parts]
    hist=[]
    for p in allfiles:
        if not p.is_file() or p.is_relative_to(HERE) or p.suffix!='.json':continue
        if p.name not in ('checkpoint.json','exploration_report.json','second_review_queue.json','independent_review.json'):continue
        raw=p.read_text(encoding='utf-8-sig')
        if q not in raw:continue
        matches=find(json.loads(raw),q)
        if matches:hist.append({'path':str(p.relative_to(ROOT)),'sha256':file_hash(p),'matching_full_records':matches})
    designs=[p for p in scoped if p.name=='design.json']
    responses=[p for p in scoped if p.name.endswith('_response.json')]
    write(HERE/q/'prior_history_inventory.json',{'question_id':q,'created_at':now(),'scoped_prior_files':{str(p.relative_to(ROOT)):file_hash(p) for p in scoped},'prior_design_paths':[str(p.relative_to(ROOT)) for p in designs],'full_raw_response_paths':[str(p.relative_to(ROOT)) for p in responses],'checkpoint_and_report_full_matching_records':hist})
    print(json.dumps({'qid':q,'designs':[str(p.relative_to(BASE)) for p in designs],'raw_responses':len(responses),'prior_screens':[{'path':r['path'],'matching_records':r['matching_full_records']} for r in hist if not r['path'].endswith('exploration_report.json')]},ensure_ascii=False))
