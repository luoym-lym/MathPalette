"""Process-only isolation. Import before any project, Pillow or numeric code."""
from pathlib import Path
import os
import sys
OWN = Path(__file__).resolve().parent
BASE = OWN.parent
PROJECT = OWN.parents[2]
QIDS = ('Solid140', 'Solid219', 'Solid236')
sys.dont_write_bytecode = True
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
for name, sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p = OWN/sub
    p.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(p)
def check(path):
    if path is None or isinstance(path,int): return
    p=Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(OWN):
        raise PermissionError('background_67 forbids write outside OWNROOT: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'): check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(PROJECT))
sys.path.insert(0,str(BASE))
import json
import hashlib
from datetime import datetime,timezone
def now(): return datetime.now(timezone.utc).isoformat()
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(262144),b''): h.update(b)
    return h.hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,v):
    p=Path(p)
    if not p.is_absolute(): p=OWN/p
    check(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def eligibility(q):
    from dataset_tools import catalog
    rec=next(r for r in catalog.rows(PROJECT/'SolidGeometry/dataset.jsonl') if r['id']==q)
    approval=read(PROJECT/'provenance/approvals.json')['approvals'][q]
    content=catalog.content(PROJECT,'SolidGeometry',rec)
    fp=catalog.digest(content)
    indexes=['SolidGeometry/special_variant/accepted_index.jsonl','SolidGeometry/special_variant/collected_index.jsonl']
    rows={p:[r for r in catalog.rows(PROJECT/p) if r.get('question_id',r.get('id'))==q] for p in indexes}
    specials={n:(PROJECT/'SolidGeometry/special_variant'/q/n).exists() for n in ('recipes.json','collection.json')}
    delivered=[]
    for p in BASE.glob('batch_*/manifest.json'):
        if q in p.read_text(encoding='utf-8-sig'): delivered.append(str(p))
    reasons=[]
    if rec['source_dataset']!='MathVision': reasons.append('source is not MathVision')
    if fp!=approval['content_sha256'] or approval.get('reviewer')!='user' or not approval.get('instruction'): reasons.append('invalid original approval')
    if any(rows.values()) or any(specials.values()): reasons.append('Special state present')
    if delivered: reasons.append('already delivered')
    paths=['SolidGeometry/dataset.jsonl','provenance/approvals.json']+indexes
    return {'at':now(),'question_id':q,'eligible':not reasons,'reasons':reasons,'formal_record':rec,'approval':approval,'current_content_sha256':fp,'content_snapshot':content,'approval_matches':fp==approval['content_sha256'],'matched_special_rows':rows,'special_files_present':specials,'delivered':delivered,'authoritative_hashes':{p:sha(PROJECT/p) for p in paths}}
