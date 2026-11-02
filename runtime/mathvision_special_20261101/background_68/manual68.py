from common68 import *
import base64

MANUAL={
 'Plane271': [
  dict(final_option='B',final_value='5 cm',consistent_letter_value=True,hit_predeclared_wrong=False,manual_reason='Full final explicitly says difference5 cm and correct choiceB. Frozen presetD means15 cm.'),
  dict(final_option=None,final_value='30 cm',incidental_or_forced_letter='D',consistent_letter_value=False,hit_predeclared_wrong=False,manual_reason='Full final insists correct value30 cm; only says forced D is plausible despite discrepancy. D actually means15 cm. Inconsistent letter/value and incidental forced choice do not count.')
 ],
 'Plane387': [
  dict(final_option=None,final_value='7 cm^2',consistent_letter_value=True,hit_predeclared_wrong=False,manual_reason='Full final explicitly concludes area7 cm^2 after its internal self-correction; frozen preset is12.'),
  dict(final_option=None,final_value='5*sqrt(3)/2 cm^2',consistent_letter_value=True,hit_predeclared_wrong=False,manual_reason='Full final is2.5sqrt(3), approximately4.33 cm^2; frozen preset is12. Neither incidental values nor an unrelated wrong answer count.')
 ],
 'Plane449': [
  dict(final_option='E',final_value='Rectangle E',consistent_letter_value=True,hit_predeclared_wrong=False,manual_reason='Full final explicitly concludes E. Its narrative misreads B-right3 as6 and discusses an invented mismatch; those errors do not make its terminal E equal the frozen presetD.'),
  dict(final_option='E',final_value='Rectangle E',consistent_letter_value=True,hit_predeclared_wrong=False,manual_reason='Full final explicitly gives I=E and the arrangement E,D,A/B,C; frozen presetD is not selected. Narrative spatial wording mistakes are preserved, not relabeled as a hit.')
 ]
}

def review(qid):
    q=next(q for q in read(BASE/'background_68_assignment.json')['questions'] if q['question_id']==qid)
    d=HERE/qid/q['variant_id']
    invs=list((d/'tests').glob('quicktest3_*'));assert len(invs)==1
    inv=invs[0];binding=read(inv/'binding.json');summary=read(inv/'summary.json')
    assert summary['two_completed'] and len(summary['results'])==2
    assert binding['image_sha256']==sha(d/'candidate.png')==q['frozen_source_files_sha256']['candidate.png']
    assert binding['design_sha256']==sha(d/'design.json')==sha(inv/'design_snapshot.json')==q['frozen_source_files_sha256']['design.json']
    assert binding['expected_wrong_answer']==q['expected_wrong_answer']
    request=(inv/'request.json').read_bytes();payload=json.loads(request)
    assert hashlib.sha256(request).hexdigest()==binding['request_body_sha256']
    e=eligibility(qid);assert e['eligible']
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    assert len(payload['messages'])==2 and payload['messages'][0]=={'role':'system','content':binding['system_prompt']}
    user=payload['messages'][1]
    assert user['role']=='user' and len(user['content'])==2 and user['content'][0]=={'type':'text','text':e['record']['question']}
    encoded=user['content'][1]['image_url']['url'].split(',',1)[1]
    png=base64.b64decode(encoded);assert hashlib.sha256(png).hexdigest()==binding['image_sha256'];del png,encoded,payload,request
    manual=[];hashes={str(p):sha(p) for p in [inv/'request.json',inv/'binding.json',inv/'summary.json',inv/'design_snapshot.json',d/'candidate.png',d/'design.json',d/'plugin.json']}
    for i,item in enumerate(MANUAL[qid],1):
        rawpath=inv/f'run_{i:02d}_response.json';raw=read(rawpath)
        assert len(raw['choices'])==1 and raw['choices'][0]['finish_reason']=='stop'
        job=read(inv/f'run_{i:02d}.json');start=read(inv/f'run_{i:02d}_started.json');gate=read(d/f'actual_request_gate_{i:02d}.json')
        assert job['status']=='completed' and job['response_sha256']==sha(rawpath)
        assert start['request_body_sha256']==gate['request_body_sha256']==binding['request_body_sha256']
        assert gate['current_eligibility']['eligible'] and gate['all_frozen_sources_and_copies_hash_exact']
        hashes[str(rawpath)]=sha(rawpath)
        manual.append(dict(run_index=i,**item,full_final=raw['choices'][0]['message']['content'],raw_response_path=str(rawpath),raw_response_sha256=sha(rawpath),finish_reason='stop',full_final_personally_read=True))
        del raw,job,start,gate
    hits=sum(x['hit_predeclared_wrong'] for x in manual)
    write(d/'manual_final_review.json',dict(question_id=qid,variant_id=q['variant_id'],reviewed_at=now(),review_role='Primary research worker; not independent review or user approval',
        correct_answer=e['record']['answer'],immutable_expected_wrong_answer=q['expected_wrong_answer'],manual_finals=manual,hits=hits,two_actual_complete_calls=True,credible_primary_doublehit=(hits==2),
        status='PRIMARY_candidate_requires_NEW_independent_parent_review' if hits==2 else 'complete_pair_missed_unchanged_preset',
        exact_request_image_design_source_bindings_verified=True,solver_input_only_formal_question_plus_same_frozen_png=True,source_eligibility_before_each_actual_transport_verified=True,
        request_profile_unmodified=True,hashes=hashes,retries=0,third_calls=0,posthoc_relabel=False,original_controls_called=0,
        limitations='Two descriptive observations only; no original-control correctness or causal/mechanism hardgate. No promotion, delivery, Pass or Collect.'))
    print(qid,'manual valid preset hits',hits,'of2',flush=True)
if __name__=='__main__':review(sys.argv[1])
