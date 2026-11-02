from local_env import *
import json, hashlib

def check_eligibility(qid, stage):
    from dataset_tools import catalog
    assignment=read_json(OWN/'assignment.json')
    assigned=next(q for q in assignment['questions'] if q['question_id']==qid)
    branch=assigned['branch']
    record=next(r for r in catalog.rows(PROJECT/branch/'dataset.jsonl') if r['id']==qid)
    approval=read_json(PROJECT/'provenance/approvals.json')['approvals'][qid]
    current=catalog.digest(catalog.content(PROJECT,branch,record))
    accepted=[];collected=[];reasons=[]
    for leaf,out in [('accepted_index.jsonl',accepted),('collected_index.jsonl',collected)]:
        path=PROJECT/branch/'special_variant'/leaf
        if path.exists():
            out.extend(r for r in catalog.rows(path) if r.get('question_id',r.get('id'))==qid)
    rp=PROJECT/branch/'special_variant'/qid/'recipes.json'
    cp=rp.with_name('collection.json')
    recipes=read_json(rp) if rp.exists() else []
    collection=read_json(cp) if cp.exists() else None
    sources={rel:sha(PROJECT/rel) for rel in assigned['frozen_source_files_sha256']}
    if sources!=assigned['frozen_source_files_sha256']:reasons.append('frozen_source_drift')
    if current!=assigned['current_content_sha256'] or current!=approval['content_sha256'] or approval.get('reviewer')!='user': reasons.append('approval_drift')
    if record!=assigned['formal_record'] or record['source_dataset']!='MathVision':reasons.append('formal_record_drift')
    if accepted or collected or recipes or collection:reasons.append('already_special_or_completed')
    return {'question_id':qid,'stage':stage,'checked_at':now(),'eligible':not reasons,'reasons':reasons,
            'current_content_sha256':current,'approval':approval,'formal_record':record,'accepted':accepted,
            'collected':collected,'recipes':recipes,'collection':collection,'source_sha256':sources}

def check_frozen(candidate):
    design=read_json(candidate/'design.json')
    frozen=read_json(candidate/'frozen_design_sha256.json')
    assert sha(candidate/'design.json')==frozen['design_sha256'], 'immutable design changed'
    for name,expected in design['frozen_files'].items():
        assert sha(candidate/name)==expected, 'frozen candidate file changed: '+name
    assert read_json(candidate/'fresh_process_replay.json')['png_bytes_exact']
    return design
