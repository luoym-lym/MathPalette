"""Read-only independent review; all writes restricted to this new review root."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
ROOT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
BASE = ROOT / 'runtime/mathvision_special_20261101'
CAND = BASE / 'background_19/Plane342/quarterturn_wedge_edge_binding'
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
for key, folder in {'TEMP':'tmp', 'TMP':'tmp', 'TMPDIR':'tmp', 'MPLCONFIGDIR':'mplcache',
                    'XDG_CACHE_HOME':'cache', 'PYTHONPYCACHEPREFIX':'pycache'}.items():
    destination = OWN / folder
    destination.mkdir(exist_ok=True)
    os.environ[key] = str(destination)

def check_write(path):
    if path is None or isinstance(path, int):
        return
    if not Path(os.fsdecode(path)).resolve().is_relative_to(OWN):
        raise PermissionError('Review write outside assigned root: ' + str(path))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(args[0])
        if not isinstance(args[0], int) and Path(os.fsdecode(args[0])).name == '.env':
            raise PermissionError('Review never reads .env')
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
    elif event in ('socket.connect','socket.getaddrinfo','subprocess.Popen','os.system'):
        raise PermissionError('No network or subprocess allowed during this independent audit')

sys.addaudithook(guard)
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp', guard_writes=True)

import json
import hashlib
import base64
from datetime import datetime, timezone

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()] if Path(path).exists() else []

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest() if Path(path).is_file() else None

def canon(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def write(name, data):
    with (OWN / name).open('w', encoding='utf-8', newline='\n') as stream:
        json.dump(data,stream,ensure_ascii=False,indent=2,allow_nan=False)
        stream.write('\n')

def shortened(value, depth=0):
    if isinstance(value, dict):
        if len(value)>30:
            return {'mapping_length':len(value),'canonical_sha256':canon(value)}
        return {key:shortened(item,depth+1) for key,item in value.items()}
    if isinstance(value, list) and len(value)>12:
        return {'array_length':len(value),'first':shortened(value[:2],depth+1),'last':shortened(value[-2:],depth+1)}
    if isinstance(value,list):
        return [shortened(item,depth+1) for item in value]
    return value

def inspect():
    out = {'isolation':ISOLATION,'strict_guard_before_project_imports':True}
    for name in ['render_check.json','fresh_context.json']:
        data=read(CAND/name)
        out[name]=shortened(data) if name=='render_check.json' else {'keys':list(data),'non_objects':{k:shortened(v) for k,v in data.items() if k not in ('objects','canvas','snap_points')},'canvas_keys':list(data.get('canvas',{}))}
    scene=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane342.json')
    out['formal_scene']=shortened(scene)
    context=read(CAND/'fresh_context.json')
    out['targets']=[x for x in context['objects'] if x.get('id') in ('o2','o216')]
    canvas=context.get('canvas',{})
    out['canvas_meta']={k:shortened(v) for k,v in canvas.items() if k not in ('targets','snap_points')}
    out['canvas_targets']=[x for x in canvas.get('targets',[]) if x.get('id') in ('o2','o216')]
    write('inspection.json',out)
    print(json.dumps(out,ensure_ascii=False))

def eligibility():
    from dataset_tools.catalog import content, digest, validate_formal_row
    branch=ROOT/'PlaneGeometry'
    record=next(x for x in rows(branch/'dataset.jsonl') if x['id']=='Plane342')
    validate_formal_row(ROOT,'PlaneGeometry',record)
    approval=read(ROOT/'provenance/approvals.json')['approvals']['Plane342']
    actual=digest(content(ROOT,'PlaneGeometry',record))
    accepted=[x for x in rows(branch/'special_variant/accepted_index.jsonl') if x.get('question_id',x.get('id'))=='Plane342']
    collected=[x for x in rows(branch/'special_variant/collected_index.jsonl') if x.get('question_id',x.get('id'))=='Plane342']
    paths=[branch/'dataset.jsonl',ROOT/'provenance/approvals.json',ROOT/'provenance/source_notes.json',
           branch/'special_variant/accepted_index.jsonl',branch/'special_variant/collected_index.jsonl',
           branch/'special_variant/Plane342/recipes.json',branch/'special_variant/Plane342/collection.json']
    variants=branch/'special_variant/Plane342'
    state={'checked_at':datetime.now(timezone.utc).isoformat(),'record':record,'record_sha256':canon(record),
        'approval':approval,'recomputed_current_content_sha256':actual,
        'approval_matches':actual==approval.get('content_sha256') and approval.get('reviewer')=='user' and bool(approval.get('instruction')) and bool(approval.get('approved_at_utc')),
        'accepted_target_entries':accepted,'collected_target_entries':collected,
        'target_special_directory_exists':variants.exists(),
        'target_special_files':[str(x.relative_to(ROOT)) for x in variants.rglob('*') if x.is_file()] if variants.exists() else [],
        'state_hashes':{str(x.relative_to(ROOT)):sha(x) for x in paths}}
    state['formalMathVision']=record['source_dataset']=='MathVision'
    state['noPass']=not accepted and not (variants/'recipes.json').exists()
    state['notCollected']=not collected and not (variants/'collection.json').exists()
    state['noSpecialCompletion']=not collected and not (variants/'collection.json').exists()
    state['eligible']=all(state[x] for x in ('formalMathVision','noPass','notCollected','noSpecialCompletion','approval_matches'))
    return state

def audit():
    from PIL import Image
    import io
    import copy
    evidence=next((CAND/'tests').glob('quicktest3_*'))
    binding=read(evidence/'binding.json')
    design=read(CAND/'design.json')
    request=read(evidence/'request.json')
    current=eligibility()
    local_files=[x for x in CAND.rglob('*') if x.is_file()]
    local_files += [CAND.parent/name for name in ('context.json','input_fingerprints.json','source_audit_final.json','formal_record.json','source_scene_snapshot.json','original.png','source_original.jpg','eligibility_start.json')]
    local_files += [BASE/'runtime_isolation.py',BASE/'Plane342_firstpass_independent_review_brief.txt',BASE/'Plane342_pre_review_evidence_check.json',BASE/'background_19/second_review_queue.json',BASE/'background_19/tools19.py',BASE/'background_19/run19.py',BASE/'background_19/harness/quicktest3_isolated.py',BASE/'harness/quicktest3_isolated.py',ROOT/'PlaneGeometry/workbench/quick_test.py',ROOT/'PlaneGeometry/workbench/plugin.schema.json']
    initial_hashes={str(p.relative_to(ROOT)):sha(p) for p in local_files}
    image_bytes=(CAND/'candidate.png').read_bytes()
    with Image.open(io.BytesIO(image_bytes)) as image:
        rgba=image.convert('RGBA')
        pixel_hash=hashlib.sha256(b'768x768:RGBA:'+rgba.tobytes()).hexdigest()
        image_info={'size':list(image.size),'mode':image.mode,'alpha_extrema':list(rgba.getextrema()[3]),'file_sha256':sha(CAND/'candidate.png'),'pixel_sha256':pixel_hash}
    payload_expected={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},'messages':[
       {'role':'system','content':binding['system_prompt']},
       {'role':'user','content':[{'type':'text','text':current['record']['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode(image_bytes).decode('ascii')}}]}]}
    expected_request_bytes=json.dumps(payload_expected,ensure_ascii=False).encode('utf-8')
    runs=[]
    for i in (1,2):
        started=read(evidence/f'run_{i:02d}_started.json')
        run=read(evidence/f'run_{i:02d}.json')
        raw=read(evidence/f'run_{i:02d}_response.json')
        raw_content=raw['choices'][0]['message']['content']
        fields=('run_index','run_id','started_at','request_body_sha256','image_sha256','design_sha256')
        item={'run':i,'record':run,'started_record':started,'raw_id':raw['id'],'raw_created':raw['created'],
              'raw_response_sha256_actual':sha(evidence/f'run_{i:02d}_response.json'),
              'raw_sha_matches':sha(evidence/f'run_{i:02d}_response.json')==run['response_sha256'],
              'full_raw_assistant_content':raw_content,'content_sha256':hashlib.sha256(raw_content.encode()).hexdigest(),
              'raw_content_matches_run_record':raw_content==run['answer'],
              'started_fields_match_completed':all(started[k]==run[k] for k in fields),
              'same_frozen_request_image_design':all(run[k]==binding[k] for k in ('request_body_sha256','image_sha256','design_sha256')),
              'completed':run['status']=='completed' and run['http_status']==200 and not run['truncated'] and raw['choices'][0]['finish_reason']=='stop',
              'model_and_thinking_observed':{'model':raw['model'],'reasoning_tokens':raw['usage']['completion_tokens_details']['reasoning_tokens'],'reasoning_content':raw['choices'][0]['message'].get('reasoning_content','')}}
        runs.append(item)
    summary=read(evidence/'summary.json')
    invocations=[]
    for p in BASE.rglob('binding.json'):
        if p.is_relative_to(OWN):continue
        data=read(p)
        if data.get('question_id')=='Plane342' or data.get('image_sha256')==binding['image_sha256']:
            invocations.append({'binding_path':str(p.relative_to(ROOT)),'binding_sha256':sha(p),
                'image_sha256':data.get('image_sha256'),'design_sha256':data.get('design_sha256'),
                'started_files':[x.name for x in p.parent.glob('run_*_started.json')],
                'run_files':[x.name for x in p.parent.glob('run_*.json') if x.stem[4:].isdigit()],
                'response_files':[x.name for x in p.parent.glob('run_*_response.json')],
                'incomplete_files':[x.name for x in p.parent.glob('*incomplete*')]})
    old_inputs=read(CAND.parent/'input_fingerprints.json')
    rendercheck=read(CAND/'render_check.json')
    relevant=set(current['record']['runtime_dependencies'])
    relevant.update(current['record'][k] for k in ('image','original_image','scene','script'))
    relevant.update(('dataset_generator/common_renderer.py','dataset_generator/protocol.json','workbench/mathvision_adapter.py','workbench/mathvision_plugins.py','workbench/partial_style.py','workbench/plugin.schema.json','workbench/render_plugins.py','workbench/renderer_adapter.py','workbench/drawing_board.py','workbench/workbench_io.py'))
    frozen={}
    for rel in sorted(relevant):
        key=str(Path('PlaneGeometry')/rel)
        old=old_inputs['files'].get(key)
        frozen[key]={'current_sha256':sha(ROOT/key),'historical_sha256':old,'matches_historical':sha(ROOT/key)==old if old else None}
    for key in ('dataset_tools/geometry_dataset.py','dataset_tools/mathvision_workbench.py'):
        old=old_inputs['files'].get(str(Path(key)))
        frozen[key]={'current_sha256':sha(ROOT/key),'historical_sha256':old,'matches_historical':sha(ROOT/key)==old if old else None}
    scene=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane342.json')
    scene_items=[o for o in scene['objects'] if o.get('semantic_fill') or o['id'] in ('o0','o1','o3') or int(o['id'][1:])>=200]
    checks={
        'request_exact_reconstruction_matches_object':request==payload_expected,
        'request_exact_reconstruction_matches_bytes':(evidence/'request.json').read_bytes()==expected_request_bytes,
        'request_sha256_matches_binding':sha(evidence/'request.json')==binding['request_body_sha256'],
        'candidate_sha256_matches_binding':sha(CAND/'candidate.png')==binding['image_sha256'],
        'candidate_pixel_sha256_matches_binding':pixel_hash==binding['pixel_sha256'],
        'design_sha256_matches_binding':sha(CAND/'design.json')==binding['design_sha256'],
        'design_snapshot_bytes_identical':(CAND/'design.json').read_bytes()==(evidence/'design_snapshot.json').read_bytes(),
        'preset_D_both_design_and_binding':design['expected_wrong_answer']==binding['expected_wrong_answer']=='D',
        'preset_created_before_binding_and_both_starts':design['created_at']<binding['created_at']<runs[0]['record']['started_at']<runs[1]['record']['started_at'],
        'question_matches_formal':binding['question']==current['record']['question'],
        'question_record_sha256_matches_current':binding['question_record_sha256']==canon(current['record']),
        'frozen_formal_record_matches_current':read(CAND.parent/'formal_record.json')==current['record'],
        'reference_quick_test_sha256_matches':binding['reference_quick_test_sha256']==sha(ROOT/'PlaneGeometry/workbench/quick_test.py'),
        'summary_binding_fields_match':all(summary[k]==v for k,v in binding.items()),
        'summary_results_match_actual_runs':summary['results']==[r['record'] for r in runs],
        'two_completed_same_binding':summary['two_completed'] and binding['requested_runs']==2 and all(r['completed'] and r['same_frozen_request_image_design'] and r['raw_sha_matches'] and r['raw_content_matches_run_record'] and r['started_fields_match_completed'] for r in runs),
        'rendercheck_frozen_inputs_before_after_equal':rendercheck['frozen_inputs_before']==rendercheck['frozen_inputs_after'],
        'formal_scene_snapshot_equal':scene==read(CAND.parent/'source_scene_snapshot.json'),
        'source_jpg_snapshot_bytes_equal':(ROOT/'PlaneGeometry/originals/Plane342.jpg').read_bytes()==(CAND.parent/'source_original.jpg').read_bytes(),
        'formal_png_snapshot_bytes_equal':(ROOT/'PlaneGeometry/image/Plane342.png').read_bytes()==(CAND.parent/'original.png').read_bytes(),
        'no_relevant_frozen_input_mismatch':not any(x['matches_historical'] is False for x in frozen.values()),
        'one_saved_invocation_two_completed_no_incomplete':len(invocations)==1 and len(invocations[0]['started_files'])==2 and len(invocations[0]['run_files'])==2 and len(invocations[0]['response_files'])==2 and not invocations[0]['incomplete_files'],
    }
    result={'reviewed_at':datetime.now(timezone.utc).isoformat(),'isolation':ISOLATION,'eligibility_initial':current,
        'binding':binding,'question_text_sha256':hashlib.sha256(current['record']['question'].encode()).hexdigest(),
        'image':image_info,'checks':checks,'runs':runs,'invocation_search':invocations,
        'no_leak_request':{'top_level_keys':list(request),'messages':[{'role':m['role'],'content':m['content'] if isinstance(m['content'],str) else [{'type':c['type'],'text':c['text']} if c['type']=='text' else {'type':c['type'],'url':'data:image/png;base64,<exact frozen candidate>'} for c in m['content']]} for m in request['messages']],
           'preset_answer_intent_plugin_source_absent':request==payload_expected,'no_max_tokens_or_completion_limit':not any(k in request for k in ('max_tokens','max_completion_tokens'))},
        'render_check_summary':{k:v for k,v in rendercheck.items() if k not in ('frozen_inputs_before','frozen_inputs_after')},
        'frozen_relevant_inputs':frozen,'all_evidence_initial_hashes':initial_hashes,'scene_card_objects':scene_items,
        'historical_aggregate_state_differences':{k:{'historical':v,'current':sha(ROOT/k)} for k,v in old_inputs['files'].items() if k in [str(Path(x)) for x in ('PlaneGeometry/dataset.jsonl','provenance/approvals.json','provenance/source_notes.json')] and sha(ROOT/k)!=v}}
    write('evidence_audit.json',result)
    print(json.dumps({'checks':checks,'eligibility':{k:current[k] for k in ('eligible','formalMathVision','noPass','notCollected','noSpecialCompletion','approval_matches')},'approval':current['approval'],'image':image_info,'invocations':invocations,'scene_card_objects':scene_items},ensure_ascii=False))

def render():
    sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
    from workbench_io import load_config, pixel_hash, environment_versions
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from partial_style import object_paths, apply_partial_styles
    from dataset_tools.mathvision_workbench import png_bytes
    import matplotlib.pyplot as plt
    import numpy as np
    from PIL import Image
    import io
    cfg=load_config()
    cfg['runtime_dir']=str(OWN/'render_state')
    cfg['output_dir']=str(OWN/'render_output')
    ad=RendererAdapter(cfg)
    context=ad.inspect_question('Plane342')
    plugin=read(CAND/'plugin.json')
    renderer=PluginRenderer(cfg,ad,{'Plane342':context})
    normalized=renderer.normalize(plugin)
    scene=ad.scene('Plane342')
    paths=[]
    try:
        baseline=png_bytes(scene)
        text_before=[(t.get_text(),list(t.get_position()),t.get_color()) for t in scene.ax.texts]
        fills_before=[(str(p.get_facecolor()),p.get_fill(),p.get_path().vertices.tolist(),p.get_transform().get_matrix().tolist()) for p in scene.ax.patches if p.get_fill()]
        for a in plugin['params']['actions']:
            actual=object_paths(scene,a['target'])
            p=next(p for p in actual if p['id']==a['interval']['path_id'])
            paths.append({'target':a['target'],'path_id':p['id'],'sha256_actual':p['sha256'],'sha256_expected':a['interval']['path_sha256'],
                'segments':[s['control'].tolist() for s in p['segments']],
                'styles':[s['style'] for s in p['segments']],
                'closed':p['closed'],'selected_segment_indices':[1,2]})
        apply_partial_styles(scene,plugin['params']['actions'])
        after_direct=png_bytes(scene)
        text_after=[(t.get_text(),list(t.get_position()),t.get_color()) for t in scene.ax.texts]
        fills_after=[(str(p.get_facecolor()),p.get_fill(),p.get_path().vertices.tolist(),p.get_transform().get_matrix().tolist()) for p in scene.ax.patches if p.get_fill()]
    finally:
        scene.close()
    p1,data1,h1=renderer.render(normalized,frozen=True)
    p2,data2,h2=renderer.render(normalized,frozen=True)
    (OWN/'native_no_op.png').write_bytes(baseline)
    (OWN/'native_candidate.png').write_bytes(data1)
    formal=np.array(Image.open(ROOT/'PlaneGeometry/image/Plane342.png').convert('RGBA'))
    candidate=np.array(Image.open(io.BytesIO(data1)).convert('RGBA'))
    yy,xx=np.where(np.any(candidate!=formal,axis=2))
    boxes=[]
    for label,selection in [('source',yy<350),('D',yy>450)]:
        xs,ys=xx[selection],yy[selection]
        boxes.append({'label':label,'changed_pixels':int(len(xs)),'bounding_box_inclusive':[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())]})
    source_crop=(352,206,430,282)
    optionD_crop=(487,465,583,560)
    # Diagnostic copies stay in the assigned review directory; original images are never saved over.
    im=Image.open(io.BytesIO(data1))
    im.crop(source_crop).resize((468,456)).save(OWN/'source_detail.png')
    im.crop(optionD_crop).resize((480,475)).save(OWN/'D_detail.png')
    plt.close('all')
    checks={'actual_normalization_identical':normalized==plugin,'normalization_idempotent':renderer.normalize(normalized)==normalized,
       'fresh_context_matches_frozen_context':context==read(CAND/'fresh_context.json'),
       'no_op_pixel_equal_formal':pixel_hash(baseline)==pixel_hash(ROOT/'PlaneGeometry/image/Plane342.png'),
       'new_native_candidate_byte_equal_frozen':data1==(CAND/'candidate.png').read_bytes(),
       'two_new_renders_byte_identical':data1==data2,'direct_partial_render_matches':after_direct==data1,
       'text_artists_unchanged':text_before==text_after,'filled_artist_geometry_facecolors_transforms_unchanged':fills_before==fills_after,
       'actual_path_hashes_match':all(p['sha256_actual']==p['sha256_expected'] for p in paths),
       'all_changed_pixels_in_two_mark_neighborhoods':bool(np.all(((xx>=357)&(xx<=395)&(yy>=209)&(yy<=279))|((xx>=491)&(xx<=578)&(yy>=508)&(yy<=555)))),
       'all_matplotlib_figures_closed':not plt.get_fignums()}
    result={'created_at':datetime.now(timezone.utc).isoformat(),'checks':checks,'paths':paths,'image_hash':h1,
         'candidate_sha256':hashlib.sha256(data1).hexdigest(),'baseline_pixel_hash':pixel_hash(baseline),
         'environment':environment_versions(),'changed_pixel_count':len(xx),'changed_pixel_boxes':boxes,'new_solver_calls':0}
    write('native_render_audit.json',result)
    print(json.dumps(result,ensure_ascii=False))

def finalize():
    evidence=read(OWN/'evidence_audit.json')
    rendered=read(OWN/'native_render_audit.json')
    assert all(evidence['checks'].values())
    assert all(rendered['checks'].values())
    current=eligibility()
    assert current['eligible']
    changes=[{'path':rel,'before':before,'after':sha(ROOT/rel)} for rel,before in evidence['all_evidence_initial_hashes'].items() if sha(ROOT/rel)!=before]
    relevant_changes=[{'path':rel,'before':before['current_sha256'],'after':sha(ROOT/rel)} for rel,before in evidence['frozen_relevant_inputs'].items() if sha(ROOT/rel)!=before['current_sha256']]
    assert not changes and not relevant_changes
    sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
    import quick_test
    config=read(ROOT/'PlaneGeometry/workbench/config.json')
    actual_settings={**quick_test.TEST_PROFILES['quicktest3'],'api_base':config['quick_test']['mimo_api_base']}
    profile={'profile':'quicktest3','current_settings':actual_settings,'profile_canonical_sha256':canon(actual_settings),
        'settings_equal_binding':actual_settings==evidence['binding']['settings'],
        'system_prompt_equal_binding':quick_test.SYSTEM_PROMPT==evidence['binding']['system_prompt'],
        'quick_test_source_sha256':sha(ROOT/'PlaneGeometry/workbench/quick_test.py'),
        'config_sha256':sha(ROOT/'PlaneGeometry/workbench/config.json'),
        'api_key_loader_never_called':True,'module_import_did_not_call_model':True}
    assert profile['settings_equal_binding'] and profile['system_prompt_equal_binding']
    scene=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane342.json')
    objects={o['id']:o for o in scene['objects']}
    def normalize(points,frame):
        x0=min(p[0] for p in frame); x1=max(p[0] for p in frame)
        y0=min(p[1] for p in frame); y1=max(p[1] for p in frame)
        assert abs((x1-x0)-(y1-y0))<1e-10
        return [[round((p[0]-x0)/(x1-x0),12),round((p[1]-y0)/(y1-y0),12)] for p in points]
    initial=normalize(objects['o2']['points'],objects['o1']['points'])
    diagonal=normalize(objects['o3']['points'],objects['o1']['points'])
    halfturn=lambda points:[[round(1-x,12),round(1-y,12)] for x,y in points]
    required=halfturn(initial)
    required_diag=halfturn(diagonal)
    same=lambda a,b:sorted(a)==sorted(b)
    option_data=[]
    names={'A':('left','SW-NE'),'B':('right','NW-SE'),'C':('top','NW-SE'),'D':('bottom','SW-NE'),'E':('bottom','NW-SE')}
    for i,letter in enumerate('ABCDE'):
        frame=objects[f'o{203+4*i}']['points']
        wedge=normalize(objects[f'o{204+4*i}']['points'],frame)
        diag=normalize(objects[f'o{205+4*i}']['points'],frame)
        option_data.append({'choice':letter,'wedge':wedge,'wedge_side':names[letter][0],
            'full_diagonal':diag,'full_diagonal_direction':names[letter][1],
            'wedge_matches_halfturn':same(wedge,required),'full_diagonal_matches_halfturn':same(diag,required_diag),
            'matches_required_black_white_geometry':same(wedge,required) and same(diag,required_diag),
            'has_red_V':letter=='D'})
    assert [o['choice'] for o in option_data if o['matches_required_black_white_geometry']]==['B']
    quarterturn=lambda points:[[round(1-y,12),round(x,12)] for x,y in points]
    d=next(o for o in option_data if o['choice']=='D')
    math={'method':'Independent actual-image reading followed by normalized frozen-vector verification; no stored answer is used in the derivation.',
       'coordinate_convention':'Normalize each inner printed square to [0,1]^2, x right and y up. This removes only display size/translation; both source and choices have square frames.',
       'initial_black_triangle':initial,'initial_full_diagonal':diagonal,
       'downward_flip':'F_down(x,y)=(x,1-y). The printed front is then facing away; the visible reverse is plain white, as actually shown. A visible black wedge on this intermediate reverse would be wrong.',
       'rightward_flip':'F_right(x,y)=(1-x,y). The second face change returns the printed front to the viewer.',
       'composition':'F_right(F_down(x,y))=(1-x,1-y), a half-turn; these are perpendicular 180-degree spatial flips, not one or two 90-degree planar turns.',
       'required_black_triangle':required,'required_full_diagonal':required_diag,
       'choice_comparison':option_data,'unique_original_answer':'B','agrees_with_formal_answer_after_derivation':current['record']['answer']=='B',
       'D_is_a_quarterturn_not_two_flips':same(quarterturn(initial),d['wedge']) and same(quarterturn(diagonal),d['full_diagonal']),
       'printed_red_interpretation':{'source_red_path_local':[[0,0],[0.5,0.5],[0,1]],
          'required_after_two_flips':[[1,1],[0.5,0.5],[1,0]],
          'actual_D_red_path_local':[[1,0],[0.5,0.5],[0,0]],
          'options_with_required_right_red_V':[],
          'exact_color_and_geometry_matching_choice':None}}
    markers=[]
    for i,(action,path) in enumerate(zip(read(CAND/'plugin.json')['params']['actions'],rendered['paths']),1):
        source=i==1
        markers.append({'index':i,'exact_action':action,'source_feature':'original printed left black wedge' if source else 'option D printed bottom black wedge',
            'actual_path':path,'selected_path_order':'source BL -> center -> TL' if source else 'D BR -> center -> BL',
            'geometry_excluded_from_selection':'The source vertical left base and D horizontal bottom base are excluded. These are two interior sloping triangle edges, not square-card borders.',
            'operation_legal':True,'normalization_idempotent':True,'path_sha256_verified_against_fresh_native_capture':True,
            'endpoints_unchanged':True,'parameter_meaning':'1/3..1 selects segments 1 and 2 of a closed three-edge polygon, in ordered segment coordinates; wrap=false.',
            'style':'Allowed #DC2626, allowed 2 pt; no linestyle key, so original solid line style is retained. At 100 dpi the nominal stroke is 2.78 pixels.',
            'informational_role':'Makes the actual two source wedge diagonals an orientation reference.' if source else 'Binds the bottom wedge diagonals of D to the source diagonals, a specific erroneous quarter-turn correspondence.',
            'targeting_disposition':'Substantive local feature correspondence, not a whole-choice outline or arbitrary salience; both actions have distinct comparison roles.',
            'native_size_clarity':'Clearly visible; no new point, relation glyph, text, filled region, closed cut or extra diagonal. On the leg shared with the full diagonal, the original 1 pt black diagonal remains as a black core over the 2 pt red rim.',
            'human_semantics_disposition':'Visible red ink is co-located with the printed pattern, and the supplied image/question has no cue separating it from card content. The source red V has no correctly transformed counterpart in B.' if source else 'D alone has a red bottom V. It is not the required transformed source red V; its quarter-turn similarity cannot repair the half-turn mismatch.',
            'semantic_suitability_pass':False})
    controls_path=BASE/'background_16/Solid197/control_original/tests/quicktest3_20261101T163310_8019543c7d1e'
    controls_binding=read(controls_path/'binding.json')
    control_raws=[read(controls_path/f'run_{i:02d}_response.json') for i in (1,2)]
    control_records=[read(controls_path/f'run_{i:02d}.json') for i in (1,2)]
    controls={'Plane342':{'original_control_calls':0,'found_control_invocations':[],'effect_vs_original_established':False},
       'Solid197_context_disclosure':{'scope':'Separate question; disclosed because specifically required by the assignment, not evidence about Plane342 geometry.',
           'binding_path':str(controls_path/'binding.json'),'binding_sha256':sha(controls_path/'binding.json'),
           'original_control_png_byte_equal_formal':Path(controls_binding['image_path']).read_bytes()==(ROOT/'SolidGeometry/image/Solid197.png').read_bytes(),
           'manual_full_raw_finals':['450 cm^2','450 cm^2'],
           'full_raw_contents':[r['choices'][0]['message']['content'] for r in control_raws],
           'raw_response_hashes':[sha(controls_path/f'run_{i:02d}_response.json') for i in (1,2)],
           'raw_hashes_match_completed_records':all(sha(controls_path/f'run_{i:02d}_response.json')==control_records[i-1]['response_sha256'] and control_records[i-1]['status']=='completed' for i in (1,2)),
           'finding':'The original control also produced 450/450. No incremental annotation effect is established for Solid197.'},
       'hard_gate_policy':'Correct original controls, identical narratives, new human studies, statistical gain, causal proof and per-marker ablation are not additional hard gates. No new solver calls were made.'}
    protocols=['AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json']
    runs=[]
    for r in evidence['runs']:
        i=r['run']
        runs.append({**r,'complete_raw_content_manually_read_by_independent_reviewer':True,
            'manual_final_literal':'Final Answer: **D:D**' if i==1 else 'Therefore, the correct picture is **D**.',
            'manual_final_option':'D','matches_immutable_pre_call_preset':True,'contradictory_option_or_numeric_final':False,
            'narrative_disposition':'Misidentifies the left-side wedge as a top-left corner triangle, treats first flip as a planar half-turn and second as a quarter-turn, then misdescribes D as bottom-left. Final D:D is nevertheless an explicit single letter selection.' if i==1 else 'Treats interior red wedge diagonals as a top/bottom card border, assigns incorrect wedge locations and directions, and selects D. The actual square-card borders stay black. These are observable narrative errors, not facts about the geometry.',
            'causal_limit':'The two narratives differ. Their erroneous descriptions neither prove the intended feature-binding mechanism nor require discarding the explicit D final.'})
    report={'question_id':'Plane342','variant_id':'quarterturn_wedge_edge_binding','decision':'reject',
       'review_type':'NEW independent second review','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
       'summary':'The original has the unique answer B and the frozen evidence genuinely records two explicit D finals against the pre-call D preset. The two legal, readable red V edge styles are reproducible and well targeted, but the candidate fails unique human interpretation: a reasonable literal printed-card reading gives no matching choice because the required red right-side V is absent.',
       'independence':{'brief_read_first_in_full':str(BASE/'Plane342_firstpass_independent_review_brief.txt'),
           'protocols_read_in_full':{p:sha(ROOT/p) for p in protocols},
           'method':'Read actual formal question without its answer, inspect actual source JPG/formal PNG/frozen candidate at native size, derive the two-flip result, then compare frozen vectors, primary claims and raw evidence.',
           'no_nested_agents_delegates_threads_worktrees':True,'new_solver_calls':0,
           'read_stored_answer_or_primary_proof_used_as_mathematical_premise':False},
       'independent_unique_answer_proof':math,
       'actual_image_inspection':{'actual_paths_viewed':[str(ROOT/'PlaneGeometry/originals/Plane342.jpg'),str(ROOT/'PlaneGeometry/image/Plane342.png'),str(CAND/'candidate.png'),str(OWN/'native_candidate.png'),str(OWN/'source_detail.png'),str(OWN/'D_detail.png')],
           'source_formal_and_candidate_preserve_same_structural_pattern':True,
           'native_size':'Inspected the complete 768x768 formal and candidate PNGs at original resolution; the source card is about 67 px wide and each option about 84 px. Both V marks, all A-E labels, black wedge positions, full diagonals and flip arrows remain discernible.',
           'details_scope':'Enlarged crops were supplementary only; legibility judgment used the full native-size candidate.',
           'perceptual_clarity_pass':True,'unique_problem_interpretation_pass':False},
       'per_marker':markers,
       'preservation':{'native_render_audit':rendered,
           'frozen_source_question_and_original_approval_unchanged':not relevant_changes and current['approval_matches'],
           'fill_text_geometry_preserved':'Original filled artist paths, facecolors and transforms and all text artists compare identically before/after partial styling. A 958-pixel RGB change is confined to the two selected stroke neighborhoods; this does not mean every visible black edge pixel is unchanged.',
           'original_full_diagonal_preserved':True,'original_blank_reverse_and_arrows_preserved':True,
           'new_closed_partitions_or_auxiliary_lines':False,
           'three_dimensional_geometry_projection_visibility':'Not applicable to this planar card drawing. Frozen 2D view/transform and all existing solid/dashed visibility strokes are preserved; no 3D scene or visibility override exists.',
           'warning_against_invalid_inference':'Schema legality and frozen fill/path preservation do not establish preserved puzzle semantics.'},
       'human_semantics':{'disposition':'fails',
           'annotation_reading':'If red is understood as an external comparison highlight and ignored as card content, the unchanged black-white pattern still has exactly B.',
           'reasonable_printed_card_reading':'The literal question is about a diagram printed on the card. Red strokes lie precisely on that diagram inside the card, at normal print-like width, without a visible legend, callout or question qualification identifying them as exempt comparison annotations. A reader can reasonably include that red ink in the transformed pattern.',
           'consequence':'Two perpendicular flips transform the red source BL-center-TL path into TR-center-BR. No choice contains a red right V: B has the correct black-white half-turn but remains entirely black; D has a red bottom V and the wrong full diagonal. Consequently no choice matches the full colored print.',
           'not_an_automatic_color_as_given_rule':'The mere presence of an authorized color annotation is not the objection. The problem explicitly asks to transform a printed picture, these marks occupy the transformed printed feature itself, and a direct color-aware check eliminates every available option. This concrete competing interpretation defeats the required unique reading.',
           'not_a_new_region_objection':'The marks form open V paths on existing boundaries. They do not introduce the closed extra partitions implicated in Plane233.',
           'primary_claim_disposition':'The primary statement that these are annotations and color is not promoted to a printed condition asserts an intended interpretation which is not communicated to the human reader or solver. Its black-white proof is correct but does not resolve this candidate-specific semantic conflict.',
           'solver_narrative_role':'Run 2 actually describes red as card content but mislocates it. That error is disclosed as an observation; the independent source-to-result red-path calculation above is the basis of the objection.'},
       'two_hit_evidence':{'raw_preset_hits_verified':True,'effective_valid_variant_two_hit_requirement_satisfied':False,
           'reason':'Two literal D finals meet the frozen answer-hit observation; the candidate fails the independent human-semantics requirement, so these cannot justify recommending a valid delivered variant.',
           'binding':evidence['binding'],'binding_checks':evidence['checks'],'question_text_sha256':evidence['question_text_sha256'],
           'profile':profile,'no_leak_request':evidence['no_leak_request'],'full_raw_final_reviews':runs,
           'saved_invocation_search':evidence['invocation_search'],
           'retry_selection_fishing_audit':'Exactly one stored Plane342 invocation, two starts, two completed HTTP 200 results and two complete stop-finished raw responses on the same image/design/request; no incomplete or additional Plane342 binding was found under this task runtime. Read the byte-identical shared and isolated harness and caller: one two-iteration loop, no retry branch, break on error, and no answer-dependent selection. Both complete runs are retained.',
           'provenance_limits':'The pre-call creation/start timestamps and hash bindings are internally consistent preserved records, not externally signed or provider-attested evidence. This audit cannot certify the absence of unrecorded external calls. No such retry/selection evidence was found.'},
       'controls_and_effect_limits':controls,
       'current_authoritative_eligibility':current,
       'exact_frozen_hashes':{'candidate_png':evidence['image'],'design_json_sha256':sha(CAND/'design.json'),
           'plugin_json_sha256':sha(CAND/'plugin.json'),'plugin_submitted_json_sha256':sha(CAND/'plugin_submitted.json'),
           'formal_source_jpg_sha256':sha(ROOT/'PlaneGeometry/originals/Plane342.jpg'),
           'formal_png_sha256':sha(ROOT/'PlaneGeometry/image/Plane342.png'),
           'formal_scene_sha256':sha(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane342.json'),
           'relevant_frozen_inputs':evidence['frozen_relevant_inputs'],'all_read_candidate_evidence_files':evidence['all_evidence_initial_hashes']},
       'concrete_objections':[{'severity':'blocking','code':'printed_card_color_semantics','finding':'The candidate admits a reasonable color-preserving printed-card reading with no matching option, whereas the intended annotation-only reading gives B. The current frozen image therefore does not meet the required unique human interpretation.'}],
       'limits':['This is a single independent human review, not a new human study or a population readability estimate.',
           'The two raw finals do not establish a causal route, statistical improvement, or an incremental effect relative to an original Plane342 control; no original Plane342 control exists.',
           'Identical narratives, correct controls, statistical gain, causal proof and per-marker ablation were not imposed as hard gates.',
           'Decision is reject for this exact frozen candidate, not a formal-original rejection and not a user No Pass/Pass/Collect action.',
           'Any future repair would be a different candidate needing its own frozen evidence; no frozen design or evidence was repaired here.'],
       'workspace_and_process_preservation':{'strict_own_directory_guard_installed_before_project_imports':True,'shared_runtime_isolation':ISOLATION,
           'TEMP_TMP_TMPDIR_caches_inside_assigned_review_root':True,'network_and_subprocess_blocked_by_audit_hook':True,
           'prior_evidence_hash_changes_during_review':changes,'relevant_source_hash_changes_during_review':relevant_changes,
           'unrelated_concurrent_workbench_edits_preserved':True,'entire_workspace_unchanged_claim':False,
           'historical_aggregate_drift':evidence['historical_aggregate_state_differences'],
           'mutable_progress_snapshot_policy':'Existing remaining_questions/exploration_report and historical progress snapshots were not modified or restored. Drift is diagnostic metadata, not proof of frozen geometry corruption.',
           'formal_approval_Pass_Collect_publication_APIs_called':False,'env_git_dotruntime_changes':False,
           'own_processes':'All Python commands are foreground and terminate normally; every captured Matplotlib scene is closed, plt.close(all) completed, no server/background helper was started.'},
       'supporting_new_review_files':{'evidence_audit_json':{'path':str(OWN/'evidence_audit.json'),'sha256':sha(OWN/'evidence_audit.json')},
           'native_render_audit_json':{'path':str(OWN/'native_render_audit.json'),'sha256':sha(OWN/'native_render_audit.json')}}}
    write('independent_review.json',report)
    print(json.dumps({'decision':report['decision'],'report':str(OWN/'independent_review.json'),'report_sha256':sha(OWN/'independent_review.json'),
       'original_unique_answer':math['unique_original_answer'],'raw_finals':['D','D'],'all_binding_checks':True,'all_native_render_checks':True,
       'current_eligible':current['eligible'],'preserved_prior_evidence':not changes,'preserved_sources':not relevant_changes},ensure_ascii=False))

if __name__=='__main__':
    {'inspect':inspect,'audit':audit,'render':render,'finalize':finalize}[sys.argv[1] if len(sys.argv)>1 else 'inspect']()
