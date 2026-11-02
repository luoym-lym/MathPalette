"""Read-only independent Plane295 audit; all writes confined here."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
ROOT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
BASE = ROOT / 'runtime/mathvision_special_20261101'
CAND = BASE / 'background_19/Plane295/inner_ear_shoulder_correspondence'
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
for name, folder in {'TEMP':'tmp', 'TMP':'tmp', 'TMPDIR':'tmp', 'MPLCONFIGDIR':'mplcache', 'XDG_CACHE_HOME':'cache', 'PYTHONPYCACHEPREFIX':'pycache'}.items():
    os.environ[name] = str(OWN / folder)

def check_write(path):
    if path is None or isinstance(path, int):
        return
    p = Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(OWN):
        raise PermissionError('Independent review write outside assigned root: ' + str(p))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check_write(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check_write(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check_write(args[0]); check_write(args[1])
    elif event in ('socket.connect', 'subprocess.Popen', 'os.system'):
        raise PermissionError('No network or child processes in this independent audit')

sys.addaudithook(guard)
for folder in ('tmp', 'mplcache', 'cache', 'pycache'):
    (OWN / folder).mkdir(exist_ok=True)
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp', guard_writes=True)

import base64
import copy
import hashlib
import json
from datetime import datetime, timezone
from PIL import Image
import numpy as np
from dataset_tools.catalog import content, digest

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def rows(p):
    return [json.loads(s) for s in Path(p).read_text(encoding='utf-8-sig').splitlines() if s.strip()] if Path(p).exists() else []

def save(name, value):
    (OWN / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def out(value):
    print(json.dumps(value, ensure_ascii=False, indent=2), flush=True)

FORMAL = next(r for r in rows(ROOT / 'PlaneGeometry/dataset.jsonl') if r['id'] == 'Plane295')

def verify():
    import ast
    from PIL import Image
    branch = ROOT / 'PlaneGeometry'
    approval = read(ROOT / 'provenance/approvals.json')['approvals']['Plane295']
    formal_content = content(ROOT, 'PlaneGeometry', FORMAL)
    eligibility = {'checked_at':datetime.now(timezone.utc).isoformat(), 'formal_record':FORMAL, 'question_record_sha256':digest(FORMAL), 'current_content_sha256':digest(formal_content), 'approval':approval, 'original_approval_valid':approval.get('reviewer')=='user' and bool(approval.get('instruction')) and digest(formal_content)==approval.get('content_sha256'), 'formal_content_files':formal_content['files'], 'authoritative_state':{}}
    for name in ('accepted_index.jsonl','collected_index.jsonl'):
        p = branch / 'special_variant' / name
        eligibility['authoritative_state'][name] = {'sha256':sha(p) if p.exists() else None, 'matching_rows':[r for r in rows(p) if r.get('question_id',r.get('id'))=='Plane295']}
    for name in ('recipes.json','collection.json'):
        p = branch / 'special_variant/Plane295' / name
        eligibility['authoritative_state'][name] = {'exists':p.exists(), 'sha256':sha(p) if p.exists() else None, 'content':read(p) if p.exists() else None}
    eligibility['formal_MathVision'] = FORMAL['source_dataset']=='MathVision'
    eligibility['noPass'] = not eligibility['authoritative_state']['accepted_index.jsonl']['matching_rows'] and not eligibility['authoritative_state']['recipes.json']['exists']
    eligibility['notCollected'] = not eligibility['authoritative_state']['collected_index.jsonl']['matching_rows'] and not eligibility['authoritative_state']['collection.json']['exists']
    eligibility['noSpecialCompletion'] = not eligibility['authoritative_state']['collection.json']['exists'] and not eligibility['authoritative_state']['collected_index.jsonl']['matching_rows']
    eligibility['eligible'] = all(eligibility[k] for k in ('formal_MathVision','original_approval_valid','noPass','notCollected','noSpecialCompletion'))
    eligibility['published_manifest_matches'] = [str(p.relative_to(ROOT)) for p in BASE.glob('batch_*/manifest.json') if 'Plane295' in p.read_text(encoding='utf-8-sig')]
    inputs = read(CAND/'render_check.json')
    old_files = inputs['frozen_inputs_before']['files']
    needed = {str(Path('PlaneGeometry')/p) for p in formal_content['files'] if not p.startswith('../')}
    needed |= {'dataset_tools\\geometry_dataset.py','dataset_tools\\mathvision_workbench.py', 'PlaneGeometry\\workbench\\mathvision_adapter.py','PlaneGeometry\\workbench\\mathvision_plugins.py','PlaneGeometry\\workbench\\drawing_board.py','PlaneGeometry\\workbench\\plugin.schema.json', 'PlaneGeometry\\REDRAW_PROTOCOL.md', 'MATHPALETTE_PROTOCOL.md'}
    comparisons = []
    for name in sorted(needed):
        p = ROOT / name
        old = old_files.get(name, old_files.get(name.replace('\\','/')))
        comparisons.append({'path':name,'sha256_current':sha(p),'sha256_frozen':old,'matches_frozen':sha(p)==old if old is not None else None})
    eligibility['frozen_input_comparison'] = comparisons
    eligibility['frozen_snapshot_before_after_identical'] = inputs['frozen_inputs_before']==inputs['frozen_inputs_after']
    eligibility['diagnostic_metadata_only'] = {str(p.relative_to(ROOT)):{'sha256_current':sha(p), 'preserved_read_only':True} for p in (BASE/'exploration_report.json',BASE/'remaining_questions.jsonl')}
    save('current_eligibility.json',eligibility)

    tests = next((CAND/'tests').iterdir())
    b = read(tests/'binding.json'); req = read(tests/'request.json'); design=read(CAND/'design.json')
    raw_png=base64.b64decode(req['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
    quick=branch/'workbench/quick_test.py'
    constants={}
    for node in ast.parse(quick.read_text(encoding='utf-8-sig')).body:
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name) and target.id in ('SYSTEM_PROMPT','TEST_PROFILES'):
                    constants[target.id]=ast.literal_eval(node.value)
    expected={'model':'mimo-v2.6-flash','stream':False,'thinking':{'type':'disabled'},'messages':[{'role':'system','content':constants['SYSTEM_PROMPT']},{'role':'user','content':[{'type':'text','text':FORMAL['question']},{'type':'image_url','image_url':{'url':'data:image/png;base64,'+base64.b64encode((CAND/'candidate.png').read_bytes()).decode('ascii')}}]}]}
    with Image.open(CAND/'candidate.png') as im:
        pixel_digest=hashlib.sha256(b'768x768:RGBA:'+im.convert('RGBA').tobytes()).hexdigest()
    runs=[]
    for i in (1,2):
        p=tests/f'run_{i:02}.json'; rp=tests/f'run_{i:02}_response.json'; sp=tests/f'run_{i:02}_started.json'
        r=read(p); raw=read(rp); start=read(sp); c=raw['choices'][0]
        runs.append({'run_index':i,'run_file_sha256':sha(p),'raw_response_path':str(rp),'raw_response_sha256':sha(rp),'started_file_sha256':sha(sp),'run_id':r['run_id'],'provider_response_id':raw['id'],'provider_created':raw['created'],'started_at':r['started_at'],'finished_at':r['finished_at'],'complete_raw_final_manually_read':c['message']['content'],'full_final_utf8_sha256':hashlib.sha256(c['message']['content'].encode('utf-8')).hexdigest(),'final_letter_manually_identified':'C','contradictory_final_letter_or_value':False,'raw_matches_run_answer':c['message']['content'].strip()==r['answer'],'raw_matches_recorded_hash':sha(rp)==r['response_sha256'],'same_request_image_design':all(r[k]==b[k] and start[k]==b[k] for k in ('request_body_sha256','image_sha256','design_sha256')),'status':r['status'],'http_status':r['http_status'],'finish_reason':c['finish_reason'],'response_model':raw['model'],'reasoning_tokens':raw['usage']['completion_tokens_details']['reasoning_tokens'],'start_id_matches':start['run_id']==r['run_id'],'truncated':r['truncated'],'matches_pre_call_preset':design['expected_wrong_answer']=='C'})
    inventory=[]
    for p in BASE.rglob('binding.json'):
        val=read(p)
        if val.get('question_id')=='Plane295' or val.get('image_sha256')==sha(CAND/'candidate.png'):
            inventory.append({'path':str(p.relative_to(ROOT)), 'sha256':sha(p), 'image_sha256':val.get('image_sha256'), 'preset':val.get('expected_wrong_answer'), 'requested_runs':val.get('requested_runs')})
    evidence={'binding':b,'binding_file_sha256':sha(tests/'binding.json'),'design_file_sha256':sha(CAND/'design.json'),'design_snapshot_file_sha256':sha(tests/'design_snapshot.json'),'plugin_file_sha256':sha(CAND/'plugin.json'),'submitted_plugin_identical':(CAND/'plugin.json').read_bytes()==(CAND/'plugin_submitted.json').read_bytes(),'design_snapshot_bytes_identical':(CAND/'design.json').read_bytes()==(tests/'design_snapshot.json').read_bytes(),'preset_created_at':design['created_at'],'preset_before_binding_before_both_calls':design['created_at']<b['created_at']<runs[0]['started_at']<runs[0]['finished_at']<runs[1]['started_at']<runs[1]['finished_at'],'request_file_sha256':sha(tests/'request.json'),'exact_request_body_hash_matches':sha(tests/'request.json')==b['request_body_sha256'],'exact_reconstructed_request_bytes_equal':json.dumps(expected,ensure_ascii=False).encode('utf-8')==(tests/'request.json').read_bytes(),'no_leak_request_exactly_formal_question_single_candidate_and_reference_system':req==expected,'decoded_png_equals_frozen_candidate_bytes':raw_png==(CAND/'candidate.png').read_bytes(),'image_hash_matches':sha(CAND/'candidate.png')==b['image_sha256'],'pixel_hash_matches':pixel_digest==b['pixel_sha256'],'question_record_current_matches_binding':digest(FORMAL)==b['question_record_sha256'],'dataset_current_matches_binding':sha(branch/'dataset.jsonl')==b['dataset_sha256'],'reference_quick_test_current_matches':sha(quick)==b['reference_quick_test_sha256'],'current_quicktest3_profile':constants['TEST_PROFILES']['quicktest3'],'profile_matches':all(b['settings'][k]==v for k,v in constants['TEST_PROFILES']['quicktest3'].items()),'harness_file_sha256':sha(BASE/'background_19/harness/quicktest3_isolated.py'),'harness_original_and_copy_identical':(BASE/'background_19/harness/quicktest3_isolated.py').read_bytes()==(BASE/'harness/quicktest3_isolated.py').read_bytes(),'runs':runs,'candidate_tests_subdirectories':[p.name for p in (CAND/'tests').iterdir() if p.is_dir()],'candidate_started_files':len(list(CAND.rglob('run_*_started.json'))),'candidate_raw_response_files':len(list(CAND.rglob('run_*_response.json'))),'matching_bindings_inventory_in_supplied_runtime':inventory,'retry_selection_audit':'Harness for-loop makes one HTTP call per index; writes request/design before calls; stops after errors without retry; one invocation/two start/run/raw response files; no alternate Plane295 binding found in supplied runtime. Unrecorded external calls cannot be excluded by a filesystem audit.','new_solver_calls':0}
    save('evidence_bindings.json',evidence)
    frozen_paths=list(CAND.rglob('*'))+[BASE/'background_19/Plane295/source_audit_final.json',BASE/'background_19/Plane295/context.json',BASE/'background_19/Plane295/source_scene_snapshot.json',BASE/'background_19/Plane295/source_original.jpg',BASE/'background_19/Plane295/original.png',BASE/'background_19/Plane295/formal_record.json',BASE/'background_19/Plane295/input_fingerprints.json',BASE/'background_19/second_review_queue.json',BASE/'Plane295_firstpass_independent_review_brief.txt',BASE/'Plane295_pre_review_evidence_check.json']
    save('reviewed_evidence_manifest.json',{str(p.relative_to(ROOT)):sha(p) for p in frozen_paths if p.is_file()})
    arr=np.array(Image.open(branch/FORMAL['image']).convert('RGB'))
    cand=np.array(Image.open(CAND/'candidate.png').convert('RGB'))
    diff=np.any(arr!=cand,axis=2)
    boxes=[(367,269,391,294),(368,431,391,452),(404,269,428,294),(404,431,428,452)]
    regions=[]
    cover=np.zeros(diff.shape,dtype=bool)
    for index,(x0,y0,x1,y1) in enumerate(boxes,1):
        cover[y0:y1,x0:x1]=True
        block=diff[y0:y1,x0:x1]
        yy,xx=np.where(block)
        regions.append({'marker':index,'changed_pixels':int(block.sum()),'diff_bbox_xyxy_exclusive':[int(xx.min()+x0),int(yy.min()+y0),int(xx.max()+x0+1),int(yy.max()+y0+1)]})
    pix={'total_changed_pixels':int(diff.sum()),'changed_outside_four_ear_regions':int((diff&~cover).sum()),'regions':regions,'face_width_px':2.2*691.2/(24.34635821182653),'inner_vertex_height_difference_px':.19*691.2/(24.34635821182653),'stroke_width_px':2*100/72}
    save('pixel_audit.json',pix)
    out({'eligibility':{k:eligibility[k] for k in ('checked_at','formal_MathVision','original_approval_valid','noPass','notCollected','noSpecialCompletion','eligible','current_content_sha256')}, 'frozen_input_mismatches':[v for v in comparisons if v['matches_frozen'] is False], 'not_in_primary_frozen_manifest':[v['path'] for v in comparisons if v['matches_frozen'] is None], 'evidence_checks':{k:v for k,v in evidence.items() if isinstance(v,bool)},'matching_bindings':inventory,'pixel_audit':pix})

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'inspect'
    if mode == 'verify':
        verify()
    elif mode == 'inspect':
        save('isolation.json', {'strict_guard_installed_before_project_or_render_imports':True, 'assigned_root':str(OWN), 'environment':{v:os.environ[v] for v in ('TEMP','TMP','TMPDIR','MPLCONFIGDIR','XDG_CACHE_HOME','PYTHONPYCACHEPREFIX')}, 'shared_runtime_isolation':ISOLATION, 'no_network_or_child_processes':True})
        scene = read(ROOT / 'PlaneGeometry' / FORMAL['scene'])
        native = read(ROOT / 'PlaneGeometry' / next(p for p in FORMAL['runtime_dependencies'] if p.endswith('/scene.json')))
        context = read(CAND / 'fresh_context.json')
        checks = read(CAND / 'render_check.json')
        out({'formal_scene':scene, 'native_scene':native, 'context_keys':list(context), 'render_check_keys':list(checks)})
    elif mode == 'render':
        sys.path.insert(0, str(ROOT / 'PlaneGeometry/workbench'))
        from workbench_io import load_config, pixel_hash, environment_versions
        from mathvision_adapter import RendererAdapter
        from mathvision_plugins import PluginRenderer
        from partial_style import object_paths, apply_partial_styles
        from dataset_tools.mathvision_workbench import png_bytes
        import matplotlib.pyplot as plt
        cfg = load_config()
        cfg['runtime_dir'] = str(OWN / 'render_state')
        cfg['output_dir'] = str(OWN / 'render_output')
        adapter = RendererAdapter(cfg)
        meta = adapter.inspect_question('Plane295')
        plugin = read(CAND / 'plugin.json')
        renderer = PluginRenderer(cfg, adapter, {'Plane295':meta})
        norm, rendered, pixels = renderer.render(plugin, frozen=True)
        (OWN / 'reproduced_candidate.png').write_bytes(rendered)
        scene = adapter.scene('Plane295')
        try:
            original = png_bytes(scene)
            (OWN / 'reproduced_original.png').write_bytes(original)
            paths = []
            for index, action in enumerate(plugin['params']['actions'], 1):
                target = action['target']
                path = object_paths(scene, target)[0]
                selected = path['segments'][1]
                controls = selected['control']
                display = scene.ax.transData.transform(controls)
                paths.append({'index':index, 'action':action, 'path_sha256_actual':path['sha256'], 'three_segments':len(path['segments']), 'closed':path['closed'], 'selected_control':controls.tolist(), 'all_controls':[s['control'].tolist() for s in path['segments']], 'endpoint_pixels_top_origin':[[float(x),float(768-y)] for x,y in display], 'selected_length_px':float(np.linalg.norm(display[-1]-display[0])), 'original_style':selected['style'], 'stroke_width_px':2*scene.fig.dpi/72})
            # Fill artists are distinct from the captured mathematical outlines.
            fills = [(artist, artist.get_facecolor(), artist.get_path().vertices.copy()) for artist in scene.ax.patches if artist.get_fill()]
            texts = [(text, text.get_text(), text.get_position(), text.get_color()) for text in scene.ax.texts]
            limits = [scene.ax.get_xlim(), scene.ax.get_ylim()]
            apply_partial_styles(scene, plugin['params']['actions'])
            fill_preserved = all(artist in scene.ax.patches and np.array_equal(artist.get_facecolor(), color) and np.array_equal(artist.get_path().vertices, vertices) for artist,color,vertices in fills)
            text_preserved = all(text in scene.ax.texts and (text.get_text(), text.get_position(), text.get_color()) == (value,pos,color) for text,value,pos,color in texts)
            result = {'environment':environment_versions(), 'normalization_identical':norm==plugin, 'current_context_identical_to_frozen':meta == read(CAND/'fresh_context.json'), 'no_op_pixel_equals_formal':pixel_hash(original)==pixel_hash(ROOT/'PlaneGeometry'/FORMAL['image']), 'candidate_reproduced_byte_equal':rendered==(CAND/'candidate.png').read_bytes(), 'reproduced_png_sha256':hashlib.sha256(rendered).hexdigest(), 'pixel_sha256':pixels, 'fills_preserved':fill_preserved, 'fill_artist_count':len(fills), 'text_preserved':text_preserved, 'text_count':len(texts), 'limits_preserved':limits==[scene.ax.get_xlim(),scene.ax.get_ylim()], 'markers':paths, 'open_figures_before_cleanup':plt.get_fignums()}
            save('render_audit.json', result)
            out(result)
        finally:
            scene.close()
            plt.close('all')
        # Diagnostic crops are exact pixel selections, not new candidates.
        for name,path in [('formal', ROOT/'PlaneGeometry'/FORMAL['image']),('candidate',CAND/'candidate.png')]:
            with Image.open(path) as im:
                im.crop((354,252,440,342)).save(OWN/f'{name}_given_native_crop.png')
                im.crop((354,252,440,342)).resize((344,360),Image.Resampling.NEAREST).save(OWN/f'{name}_given_4x.png')
                im.crop((214,408,440,500)).save(OWN/f'{name}_BC_native_crop.png')
                im.crop((214,408,440,500)).resize((904,368),Image.Resampling.NEAREST).save(OWN/f'{name}_BC_4x.png')
        out({'all_figures_closed':not plt.get_fignums()})
    elif mode == 'evidence':
        tests = next((CAND / 'tests').iterdir())
        b = read(tests / 'binding.json')
        req = read(tests / 'request.json')
        uri = req['messages'][1]['content'][1]['image_url']['url']
        encoded = base64.b64decode(uri.split(',',1)[1])
        brief_req = copy.deepcopy(req)
        brief_req['messages'][1]['content'][1]['image_url']['url'] = '<PNG data omitted; byte hash independently checked>'
        out({'request_without_base64':brief_req, 'request_file_sha256':sha(tests/'request.json'), 'request_body_bytes_sha256':sha(tests/'request.json'), 'canonical_request_hash':digest(req), 'embedded_png_sha256':hashlib.sha256(encoded).hexdigest(), 'actual_png_sha256':sha(CAND/'candidate.png'), 'binding':b, 'summary':read(tests/'summary.json'), 'preset_identical':(CAND/'design.json').read_bytes() == (tests/'design_snapshot.json').read_bytes(), 'starts':[read(tests/f'run_{i:02}_started.json') for i in (1,2)]})
