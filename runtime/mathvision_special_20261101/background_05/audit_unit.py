import os,sys,json,hashlib,importlib.util,base64
from pathlib import Path
from datetime import datetime,timezone
UNIT=Path(__file__).resolve().parent
ROOT=next(p for p in UNIT.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
BASE=ROOT/'runtime/mathvision_special_20261101'
for var,name in {'TEMP':'audit_temp','TMP':'audit_temp','MPLCONFIGDIR':'audit_mpl_cache','XDG_CACHE_HOME':'audit_cache'}.items():
    target=UNIT/name;target.mkdir(parents=True,exist_ok=True);os.environ[var]=str(target)
sys.dont_write_bytecode=True;os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.path.insert(0,str(BASE))
from runtime_isolation import install
ISOLATION=install(UNIT/'audit_render_tmp')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):
    with Path(p).open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
spec=importlib.util.spec_from_file_location('_existing_isolated_harness_readonly',BASE/'harness/quicktest3_isolated.py');harness=importlib.util.module_from_spec(spec);spec.loader.exec_module(harness)
results=[]
for p in sorted(UNIT.rglob('binding.json')):
    binding=read(p);folder=p.parent;branch=binding['branch'];qid=binding['question_id'];reference=harness.reference_module(branch)
    image=Path(binding['image_path']);design=Path(binding['design_path']);request=read(folder/'request.json');summary=read(folder/'summary.json')
    formal=next(json.loads(l) for l in (ROOT/branch/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if l.strip() and json.loads(l)['id']==qid)
    issues=[]
    def require(flag,why):
        if not flag:issues.append(why)
    require(image.resolve().is_relative_to(UNIT),'image outside this unit');require(design.resolve().is_relative_to(UNIT),'design outside unit')
    require(digest(image)==binding['image_sha256'],'image bytes changed');require(digest(design)==binding['design_sha256'],'design changed');require(digest(folder/'design_snapshot.json')==binding['design_sha256'],'design snapshot differs')
    require(digest(folder/'request.json')==binding['request_body_sha256'],'request bytes differ');require(read(design)['expected_wrong_answer']==binding['expected_wrong_answer'],'preset changed')
    require(binding['expected_wrong_answer']!=formal['answer'],'preset not wrong');require(formal['source_dataset']=='MathVision','not MathVision')
    require(binding['question_record_sha256']==hashlib.sha256(json.dumps(formal,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),'formal record changed')
    require(binding['dataset_sha256']==digest(ROOT/branch/'dataset.jsonl'),'formal dataset changed')
    require(request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'} and request['stream'] is False,'wrong profile')
    require(set(request)=={'model','stream','thinking','messages'},'extra request fields');require(len(request['messages'])==2,'history leakage')
    require(request['messages'][0]=={'role':'system','content':reference.SYSTEM_PROMPT},'system prompt differs')
    user=request['messages'][1];require(user.get('role')=='user' and len(user.get('content',[]))==2,'extra user input')
    require(user['content'][0]=={'type':'text','text':formal['question']},'text differs from exact formal question')
    block=user['content'][1];require(block['type']=='image_url' and set(block)=={'type','image_url'} and set(block['image_url'])=={'url'},'extra image block fields')
    require(base64.b64decode(block['image_url']['url'].split(',',1)[1])==image.read_bytes(),'image payload differs')
    require(summary['two_completed'] and len(summary['results'])==2,'not two completed')
    profile=dict(reference.TEST_PROFILES['quicktest3']);profile['api_base']=binding['settings']['api_base'];require(binding['settings']==profile,'profile differs from reference')
    require(binding['reference_quick_test_sha256']==digest(ROOT/branch/'workbench/quick_test.py'),'reference code changed')
    jobs=[]
    for ix in [1,2]:
        job=read(folder/f'run_{ix:02d}.json');started=read(folder/f'run_{ix:02d}_started.json')
        require(job['status']=='completed' and job['finish_reason']=='stop' and not job.get('truncated'),'incomplete call')
        require(job['request_body_sha256']==binding['request_body_sha256'] and job['image_sha256']==binding['image_sha256'] and job['design_sha256']==binding['design_sha256'],'run binding differs')
        require(digest(folder/f'run_{ix:02d}_response.json')==job['response_sha256'],'raw response differs')
        require(started['run_id']==job['run_id'],'run id mismatch');jobs.append({'run_index':ix,'status':job['status'],'run_id':job['run_id'],'final_answer_path':str(folder/f'run_{ix:02d}.json'),'raw_response_sha256':job['response_sha256']})
    require(jobs[0]['run_id']!=jobs[1]['run_id'],'same job reused')
    results.append({'question_id':qid,'branch':branch,'image_path':str(image),'design_path':str(design),'binding_path':str(p),'same_frozen_png_sha256':binding['image_sha256'],'immutable_design_sha256':binding['design_sha256'],'request_body_sha256':binding['request_body_sha256'],'expected_wrong_answer':binding['expected_wrong_answer'],'exact_formal_question_and_png_only':not issues,'complete_pair':summary['two_completed'],'runs':jobs,'issues':issues})
report={'checked_at':datetime.now(timezone.utc).isoformat(),'isolation':ISOLATION,'pair_count':len(results),'completed_call_count':2*len(results),'all_bindings_valid':all(not r['issues'] for r in results),'bindings':results,'manual_answer_grading':'Not performed by this audit. Manual owner judgments and complete raw finals are separately retained.','credential_handling':'No credential was read by this audit; request payloads contain no authentication headers.'}
write(UNIT/'evidence_binding_audit.json',report)
print(json.dumps({'pairs':report['pair_count'],'calls':report['completed_call_count'],'all_bindings_valid':report['all_bindings_valid']}))
