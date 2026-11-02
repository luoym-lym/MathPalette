from review_env import *
import base64
import copy
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from PIL import Image

QID = 'Plane242'
VID = 'r24_disconnected_gray_arc_assembly'
CAND = BASE / 'background_24' / QID / VID
TEST = next((CAND / 'tests').iterdir())
BRANCH = ROOT / 'PlaneGeometry'
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def rows(p): return [json.loads(x) for x in Path(p).read_text(encoding='utf-8-sig').splitlines() if x.strip()]
def sha(data): return hashlib.sha256(data).hexdigest()
def fh(p): return sha(Path(p).read_bytes()) if Path(p).is_file() else None
def canon(x): return sha(json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode())
def now(): return datetime.now(timezone.utc).isoformat()
def write(p, data):
    with (HERE / p).open('x', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False); f.write('\n')
def rel(p): return str(Path(p).relative_to(ROOT))
def inventory(paths):
    result = {}
    for p in sorted(set(paths)):
        s = p.stat()
        result[rel(p)] = {'sha256':fh(p), 'bytes':s.st_size,
                         'mtime_utc':datetime.fromtimestamp(s.st_mtime, timezone.utc).isoformat(),
                         'ctime_utc':datetime.fromtimestamp(s.st_ctime, timezone.utc).isoformat()}
    return result

record = next(x for x in rows(BRANCH / 'dataset.jsonl') if x['id'] == QID)
design = read(CAND / 'design.json')
binding = read(TEST / 'binding.json')
plugin = read(CAND / 'plugin.json')
context = read(CAND / 'context.json')
render_check = read(CAND / 'render_check.json')
paths = [p for p in CAND.rglob('*') if p.is_file()]
paths += [BRANCH / record[k] for k in ('image','original_image','scene','script')]
paths += [BRANCH / p for p in record['runtime_dependencies']]
paths += [BRANCH / 'dataset_generator/common_renderer.py', BRANCH / 'dataset_generator/protocol.json',
          ROOT / 'dataset_tools/geometry_dataset.py', ROOT / 'dataset_tools/mathvision_workbench.py',
          ROOT / 'provenance/approvals.json', BRANCH / 'dataset.jsonl',
          BRANCH / 'special_variant/accepted_index.jsonl', BRANCH / 'special_variant/collected_index.jsonl',
          ROOT / 'MATHPALETTE_PROTOCOL.md', ROOT / 'AGENTS.md', BRANCH / 'REDRAW_PROTOCOL.md',
          BRANCH / 'workbench/README.md', BRANCH / 'workbench/agent_prompt.md',
          BRANCH / 'workbench/plugin.schema.json', BRANCH / 'workbench/quick_test.py',
          BASE / 'runtime_isolation.py', BASE / 'harness/quicktest3_isolated.py',
          BASE / 'background_24/harness/quicktest3_isolated.py', BASE / 'background_24/run24.py',
          BASE / 'background_24/tools24.py', BASE / 'background_24/Plane242/primary_math_audit.json',
          BASE / 'background_24/Plane242/source_scene_snapshot.json',
          BASE / 'annotation_semantics_lessons_20261102.json']
paths += list((BRANCH / 'workbench').glob('*.py'))
paths += [p for p in (BASE / 'background_07/plane_worker/Plane242').rglob('*') if p.is_file()]
for d in ('Plane295_inner_ear_shoulder_correspondence', 'Plane342_quarterturn_wedge_edge_binding',
          'Plane233_two_U_partial_partition_binding'):
    p = BASE / 'independent_review' / d / 'independent_review.json'
    if p.is_file(): paths.append(p)
paths += list(BASE.glob('batch_*/manifest.json'))
before = inventory(paths)

from dataset_tools.catalog import content, digest
approved = read(ROOT / 'provenance/approvals.json')['approvals'][QID]
fingerprint = digest(content(ROOT, 'PlaneGeometry', record))
accept = [x for x in rows(BRANCH / 'special_variant/accepted_index.jsonl') if x.get('question_id',x.get('id')) == QID]
collect = [x for x in rows(BRANCH / 'special_variant/collected_index.jsonl') if x.get('question_id',x.get('id')) == QID]
special_dir = BRANCH / 'special_variant' / QID
special_files = {name:read(special_dir / name) if (special_dir / name).is_file() else None
                 for name in ('recipes.json','collection.json')}
batch_overlaps = [rel(p) for p in BASE.glob('batch_*/manifest.json') if QID in p.read_text(encoding='utf-8-sig')]
eligibility = {'checked_at_utc':now(), 'formal_record':record, 'approval':approved,
               'computed_current_content_sha256':fingerprint,
               'valid_current_user_approval':approved.get('reviewer') == 'user' and fingerprint == approved['content_sha256'],
               'accepted_index_matches':accept, 'collected_index_matches':collect,
               'question_special_records':special_files, 'published_batch_overlaps':batch_overlaps}
eligibility['eligible'] = (record['source_dataset'] == 'MathVision' and eligibility['valid_current_user_approval']
                          and not accept and not collect and not any(special_files.values()) and not batch_overlaps)

raw_request = (TEST / 'request.json').read_bytes()
request = json.loads(raw_request)
embedded = base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1], validate=True)
def px(p):
    with Image.open(p) as im:
        rgba = im.convert('RGBA')
        return sha(f'{im.width}x{im.height}:RGBA:'.encode() + rgba.tobytes())
request_summary = copy.deepcopy(request)
request_summary['messages'][1]['content'][1]['image_url']['url'] = '[PNG bytes independently decoded and hash checked]'
checks = {
    'candidate_bytes_equal_embedded_request':embedded == (CAND/'candidate.png').read_bytes(),
    'image_sha256_matches':fh(CAND/'candidate.png') == binding['image_sha256'],
    'pixel_sha256_matches':px(CAND/'candidate.png') == binding['pixel_sha256'],
    'design_sha256_matches':fh(CAND/'design.json') == binding['design_sha256'],
    'snapshot_byte_equal_design':(TEST/'design_snapshot.json').read_bytes() == (CAND/'design.json').read_bytes(),
    'request_body_sha256_matches':sha(raw_request) == binding['request_body_sha256'],
    'formal_question_exact':request['messages'][1]['content'][0]['text'] == record['question'] == binding['question'],
    'formal_record_sha256_matches':canon(record) == binding['question_record_sha256'],
    'current_dataset_sha256_matches':fh(BRANCH/'dataset.jsonl') == binding['dataset_sha256'],
    'quick_test_reference_sha256_matches':fh(BRANCH/'workbench/quick_test.py') == binding['reference_quick_test_sha256'],
    'preset_is_D_and_wrong':design['expected_wrong_answer'] == binding['expected_wrong_answer'] == 'D' != record['answer'],
    'exact_request_structure_no_extra_instructions':set(request) == {'model','stream','thinking','messages'}
        and len(request['messages']) == 2 and len(request['messages'][1]['content']) == 2,
    'quicktest3_model_disabled':request['model'] == 'mimo-v2.6-flash' and request['thinking'] == {'type':'disabled'},
    'no_token_limit_fields':not ({'max_tokens','max_completion_tokens'} & set(request)),
    'design_precedes_calls':design['created_at'] < binding['created_at'],
    'harness_copy_byte_equal':(BASE/'harness/quicktest3_isolated.py').read_bytes() == (BASE/'background_24/harness/quicktest3_isolated.py').read_bytes(),
}
run_details = []
for i in (1,2):
    stem = f'run_{i:02d}'
    start, run, raw = [read(TEST/(stem+s+'.json')) for s in ('_started','','_response')]
    final = raw['choices'][0]['message']['content']
    rchecks = {'response_hash':fh(TEST/(stem+'_response.json')) == run['response_sha256'],
               'complete_stop':run['status'] == 'completed' and run['finish_reason'] == raw['choices'][0]['finish_reason'] == 'stop' and not run['truncated'],
               'exact_complete_answer':final == run['answer'],
               'bindings_match':all(start[k] == run[k] == binding[k] for k in ('request_body_sha256','image_sha256','design_sha256')),
               'same_run_id':start['run_id'] == run['run_id'],
               'model_matches':raw['model'] == run['response_model'] == 'mimo-v2.6-flash',
               'no_reasoning_tokens':raw['usage']['completion_tokens_details']['reasoning_tokens'] == 0}
    run_details.append({'run_index':i,'record':run,'raw_response':raw,'complete_final_text':final,
                        'independently_read_terminal_answer':'D','checks':rchecks})
checks['exactly_two_completed_candidate_calls'] = (len(list((CAND/'tests').glob('*/binding.json'))) == 1
    and len(list((CAND/'tests').rglob('run_*_started.json'))) == 2
    and len(list((CAND/'tests').rglob('run_*_response.json'))) == 2
    and len(list((CAND/'tests').rglob('run_??.json'))) == 2
    and not list((CAND/'tests').rglob('*incomplete*')))

# Relevant frozen sources and dependencies, separate from all-library manifests.
hist_files = render_check['input_fingerprints']['files']
relevant_paths = [p for p in paths if p.is_relative_to(BRANCH) and
    (QID in str(p) or p.is_relative_to(BRANCH/'workbench') or
     p.name in ('protocol.json','common_renderer.py','runtime.py','protocol_renderer.py'))]
relevant_paths += [ROOT/'dataset_tools/geometry_dataset.py', ROOT/'dataset_tools/mathvision_workbench.py']
historical = {rel(p):{'recorded':hist_files.get(rel(p)), 'current':fh(p),
                    'matches':hist_files.get(rel(p)) == fh(p) if rel(p) in hist_files else None}
              for p in sorted(set(relevant_paths))}

# Read-only cross-history discovery. Only matching candidate hashes count as repeats.
bindings_found, controls = [], []
for p in BASE.rglob('binding.json'):
    if p.is_relative_to(HERE): continue
    b = read(p)
    if b.get('question_id') != QID: continue
    row = {'path':rel(p),'sha256':fh(p),'image_sha256':b.get('image_sha256'),
           'expected_wrong_answer':b.get('expected_wrong_answer'), 'requested_runs':b.get('requested_runs')}
    bindings_found.append(row)
    if b.get('image_sha256') == fh(BRANCH/record['image']): controls.append(row)

out = {'question_id':QID,'variant_id':VID,'checked_at_utc':now(),'pid':os.getpid(),
       'isolation':ISOLATION,'strict_own_directory_guard_before_project_imports':True,
       'network_and_child_process_blocked':True,'eligibility':eligibility,'binding':binding,
       'request_summary':request_summary,'checks':checks,'runs':run_details,
       'historical_relevant_source_comparisons':historical,'same_question_binding_inventory':bindings_found,
       'original_controls_found':controls,'frozen_artifacts_before':before}
write('evidence_audit.json',out)
print(json.dumps({'evidence_audit':str(HERE/'evidence_audit.json'),'eligible':eligibility['eligible'],
                  'checks':checks,'run_checks':[x['checks'] for x in run_details],
                  'source_mismatches':{k:v for k,v in historical.items() if v['matches'] is False},
                  'same_question_bindings':bindings_found,'controls':controls},ensure_ascii=False))
