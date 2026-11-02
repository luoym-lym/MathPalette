"""Process-only, background_71 write confinement; imported before project code."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
BASE = OWN.parent
PROJECT = OWN.parents[2]
QIDS = ['Solid120', 'Solid138', 'Solid169', 'Solid213', 'Solid215']
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = OWN / sub
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def check(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('background_71 write outside OWNROOT: ' + str(resolved))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
        check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(BASE))

import json
import hashlib
from datetime import datetime, timezone

def now(): return datetime.now(timezone.utc).isoformat()
def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''): h.update(block)
    return h.hexdigest()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def save(path, data):
    p = Path(path)
    if not p.is_absolute(): p = OWN/p
    check(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8')

def eligibility(qid):
    from dataset_tools import catalog
    rec = next(r for r in catalog.rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']==qid)
    approval = read(PROJECT/'provenance/approvals.json')['approvals'][qid]
    content = catalog.content(PROJECT, 'SolidGeometry', rec)
    fingerprint = catalog.digest(content)
    indexes = ['SolidGeometry/special_variant/accepted_index.jsonl','SolidGeometry/special_variant/collected_index.jsonl']
    matches = {p:[r for r in catalog.rows(PROJECT/p) if r.get('question_id',r.get('id'))==qid] for p in indexes}
    special = {n:(PROJECT/'SolidGeometry/special_variant'/qid/n).exists() for n in ('recipes.json','collection.json')}
    reasons = []
    if rec['source_dataset']!='MathVision': reasons.append('not MathVision')
    if fingerprint!=approval['content_sha256'] or approval.get('reviewer')!='user' or not approval.get('instruction'):
        reasons.append('invalid original user approval fingerprint')
    if any(matches.values()) or any(special.values()): reasons.append('Special state present')
    return {'at':now(),'question_id':qid,'eligible':not reasons,'reasons':reasons,'formal_record':rec,
            'approval':approval,'approval_matches':fingerprint==approval['content_sha256'],
            'current_content_sha256':fingerprint,'content_snapshot':content,'matched_special_rows':matches,
            'special_files_present':special,'authoritative_hashes':{p:sha(PROJECT/p) for p in indexes+['SolidGeometry/dataset.jsonl','provenance/approvals.json']}}

def install_render():
    from runtime_isolation import install
    result = install(OWN/'render_tmp')
    sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
    return result
