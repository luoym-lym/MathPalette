from env67 import *
import argparse
import base64
import gc

parser=argparse.ArgumentParser()
parser.add_argument('mode',choices=['pre','post'])
parser.add_argument('question',choices=QIDS)
args=parser.parse_args()
q=args.question
row=next(x for x in read(OWN/'copied_frozen_candidates.json') if x['question_id']==q)
d=Path(row['directory'])
if args.mode=='pre':
    assert not (OWN/'local_failure_checkpoint.json').exists()
    assert not (OWN/'remote_failure_stop.json').exists()
    assert read(OWN/'zero_call_final_gate.json')['all_three_zero_prior_actual_calls_proved']
    assert not (d/'precall_fresh_audit.json').exists(),'No repeat invocation allowed'
    assert not list(d.glob('tests/**/run_*')),'Prior actual invocation blocks unchanged reuse'
    e=eligibility(q); assert e['eligible'],e['reasons']
    provenance=read(d/'reuse_provenance.json')
    for r in provenance['source_copy_hashes']:
        assert sha(r['source'])==r['source_sha256']==sha(r['copy'])==r['copy_sha256']
    assert sha(d/'candidate.png')==row['PNG_sha256']
    assert sha(d/'design.json')==row['design_sha256']
    h=read(OWN/'harness_relocation_byte_audit.json')
    assert sha(h['local_copy'])==h['local_copy_sha256'] and sha(h['source'])==h['source_sha256']
    save(d/'precall_fresh_audit.json',{'at':now(),'question_id':q,'variant_id':row['variant_id'],'original_date_and_wrong_preset_preserved':True,'expected_wrong_answer':row['expected_wrong_answer'],'planned_actual_calls':2,'runs_argument':2,'eligible':e,'full_reuse_source_and_copy_hashes_rechecked':True,'zero_call_scan':str(OWN/'zero_call_final_gate.json'),'fresh_primary_review':str(OWN/q/'fresh_primary_math_native_every_marker_review.json'),'fresh_replay':str(OWN/q/'fresh_offline_replay_audit.json'),'harness_exact_local_bootstrap_only_audit':h,'only_solver_inputs':'Exact formal question and this unchanged frozen PNG; no design, answer, preset, history, parameters or intention in payload.','no_retry_third_call_cherry_pick_relabel':True})
    print(q,'PRECALL_CURRENT_APPROVAL_SOURCE_HASH_ZERO_SCHEMA_REPLAY_PASS',flush=True)
else:
    folders=list((d/'tests').glob('quicktest3_*'))
    assert len(folders)==1,'Exactly one harness invocation permitted'
    t=folders[0]
    binding=read(t/'binding.json')
    request_bytes=(t/'request.json').read_bytes()
    payload=json.loads(request_bytes)
    e=eligibility(q)
    assert e['eligible']
    assert set(payload)=={'model','stream','thinking','messages'}
    assert payload['model']=='mimo-v2.6-flash' and payload['thinking']=={'type':'disabled'} and payload['stream'] is False
    messages=payload['messages']
    assert len(messages)==2 and messages[0]=={'role':'system','content':binding['system_prompt']}
    assert messages[1]['role']=='user' and len(messages[1]['content'])==2
    assert messages[1]['content'][0]=={'type':'text','text':e['formal_record']['question']}
    assert messages[1]['content'][1]['type']=='image_url'
    embedded=base64.b64decode(messages[1]['content'][1]['image_url']['url'].split(',',1)[1],validate=True)
    assert embedded==(d/'candidate.png').read_bytes()
    assert hashlib.sha256(embedded).hexdigest()==binding['image_sha256']==row['PNG_sha256']
    del embedded,payload,messages
    assert hashlib.sha256(request_bytes).hexdigest()==binding['request_body_sha256']
    assert sha(d/'design.json')==sha(t/'design_snapshot.json')==binding['design_sha256']==row['design_sha256']
    assert binding['expected_wrong_answer']==row['expected_wrong_answer'] and binding['requested_runs']==2
    summary=read(t/'summary.json') if (t/'summary.json').exists() else None
    raw=[]
    complete=True
    with (d/'full_new_finals.txt').open('x',encoding='utf-8') as finals:
        for i in (1,2):
            p=t/f'run_{i:02d}.json'
            start=t/f'run_{i:02d}_started.json'
            response=t/f'run_{i:02d}_response.json'
            record={'run':i,'started_exists':start.exists(),'run_record_exists':p.exists(),'raw_response_exists':response.exists()}
            if start.exists():
                s=read(start); record['started']=s
                assert s['request_body_sha256']==binding['request_body_sha256'] and s['image_sha256']==binding['image_sha256'] and s['design_sha256']==binding['design_sha256']
            if p.exists():
                run=read(p); record['run_record']=run
                complete=complete and run.get('status')=='completed' and not run.get('truncated')
                finals.write('\nRUN '+str(i)+' STATUS '+str(run.get('status'))+'\n')
            else: complete=False
            if response.exists():
                assert sha(response)==run['response_sha256']
                v=read(response)
                record['raw_response_sha256']=sha(response)
                record['raw_finish_reasons']=[c.get('finish_reason') for c in v.get('choices',[])]
                complete=complete and record['raw_finish_reasons']==['stop']
                for c in v.get('choices',[]):
                    content=c.get('message',{}).get('content')
                    assert content==run['answer']
                    finals.write('FINISH '+str(c.get('finish_reason'))+'\n'+str(content)+'\n')
                del v
            else: complete=False
            raw.append(record)
            gc.collect()
    starts=list(t.glob('run_*_started.json'))
    allfiles=[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in t.iterdir() if p.is_file()]
    complete=complete and len(starts)==2 and summary is not None and summary.get('two_completed') is True
    audit={'at':now(),'question_id':q,'variant_id':row['variant_id'],'expected_wrong_answer':row['expected_wrong_answer'],'evidence_directory':str(t),'same_frozen_exact_PNG_only_formal_question_payload_verified':True,'unchanged_profile_system_model_thinking_verified':True,'actual_start_count':len(starts),'complete_exact_pair':complete,'all_files':allfiles,'binding':binding,'runs':raw,'full_finals_for_manual_read':str(d/'full_new_finals.txt'),'no_automatic_success_grading':True,'postcall_authoritative_eligibility':e}
    save(d/'postcall_binding_raw_audit.json',audit)
    if not complete:
        save('remote_failure_stop.json',{'at':now(),'question_id':q,'evidence_directory':str(t),'actual_starts':len(starts),'reason':'Harness did not yield exactly two complete non-truncated final responses. Stop all subsequent calls without retry.','audit':str(d/'postcall_binding_raw_audit.json')})
    print(q,'ACTUAL_STARTS',len(starts),'COMPLETE_PAIR',complete,'FULL_FINALS',str(d/'full_new_finals.txt'),flush=True)
