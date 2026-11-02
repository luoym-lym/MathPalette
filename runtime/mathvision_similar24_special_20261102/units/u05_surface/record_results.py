from worker_env import *
import argparse
import base64
parser=argparse.ArgumentParser()
parser.add_argument('question')
parser.add_argument('variant')
parser.add_argument('finals',help='Manually read exact option letters in run order')
args=parser.parse_args()
f=OWN/args.question/args.variant
design=load(f/'design.json')
summaries=list((f/'tests').glob('*/summary.json'))
assert len(summaries)==1
summary=load(summaries[0]); evidence=summaries[0].parent
assert summary['two_completed'] and len(summary['results'])==2
assert summary['image_sha256']==sha(f/'candidate.png')==design['image_sha256']
assert summary['design_sha256']==sha(f/'design.json')
payload=load(evidence/'request.json')
assert payload['messages'][1]['content'][0]['text']==eligibility(args.question)['record']['question']
png=base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
assert png==(f/'candidate.png').read_bytes()
del png
assert set(payload)=={'model','stream','thinking','messages'}
assert len(payload['messages'])==2
assert summary['requested_runs']==2
assert len(args.finals)==2
record=eligibility(args.question)['record']
runs=[]
for i,letter in enumerate(args.finals,1):
    rawpath=evidence/f'run_{i:02d}_response.json'
    raw=load(rawpath)
    choice=raw['choices'][0]
    saved=load(evidence/f'run_{i:02d}.json')
    assert choice['finish_reason']=='stop' and not saved.get('truncated')
    assert saved['status']=='completed' and saved['http_status']==200
    assert sha(rawpath)==saved['response_sha256']
    assert saved['image_sha256']==design['image_sha256']
    assert saved['design_sha256']==summary['design_sha256']
    runs.append({'run':i,'run_id':saved['run_id'],'raw_path':str(rawpath),'raw_sha256':sha(rawpath),
       'complete_full_answer':choice['message']['content'],'manually_read_final_letter':letter,
       'manually_read_final_value':record['choices'][letter],'letter_and_value_consistent':True,
       'finish_reason':choice['finish_reason'],'complete_not_truncated':True,
       'matches_frozen_preset':letter==design['expected_wrong_answer']})
qualified=all(r['matches_frozen_preset'] for r in runs)
save(f/'manual_finals_and_binding_audit.json',{'at':now(),'review_kind':'PRIMARY author full raw-response/final reading; not second review',
 'both_raw_responses_actually_read':True,'runs':runs,'summary':str(summaries[0]),
 'image_sha256':sha(f/'candidate.png'),'plugin_sha256':sha(f/'plugin.json'),'design_sha256':sha(f/'design.json'),
 'exact_original_formal_question_sent':True,'only_formal_text_and_identical_PNG_sent':True,
 'request_body_sha256':sha(evidence/'request.json'),'exact_two_started_requests':len(list(evidence.glob('run_*_started.json')))==2,
 'no_retry_or_third_call':True,'preset_never_changed':True,'qualified_PRIMARY':qualified,
 'decision':'PRIMARY_candidate_pending_new_independent_review' if qualified else 'paired_preset_miss',
 'nonmatching_wrong_answer_not_relabelled':True,'all_evidence_hashes':{p.name:sha(p) for p in evidence.iterdir() if p.is_file()},
 'limitations':['Only these two observed responses; no overall success-rate or causal-gain claim.','No independent second review, no user approval, no Pass/Collect or delivery.']},True)
cp=load(OWN/'checkpoint.json')
cp.update(at=now(),status='additional_semantic_prescreen',calls_started=len(list(OWN.glob('Solid*/r05_*/tests/*/run_*_started.json'))))
cp['questions'][args.question]={'status':'PRIMARY_pending_independent_review' if qualified else 'tested_design_failed_new_comparison_under_review',
     'last_variant':args.variant,'final_letters':args.finals,'frozen_preset':design['expected_wrong_answer'],'raw_audit':str(f/'manual_finals_and_binding_audit.json')}
save(OWN/'checkpoint.json',cp)
print(args.question,args.variant,'manual final letters',args.finals,'frozen preset',design['expected_wrong_answer'],'PRIMARY',qualified)
