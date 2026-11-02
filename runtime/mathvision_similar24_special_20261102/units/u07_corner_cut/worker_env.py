"""Unit u07 only: process-local environment, original isolation, strict write guard."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[3]
TASK = OWN.parents[1]
OLD = PROJECT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
for name, sub in {'TEMP':'ownruntime/tmp', 'TMP':'ownruntime/tmp',
                  'MPLCONFIGDIR':'ownruntime/mpl', 'XDG_CACHE_HOME':'ownruntime/cache'}.items():
    os.environ[name] = str(OWN / sub)

def checked(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('u07 strict write guard: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            checked(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        checked(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        checked(args[0]); checked(args[1])

sys.addaudithook(guard)
for name in ('ownruntime/tmp','ownruntime/mpl','ownruntime/cache'):
    (OWN / name).mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(OLD))
import runtime_isolation
ISOLATION = runtime_isolation.install(OWN / 'ownruntime/scene', guard_writes=True)

import json
import hashlib
from datetime import datetime, timezone

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def write(path, data, immutable=False):
    path = Path(path)
    checked(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x' if immutable else 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')

def eligibility(qid):
    from dataset_tools.catalog import content, digest
    assignment = read(OWN/'assignment.json')
    assigned = next(x for x in assignment['questions'] if x['question_id']==qid)
    rows = [json.loads(line) for line in (PROJECT/'PlaneGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    row = next(x for x in rows if x['id']==qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    actual = digest(content(PROJECT,'PlaneGeometry',row))
    mismatches = {p:{'expected':v,'current':sha(PROJECT/p)} for p,v in assigned['frozen_source_files_sha256'].items() if sha(PROJECT/p)!=v}
    accepted=[]; collected=[]
    for file, target in [('accepted_index.jsonl',accepted),('collected_index.jsonl',collected)]:
        path=PROJECT/'PlaneGeometry/special_variant'/file
        if path.exists():
            for line in path.read_text(encoding='utf-8-sig').splitlines():
                if line.strip():
                    entry=json.loads(line)
                    if entry.get('question_id',entry.get('id'))==qid: target.append(entry)
    recipes=PROJECT/'PlaneGeometry/special_variant'/qid/'recipes.json'
    collection=PROJECT/'PlaneGeometry/special_variant'/qid/'collection.json'
    recipe_data=read(recipes) if recipes.exists() else []
    collection_data=read(collection) if collection.exists() else None
    result={'checked_at':now(),'question_id':qid,'source_dataset':row['source_dataset'],
            'formal_record':row,'approval':approval,'current_content_sha256':actual,
            'assigned_record_unchanged':row==assigned['formal_record'],
            'source_hash_mismatches':mismatches,'accepted_entries':accepted,
            'collected_entries':collected,'recipes':recipe_data,'collection':collection_data}
    result['eligible']=(row==assigned['formal_record'] and row['source_dataset']=='MathVision'
        and actual==approval['content_sha256']==assigned['current_content_sha256']
        and approval.get('reviewer')=='user' and not mismatches and not accepted and not collected
        and not recipe_data and not collection_data)
    return result

def setup_renderer():
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    config=load_config()
    config['runtime_dir']=str(OWN/'ownruntime/workbench')
    config['output_dir']=str(OWN/'ownruntime/output')
    adapter=RendererAdapter(config)
    metadata={qid:adapter.inspect_question(qid) for qid in ('Plane194','Plane245')}
    return config,adapter,metadata,PluginRenderer(config,adapter,metadata)
