"""Independent offline review. No solver, network, state, or authority mutations."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
ROOT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = OWN.parent.parent
UNIT = TASK / 'units/u04_angles'
QUESTION = UNIT / 'Plane321'
CANDIDATE = QUESTION / 'a01_pivot_legs_vs_true_bases'
REFERENCE = TASK / 'references/Plane427'
OLD = ROOT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, sub in {'TEMP':'tmp', 'TMP':'tmp', 'MPLCONFIGDIR':'mpl', 'XDG_CACHE_HOME':'cache', 'PYTHONPYCACHEPREFIX':'pycache'}.items():
    target = OWN / 'ownruntime' / sub
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['MPLBACKEND'] = 'Agg'

def write_check(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Independent review strict writeguard: ' + str(resolved))

def audit(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
        write_check(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        write_check(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        write_check(args[0]); write_check(args[1])
    elif event in ('socket.connect', 'socket.bind', 'subprocess.Popen', 'os.system', 'os.spawn'):
        raise PermissionError('Review disallows network and child processes: ' + event)
sys.addaudithook(audit)

import base64
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import traceback
sys.path.insert(0, str(ROOT))

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def save(name, data):
    p = OWN / name
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')

def printj(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))

def inspect():
    history = read(TASK/'history_index.json')
    h = next(q for q in history['questions'] if q['question_id']=='Plane321')
    printj({'history_root_keys':list(history), 'scoped_history':h})
    for relative in ['parent_audits/native_u01_u04/audit.json', 'units/u04_angles/readonly_preservation_final.json', 'units/u04_angles/complete_call_ledger.json']:
        data = read(TASK/relative)
        if 'evidence' in data:
            data['evidence'] = [x for x in data['evidence'] if x.get('question_id')=='Plane321']
        if 'protected_files' in data:
            data['protected_file_count'] = len(data.pop('protected_files'))
        if 'calls' in data:
            data['calls'] = [x for x in data['calls'] if x.get('question_id')=='Plane321']
        printj({'path':relative,'data':data})
    for name in ['manual_final_review.json', 'primary_review.json', 'reference_transfer.json', 'primary_review_before_calls.json']:
        printj({'path':str(CANDIDATE/name),'data':read(CANDIDATE/name)})

def snapshot():
    files = set(QUESTION.rglob('*')) | set(REFERENCE.rglob('*'))
    files.update(UNIT/name for name in ['assignment.json','complete_call_ledger.json','readonly_preservation_final.json','harness_integrity.json','history_scoped_index.json','history_full_raw_responses.json','history_full_read_manifest.json','offline_error_01.json','finalization_error_01.json'])
    files.update(TASK/name for name in ['task.json','reference_style_summary.json','reference_manifest.json','history_index.json','parent_review_preflight.json','parent_imitation_priority_20261102.txt','parent_audits/native_u01_u04/audit.json'])
    assignment=next(q for q in read(UNIT/'assignment.json')['questions'] if q['question_id']=='Plane321')
    files.update(ROOT/p for p in assignment['frozen_source_files_sha256'])
    files.update(ROOT/p for p in read(REFERENCE/'reference.json')['frozen_source_files_sha256'])
    files.update((OLD/'root_explore/Plane321').rglob('*'))
    files.update(ROOT/p for p in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json','PlaneGeometry/workbench/mathvision_adapter.py','PlaneGeometry/workbench/mathvision_plugins.py','PlaneGeometry/workbench/workbench_io.py','PlaneGeometry/workbench/quick_test.py','dataset_tools/mathvision_workbench.py','dataset_tools/catalog.py','dataset_tools/geometry_dataset.py'])
    files.add(OLD/'runtime_isolation.py')
    data={str(p.relative_to(ROOT)):sha(p) for p in sorted(files) if p.is_file()}
    save('scoped_sources_before.json', {'created_at':now(),'files':data,'scope':'Candidate and question evidence, current reference snapshot, both formal render dependencies, old Plane321 trials, relevant protocols/adapters and finite parent audit. No claim about unrelated workspace.'})
    printj({'scoped_file_count':len(data)})

def replay():
    spec=importlib.util.spec_from_file_location('_independent_readonly_runtime_isolation', OLD/'runtime_isolation.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    isolation=module.install(OWN/'ownruntime/native', guard_writes=False)
    sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
    from workbench_io import load_config, pixel_hash, environment_versions
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from dataset_tools.mathvision_workbench import png_bytes
    config=load_config(ROOT/'PlaneGeometry/workbench/config.json')
    config['runtime_dir']=str(OWN/'ownruntime/state')
    config['output_dir']=str(OWN/'ownruntime/output')
    adapter=RendererAdapter(config)
    context=adapter.inspect_question('Plane321')
    frozen=read(QUESTION/'context.json')
    assert context == frozen, 'Exact current context mismatch'
    assert json.dumps(context,ensure_ascii=False,separators=(',',':')) == json.dumps(frozen,ensure_ascii=False,separators=(',',':')), 'Context key order mismatch'
    scene=adapter.scene('Plane321')
    try:
        noop=png_bytes(scene)
    finally:
        scene.close()
    noop_path=OWN/('noop_formal.png' if not (OWN/'noop_formal.png').exists() else 'noop_formal_after_serialization_correction.png')
    with noop_path.open('xb') as stream:
        stream.write(noop)
    formal=(ROOT/'PlaneGeometry/image/Plane321.png').read_bytes()
    assert pixel_hash(noop)==pixel_hash(formal)
    renderer=PluginRenderer(config,adapter,{'Plane321':context})
    plugin=read(CANDIDATE/'plugin.json')
    normalized, png, pixels=renderer.render(plugin,frozen=True)
    assert normalized==plugin
    assert json.dumps(normalized,ensure_ascii=False,separators=(',',':'))==json.dumps(plugin,ensure_ascii=False,separators=(',',':')), 'Plugin order mismatch'
    assert png==(CANDIDATE/'candidate.png').read_bytes()
    assert pixels==read(CANDIDATE/'design.json')['pixel_sha256']
    (OWN/'exact_replay.png').write_bytes(png)
    save('exact_replay.json',{'created_at':now(),'pid':os.getpid(),'context_exact_values_order_keys':True,'plugin_exact_values_order_keys':True,'noop_formal_bytes_equal':noop==formal,'noop_formal_pixels_equal':True,'noop_png_sha256':hashlib.sha256(noop).hexdigest(),'candidate_bytes_equal':True,'candidate_pixels_equal':True,'numeric_tolerance_used':False,'candidate_sha256':hashlib.sha256(png).hexdigest(),'candidate_pixel_sha256':pixels,'formal_sha256':hashlib.sha256(formal).hexdigest(),'formal_pixel_sha256':pixel_hash(formal),'environment':environment_versions(),'runtime_redirect':isolation,'strict_guard_installed_before_project_numeric_imports':True,'strict_guard_root':str(OWN),'env':{k:os.environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME']},'adapters_schema_edited':False,'only_runtime_temp_path_redirected_in_memory':True})
    printj(read(OWN/'exact_replay.json'))

def eligibility():
    from dataset_tools import catalog
    record=next(q for q in catalog.rows(ROOT/'PlaneGeometry/dataset.jsonl') if q['id']=='Plane321')
    assignment=next(q for q in read(UNIT/'assignment.json')['questions'] if q['question_id']=='Plane321')
    approval=read(ROOT/'provenance/approvals.json')['approvals']['Plane321']
    content=catalog.content(ROOT,'PlaneGeometry',record)
    fingerprint=catalog.digest(content)
    special=ROOT/'PlaneGeometry/special_variant'
    indices={name:[r for r in catalog.rows(special/name) if r.get('question_id',r.get('id'))=='Plane321'] if (special/name).exists() else [] for name in ['accepted_index.jsonl','collected_index.jsonl']}
    sources={p:sha(ROOT/p) for p in assignment['frozen_source_files_sha256']}
    drift={p:{'frozen':h,'current':sources[p]} for p,h in assignment['frozen_source_files_sha256'].items() if h!=sources[p]}
    recipes=read(special/'Plane321/recipes.json') if (special/'Plane321/recipes.json').exists() else []
    collection=read(special/'Plane321/collection.json') if (special/'Plane321/collection.json').exists() else None
    result={'created_at':now(),'question_id':'Plane321','current_content_sha256':fingerprint,'approval':approval,'formal_record_equals_frozen':record==assignment['formal_record'],'fingerprint_matches_approval_and_assignment':fingerprint==approval['content_sha256']==assignment['current_content_sha256'],'current_special_entries':indices,'recipes':recipes,'collection':collection,'source_files':sources,'source_drift':drift,'eligible':not drift and not any(indices.values()) and not recipes and collection is None and fingerprint==approval['content_sha256']==assignment['current_content_sha256'] and record==assignment['formal_record'],'authority_changed':False}
    save('current_eligibility.json',result)
    printj(result)

def bindings():
    evidence=next((CANDIDATE/'tests').glob('*/summary.json')).parent
    summary=read(evidence/'summary.json'); binding=read(evidence/'binding.json'); design=read(CANDIDATE/'design.json'); plugin=read(CANDIDATE/'plugin.json'); request=read(evidence/'request.json')
    record=read(QUESTION/'formal_record.json')
    sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
    import quick_test
    assert set(request)=={'model','messages','thinking','stream'} and request['stream'] is False
    assert request['model']=='mimo-v2.6-flash' and request['thinking']=={'type':'disabled'}
    assert request['messages'][0]=={'role':'system','content':quick_test.SYSTEM_PROMPT}
    assert len(request['messages'])==2 and request['messages'][1]['role']=='user'
    content=request['messages'][1]['content']
    assert len(content)==2 and content[0]=={'type':'text','text':record['question']}
    assert set(request['messages'][1])=={'role','content'} and set(content[1])=={'type','image_url'} and set(content[1]['image_url'])=={'url'}
    assert content[1]['type']=='image_url' and content[1]['image_url']['url'].startswith('data:image/png;base64,')
    assert base64.b64decode(content[1]['image_url']['url'].split(',',1)[1],validate=True)==(CANDIDATE/'candidate.png').read_bytes()
    assert len(summary['results'])==len(list(evidence.glob('run_*_started.json')))==len(list(evidence.glob('run_*_response.json')))==len(list(evidence.glob('run_[0-9][0-9].json')))==2
    assert binding['requested_runs']==summary['requested_runs']==2
    configured=dict(quick_test.TEST_PROFILES['quicktest3'],api_base=quick_test.MIMO_API_BASE)
    assert summary['settings']==binding['settings']==configured
    assert binding['system_prompt']==summary['system_prompt']==quick_test.SYSTEM_PROMPT
    assert binding['image_path']==str(CANDIDATE/'candidate.png') and binding['design_path']==str(CANDIDATE/'design.json')
    assert (evidence/'design_snapshot.json').read_bytes()==(CANDIDATE/'design.json').read_bytes()
    assert sha(CANDIDATE/'candidate.png')==summary['image_sha256']==binding['image_sha256']==design['png_sha256']
    assert sha(CANDIDATE/'plugin.json')==design['plugin_sha256']
    assert sha(CANDIDATE/'design.json')==summary['design_sha256']==binding['design_sha256']
    assert sha(evidence/'request.json')==summary['request_body_sha256']==binding['request_body_sha256']
    assert sha(ROOT/'PlaneGeometry/workbench/quick_test.py')==summary['reference_quick_test_sha256']
    assert summary['question_record_sha256']==hashlib.sha256(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert sha(ROOT/'PlaneGeometry/dataset.jsonl')==summary['dataset_sha256']
    for key,value in binding.items():
        assert summary[key]==value
    assert design['expected_wrong_answer']=='B' and design['expected_wrong_value_degrees']=='120'
    assert design['created_at']<binding['created_at']<summary['results'][0]['started_at']
    runs=[]
    for index in (1,2):
        run=read(evidence/f'run_{index:02d}.json'); started=read(evidence/f'run_{index:02d}_started.json'); raw=read(evidence/f'run_{index:02d}_response.json')
        assert run==summary['results'][index-1]
        for k,v in started.items():
            assert run[k]==v
        assert run['response_sha256']==sha(evidence/f'run_{index:02d}_response.json')
        assert run['request_body_sha256']==binding['request_body_sha256'] and run['design_sha256']==binding['design_sha256'] and run['image_sha256']==binding['image_sha256']
        assert len(raw['choices'])==1 and raw['choices'][0]['finish_reason']==run['finish_reason']=='stop'
        assert raw['choices'][0]['message']['content']==run['answer']
        assert run['status']=='completed' and run['http_status']==200 and run['truncated'] is False
        assert raw['model']==run['response_model']=='mimo-v2.6-flash'
        assert raw['usage']['completion_tokens_details']['reasoning_tokens']==0
        runs.append({'run_index':index,'raw_path':str(evidence/f'run_{index:02d}_response.json'),'raw_sha256':run['response_sha256'],'started_at':run['started_at'],'finished_at':run['finished_at'],'raw_content':run['answer'],'characters':len(run['answer']),'finish_reason':run['finish_reason'],'truncated':False,'run_id':run['run_id']})
    result={'created_at':now(),'paths_and_hashes':{str(p):sha(p) for p in [CANDIDATE/'candidate.png',CANDIDATE/'plugin.json',CANDIDATE/'design.json',evidence/'summary.json',evidence/'binding.json',evidence/'request.json',evidence/'design_snapshot.json']},'preset_created_at':design['created_at'],'binding_created_at':binding['created_at'],'all_exact_binding_checks':True,'request_only_configured_system_formal_question_png':True,'request_keys':list(request),'runs':runs,'actual_complete_calls':2,'no_api_request_by_reviewer':True}
    save('frozen_binding_audit.json',result)
    printj({k:v for k,v in result.items() if k!='runs'})

def preservation():
    before=read(OWN/'scoped_sources_before.json')['files']
    differences={p:{'before':h,'after':sha(ROOT/p) if (ROOT/p).exists() else None} for p,h in before.items() if not (ROOT/p).exists() or sha(ROOT/p)!=h}
    primary=read(UNIT/'readonly_preservation_final.json')
    scoped=[x for x in primary['protected_files'] if 'Plane321' in x['path'] or x['path'].startswith(('AGENTS','MATHPALETTE','PlaneGeometry'))]
    primary_drift=[{'path':x['path'],'expected':x['after'],'current':sha(ROOT/x['path']) if (ROOT/x['path']).exists() else None} for x in scoped if not (ROOT/x['path']).exists() or sha(ROOT/x['path'])!=x['after']]
    result={'created_at':now(),'scoped_file_count':len(before),'review_start_end_differences':differences,'primary_historical_scoped_files_compared':len(scoped),'primary_historical_scoped_drift':primary_drift,'no_restore_attempted':True,'whole_workspace_unchanged_claimed':False,'owned_subprocesses_started':0,'owned_servers_started':0,'owned_network_calls':0,'no_user_authority_operations':True}
    save('scoped_preservation_final.json',result)
    printj(result)

def history():
    h=next(q for q in read(TASK/'history_index.json')['questions'] if q['question_id']=='Plane321')
    saved=[]
    old_responses=[]
    for item in h['designs']:
        directory=ROOT/item['directory']
        design=read(directory/'design.json')
        plugin=read(directory/'plugin.json')
        evidence=next((directory/'tests').glob('*/summary.json')).parent
        summary=read(evidence/'summary.json')
        assert sha(directory/'candidate.png')==item['frozen_candidate_png_sha256']
        assert sha(directory/'design.json')==item['design_sha256']
        for index in (1,2):
            raw_path=evidence/f'run_{index:02d}_response.json'
            raw=read(raw_path)
            run=summary['results'][index-1]
            assert sha(raw_path)==run['response_sha256']
            assert raw['choices'][0]['message']['content']==run['answer']
            old_responses.append({'variant_id':item['variant_id'],'run_index':index,'raw_path':str(raw_path),'raw_sha256':sha(raw_path),'full_content':run['answer']})
        saved.append({'variant_id':item['variant_id'],'preset':item['predeclared_wrong_answer'],'candidate_sha256':sha(directory/'candidate.png'),'design':design,'plugin':plugin,'calls':len(summary['results']),'answer_endings':[x['answer'][-550:] for x in summary['results']],'incomplete':[x for x in summary['results'] if x.get('status')!='completed' or x.get('truncated') or x.get('finish_reason')!='stop'],'unchanged':True})
    relevant={k:v for k,v in h.items() if k!='designs'}
    save('old_history_read.json',{'created_at':now(),'history_index_scoped_record':h,'old_frozen_trials':saved,'old_raw_responses':old_responses,'all_old_trials_read_only':True})
    printj({'history_keys':list(h),'other_history_references':{k:v for k,v in relevant.items() if 'reference' in k or 'trial' in k},'old_frozen_trials':saved})

def request_scan():
    exact_question=read(QUESTION/'formal_record.json')['question']
    candidate_sha=sha(CANDIDATE/'candidate.png')
    matches=[]; errors=[]; manifests={}; count=0
    for p in sorted((ROOT/'runtime').rglob('request.json')):
        if p.is_relative_to(OWN):
            continue
        count+=1
        try:
            request=read(p)
            messages=request.get('messages',[])
            text=''; hashes=[]
            for message in messages:
                content=message.get('content')
                if message.get('role')=='user' and isinstance(content,list):
                    text=''.join(c.get('text','') for c in content if c.get('type')=='text')
                    for c in content:
                        url=c.get('image_url',{}).get('url','')
                        if url.startswith('data:image/'):
                            hashes.append(hashlib.sha256(base64.b64decode(url.split(',',1)[1],validate=True)).hexdigest())
            if text==exact_question or candidate_sha in hashes:
                record={'path':str(p.relative_to(ROOT)),'request_sha256':sha(p),'exact_question_match':text==exact_question,'image_hashes':hashes,'exact_candidate_png_match':candidate_sha in hashes,'run_started_files':[str(x.relative_to(ROOT)) for x in sorted(p.parent.glob('run_*_started.json'))],'raw_response_files':[str(x.relative_to(ROOT)) for x in sorted(p.parent.glob('run_*_response.json'))]}
                matches.append(record)
                manifests[str(p.relative_to(ROOT))]=sha(p)
        except Exception as error:
            errors.append({'path':str(p.relative_to(ROOT)),'error':repr(error)})
    prior=read(CANDIDATE/'global_prior_request_audit.json')
    assert prior['exact_image_matches']==[] and prior['parse_errors']==[]
    # Recompute the primary prefreeze request scan hashes, including ZIP evidence paths if present.
    primary_changed=[]
    for path,expected in prior['scanned_sha256'].items():
        p=ROOT/path
        if p.is_file() and sha(p)!=expected:
            primary_changed.append(path)
    assert not primary_changed
    exact=[x for x in matches if x['exact_candidate_png_match']]
    same_request=[x for x in exact if x['exact_question_match']]
    assert len(same_request)==1 and Path(ROOT/same_request[0]['path']).parent==next((CANDIDATE/'tests').iterdir())
    assert len(same_request[0]['run_started_files'])==len(same_request[0]['raw_response_files'])==2
    result={'created_at':now(),'runtime_request_files_scanned':count,'same_question_or_same_candidate_matches':matches,'parse_errors':errors,'same_question_same_candidate_request_directories':len(same_request),'actual_started_records_for_this_request':2,'hidden_third_call_in_saved_records':False,'primary_prefreeze_scan_file_count':len(prior['scanned_sha256']),'primary_prefreeze_scan_record_hashes_drift':primary_changed,'primary_prefreeze_exact_image_matches':prior['exact_image_matches'],'cross_id_transfer_rule':'Current nine reference transfer authorized. Different formal text/options is assessed separately; no same-image cross-ID transfer assumed a repeated same request.','limitations':'Saved-file audit cannot establish absence of unrecorded external provider calls. No such call is indicated by scoped ledger and records.'}
    save('request_history_scan.json',result)
    printj(result)

def exact_math():
    # Each scalar is a+b*sqrt(3), represented by two Fractions.
    def q(a=0,b=0): return (F(a),F(b))
    def add(x,y): return (x[0]+y[0],x[1]+y[1])
    def neg(x): return (-x[0],-x[1])
    def mul(x,y): return (x[0]*y[0]+3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def rotate(p,c,s): return (add(mul(c,p[0]),neg(mul(s,p[1]))),add(mul(s,p[0]),mul(c,p[1])))
    def serial(p): return [[str(a),str(b)] for a,b in p]
    points={'A':(q(),q()),'B':(q(-2),q()),'C':(q(-1),q(0,-1)),'D':(q(1),q(0,-1))}
    rotations={0:(q(1),q()),60:(q(F(1,2)),q(0,F(1,2))),120:(q(F(-1,2)),q(0,F(1,2))),180:(q(-1),q()),240:(q(F(-1,2)),q(0,F(-1,2))),300:(q(F(1,2)),q(0,F(-1,2)))}
    results={}
    for angle,(c,s) in rotations.items():
        transformed={name:rotate(points[name],c,s) for name in ('A','C','D')}
        matches={name:next((n for n,v in points.items() if v==p),None) for name,p in transformed.items()}
        results[str(angle)]={'transformed_points':{n:serial(p) for n,p in transformed.items()},'vertex_matches':matches,'covers_target':set(transformed.values())==set(points[n] for n in ('A','B','C'))}
    assert [a for a,v in results.items() if v['covers_target']]==['300']
    c,s=rotations[300]
    source=[('A','C','blue'),('A','D','blue'),('C','D','red')]
    target={(frozenset((points[a],points[b])),color) for a,b,color in [('A','B','blue'),('A','C','blue'),('B','C','red')]}
    moved={(frozenset((rotate(points[a],c,s),rotate(points[b],c,s))),color) for a,b,color in source}
    assert moved==target
    proof={
      'question_id':'Plane321','author':'Independent second reviewer','basis':'Formal equilateral words and actual source JPG/formal PNG layout, independently inspected. Approval answer, primary proof, and model outputs do not serve as premises.',
      'normalized_geometry':'Translate A to origin and positively scale the shared side to length2. Actual source arrangement places B=(-2,0), C=(-1,-sqrt(3)), D=(1,-sqrt(3)); A=(0,0). This uses only the two equilateral triangles on opposite sides of AC, preserving the source orientation. The frozen x coordinates B0,A6,C3,D9 with common upper y5.196152422706632 have precisely this same placement; floating coordinates are drawing inputs, not exact-given measurements.',
      'coverage':'Both equilateral triangles share side AC, hence have equal positive side length and area. Rigid rotation preserves area. Full containment can hold only at equality: if two compact triangles with equal area differed under containment, some nonempty open subset of the larger triangle would lie outside the smaller, contradicting equal area. First covers therefore means first whole-triangle coincidence, not first touching or partial overlap.',
      'all_continuous_angles_exhausted':'A rotation about A fixes the vertex A, and equality of the two convex triangles must map extreme vertices to extreme vertices. Only two bijections for remaining vertices are possible. C->B and D->C both require theta=300 (mod360), since radial directions AC240, AD300, AB180. C->C would require theta=0 (mod360), whereas D->B requires theta=240 (mod360); these conditions are incompatible. These two permutations exhaust continuous rotations, not merely the answer choices.',
      'first_positive_CCW_angle':'Exactly theta=300+360k, k integer, achieves coverage. The first positive counterclockwise angle is300 degrees, option E. Clockwise60 is a different directed motion. The equilateral120 symmetry is about its centroid; it does not provide extra symmetry about fixed vertexA.',
      'wrong_preset':'120 degrees is the real undirected angle BAD (and BCD), not the directed angle giving whole-triangle coverage. At CCW120, neither moving nonpivot vertex lands at B or C. BAD is not straight, and no rotation about A sends distinct C to A.',
      'exact_arithmetic':'Fraction pairs in Q(sqrt(3)); no solver, numerical tolerance, fitted geometry or approximate equality.',
      'option_and_zero_enumeration':results,'colored_boundary_preserved_at_300':moved==target,
      'literal_color_reading':'Blue source AC/AD maps to target AB/AC, red source CD maps to red BC. Treating the annotations even as intrinsic boundary colors does not change or remove the unique300 answer. Fixed printed vertex identities would prevent rotating any labelled diagram as usual; the task uses labels as location names, unchanged from original.'}
    save('independent_math_proof.json',proof)
    printj(proof)

def support():
    import struct
    from PIL import Image
    import io
    def chunks(data):
        result=[]; offset=8
        while offset<len(data):
            size=struct.unpack('>I',data[offset:offset+4])[0]
            typ=data[offset+4:offset+8].decode('ascii')
            payload=data[offset+8:offset+8+size]
            result.append({'type':typ,'size':size,'sha256':hashlib.sha256(payload).hexdigest(),'text':payload.decode('latin1') if typ in ('tEXt','iTXt') else None})
            offset+=size+12
        return result
    diagnostic={}
    for name,p in [('noop',OWN/'noop_formal.png'),('formal',ROOT/'PlaneGeometry/image/Plane321.png'),('candidate',CANDIDATE/'candidate.png')]:
        data=p.read_bytes()
        with Image.open(io.BytesIO(data)) as image:
            diagnostic[name]={'size':list(image.size),'mode':image.mode,'rgba_sha256':hashlib.sha256(image.convert('RGBA').tobytes()).hexdigest(),'chunks':chunks(data)}
    with Image.open(OWN/'noop_formal.png') as a, Image.open(ROOT/'PlaneGeometry/image/Plane321.png') as b:
        assert a.convert('RGBA').tobytes()==b.convert('RGBA').tobytes()
    assert (OWN/'noop_formal.png').read_bytes()==(OWN/'noop_formal_after_serialization_correction.png').read_bytes()
    ref=read(REFERENCE/'reference.json')
    current_ref={}
    for name,item in ref['copied_files'].items():
        actual=sha(ROOT/item['source']); snapshot=sha(REFERENCE/name)
        current_ref[name]={'expected':item['sha256'],'snapshot':snapshot,'current':actual,'exact_equal':actual==snapshot==item['sha256']}
        assert current_ref[name]['exact_equal']
    original=(OLD/'harness/quicktest3_isolated.py').read_bytes()
    copied=(UNIT/'ownruntime/harness/quicktest3_isolated.py').read_bytes()
    old_line=b'PROJECT = Path(__file__).resolve().parents[3]'
    new_line=("PROJECT = Path("+repr(str(ROOT))+")").encode()
    assert original.count(old_line)==copied.count(new_line)==1
    assert copied.replace(new_line,old_line)==original
    ledger=read(UNIT/'complete_call_ledger.json')
    rows=[x for x in ledger['calls'] if x['question_id']=='Plane321']
    binding=read(OWN/'frozen_binding_audit.json')
    assert len(rows)==2
    for row,run in zip(rows,binding['runs']):
        assert row['run_id']==run['run_id'] and row['response_sha256']==run['raw_sha256']
    api=read(CANDIDATE/'api_process_finished.json')
    assert api['actual_urllib_request_events']==2 and api['all_synchronous_requests_returned'] is True
    assert api['child_processes_started']==api['servers_started']==0
    old_audit=read(CANDIDATE/'global_prior_request_audit.json')
    missing=[p for p in old_audit['scanned_sha256'] if not (ROOT/p).is_file()]
    queue=next(q for q in read(UNIT/'second_review_queue.json') if q['question_id']=='Plane321')
    assert queue['image_sha256']==sha(CANDIDATE/'candidate.png') and queue['plugin_sha256']==sha(CANDIDATE/'plugin.json') and queue['design_sha256']==sha(CANDIDATE/'design.json')
    parent=read(TASK/'parent_audits/native_u01_u04/audit.json')
    evidence=next(e for e in parent['evidence'] if e['question_id']=='Plane321')
    method=read(TASK/'parent_audits/native_u01_u04/method_fidelity.json')['Plane321']
    result={'created_at':now(),'png_serialization_diagnostic':diagnostic,'first_noop_failure':'Reviewer initially asserted noop PNG byte equality, beyond the requested no-op pixel check. Exact RGBA equality was already true. Original assertion error and first PNG are preserved. Own corrected code records byte inequality honestly and still requires byte-for-byte candidate equality; no source, adapter, numeric, key, order, path or pixel equality gate was relaxed.','current_reference_copies':current_ref,'canonical_harness_sha256':sha(OLD/'harness/quicktest3_isolated.py'),'copied_harness_sha256':sha(UNIT/'ownruntime/harness/quicktest3_isolated.py'),'reverse_project_locator_replacement_bytes_equal':True,'process_finished_record':api,'exact_candidate_ledger_calls':rows,'parent_audit_scoped_evidence':evidence,'parent_method_fidelity_objections_read':method,'primary_prefreeze_scan_non_file_references':missing,'primary_errors_preserved':[str(UNIT/'offline_error_01.json'),str(UNIT/'finalization_error_01.json')],'own_errors_preserved':[str(p) for p in sorted(OWN.glob('offline_error_*.json'))]}
    save('supporting_integrity_audit.json',result)
    printj({k:v for k,v in result.items() if k not in ['exact_candidate_ledger_calls','parent_audit_scoped_evidence']})

def archives():
    from zipfile import ZipFile
    prior=read(CANDIDATE/'global_prior_request_audit.json')
    verified=[]; matches=[]; errors=[]
    exact_question=read(QUESTION/'formal_record.json')['question']
    candidate_hash=sha(CANDIDATE/'candidate.png')
    for path,expected in prior['scanned_sha256'].items():
        if '::' not in path:
            assert sha(ROOT/path)==expected
            continue
        archive,member=path.split('::',1)
        with ZipFile(ROOT/archive,'r') as stream:
            data=stream.read(member)
        actual=hashlib.sha256(data).hexdigest()
        assert actual==expected
        request=json.loads(data)
        text=''; images=[]
        for m in request['messages']:
            if m['role']=='user' and isinstance(m['content'],list):
                for c in m['content']:
                    if c.get('type')=='text': text+=c['text']
                    if c.get('type')=='image_url': images.append(hashlib.sha256(base64.b64decode(c['image_url']['url'].split(',',1)[1],validate=True)).hexdigest())
        verified.append({'path':path,'sha256':actual})
        if text==exact_question or candidate_hash in images:
            matches.append({'path':path,'exact_question_match':text==exact_question,'candidate_match':candidate_hash in images})
    assert matches==[]
    save('archive_history_audit.json',{'created_at':now(),'prior_scan_entries_verified':len(prior['scanned_sha256']),'archive_request_entries_verified':verified,'same_question_or_same_candidate_matches':matches,'errors':errors,'archives_read_without_extraction':True})
    printj({'verified_prior_request_entries':len(prior['scanned_sha256']),'verified_archive_request_entries':len(verified),'matches':matches,'errors':errors})

def finalize_review():
    binding=read(OWN/'frozen_binding_audit.json')
    replay=read(OWN/'exact_replay.json')
    eligibility=read(OWN/'current_eligibility.json')
    preservation=read(OWN/'scoped_preservation_final.json')
    process=read(OWN/'process_closure_os.json')
    history_data=read(OWN/'old_history_read.json')
    scan=read(OWN/'request_history_scan.json')
    archive=read(OWN/'archive_history_audit.json')
    support_data=read(OWN/'supporting_integrity_audit.json')
    proof=read(OWN/'independent_math_proof.json')
    assert replay['candidate_bytes_equal'] and replay['noop_formal_pixels_equal'] and eligibility['eligible']
    assert not preservation['review_start_end_differences'] and not preservation['primary_historical_scoped_drift']
    assert not process['owned_review_python_processes']
    assert not scan['parse_errors'] and not archive['errors'] and not archive['same_question_or_same_candidate_matches']
    frozen=next(q for q in read(UNIT/'assignment.json')['questions'] if q['question_id']=='Plane321')
    assert eligibility['approval']==frozen['approval']
    assert read(ROOT/'provenance/approvals.json')['approvals']['Plane321']==eligibility['approval']
    plugin=read(CANDIDATE/'plugin.json'); context=read(QUESTION/'context.json')
    role_by_target={
      'o0':('AB','Target triangle ABC has blue A-incident leg AB. It receives moving blue AC at300; pairing it with shared AC shows the two pivot legs of the target.','Full top horizontal blue stroke visible, black label B and A clear.'),
      'o1':('BC','Target red base BC is opposite pivotA and receives source red CD at300. It is a real corresponding base, useful for comparing full triangle motion rather than only one outer ray.','Full lower-left sloped red edge visible, incidence atB andC unchanged.'),
      'o2':('AC','The existing common blue side participates in both leg pairs: source AC maps to target AB, while source AD maps to target AC. Shared visual location is not a claim that AC remains fixed during rotation.','Entire middle diagonal blue stroke visible. It is a single original segment, without double tracing or a new point at either endpoint.'),
      'o3':('AD','Source blue A-incident leg AD pairs with source AC and receives no invented extension; at300 it maps to target blue AC. This completes the same two-leg role grouping as the reference.','Full right sloped blue edge visible; D remains readable and geometry stays fixed.'),
      'o4':('CD','Source red base CD is opposite fixedA and maps to target red BC at300. The red pair supports genuine base correspondence. Its static120-degree opening atC is an existing angle, not the requested directed rotation.','Full bottom horizontal red stroke visible, C/D black labels clear; no cut or partition is drawn.')
    }
    marks=[]
    for action in plugin['params']['actions']:
        edge,info,human=role_by_target[action['target']]
        target=next(o for o in context['objects'] if o['id']==action['target'])
        marks.append({'target':action['target'],'edge':edge,'action_exact':action,'frozen_geometry':target['geometry'],'partial_interval':None,'actual_scope':'Entire existing segment; no partial interval supplied.','legal':'set_object_style on existing stable object, approved palette, whitelist1.5pt. Linestyle omitted, retaining solid original.','information':info,'native_human_review':human,'useful_in_correspondence_group':True,'overwritten_or_useless':False,'new_given_condition':False,'causal_necessity_established':False})
    readings=[]
    finals=[
      'The correct choice is **B: $120^{\\circ}$**.',
      'Therefore, the angle of rotation is $120^{\\circ}$.\n\nChoice: B'
    ]
    diagnoses=[
      'It initially selects the valid C->B correspondence, then contradicts its own equilateral BAC60 by inventing B,A,D collinearity and BAD180. It subtracts60 and incorrectly treats the result120 as the counterclockwise CAB sweep. Actually BAD120, CAB60 clockwise, and CAB300 counterclockwise. The trailing literal System Instruction: has no further mathematical answer or authority; service finish_reason is stop and raw text is intact.',
      'It incorrectly requires AD->AB, traverses two clockwise60 sectors while calling them counterclockwise, and then asserts C->A although distance from fixed pivotA is positive and must remain positive. At actual CCW120 neither nonpivot vertex reaches B or C. Its static60+60 narrative differs from run1 and does not prove the specific red-base mechanism.'
    ]
    for raw,final,diagnosis in zip(binding['runs'],finals,diagnoses):
        assert final in raw['raw_content']
        readings.append(dict(raw,complete_raw_response_personally_read=True,exact_final=final,final_letter='B',final_value_degrees='120',matches_frozen_preset=True,reasoning_divergence=diagnosis,entire_content_preserved=True))
    old_outcomes={
      'outer_rays':{'preset':'B','finals':['B120','D240'],'preset_hits':1},
      'outer_reflex':{'preset':'D','finals':['D240','B120'],'preset_hits':1},
      'short_sector':{'preset':'A','finals':['B120','D240'],'preset_hits':0},
      'vertex_correspondence':{'preset':'D','finals':['E300','B120'],'preset_hits':0}
    }
    for trial in history_data['old_frozen_trials']:
        old_outcomes[trial['variant_id']].update(candidate_sha256=trial['candidate_sha256'],calls=trial['calls'],failed_or_aborted=trial['incomplete'],retained_unchanged=True)
    evidence=next((CANDIDATE/'tests').glob('*/summary.json')).parent
    reviewed_paths=[CANDIDATE/'candidate.png',CANDIDATE/'plugin.json',CANDIDATE/'design.json',evidence/'summary.json',evidence/'binding.json',evidence/'request.json',evidence/'design_snapshot.json',CANDIDATE/'manual_final_review.json',CANDIDATE/'primary_review.json',CANDIDATE/'reference_transfer.json',QUESTION/'primary_math_proof.json',QUESTION/'exact_mathematical_checks.json',UNIT/'complete_call_ledger.json',UNIT/'readonly_preservation_final.json',TASK/'parent_audits/native_u01_u04/audit.json',TASK/'parent_audits/native_u01_u04/method_fidelity.json']
    report={
      'schema_version':'1.0','created_at':now(),'role':'NEW_INDEPENDENT_SECOND_REVIEW','decision':'recommended',
      'question_id':'Plane321','variant_id':CANDIDATE.name,'candidate_directory':str(CANDIDATE),'own_writable_root':str(OWN),
      'candidate_png_path':str(CANDIDATE/'candidate.png'),'candidate_png_sha256':sha(CANDIDATE/'candidate.png'),'plugin_path':str(CANDIDATE/'plugin.json'),'plugin_sha256':sha(CANDIDATE/'plugin.json'),'design_path':str(CANDIDATE/'design.json'),'design_sha256':sha(CANDIDATE/'design.json'),'summary_path':str(evidence/'summary.json'),'summary_sha256':sha(evidence/'summary.json'),
      'recommendation_meaning':'Research recommendation for this exact frozen image and two recorded preset hits only. It is not original-question approval, user Special approval, Pass, Collect, publication, or permission to modify any authoritative source.',
      'independence':{'designed_candidate':False,'tested_candidate_with_model':False,'child_agent_used':False,'provider_or_model_switched':False,'new_solver_api_calls':0,'scope_expanded':False,'new_alternative_created':False,'parent_reports_used_as_proof':False},
      'method_fidelity':{'classification':'close imitation','current_reference':'Plane427 CURRENT user C01','reference_png_sha256':sha(REFERENCE/'C01.png'),'reference_plugin_sha256':sha(REFERENCE/'C01.json'),'actual_reference_viewed_native':True,'actual_reference_plugin_read':True,'reference_actions_exact':read(REFERENCE/'C01.json')['params']['actions'],'observation':'Current reference has ST and TV red, dotted SV base blue, with original70 and requested-angle arcs retained. o0 interval start0.3333333333333333 end0.6666666666666666 wrapfalse selects ST in R-S-T-R; o1 start0 end0.6666666666666665 wraptrue selects TV in T-U-V-T. These exact saved parameters and path hashes are retained; no rounding or replacement from old18.','transfer':'Candidate uses the same pivot-incident two-leg group versus opposite-base group on each existing equilateral triangle. Blue AC/AD and AB/AC are leg pairs; red CD and BC are corresponding opposite bases. Palette roles are swapped relative to current reference; this is acknowledged and does not change the transferred geometric comparison. Five existing segments and uniform1.5pt width are a modest application to the two-triangle scene.','why_close':'It repeats the same existing-edge role comparison, without auxiliary lines, dots, synthetic partition, option coloring, or invented relationships. All colored edges preserve the correct rigid mapping.','not_a_mechanism_claim':'120 static opening is an intelligible possible confusion, but two narratives do not establish that the exact frozen proposed mechanism occurred.'},
      'native_visual_review':{'view_image_detail':'original','images_personally_viewed':[{'path':str(REFERENCE/'C01.png'),'resolution':[768,768]},{'path':str(QUESTION/'source.jpg'),'resolution':[540,388]},{'path':str(QUESTION/'formal.png'),'resolution':[768,768]},{'path':str(CANDIDATE/'candidate.png'),'resolution':[768,768]}],'source_snapshot_equals_current_JPG':sha(QUESTION/'source.jpg')==sha(ROOT/'PlaneGeometry/originals/Plane321.jpg'),'formal_snapshot_equals_current_PNG':sha(QUESTION/'formal.png')==sha(ROOT/'PlaneGeometry/image/Plane321.png'),'observations':'Five original solid segments, white interiors/background, and four black vertex labels remain clearly visible. No arrows, arcs, angle numbers, ticks, dots, new cuts, printed pattern or text are added to Plane321. The line width is modest and no label is occluded. Original target has no dashes, semantic gray or fill to preserve.','every_mark_review':marks,'same_color_interpretation':'Annotations compare true roles and correspondence; they do not assert new equalities or extra geometric givens. All five original sides are already equal from the two equilateral conditions and sharedAC.','literal_material_color_check':'Even if red/blue are read as intrinsic edge printing, the source blue-blue-red boundary maps exactly to the target blue-blue-red boundary at300. Unique answer unchanged. No reasonable extra color reading supplies120 as a full-coverage solution.','three_dimensional_world_geometry':'Not applicable to this planar problem. Frozen2D geometry, viewport projection, connectivity and original solid visibility are independently unchanged, as exact context and no-op pixel equality verify.'},
      'original_mathematical_proof':proof,'original_answer':{'letter':'E','degrees':'300','independently_proved':True},'frozen_wrong_preset':{'letter':'B','degrees':'120','created_at':binding['preset_created_at'],'before_both_calls':True},
      'complete_final_readings':readings,'frozen_integrity':binding,'exact_offline_replay':replay,'current_eligibility':eligibility,
      'history_audit':{'old_trials':old_outcomes,'old_complete_raw_contents_personally_read':8,'current_candidate_actual_calls':2,'current_candidate_complete_calls':2,'new_current_call_errors_or_aborts':0,'separate_old_images_not_rerun':True,'partial_hits_preserved':'Old outer_rays B/D and outer_reflex D/B remain partial hits, not two-hit successes. All unsuccessful variants retain original presets, raw records and images.','substantive_difference':'The new candidate creates actual corresponding red opposite-base pair BC/CD and blue pivot-leg groups for both triangles. Earlier trials highlighted outer AB/AD rays or short AB/AC sector or added B/D point markers. This is a real role partition change, with color-preserving correct mapping, rather than a filename, width-only or recoloring-only reattempt of an old failed PNG.','request_scan':str(OWN/'request_history_scan.json'),'archive_scan':str(OWN/'archive_history_audit.json'),'saved_runtime_request_files_scanned':scan['runtime_request_files_scanned'],'prefreeze_request_entries_hash_verified':archive['prior_scan_entries_verified'],'zip_request_entries_verified':len(archive['archive_request_entries_verified']),'same_question_current_PNG_request_directories':1,'hidden_third_call_or_selection_found':False,'cross_id':'No same-candidate cross-ID request appeared. Authorized current-nine reference transfer is provenance, and exact question/options were compared independently of image.'},
      'objections_and_corrections':[
        {'issue':'Current reference palette differs from old18 and candidate swaps it.','disposition':'Resolved by personally viewing current C01 and plugin, checking current source byte equality, and comparing true pivot-leg/base roles. Report explicitly records reference redlegs/bluebase and candidate bluelegs/redbases. No old label/color is silently substituted.'},
        {'issue':'Two incorrect narratives do not verify proposed mechanism.','disposition':'Retained limitation. Run1 fabricates collinearity; run2 uses impossible vertex mapping and reversed directed sectors. Both unambiguous final letter/value pairs nonetheless equal frozenB120, with full stop-completed raw records. No causal conclusion is asserted.'},
        {'issue':'Run1 ends with literal System Instruction:.','disposition':'No competing answer follows. It is untrusted response text, not an instruction and not evidence of truncation. Raw finish_reasonstop, HTTP200 and complete content equality are verified; exact tail is preserved.'},
        {'issue':'Reviewer first imposed noop PNG byte equality.','disposition':'Own original error and initialPNG preserved. Exact pixels and IDAT payloads already matched; only Software text metadata differs between workbench and formal serializer. Own audit records bytefalse and pixeltrue honestly. Frozen candidatePNG still passes exact byte equality. No source or drawing/schema/adapter change; no numerical tolerance.'},
        {'issue':'Existing partial/failed history and ordinary runtime scaffolding must not become approval.','disposition':'Old four designs/eight calls and two parent reporting errors are retained. Canonical harness reversal confirms only local project locator differs. Runtime scaffolding is process isolation, not formal-question or Special approval.'}
      ],
      'blocking_objections':[],
      'limitations':[
        'Two observed hits establish neither a general success rate, causal/statistical gain, reliable internal reasoning mechanism, nor each individual mark\'s causal necessity.',
        'No control call was made. Correct controls or incremental causal gain are not imposed as extra hard criteria; useful informational correspondence and clarity were reviewed independently of model failure.',
        'Saved records, request bytes, 2 started records, 2 complete raws, ledger and 2 urllib events support exactly the recorded two calls. Offline artifacts cannot establish absence of entirely unrecorded external provider activity.',
        'Preservation is scoped to164 snapshotted files,60 relevant primary historical records, approved target/reference source fingerprints, and examined request archives. Mutable parent progress or unrelated user workbench files are not claimed globally unchanged.',
        'The report authorizes no Pass, Collect, publication, source edit, resumed old exploration, alternative design or further model request.'
      ],
      'source_preservation':preservation,'process_closure':dict(process,final_report_python_run='Synchronous offline finalizer only; no persistent/background process or child created; command completion is recorded by the invoking tool.'),
      'source_evidence_hashes':{str(p):sha(p) for p in reviewed_paths},
      'own_evidence_hashes':{p.name:sha(p) for p in OWN.glob('*.json') if p.name!='independent_review.json'},
      'own_offline_errors_preserved':support_data['own_errors_preserved'],'all_audit_corrections_only_in_own_root':True,
      'user_approval_or_Pass_Collect_record_written':False
    }
    save('independent_review.json',report)
    printj({'decision':report['decision'],'question_id':report['question_id'],'variant_id':report['variant_id'],'method_fidelity':report['method_fidelity']['classification'],'report':str(OWN/'independent_review.json'),'report_sha256':sha(OWN/'independent_review.json'),'original':'E300','finals':['B120','B120'],'candidate_exact_byte_replay':True,'no_op_exact_formal_pixels':True,'current_eligible':True,'preserved_scoped_files':preservation['scoped_file_count'],'user_approval_or_Pass_Collect':False})

if __name__=='__main__':
    try:
        globals()[sys.argv[1]]()
    except BaseException:
        original=traceback.format_exc()
        error=OWN/('offline_error_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%f')+'.json')
        save(error.name,{'created_at':now(),'mode':sys.argv[1:],'traceback':original,'original_error_preserved':True})
        raise
