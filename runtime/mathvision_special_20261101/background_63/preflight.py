from bootstrap import *
import gc
import shutil
from dataset_tools.catalog import content,digest

assignment=read(BASE/'background_63_assignment.json')
checks=[]
for rawpath,expected in assignment['source_and_old_evidence_current_hashes'].items():
    p=Path(rawpath)
    checks.append({'path':str(p),'expected':expected,'current':sha(p) if p.is_file() else None})
for q in assignment['questions']:
    for name,expected in q['frozen_files_sha256'].items():
        p=Path(q['source_directory'])/name
        checks.append({'path':str(p),'expected':expected,'current':sha(p)})
write(HERE/'assignment_hash_freshness.json',{'checked_at':now(),'checks':checks,'all_exact':all(x['current']==x['expected'] for x in checks)})
for name in ('remaining_questions.jsonl','refinement_dispatch_20261102.json'):
    p=BASE/name
    if p.is_file():
        shutil.copyfile(p,HERE/'readin_snapshots'/(name+'.'+sha(p)+'.snapshot'))
for q in assignment['questions']:
    qid=q['question_id'];d=HERE/qid;d.mkdir(exist_ok=True)
    record=next(r for r in rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']==qid)
    assert record==q['formal_record']
    approval=read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    payload=content(PROJECT,'SolidGeometry',record)
    current=digest(payload)
    accepted=[r for r in rows(PROJECT/'SolidGeometry/special_variant/accepted_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    collected=[r for r in rows(PROJECT/'SolidGeometry/special_variant/collected_index.jsonl') if r.get('question_id',r.get('id'))==qid]
    sd=PROJECT/'SolidGeometry/special_variant'/qid
    sf=[str(p) for p in sd.rglob('*') if p.is_file()] if sd.exists() else []
    rootrow=next(r for r in rows(PROJECT/'question_bank.jsonl') if r['id']==qid)
    valid=approval.get('reviewer')=='user' and bool(approval.get('instruction')) and bool(approval.get('approved_at_utc')) and current==approval['content_sha256']
    eligible=record['source_dataset']=='MathVision' and valid and not accepted and not collected and not sf and not rootrow.get('special_plugins')
    report=dict(checked_at=now(),question_id=qid,record=record,approval=approval,current_content_sha256=current,approval_matches_current=valid,accepted=accepted,collected=collected,formal_special_files=sf,root_special_plugins=rootrow.get('special_plugins'),eligible=eligible,frozen_content=payload)
    write(d/'fresh_eligibility_and_approval.json',report)
    assert eligible
    print(qid,current,'eligible',flush=True)
    del payload,report,approval,record;gc.collect()
write(HERE/'preflight_complete.json',{'checked_at':now(),'source_and_old_frozen_hashes_exact':all(x['current']==x['expected'] for x in checks),'question_ids':['Solid206','Solid207'],'no_API':True})
