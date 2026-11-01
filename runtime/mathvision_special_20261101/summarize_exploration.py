"""Readable checkpoint of new runtime work; no automatic success grading."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def save(name,data):
    (HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def is_control(path):
    return any('control' in part.lower() for part in path.relative_to(HERE).parts)

def main():
    inventory=read(HERE/'inventory.json')
    eligible={r['id']: {**r,'branch':branch} for branch,group in inventory.items() for r in group['eligible']}
    reviews={}
    for path in (HERE/'independent_review').rglob('independent_review.json'):
        value=read(path)
        candidate=value.get('candidate_directory',value.get('candidate_path',''))
        candidate=candidate.replace('\\','/').removeprefix('runtime/mathvision_special_20261101/')
        if candidate.endswith('/candidate.png'):
            candidate=candidate[:-len('/candidate.png')]
        reviews[candidate]={'decision':value['decision'],'review_file':str(path.relative_to(HERE)).replace('\\','/'),'rationale':value.get('rationale',value.get('strict_conclusion',''))}
    attempts=[]
    used=set()
    for path in HERE.rglob('design.json'):
        relative=path.relative_to(HERE)
        if relative.parts[0].startswith('batch_') or is_control(path):
            continue
        design=read(path)
        qid=design.get('question_id')
        if qid not in eligible:
            continue
        used.add(qid)
        folder=path.parent
        key=str(folder.relative_to(HERE)).replace('\\','/')
        summaries=[]
        for result in (folder/'tests').glob('*/summary.json'):
            value=read(result)
            summaries.append({'path':str(result.relative_to(HERE)).replace('\\','/'),'two_completed':value.get('two_completed',False),'expected_wrong_answer':value.get('expected_wrong_answer'),'statuses':[r.get('status') for r in value.get('results',[])],'answers_tail_for_review':[r.get('answer','')[-600:] for r in value.get('results',[])],'note':'Answer tails are for manual inspection; no automatic final-answer success grading.'})
        controls=[]
        for result in folder.rglob('summary.json'):
            if is_control(result):
                value=read(result)
                controls.append({'path':str(result.relative_to(HERE)).replace('\\','/'),'answers_tail':[r.get('answer','')[-600:] for r in value.get('results',[])]})
        attempts.append({'question_id':qid,'candidate':key,'predeclared_wrong_answer':design.get('expected_wrong_answer',design.get('predicted_wrong_answer')),'formal_correct_answer':eligible[qid]['answer'],'mechanism':design.get('mechanism',design.get('design_reason','')),'design_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'tests':summaries,'original_controls':controls,'independent_review':reviews.get(key),'approval_status':'No user Pass/Collect recorded'})
    assessed=set(used)
    work_units=[]
    for path in HERE.glob('background_*/checkpoint.json'):
        value=read(path)
        assessed_ids=value.get('new_question_ids',value.get('assessed_question_ids',[]))
        assessed.update(assessed_ids)
        assessed.update(x.get('qid') for x in value.get('prepared_five_drafts',[]) if x.get('qid'))
        work_units.append({'checkpoint':str(path.relative_to(HERE)).replace('\\','/'),
                           'new_questions':assessed_ids,
                           'completed_calls':value.get('completed_calls_including_control',value.get('total_completed_calls',value.get('all_completed_API_call_count'))),
                           'aborted_calls':value.get('aborted_calls',value.get('aborted_or_incomplete_calls',value.get('aborted_first_call_count'))),
                           'new_qualified_deliveries':value.get('new_qualified_deliveries',0)})
    batches=[]
    delivered=set()
    for path in HERE.glob('batch_*/manifest.json'):
        value=read(path)
        entries=value.get('candidates',[])
        delivered.update(x['question_id'] for x in entries)
        batches.append({'batch':value['batch'],'candidates':[x['question_id'] for x in entries],'review_html':str(path.parent.relative_to(HERE))+'/review.html','zip':path.parent.name+'.zip'})
    complete_pairs=sum(any(s['two_completed'] for s in a['tests']) for a in attempts)
    result={'created_at':datetime.now(timezone.utc).isoformat(),'scope':{'formal_mathvision_total':sum(v['mathvision_total'] for v in inventory.values()),'excluded_existing_pass_or_collect':sum(len(v['excluded']) for v in inventory.values()),'eligible_total':len(eligible),'eligible_by_branch':{b:v['eligible_count'] for b,v in inventory.items()}},'new_runtime_work':{'candidate_designs':len(attempts),'distinct_questions_explored':len(assessed),'questions_with_saved_designs':len(used),'candidates_with_complete_two_call_evidence':complete_pairs,'delivered_questions':sorted(delivered),'questions_without_deliverable':len(eligible)-len(delivered)},'delivered_batches':batches,'background_work_units':work_units,'quality_gate':'Frozen prediction + same PNG + 2 final-answer hits + independent mathematical/visual/information/necessity review; no Pass/Collect','reviews':reviews,'attempts':attempts,'limitations':['Formal questions and all pre-existing files remain read-only.','A correct original control and identical model reasoning are not added hard requirements; original-control errors and reasoning limitations are disclosed.','Some candidates intentionally rejected after two hits for weak information targeting.','All logs here are new authorized runtime experiments, not restored historical evaluation logs.']}
    save('exploration_report.json',result)
    remaining=[]
    for qid,record in eligible.items():
        if qid not in delivered:
            remaining.append({'question_id':qid,'branch':record['branch'],'status':'explored_no_deliverable' if qid in assessed else 'not_yet_explored','question':record['question'],'answer':record['answer']})
    (HERE/'remaining_questions.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in remaining),encoding='utf-8')
    print(json.dumps({'scope':result['scope'],'new_runtime_work':result['new_runtime_work'],'batches':batches},ensure_ascii=False))

if __name__=='__main__':
    main()
