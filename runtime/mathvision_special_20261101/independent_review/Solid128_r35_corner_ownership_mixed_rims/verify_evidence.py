from audit_bootstrap import *
import ast
import base64
import copy
from dataset_tools import catalog

def rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()] if Path(path).exists() else []

checks = {}
def check(name, condition):
    checks[name] = bool(condition)

branch = ROOT / 'SolidGeometry'
records = [r for r in rows(branch/'dataset.jsonl') if r.get('id') == 'Solid128']
assert len(records) == 1
record = records[0]
approval = read(ROOT/'provenance/approvals.json')['approvals'].get('Solid128')
content_hash = catalog.digest(catalog.content(ROOT,'SolidGeometry',record))
indexes = {}
for name in ['accepted_index.jsonl', 'collected_index.jsonl']:
    p = branch/'special_variant'/name
    indexes[name]={'path':str(p),'sha256':sha(p),'matching_records':[r for r in rows(p) if r.get('question_id',r.get('id')) == 'Solid128']}
special = {}
for name in ['recipes.json','collection.json']:
    p = branch/'special_variant/Solid128'/name
    special[name]={'path':str(p),'exists':p.exists(),'sha256':sha(p) if p.is_file() else None,'data':read(p) if p.is_file() else None}
batch_matches=[str(p.relative_to(ROOT)) for p in BASE.glob('batch_*/manifest.json') if 'Solid128' in p.read_text(encoding='utf-8-sig')]
eligible = (record['source_dataset']=='MathVision' and approval['reviewer']=='user' and bool(approval['instruction']) and bool(approval['approved_at_utc']) and approval['content_sha256']==content_hash and not any(x['matching_records'] for x in indexes.values()) and not any(x['exists'] for x in special.values()) and not batch_matches)
write('authoritative_eligibility.json',{'checked_at':now(),'eligible':eligible,'formal_record':record,'formal_dataset_sha256':sha(branch/'dataset.jsonl'),'formal_question_record_canonical_sha256':canonical_hash(record),'original_approval':approval,'approvals_file_sha256':sha(ROOT/'provenance/approvals.json'),'recomputed_original_content_sha256':content_hash,'approval_fingerprint_matches':content_hash==approval['content_sha256'],'indexes':indexes,'recipes_and_collection_including_special_completion':special,'published_batch_manifest_matches':batch_matches,'authority':'Current formal branch dataset, approval, accepted/collected indexes and per-question recipes/collection; historical inventory is diagnostic only'})
check('current_authoritative_eligibility',eligible)

binding = read(TEST/'binding.json')
design = read(CANDIDATE/'design.json')
primary = read(CANDIDATE/'primary_review.json')
request = read(TEST/'request.json')
frozen = read(QUESTION/'input_fingerprints.json')
hashes = {p: {'recorded':h,'actual':sha(ROOT/p),'equal':sha(ROOT/p)==h} for p,h in frozen['files'].items()}
check('all_formal_source_protocol_renderer_input_hashes',all(x['equal'] for x in hashes.values()))
check('current_record_matches_frozen_record',canonical_hash(record)==frozen['question_record_sha256']==binding['question_record_sha256'])
check('formal_record_snapshot_semantic_equal',record==read(QUESTION/'formal_record.json'))
check('current_scene_matches_frozen_snapshot',read(branch/record['scene'])==read(QUESTION/'scene_snapshot.json'))
check('candidate_context_snapshot_byte_equal',(QUESTION/'context.json').read_bytes()==(CANDIDATE/'context.json').read_bytes())
check('current_source_notes_match_snapshot',read(ROOT/'provenance/source_notes.json')['Solid128']==read(QUESTION/'source_notes.json'))
check('formal_source_and_png_copies_equal',(QUESTION/'source_original.jpg').read_bytes()==(branch/record['original_image']).read_bytes() and (QUESTION/'original.png').read_bytes()==(branch/record['image']).read_bytes())
check('design_snapshot_byte_equal',(TEST/'design_snapshot.json').read_bytes()==(CANDIDATE/'design.json').read_bytes())
check('same_frozen_preset_81',design['expected_wrong_answer']==binding['expected_wrong_answer']==read(TEST/'design_snapshot.json')['expected_wrong_answer']=='81')
check('image_design_plugin_difference_hashes_bound',sha(CANDIDATE/'candidate.png')==design['png_sha256']==primary['image_sha256']==binding['image_sha256'] and sha(CANDIDATE/'design.json')==primary['design_sha256']==binding['design_sha256'] and sha(CANDIDATE/'plugin.json')==design['plugin_sha256']==primary['plugin_sha256'] and sha(CANDIDATE/'design_difference_audit.json')==design['design_difference_audit_sha256']==primary['difference_audit_sha256'])
check('dataset_binding_matches_current',sha(branch/'dataset.jsonl')==binding['dataset_sha256'])
check('raw_request_sha256_binding',sha(TEST/'request.json')==binding['request_body_sha256'])
check('request_exact_keys_no_overrides',set(request)=={'model','stream','thinking','messages'})
check('request_mimo_nonstream_thinking_disabled',request['model']=='mimo-v2.6-flash' and request['stream'] is False and request['thinking']=={'type':'disabled'})
msgs=request['messages']; content=msgs[1]['content']
check('request_only_standard_system_and_formal_question_png',len(msgs)==2 and msgs[0]=={'role':'system','content':binding['system_prompt']} and set(msgs[1])=={'role','content'} and msgs[1]['role']=='user' and len(content)==2 and content[0]=={'type':'text','text':record['question']} and set(content[1])=={'type','image_url'} and set(content[1]['image_url'])=={'url'})
imagebytes=base64.b64decode(content[1]['image_url']['url'].split(',',1)[1],validate=True)
check('base64_payload_exact_frozen_candidate_png',content[1]['image_url']['url'].startswith('data:image/png;base64,') and imagebytes==(CANDIDATE/'candidate.png').read_bytes())

quicktest_path=branch/'workbench/quick_test.py'
source=quicktest_path.read_text(encoding='utf-8-sig')
assignments={}
for node in ast.parse(source).body:
    if isinstance(node,ast.Assign):
        for target in node.targets:
            if isinstance(target,ast.Name) and target.id in ['TEST_PROFILES','SYSTEM_PROMPT','MIMO_API_BASE']:
                try: assignments[target.id]=ast.literal_eval(node.value)
                except (ValueError,TypeError): pass
check('reference_quick_test_code_hash_unchanged',sha(quicktest_path)==binding['reference_quick_test_sha256'])
check('system_prompt_matches_reference_code',assignments['SYSTEM_PROMPT']==binding['system_prompt'])
profile=assignments['TEST_PROFILES']['quicktest3']
check('profile_matches_reference_code',all(binding['settings'][k]==v for k,v in profile.items()))
check('endpoint_matches_config',binding['settings']['api_base']==read(branch/'workbench/config.json')['quick_test']['mimo_api_base'])
harness = BASE/'harness/quicktest3_isolated.py'
hi=read(CANDIDATE/'harness_isolation_audit.json')
hsource=harness.read_text(encoding='utf-8-sig')
check('harness_full_and_core_hash_match',sha(harness)==hi['reference_sha256'] and hashlib.sha256(hsource[hsource.index('def timestamp():'):].encode()).hexdigest()==hi['unchanged_core_from_def_timestamp_sha256'])

evidence = []
run_ids=[]; response_ids=[]
for i in (1,2):
    stem=f'run_{i:02d}'
    run=read(TEST/(stem+'.json')); start=read(TEST/(stem+'_started.json')); raw=read(TEST/(stem+'_response.json'))
    choice=raw['choices'][0]; answer=choice['message']['content']
    check(stem+'_complete_raw_record_matches',run['status']=='completed' and run['http_status']==200 and run['finish_reason']==choice['finish_reason']=='stop' and run['truncated'] is False and run['thinking']=='' and run['answer']==answer and run['response_model']==raw['model']=='mimo-v2.6-flash' and run['usage']==raw['usage'] and len(raw['choices'])==1)
    check(stem+'_exact_raw_response_hash',run['response_sha256']==sha(TEST/(stem+'_response.json')))
    check(stem+'_started_record_unmodified_subset',all(run.get(k)==v for k,v in start.items()))
    check(stem+'_request_image_design_bindings',run['request_body_sha256']==binding['request_body_sha256'] and run['image_sha256']==binding['image_sha256'] and run['design_sha256']==binding['design_sha256'])
    check(stem+'_zero_reasoning_tokens',raw['usage']['completion_tokens_details']['reasoning_tokens']==0)
    check(stem+'_provider_created_between_start_finish',datetime.datetime.fromisoformat(run['started_at']).timestamp() <= raw['created'] <= datetime.datetime.fromisoformat(run['finished_at']).timestamp())
    evidence.append({'run_index':i,'run_id':run['run_id'],'provider_response_id':raw['id'],'provider_created':raw['created'],'started_at':run['started_at'],'finished_at':run['finished_at'],'http_status':run['http_status'],'finish_reason':choice['finish_reason'],'full_raw_response_path':str(TEST/(stem+'_response.json')),'full_raw_response_sha256':sha(TEST/(stem+'_response.json')),'run_record_sha256':sha(TEST/(stem+'.json')),'full_assistant_content_exact':answer,'full_content_characters':len(answer),'actual_newline_count':answer.count('\n'),'literal_backslash_n_count':answer.count('\\n'),'manually_read_entire_content':True,'manual_final_value':'81','manual_terminal_text':'**Answer:**\n**81** cubes are needed to completely fill the square area.' if i==1 else '**Answer:** 81 cubes are needed to completely fill the square area.','preset_match':True,'contradictory_final_letter_or_value':False,'usage':raw['usage'],'narrative_assessment':'Uses 36=4n (or 4s), divides by four to obtain 9, and then squares 9. Treats a corner-allocation/centerline count as the inside side length. This is the predeclared mathematical error. Does not explicitly refer to red ink or assert that color is a given equality.'})
    run_ids.append(run['run_id']); response_ids.append(raw['id'])
check('two_distinct_calls',len(set(run_ids))==len(set(response_ids))==2)
summary=read(TEST/'summary.json')
check('summary_binds_all_source_and_run_records',summary['two_completed'] is True and summary['requested_runs']==2 and summary['results']==[read(TEST/'run_01.json'),read(TEST/'run_02.json')] and all(summary[k]==v for k,v in binding.items()))
check('exactly_two_run_records_and_two_raw_responses_in_candidate',sorted(p.name for p in TEST.glob('run_??.json'))==['run_01.json','run_02.json'] and sorted(p.name for p in TEST.glob('run_??_response.json'))==['run_01_response.json','run_02_response.json'] and len(list((CANDIDATE/'tests').glob('quicktest3_*')))==1)
all_bindings=[]
for p in BASE.rglob('binding.json'):
    if p.is_relative_to(OWN): continue
    try:
        if read(p).get('question_id')=='Solid128': all_bindings.append(str(p.relative_to(ROOT)))
    except (ValueError,OSError): pass
all_raw_responses=[str(p.relative_to(ROOT)) for p in BASE.rglob('run_*_response.json') if 'Solid128' in p.parts and not p.is_relative_to(OWN)]
check('no_other_Solid128_binding_or_raw_response_in_available_runtime',all_bindings==[str((TEST/'binding.json').relative_to(ROOT))] and len(all_raw_responses)==2)
chronology={'difference_declared':read(CANDIDATE/'design_difference_audit.json')['created_at'],'design_created':design['created_at'],'primary_created':primary['created_at'],'binding_created':binding['created_at'],'run_1_started':evidence[0]['started_at'],'run_1_finished':evidence[0]['finished_at'],'run_2_started':evidence[1]['started_at'],'run_2_finished':evidence[1]['finished_at']}
times=[datetime.datetime.fromisoformat(t) for t in chronology.values()]
check('preset_design_primary_before_calls_and_calls_sequential',times==sorted(times))
check('preset_design_plugin_image_mtime_before_first_call',all(datetime.datetime.fromtimestamp((CANDIDATE/p).stat().st_mtime,datetime.timezone.utc) < times[4] for p in ['design.json','plugin.json','candidate.png','primary_review.json','design_difference_audit.json']))
old=BASE/'background_15/Solid128'
check('old_formal_and_scene_semantics_equal_current',read(old/'formal_record.json')==record and read(old/'source_scene_snapshot.json')==read(branch/record['scene']))
oldhashes=read(old/'frozen_inputs.json')['files']
old_file_checks={p:{'recorded':h,'actual':sha(ROOT/p),'equal':sha(ROOT/p)==h} for p,h in oldhashes.items()}
old_files=list(old.rglob('*'))
check('old_prescreen_has_no_saved_plugin_candidate_test',not any(p.is_file() and (p.name=='candidate.png' or 'plugin' in p.name or p.name.startswith('run_')) for p in old_files))
history=read(BASE/'background_35/history_read_audit.json')
old_manifest=next(x for x in history['all_previous_same_question_files_read_in_full'] if x['question_id']=='Solid128')
check('all_historical_Solid128_evidence_hashes_unchanged',all(sha(ROOT/x['path'])==x['sha256'] for x in old_manifest['old_files']))

files={str(p.relative_to(ROOT)): {'sha256':sha(p),'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat(),'bytes':p.stat().st_size} for p in sorted(TEST.iterdir()) if p.is_file()}
for p in [CANDIDATE/'design.json',CANDIDATE/'plugin.json',CANDIDATE/'candidate.png',CANDIDATE/'primary_review.json',CANDIDATE/'design_difference_audit.json',harness,quicktest_path,BASE/'background_35/run35.py',BASE/'background_35/tools35.py',old/'primary_prescreen.json']:
    files[str(p.relative_to(ROOT))]={'sha256':sha(p),'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat(),'bytes':p.stat().st_size}
result={'checked_at':now(),'checks':checks,'all_checks_passed':all(checks.values()),'failed_checks':[k for k,v in checks.items() if not v],'frozen_input_hash_checks':hashes,'historical_input_hash_checks':old_file_checks,'raw_evidence_and_design_files':files,'chronology_utc':chronology,'request_structure_without_redundant_base64':{'keys':sorted(request),'model':request['model'],'stream':request['stream'],'thinking':request['thinking'],'system':msgs[0]['content'],'user_text':content[0]['text'],'decoded_png_bytes':len(imagebytes),'decoded_png_sha256':hashlib.sha256(imagebytes).hexdigest()},'all_available_Solid128_bindings':all_bindings,'all_available_Solid128_raw_responses':all_raw_responses,'complete_manually_read_responses':evidence,'scope_limit':'Audit of available immutable local request/response evidence and harness, without provider-side transport logs. No new solver or control call; no causal/statistical claim. Cached input tokens on run 2 do not mean the first assistant answer was included in the request.'}
write('evidence_audit.json',result)
print(json.dumps({'checks':checks,'failed_checks':result['failed_checks'],'chronology':chronology,'raw_content_lengths':[e['full_content_characters'] for e in evidence],'raw_actual_newlines':[e['actual_newline_count'] for e in evidence],'old_hash_differences':[p for p,v in old_file_checks.items() if not v['equal']]},ensure_ascii=False,indent=2))
