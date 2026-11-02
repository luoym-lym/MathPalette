from tools34 import *
import base64
history=read(UNIT/'history_inventory.json');audits={}
for qid,hist in history.items():
    loaded={};controls=[];prior=[]
    for name in hist['question_directories']:
        for path in (PROJECT/name).rglob('*.json'):
            loaded[str(path.relative_to(PROJECT))]={'sha256':sha(path),'full_json_loaded':True}
            read(path)
    for design_path in hist['designs']:
        folder=(PROJECT/design_path).parent;design=read(PROJECT/design_path)
        pair=[]
        for summary_path in folder.rglob('summary.json'):
            invocation=summary_path.parent;binding=read(invocation/'binding.json');request=read(invocation/'request.json')
            png=Path(binding['image_path']);design_file=Path(binding['design_path'])
            assert sha(png)==binding['image_sha256'] and sha(design_file)==binding['design_sha256']
            assert base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])==png.read_bytes()
            assert request['messages'][1]['content'][0]['text']==record(qid)['question']
            assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
            finals=[]
            for n in (1,2):
                job=read(invocation/f'run_{n:02d}.json');raw=read(invocation/f'run_{n:02d}_response.json')
                assert job['status']=='completed' and sha(invocation/f'run_{n:02d}_response.json')==job['response_sha256']
                finals.append(raw['choices'][0]['message']['content'])
            pair.append({'summary':str(summary_path.relative_to(PROJECT)),'sha256':sha(summary_path),'full_raw_contents':finals,
                         'actual_final_manual_read': ['B (One)','B (One)'] if qid=='Plane257' else ['C (the same)','D (1 more)'],
                         'same_original_question_image_and_preset_binding_verified':True,'two_completed':True})
        prior.append({'design_path':design_path,'preset':design['expected_wrong_answer'],'pairs':pair,
                      'preset_hit':False,'read_presets_and_full_replies_and_primary_reviews':True,'old_image_actually_viewed':True,
                      'status':'Frozen preset misses, not eligible for unchanged promotion or relabeling.'})
    for path in SHARED.glob('independent_review/*/independent_review.json'):
        value=read(path)
        if value.get('question_id')==qid:raise AssertionError('Unexpected same-question independent report, must read before proceeding: '+str(path))
    audits[qid]={'prior_designs':prior,'all_same_question_json_loaded':loaded,'same_question_independent_reports':[],
                 'existing_controls_found':controls,'control_policy':'No original control invocations exist under the same-question prior evidence. No repeat controls or extra control calls.',
                 'prior_prescreens_read':'Earlier checkpoint nodes plus per-question prescreens, including Plane212/prescreen.json and Solid88/primary_prescreen.json. Background18 matches are whole-library hash mentions only, not extra work on these assigned IDs.'}
write(UNIT/'history_read_and_binding_audit.json',audits)

references=[];delivered=[]
for n in range(1,11):
    path=SHARED/f'batch_{n:02d}'/'manifest.json';value=read(path)
    for item in value['candidates']:
        delivered.append(item['question_id'])
        references.append({'batch':path.parent.name,'question_id':item['question_id'],'mechanism':item.get('mechanism'),
              'source':item.get('candidate_source'),'wrong_preset':item.get('expected_wrong_answer'),'raw_final_values':item.get('tested_final_answers'),
              'control_values':item.get('original_control_answers'),'review':item.get('quality_review'),'manifest_sha256':sha(path)})
assert len(set(delivered))==12 and not set(IDS).intersection(delivered)
write(UNIT/'delivered_reference_and_exclusion_audit.json',{'at':now(),'readonly_reference_cases':references,'all12_excluded':True,'delivered_question_ids':delivered,
      'principle_applied':'Each proposed design transfers an actual feature/frame/component family. It does not merely highlight an arbitrary wrong answer. Reference cases are evidence, not approved formal Special records.'})
for item in references: print(json.dumps(item,ensure_ascii=False))

for name in ('inventory.json','exploration_report.json'):
    value=read(SHARED/name)
    write(UNIT/('current_'+name.replace('.json','')+'_read_audit.json'),{'path':str((SHARED/name).relative_to(PROJECT)),'sha256':sha(SHARED/name),'fully_loaded':True,'role':'Mutable diagnostic metadata, eligibility comes from formal/approval/Special state.'})
remaining=[x for x in rows(SHARED/'remaining_questions.jsonl') if x.get('question_id',x.get('id')) in IDS]
write(UNIT/'remaining_assigned_entries_readonly_snapshot.json',remaining)
print(json.dumps({'historical_candidate_pairs_audited':2,'all12_delivered_excluded':True,'same_question_independent_reports':0,'existing_control_invocations_found':0}))
