from own_bootstrap import *

directory=Path(sys.argv[1]).resolve()
final_values=sys.argv[2].split(',')
assert len(final_values)==2
summaries=list((directory/'tests').rglob('summary.json'))
assert len(summaries)==1
summary_path=summaries[0];summary=load(summary_path)
assert summary['two_completed'] and len(summary['results'])==2
assert summary['image_sha256']==sha(directory/'candidate.png')
assert summary['design_sha256']==sha(directory/'design.json')
binding=load(summary_path.parent/'binding.json')
assert binding['design_sha256']==summary['design_sha256']
expected=load(directory/'design.json')['expected_wrong_answer']
reviews=[]
for i,(result,value) in enumerate(zip(summary['results'],final_values),1):
    raw_path=summary_path.parent/f'run_{i:02d}_response.json'
    raw=load(raw_path)
    assert result['status']=='completed' and not result['truncated'] and raw['choices'][0]['finish_reason']=='stop'
    text=raw['choices'][0]['message']['content']
    assert text==result['answer']
    assert sha(raw_path)==result['response_sha256']
    reviews.append({'run_index':i,'raw_path':str(raw_path),'raw_sha256':sha(raw_path),
        'entire_raw_response_and_entire_answer_read_by_primary':True,'full_answer_text':text,
        'manual_final_value':value,'manual_final_letter':None,'expected_value':expected,
        'complete_nontruncated':True,'finish_reason':'stop','final_letter_value_conflict':False,
        'matches_frozen_preset':value==expected,
        'judgment_basis':'Primary agent read complete verbatim response; only the final committed edge identifier counts, not intermediate mentions.'})
passed=all(r['matches_frozen_preset'] for r in reviews)
request=load(summary_path.parent/'request.json')
assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
assert request['stream'] is False and len(request['messages'])==2
assert request['messages'][1]['content'][0]['text']==summary['question']
assert [p['type'] for p in request['messages'][1]['content']]==['text','image_url']
assert not any(k in request for k in ('max_tokens','max_completion_tokens'))
assert hashlib.sha256((summary_path.parent/'request.json').read_bytes()).hexdigest()==summary['request_body_sha256']
import base64
png=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1]);assert hashlib.sha256(png).hexdigest()==summary['image_sha256'];del png,request
report={'question_id':summary['question_id'],'variant_id':load(directory/'design.json')['variant_id'],
    'review_type':'PRIMARY only','reviewed_at':now(),'summary_path':str(summary_path),'summary_sha256':sha(summary_path),
    'design_sha256':summary['design_sha256'],'image_sha256':summary['image_sha256'],'plugin_sha256':sha(directory/'plugin.json'),
    'correct_answer':'5','frozen_wrong_preset':expected,'reviews':reviews,'double_hit':passed,
    'decision':'PRIMARY_CANDIDATE_PENDING_NEW_INDEPENDENT_REVIEW' if passed else 'FAIL_PREDECLARED_TWO_HIT_GATE',
    'actual_calls':2,'third_call_or_relabel':False,'original_payload_verified':True,
    'no_general_success_or_causal_claim':True,'not_user_approval_Pass_Collect_or_delivery':True}
save(directory/'manual_final_review.json',report,exclusive=True)
cp=load(OWN/'checkpoint.json');cp.update(updated_at=now(),phase='primary_assessment')
cp.setdefault('attempts',[]).append({'question_id':summary['question_id'],'variant_id':report['variant_id'],
   'directory':str(directory),'frozen_preset':expected,'actual_calls':2,'finals':final_values,'double_hit':passed,
   'manual_final_review_path':str(directory/'manual_final_review.json')})
if passed:
    entry={'question_id':summary['question_id'],'variant_id':report['variant_id'],'candidate_directory':str(directory),
       'image_sha256':summary['image_sha256'],'plugin_sha256':sha(directory/'plugin.json'),'design_sha256':summary['design_sha256'],
       'original_correct_answer':'5','frozen_wrong_preset':load(directory/'design.json')['preset_semantics'],
       'two_complete_final_answers':reviews,'summary_path':str(summary_path),'summary_sha256':sha(summary_path),
       'primary_review_path':str(directory/'manual_final_review.json'),'primary_math_path':str(OWN/'Solid166/primary_math.json'),
       'primary_visual_review_path':str(directory/'primary_visual_review.json'),
       'reference_transfer_path':str(directory/'reference_transfer.json'),'history_difference_path':str(directory/'history_difference.json'),
       'eligibility_before_each_actual_call':[str(directory/'tests'/f'pre_network_run_{i:02d}.json') for i in (1,2)],
       'status':'PRIMARY_PENDING_NEW_INDEPENDENT_REVIEW','independent_second_review_performed':False,
       'limitations':['No user approval, Pass, Collect or delivery.','Only these two observed finals support the preset; no overall success-rate or causal gain claim.','Parent must create a new independent reviewer with complete raw/source/semantic evidence.']}
    queue=load(OWN/'second_review_queue.json');queue.append(entry);save(OWN/'second_review_queue.json',queue)
    cp['PRIMARY_candidates'].append({'question_id':entry['question_id'],'variant_id':entry['variant_id'],'directory':str(directory)})
    cp['questions'][summary['question_id']]={'status':'PRIMARY_PENDING_NEW_INDEPENDENT_REVIEW','candidate_directory':str(directory),'actual_calls_total':sum(a['actual_calls'] for a in cp['attempts'] if a['question_id']==summary['question_id'])}
else:
    cp['questions'][summary['question_id']]={'status':'continue_substantive_alternative_design','last_failed_directory':str(directory),'reason':'Final values do not both equal frozen preset; all raw preserved.','actual_calls_total':sum(a['actual_calls'] for a in cp['attempts'] if a['question_id']==summary['question_id'])}
save(OWN/'checkpoint.json',cp)
print(json.dumps({'variant':report['variant_id'],'preset':expected,'final_values':final_values,'double_hit':passed},ensure_ascii=False))
