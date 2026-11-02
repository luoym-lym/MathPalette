"""Own-process environment and own-root write isolation; no remote settings."""
from pathlib import Path
import os
import sys

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
BASE = OWN.parent
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, folder in {'TEMP':'tmp', 'TMP':'tmp', 'MPLCONFIGDIR':'mpl_cache', 'XDG_CACHE_HOME':'cache'}.items():
    directory = OWN / folder
    directory.mkdir(exist_ok=True)
    os.environ[key] = str(directory)

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('background_70 write outside own directory: ' + str(resolved))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check_write(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check_write(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check_write(args[0])
        check_write(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(PROJECT / 'PlaneGeometry/workbench'))

import json
import hashlib
from datetime import datetime, timezone

QIDS = ('Plane186', 'Plane269', 'Plane273', 'Plane275', 'Plane314', 'Plane326', 'Plane378', 'Plane394')
RELATED = ('Plane258', 'Plane412', 'Plane436')

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path, value, *, replace=False):
    p = Path(path)
    if not p.is_absolute():
        p = OWN / p
    check_write(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w' if replace else 'x', encoding='utf-8', newline='\n') as out:
        json.dump(value, out, ensure_ascii=False, indent=2, allow_nan=False)
        out.write('\n')

def row(qid):
    with (PROJECT/'PlaneGeometry/dataset.jsonl').open(encoding='utf-8-sig') as stream:
        for line in stream:
            val = json.loads(line)
            if val['id'] == qid:
                return val
    raise KeyError(qid)

def eligibility(qid):
    assert qid in QIDS
    from dataset_tools import catalog
    rec = row(qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'].get(qid, {})
    fingerprint = catalog.digest(catalog.content(PROJECT, 'PlaneGeometry', rec))
    matches = {}
    files = ['PlaneGeometry/dataset.jsonl', 'provenance/approvals.json', 'provenance/source_notes.json']
    for name in ('accepted_index.jsonl', 'collected_index.jsonl'):
        p = PROJECT/'PlaneGeometry/special_variant'/name
        files.append(str(p.relative_to(PROJECT)))
        matches[name] = [r for r in catalog.rows(p) if r.get('question_id', r.get('id')) == qid]
    specials = {}
    for name in ('recipes.json', 'collection.json'):
        p = PROJECT/'PlaneGeometry/special_variant'/qid/name
        specials[name] = {'exists':p.exists(), 'sha256':sha(p) if p.exists() else None}
    delivered = []
    for p in sorted(BASE.glob('batch_*/manifest.json')):
        data = read(p)
        if qid in json.dumps(data, ensure_ascii=False):
            delivered.append(str(p))
        del data
    reasons = []
    if rec.get('source_dataset') != 'MathVision': reasons.append('source not MathVision')
    if approval.get('reviewer') != 'user' or not approval.get('instruction') or fingerprint != approval.get('content_sha256'):
        reasons.append('current original approval mismatch')
    if any(matches.values()) or any(v['exists'] for v in specials.values()): reasons.append('Special state present')
    if delivered: reasons.append('already delivered')
    return {'checked_at':now(), 'question_id':qid, 'eligible':not reasons, 'reasons':reasons,
            'formal_record':rec, 'approval':approval, 'current_content_sha256':fingerprint,
            'original_approval_fingerprint_matches':fingerprint == approval.get('content_sha256'),
            'matched_special_rows':matches, 'special_files':specials, 'delivered_references':delivered,
            'authoritative_hashes':{p:sha(PROJECT/p) for p in files}}
