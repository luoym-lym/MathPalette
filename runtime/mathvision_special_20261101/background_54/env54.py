"""Unit-local environment and strict write guard; import before project modules."""
from pathlib import Path
import os
import sys
import json
import hashlib
from datetime import datetime, timezone

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
BASE = OWN.parent
sys.dont_write_bytecode = True
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
for name, sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = OWN / sub
    target.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(target)

def _check(path):
    if path is None or isinstance(path, int):
        return
    p = Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(OWN):
        raise PermissionError('background_54 write outside own root blocked: ' + str(p))

def _guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
        _check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        _check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        _check(args[0]); _check(args[1])

sys.addaudithook(_guard)
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')
sys.path.insert(0, str(PROJECT / 'PlaneGeometry/workbench'))
sys.path.insert(0, str(PROJECT))

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path, data):
    p = Path(path)
    if not p.is_absolute():
        p = OWN / p
    _check(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8')

def eligibility(qid):
    from dataset_tools import catalog
    branch = PROJECT/'PlaneGeometry'
    rec = next(r for r in catalog.rows(branch/'dataset.jsonl') if r['id']==qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    fingerprint = catalog.digest(catalog.content(PROJECT, 'PlaneGeometry', rec))
    sources = ['PlaneGeometry/dataset.jsonl','provenance/approvals.json','PlaneGeometry/special_variant/accepted_index.jsonl','PlaneGeometry/special_variant/collected_index.jsonl']
    indices = {p:catalog.rows(PROJECT/p) for p in sources[2:]}
    matches = {p:[r for r in rs if r.get('question_id',r.get('id'))==qid] for p,rs in indices.items()}
    recipe = branch/'special_variant'/qid/'recipes.json'
    collection = branch/'special_variant'/qid/'collection.json'
    reasons = []
    if rec['source_dataset']!='MathVision': reasons.append('not MathVision')
    if fingerprint!=approval['content_sha256'] or approval.get('reviewer')!='user': reasons.append('approval mismatch')
    if any(matches.values()) or recipe.exists() or collection.exists(): reasons.append('Special state present')
    delivered=[]
    for p in BASE.glob('batch_*/manifest.json'):
        val=read(p)
        if qid in json.dumps(val): delivered.append(str(p))
    if delivered: reasons.append('already delivered')
    sources += [str(p.relative_to(PROJECT)) for p in [recipe,collection] if p.exists()]
    return {'checked_at':now(),'question_id':qid,'eligible':not reasons,'reasons':reasons,
            'formal_record':rec,'approval':approval,'current_content_sha256':fingerprint,
            'approval_matches':fingerprint==approval['content_sha256'],'matched_special_rows':matches,
            'delivered_references':delivered,'authoritative_hashes':{p:sha(PROJECT/p) for p in sources}}
