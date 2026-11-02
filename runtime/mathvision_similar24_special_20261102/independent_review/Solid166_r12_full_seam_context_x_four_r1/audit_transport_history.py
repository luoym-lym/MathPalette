from review_bootstrap import *

def run():
    import ast
    import base64
    from PIL import Image
    import io
    source_ast=ast.parse((PROJECT/'SolidGeometry/workbench/quick_test.py').read_text(encoding='utf-8'))
    constants={}
    for node in source_ast.body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            if node.targets[0].id in ('SYSTEM_PROMPT','TEST_PROFILES'):
                constants[node.targets[0].id]=ast.literal_eval(node.value)
    formal=load(OWN/'current_eligibility.json')['formal_record']
    expected_profile={**constants['TEST_PROFILES']['quicktest3'],'api_base':'https://token-plan-cn.xiaomimimo.com/v1'}
    all_trials=[]
    for directory in sorted((UNIT/'Solid166').glob('r[0-9][0-9]_*')):
        invocations=list((directory/'tests').glob('quicktest3_*'))
        assert len(invocations)==1
        invocation=invocations[0]
        binding=load(invocation/'binding.json')
        summary=load(invocation/'summary.json')
        design=load(directory/'design.json')
        assert (invocation/'design_snapshot.json').read_bytes()==(directory/'design.json').read_bytes()
        assert len(list(invocation.glob('*_started.json')))==2
        assert len(list(invocation.glob('*_response.json')))==2
        assert len(summary['results'])==2 and summary['two_completed'] is True
        assert binding['requested_runs']==2
        assert binding['question_id']=='Solid166' and binding['branch']=='SolidGeometry'
        assert binding['question']==formal['question'] and binding['expected_wrong_answer']==design['expected_wrong_answer']
        assert binding['profile']=='quicktest3' and binding['settings']==expected_profile
        assert binding['system_prompt']==constants['SYSTEM_PROMPT']
        assert binding['question_record_sha256']==hashlib.sha256(canonical(formal).encode()).hexdigest()
        assert binding['reference_quick_test_sha256']==sha(PROJECT/'SolidGeometry/workbench/quick_test.py')
        assert binding['image_path']==str(directory/'candidate.png')
        assert binding['design_path']==str(directory/'design.json')
        assert binding['image_sha256']==sha(directory/'candidate.png')==sha(directory/'candidate_repeat.png')
        assert binding['design_sha256']==sha(directory/'design.json')
        assert binding['request_body_sha256']==sha(invocation/'request.json')
        for k,v in binding.items(): assert canonical(summary[k])==canonical(v),k
        png=(directory/'candidate.png').read_bytes()
        payload={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},
          'messages':[{'role':'system','content':constants['SYSTEM_PROMPT']},
                      {'role':'user','content':[{'type':'text','text':formal['question']},
                       {'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(png).decode('ascii')}}]}]}
        assert (invocation/'request.json').read_bytes()==json.dumps(payload,ensure_ascii=False).encode('utf-8')
        with Image.open(io.BytesIO(png)) as im:
            pixel=hashlib.sha256(b'768x768:RGBA:'+im.convert('RGBA').tobytes()).hexdigest()
            assert im.size==(768,768) and binding['pixel_sha256']==pixel
        assert design['created_at']<binding['created_at']
        runs=[]
        for i in (1,2):
            raw_path=invocation/f'run_{i:02d}_response.json'
            raw=load(raw_path)
            job=load(invocation/f'run_{i:02d}.json')
            started=load(invocation/f'run_{i:02d}_started.json')
            assert canonical(summary['results'][i-1])==canonical(job)
            for k,v in started.items(): assert canonical(job[k])==canonical(v)
            assert job['run_index']==i and job['http_status']==200 and job['status']=='completed'
            assert job['finish_reason']=='stop' and job['truncated'] is False
            assert job['response_sha256']==sha(raw_path)
            assert raw['model']==job['response_model']=='mimo-v2.6-flash'
            assert len(raw['choices'])==1 and raw['choices'][0]['finish_reason']=='stop'
            content=raw['choices'][0]['message']['content']
            assert content==job['answer'] and job['thinking']==''
            for key in ('image_sha256','design_sha256','request_body_sha256'): assert job[key]==binding[key]
            assert binding['created_at']<=started['started_at']<job['finished_at']
            gate=load(directory/'tests'/f'pre_network_run_{i:02d}.json')
            assert gate['request_index']==i and gate['source_frozen'] is True
            assert gate['request_body_sha256']==binding['request_body_sha256']
            assert gate['image_sha256']==binding['image_sha256'] and gate['design_sha256']==binding['design_sha256']
            assert gate['eligibility']['eligible'] is True
            runs.append({'run':i,'started_at':job['started_at'],'finished_at':job['finished_at'],
              'raw_path':str(raw_path),'raw_sha256':sha(raw_path),'characters':len(content),
              'finish_reason':'stop','truncated':False,'complete_answer':content,
              'raw_provider_created':raw.get('created'),'raw_provider_id':raw['id']})
        api=load(directory/'own_api_process.json')
        assert api['network_requests']==2 and api['status']=='harness_returned' and api['ended_at']
        evidence_hashes=load(directory/'evidence_hashes.json')['file_sha256']
        assert all(sha(directory/p)==h for p,h in evidence_hashes.items())
        manual=load(directory/'manual_final_review.json')
        all_trials.append({'variant_id':directory.name,'candidate_directory':str(directory),
          'PNG_sha256':sha(directory/'candidate.png'),'plugin_sha256':sha(directory/'plugin.json'),
          'design_sha256':sha(directory/'design.json'),'preset':design['expected_wrong_answer'],
          'summary_sha256':sha(invocation/'summary.json'),'request_sha256':sha(invocation/'request.json'),
          'binding_sha256':sha(invocation/'binding.json'),'design_snapshot_sha256':sha(invocation/'design_snapshot.json'),
          'frozen_at':design['created_at'],'binding_at':binding['created_at'],
          'exact_input_and_two_complete_raw_bindings':True,'saved_manual_review':manual,
          'runs':runs})
    assert len(all_trials)==12
    assert len({v['PNG_sha256'] for v in all_trials})==12
    assert len({v['request_sha256'] for v in all_trials})==12
    assert len(list((UNIT/'Solid166').rglob('*_started.json')))==24
    # No Python harness code is imported or executed in this transport audit.
    old=(OLD/'harness/quicktest3_isolated.py').read_text(encoding='utf-8')
    unit=(UNIT/'harness/quicktest3_isolated.py').read_text(encoding='utf-8')
    assert unit.replace("PROJECT = Path('C:\\\\Users\\\\lym\\\\Desktop\\\\Research\\\\MathPalette-publish')",
                        'PROJECT = Path(__file__).resolve().parents[3]')==old
    save('all_twelve_trial_transport_audit.json',{'checked_at':now(),'actual_complete_calls':24,
      'candidate_count':12,'distinct_PNGs':12,'distinct_requests':12,'no_new_calls':True,
      'no_hidden_third_call_in_saved_unit_evidence':True,'canonical_harness_only_project_path_difference':True,
      'claims_limited_to_saved_artifacts':True,'trials':all_trials})
    queue=load(UNIT/'second_review_queue.json')[0]
    last=all_trials[-1]
    assert queue['image_sha256']==last['PNG_sha256'] and queue['plugin_sha256']==last['plugin_sha256']
    assert queue['design_sha256']==last['design_sha256'] and queue['summary_sha256']==last['summary_sha256']
    assert [r['complete_answer'] for r in last['runs']]==[r['full_answer_text'] for r in queue['two_complete_final_answers']]
    save('candidate_transport_audit.json',last)
    print('All 12 distinct PNGs and all24 saved complete calls bind exactly; r12 queue/hash/request/raw/snapshot checks passed.')
    history=load(TASK/'history_index.json')
    scoped=next(q for q in history['questions'] if q['question_id']=='Solid166')
    compact=[]
    for d in scoped['designs']:
        compact.append({k:d.get(k) for k in ('directory','variant_id','predeclared_wrong_answer',
          'frozen_candidate_png_sha256','unique_started_call_count_from_saved_records','do_not_retest_this_frozen_png')})
    matches=[]
    for root in (TASK,OLD):
        for p in root.rglob('binding.json'):
            if p.is_relative_to(OWN): continue
            b=load(p)
            if b.get('image_sha256')==last['PNG_sha256']:
                matches.append({'path':str(p),'question_id':b.get('question_id'),'request_sha256':b.get('request_body_sha256')})
    assert len(matches)==1 and Path(matches[0]['path']).parent==Path(last['runs'][0]['raw_path']).parent
    read_manifest=load(UNIT/'read_source_manifest.json')
    old_checks={p:{'expected':v['sha256'],'actual':sha(PROJECT/p)} for p,v in read_manifest.items()}
    assert all(v['expected']==v['actual'] for v in old_checks.values())
    save('old_evidence_preservation.json',{'checked_at':now(),'checks':old_checks,'all_match':True,
          'candidate_hash_binding_matches':matches,'old_designs':compact,'old_history_index_sha256':sha(TASK/'history_index.json')})
    print('OLD DESIGN SUMMARY',canonical(compact))
    print('History raw/source/reference preservation checks',len(old_checks))
    for p in sorted((OLD/'background_03/solid_worker/Solid166').rglob('run_*_response.json')):
        print('OLD COMPLETE RAW',str(p),p.read_text(encoding='utf-8'))
    for p in sorted((UNIT/'Solid166').glob('r*/*manual_final*json')):
        data=load(p)
        if p.name=='manual_final_review.json':
            print('CURRENT OUTCOME',p.parent.name,canonical({k:v for k,v in data.items() if k not in ('reviews',)}))
    # The closest three predecessors are read in full, for comparison only.
    for name in ('r08_four_with_true_three_two','r10_three_with_true_one_four','r11_one_with_true_three_two'):
        d=UNIT/'Solid166'/name
        print('CLOSE PREDECESSOR PLUGIN',name,canonical(load(d/'plugin.json')))
        for p in sorted((d/'tests').rglob('run_*_response.json')):
            print('CLOSE PREDECESSOR COMPLETE RAW',name,p.name,p.read_text(encoding='utf-8'))

if __name__=='__main__': main(run)
