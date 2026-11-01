"""Independent read-only evidence and finite geometry audit. Run with Python -B.

No project modules, renderer, network client, or solver are imported/executed.
Only this review's two directories receive output.
"""
from pathlib import Path
import ast
import base64
from collections import Counter
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
import os
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
TASK = ROOT / 'runtime/mathvision_special_20261101'
OWN = TASK / 'independent_review'
CASES = [
    ('SolidGeometry', 'Solid142', 'solid_worker', 'orthogonal_cut_feature_swap', 'original_control', 'A'),
    ('PlaneGeometry', 'Plane233', 'plane_parts', 'two_U_partial_partition_binding', 'original_controls', 'B'),
]
assert sys.dont_write_bytecode
for key, name in [('MPLCONFIGDIR', 'mpl'), ('XDG_CACHE_HOME', 'cache'), ('TEMP', 'tmp'), ('TMP', 'tmp')]:
    dest = Path(__file__).parent / name
    dest.mkdir(exist_ok=True)
    os.environ[key] = str(dest)
from PIL import Image

def validate_schema(value, schema, root=None):
    """Evaluate every keyword used by the actual schema; fail on violation."""
    root = root or schema
    if '$ref' in schema:
        target = root
        for part in schema['$ref'].split('/')[1:]: target = target[part]
        return validate_schema(value, target, root)
    if 'oneOf' in schema:
        successes = 0
        for option in schema['oneOf']:
            try: validate_schema(value, option, root); successes += 1
            except AssertionError: pass
        assert successes == 1
    if 'const' in schema: assert value == schema['const']
    if 'enum' in schema: assert value in schema['enum']
    typ = schema.get('type')
    if typ == 'object':
        assert isinstance(value, dict)
        assert set(schema.get('required', [])) <= value.keys()
        if schema.get('additionalProperties') is False: assert value.keys() <= schema['properties'].keys()
        for k,v in value.items():
            if k in schema.get('properties', {}): validate_schema(v, schema['properties'][k], root)
    elif typ == 'array':
        assert isinstance(value, list)
        assert len(value) >= schema.get('minItems', 0) and len(value) <= schema.get('maxItems', float('inf'))
        for item in value:
            if 'items' in schema: validate_schema(item, schema['items'], root)
    elif typ == 'string':
        assert isinstance(value, str)
        assert len(value) <= schema.get('maxLength', float('inf'))
        if 'pattern' in schema: assert re.search(schema['pattern'], value)
    elif typ == 'number':
        assert type(value) in [int,float] and math.isfinite(value)
        assert schema.get('minimum', -float('inf')) <= value <= schema.get('maximum', float('inf'))
    elif typ == 'boolean': assert type(value) is bool
    elif typ is not None: raise AssertionError('Unhandled schema type '+typ)

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def sha(b):
    return hashlib.sha256(b).hexdigest()

def fh(p):
    p = Path(p)
    return sha(p.read_bytes()) if p.is_file() else None

def canon(d):
    return sha(json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())

def rows(p):
    return [json.loads(l) for l in Path(p).read_text(encoding='utf-8-sig').splitlines() if l.strip()]

def pix(p):
    with Image.open(p) as im:
        rgba = im.convert('RGBA')
        assert rgba.size == (768, 768) and rgba.getextrema()[3] == (255, 255)
        return sha(b'768x768:RGBA:' + rgba.tobytes())

def write(p, d):
    p = Path(p).resolve()
    assert p.is_relative_to(OWN.resolve())
    p.parent.mkdir(exist_ok=True, parents=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')

def rel(p):
    return Path(p).resolve().relative_to(ROOT).as_posix()

def formal_content(branch, record):
    paths = [record[k] for k in ['image', 'original_image', 'script', 'scene'] if record.get(k)]
    paths += record.get('runtime_dependencies', [])
    paths += ['dataset_generator/common_renderer.py', 'dataset_generator/protocol.json']
    files = {p: fh(ROOT / branch / p) for p in paths}
    files['../dataset_tools/geometry_dataset.py'] = fh(ROOT / 'dataset_tools/geometry_dataset.py')
    return {'branch': branch, 'record': record, 'files': files,
            'source_notes': read(ROOT / 'provenance/source_notes.json').get(record['id'], {})}

def literal_assignment(path, name):
    for node in ast.parse(Path(path).read_text(encoding='utf-8-sig')).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError(name)

def pixel_difference_scope(branch, rec, folder, context, plugin):
    import numpy as np
    original=np.array(Image.open(ROOT/branch/rec['image']).convert('RGBA'))
    candidate=np.array(Image.open(folder/'candidate.png').convert('RGBA'))
    yy,xx=np.where(np.any(original!=candidate,axis=2))
    pixels=np.stack([xx,yy],axis=1).astype(float)
    minimum=np.full(len(pixels),np.inf)
    object_minimum=np.full(len(pixels),np.inf)
    canvas=np.array(context['canvas']['data_to_pixel'])
    if branch=='SolidGeometry':
        pathmap=read(folder/'marker_path_bindings.json')
    else:
        pathmap=read(folder/'path_fingerprints.json')
    for action in plugin['params']['actions']:
        path=pathmap[action['target']][0]
        controls=path.get('controls',path.get('exact_controls'))
        for a,b in controls:
            a=(canvas@np.array([*a,1]))[:2];b=(canvas@np.array([*b,1]))[:2]
            v=b-a;t=np.clip((pixels-a)@v/(v@v),0,1)
            object_minimum=np.minimum(object_minimum,np.linalg.norm(pixels-(a+t[:,None]*v),axis=1))
        interval=action.get('interval')
        if interval:
            n=len(controls);controls=controls[round(n*interval['start']):round(n*interval['end'])]
        for a,b in controls:
            a=(canvas@np.array([*a,1]))[:2];b=(canvas@np.array([*b,1]))[:2]
            v=b-a;t=np.clip((pixels-a)@v/(v@v),0,1)
            minimum=np.minimum(minimum,np.linalg.norm(pixels-(a+t[:,None]*v),axis=1))
    assert object_minimum.max()<3.5,object_minimum.max()
    outside=minimum>=3.5
    old=original[yy[outside],xx[outside],:3];new=candidate[yy[outside],xx[outside],:3]
    assert np.all(old[:,0]==old[:,1]) and np.all(old[:,1]==old[:,2]) and np.all(new[:,0]==new[:,1]) and np.all(new[:,1]==new[:,2])
    return {'changed_pixel_count':len(pixels),'max_distance_to_styled_original_object_strokes_px':float(object_minimum.max()),
            'all_changed_pixels_within_3_5_px_of_styled_original_objects':True,
            'all_pixels_outside_styled_object_stroke_neighborhoods_identical':True,
            'changed_pixels_beyond_selected_interval_stroke_neighborhoods':int(outside.sum()),
            'those_pixels_remain_grayscale':True,
            'max_channel_delta_beyond_selected_intervals':int(np.abs(old.astype(int)-new.astype(int)).max()) if len(old) else 0,
            'partial_style_limit':('Splitting and restroking line16 changes a few grayscale antialias/join pixels on its unchanged black portions. This is renderer rasterization, not changed contour geometry; reported explicitly.' if outside.any() else 'No changed pixel lies beyond the selected stroke neighborhoods.'),
            'method':'Direct RGBA comparison to formal original; distance to independently mapped original vector stroke segments. No renderer run.'}

def audit_call_dir(folder, branch, qid, rec, expected, is_control):
    tests = list((folder / 'tests').iterdir())
    assert len(tests) == 1
    t = tests[0]
    b, summary = read(t / 'binding.json'), read(t / 'summary.json')
    req_bytes = (t / 'request.json').read_bytes()
    req = json.loads(req_bytes)
    design_bytes = (t / 'design_snapshot.json').read_bytes()
    design = json.loads(design_bytes)
    png = Path(b['image_path'])
    reference = ROOT / branch / 'workbench/quick_test.py'
    system = literal_assignment(reference, 'SYSTEM_PROMPT')
    profile = literal_assignment(reference, 'TEST_PROFILES')['quicktest3']
    checks = {
        'identity': b['question_id'] == qid and b['branch'] == branch,
        'question_exact': b['question'] == rec['question'],
        'formal_record_hash': b['question_record_sha256'] == canon(rec),
        'formal_dataset_hash': b['dataset_sha256'] == fh(ROOT / branch / 'dataset.jsonl'),
        'request_hash': b['request_body_sha256'] == sha(req_bytes),
        'reference_quick_test_hash': b['reference_quick_test_sha256'] == fh(reference),
        'system_prompt_unchanged': b['system_prompt'] == system,
        'profile': b['profile'] == 'quicktest3' and all(b['settings'][k] == v for k, v in profile.items()),
        'design_snapshot_hash': b['design_sha256'] == sha(design_bytes) == fh(folder / 'design.json'),
        'preset_snapshot': design['expected_wrong_answer'] == b['expected_wrong_answer'] == expected != rec['answer'],
        'png_hash': b['image_sha256'] == fh(png),
        'pixel_hash': b['pixel_sha256'] == pix(png),
        'only_solver_system_question_png': req == {
            'model': 'mimo-v2.6-flash', 'stream': False, 'thinking': {'type': 'disabled'},
            'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': [
                {'type': 'text', 'text': rec['question']},
                {'type': 'image_url', 'image_url': {'url': 'data:image/png;base64,' + base64.b64encode(png.read_bytes()).decode('ascii')}}]}]},
        'two_completed_summary': summary['two_completed'] and len(summary['results']) == 2,
    }
    if is_control:
        checks['separate_original_control_bytes'] = png.read_bytes() == (ROOT / branch / rec['image']).read_bytes()
    else:
        checks['tested_candidate_bytes'] = png.read_bytes() == (folder / 'candidate.png').read_bytes()
    runs = []
    for i in [1, 2]:
        start = read(t / f'run_{i:02d}_started.json')
        run = read(t / f'run_{i:02d}.json')
        rawpath = t / f'run_{i:02d}_response.json'
        raw = read(rawpath)
        fields = ['run_index', 'run_id', 'started_at', 'request_body_sha256', 'image_sha256', 'design_sha256']
        rc = {
            'start_binding': all(start[k] == run[k] for k in fields),
            'immutable_request_png_design': all(run[k] == b[k] for k in fields[3:]),
            'preset_before_start': design['created_at'] < b['created_at'] < run['started_at'],
            'raw_response_hash': run['response_sha256'] == fh(rawpath),
            'raw_answer_equals_record': raw['choices'][0]['message']['content'].strip() == run['answer'],
            'completed_http200_stop': run['http_status'] == 200 and run['status'] == 'completed' and run['finish_reason'] == raw['choices'][0]['finish_reason'] == 'stop',
            'not_truncated': run['truncated'] is False,
            'model_matches': run['response_model'] == raw['model'] == 'mimo-v2.6-flash',
            'disabled_reasoning': raw['usage']['completion_tokens_details']['reasoning_tokens'] == 0 and not run['thinking'],
            'summary_equals_complete_run': summary['results'][i - 1] == run,
            'no_unfinished_artifacts': not list(t.glob('*incomplete*')) and not list(t.glob('*error*')),
        }
        assert all(rc.values()), (qid, folder, i, rc)
        runs.append({k: run[k] for k in ['run_id', 'started_at', 'finished_at', 'response_sha256', 'http_status', 'finish_reason', 'truncated']} | {
            'response_id': raw['id'], 'response_path': rel(rawpath), 'checks': rc,
            'full_answer_sha256': sha(run['answer'].encode()),
            'provider_prompt_cached_tokens': raw['usage']['prompt_tokens_details']['cached_tokens']})
    checks['distinct_stateless_calls'] = runs[0]['run_id'] != runs[1]['run_id'] and runs[0]['response_id'] != runs[1]['response_id']
    checks['sequential_complete_calls'] = runs[0]['finished_at'] < runs[1]['started_at']
    assert all(checks.values()), (qid, folder, checks)
    return {'test_directory': rel(t), 'checks': checks, 'request_body_sha256': sha(req_bytes),
            'design_snapshot_sha256': sha(design_bytes), 'created_at': design['created_at'],
            'png_sha256': b['image_sha256'], 'pixel_sha256': b['pixel_sha256'], 'runs': runs}

def audit_evidence(branch, qid, worker, variant, controls, expected):
    folder = TASK / 'background_06' / worker / qid / variant
    own = OWN / f'{qid}_{variant}'
    rec = next(r for r in rows(ROOT / branch / 'dataset.jsonl') if r['id'] == qid)
    approve = read(ROOT / 'provenance/approvals.json')['approvals'][qid]
    plugin = read(folder / 'plugin.json')
    render = read(folder / 'render_check.json')
    context = read(folder / 'context.json')
    schema = read(ROOT / branch / 'workbench/plugin.schema.json')
    validate_schema(plugin, schema)
    errors = []
    assert not errors, errors
    objs = {o['id']: o for o in context['objects']}
    scene = read(ROOT / branch / rec['scene'])
    scene_objs = {o['id']: o for o in scene['objects']}
    whitelist = all(a['type'] == 'set_object_style' and a['color'] in ['#DC2626', '#2563EB'] and a['linewidth_pt'] in [1.5, 2] and 'linestyle' not in a and objs[a['target']]['styleable'] and objs[a['target']]['geometry'] == scene_objs[a['target']] for a in plugin['params']['actions'])
    assert whitelist
    fingerprints = render.get('frozen_inputs', render.get('input_fingerprints'))
    changes = []
    for p, old in fingerprints['files'].items():
        if fh(ROOT / p) != old:
            changes.append({'path': p, 'old': old, 'current': fh(ROOT / p)})
    assert not changes, changes
    assert fingerprints['question_record_sha256'] == canon(rec)
    hist = read(folder / 'eligibility_immediately_before_calls.json')
    authority = hist.get('checks_sha256', hist.get('authoritative_state_hashes', {}))
    authority_changed = [{'path': p, 'historical': old, 'current': fh(ROOT / p)} for p, old in authority.items() if fh(ROOT / p) != old]
    special = {}
    for name in ['accepted_index.jsonl', 'collected_index.jsonl']:
        p = ROOT / branch / 'special_variant' / name
        special[name] = [r for r in rows(p) if qid in json.dumps(r)]
    for name in ['recipes.json', 'collection.json']:
        p = ROOT / branch / 'special_variant' / qid / name
        special[name] = read(p) if p.is_file() else None
    assert all(not v for v in special.values()), special
    approval_hash = canon(formal_content(branch, rec))
    assert approval_hash == approve['content_sha256'] and approve['reviewer'] == 'user' and approve['instruction']
    replay_dir = TASK / 'delivery_validation' / qid
    replay = read(replay_dir / 'replay_verification.json')
    assert all(replay[k] for k in ['formal_noop_baseline_matches', 'matches_tested_png_bytes', 'two_delivery_replays_identical', 'formal_inputs_unchanged'])
    assert (replay_dir / 'reproduced.png').read_bytes() == (folder / 'candidate.png').read_bytes()
    assert replay['png_sha256'] == render['png_sha256'] == fh(folder / 'candidate.png')
    assert replay['pixel_sha256'] == render['pixel_sha256'] == pix(folder / 'candidate.png')
    assert replay['plugin_sha256'] == fh(folder / 'plugin.json')
    assert context['original_pixel_sha256'] == pix(ROOT / branch / rec['image'])
    source_path = ROOT / branch / f'dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/{qid}/source.json'
    source_doc = read(source_path)
    source = source_doc.get('record', source_doc)
    source_question = re.sub(r'<image\d+>', '', source['question']).strip()
    expected_question = source_question + '\nChoices:\n' + '\n'.join(f'{k}:{k}' for k in 'ABCDE')
    assert rec['question'] == expected_question and rec['answer'] == source['answer']
    assert fh(ROOT / branch / rec['original_image']) == source_doc['source_sha256']
    primary_read = {}
    for p in folder.glob('*.json'):
        primary_read[p.name] = {'sha256': fh(p), 'top_level_keys': list(read(p))}
    baseline = render.get('baseline_matches_formal', render.get('baseline_pixel_match'))
    repeat = render.get('deterministic', render.get('two_byte_identical_redraws'))
    assert baseline and repeat
    evidence = {
        'question_id': qid, 'independent_audited_at': datetime.now(timezone.utc).isoformat(),
        'formal_record_sha256': canon(rec), 'formal_question': rec['question'], 'formal_answer': rec['answer'],
        'formal_source_dataset': rec['source_dataset'], 'formal_source_key': rec['source_key'],
        'original_approval': approve, 'recomputed_approval_content_sha256': approval_hash,
        'source_record': {'source_json_path': rel(source_path), 'source_answer': source['answer'], 'source_options': source['options'],
                          'formal_question_equals_source_minus_image_tags_plus_choice_list': True,
                          'original_source_jpg_hash_verified': True},
        'current_special_state': special, 'current_eligible': rec['source_dataset'] == 'MathVision' and not any(special.values()),
        'schema_validation_errors': errors, 'all_actions_whitelisted_and_bind_original_scene_geometry': whitelist,
        'frozen_fingerprint_file_count': len(fingerprints['files']), 'frozen_fingerprint_mismatches': changes,
        'authoritative_historical_hash_mismatches': authority_changed,
        'runtime_progress_diagnostics': {str(p.relative_to(ROOT)): fh(p) for p in [TASK / 'exploration_report.json', TASK / 'remaining_questions.jsonl']},
        'historical_runtime_progress_hashes': hist.get('diagnostic_runtime_metadata_hashes', {'remaining_questions.jsonl': hist.get('remaining_sha256'), 'exploration_report.json': hist.get('report_sha256')}),
        'mutable_progress_rule': 'Historical records and false diagnostics left unchanged. Runtime progress hashes are diagnostic; formal approval and actual Special state establish current eligibility.',
        'no_op_baseline': baseline, 'primary_repeated_bytes': repeat,
        'parent_portable_replay_report': replay, 'parent_reproduced_png_current_bytes_verified': True,
        'parent_replay_limit': 'Existing two-replay report inspected; no new renderer executed. Its retained reproduced PNG was hashed and compared directly.',
        'pixel_difference_scope': pixel_difference_scope(branch,rec,folder,context,plugin),
        'primary_json_files_read': primary_read,
        'candidate': audit_call_dir(folder, branch, qid, rec, expected, False),
        'original_controls': audit_call_dir(folder.parent / controls, branch, qid, rec, expected, True),
        'runtime_policy': {'python_B': True, 'project_modules_imported': False, 'render_executed': False, 'new_solver_calls': 0,
                           'own_outputs_only': True},
    }
    assert not authority_changed, authority_changed
    write(own / 'evidence_audit.json', evidence)
    return rec, scene, context, plugin, folder, own

def edge(a, b):
    return tuple(sorted((tuple(a), tuple(b))))

def cell_edges(x, y):
    return {edge((x,y), (x+1,y)), edge((x+1,y), (x+1,y+1)), edge((x+1,y+1), (x,y+1)), edge((x,y+1), (x,y))}

def norm(cells):
    x0 = min(x for x,y in cells); y0 = min(y for x,y in cells)
    return frozenset((x-x0,y-y0) for x,y in cells)

def orientations(cells):
    result = set()
    for reflect in [1, -1]:
        for k in range(4):
            q = [(reflect*x,y) for x,y in cells]
            for _ in range(k): q = [(-y,x) for x,y in q]
            result.add(norm(q))
    return result

def boundary(cells):
    counts = Counter(e for c in cells for e in cell_edges(*c))
    return {e for e, n in counts.items() if n == 1}

def plane_math(scene, context, plugin, folder, own):
    groups = {}
    for group in ['given', *'ABCDE']:
        edges = {edge(*o['points']) for o in scene['objects'] if o['id'].startswith(group+'_')}
        xs = [p[0] for e in edges for p in e]; ys = [p[1] for e in edges for p in e]
        cells = {(x,y) for x in range(min(xs),max(xs)) for y in range(min(ys),max(ys)) if cell_edges(x,y) <= edges}
        groups[group] = cells
    board = norm(groups['given'])
    assert board == frozenset(itertools.product(range(4), repeat=2)) - {(3,0)}
    results = {}
    for letter in 'ABCDE':
        variants = orientations(groups[letter]); placements = set()
        for v in variants:
            for dx in range(4):
                for dy in range(4):
                    placed = frozenset((x+dx,y+dy) for x,y in v)
                    if placed <= board: placements.add(placed)
        ordered = sorted(placements, key=lambda p: sorted(p))
        covers = []
        for triple in itertools.combinations(ordered, 3):
            if len(set.union(*(set(p) for p in triple))) == 15:
                assert set.union(*(set(p) for p in triple)) == board
                covers.append([sorted(p) for p in triple])
        results[letter] = {'cells': sorted(norm(groups[letter])), 'orientation_count': len(variants),
                           'placement_count': len(ordered), 'solution_count': len(covers), 'witnesses': covers,
                           'unordered_triples_exhausted': math.comb(len(ordered),3)}
    primary = read(folder.parent / 'mathematical_enumeration.json')
    for letter in 'ABCDE':
        for k in ['cells', 'orientation_count', 'placement_count', 'solution_count']:
            assert json.loads(json.dumps(results[letter][k])) == primary['results'][letter][k]
    assert [k for k,v in results.items() if v['solution_count']] == ['A']
    # Independently recover every U placement whose entire boundary is red.
    objects = {o['id']:o for o in scene['objects']}
    colored = {a['target'] for a in plugin['params']['actions']}
    board_edges = {edge(*objects[q]['points']) for q in colored if q.startswith('given_')}
    all_u = set()
    for v in orientations(groups['B']):
        for dx in range(11,15):
            for dy in range(7,11):
                p = frozenset((x+dx,y+dy) for x,y in v)
                if p <= groups['given'] and boundary(p) <= board_edges: all_u.add(p)
    patches = sorted(all_u, key=lambda p:sorted(p))
    assert len(patches)==2 and patches[0].isdisjoint(patches[1])
    leftover = groups['given'] - set.union(*(set(p) for p in patches))
    components = []
    remaining = set(leftover)
    while remaining:
        component = {remaining.pop()}; frontier = list(component)
        while frontier:
            x,y = frontier.pop()
            for n in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if n in remaining:remaining.remove(n);component.add(n);frontier.append(n)
        components.append(sorted(component))
    assert len(components)==2 and sorted(map(len,components))==[2,3]
    patch_bounds = [boundary(p) for p in patches]
    assert board_edges == set.union(*patch_bounds)
    b_edges = {edge(*objects[q]['points']) for q in colored if q.startswith('B_')}
    assert b_edges == boundary(groups['B'])
    assert len(colored)==34 and len(board_edges)==22 and len(b_edges)==12
    # Explicitly test the literal-given-cut reading of the highlighted network.
    unvisited=set(groups['given']); cut_components=[]
    while unvisited:
        component={unvisited.pop()}; frontier=list(component)
        while frontier:
            x,y=frontier.pop()
            for n in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if n in unvisited and not (cell_edges(x,y)&cell_edges(*n)&board_edges):
                    unvisited.remove(n);component.add(n);frontier.append(n)
        cut_components.append(sorted(component))
    assert sorted(map(len,cut_components))==[2,3,5,5]
    role_list = []
    for i,a in enumerate(plugin['params']['actions']):
        q = a['target']; e = edge(*objects[q]['points'])
        roles = [f'source_U_{j+1}_complete_boundary' for j,b in enumerate(patch_bounds) if e in b] if q.startswith('given_') else ['B_U_complete_boundary']
        assert roles
        role_list.append({'action_index':i, 'target':q, 'edge':e, 'roles':roles})
    # Validate saved exact vector controls and their hashes without a renderer.
    paths = read(folder/'path_fingerprints.json'); targets={t['id']:t for t in context['canvas']['targets']}
    for q, ps in paths.items():
        for p in ps:
            assert canon(p['exact_controls'])==p['sha256']
            assert targets[q]['partial_paths'][0]['sha256']==p['sha256']
            assert edge(*[(round(x),round(y)) for x,y in p['exact_controls'][0]]) == edge(*objects[q]['points'])
    d={'question_id':'Plane233', 'method':'Recover cells from four frozen unit edges; independently generate all D4 orientations and translations, enumerate every unordered triple of legal placements.',
       'board_cells': sorted(board), 'actual_board_cells':sorted(groups['given']), 'options':results,
       'matches_primary_counts_and_cells':True,'unique_correct_answer':'A', 'marked_patches':[sorted(p) for p in patches],
       'complement':sorted(leftover),'complement_components':components,'complement_is_U':norm(leftover) in orientations(groups['B']),
       'patch_boundary_counts':[len(b) for b in patch_bounds], 'shared_board_boundary_edges':sorted(patch_bounds[0]&patch_bounds[1]),
       'if_red_edges_are_given_cuts_components':cut_components,'if_red_edges_are_given_cuts_areas':sorted(map(len,cut_components)),
       'distinct_board_actions':22,'distinct_B_actions':12,'all_34_exact_roles':role_list,'exact_path_hashes_verified':True,
       'congruence_interpretation':'Three equal pieces is interpreted as three congruent grid pieces, the original puzzle convention. All five options already have area five, so area-only would not be a single-answer puzzle.'}
    write(own/'independent_math.json',d)
    return d

def solid_math(scene, context, plugin, folder, own):
    import numpy as np
    pts = {k:np.array(v,float) for k,v in scene['points'].items()}
    origin = pts['p1']; u=(pts['p2']-origin)/2; v=(pts['p7']-origin)/2
    assert np.allclose([u@u,v@v,u@v],[1,1,0],rtol=0,atol=1e-12)
    flat = {f'p{i}':[float((pts[f'p{i}']-origin)@u),float((pts[f'p{i}']-origin)@v)] for i in range(1,11)}
    expected = [[0,0],[2,0],[2,2],[1.17,2],[1,2-.17*math.sqrt(3)],[.83,2],[0,2],[0,1.17],[.17*math.sqrt(3),1],[0,.83]]
    assert np.allclose(list(flat.values()),expected,rtol=0,atol=1e-12)
    # Rigid rotation between the rear and front packet verified in world 3D.
    a=np.stack([pts[f'p{i}'] for i in range(1,11)]); b=np.stack([pts[f'p{i}'] for i in range(11,21)])
    assert np.max(np.abs(np.linalg.norm(a[:,None]-a[None,:],axis=2)-np.linalg.norm(b[:,None]-b[None,:],axis=2)))<1e-12
    pmat=np.array(scene['projection']['matrix']);porigin=np.array(scene['projection']['origin']);offset=np.array(scene['projection']['offset'])
    objects={o['id']:o for o in scene['objects']}
    paths=read(folder/'marker_path_bindings.json')
    for q, ps in paths.items():
        o=objects[q]; projected=[(pmat@(pts[p]-porigin)+offset).tolist() for p in o['points']]
        expected_controls=[[a,b] for a,b in zip(projected,projected[1:])]
        assert np.allclose(ps[0]['controls'],expected_controls,rtol=0,atol=2e-14)
        assert canon(ps[0]['controls'])==ps[0]['sha256']
    assert paths['line16'][0]['sha256']=='7ec1c604af8d1cb5cd032e04e6ea2b509d729ab335ea2f691bd6d0adb824edeb'
    intervals=[]
    for action in plugin['params']['actions'][:2]:
        it=action['interval']; n=len(paths['line16'][0]['controls']);lo=round(it['start']*n);hi=round(it['end']*n)
        assert (lo,hi) in [(3,5),(7,9)]
        intervals.append({'interval':[it['start'],it['end']],'segment_indices':list(range(lo,hi)),
                          'point_ids':objects['line16']['points'][lo:hi+1], 'exact_controls':paths['line16'][0]['controls'][lo:hi]})
    # Put the opened full sheet in [0,4]^2: reflection axes u=0,v=2.
    upper=np.array([flat['p4'],flat['p5'],flat['p6'],[1,4-flat['p5'][1]]])
    left=np.array([flat['p8'],flat['p9'],flat['p10'],[-flat['p9'][0],1]])
    # Translation +2 in u gives sheet center (2,2); duplicates across other fold.
    result=[]
    for label,hole in [('upper',upper),('left',left)]:
        for j in range(2):
            h=hole.copy()
            if j:
                if label=='upper':h[:,0]*=-1
                else:h[:,1]=4-h[:,1]
            h[:,0]+=2
            width,height=np.ptp(h,axis=0)
            result.append({'cut':label,'center':h.mean(axis=0).tolist(),'width':float(width),'height':float(height),
                           'orientation':'vertical' if height>width else 'horizontal'})
    option_data={}
    faces=[o for o in scene['objects'] if o['type']=='face' and o.get('holes')]
    im=Image.open(folder/'candidate.png').convert('RGBA')
    canvas=np.array(context['canvas']['data_to_pixel'])
    for letter, face in zip('ABCDE',faces):
        outer=np.array([pts[p][:2] for p in face['points']]); center=outer.mean(axis=0); holes=[]
        for ring in face['holes']:
            arr=np.array([pts[p][:2] for p in ring]);c=arr.mean(axis=0);w,h=np.ptp(arr,axis=0)
            position='center' if np.linalg.norm(c-center)<1e-8 else ('left' if c[0]<center[0]-1e-8 else 'right' if c[0]>center[0]+1e-8 else 'top' if c[1]>center[1] else 'bottom')
            pixel=canvas@np.array([*c,1]);rgba=im.getpixel((round(pixel[0]),round(pixel[1])))
            assert rgba==(255,255,255,255)
            holes.append({'position':position,'width':float(w),'height':float(h),'orientation':'square' if abs(w-h)<1e-12 else 'vertical' if h>w else 'horizontal','white_center_rgba':rgba})
        option_data[letter]=holes
    assert all(h['orientation']==('vertical' if h['position'] in ['left','right'] else 'horizontal') for h in option_data['C'])
    d={'question_id':'Solid142','orthonormal_packet_basis':[u.tolist(),v.tolist()],'flat_rear_contour':flat,
       'front_packet_congruent_in_world_3d':True,'line16_path_sha256':paths['line16'][0]['sha256'],
       'exact_notch_interval_vertices':intervals,'unfolded_holes':result,'actual_option_holes':option_data,
       'projection_visibility_binding_verified':canon(scene['projection'])==scene['visibility']['projection_sha256'],
       'unique_correct_answer':'C','exclusions':{'A':'all four vertical; top/bottom should be horizontal','B':'squares rather than non-square rhombi','D':'all four horizontal; left/right should be vertical','E':'extra central hole with no cut at folded corner'},
       'original_given_interpretation':'The schematic partly opened quarter packet encodes two perpendicular folds; the same visible fold construction and notches occur in source, formal and candidate. No fold sequence, dimensions or relation is added by styling.'}
    assert d['projection_visibility_binding_verified']
    write(own/'independent_math.json',d)
    return d

if __name__=='__main__':
    for case in CASES:
        rec,scene,context,plugin,folder,own=audit_evidence(*case)
        math_result=solid_math(scene,context,plugin,folder,own) if case[1]=='Solid142' else plane_math(scene,context,plugin,folder,own)
        print(json.dumps({'question_id':case[1],'evidence_checks':'all passed','math_unique_answer':math_result['unique_correct_answer'],'review_directory':rel(own)}))
