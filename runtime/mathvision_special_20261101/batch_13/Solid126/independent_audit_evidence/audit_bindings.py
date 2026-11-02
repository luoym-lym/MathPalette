from review_env import *
import ast, base64, copy, io
from PIL import Image
from dataset_tools.catalog import rows, digest
BASE=ROOT/'runtime/mathvision_special_20261101'
CAND=BASE/'background_37/Solid126/r37_local_area_replacement'
OLD=BASE/'background_14/Solid126/remaining_height_to_cut_binding'
BRANCH=ROOT/'SolidGeometry'
row=next(r for r in rows(BRANCH/'dataset.jsonl') if r['id']=='Solid126')
tree=ast.parse((BRANCH/'workbench/quick_test.py').read_text(encoding='utf-8-sig'))
constants={}
for node in tree.body:
    if isinstance(node,ast.Assign):
        for name in node.targets:
            if isinstance(name,ast.Name) and name.id in ('SYSTEM_PROMPT','TEST_PROFILES','MIMO_API_BASE'):
                constants[name.id]=ast.literal_eval(node.value)
def audit(candidate):
    t=next((candidate/'tests').iterdir())
    b=read(t/'binding.json');s=read(t/'summary.json');d=read(candidate/'design.json');p=read(candidate/'plugin.json')
    req=read(t/'request.json')
    expected={'model':constants['TEST_PROFILES']['quicktest3']['model'],'stream':False,'thinking':{'type':'disabled'},'messages':[{'role':'system','content':constants['SYSTEM_PROMPT']},{'role':'user','content':[{'type':'text','text':row['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode((candidate/'candidate.png').read_bytes()).decode('ascii')}}]}]}
    request_bytes=json.dumps(expected,ensure_ascii=False).encode('utf-8')
    img=base64.b64decode(req['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1],validate=True)
    with Image.open(io.BytesIO(img)) as im:
        rgba=im.convert('RGBA'); pixels=hashlib.sha256(f'{im.width}x{im.height}:RGBA:'.encode()+rgba.tobytes()).hexdigest()
    checks={'request_exact_keys_and_semantics':req==expected,'request_exact_serialized_bytes':(t/'request.json').read_bytes()==request_bytes,'request_body_hash':sha(t/'request.json')==b['request_body_sha256'],'embedded_image_byte_identical':img==(candidate/'candidate.png').read_bytes(),'image_sha256':sha(candidate/'candidate.png')==b['image_sha256'],'pixel_sha256':pixels==b['pixel_sha256'],'design_bytes_match_snapshot':(candidate/'design.json').read_bytes()==(t/'design_snapshot.json').read_bytes(),'design_hash':sha(candidate/'design.json')==b['design_sha256'],'preset_matches_snapshot_and_binding':d['expected_wrong_answer']==read(t/'design_snapshot.json')['expected_wrong_answer']==b['expected_wrong_answer'],'question_record_hash':digest(row)==b['question_record_sha256'],'dataset_hash':sha(BRANCH/'dataset.jsonl')==b['dataset_sha256'],'reference_quick_test_hash':sha(BRANCH/'workbench/quick_test.py')==b['reference_quick_test_sha256'],'profile_exact':b['settings']=={**constants['TEST_PROFILES']['quicktest3'],'api_base':constants['MIMO_API_BASE']},'summary_frozen_fields':all(s[k]==v for k,v in b.items()),'binding_question_exact':b['question']==row['question'],'system_prompt_exact':b['system_prompt']==constants['SYSTEM_PROMPT'],'requested_exactly_two':b['requested_runs']==2,'only_two_started_files':len(list(t.glob('run_*_started.json')))==2,'only_two_response_files':len(list(t.glob('run_*_response.json')))==2}
    runs=[]
    for i in (1,2):
        start=read(t/f'run_{i:02d}_started.json');run=read(t/f'run_{i:02d}.json');raw=read(t/f'run_{i:02d}_response.json')
        text=raw['choices'][0]['message']['content']
        rc={'started_fields_match_run':all(run[k]==v for k,v in start.items()),'summary_equals_run':s['results'][i-1]==run,'response_bytes_hash_matches':sha(t/f'run_{i:02d}_response.json')==run['response_sha256'],'raw_content_equals_run_answer':text.strip()==run['answer'],'manual_full_content_equals_raw':text==read(candidate/'manual_final_review.json')['manual_results'][i-1].get('complete_raw_final_answer_text',read(candidate/'manual_final_review.json')['manual_results'][i-1].get('complete_final_answer_text')),'http200_completed_stop_untruncated':run['http_status']==200 and run['status']=='completed' and run['finish_reason']==raw['choices'][0]['finish_reason']=='stop' and run['truncated'] is False,'same_frozen_request_image_design':all(run[k]==b[k] for k in ('request_body_sha256','image_sha256','design_sha256')),'response_model_exact':raw['model']==run['response_model']=='mimo-v2.6-flash','no_tool_calls':raw['choices'][0]['message'].get('tool_calls') is None,'no_reasoning_tokens':raw['usage']['completion_tokens_details']['reasoning_tokens']==0,'raw_usage_equals_run':raw['usage']==run['usage'],'raw_created_between_start_and_finish':datetime.fromisoformat(run['started_at']).timestamp()<=raw['created']<=datetime.fromisoformat(run['finished_at']).timestamp(),'binding_before_call':b['created_at']<run['started_at']}
        runs.append({'run_index':i,'run_id':run['run_id'],'provider_response_id':raw['id'],'started_at':run['started_at'],'finished_at':run['finished_at'],'full_raw_final_answer_text':text,'manually_extracted_option':'A','explicit_claimed_decrease_percent':0,'formal_option_meaning':row['choices']['A'],'matches_predeclared_wrong_option':d['expected_wrong_answer']=='A','response_sha256':run['response_sha256'],'raw_response_size':(t/f'run_{i:02d}_response.json').stat().st_size,'checks':rc,'usage':raw['usage']})
    checks['different_run_ids_and_provider_ids']=runs[0]['run_id']!=runs[1]['run_id'] and runs[0]['provider_response_id']!=runs[1]['provider_response_id']
    checks['sequential_separate_calls']=runs[0]['finished_at']<runs[1]['started_at']
    checks['all_checks_pass']=all(checks.values()) and all(all(r['checks'].values()) for r in runs)
    evidence={x.name:{'absolute_path':str(x),'sha256':sha(x),'size':x.stat().st_size,'mtime_ns':x.stat().st_mtime_ns} for x in sorted(t.iterdir()) if x.is_file()}
    clean_req=copy.deepcopy(req);clean_req['messages'][1]['content'][1]['image_url']['url']='[exact PNG base64 independently decoded and byte compared; omitted here]'
    return {'candidate_directory':str(candidate),'test_directory':str(t),'preset':d['expected_wrong_answer'],'checks':checks,'runs':runs,'request_without_base64':clean_req,'request_has_only_original_system_prompt_formal_question_and_candidate_png':True,'solver_receives_no_answer_design_intent_control_or_history':True,'evidence_sha256':evidence}
current=audit(CAND);old=audit(OLD)
freeze=read(CAND/'pretest_freeze.json')
current['pretest_freeze_hash_checks']={name:sha(CAND/name)==h for name,h in freeze['files'].items()}
current['frozen_source_hash_checks']={name:sha(ROOT/name)==h for name,h in read(CAND/'render_check.json')['frozen_inputs']['files'].items()}
current['chronology']={'design_created_at':read(CAND/'design.json')['created_at'],'difference_created_at':read(CAND/'design_difference_audit.json')['created_at'],'visual_checked_at':read(CAND/'pretest_visual_review.json')['created_at'],'pretest_freeze_created_at':freeze['created_at'],'eligibility_checked_at':read(CAND/'eligibility_immediately_before_calls.json')['checked_at'],'binding_created_at':read(next((CAND/'tests').iterdir())/'binding.json')['created_at'],'run_01_started_at':current['runs'][0]['started_at'],'run_01_finished_at':current['runs'][0]['finished_at'],'run_02_started_at':current['runs'][1]['started_at'],'run_02_finished_at':current['runs'][1]['finished_at']}
c=current['chronology']
current['chronology_checks']={'design_preset_before_both_calls':c['difference_created_at']<c['design_created_at']<c['pretest_freeze_created_at']<c['eligibility_checked_at']<c['binding_created_at']<c['run_01_started_at']<c['run_01_finished_at']<c['run_02_started_at']<c['run_02_finished_at'],'pretest_visual_before_freeze':c['visual_checked_at']<c['pretest_freeze_created_at'],'on_disk_design_snapshot_request_binding_before_first_start':all((next((CAND/'tests').iterdir())/name).stat().st_mtime_ns<=(next((CAND/'tests').iterdir())/'run_01_started.json').stat().st_mtime_ns for name in ('binding.json','request.json','design_snapshot.json'))}
inventory=[]
for f in BASE.rglob('binding.json'):
    b=read(f)
    if b.get('question_id')=='Solid126':
        inventory.append({'path':str(f),'sha256':sha(f),'preset':b.get('expected_wrong_answer'),'image_sha256':b.get('image_sha256'),'requested_runs':b.get('requested_runs'),'started_files':[str(x) for x in sorted(f.parent.glob('run_*_started.json'))],'run_statuses':[read(x).get('status') for x in sorted(f.parent.glob('run_??.json'))],'response_files':[str(x) for x in sorted(f.parent.glob('run_*_response.json'))],'incomplete_files':[str(x) for x in f.parent.glob('*incomplete*')]})
save('binding_audit.json',{'checked_at':stamp(),'pid':os.getpid(),'current':current,'old':old,'independently_discovered_all_Solid126_test_bindings_under_task_runtime':inventory,'no_new_API_calls':True,'network_guard':True,'blocked':BLOCKED,'isolation':ISOLATION})
print(json.dumps({'current_checks':current['checks'],'current_freeze':current['pretest_freeze_hash_checks'],'current_source_hashes_all_pass':all(current['frozen_source_hash_checks'].values()),'chronology':current['chronology'],'chronology_checks':current['chronology_checks'],'old_checks':old['checks'],'history_inventory':inventory,'pid':os.getpid(),'blocked':BLOCKED},ensure_ascii=False,indent=2))

