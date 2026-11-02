import review_bootstrap as b
import base64
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from dataset_tools import catalog

ROOT, PROJECT = b.ROOT, b.PROJECT
BASE = PROJECT / 'runtime/mathvision_special_20261101'
UNIT = BASE / 'background_16'
QROOT = UNIT / 'Solid197'
CAND = QROOT / 'crease_side_binding'

def read(p):
    return json.loads(Path(p).read_text(encoding='utf-8-sig'))

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def hbytes(data):
    return hashlib.sha256(data).hexdigest()

def write(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def matching_nodes(value):
    found = []
    if isinstance(value, dict):
        if value.get('question_id', value.get('qid')) == 'Solid197':
            return [value]
        if 'Solid197' in value:
            found.append(value['Solid197'])
        for k, v in value.items():
            if k != 'Solid197':
                found.extend(matching_nodes(v))
    elif isinstance(value, list):
        for v in value:
            found.extend(matching_nodes(v))
    return found

record = next(r for r in catalog.rows(PROJECT / 'SolidGeometry/dataset.jsonl') if r['id'] == 'Solid197')
approval = read(PROJECT / 'provenance/approvals.json')['approvals']['Solid197']
current_content = catalog.content(PROJECT, 'SolidGeometry', record)
catalog.validate_formal_row(PROJECT, 'SolidGeometry', record)
special = PROJECT / 'SolidGeometry/special_variant'
elig_paths = [PROJECT / 'SolidGeometry/dataset.jsonl', PROJECT / 'provenance/approvals.json',
              PROJECT / 'provenance/source_notes.json']
elig = {'checked_at': datetime.now(timezone.utc).isoformat(), 'formal_record': record,
        'record_sha256': catalog.digest(record), 'approval': approval,
        'current_content_sha256': catalog.digest(current_content),
        'approval_matches_current_content': catalog.digest(current_content) == approval['content_sha256'],
        'source_notes': current_content['source_notes']}
for name in ['accepted_index.jsonl', 'collected_index.jsonl']:
    p = special / name
    elig_paths.append(p)
    elig[name] = [r for r in catalog.rows(p) if r.get('question_id', r.get('id')) == 'Solid197'] if p.exists() else []
for name in ['recipes.json', 'collection.json']:
    p = special / 'Solid197' / name
    elig_paths.append(p)
    elig[name] = read(p) if p.exists() else None
elig['special_question_directory_exists'] = (special / 'Solid197').exists()
elig['authoritative_hashes'] = {p.relative_to(PROJECT).as_posix(): sha(p) if p.exists() else None for p in elig_paths}
elig['formal_MathVision'] = record['source_dataset'] == 'MathVision'
elig['noPass'] = not elig['accepted_index.jsonl'] and elig['recipes.json'] is None
elig['notCollected'] = not elig['collected_index.jsonl']
elig['noSpecialCompletion'] = elig['collection.json'] is None
elig['eligible'] = all(elig[k] for k in ['formal_MathVision', 'noPass', 'notCollected', 'noSpecialCompletion', 'approval_matches_current_content'])

fp = read(QROOT / 'input_fingerprints.json')
frozen = {p: {'expected': expected, 'actual': sha(PROJECT / p)} for p, expected in fp['files'].items()}
frozen_mismatches = {p: x for p, x in frozen.items() if x['expected'] != x['actual']}
selected = {}
for name in ['primary_math_proofs.json', 'source_preservation_final.json', 'second_review_queue.json',
             'evidence_manifest.json', 'evidence_binding_audit.json', 'scope_audit.json', 'final_verification.json']:
    p = UNIT / name
    data = read(p)
    selected[name] = {'sha256': sha(p), 'root_keys': list(data) if isinstance(data, dict) else None,
                      'Solid197': matching_nodes(data)}
for name in ['exploration_report.json', 'remaining_questions.jsonl']:
    p = BASE / name
    data = catalog.rows(p) if p.suffix == '.jsonl' else read(p)
    selected[name] = {'diagnostic_only': True, 'sha256': sha(p), 'Solid197': matching_nodes(data)}
write(ROOT / 'selected_primary_and_history.json', selected)

evidence = {}
for kind in ['crease_side_binding', 'control_original']:
    parent = QROOT / kind
    dirs = sorted(p for p in (parent / 'tests').iterdir() if p.is_dir())
    entries = []
    for d in dirs:
        binding = read(d / 'binding.json')
        request = read(d / 'request.json')
        request_full_sha = sha(d / 'request.json')
        url = request['messages'][1]['content'][1]['image_url']['url']
        image_data = base64.b64decode(url.split(',', 1)[1], validate=True)
        sanitized = copy.deepcopy(request)
        sanitized['messages'][1]['content'][1]['image_url']['url'] = '<PNG bytes, sha256=' + hbytes(image_data) + '>'
        runs = []
        for p in sorted(d.glob('run_[0-9][0-9].json')):
            run = read(p)
            stem = p.stem
            rawpath = d / (stem + '_response.json')
            raw = read(rawpath)
            started = read(d / (stem + '_started.json'))
            body = raw['choices'][0]['message']['content']
            checks = {
                'raw_sha_matches_job': sha(rawpath) == run['response_sha256'],
                'raw_full_body_equals_record': body == run['answer'],
                'same_request': run['request_body_sha256'] == request_full_sha == binding['request_body_sha256'],
                'same_image': run['image_sha256'] == binding['image_sha256'] == hbytes(image_data) == sha(parent / 'candidate.png'),
                'same_design': run['design_sha256'] == binding['design_sha256'] == sha(parent / 'design.json') == sha(d / 'design_snapshot.json'),
                'start_record_matches': all(run[k] == v for k, v in started.items()),
                'complete': run['status'] == 'completed' and run['http_status'] == 200 and not run['truncated'] and raw['choices'][0]['finish_reason'] == 'stop',
                'correct_profile': raw['model'] == run['response_model'] == request['model'] == 'mimo-v2.6-flash' and request['thinking'] == {'type': 'disabled'},
                'no_hidden_reasoning': run['thinking'] == '' and raw['usage']['completion_tokens_details']['reasoning_tokens'] == 0,
                'preset_before_call': read(parent / 'design.json')['created_at'] < binding['created_at'] < run['started_at'],
            }
            assert all(checks.values()), (kind, stem, checks)
            runs.append({'record': run, 'raw_response': raw, 'checks': checks,
                         'raw_sha256': sha(rawpath), 'run_sha256': sha(p),
                         'started_sha256': sha(d / (stem + '_started.json')),
                         'complete_body_sha256': hbytes(body.encode('utf-8')),
                         'raw_path': str(rawpath), 'run_path': str(p)})
        checks = {'exactly_two_runs': len(runs) == 2, 'one_test_directory': len(dirs) == 1,
                  'no_failed_artifacts': not list(d.glob('*incomplete*')) and all(r['checks']['complete'] for r in runs),
                  'payload_keys_only_model_stream_thinking_messages': set(request) == {'model', 'stream', 'thinking', 'messages'},
                  'only_system_and_user_roles': [m['role'] for m in request['messages']] == ['system', 'user'],
                  'only_question_and_one_png_in_user_content': [x['type'] for x in request['messages'][1]['content']] == ['text', 'image_url'],
                  'question_exact_formal': request['messages'][1]['content'][0]['text'] == record['question'] == binding['question'],
                  'formal_record_binding': binding['question_record_sha256'] == catalog.digest(record),
                  'dataset_binding': binding['dataset_sha256'] == sha(PROJECT / 'SolidGeometry/dataset.jsonl'),
                  'request_sha_matches_binding': binding['request_body_sha256'] == request_full_sha,
                  'design_snapshot_exact_bytes': (parent / 'design.json').read_bytes() == (d / 'design_snapshot.json').read_bytes(),
                  'profile_thinking_disabled': request['thinking'] == {'type': 'disabled'},
                  'preset_450': binding['expected_wrong_answer'] == read(d / 'design_snapshot.json')['expected_wrong_answer'] == '450'}
        assert all(checks.values()), (kind, checks)
        entries.append({'directory': str(d), 'binding': binding, 'request_sanitized': sanitized,
                        'binding_sha256': sha(d / 'binding.json'), 'request_sha256': request_full_sha,
                        'design_snapshot_sha256': sha(d / 'design_snapshot.json'),
                        'embedded_png_sha256': hbytes(image_data), 'checks': checks, 'runs': runs})
    evidence[kind] = entries

protected = {p: sha(p) for p in QROOT.rglob('*') if p.is_file()}
for p in [PROJECT / x for x in fp['files']] + [UNIT / x for x in selected if (UNIT / x).exists()]:
    protected[p] = sha(p)
protected.update({p: sha(p) for p in [UNIT/'quicktest3_isolated.py', PROJECT/'SolidGeometry/workbench/quick_test.py',
                                   BASE/'Solid197_firstpass_independent_review_brief.txt', BASE/'Solid197_pre_review_evidence_check.json']})
result = {'isolation': b.ISOLATION, 'current_eligibility': elig, 'frozen_inputs': frozen,
          'frozen_input_mismatches': frozen_mismatches, 'record_matches_snapshot': record == read(QROOT/'formal_record.json'),
          'evidence': evidence, 'read_only_baseline': {str(p): v for p,v in protected.items()},
          'harness_sha256': sha(UNIT/'quicktest3_isolated.py'), 'profile_source_sha256': sha(PROJECT/'SolidGeometry/workbench/quick_test.py')}
write(ROOT/'audit_bindings.json', result)
print(json.dumps({'isolation': b.ISOLATION, 'eligibility': elig, 'frozen_mismatches': frozen_mismatches,
                  'evidence_checks': {k:[{'checks':x['checks'],'runs':[r['checks'] for r in x['runs']]} for x in v] for k,v in evidence.items()},
                  'selected_primary_and_history': selected}, ensure_ascii=False, indent=2))
