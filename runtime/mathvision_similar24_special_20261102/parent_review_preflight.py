"""Finite read-only frozen-evidence checks; output only in this case runtime."""
import base64
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

spec = importlib.util.spec_from_file_location('readonly_publish_evidence', HERE/'publish_batch.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
rows = []
units = ['u01_fold_locations', 'u04_angles', 'u09_octa_nets']
for unit in units:
    entries = read(HERE/'units'/unit/'second_review_queue.json')
    assert len(entries) == 1
    entry = entries[0]
    source = Path(entry['candidate_directory'])
    assert source.is_relative_to(HERE)
    summary, record, summary_path = helper.verify_evidence(source)
    evidence = summary_path.parent
    assert summary['requested_runs'] == len(summary['results']) == 2
    assert sha(source/'design.json') == sha(evidence/'design_snapshot.json') == summary['design_sha256'] == entry['design_sha256']
    assert sha(source/'plugin.json') == entry['plugin_sha256']
    assert sha(source/'candidate.png') == summary['image_sha256'] == entry['image_sha256']
    request = read(evidence/'request.json')
    assert request['model'] == 'mimo-v2.6-flash'
    assert request['thinking'] == {'type': 'disabled'}
    assert 'max_tokens' not in request
    assert summary['profile'] == 'quicktest3'
    assert len(request['messages']) == 2
    assert request['messages'][0] == {'role':'system', 'content':summary['system_prompt']}
    assert request['messages'][1]['role'] == 'user'
    assert summary['request_body_sha256'] == sha(evidence/'request.json')
    assert record['source_dataset'] == 'MathVision'
    assert summary['question'] == record['question']
    assert datetime.fromisoformat(read(source/'design.json')['created_at']) < datetime.fromisoformat(summary['results'][0]['started_at'])
    runs = []
    for index, result in enumerate(summary['results'], 1):
        raw_path = evidence/f'run_{index:02d}_response.json'
        raw = read(raw_path)
        choice = raw['choices'][0]
        assert choice['finish_reason'] == result['finish_reason'] == 'stop'
        assert choice['message']['content'] == result['answer']
        assert result['request_body_sha256'] == summary['request_body_sha256']
        assert result['response_model'] == raw['model'] == request['model']
        runs.append({'run_index':index, 'raw_path':str(raw_path), 'raw_sha256':sha(raw_path), 'finish_reason':choice['finish_reason'], 'complete_content_equals_summary':True})
    rows.append({'question_id':record['id'], 'unit':unit, 'candidate_directory':str(source), 'variant_id':source.name,
                 'candidate_sha256':sha(source/'candidate.png'), 'plugin_sha256':sha(source/'plugin.json'),
                 'design_sha256':sha(source/'design.json'), 'summary_path':str(summary_path), 'summary_sha256':sha(summary_path),
                 'expected_wrong_answer':summary['expected_wrong_answer'], 'correct_formal_answer':record['answer'],
                 'requested_runs':2, 'complete_frozen_bound_calls':2, 'raw_runs':runs,
                 'status':'EVIDENCE_PREFLIGHT_ONLY; NEW independent semantic/math review still required'})
out = {'created_at_utc':datetime.now(timezone.utc).isoformat(), 'solver_calls':0,
       'review_gate':'This program verifies integrity only; no human-semantic approval or qualification.', 'candidates':rows}
destination = HERE/'parent_review_preflight.json'
destination.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'output':str(destination), 'candidates':[r['question_id'] for r in rows], 'solver_calls':0}, ensure_ascii=False))
