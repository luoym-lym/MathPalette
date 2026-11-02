import own_runtime as rt
import sys,json,hashlib,base64
from pathlib import Path

def review(d,manual):
    d=Path(d).resolve();rt.check_write(d)
    design=rt.read(d/'design.json');qid=design['question_id']
    evidence=list((d/'tests').glob('quicktest3_*'))
    assert len(evidence)==1
    e=evidence[0];summary=rt.read(e/'summary.json');binding=rt.read(e/'binding.json')
    assert summary['two_completed'] is True
    assert len(list(e.glob('run_??_started.json')))==2
    assert len(summary['results'])==2 and len(manual)==2
    request=(e/'request.json').read_bytes();payload=json.loads(request)
    record=next(json.loads(s) for s in (rt.PROJECT/'PlaneGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if json.loads(s)['id']==qid)
    assert payload['messages'][1]['content'][0]['text']==record['question']==binding['question']
    image=base64.b64decode(payload['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
    assert image==(d/'candidate.png').read_bytes()
    assert hashlib.sha256(request).hexdigest()==binding['request_body_sha256']
    assert rt.sha(d/'design.json')==binding['design_sha256']
    assert (e/'design_snapshot.json').read_bytes()==(d/'design.json').read_bytes()
    assert rt.sha(d/'candidate.png')==binding['image_sha256']==design['image_sha256']
    findings=[]
    for i,(result,decision) in enumerate(zip(summary['results'],manual),1):
        p=e/f'run_{i:02d}_response.json';raw=p.read_bytes();obj=json.loads(raw)
        assert result['status']=='completed' and not result['truncated']
        assert result['finish_reason']=='stop' and obj['choices'][0]['finish_reason']=='stop'
        assert hashlib.sha256(raw).hexdigest()==result['response_sha256']
        full=obj['choices'][0]['message']['content'];assert full==result['answer']
        assert decision['full_final_manually_read'] is True
        hit=decision['final_answer']==str(design['expected_wrong_answer']) and decision['value_letter_consistent']
        findings.append({'run_index':i,'raw_response_path':str(p),'raw_response_sha256':rt.sha(p),
            'finish_reason':'stop','full_content':full,**decision,'matches_frozen_preset':hit})
    qualified=all(f['matches_frozen_preset'] for f in findings)
    result={'question_id':qid,'variant_id':design['variant_id'],'reviewed_at':rt.now(),
        'review_role':'PRIMARY_AUTHOR_ONLY_NOT_INDEPENDENT','frozen_expected_wrong_answer':design['expected_wrong_answer'],
        'frozen_expected_wrong_value':design['expected_wrong_value'],'correct_answer':design['correct_answer'],
        'actual_complete_runs':2,'all_raw_answers_read_in_full_manually':True,'bindings_exact':True,
        'raw_final_reviews':findings,'credible_primary_two_hit_candidate':qualified,
        'status':'PRIMARY_TWO_HIT_REQUIRES_NEW_PARENT_SECOND_REVIEW' if qualified else 'MISS_NO_RETEST_NO_POSTHOC_PRESET_CHANGE',
        'summary_path':str(e/'summary.json'),'summary_sha256':rt.sha(e/'summary.json'),
        'image_sha256':rt.sha(d/'candidate.png'),'plugin_sha256':rt.sha(d/'plugin.json'),'design_sha256':rt.sha(d/'design.json'),
        'human_primary_review_path':str(d/'visual_primary_before_calls.json'),
        'reference_transfer_path':str(d/'reference_transfer.json'),'limits':design['limitations']}
    rt.save(d/'primary_final_review.json',result)
    queue=rt.read(rt.OWN/'second_review_queue.json')
    assert not any(r['candidate_directory']==str(d) for r in queue)
    if qualified:
        queue.append({'question_id':qid,'variant_id':design['variant_id'],'candidate_directory':str(d),
            'image_sha256':rt.sha(d/'candidate.png'),'plugin_sha256':rt.sha(d/'plugin.json'),'design_sha256':rt.sha(d/'design.json'),
            'original_correct_answer':design['correct_answer'],'frozen_wrong_preset':{'answer':design['expected_wrong_answer'],'value':design['expected_wrong_value']},
            'two_complete_finals':findings,'summary_path':str(e/'summary.json'),'primary_review_path':str(d/'primary_final_review.json'),
            'reference_transfer_path':str(d/'reference_transfer.json'),'limitations':design['limitations'],
            'status':'PRIMARY_ONLY_NEW_INDEPENDENT_SECOND_REVIEW_REQUIRED'})
    rt.save(rt.OWN/'second_review_queue.json',queue)
    print(qid,design['variant_id'],[f['final_answer'] for f in findings],qualified)

if __name__=='__main__':
    d=Path(sys.argv[1]);review(d,rt.read(d/'manual_decisions.json'))
