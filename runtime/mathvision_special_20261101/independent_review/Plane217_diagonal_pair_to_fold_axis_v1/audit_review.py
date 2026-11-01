"""Independent, offline review of exactly Plane217 and Plane234. Run Python -B."""
from pathlib import Path
import ast
import base64
from datetime import datetime, timezone
import hashlib
import json
import math
import os
import sys

sys.dont_write_bytecode = True
PROJECT = next(p for p in Path(__file__).resolve().parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = PROJECT / 'runtime/mathvision_special_20261101'
OWN = [TASK / 'independent_review/Plane217_diagonal_pair_to_fold_axis_v1',
       TASK / 'independent_review/Plane234_three_feature_match_ignores_gray']
for p in OWN:
    p.mkdir(parents=True, exist_ok=True)
for key, name in [('MPLCONFIGDIR', 'mpl_cache'), ('TEMP', 'tmp'), ('TMP', 'tmp'), ('XDG_CACHE_HOME', 'cache')]:
    p = OWN[0] / name
    p.mkdir(exist_ok=True)
    os.environ[key] = str(p)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def strict_guard(event, args):
    def check(path):
        if path is None or isinstance(path, int):
            return
        path = Path(os.fsdecode(path)).resolve()
        if not any(path.is_relative_to(p.resolve()) for p in OWN):
            raise PermissionError('Independent reviewer write outside own folders: ' + str(path))
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check(args[0]); check(args[1])
    elif event in ('socket.connect', 'socket.connect_ex', 'socket.getaddrinfo'):
        raise PermissionError('Offline independent review: network calls forbidden')
sys.addaudithook(strict_guard)
sys.path[:0] = [str(TASK), str(PROJECT), str(PROJECT / 'PlaneGeometry/workbench')]
from runtime_isolation import install
ISOLATION = install(OWN[0] / 'render_tmp')
from PIL import Image, ImageDraw
import numpy as np
from dataset_tools import catalog
from dataset_tools.mathvision_workbench import build_scene, png_bytes
from partial_style import object_paths
from mathvision_plugins import PluginRenderer
from workbench_io import canonical_hash, pixel_hash, load_config, environment_versions

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rel(p):
    return Path(p).resolve().relative_to(PROJECT).as_posix()
def write(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
def rows(p):
    return [json.loads(x) for x in Path(p).read_text(encoding='utf-8-sig').splitlines() if x.strip()] if Path(p).exists() else []

RECORDS = {x['id']: x for x in rows(PROJECT / 'PlaneGeometry/dataset.jsonl') if x['id'] in ('Plane217', 'Plane234')}
CANDIDATES = [TASK / 'background_05/plane_a/Plane217/diagonal_pair_to_fold_axis_v1',
              TASK / 'background_05/plane_b/Plane234/three_feature_match_ignores_gray']
protected = set()
for c in CANDIDATES:
    protected.update(x for x in c.parent.rglob('*') if x.is_file())
    for p in read(c / 'render_check.json')['input_fingerprints']['files']:
        protected.add(PROJECT / p)
for p in ['MATHPALETTE_PROTOCOL.md', 'PlaneGeometry/REDRAW_PROTOCOL.md', 'PlaneGeometry/workbench/README.md',
          'PlaneGeometry/workbench/agent_prompt.md', 'PlaneGeometry/workbench/plugin.schema.json',
          'PlaneGeometry/workbench/quick_test.py', 'PlaneGeometry/workbench/config.json',
          'PlaneGeometry/special_variant/accepted_index.jsonl', 'PlaneGeometry/special_variant/collected_index.jsonl',
          'provenance/approvals.json', 'provenance/source_notes.json', 'question_bank.jsonl',
          'runtime/mathvision_special_20261101/remaining_questions.jsonl',
          'runtime/mathvision_special_20261101/exploration_report.json',
          'runtime/mathvision_special_20261101/harness/quicktest3_isolated.py',
          'runtime/mathvision_special_20261101/review_batch_05_brief.txt']:
    if (PROJECT / p).is_file():
        protected.add(PROJECT / p)
BEFORE = {rel(p): sha(p) for p in protected}
write(OWN[0] / 'protected_files_before.json', BEFORE)

# Read constants statically: never import/execute the API harness or load a key.
tree = ast.parse((PROJECT / 'PlaneGeometry/workbench/quick_test.py').read_text(encoding='utf-8'))
constants = {}
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ('SYSTEM_PROMPT', 'TEST_PROFILES', 'MIMO_API_BASE'):
                constants[target.id] = ast.literal_eval(node.value)
approvals = read(PROJECT / 'provenance/approvals.json')['approvals']
accepted = rows(PROJECT / 'PlaneGeometry/special_variant/accepted_index.jsonl')
collected = rows(PROJECT / 'PlaneGeometry/special_variant/collected_index.jsonl')

class Adapter:
    def is_native(self, qid):
        return qid in RECORDS
    def scene(self, qid):
        return build_scene(PROJECT / 'PlaneGeometry', RECORDS[qid])

def test_evidence(c, record, target):
    t, = (c / 'tests').iterdir()
    binding = read(t / 'binding.json')
    request = read(t / 'request.json')
    summary = read(t / 'summary.json')
    snapshot = read(t / 'design_snapshot.json')
    checks = {}
    checks['exact_request_keys'] = set(request) == {'model', 'stream', 'thinking', 'messages'}
    checks['request_hash'] = sha(t / 'request.json') == binding['request_body_sha256']
    checks['formal_record_hash'] = canonical_hash(record) == binding['question_record_sha256']
    checks['dataset_hash'] = sha(PROJECT / 'PlaneGeometry/dataset.jsonl') == binding['dataset_sha256']
    checks['quicktest_reference_hash'] = sha(PROJECT / 'PlaneGeometry/workbench/quick_test.py') == binding['reference_quick_test_sha256']
    checks['exact_profile'] = binding['profile'] == 'quicktest3' and binding['settings'] == {
        **constants['TEST_PROFILES']['quicktest3'], 'api_base': constants['MIMO_API_BASE']}
    checks['exact_model_thinking_nonstreaming'] = request['model'] == 'mimo-v2.6-flash' and request['thinking'] == {'type': 'disabled'} and request['stream'] is False
    expected_messages = [
        {'role': 'system', 'content': constants['SYSTEM_PROMPT']},
        {'role': 'user', 'content': [{'type': 'text', 'text': record['question']},
         {'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,' + base64.b64encode((c/'candidate.png').read_bytes()).decode('ascii')}}]}]
    checks['only_existing_system_and_exact_formal_question_and_candidate_png'] = request['messages'] == expected_messages
    checks['binding_prompt_question_identity'] = binding['system_prompt'] == constants['SYSTEM_PROMPT'] and binding['question'] == record['question']
    checks['candidate_byte_and_pixel_identity'] = sha(c / 'candidate.png') == binding['image_sha256'] and pixel_hash(c / 'candidate.png') == binding['pixel_sha256']
    checks['design_and_snapshot_byte_identity'] = (c/'design.json').read_bytes() == (t/'design_snapshot.json').read_bytes() and sha(c/'design.json') == binding['design_sha256']
    checks['image_and_design_paths_identity'] = Path(binding['image_path']).resolve() == (c/'candidate.png').resolve() and Path(binding['design_path']).resolve() == (c/'design.json').resolve()
    checks['predeclared_target'] = snapshot['expected_wrong_answer'] == binding['expected_wrong_answer'] == target
    checks['summary_frozen_binding_exact'] = all(summary[k] == v for k,v in binding.items())
    checks['summary_two_complete_runs'] = summary['two_completed'] is True and binding['requested_runs'] == 2 and len(summary['results']) == 2
    runs = []
    for i in (1,2):
        run = read(t / f'run_{i:02d}.json')
        started = read(t / f'run_{i:02d}_started.json')
        raw_path = t / f'run_{i:02d}_response.json'
        raw = read(raw_path)
        choice, = raw['choices']
        msg = choice['message']
        prefix = f'run_{i}_'
        checks[prefix+'response_raw_hash'] = sha(raw_path) == run['response_sha256']
        checks[prefix+'start_binding'] = all(run[k] == v for k,v in started.items()) and all(run[k] == binding[k] for k in ('request_body_sha256','image_sha256','design_sha256'))
        checks[prefix+'preset_before_start'] = datetime.fromisoformat(snapshot['created_at']) <= datetime.fromisoformat(binding['created_at']) < datetime.fromisoformat(started['started_at'])
        checks[prefix+'complete_no_truncation'] = run['status'] == 'completed' and run['http_status'] == 200 and run['truncated'] is False and choice['finish_reason'] == run['finish_reason'] == 'stop'
        checks[prefix+'actual_model_and_no_thinking'] = raw['model'] == run['response_model'] == 'mimo-v2.6-flash' and run['thinking'] == '' and raw['usage']['completion_tokens_details']['reasoning_tokens'] == 0
        checks[prefix+'complete_body_matches_record'] = msg['content'].strip() == run['answer'] and run['usage'] == raw['usage'] and not msg.get('tool_calls')
        checks[prefix+'summary_result_exact'] = summary['results'][i-1] == run
        checks[prefix+'timing_order'] = datetime.fromisoformat(run['started_at']) < datetime.fromisoformat(run['finished_at'])
        checks[prefix+'provider_creation_between_start_and_finish'] = datetime.fromisoformat(run['started_at']).timestamp()-2 <= raw['created'] <= datetime.fromisoformat(run['finished_at']).timestamp()+2
        runs.append({'run_index': i, 'run_id': run['run_id'], 'provider_response_id': raw['id'],
                     'started_at': run['started_at'], 'finished_at': run['finished_at'],
                     'response_sha256': sha(raw_path), 'raw_response_path': rel(raw_path),
                     'finish_reason': choice['finish_reason'], 'complete_raw_answer': msg['content'],
                     'provider_cached_prompt_tokens': raw['usage']['prompt_tokens_details']['cached_tokens']})
    checks['distinct_stateless_run_and_response_ids'] = runs[0]['run_id'] != runs[1]['run_id'] and runs[0]['provider_response_id'] != runs[1]['provider_response_id']
    checks['separate_sequential_calls'] = datetime.fromisoformat(runs[0]['finished_at']) <= datetime.fromisoformat(runs[1]['started_at'])
    return {'directory': rel(t), 'binding': binding, 'checks': checks, 'runs': runs,
            'all_checks_pass': all(checks.values())}

for index, (qid, c, target) in enumerate(zip(('Plane217','Plane234'), CANDIDATES, ('A','D'))):
    out = OWN[index]
    record = RECORDS[qid]
    audit = {'question_id': qid, 'reviewed_at_utc': datetime.now(timezone.utc).isoformat(),
             'review_scope': 'New independent second reviewer; offline; no new model calls, subagents, Pass, Collect or publication.',
             'isolation': ISOLATION, 'strict_own_folder_write_guard': True,
             'environment': environment_versions(), 'checks': {}}
    checks = audit['checks']
    catalog.validate_formal_row(PROJECT, 'PlaneGeometry', record)
    approval = approvals[qid]
    current_content_sha = catalog.digest(catalog.content(PROJECT, 'PlaneGeometry', record))
    checks['current_user_approval_content_fingerprint'] = current_content_sha == approval['content_sha256'] and approval['reviewer'] == 'user' and bool(approval['instruction'])
    audit['approval'] = {**approval, 'computed_current_content_sha256': current_content_sha}
    checks['formal_mathvision'] = record['source_dataset'] == 'MathVision'
    checks['not_in_accepted_index'] = not any(x.get('question_id',x.get('id')) == qid for x in accepted)
    checks['not_in_collected_index_including_special_completion'] = not any(x.get('question_id',x.get('id')) == qid for x in collected)
    checks['no_formal_special_directory_or_collection_or_recipe'] = not (PROJECT / 'PlaneGeometry/special_variant' / qid).exists()
    checks['root_catalog_record_exact'] = next(x for x in rows(PROJECT/'question_bank.jsonl') if x.get('id') == qid)['question'] == record['question']
    audit['current_formal_record'] = record
    input_report = read(c / 'render_check.json')
    inputs = input_report['input_fingerprints']
    file_checks = {p: sha(PROJECT/p) == h for p,h in inputs['files'].items()}
    audit['input_file_hashes'] = {p: {'recorded':h, 'current':sha(PROJECT/p), 'match':file_checks[p]} for p,h in inputs['files'].items()}
    checks['all_recorded_render_input_file_hashes_current'] = all(file_checks.values())
    checks['render_record_and_environment_match'] = inputs['question_record_sha256'] == canonical_hash(record) and inputs['environment'] == environment_versions()
    checks['render_report_candidate_plugin_design_pixel_hashes'] = (
        input_report['png_sha256'] == sha(c/'candidate.png') and input_report['pixel_sha256'] == pixel_hash(c/'candidate.png')
        and input_report['plugin_sha256'] == sha(c/'plugin.json') and input_report['design_sha256'] == sha(c/'design.json'))
    checks['existing_repeat_and_noop_reports'] = input_report['baseline_pixel_match'] is True and input_report['two_byte_identical_redraws'] is True
    checks['runtime_original_copy_exact_formal_png'] = (c.parent/'original.png').read_bytes() == (PROJECT/'PlaneGeometry'/record['image']).read_bytes()
    audit['eligibility_state_hashes_current'] = {}
    for p,h in read(c/'eligibility_immediately_before_calls.json')['state_hashes'].items():
        path = PROJECT / p
        audit['eligibility_state_hashes_current'][p] = {'recorded': h, 'current':sha(path) if path.is_file() else None, 'match': (sha(path) if path.is_file() else None) == h}
    checks['recorded_eligibility_snapshot_hashes_current'] = all(x['match'] for x in audit['eligibility_state_hashes_current'].values())
    audit['candidate_tests'] = test_evidence(c, record, target)
    checks['all_candidate_test_integrity_checks'] = audit['candidate_tests']['all_checks_pass']
    if qid == 'Plane217':
        # The optional control design deliberately retains preset A. C/C are
        # manually read correct control finals, not a control preset or gate.
        audit['control_tests'] = test_evidence(c.parent/'original_control', record, 'A')
        checks['all_control_test_integrity_checks'] = audit['control_tests']['all_checks_pass']
        checks['control_is_exact_current_formal_png'] = (c.parent/'original_control/candidate.png').read_bytes() == (PROJECT/'PlaneGeometry'/record['image']).read_bytes()
    else:
        audit['control_tests'] = None

    # Fresh native capture and exact production executor; guards precede imports.
    scene = build_scene(PROJECT/'PlaneGeometry', record)
    try:
        baseline = png_bytes(scene)
        checks['fresh_noop_matches_formal_pixels'] = pixel_hash(baseline) == pixel_hash(PROJECT/'PlaneGeometry'/record['image'])
        (out/'reproduced_original.png').write_bytes(baseline)
        scene.fig.canvas.draw()
        claimed_paths = read(c / 'path_fingerprints_complete.json')
        actual_paths = {oid:[{k:p[k] for k in ('id','sha256','closed')} for p in object_paths(scene, oid)] for oid in claimed_paths}
        audit['current_actual_vector_path_fingerprints'] = actual_paths
        checks['every_claimed_vector_path_fingerprint_matches_actual'] = actual_paths == claimed_paths
        context = read(c/'context.json')
        checks['context_original_pixel_identity'] = context['original_pixel_sha256'] == pixel_hash(baseline)
        fresh_objects = {x['id']:x for x in scene.objects}
        checks['context_objects_exact_fresh_capture'] = all(fresh_objects[x['id']] == x for x in context['objects']) and len(fresh_objects) == len(context['objects'])
        fresh_metadata = {'original_pixel_sha256':pixel_hash(baseline), 'objects':scene.objects, 'snap_points':scene.snap_points,
                          'canvas':{'xlim':scene.ax.get_xlim(), 'ylim':scene.ax.get_ylim()}}
        if qid == 'Plane234':
            ob = {x['id']:x for x in read(PROJECT/'PlaneGeometry'/record['scene'])['objects']}
            overlay_checks = []
            for a in read(c/'plugin.json')['params']['actions']:
                if a['type'] == 'add_line':
                    name, edge = a['id'].removeprefix('Pair_').split('_edge')
                    commands = ob[name]['commands']
                    verts = [commands[j]['point'] for j in range(3)]
                    exact = [verts[int(edge)],verts[int(edge)+1]]
                    overlay_checks.append({'action_id':a['id'], 'original_object':name,
                                           'original_exact_endpoints':exact, 'endpoints':a['endpoints'],
                                           'exact_endpoint_match':a['endpoints'] == exact,
                                           'same_actual_vector_side': any(np.allclose(s['control'],a['endpoints'],atol=1e-12,rtol=0) for p in object_paths(scene,name) for s in p['segments'] if len(s['control']) == 2)})
            audit['overlay_endpoint_audit'] = overlay_checks
            checks['all_eight_overlays_exactly_existing_sides'] = len(overlay_checks) == 8 and all(x['exact_endpoint_match'] and x['same_actual_vector_side'] for x in overlay_checks)
    finally:
        scene.close()
    config = load_config()
    config['runtime_dir'] = str(out/'state')
    config['output_dir'] = str(out/'output')
    executor = PluginRenderer(config, Adapter(), {qid:fresh_metadata})
    plugin = read(c/'plugin.json')
    normalized, data1, pixels1 = executor.render(plugin, frozen=True)
    normalized2, data2, pixels2 = executor.render(plugin, frozen=True)
    checks['actual_schema_and_whitelist_normalized_frozen_plugin'] = normalized == normalized2 == plugin
    checks['fresh_repeated_candidate_bytes_exact_tested_png'] = data1 == data2 == (c/'candidate.png').read_bytes()
    checks['fresh_repeated_candidate_pixels_exact_tested_png'] = pixels1 == pixels2 == pixel_hash(c/'candidate.png')
    (out/'reproduced_candidate.png').write_bytes(data1)
    audit['original_and_candidate_hashes'] = {
        'source_image_sha256':sha(PROJECT/'PlaneGeometry'/record['original_image']),
        'formal_png_sha256':sha(PROJECT/'PlaneGeometry'/record['image']),
        'formal_pixel_sha256':pixel_hash(PROJECT/'PlaneGeometry'/record['image']),
        'candidate_png_sha256':sha(c/'candidate.png'), 'candidate_pixel_sha256':pixels1,
        'plugin_sha256':sha(c/'plugin.json'), 'design_sha256':sha(c/'design.json')}
    if qid == 'Plane234':
        formal = Image.open(PROJECT/'PlaneGeometry'/record['image']).convert('RGB')
        candidate = Image.open(c/'candidate.png').convert('RGB')
        # Own analysis only. No candidate replacement, presentation or new test.
        for label, box in [('source',(350,285,461,393)),('option_D',(513,437,582,484))]:
            canvas = Image.new('RGB', ((box[2]-box[0])*12, (box[3]-box[1])*6+24),'white')
            for k,im in enumerate((formal,candidate)):
                crop = im.crop(box).resize(((box[2]-box[0])*6,(box[3]-box[1])*6),Image.Resampling.NEAREST)
                canvas.paste(crop,(k*crop.width,24))
            ImageDraw.Draw(canvas).text((4,4),'ORIGINAL (left) / TESTED CANDIDATE (right); 6x ANALYSIS ONLY',fill='black')
            canvas.save(out/f'analysis_{label}_comparison_6x.png')
        fill_audit = read(c/'semantic_fill_preservation_audit.json')
        fa=np.array(formal); ca=np.array(candidate)
        audit['independent_fill_pixel_recheck'] = []
        for ray in fill_audit['rays']:
            coords = ray['unchanged_fill_pixel_locations']
            passed = all(list(fa[y,x]) == list(ca[y,x]) == ray['unchanged_semantic_fill_rgb'] for x,y in coords)
            audit['independent_fill_pixel_recheck'].append({'object_id':ray['object_id'], 'reported_retained_count':ray['identical_fill_pixels_still_visible'], 'coordinates_count':len(coords), 'all_listed_pixels_verified':passed})
        checks['all_reported_retained_fill_pixels_exist_unchanged'] = all(x['all_listed_pixels_verified'] and x['coordinates_count'] == x['reported_retained_count'] for x in audit['independent_fill_pixel_recheck'])

    audit['historical_eligibility_metadata_note'] = (
        'Historical exploration_report.json and remaining_questions.jsonl hashes are recorded honestly above. '
        'They now describe these questions as explored_no_deliverable. These mutable runtime summaries '
        'are not the formal approval or Special eligibility authority; current formal, approval, '
        'accepted, collected, special-completion and candidate evidence were independently checked.')
    audit['all_checks_pass_including_historical_runtime_metadata'] = all(checks.values())
    audit['all_required_integrity_checks_pass'] = all(v for k,v in checks.items() if k != 'recorded_eligibility_snapshot_hashes_current')
    write(out/'integrity_audit.json',audit)
    print(qid, 'required_integrity',audit['all_required_integrity_checks_pass'], 'diagnostic_mismatches', [k for k,v in checks.items() if not v], flush=True)
    print(qid, 'test failures', [k for k,v in audit['candidate_tests']['checks'].items() if not v], flush=True)

AFTER = {p:sha(PROJECT/p) for p in BEFORE}
preserved = {'checked_existing_files':len(BEFORE), 'all_preserved':BEFORE == AFTER,
             'changed':[p for p in BEFORE if BEFORE[p] != AFTER[p]],
             'no_existing_files_deleted':all((PROJECT/p).is_file() for p in BEFORE)}
for out in OWN:
    write(out/'preservation_audit.json',preserved)
print('Preservation',json.dumps(preserved),flush=True)
