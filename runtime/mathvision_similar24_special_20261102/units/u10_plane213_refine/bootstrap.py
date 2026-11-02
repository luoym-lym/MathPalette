from pathlib import Path
import os,sys
sys.dont_write_bytecode=True
OWN=Path(__file__).resolve().parent
TASK=OWN.parents[1]
ROOT=next(p for p in OWN.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
OLD=ROOT/'runtime/mathvision_special_20261101'
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
for k,v in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache'}.items():
 p=OWN/v;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
def guard(event,args):
 if event=='open':
  if not args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):return
  paths=[args[0]]
 elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):paths=[args[0]]
 elif event in ('os.rename','os.replace','os.link','os.symlink'):paths=args[:2]
 else:return
 for p in paths:
  if p is None or isinstance(p,int):continue
  if not Path(os.fsdecode(p)).resolve().is_relative_to(OWN):raise PermissionError('u10 writes only own runtime: '+str(p))
sys.addaudithook(guard)
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(OLD))
import hashlib,json
from datetime import datetime,timezone
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(262144),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def save(p,d):
 p=Path(p)
 if not p.is_absolute():p=OWN/p
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def eligibility():
 from dataset_tools import catalog
 q='Plane213';b='PlaneGeometry';rec=next(r for r in catalog.rows(ROOT/b/'dataset.jsonl') if r['id']==q)
 app=read(ROOT/'provenance/approvals.json')['approvals'][q];fp=catalog.digest(catalog.content(ROOT,b,rec))
 assert rec['source_dataset']=='MathVision' and app['reviewer']=='user' and app['instruction'] and fp==app['content_sha256']
 for n in ['accepted_index.jsonl','collected_index.jsonl']:
  assert not [r for r in catalog.rows(ROOT/b/'special_variant'/n) if r.get('question_id',r.get('id'))==q]
 assert not any((ROOT/b/'special_variant'/q/n).exists() for n in ['recipes.json','collection.json'])
 initial=read(TASK/'eligibility_initial.json')[q]
 assert rec==initial['formal_record']
 assert all(sha(ROOT/p)==v for p,v in initial['frozen_source_files_sha256'].items())
 return {'at_utc':now(),'question_id':q,'eligible':True,'formal_record':rec,'approval':app,'current_content_sha256':fp,'frozen_source_files_sha256':initial['frozen_source_files_sha256']}
