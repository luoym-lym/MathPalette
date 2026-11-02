from review_bootstrap import *
import ast
import base64
import io
import re
from PIL import Image
sys.path.insert(0,str(PROJECT))
from dataset_tools.catalog import content,digest

def rows(p):
    return [json.loads(line) for line in p.read_text(encoding='utf-8-sig').splitlines() if line.strip()] if p.is_file() else []

row=next(r for r in rows(PROJECT/'PlaneGeometry/dataset.jsonl') if r['id']=='Plane427')
approval=read(PROJECT/'provenance/approvals.json')['approvals']['Plane427']
current_content=content(PROJECT,'PlaneGeometry',row)
# Independently assemble the complete original-content object from the documented fingerprint contract.
paths=[row[k] for k in ['image','original_image','script','scene']]+row['runtime_dependencies']+['dataset_generator/common_renderer.py','dataset_generator/protocol.json']
independent_files={p:sha(PROJECT/'PlaneGeometry'/p) for p in paths}
independent_files['../dataset_tools/geometry_dataset.py']=sha(PROJECT/'dataset_tools/geometry_dataset.py')
independent_content={'branch':'PlaneGeometry','record':row,'files':independent_files,'source_notes':read(PROJECT/'provenance/source_notes.json').get('Plane427',{})}
assert current_content==independent_content
original_fingerprint=digest(independent_content)
accepted={name:[r for r in rows(PROJECT/'PlaneGeometry/special_variant'/name) if r.get('question_id',r.get('id'))=='Plane427'] for name in ['accepted_index.jsonl','collected_index.jsonl']}
records={name:read(PROJECT/'PlaneGeometry/special_variant/Plane427'/name) if (PROJECT/'PlaneGeometry/special_variant/Plane427'/name).exists() else None for name in ['recipes.json','collection.json']}
rootrow=next(r for r in rows(PROJECT/'question_bank.jsonl') if r['id']=='Plane427')
delivered=[]
for p in TASK.glob('batch_*/manifest.json'):
    obj=read(p)
    if 'Plane427' in p.read_text(encoding='utf-8-sig'):delivered.append(str(p))
eligibility={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'formal_record':row,'original_approval':approval,'independently_computed_original_content_sha256':original_fingerprint,
 'original_content':independent_content,'valid_current_user_approval':approval.get('reviewer')=='user' and bool(approval.get('instruction')) and bool(approval.get('approved_at_utc')) and original_fingerprint==approval['content_sha256'],
 'accepted_and_collected_matches':accepted,'recipes_and_collection':records,'root_catalog_special_plugins':rootrow.get('special_plugins'),
 'root_catalog_base_plugins':rootrow.get('base_plugins'),'delivered_manifest_matches':delivered,
 'eligible':row['source_dataset']=='MathVision' and original_fingerprint==approval['content_sha256'] and not any(accepted.values()) and not any(records.values()) and not rootrow.get('special_plugins') and not delivered}
assert eligibility['eligible']
write('eligibility_current.json',eligibility)

design=read(CAND/'design.json');binding=read(TEST/'binding.json');summary=read(TEST/'summary.json');request=read(TEST/'request.json')
assert (TEST/'design_snapshot.json').read_bytes()==(CAND/'design.json').read_bytes()
png=(CAND/'candidate.png').read_bytes()
with Image.open(io.BytesIO(png)) as im:
    rgba=im.convert('RGBA');pixel_digest=hashlib.sha256(b'768x768:RGBA:'+rgba.tobytes()).hexdigest()
reference=PROJECT/'PlaneGeometry/workbench/quick_test.py'
tree=ast.parse(reference.read_text(encoding='utf-8-sig'))
constants={}
for node in tree.body:
    if isinstance(node,ast.Assign):
        for target in node.targets:
            if isinstance(target,ast.Name) and target.id in ['SYSTEM_PROMPT','TEST_PROFILES','MIMO_API_BASE']:
                constants[target.id]=ast.literal_eval(node.value)
profile=constants['TEST_PROFILES']['quicktest3']
expected_request={'model':profile['model'],'stream':False,'thinking':profile['thinking'],
 'messages':[{'role':'system','content':constants['SYSTEM_PROMPT']},{'role':'user','content':[{'type':'text','text':row['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(png).decode('ascii')}}]}]}
assert request==expected_request
assert json.dumps(expected_request,ensure_ascii=False).encode('utf-8')==(TEST/'request.json').read_bytes()
assert binding['reference_quick_test_sha256']==sha(reference)
for key,actual in {'request_body_sha256':sha(TEST/'request.json'),'design_sha256':sha(CAND/'design.json'),'image_sha256':sha(CAND/'candidate.png'),
                   'pixel_sha256':pixel_digest,'question_record_sha256':digest(row),'dataset_sha256':sha(PROJECT/'PlaneGeometry/dataset.jsonl')}.items():
    assert binding[key]==actual and summary[key]==actual
assert binding['expected_wrong_answer']==design['expected_wrong_answer']=='B' and design['correct_answer']==row['answer']=='D'
assert {k:v for k,v in binding['settings'].items() if k!='api_base'}==profile
assert binding['settings']['api_base']==constants['MIMO_API_BASE']
assert binding['question']==row['question'] and binding['system_prompt']==constants['SYSTEM_PROMPT']
assert binding['requested_runs']==2
for key,value in binding.items():assert summary[key]==value

def timeparse(s):return datetime.fromisoformat(s.replace('Z','+00:00'))
runs=[]
for i in [1,2]:
    started_path=TEST/f'run_{i:02d}_started.json'; run_path=TEST/f'run_{i:02d}.json';raw_path=TEST/f'run_{i:02d}_response.json'
    started=read(started_path);run=read(run_path);raw=read(raw_path)
    for key,value in started.items():assert run[key]==value
    for key in ['request_body_sha256','image_sha256','design_sha256']:assert run[key]==binding[key]
    assert run==summary['results'][i-1]
    assert run['response_sha256']==sha(raw_path)
    assert run['status']=='completed' and run['http_status']==200 and run['finish_reason']=='stop' and run['truncated'] is False
    assert len(raw['choices'])==1 and raw['choices'][0]['finish_reason']=='stop' and raw['choices'][0]['index']==0
    message=raw['choices'][0]['message']
    assert message['role']=='assistant' and not message.get('tool_calls')
    assert message['content'].strip()==run['answer'] and run['thinking']==''
    assert raw['model']==run['response_model']==profile['model'] and raw['usage']==run['usage']
    assert raw['usage']['completion_tokens_details']['reasoning_tokens']==0
    assert timeparse(design['created_at_utc'])<timeparse(binding['created_at'])<=timeparse(started['started_at'])<timeparse(run['finished_at'])
    created=datetime.fromtimestamp(raw['created'],tz=timezone.utc)
    assert timeparse(started['started_at'])<=created<=timeparse(run['finished_at'])
    runs.append({'run_index':i,'run_id':run['run_id'],'response_id':raw['id'],'started_at':run['started_at'],'provider_created_at':created.isoformat(),'finished_at':run['finished_at'],
     'http_status':200,'status':'completed','finish_reason':'stop','untruncated':True,'response_model':raw['model'],'usage':raw['usage'],
     'full_assistant_content':message['content'],'content_utf8_sha256':hashlib.sha256(message['content'].encode('utf-8')).hexdigest(),
     'final_letter':'B','final_degrees':25,'terminal_letter_and_value_consistent':True,'matches_predeclared_wrong_answer':True,
     'actual_reasoning':'Both use STV=70-60=10, TSV=(180-10)/2=85, RSV=85-60=25. This is an incorrect ray-order computation, not the prospectively hypothesized correct intermediate 25 followed by an omitted subtraction.',
     'additional_error':'Run 2 calls RT -> TV a rotation correspondence; actual correspondence is RT -> UT. RT=TV still holds by congruent equilateral sides.' if i==2 else None,
     'hashes':{'raw_response':sha(raw_path),'run_record':sha(run_path),'started_record':sha(started_path)},'raw_response_path':str(raw_path)})
assert runs[0]['run_id']!=runs[1]['run_id'] and runs[0]['response_id']!=runs[1]['response_id']
assert timeparse(runs[0]['finished_at'])<=timeparse(runs[1]['started_at'])

# Read-only full-task evidence scan, including all existing quick-test request/binding copies.
all_files=[]
for scanroot in [TASK,PROJECT/'.runtime/plane_special/quick_tests']:
    if not scanroot.exists():continue
    for parent,dirs,files in os.walk(scanroot):
        dirs[:]=[d for d in dirs if not (Path(parent)/d).resolve().is_relative_to(OWN) and d not in ['node_modules','__pycache__','.git']]
        all_files.extend(Path(parent)/n for n in files)
binding_matches=[];request_matches=[];scan_errors=[]
scanned_bindings=0;scanned_requests=0
for p in all_files:
    if p.name not in ['binding.json','request.json']:continue
    try:obj=read(p)
    except Exception as exc:scan_errors.append({'path':str(p),'error':str(exc)});continue
    if p.name=='binding.json':
        scanned_bindings+=1
        if obj.get('question_id')=='Plane427' or obj.get('image_sha256')==sha(CAND/'candidate.png'):
            binding_matches.append({'path':str(p),'sha256':sha(p),'binding':obj})
    else:
        scanned_requests+=1;is_question=False;image_hashes=[]
        for message in obj.get('messages',[]):
            body=message.get('content')
            if isinstance(body,list):
                for item in body:
                    if item.get('type')=='text' and item.get('text')==row['question']:is_question=True
                    if item.get('type')=='image_url':
                        url=item.get('image_url',{}).get('url','')
                        if url.startswith('data:image/png;base64,'):
                            image_hashes.append(hashlib.sha256(base64.b64decode(url.split(',',1)[1],validate=True)).hexdigest())
        if is_question or sha(CAND/'candidate.png') in image_hashes:
            request_matches.append({'path':str(p),'sha256':sha(p),'formal_question':is_question,'image_hashes':image_hashes})

invocation_dirs={Path(m['path']).parent for m in binding_matches+request_matches}
matching_run_records=[];orphan_artifacts=[]
for directory in sorted(invocation_dirs):
    for p in sorted(directory.glob('run_*.json')):
        obj=read(p)
        if re.fullmatch(r'run_\d+\.json',p.name):
            matching_run_records.append({'path':str(p),'sha256':sha(p),'run_id':obj.get('run_id'),'status':obj.get('status'),'image_sha256':obj.get('image_sha256'),'expected_wrong_answer':read(directory/'binding.json').get('expected_wrong_answer') if (directory/'binding.json').exists() else None})
    orphan_artifacts.extend(str(p) for p in directory.iterdir() if any(s in p.name.lower() for s in ['incomplete','error','abort']))
unique_runs={r['run_id'] for r in matching_run_records}
assert unique_runs=={r['run_id'] for r in runs}
assert all(r['status']=='completed' for r in matching_run_records) and not orphan_artifacts

all_question_paths=[str(p.relative_to(PROJECT)) for p in all_files if 'Plane427' in str(p)]
question_paths_with_calls=[p for p in all_question_paths if any(s in p.lower() for s in ['binding.json','started.json','response.json','summary.json','incomplete','abort'])]
assert not any('background_20/Plane427' in s.replace('\\','/') for s in question_paths_with_calls)

file_hashes={str(p.relative_to(PROJECT)):sha(p) for p in sorted(TEST.iterdir()) if p.is_file()}
for p in [CAND/'candidate.png',CAND/'plugin.json',CAND/'design.json',CAND.parent/'context.json',CAND.parent/'source_scene_snapshot.json',CAND.parent/'formal_record.json',reference,TASK/'harness/quicktest3_isolated.py',TASK/'background_41/harness/quicktest3_isolated.py']:
    file_hashes[str(p.relative_to(PROJECT))]=sha(p)
harness_equal=(TASK/'harness/quicktest3_isolated.py').read_bytes()==(TASK/'background_41/harness/quicktest3_isolated.py').read_bytes()
assert harness_equal

evidence={'question_id':'Plane427','variant_id':'r41_isosceles_base_angle_frame','formal_question':row['question'],'choices':row['choices'],'unique_correct_answer':{'letter':'D','degrees':35},
 'predeclared_wrong_answer':{'letter':'B','degrees':25},'candidate_png_sha256':sha(CAND/'candidate.png'),'candidate_pixel_sha256':pixel_digest,
 'request_sha256':sha(TEST/'request.json'),'design_sha256':sha(CAND/'design.json'),'design_snapshot_byte_equal':True,'plugin_sha256':sha(CAND/'plugin.json'),
 'input_only_exact_formal_question_and_candidate_PNG':True,'system_prompt_exactly_current_reference':True,'profile':profile,'no_max_tokens_or_local_timeout_change':True,
 'no_answer_intent_history_control_or_geometry_parameters_in_payload':True,'design_created_at':design['created_at_utc'],'binding_created_at':binding['created_at'],'two_runs':runs,
 'chronology_internally_consistent':True,'chronology_limit':'File hashes, retained records, metadata and provider-created timestamps are mutually consistent. This is a local artifact audit, not an external trusted timestamp or provider-account audit.',
 'file_hashes':file_hashes,'harness_source_copy_byte_equal':harness_equal,
 'full_task_scan':{'roots':[str(TASK),str(PROJECT/'.runtime/plane_special/quick_tests')],'files_visited':len(all_files),'binding_files_fully_parsed':scanned_bindings,'request_files_fully_parsed':scanned_requests,
                  'binding_matches':binding_matches,'request_matches':request_matches,'matching_run_records':matching_run_records,'unique_call_count':len(unique_runs),'scan_errors':scan_errors,
                  'orphan_error_abort_incomplete_artifacts':orphan_artifacts,'all_Plane427_paths':all_question_paths,'original_controls_found':[],
                  'no_preset_relabel_or_selection_found':True,'old_background20_has_no_Plane427_candidate_or_call':True},
 'mechanism_limit':'The retained prospective hypothesis remains intermediate-angle/target-angle-frame confusion. Neither narrative demonstrates it. The observed error is a different angle-order/sign calculation. Final B25/B25 is confirmed, causal influence and gain are unproven.'}
write('evidence_audit.json',evidence)
print(json.dumps({'eligibility':{k:v for k,v in eligibility.items() if k not in ['formal_record','original_content']},'evidence':{k:v for k,v in evidence.items() if k not in ['two_runs','full_task_scan','file_hashes']},
 'scan':{k:v for k,v in evidence['full_task_scan'].items() if k not in ['all_Plane427_paths','binding_matches']},'hashes':file_hashes},ensure_ascii=False,indent=2))
