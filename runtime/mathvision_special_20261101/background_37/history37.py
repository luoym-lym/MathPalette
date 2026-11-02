from tools37 import *
for q in sys.argv[1:]:
    print('\nHISTORY',q)
    old=OLD[q]
    for p in old.rglob('design.json'):
        d=read(p);print('DESIGN',json.dumps(d,ensure_ascii=False))
        for n in ['pretest_visual_review.json','primary_review.json','manual_final_review.json']:
            f=p.parent/n
            if f.exists():
                x=read(f);print(n,json.dumps({k:v for k,v in x.items() if k not in ['input_freeze','each_marker_role_and_source_binding','manual_results','pretest_proof_unchanged']},ensure_ascii=False))
        for f in sorted(p.parent.rglob('run_*_response.json')):
            data=read(f);print('RAW_RESPONSE',str(f),json.dumps(data,ensure_ascii=False))
    for n in ['prescreen.json']:
        if (old/n).exists():print(n,json.dumps(read(old/n),ensure_ascii=False))
    assessments=old.parent/'assessments.json'
    if assessments.exists():print('ASSESSMENT',json.dumps([x for x in read(assessments) if x.get('question_id')==q],ensure_ascii=False))
    cp=read(old.parent/'checkpoint.json')
    def select(v):
        if isinstance(v,dict):
            if v.get('question_id')==q:return v
            return {k:x for k,w in v.items() if (x:=select(w)) not in ({},[],None)}
        if isinstance(v,list):return [x for w in v if (x:=select(w)) not in ({},[],None)]
        return None
    print('CHECKPOINT_RELEVANT',json.dumps(select(cp),ensure_ascii=False))
