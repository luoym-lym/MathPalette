from unit_env import *
import base64

qid,vid,letters=sys.argv[1:4]
letters=letters.split(',')
folder=OWN/qid/vid
summaries=list(folder.glob('tests/*/summary.json'))
assert len(summaries)==1
summary_path=summaries[0]
summary=read(summary_path)
binding=read(summary_path.parent/'binding.json')
design=read(folder/'design.json')
assert len(letters)==len(summary['results'])==2
request_data=(summary_path.parent/'request.json').read_bytes()
request=json.loads(request_data)
blocks=request['messages'][1]['content']
assert blocks[0]['text']==eligibility(qid)['record']['question']
assert sha(base64.b64decode(blocks[1]['image_url']['url'].split(',',1)[1]))==design['candidate_sha256']
assert sha(request_data)==binding['request_body_sha256']==summary['request_body_sha256']
assert sha((folder/'design.json').read_bytes())==binding['design_sha256']
assert (summary_path.parent/'design_snapshot.json').read_bytes()==(folder/'design.json').read_bytes()
reviews=[]
for i,(letter,job) in enumerate(zip(letters,summary['results']),1):
    raw_path=summary_path.parent/f'run_{i:02d}_response.json'
    raw=raw_path.read_bytes()
    data=json.loads(raw)
    answer=data['choices'][0]['message']['content']
    assert job['answer']==answer and sha(raw)==job['response_sha256']
    assert job['request_body_sha256']==binding['request_body_sha256']
    assert job['image_sha256']==binding['image_sha256']==design['candidate_sha256']
    assert job['design_sha256']==binding['design_sha256']
    complete=job['status']=='completed' and not job['truncated'] and data['choices'][0]['finish_reason']=='stop'
    reviews.append({'run_index':i,'full_raw_response_path':str(raw_path),'raw_sha256':sha(raw),
                    'complete_answer_text':answer,'finish_reason':data['choices'][0]['finish_reason'],
                    'complete_nontruncated':complete,'final_letter_read_manually':letter,
                    'final_value_read_manually':design['formal_record']['choices'][letter],
                    'letter_value_conflict':False,'matches_frozen_wrong_preset':complete and letter==design['expected_wrong_answer'],
                    'review_method':'Author read the entire raw response and final answer; letters passed explicitly after manual reading, not extracted from incidental body mentions.'})
two_hit=all(r['matches_frozen_wrong_preset'] for r in reviews)
review={'reviewed_at':now(),'review_kind':'PRIMARY_MANUAL_FULL_FINAL_AND_BINDING_REVIEW',
        'question_id':qid,'variant_id':vid,'original_correct_answer':'E',
        'frozen_wrong_preset':{'letter':design['expected_wrong_answer'],'value':design['expected_wrong_value']},
        'runs':reviews,'two_hit':two_hit,'actual_calls':2,'summary_path':str(summary_path),
        'binding_sha256':sha((summary_path.parent/'binding.json').read_bytes()),
        'image_sha256':design['candidate_sha256'],'design_sha256':binding['design_sha256'],
        'outcome':'PRIMARY_CANDIDATE_REQUIRES_NEW_INDEPENDENT_PARENT_REVIEW' if two_hit else 'FAILED_EXACT_TWO_HIT_GATE_DO_NOT_RETEST',
        'mechanism_inference_limit':'Final-answer agreement is observational. Model explanations may contain misread coordinates, arithmetic errors, or another mechanism; no causal or general-rate claim follows.',
        'no_third_call_or_posthoc_preset_change':True}
save(folder/'manual_full_final_review.json',review)
if two_hit:
    queue=read(OWN/'second_review_queue.json')
    queue.append({'question_id':qid,'variant_id':vid,'candidate_directory':str(folder),
                  'image_sha256':design['candidate_sha256'],'plugin_sha256':design['plugin_sha256'],
                  'design_sha256':binding['design_sha256'],'original_correct_answer':'E',
                  'frozen_wrong_preset':review['frozen_wrong_preset'],'two_complete_finals':reviews,
                  'summary_path':str(summary_path),'primary_review_path':str(folder/'primary_review_before_calls.json'),
                  'manual_final_review_path':str(folder/'manual_full_final_review.json'),
                  'reference_transfer_path':str(folder/'reference_transfer.json'),
                  'status':'PRIMARY_ONLY_NEW_INDEPENDENT_PARENT_REVIEW_REQUIRED',
                  'limitations':['Only these two observed calls support answer agreement; no causal/general-rate claim.',
                                 'No independent second review, user approval, Pass, Collect, or delivery performed.']})
    save(OWN/'second_review_queue.json',queue,replace=True)
checkpoint=read(OWN/'checkpoint.json')
checkpoint['updated_at']=now()
checkpoint['new_actual_calls']=len(list(OWN.glob('Plane*/**/tests/*/run_*_started.json')))
checkpoint['question_status'][qid]='PRIMARY_candidate_pending_parent_second_review' if two_hit else 'current_candidate_failed_material_refinement_assessment_pending'
checkpoint['status']='research_in_progress'
checkpoint['PRIMARY_candidates']=len(read(OWN/'second_review_queue.json'))
save(OWN/'checkpoint.json',checkpoint,replace=True)
print(json.dumps({'qid':qid,'finals':letters,'frozen_wrong':design['expected_wrong_answer'],'two_hit':two_hit,'total_calls':checkpoint['new_actual_calls']}))
