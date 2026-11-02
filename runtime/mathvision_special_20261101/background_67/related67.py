from env67 import *
import re
A=read(OWN/'snapshots/background_67_assignment.json')
items={x['question_id']:x for x in A['questions']}
results={q:[] for q in QIDS}
count=0
for branch in ('Analytics','PlaneGeometry','SolidGeometry'):
    path=PROJECT/branch/'dataset.jsonl'
    with path.open(encoding='utf-8-sig') as f:
        for line in f:
            if not line.strip(): continue
            r=json.loads(line); count+=1
            p=PROJECT/branch/r['image']
            ih=sha(p)
            for q,v in items.items():
                if r['id']==q: continue
                src=v['source_assignment_question']['source_inputs']
                reasons=[]
                if ih==src['formal_png_sha256']: reasons.append('exact_same_formal_PNG')
                if r.get('source_dataset')=='MathVision' and r.get('source_key')==v['formal_record']['source_key']: reasons.append('same_MathVision_source_key')
                if re.sub(r'\s+','',r['question'])==re.sub(r'\s+','',v['formal_record']['question']): reasons.append('same_formal_question_ignoring_whitespace')
                if reasons: results[q].append({'branch':branch,'id':r['id'],'reasons':reasons,'formal_record':r,'formal_PNG_sha256':ih})
            del r
save('related_duplicate_source_audit.json',{'at':now(),'scope':list(QIDS),'formal_records_checked':count,'methods':['Exact formal PNG SHA256 across all three formal branches','Same MathVision source_key','Same complete formal question ignoring whitespace'],'results':results,'semantic_limit':'No universal semantic-duplicate claim. Every scoped old history artifact and whole-task tested-PNG binding is also audited separately.','no_other_question_designs_or_calls':True})
print('RELATED_DUPLICATE_SOURCE',count,{q:len(v) for q,v in results.items()},flush=True)
