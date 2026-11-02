"""Own-root isolation. All project imports happen after cache and write guard setup."""
import os
import sys
from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone

OWN = Path(__file__).resolve().parent
PROJECT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = OWN.parents[1]
OLD = PROJECT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, name in {'TEMP':'ownruntime/tmp', 'TMP':'ownruntime/tmp', 'MPLCONFIGDIR':'ownruntime/mpl', 'XDG_CACHE_HOME':'ownruntime/cache'}.items():
    directory = OWN / name
    directory.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(directory)

def check(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('u05 strict write guard: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])
sys.addaudithook(guard)
for path in (PROJECT, PROJECT/'SolidGeometry/workbench', OLD):
    sys.path.insert(0, str(path))
import runtime_isolation
ISOLATION = runtime_isolation.install(OWN/'ownruntime/bridge', guard_writes=True)

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path, value, immutable=False):
    path = Path(path)
    check(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x' if immutable else 'w', encoding='utf-8', newline='\n') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')

def eligibility(qid):
    from dataset_tools import catalog
    rows = catalog.rows(PROJECT/'SolidGeometry/dataset.jsonl')
    record = next(r for r in rows if r['id']==qid)
    approval = load(PROJECT/'provenance/approvals.json')['approvals'][qid]
    digest = catalog.digest(catalog.content(PROJECT, 'SolidGeometry', record))
    special = PROJECT/'SolidGeometry/special_variant'
    def matches(name):
        path = special/name
        return [r for r in catalog.rows(path) if r.get('question_id',r.get('id'))==qid] if path.is_file() else []
    accepted, collected = matches('accepted_index.jsonl'), matches('collected_index.jsonl')
    recipes_path, collection_path = special/qid/'recipes.json', special/qid/'collection.json'
    recipes = load(recipes_path) if recipes_path.is_file() else None
    collection = load(collection_path) if collection_path.is_file() else None
    assignment = next(r for r in load(OWN/'assignment.json')['questions'] if r['question_id']==qid)
    files = {p:{'expected':h,'actual':sha(PROJECT/p)} for p,h in assignment['frozen_source_files_sha256'].items()}
    checks = {'formal_mathvision':record['source_dataset']=='MathVision',
              'approval_current':digest==approval['content_sha256']==assignment['current_content_sha256'],
              'formal_record_matches_assignment':record==assignment['formal_record'],
              'source_bytes_unchanged':all(v['expected']==v['actual'] for v in files.values()),
              'no_pass':not accepted and not recipes, 'no_collect':not collected and not collection}
    return {'at':now(),'question_id':qid,'record':record,'approval':approval,'content_sha256':digest,
            'accepted':accepted,'collected':collected,'recipes':recipes,'collection':collection,
            'checks':checks,'eligible':all(checks.values()),'source_files':files,
            'state_hashes':{str(p.relative_to(PROJECT)):sha(p) for p in [PROJECT/'SolidGeometry/dataset.jsonl',PROJECT/'provenance/approvals.json',special/'accepted_index.jsonl',special/'collected_index.jsonl'] if p.is_file()}}

def environment():
    import platform
    import importlib.metadata
    return {'python':sys.version,'executable':sys.executable,'platform':platform.platform(),
            'packages':{p:importlib.metadata.version(p) for p in ('numpy','matplotlib','Pillow')},
            'environment':{k:os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')},
            'strict_write_root':str(OWN),'runtime_isolation':ISOLATION,'pid':os.getpid()}
