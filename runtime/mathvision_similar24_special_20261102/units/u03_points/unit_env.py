"""Unit-local isolation; no library edits and no writes outside this unit."""
from pathlib import Path
import os
import sys

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[3]
TASK = OWN.parents[1]
OLD = PROJECT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
for name, folder in {'TEMP':'ownruntime/tmp', 'TMP':'ownruntime/tmp',
                     'MPLCONFIGDIR':'ownruntime/mpl', 'XDG_CACHE_HOME':'ownruntime/cache'}.items():
    path = OWN / folder
    path.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(path)

def checked(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('u03 writeguard: outside own_root: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            checked(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        checked(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        checked(args[0]); checked(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(OLD))
import runtime_isolation
ISOLATION = runtime_isolation.install(OWN / 'ownruntime/scene_temp')
sys.path.insert(0, str(PROJECT / 'PlaneGeometry/workbench'))

import hashlib
import json
from datetime import datetime, timezone

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path, value, *, replace=False):
    path = Path(path)
    checked(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w' if replace else 'x', encoding='utf-8', newline='\n') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')

ASSIGNMENT = read(OWN / 'assignment.json')
QIDS = ASSIGNMENT['question_ids']

def eligibility(qid):
    from dataset_tools import catalog
    branch = PROJECT / 'PlaneGeometry'
    row = next(r for r in catalog.rows(branch / 'dataset.jsonl') if r['id'] == qid)
    approval = catalog.read(PROJECT / 'provenance/approvals.json')['approvals'][qid]
    content = catalog.content(PROJECT, 'PlaneGeometry', row)
    fingerprint = catalog.digest(content)
    original = next(q for q in ASSIGNMENT['questions'] if q['question_id'] == qid)
    frozen = original['frozen_source_files_sha256']
    hashes = {p: sha((PROJECT / p).read_bytes()) for p in frozen}
    differences = {p: {'expected': frozen[p], 'actual': v} for p,v in hashes.items() if frozen[p] != v}
    special = branch / 'special_variant'
    accepted = [r for r in catalog.rows(special / 'accepted_index.jsonl') if r.get('question_id',r.get('id')) == qid]
    collected = [r for r in catalog.rows(special / 'collected_index.jsonl') if r.get('question_id',r.get('id')) == qid]
    recipe_path = special / qid / 'recipes.json'
    collection_path = special / qid / 'collection.json'
    recipe = read(recipe_path) if recipe_path.exists() else None
    collection = read(collection_path) if collection_path.exists() else None
    eligible = (row == original['formal_record'] and row['source_dataset'] == 'MathVision'
                and fingerprint == approval['content_sha256'] == original['current_content_sha256']
                and approval['reviewer'] == 'user' and not differences and not accepted and not collected
                and not recipe and not collection)
    return {'question_id':qid, 'checked_at':now(), 'eligible':eligible,
            'record':row, 'approval':approval, 'current_content_sha256':fingerprint,
            'content':content, 'frozen_source_sha256':hashes, 'frozen_source_differences':differences,
            'accepted_entries':accepted, 'collected_entries':collected, 'recipes':recipe, 'collection':collection}

def adapter_context(qid):
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    config = load_config(PROJECT / 'PlaneGeometry/workbench/config.json')
    adapter = RendererAdapter(config)
    metadata = adapter.inspect_question(qid)
    return config, adapter, metadata
