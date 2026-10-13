"""Build or verify the formal catalog. Never infer user approval from rendering."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
import tempfile
import time
from pathlib import Path

if __package__:
    from .answer_schema import validate_answer
else:
    from answer_schema import validate_answer

ROOT = Path(__file__).resolve().parents[1]
BRANCHES = ('Analytics', 'PlaneGeometry', 'SolidGeometry')
PATH_FIELDS = ('image', 'original_image', 'script', 'scene')
COMMON_SCENE_FIELDS = {'scene_schema_version', 'protocol_version', 'id', 'status',
    'source_dataset', 'source_image', 'view', 'points', 'objects', 'labels', 'constraints', 'ambiguities'}
FORMAL_SCENE_FIELDS = {
    'PlaneGeometry': COMMON_SCENE_FIELDS | {'distance_markers'},
    'SolidGeometry': COMMON_SCENE_FIELDS | {'subject', 'source_note', 'world_unit',
                                         'projection', 'visibility', 'dimensions'},
}

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()]

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def contained(root, relative):
    root = Path(root).resolve()
    target = (root/relative).resolve()
    if not target.is_relative_to(root) or target == root:
        raise ValueError(f'Invalid data path: {relative}')
    return target

def validate_formal_row(root, branch, row):
    validate_answer(row)
    if not isinstance(row.get('source_dataset'), str) or not row['source_dataset'].strip():
        raise ValueError(f"{row['id']}: a source dataset name is required")
    if branch in FORMAL_SCENE_FIELDS:
        if not row.get('scene'):
            raise ValueError(f"{row['id']}: a frozen geometry scene is required")
        scene = read(contained(Path(root)/branch, row['scene']))
        if set(scene) != FORMAL_SCENE_FIELDS[branch]:
            raise ValueError(f"{row['id']}: scene fields do not match the formal drawing schema")
        if scene['id'] != row['id'] or scene['source_dataset'] != row['source_dataset']:
            raise ValueError(f"{row['id']}: scene identity/source differs from the formal record")

def content(root, branch, row):
    root = Path(root)
    paths = [row[k] for k in PATH_FIELDS if row.get(k)]
    dependencies = row.get('runtime_dependencies', [])
    if not isinstance(dependencies, list) or any(not isinstance(p, str) or Path(p).is_absolute() or '\\' in p for p in dependencies):
        raise ValueError('runtime_dependencies must be a list of branch-relative paths')
    paths += dependencies
    paths += ['dataset_generator/common_renderer.py', 'dataset_generator/protocol.json']
    files = {p:file_hash(contained(root/branch,p)) for p in paths}
    if branch != 'Analytics':
        files['../dataset_tools/geometry_dataset.py'] = file_hash(root/'dataset_tools/geometry_dataset.py')
    notes_path=root/'provenance/source_notes.json'
    notes=read(notes_path).get(row['id'],{}) if notes_path.exists() else {}
    return {'branch':branch,'record':row,'files':files,'source_notes':notes}

def assert_formal_dataset(dataset_file):
    dataset_file=Path(dataset_file).resolve()
    branch=dataset_file.parent.name
    root=dataset_file.parent.parent
    if branch not in BRANCHES or dataset_file.name!='dataset.jsonl':
        raise ValueError('Use a formal branch dataset.jsonl')
    approvals=read(root/'provenance/approvals.json')['approvals']
    for row in rows(dataset_file):
        validate_formal_row(root, branch, row)
        approval=approvals.get(row['id'],{})
        if (approval.get('reviewer')!='user' or not approval.get('instruction') or
                digest(content(root,branch,row))!=approval.get('content_sha256')):
            raise ValueError(f"{row['id']}: explicit approval of current original required")

def catalog(root=ROOT):
    root = Path(root)
    approvals = read(root/'provenance/approvals.json')['approvals']
    result, seen = [], set()
    required={'id','source_dataset','question','answer','answer_type','image','original_image','script'}
    for branch in BRANCHES:
        branch_rows=rows(root/branch/'dataset.jsonl')
        for row in branch_rows:
            qid=row['id']
            if qid in seen or not required.issubset(row):
                raise ValueError(f'Duplicate or incomplete formal row: {qid}')
            validate_formal_row(root, branch, row)
            seen.add(qid)
            approval=approvals.get(qid)
            if not approval or approval.get('reviewer')!='user' or not approval.get('instruction') or not approval.get('approved_at_utc'):
                raise ValueError(f'Missing explicit user approval: {qid}')
            current=digest(content(root,branch,row))
            if current != approval.get('content_sha256'):
                raise ValueError(f'{qid}: approved content changed; user reapproval required')
            item={'branch':branch,**row}
            for key in PATH_FIELDS:
                if item.get(key): item[key]=f'{branch}/{item[key]}'
            for category,field in [('base_variant','base_plugins'),('special_variant','special_plugins')]:
                path=root/branch/category/qid/'recipes.json'
                variants=read(path) if path.exists() else []
                expected='generated' if category=='base_variant' else 'passed'
                for variant in variants:
                    if variant['question_id']!=qid or variant.get('status')!=expected:
                        raise ValueError(f'Unaccepted variant in formal package: {qid}')
                    for path_key,hash_key in [('image_path','png_sha256'),('plugin_path','plugin_sha256')]:
                        artifact=contained(root/branch,variant[path_key])
                        if file_hash(artifact)!=variant[hash_key]:
                            raise ValueError(f'Variant hash mismatch: {artifact}')
                item[field]=[f'{branch}/'+v['plugin_path'] for v in variants]
            result.append(item)
    if set(approvals)!=seen:
        raise ValueError('Approval records must match the formal question set exactly')
    return result

@contextmanager
def catalog_write_lock(root, timeout=30):
    """Serialize catalog reads and replacement across the independent workbenches."""
    directory = Path(root) / '.runtime' / 'catalog'
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / 'build.lock').open('a+b') as handle:
        if os.fstat(handle.fileno()).st_size == 0:
            handle.write(b'0')
            handle.flush()
        deadline = time.monotonic() + timeout
        acquired = False
        try:
            while not acquired:
                handle.seek(0)
                try:
                    if os.name == 'nt':
                        import msvcrt
                        msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                    else:
                        import fcntl
                        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    acquired = True
                except OSError as error:
                    if time.monotonic() >= deadline:
                        raise TimeoutError('Another workbench is updating the formal catalog; try again.') from error
                    time.sleep(0.05)
            yield
        finally:
            if acquired:
                handle.seek(0)
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def build(root=ROOT):
    root = Path(root).resolve()
    with catalog_write_lock(root):
        return build_locked(root)

def build_locked(root=ROOT):
    """Build while the caller holds catalog_write_lock across a larger transaction."""
    root = Path(root).resolve()
    result = catalog(root)
    target = root / 'question_bank.jsonl'
    descriptor, name = tempfile.mkstemp(prefix='.question_bank.', suffix='.tmp', dir=root)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8', newline='\n') as handle:
            handle.write(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in result))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['build','check'])
    args=parser.parse_args()
    result=build() if args.command=='build' else catalog()
    if args.command=='check' and result!=rows(ROOT/'question_bank.jsonl'):
        raise SystemExit('Root catalog is stale; run catalog.py build')
    print(json.dumps({'questions':len(result),'branches':{b:sum(r['branch']==b for r in result) for b in BRANCHES},
        'base_variants':sum(len(r['base_plugins']) for r in result),'special_variants':sum(len(r['special_plugins']) for r in result)},ensure_ascii=False))
