import os
import sys

sys.dont_write_bytecode = True
UNIT = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(UNIT)))
SHARED = os.path.dirname(UNIT)
for key, name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'bytecode_disabled'}.items():
    destination = os.path.join(UNIT, name)
    os.makedirs(destination, exist_ok=True)
    os.environ[key] = destination
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def _inside(path):
    if path is None or isinstance(path, int):
        return
    resolved = os.path.normcase(os.path.realpath(os.fsdecode(path)))
    root = os.path.normcase(os.path.realpath(UNIT))
    if os.path.commonpath([resolved, root]) != root:
        raise PermissionError('background_34 write outside own directory blocked: ' + resolved)

def _write_guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
            _inside(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        _inside(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        _inside(args[0]); _inside(args[1])
sys.addaudithook(_write_guard)

from pathlib import Path
UNIT = Path(UNIT)
PROJECT = Path(PROJECT)
SHARED = Path(SHARED)
sys.path.insert(0, str(SHARED))
sys.path.insert(0, str(PROJECT))
from runtime_isolation import install
ISOLATION = install(UNIT/'render_tmp')

import hashlib
import json
from datetime import datetime, timezone

IDS = ['Plane212','Plane257','Plane336','Plane338','Plane340','Solid88','Solid184','Solid226']
def now(): return datetime.now(timezone.utc).isoformat()
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def canonical(value): return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')).hexdigest()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(value,stream,ensure_ascii=False,indent=2,allow_nan=False)
        stream.write('\n')
def rows(path): return [json.loads(line) for line in Path(path).read_text(encoding='utf-8-sig').splitlines() if line.strip()]
def branch_of(qid): return 'PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry'
def record(qid): return next(row for row in rows(PROJECT/branch_of(qid)/'dataset.jsonl') if row['id']==qid)

def eligibility(qid):
    from dataset_tools import catalog
    branch = branch_of(qid)
    root = PROJECT/branch
    rec = record(qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'].get(qid)
    notes, _ = catalog._source_notes_snapshot(PROJECT)
    actual = catalog.digest(catalog.content(PROJECT,branch,rec,source_notes=notes))
    indexes = {}
    matches = {}
    for name in ('accepted_index.jsonl','collected_index.jsonl'):
        path = root/'special_variant'/name
        entries = rows(path) if path.is_file() else []
        indexes[str(path.relative_to(PROJECT))] = sha(path) if path.is_file() else None
        matches[name] = [row for row in entries if row.get('question_id',row.get('id'))==qid]
    collection = root/'special_variant'/qid/'collection.json'
    coll = read(collection) if collection.exists() else None
    recipes = root/'special_variant'/qid/'recipes.json'
    recipe = read(recipes) if recipes.exists() else None
    current = coll.get('current') if isinstance(coll,dict) else None
    plugins = sorted(str(p.relative_to(PROJECT)) for p in (root/'special_variant'/qid/'plugins').glob('*.json'))
    checks = {'formal_mathvision':rec.get('source_dataset')=='MathVision',
              'original_approval_current':bool(approval and approval.get('reviewer')=='user' and approval.get('instruction') and approval.get('content_sha256')==actual),
              'no_pass':not matches['accepted_index.jsonl'] and not plugins,
              'not_collected':not matches['collected_index.jsonl'] and not current,
              'no_special_completion':not (isinstance(current,dict) and current.get('special_case'))}
    return {'at':now(),'question_id':qid,'branch':branch,'record':rec,'record_sha256':canonical(rec),'approval':approval,'computed_approval_content_sha256':actual,
            'checks':checks,'eligible':all(checks.values()),'index_hashes_mutable_state':indexes,
            'accepted_matches':matches['accepted_index.jsonl'],'collected_matches':matches['collected_index.jsonl'],
            'collection':coll,'recipes':recipe,'formal_special_plugins':plugins}

def source_files(qid):
    rec=record(qid); root=PROJECT/branch_of(qid)
    rel=[rec.get(k) for k in ('image','scene','script','original_image')]+rec.get('runtime_dependencies',[])
    paths=[root/p for p in rel if p]
    paths += [PROJECT/'provenance/approvals.json',PROJECT/'provenance/source_notes.json']
    return {str(p.relative_to(PROJECT)):sha(p) for p in paths if p.is_file()}

def adapter(branch):
    sys.path.insert(0,str(PROJECT/branch/'workbench'))
    if branch=='SolidGeometry':
        source=SHARED/'solid_explore/bridge_adapter.py'
        target=UNIT/'bridge_adapter.py'
        if not target.exists(): target.write_bytes(source.read_bytes())
        import bridge_adapter
        return bridge_adapter.RuntimeBridgeAdapter()
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    config=load_config(); config['runtime_dir']=str(UNIT/'state');config['output_dir']=str(UNIT/'outputs')
    return RendererAdapter(config)

if __name__=='__main__':
    print(json.dumps({'isolation':ISOLATION,'unit':str(UNIT),'strict_unit_write_guard':True}))
