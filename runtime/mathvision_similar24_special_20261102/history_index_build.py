"""Read-only index of old candidate/test history; no model or rendering calls."""
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime, timezone
import base64
import hashlib
import json
import os
import re
import sys
import zipfile

sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / 'runtime/mathvision_special_20261101'
MATCH = ROOT / 'runtime/mathvision_similar9_20261102/uncollected_matches.json'
OUT = HERE / 'history_index.json'
assert not OUT.exists(), 'Never replace an existing history index.'


def guard(event, args):
    def allowed(path):
        if path is None or isinstance(path, int):
            return
        assert Path(os.fsdecode(path)).resolve() == OUT, 'Read-only history scan: ' + str(path)
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        allowed(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        allowed(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        allowed(args[0]); allowed(args[1])


sys.addaudithook(guard)


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(262144), b''):
            h.update(block)
    return h.hexdigest()


def relative(path):
    return Path(path).relative_to(ROOT).as_posix()


parse_errors = []
hashes = {}


def read(path):
    raw = Path(path).read_bytes()
    hashes[relative(path)] = sha_bytes(raw)
    try:
        return json.loads(raw.decode('utf-8-sig'))
    except Exception as exc:
        parse_errors.append({'path': relative(path), 'error_type': type(exc).__name__, 'error': str(exc)[:250]})
        return None


scope = read(MATCH)['candidate_ids']
SCOPE = set(scope)
REFS = {'Plane217', 'Plane233', 'Plane308', 'Plane427', 'Solid126', 'Solid142', 'Solid167', 'Solid176', 'Solid203'}
all_files = [p for p in OLD.rglob('*') if p.is_file()]
question_re = re.compile(r'^(?:Plane|Solid)\d+$')
formal = {}
for branch in ('PlaneGeometry', 'SolidGeometry'):
    p = ROOT / branch / 'dataset.jsonl'
    raw = p.read_bytes(); hashes[relative(p)] = sha_bytes(raw)
    for line in raw.decode('utf-8-sig').splitlines():
        if line.strip():
            record = json.loads(line)
            if record.get('source_dataset') == 'MathVision':
                formal[record['id']] = {'branch': branch, 'record': record}


def question_of(path, data=None):
    if isinstance(data, dict):
        for key in ('question_id', 'qid'):
            q = data.get(key)
            if isinstance(q, str) and question_re.fullmatch(q):
                return q
    for component in reversed(Path(path).parts):
        if question_re.fullmatch(component):
            return component
    return None


# Unique actual invocations are identified by immutable run_id. Path aliases, ZIP
# copies, and delivered copies must never inflate the number of genuine calls.
transports = {}
request_image_hashes = defaultdict(list)
summary_objects = {}


def absorb_transport(data, label, container=None):
    if not isinstance(data, dict) or not data.get('image_sha256'):
        return
    q = data.get('question_id')
    image = data['image_sha256']
    if not isinstance(q, str) or q not in formal:
        return
    key = (q, image, data.get('request_body_sha256', 'UNKNOWN'))
    group = transports.setdefault(key, {'question_id': q, 'image_sha256': image,
                                       'request_body_sha256': key[2], 'aliases': [], 'runs': {},
                                       'expected_wrong_answers': [], 'source_design_sha256': []})
    group['aliases'].append(label)
    expected = data.get('expected_wrong_answer')
    if expected is not None and expected not in group['expected_wrong_answers']:
        group['expected_wrong_answers'].append(expected)
    dsha = data.get('design_sha256')
    if dsha and dsha not in group['source_design_sha256']:
        group['source_design_sha256'].append(dsha)
    for index, run in enumerate(data.get('results', []), 1):
        run_key = run.get('run_id') or f"{data.get('created_at')}:{run.get('started_at')}:{index}"
        old = group['runs'].get(run_key, {})
        compact = {k: run.get(k) for k in ('run_id', 'run_index', 'status', 'http_status', 'truncated',
                                         'finish_reason', 'response_sha256', 'image_sha256',
                                         'design_sha256', 'request_body_sha256', 'started_at',
                                         'finished_at', 'error_type', 'error', 'elapsed_seconds') if k in run}
        answer = run.get('answer')
        if isinstance(answer, str):
            compact['complete_answer_text_path'] = label + '#/results/' + str(index - 1) + '/answer'
            compact['answer_ending_700_chars'] = answer[-700:]
        if container is not None:
            response = container / f'run_{index:02d}_response.json'
            compact['raw_response_path'] = relative(response) if response.exists() else None
            if response.exists():
                compact['raw_response_sha256'] = sha(response)
                compact['raw_response_sha_matches_summary'] = compact['raw_response_sha256'] == run.get('response_sha256')
                hashes[relative(response)] = compact['raw_response_sha256']
        group['runs'][run_key] = {**old, **compact}
    if container is not None:
        for started in container.glob('run_*_started.json'):
            d = read(started)
            if not isinstance(d, dict):
                continue
            run_key = d.get('run_id') or f"{data.get('created_at')}:{d.get('started_at')}:{d.get('run_index')}"
            if run_key not in group['runs']:
                group['runs'][run_key] = {'run_id': d.get('run_id'), 'run_index': d.get('run_index'),
                                         'status': 'started_without_complete_summary_record',
                                         'started_path': relative(started), 'started_at': d.get('started_at')}


for path in all_files:
    if path.name not in ('summary.json', 'binding.json'):
        continue
    data = read(path)
    if isinstance(data, dict) and data.get('question_id') in formal and data.get('image_sha256'):
        absorb_transport(data, relative(path), path.parent)
        if path.name == 'summary.json':
            summary_objects[relative(path)] = {'question_id': data['question_id'],
                                             'image_sha256': data['image_sha256'],
                                             'two_completed': data.get('two_completed'),
                                             'requested_runs': data.get('requested_runs')}
    del data

# Decode only the embedded image, never store or print a request body/base64.
request_count = 0
question_text_to_id = defaultdict(list)
for q, item in formal.items():
    question_text_to_id[item['record']['question']].append(q)
for path in all_files:
    if path.name != 'request.json':
        continue
    data = read(path)
    if not isinstance(data, dict):
        continue
    messages = data.get('messages', [])
    for message in messages:
        content = message.get('content') if isinstance(message, dict) else None
        if not isinstance(content, list):
            continue
        texts = [v.get('text') for v in content if isinstance(v, dict) and v.get('type') == 'text']
        qs = question_text_to_id.get(texts[0], []) if texts else []
        for part in content:
            if not isinstance(part, dict) or part.get('type') != 'image_url':
                continue
            value = part.get('image_url', {})
            url = value.get('url', '') if isinstance(value, dict) else ''
            if not url.startswith('data:image/') or ',' not in url:
                continue
            try:
                image = base64.b64decode(url.split(',', 1)[1], validate=True)
                digest = sha_bytes(image)
                request_image_hashes[digest].append({'request_path': relative(path), 'question_ids_by_exact_formal_text': qs,
                                                      'question_id_by_path': question_of(path),
                                                      'request_file_sha256': hashes[relative(path)]})
                request_count += 1
                del image
            except Exception as exc:
                parse_errors.append({'path': relative(path), 'error_type': type(exc).__name__, 'error': str(exc)[:250]})
    del data

# ZIP tests are aliases of originals in normal delivery packages, but are scanned
# explicitly so an otherwise hidden matching image/preset is never overlooked.
zip_count = 0
for zpath in sorted(OLD.glob('batch_[0-9][0-9].zip')):
    hashes[relative(zpath)] = sha(zpath)
    with zipfile.ZipFile(zpath) as archive:
        zip_count += 1
        for name in archive.namelist():
            if Path(name).name not in ('summary.json', 'binding.json'):
                continue
            try:
                data = json.loads(archive.read(name).decode('utf-8-sig'))
                absorb_transport(data, relative(zpath) + '::' + name)
            except Exception as exc:
                parse_errors.append({'path': relative(zpath) + '::' + name, 'error_type': type(exc).__name__, 'error': str(exc)[:250]})

for group in transports.values():
    runs = list(group['runs'].values())
    group['runs'] = runs
    group['actual_unique_started_run_count'] = len(runs)
    group['unique_complete_run_count'] = sum(r.get('status') == 'completed' and r.get('http_status') == 200 and not r.get('truncated') for r in runs)
    group['failed_aborted_or_unknown_count'] = len(runs) - group['unique_complete_run_count']
    group['all_request_aliases'] = request_image_hashes.get(group['image_sha256'], [])

transport_by_hash = defaultdict(list)
for group in transports.values():
    transport_by_hash[group['image_sha256']].append(group)

candidate_pngs = defaultdict(list)
for path in all_files:
    if path.name != 'candidate.png':
        continue
    q = question_of(path)
    if q:
        digest = sha(path)
        candidate_pngs[digest].append({'question_id': q, 'path': relative(path)})

formal_pngs = defaultdict(list)
for q, item in formal.items():
    image_path = ROOT / item['branch'] / item['record']['image']
    digest = sha(image_path)
    formal_pngs[digest].append({'question_id': q, 'path': relative(image_path)})
    if q in SCOPE | REFS:
        hashes[relative(image_path)] = digest

design_paths = [p for p in all_files if p.name == 'design.json']
scoped_paths = {q: [] for q in scope}
for path in all_files:
    q = question_of(path)
    if q in SCOPE and path.suffix.lower() in ('.json', '.jsonl', '.txt', '.log', '.py'):
        scoped_paths[q].append(relative(path))


def manual_final_fields(data):
    found = []
    def walk(value, pointer=''):
        if isinstance(value, dict):
            for key, child in value.items():
                loc = pointer + '/' + str(key)
                if re.search(r'final|manual|observed|outcome|preset|primary_twohit|two_hit|twohit', str(key), re.I):
                    if child is None or isinstance(child, (str, int, float, bool)):
                        found.append({'json_pointer': loc, 'value': child[:1000] if isinstance(child, str) else child})
                    elif isinstance(child, list) and len(child) <= 10 and all(v is None or isinstance(v, (str, int, float, bool)) for v in child):
                        found.append({'json_pointer': loc, 'value': [v[:1000] if isinstance(v, str) else v for v in child]})
                if isinstance(child, (dict, list)):
                    walk(child, loc)
        elif isinstance(value, list):
            for i, child in enumerate(value):
                if isinstance(child, (dict, list)):
                    walk(child, pointer + '/' + str(i))
    walk(data)
    return found


questions = []
for q in scope:
    designs = []
    for path in design_paths:
        if question_of(path) != q:
            continue
        d = read(path)
        if not isinstance(d, dict):
            continue
        folder = path.parent
        image = folder / 'candidate.png'
        image_sha = sha(image) if image.exists() else d.get('png_sha256', d.get('image_sha256'))
        plugin = folder / 'plugin.json'
        if image.exists(): hashes[relative(image)] = image_sha
        if plugin.exists(): hashes[relative(plugin)] = sha(plugin)
        groups = transport_by_hash.get(image_sha, [])
        own = [g for g in groups if g['question_id'] == q]
        calls = sum(g['actual_unique_started_run_count'] for g in own)
        complete = sum(g['unique_complete_run_count'] for g in own)
        failed = sum(g['failed_aborted_or_unknown_count'] for g in own)
        rows = {'directory': relative(folder), 'design_path': relative(path), 'design_sha256': hashes[relative(path)],
                'variant_id': d.get('variant_id') or folder.name,
                'original_created_at': d.get('created_at', d.get('created_at_utc')),
                'predeclared_wrong_answer': d.get('expected_wrong_answer', d.get('predicted_wrong_answer')),
                'correct_answer_in_design': d.get('correct_answer'),
                'mechanism': d.get('mechanism', d.get('intent')),
                'frozen_candidate_png_path': relative(image) if image.exists() else None,
                'frozen_candidate_png_sha256': image_sha,
                'plugin_path': relative(plugin) if plugin.exists() else None,
                'candidate_hash_aliases': candidate_pngs.get(image_sha, []),
                'all_matching_transport_records': own,
                'unique_started_call_count_from_saved_records': calls,
                'unique_complete_call_count_from_saved_records': complete,
                'failed_aborted_or_unknown_call_count': failed,
                'zero_saved_actual_call_evidence': calls == 0,
                'cross_question_transport_matches': [g for g in groups if g['question_id'] != q],
                'matching_embedded_requests': request_image_hashes.get(image_sha, []),
                'do_not_retest_this_frozen_png': calls > 0 or bool(request_image_hashes.get(image_sha)),
                'manual_and_primary_review_records': []}
        for candidate in folder.rglob('*.json'):
            if candidate.name in ('design.json', 'design_snapshot.json', 'request.json', 'binding.json', 'summary.json', 'plugin.json', 'plugin_submitted.json'):
                continue
            if not re.search(r'review|final|audit|result|outcome|checkpoint', candidate.name, re.I):
                continue
            if candidate.stat().st_size > 3_000_000:
                continue
            value = read(candidate)
            if value is None:
                continue
            extracted = manual_final_fields(value)
            if extracted:
                rows['manual_and_primary_review_records'].append({'path': relative(candidate), 'fields': extracted})
        designs.append(rows)
    proofs = []
    reviews = []
    for path in all_files:
        name = path.name
        path_text = relative(path)
        if q not in path_text or path.suffix.lower() != '.json':
            continue
        if name == 'independent_review.json' or ('independent_review' in path.parts and re.search(r'review|verdict|objection', name)):
            d = read(path)
            if isinstance(d, dict):
                reviews.append({'path': path_text, 'decision': d.get('decision', d.get('verdict')),
                                'variant_id': d.get('variant_id', d.get('candidate_id')),
                                'objections_or_issues': {k: d[k] for k in ('issues', 'blocking_objections', 'objections', 'reason', 'summary', 'limitations') if k in d}})
        elif re.search(r'math|proof|primary.*review|manual.*final|full.*final', name, re.I):
            proofs.append(path_text)
    f = formal[q]
    formal_path = ROOT / f['branch'] / f['record']['image']
    image_sha = sha(formal_path)
    q_transports = [g for g in transports.values() if g['question_id'] == q]
    questions.append({'question_id': q, 'branch': f['branch'], 'formal_correct_answer': f['record']['answer'],
                      'formal_png_sha256': image_sha, 'formal_identical_image_questions': formal_pngs[image_sha],
                      'formal_original_png_prior_transport_records': transport_by_hash.get(image_sha, []),
                      'candidate_design_count': len(designs), 'designs': designs,
                      'all_saved_transport_groups_for_question': q_transports,
                      'independent_review_references': reviews,
                      'additional_math_manual_history_references': sorted(set(proofs)),
                      'other_scoped_history_file_references': scoped_paths[q],
                      'no_tested_design_found': not any(g['actual_unique_started_run_count'] for g in q_transports)})

# Freeze everything actually parsed/used without modifying historical snapshots.
source_drift = [path for path, old_hash in hashes.items() if sha(ROOT / path) != old_hash]
assert not source_drift, 'Historical sources changed during read-only scan: ' + str(source_drift[:5])
report = {
    'created_at_utc': datetime.now(timezone.utc).isoformat(),
    'task': 'Old-history index for new user-reference-derived 24-question Special task',
    'scope_question_ids': scope,
    'new_model_API_calls': 0, 'new_designs': 0, 'approvals_or_Pass_Collect_changes': 0,
    'scan': {'old_root': relative(OLD), 'source_file_count': len(all_files),
             'transport_group_count_all_questions': len(transports),
             'embedded_request_images_decoded_without_storing_base64': request_count,
             'delivered_ZIP_archives_scanned': zip_count, 'tracked_readonly_files': len(hashes),
             'tracked_file_hashes_unchanged': True,
             'saved_history_only_not_provider_account_audit': True},
    'rules': [
        'Existing saved starts count as actual request evidence even if response/summary is incomplete.',
        'Never retest a tested, failed, aborted, truncated or unknown-transport frozen image; preserve its original preset and results.',
        'Do not infer exact zero historical calls merely from missing design or candidate-local tests: review all matching transport groups and malformed-record warnings.',
        'Image-equal questions may have different formal questions/choices; do not transplant final-answer evidence across question IDs.',
        'Formal-image twins Plane213/Plane233 and Plane364/Plane423 are explicitly recorded. The latter have different choices.',
        'Counts deduplicate immutable run_id across source copies, delivery trees and ZIP aliases.',
        'Stored manual final fields are references to old authors judgments, not new independent review approvals.',
    ],
    'questions': questions,
    'cross_id_candidate_hash_collisions_involving_scope': [
        {'image_sha256': digest, 'candidate_aliases': aliases,
         'transport_records': transport_by_hash.get(digest, [])}
        for digest, aliases in candidate_pngs.items()
        if len({a['question_id'] for a in aliases}) > 1 and any(a['question_id'] in SCOPE for a in aliases)
    ],
    'parse_errors_preserved_not_repaired': parse_errors,
    'tracked_readonly_source_sha256': hashes,
}
with OUT.open('x', encoding='utf-8', newline='\n') as stream:
    json.dump(report, stream, ensure_ascii=False, indent=2, allow_nan=False)
    stream.write('\n')
print(json.dumps({'output': str(OUT), 'question_count': len(questions),
                  'design_count': sum(q['candidate_design_count'] for q in questions),
                  'unique_transport_groups': len(transports), 'parse_errors': len(parse_errors),
                  'read_only_files': len(hashes), 'new_API_calls': 0}, ensure_ascii=False))
