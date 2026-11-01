"""Read-only evidence checks for one independent review; run with Python -B."""
from pathlib import Path
from collections import Counter
from datetime import datetime
from itertools import combinations
import ast
import base64
import hashlib
import json
import math
import os
import re
import sys

sys.dont_write_bytecode = True
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
TASK = ROOT / 'runtime/mathvision_special_20261101'
CAND = TASK / 'background_03/solid_worker/Solid203/bridge_terminal_edge_pair'
DELIVERY = TASK / 'delivery_validation/Solid203'
for variable, name in [('TEMP', 'tmp'), ('TMP', 'tmp'), ('MPLCONFIGDIR', 'mpl'), ('XDG_CACHE_HOME', 'cache')]:
    folder = OUT / name
    folder.mkdir(exist_ok=True)
    os.environ[variable] = str(folder)

from PIL import Image, ImageChops

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def file_sha(path):
    return sha(Path(path).read_bytes())

def canonical(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())

def rel(path):
    return Path(path).relative_to(ROOT).as_posix()

def pixels(path):
    with Image.open(path) as image:
        rgba = image.convert('RGBA')
        return rgba, sha(f'{rgba.width}x{rgba.height}:RGBA:'.encode() + rgba.tobytes())

record = next(r for r in map(json.loads, (ROOT / 'SolidGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines()) if r['id'] == 'Solid203')
scene_path = ROOT / 'SolidGeometry' / record['scene']
scene = read(scene_path)
render = read(CAND / 'replay/render_check.json')
frozen = render['frozen_inputs']['files']
protected = set(CAND.rglob('*')) | {ROOT / p for p in frozen}
protected |= {ROOT / p for p in ['SolidGeometry/dataset.jsonl', 'SolidGeometry/special_variant/accepted_index.jsonl', 'SolidGeometry/special_variant/collected_index.jsonl', 'provenance/approvals.json']}
protected |= {DELIVERY / 'replay_verification.json', DELIVERY / 'reproduced.png'}
before = {rel(p): file_sha(p) for p in protected if p.is_file()}
checks = {}

def check(name, condition):
    checks[name] = bool(condition)

check('formal_MathVision', record['source_dataset'] == 'MathVision' and record['source_key'] == 'test:1943' and record['answer'] == 'E')
check('formal_snapshot_equal', read(CAND / 'formal_record.json') == record)
eligibility = {}
for name in ['accepted_index.jsonl', 'collected_index.jsonl']:
    path = ROOT / 'SolidGeometry/special_variant' / name
    entries = [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    matches = [entry for entry in entries if 'Solid203' in json.dumps(entry, ensure_ascii=False)]
    eligibility[name] = {'sha256': file_sha(path), 'matching_records': matches}
check('no_Pass_Collect_or_special_case', not any(x['matching_records'] for x in eligibility.values()) and not (ROOT / 'SolidGeometry/special_variant/Solid203').exists())
approval = read(ROOT / 'provenance/approvals.json')['approvals']['Solid203']
approval_paths = [record[k] for k in ['image', 'original_image', 'script', 'scene'] if record.get(k)] + record['runtime_dependencies'] + ['dataset_generator/common_renderer.py', 'dataset_generator/protocol.json']
approval_files = {p: file_sha(ROOT / 'SolidGeometry' / p) for p in approval_paths}
approval_files['../dataset_tools/geometry_dataset.py'] = file_sha(ROOT / 'dataset_tools/geometry_dataset.py')
approval_content = {'branch': 'SolidGeometry', 'record': record, 'files': approval_files, 'source_notes': read(ROOT / 'provenance/source_notes.json').get('Solid203', {})}
approval_computed = canonical(approval_content)
check('current_formal_user_approval_fingerprint', approval_computed == approval['content_sha256'] and approval['reviewer'] == 'user' and bool(approval['instruction']))
frozen_checks = {p: {'expected': expected, 'actual': file_sha(ROOT / p)} for p, expected in frozen.items()}
check('all_frozen_input_files_match', all(x['expected'] == x['actual'] for x in frozen_checks.values()))
check('frozen_question_record_match', canonical(record) == render['frozen_inputs']['question_record_sha256'])
check('runtime_adapter_hash_matches', file_sha(TASK / 'background_03/solid_worker/bridge_adapter_local.py') == render['frozen_inputs']['runtime_adapter_sha256'])

plugin = read(CAND / 'plugin.json')
schema = read(ROOT / 'SolidGeometry/workbench/plugin.schema.json')
def schema_validate(value, rule, path='$'):
    """Validate the actual schema keywords used by this plugin, without dependencies."""
    if '$ref' in rule:
        ref = rule['$ref']
        assert ref.startswith('#/$defs/')
        return schema_validate(value, schema['$defs'][ref.rsplit('/', 1)[1]], path)
    if 'oneOf' in rule:
        branches = [schema_validate(value, branch, path) for branch in rule['oneOf']]
        return [] if sum(not errors for errors in branches) == 1 else [path + ': oneOf failed']
    errors = []
    types = {'object': dict, 'array': list, 'string': str, 'number': (int, float), 'boolean': bool}
    if 'type' in rule and (not isinstance(value, types[rule['type']]) or (rule['type'] == 'number' and isinstance(value, bool))):
        return [path + ': wrong type']
    if 'const' in rule and value != rule['const']:
        errors.append(path + ': const failed')
    if 'enum' in rule and value not in rule['enum']:
        errors.append(path + ': enum failed')
    if isinstance(value, dict):
        if any(k not in value for k in rule.get('required', [])):
            errors.append(path + ': missing required property')
        if rule.get('additionalProperties') is False and set(value) - set(rule.get('properties', {})):
            errors.append(path + ': unknown property')
        for key, item in value.items():
            if key in rule.get('properties', {}):
                errors.extend(schema_validate(item, rule['properties'][key], path+'.'+key))
    if isinstance(value, list):
        if len(value) < rule.get('minItems', 0) or len(value) > rule.get('maxItems', math.inf):
            errors.append(path + ': item count failed')
        for i, item in enumerate(value):
            if 'items' in rule:
                errors.extend(schema_validate(item, rule['items'], path+f'[{i}]'))
    if isinstance(value, str):
        if len(value) > rule.get('maxLength', math.inf) or ('pattern' in rule and not re.search(rule['pattern'], value)):
            errors.append(path + ': string constraint failed')
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if value < rule.get('minimum', -math.inf) or value > rule.get('maximum', math.inf):
            errors.append(path + ': numeric range failed')
    return errors
schema_errors = schema_validate(plugin, schema)
check('plugin_valid_actual_schema', not schema_errors)
check('only_two_permitted_original_edge_style_actions', plugin['params']['actions'] == [
    {'type': 'set_object_style', 'target': 'line_20', 'color': '#DC2626', 'linewidth_pt': 2},
    {'type': 'set_object_style', 'target': 'line_24', 'color': '#DC2626', 'linewidth_pt': 2}])
objects = {obj['id']: obj for obj in scene['objects']}
context = read(CAND / 'replay/context.json')
context_objects = {obj['id']: obj for obj in context['objects']}
edge_binding = {'x': 'line_20', 'A': 'line_24', 'B': 'line_15', 'C': 'line_8', 'D': 'line_13', 'E': 'line_11'}
label_bindings = {}
for label, edge_id in edge_binding.items():
    edge = objects[edge_id]
    points = [scene['points'][v] for v in edge['points']]
    label_object = next(obj for obj in scene['labels'] if obj['text'] == label)
    midpoint = [sum(p[i] for p in points) / 2 for i in range(3)]
    label_bindings[label] = {'object': edge_id, 'points': edge['points'], 'label_id': label_object['id'], 'anchor': label_object['anchor'], 'anchor_is_edge_midpoint': all(abs(a-b) < 1e-12 for a, b in zip(midpoint, scene['points'][label_object['anchor']]))}
check('all_label_source_bindings', all(x['anchor_is_edge_midpoint'] for x in label_bindings.values()))
check('selected_context_matches_formal_objects', all(context_objects[e]['geometry'] == objects[e] and context_objects[e]['source_call'] == {'scene_object_id': e, 'native_object_id': e} for e in ['line_20', 'line_24']))

# Independent seed differs from the primary proof. Derive propagation from formal faces.
faces = {obj['id']: obj['points'] for obj in scene['objects'] if obj['type'] == 'face' and all(p.startswith('n') for p in obj['points'])}
folded = {'n0': (1, 0, 0), 'n1': (0, 1, 0), 'n2': (0, 0, 1)}
known = {'face0'}
propagation = []
while len(known) < len(faces):
    progress = False
    for old in list(sorted(known)):
        for new in sorted(set(faces) - known):
            common = set(faces[old]) & set(faces[new])
            if len(common) != 2:
                continue
            a = next(iter(set(faces[old]) - common))
            b = next(iter(set(faces[new]) - common))
            value = tuple(-v for v in folded[a])
            if b in folded:
                assert folded[b] == value
            folded[b] = value
            propagation.append({'from': old, 'to': new, 'hinge': sorted(common), 'opposite_vertices': [a, b], 'assigned': value})
            known.add(new)
            progress = True
    if not progress:
        raise ValueError('Disconnected or inconsistent face propagation')
face_triples = {name: sorted(folded[v] for v in vertices) for name, vertices in sorted(faces.items())}
physical_edges = Counter(tuple(sorted([folded[a], folded[b]])) for vertices in faces.values() for a, b in combinations(vertices, 2))
endpoint_pairs = {label: sorted(folded[v] for v in objects[edge_id]['points']) for label, edge_id in edge_binding.items()}
matches = [label for label in 'ABCDE' if endpoint_pairs[label] == endpoint_pairs['x']]
net_segments = {tuple(sorted(obj['points'])) for obj in scene['objects'] if obj['type'] == 'segment' and all(p.startswith('n') for p in obj['points'])}
side_lengths = [math.dist(scene['points'][a], scene['points'][b]) for vertices in faces.values() for a, b in combinations(vertices, 2)]
check('eight_regular_triangles_with_all_edges_present', len(faces) == 8 and all(abs(x-1) < 1e-12 for x in side_lengths) and all(tuple(sorted(pair)) in net_segments for vertices in faces.values() for pair in combinations(vertices, 2)))
check('all_eight_octahedron_faces_distinct', len({tuple(x) for x in face_triples.values()}) == 8)
check('six_vertices_twelve_edges_each_in_two_faces', len(set(folded.values())) == 6 and len(physical_edges) == 12 and set(physical_edges.values()) == {2})
check('unique_correct_answer_E', matches == ['E'])
mathematics = {'seed_face': 'face0', 'seed': {k: list(folded[k]) for k in ['n0', 'n1', 'n2']}, 'propagation': propagation, 'folded_vertices': folded, 'all_face_triples': face_triples, 'labelled_endpoints': endpoint_pairs, 'unique_match': matches}

candidate, candidate_pixels = pixels(CAND / 'candidate.png')
original, original_pixels = pixels(ROOT / 'SolidGeometry' / record['image'])
diff = ImageChops.difference(candidate.convert('RGB'), original.convert('RGB'))
changed = [(i % diff.width, i // diff.width) for i, value in enumerate(diff.get_flattened_data()) if any(value)]
transform = context['canvas']['data_to_pixel']
def projected(vertex):
    p = scene['points'][vertex]
    return tuple(sum(row[i]*p[i] for i in range(2)) + row[2] for row in transform[:2])
def distance_to_segment(p, a, b):
    d = (b[0]-a[0], b[1]-a[1])
    t = max(0, min(1, sum((p[i]-a[i])*d[i] for i in range(2)) / sum(v*v for v in d)))
    return math.dist(p, tuple(a[i] + t*d[i] for i in range(2)))
segments = {edge: [projected(p) for p in objects[edge]['points']] for edge in ['line_20', 'line_24']}
max_distance = max(min(distance_to_segment(p, *ends) for ends in segments.values()) for p in changed)
check('opaque_standard_candidate', candidate.size == (768, 768) and candidate.getextrema()[3] == (255, 255) and candidate.getpixel((0, 0)) == (255, 255, 255, 255))
check('actual_pixel_changes_only_along_two_selected_edges', len(changed) > 0 and max_distance < 3)
images = {'candidate_png_sha256': file_sha(CAND / 'candidate.png'), 'candidate_pixel_sha256': candidate_pixels, 'formal_png_sha256': file_sha(ROOT / 'SolidGeometry' / record['image']), 'formal_pixel_sha256': original_pixels, 'source_jpg_sha256': file_sha(ROOT / 'SolidGeometry' / record['original_image']), 'modified_pixel_count': len(changed), 'modified_bbox': diff.getbbox(), 'projected_mark_endpoints_px': segments, 'max_modified_pixel_distance_from_selected_edges_px': max_distance}
check('replay_and_delivery_png_bytes_identical', (CAND / 'candidate.png').read_bytes() == (CAND / 'replay/candidate.png').read_bytes() == (DELIVERY / 'reproduced.png').read_bytes())
check('original_control_bytes_equal_formal_png', (CAND / 'original.png').read_bytes() == (ROOT / 'SolidGeometry' / record['image']).read_bytes())
delivery = read(DELIVERY / 'replay_verification.json')
check('delivery_and_primary_report_hashes_match_actual', all(report['png_sha256'] == images['candidate_png_sha256'] and report['pixel_sha256'] == candidate_pixels for report in [delivery, render]) and delivery['formal_noop_baseline_matches'] and delivery['two_delivery_replays_identical'])

tree = ast.parse((ROOT / 'SolidGeometry/workbench/quick_test.py').read_text(encoding='utf-8-sig'))
constants = {target.id: ast.literal_eval(node.value) for node in tree.body if isinstance(node, ast.Assign) for target in node.targets if isinstance(target, ast.Name) and target.id in {'SYSTEM_PROMPT', 'TEST_PROFILES'}}
tests = {}
for kind, subdir, imagepath, designpath, manual_finals in [
    ('candidate', 'tests/quicktest3_20261101T113921_5c07ba30a1ea', CAND/'candidate.png', CAND/'design.json', ['A', 'A']),
    ('control', 'control_tests/quicktest3_20261101T114107_ebe8657e7600', CAND/'original.png', CAND/'control_design.json', ['A', 'B'])]:
    directory = CAND / subdir
    binding = read(directory / 'binding.json')
    request = read(directory / 'request.json')
    snapshot = read(directory / 'design_snapshot.json')
    summary = read(directory / 'summary.json')
    check(kind+'_request_hash', file_sha(directory/'request.json') == binding['request_body_sha256'])
    check(kind+'_image_and_pixels_hash', file_sha(imagepath) == binding['image_sha256'] and pixels(imagepath)[1] == binding['pixel_sha256'])
    check(kind+'_image_path_identity', Path(binding['image_path']).resolve() == imagepath.resolve())
    check(kind+'_design_and_snapshot_hash', designpath.read_bytes() == (directory/'design_snapshot.json').read_bytes() and file_sha(designpath) == binding['design_sha256'])
    check(kind+'_question_and_dataset_hash', canonical(record) == binding['question_record_sha256'] and file_sha(ROOT/'SolidGeometry/dataset.jsonl') == binding['dataset_sha256'] and binding['question'] == record['question'])
    check(kind+'_reference_quicktest_hash', file_sha(ROOT/'SolidGeometry/workbench/quick_test.py') == binding['reference_quick_test_sha256'])
    check(kind+'_quicktest3_profile', binding['profile'] == 'quicktest3' and {k:binding['settings'][k] for k in constants['TEST_PROFILES']['quicktest3']} == constants['TEST_PROFILES']['quicktest3'])
    check(kind+'_payload_keys_and_settings', set(request) == {'model', 'stream', 'thinking', 'messages'} and request['model'] == 'mimo-v2.6-flash' and request['thinking'] == {'type':'disabled'} and request['stream'] is False)
    messages = request['messages']
    check(kind+'_only_existing_system_prompt_and_one_user_message', len(messages) == 2 and messages[0] == {'role':'system', 'content':constants['SYSTEM_PROMPT']} and set(messages[1]) == {'role','content'} and messages[1]['role'] == 'user' and len(messages[1]['content']) == 2)
    content = messages[1]['content']
    check(kind+'_only_formal_question_and_exact_image_bytes', content[0] == {'type':'text', 'text':record['question']} and set(content[1]) == {'type','image_url'} and content[1]['type'] == 'image_url' and set(content[1]['image_url']) == {'url'} and content[1]['image_url']['url'].startswith('data:image/png;base64,') and base64.b64decode(content[1]['image_url']['url'].split(',',1)[1], validate=True) == imagepath.read_bytes())
    run_records = []
    for index in [1, 2]:
        run = read(directory / f'run_{index:02d}.json')
        start = read(directory / f'run_{index:02d}_started.json')
        responsepath = directory / f'run_{index:02d}_response.json'
        response = read(responsepath)
        choice = response['choices'][0]
        check(f'{kind}_run{index}_response_hash', file_sha(responsepath) == run['response_sha256'])
        check(f'{kind}_run{index}_start_and_bindings', all(run[k] == start[k] for k in start) and all(run[k] == binding[k] for k in ['request_body_sha256','image_sha256','design_sha256']))
        check(f'{kind}_run{index}_complete_untruncated_model', run['status'] == 'completed' and run['http_status'] == 200 and run['truncated'] is False and run['finish_reason'] == choice['finish_reason'] == 'stop' and run['response_model'] == response['model'] == 'mimo-v2.6-flash' and len(response['choices']) == 1 and choice['message']['content'].strip() == run['answer'] and response['usage']['completion_tokens_details']['reasoning_tokens'] == 0 and not run['thinking'])
        check(f'{kind}_run{index}_summary_equal', summary['results'][index-1] == run)
        check(f'{kind}_run{index}_binding_precedes_start', datetime.fromisoformat(binding['created_at']) < datetime.fromisoformat(start['started_at']))
        run_records.append({'run':index, 'run_id':run['run_id'], 'response_id':response['id'], 'started_at':run['started_at'], 'finished_at':run['finished_at'], 'response_sha256':file_sha(responsepath), 'raw_body_bytes':responsepath.stat().st_size, 'finish_reason':choice['finish_reason'], 'final_answer_manually_read':manual_finals[index-1], 'final_excerpt':choice['message']['content'][-220:], 'usage':response['usage']})
    check(kind+'_two_separate_run_and_response_ids', run_records[0]['run_id'] != run_records[1]['run_id'] and run_records[0]['response_id'] != run_records[1]['response_id'])
    check(kind+'_second_request_after_first_completion', datetime.fromisoformat(run_records[0]['finished_at']) < datetime.fromisoformat(run_records[1]['started_at']))
    tests[kind] = {'evidence_directory':rel(directory), 'binding_created_at':binding['created_at'], 'request_sha256':binding['request_body_sha256'], 'design_sha256':binding['design_sha256'], 'image_sha256':binding['image_sha256'], 'pixel_sha256':binding['pixel_sha256'], 'question_record_sha256':binding['question_record_sha256'], 'dataset_sha256':binding['dataset_sha256'], 'runs':run_records, 'manual_final_answers':manual_finals}
check('target_A_frozen_before_both_candidate_calls', read(CAND/'design.json')['expected_wrong_answer'] == 'A' and read(CAND/'tests/quicktest3_20261101T113921_5c07ba30a1ea/design_snapshot.json')['expected_wrong_answer'] == 'A')
prepared = read(CAND/'prepared_copy.json')['files_sha256']
check('immutable_prepared_copy_hashes', all(file_sha(CAND/p) == expected for p, expected in prepared.items()))
check('original_evidence_and_formal_inputs_unchanged_during_audit', all(file_sha(ROOT/p) == expected for p, expected in before.items()))
audit = {'checks':checks, 'all_checks_pass':all(checks.values()), 'schema_errors':schema_errors, 'eligibility':eligibility, 'approval':{'stored_sha256':approval['content_sha256'], 'computed_sha256':approval_computed, 'approved_at_utc':approval['approved_at_utc']}, 'frozen_input_checks':frozen_checks, 'question_record_sha256':canonical(record), 'label_source_bindings':label_bindings, 'mathematics':mathematics, 'images':images, 'tests':tests, 'protected_input_hashes':before, 'renderer_reexecuted_by_this_reviewer':False}
with (OUT/'technical_audit.json').open('w', encoding='utf-8', newline='\n') as stream:
    json.dump(audit, stream, ensure_ascii=False, indent=2)
    stream.write('\n')
print(json.dumps({'all_checks_pass':audit['all_checks_pass'], 'failed_checks':[k for k,v in checks.items() if not v], 'checks_count':len(checks), 'mathematics':mathematics, 'images':images, 'tests':tests}, ensure_ascii=False, indent=2))
