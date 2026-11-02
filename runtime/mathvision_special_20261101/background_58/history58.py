from env58 import *
import base64
import gc

manifest = read(OWN/'old_history_manifest.json')
for qid in QIDS + RELATED:
    report = {'question_id':qid,'created_at':now(),'files':[], 'full_raw_responses':[], 'designs':[], 'plugins':[], 'assessments':[]}
    for entry in manifest[qid]:
        p = PROJECT / entry['path']
        check = {'path':str(p),'sha256':sha(p),'hash_matches_inventory':sha(p)==entry['sha256']}
        assert check['hash_matches_inventory']
        if p.suffix.lower()=='.json':
            try:
                data = read(p)
                check['full_UTF8_JSON_read']=True
                if p.name.endswith('_response.json') and isinstance(data,dict) and data.get('choices'):
                    messages = [{'finish_reason':v.get('finish_reason'), 'message':v.get('message')} for v in data['choices']]
                    report['full_raw_responses'].append({'path':str(p),'sha256':check['sha256'],'choices':messages})
                elif p.name in ('design.json','design_snapshot.json'):
                    report['designs'].append({'path':str(p),'sha256':check['sha256'],'value':data})
                elif p.name in ('plugin.json','plugin_input.json'):
                    report['plugins'].append({'path':str(p),'sha256':check['sha256'],'value':data})
                elif p.name in ('assessment.json','prescreen.json','prescreen_assessment.json','primary_rejection.json',
                                'manual_final_review.json','primary_review.json','primary_visual_review.json','design_difference_audit.json',
                                'refinement_result.json','history_audit.json','exact_route_math.json'):
                    report['assessments'].append({'path':str(p),'sha256':check['sha256'],'value':data})
                del data
            except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                check['malformed_preserved']=str(exc)
        report['files'].append(check)
    save(f'history_reads/{qid}.json',report)
    print(qid, len(report['files']), 'full files; raw responses',len(report['full_raw_responses']),flush=True)
    del report
    gc.collect()

# Whole task binding search supplements the path-based inventory. No raw bodies retained.
found=[]
for p in BASE.rglob('binding.json'):
    if p.is_relative_to(OWN): continue
    data=read(p)
    qid=data.get('question_id')
    if qid in QIDS + RELATED:
        request_path=p.parent/'request.json'
        body=request_path.read_bytes()
        request=json.loads(body)
        user=request['messages'][1]['content']
        png=base64.b64decode(user[1]['image_url']['url'].split(',',1)[1])
        check={'path':str(p),'sha256':sha(p),'question_id':qid,'preset':data.get('expected_wrong_answer'),
            'request_sha256':hashlib.sha256(body).hexdigest(), 'request_hash_matches':hashlib.sha256(body).hexdigest()==data['request_body_sha256'],
            'png_sha256':hashlib.sha256(png).hexdigest(), 'PNG_matches_binding':hashlib.sha256(png).hexdigest()==data['image_sha256'],
            'only_formal_question_and_candidatePNG':user[0]['text']==row(qid)['question'] and len(user)==2,
            'remote_profile':{k:request.get(k) for k in ('model','thinking','stream')},
            'request_top_fields':list(request), 'started_files':[str(f) for f in p.parent.glob('run_*_started.json')]}
        assert check['request_hash_matches'] and check['PNG_matches_binding'] and check['only_formal_question_and_candidatePNG']
        found.append(check)
        del body,request,user,png
    del data
save('whole_task_old_bindings.json',found)
print('whole task relevant bindings',len(found),flush=True)
