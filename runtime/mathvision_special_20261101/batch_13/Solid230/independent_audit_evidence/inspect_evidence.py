from review_env import *
import base64
import ast
from dataset_tools.catalog import content, digest, validate_formal_row

checks = {}
def check(name, value):
    checks[name] = bool(value)

record = next(r for r in rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id']=='Solid230')
approval = read(ROOT/'provenance/approvals.json')['approvals']['Solid230']
# Reconstruct the approved fingerprint independently, then cross-check catalog.
paths = [record[k] for k in ['image','original_image','script','scene'] if record.get(k)]
paths += record.get('runtime_dependencies', []) + ['dataset_generator/common_renderer.py','dataset_generator/protocol.json']
approved_payload = {'branch':'SolidGeometry', 'record':record,
    'files':{p:fh(ROOT/'SolidGeometry'/p) for p in paths},
    'source_notes':read(ROOT/'provenance/source_notes.json').get('Solid230',{})}
approved_payload['files']['../dataset_tools/geometry_dataset.py'] = fh(ROOT/'dataset_tools/geometry_dataset.py')
actual_approval = canonical(approved_payload)
check('independent_approval_fingerprint_matches', actual_approval == approval['content_sha256'])
check('catalog_and_independent_fingerprint_match', actual_approval == digest(content(ROOT,'SolidGeometry',record)))
validate_formal_row(ROOT,'SolidGeometry',record)
special = {}
for name in ['accepted_index.jsonl','collected_index.jsonl']:
    p = ROOT/'SolidGeometry/special_variant'/name
    special[name] = {'path':str(p), 'sha256':fh(p), 'matching_rows':[r for r in rows(p) if r.get('id',r.get('question_id'))=='Solid230']}
for name in ['recipes.json','collection.json']:
    p = ROOT/'SolidGeometry/special_variant/Solid230'/name
    special[name] = {'path':str(p), 'exists':p.exists(), 'content':read(p) if p.exists() else None}
delivered = [str(p) for p in SHARED.glob('batch_*/manifest.json') if 'Solid230' in p.read_text(encoding='utf-8-sig')]
bank = next(r for r in rows(ROOT/'question_bank.jsonl') if r['id']=='Solid230')
eligible = (record['source_dataset']=='MathVision' and approval['reviewer']=='user' and bool(approval['instruction'])
    and actual_approval==approval['content_sha256'] and not any(special[n]['matching_rows'] for n in ['accepted_index.jsonl','collected_index.jsonl'])
    and not any(special[n]['exists'] for n in ['recipes.json','collection.json']) and not delivered and not bank.get('special_plugins'))
check('currently_eligible', eligible)
write('eligibility_current.json', {'at':now(),'question_id':'Solid230','eligible':eligible,'record':record,'approval':approval,
    'fingerprint_payload':approved_payload,'independently_computed_content_sha256':actual_approval,
    'formal_record_canonical_sha256':canonical(record),'special':special,'delivered_manifests':delivered,
    'derived_question_bank_record':bank,'mutable_progress_is_diagnostic_only':True})

design, binding, summary, request, freeze = [read(p) for p in [CAND/'design.json',TEST/'binding.json',TEST/'summary.json',TEST/'request.json',CAND/'pretest_freeze.json']]
reference_path = ROOT/'SolidGeometry/workbench/quick_test.py'
tree = ast.parse(reference_path.read_text(encoding='utf-8-sig'))
reference = {}
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ['SYSTEM_PROMPT','TEST_PROFILES','MIMO_API_BASE']:
                reference[target.id] = ast.literal_eval(node.value)
profile = {**reference['TEST_PROFILES']['quicktest3'], 'api_base':read(ROOT/'SolidGeometry/workbench/config.json')['quick_test']['mimo_api_base']}
expected_request = {'model':profile['model'],'stream':False,'thinking':profile['thinking'],
    'messages':[{'role':'system','content':reference['SYSTEM_PROMPT']},
    {'role':'user','content':[{'type':'text','text':record['question']},
    {'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode((CAND/'candidate.png').read_bytes()).decode('ascii')}}]}]}
check('request_exactly_formal_question_and_candidate_with_original_system', request==expected_request)
check('request_exact_original_serialization', (TEST/'request.json').read_bytes()==json.dumps(expected_request,ensure_ascii=False).encode('utf-8'))
check('no_choices_in_formal_number_question', record['answer_type']=='number' and 'choices' not in record)
source=read(ROOT/'SolidGeometry'/record['runtime_dependencies'][3])
check('source_question_only_image_token_removed', source['question'].replace('<image1>','').strip()==record['question'] and source['options']==[] and source['answer']==record['answer'])
check('profile_original_mimo_disabled', binding['settings']==profile and binding['profile']=='quicktest3' and binding['reference_quick_test_sha256']==fh(reference_path))
check('binding_dataset',binding['dataset_sha256']==fh(ROOT/'SolidGeometry/dataset.jsonl'))
check('binding_formal_record', binding['question_record_sha256']==canonical(record))
check('binding_request', binding['request_body_sha256']==fh(TEST/'request.json'))
check('binding_image', binding['image_sha256']==fh(CAND/'candidate.png') and Path(binding['image_path']).resolve()==(CAND/'candidate.png').resolve())
check('binding_design_and_snapshot', binding['design_sha256']==fh(CAND/'design.json')==fh(TEST/'design_snapshot.json') and Path(binding['design_path']).resolve()==(CAND/'design.json').resolve())
check('preset_42_frozen', str(design['expected_wrong_answer'])==str(binding['expected_wrong_answer'])==str(freeze['expected_wrong_answer'])=='42')
check('all_pretest_hashes', all(fh(CAND/p)==v for p,v in freeze['files'].items()))
frozen = read(SHARED/'background_37/Solid230/frozen_inputs.json')
frozen_checks={p:{'recorded':v,'current':fh(ROOT/p),'matches':fh(ROOT/p)==v} for p,v in frozen['files'].items()}
check('all_original_frozen_dependencies_match', all(x['matches'] for x in frozen_checks.values()))
check('parent_and_candidate_context_byte_equal', fh(SHARED/'background_37/Solid230/context.json')==fh(CAND/'context.json'))
runs=[]
for i in [1,2]:
    prefix='run_'+str(i).zfill(2)
    start,run,raw=[read(TEST/(prefix+s)) for s in ['_started.json','.json','_response.json']]
    for name in ['run_index','run_id','started_at','request_body_sha256','image_sha256','design_sha256']:
        check(prefix+'_'+name,run[name]==start[name])
    for field, value in [('request_body_sha256',fh(TEST/'request.json')),('image_sha256',fh(CAND/'candidate.png')),('design_sha256',fh(CAND/'design.json'))]:
        check(prefix+'_bound_'+field,run[field]==value)
    check(prefix+'_raw_response_hash',run['response_sha256']==fh(TEST/(prefix+'_response.json')))
    choice=raw['choices'][0]
    final=choice['message']['content']
    check(prefix+'_complete',len(raw['choices'])==1 and run['http_status']==200 and run['status']=='completed' and not run['truncated'] and run['finish_reason']==choice['finish_reason']=='stop')
    check(prefix+'_raw_and_saved_answer_identical',run['answer']==final and summary['results'][i-1]==run)
    check(prefix+'_model',raw['model']==run['response_model']==profile['model'])
    check(prefix+'_no_reasoning_tokens',raw['usage']['completion_tokens_details']['reasoning_tokens']==0 and run['thinking']=='')
    check(prefix+'_final_42',final.rstrip().endswith('**42**.'))
    check(prefix+'_both_ones_counted_and_middle_right_five',('Top face: 1 dot' in final or 'Top face shows 1' in final) and ('Right face: 1 dot' in final or 'Right face shows 1' in final) and ('Right face: 5 dots' in final or 'Right face shows 5' in final))
    runs.append({'run_index':i,'run_id':run['run_id'],'response_id':raw['id'],'started_at':run['started_at'],'finished_at':run['finished_at'],
        'http_status':run['http_status'],'finish_reason':run['finish_reason'],'truncated':run['truncated'],
        'complete_final_answer_text':final,'extracted_final_number':'42','option_letter':None,
        'raw_response_sha256':fh(TEST/(prefix+'_response.json')),'run_sha256':fh(TEST/(prefix+'.json')),'started_sha256':fh(TEST/(prefix+'_started.json')),
        'actual_error':'Both real 1 faces explicitly counted; unmarked middle-right 6 misread as 5. Frozen equal-value collapse is not supported.'})
check('distinct_independent_run_and_response_ids',runs[0]['run_id']!=runs[1]['run_id'] and runs[0]['response_id']!=runs[1]['response_id'])
check('summary_full_binding_consistent', all(summary[k]==v for k,v in binding.items()) and summary['two_completed'] and len(summary['results'])==2)
times = [design['created_at'], freeze['created_at'],read(CAND/'eligibility_immediately_before_calls.json')['checked_at'],binding['created_at'],runs[0]['started_at'],runs[0]['finished_at'],runs[1]['started_at'],runs[1]['finished_at']]
check('chronology', times==sorted(times))
check('exactly_two_no_extra_started_or_raw_in_this_variant',len(list(TEST.glob('run_*_started.json')))==2 and len(list(TEST.glob('run_*_response.json')))==2 and len(list((CAND/'tests').iterdir()))==1)
manual=read(CAND/'manual_final_review.json')
check('manual_transcripts_match_raw',all(x['complete_raw_final_answer_text']==runs[i]['complete_final_answer_text'] for i,x in enumerate(manual['manual_results'])))
write('evidence_audit.json', {'at':now(),'pid':os.getpid(),'checks':checks,'all_checks_pass':all(checks.values()),'source_question_and_options':source,
    'original_profile_and_system':reference,'bound_profile':profile,'chronology':times,
    'request_keys':list(request),'input_payload_description':'Exactly original system + formal question + same candidate data URL. No answer, intent, design, original/control image, or history in request.',
    'design_sha256':fh(CAND/'design.json'),'plugin_sha256':fh(CAND/'plugin.json'),'candidate_sha256':fh(CAND/'candidate.png'),
    'binding_sha256':fh(TEST/'binding.json'),'request_sha256':fh(TEST/'request.json'),'summary_sha256':fh(TEST/'summary.json'),
    'design_snapshot_sha256':fh(TEST/'design_snapshot.json'),'pretest_freeze_sha256':fh(CAND/'pretest_freeze.json'),
    'all_frozen_dependencies':frozen_checks,'runs':runs,
    'evidence_scope':'Two separate completed recorded HTTP calls to original profile. No new API/control/retry. Local artifacts checked directly; parent precheck not substituted.'})
print(json.dumps({'all_checks_pass':all(checks.values()),'failed_checks':[k for k,v in checks.items() if not v], 'eligible':eligible,'approval_sha256':actual_approval,'evidence_pid':os.getpid()}))

# Read old histories and exact primary objections; display focused original nodes.
def find_nodes(value, predicate, pointer='$'):
    found=[]
    if isinstance(value,dict):
        if predicate(value):
            found.append({'pointer':pointer,'content':value})
        else:
            for k,v in value.items():
                if k=='Solid230':found.append({'pointer':pointer+'.'+k,'content':v})
                else:found+=find_nodes(v,predicate,pointer+'.'+k)
    elif isinstance(value,list):
        for i,v in enumerate(value):found+=find_nodes(v,predicate,pointer+'['+str(i)+']')
    return found
history={}
for path in [SHARED/'background_13/checkpoint.json', SHARED/'background_37/old_history_audit.json', SHARED/'background_37/checkpoint.json', SHARED/'background_37/second_review_queue.json', SHARED/'background_37/independent_primary_math_audit.json']:
    obj=read(path)
    history[rel(path)]=find_nodes(obj,lambda d:d.get('question_id',d.get('id'))=='Solid230')
write('history_primary_exact_excerpts.json',history)
for name, nodes in history.items():
    print('HISTORY '+name)
    if 'checkpoint' in name or 'queue' in name:
        for node in nodes:
            content=node['content']
            if isinstance(content,dict):
                keep={k:v for k,v in content.items() if k not in ['eligibility_current','raw_binding_audit','details','raw_evidence','pretest_freeze','frozen_inputs','inputs','eligibility_at_start']}
                print(json.dumps({'pointer':node['pointer'],'content':keep},ensure_ascii=False))
    else:print(json.dumps(nodes,ensure_ascii=False))
