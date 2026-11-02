from pathlib import Path
import os,sys
sys.dont_write_bytecode=True
OWN=Path(__file__).resolve().parent
TASK=OWN.parents[1]
ROOT=next(p for p in OWN.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
OLD=ROOT/'runtime/mathvision_special_20261101'
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
for key,sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache'}.items():
 p=OWN/sub;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
def guard(event,args):
 if event=='open':
  if not args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):return
  paths=[args[0]]
 elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):paths=[args[0]]
 elif event in ('os.rename','os.replace','os.link','os.symlink'):paths=args[:2]
 else:return
 for p in paths:
  if p is None or isinstance(p,int):continue
  if not Path(os.fsdecode(p)).resolve().is_relative_to(OWN):raise PermissionError('u12 own-runtime write guard: '+str(p))
sys.addaudithook(guard)
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(OLD))
import hashlib,json
from datetime import datetime,timezone
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
 p=Path(p)
 if not p.is_absolute():p=OWN/p
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def eligibility(q):
 from dataset_tools import catalog
 assert q in ['Solid186','Solid226']
 rec=next(r for r in catalog.rows(ROOT/'SolidGeometry/dataset.jsonl') if r['id']==q)
 app=read(ROOT/'provenance/approvals.json')['approvals'][q]
 fp=catalog.digest(catalog.content(ROOT,'SolidGeometry',rec))
 assert app['reviewer']=='user' and app['instruction'] and fp==app['content_sha256']
 assert rec['source_dataset']=='MathVision' and rec==read(TASK/'eligibility_initial.json')[q]['formal_record']
 for n in ['accepted_index.jsonl','collected_index.jsonl']:
  assert not any(r.get('question_id',r.get('id'))==q for r in catalog.rows(ROOT/'SolidGeometry/special_variant'/n))
 assert not any((ROOT/'SolidGeometry/special_variant'/q/n).exists() for n in ['recipes.json','collection.json'])
 return {'at_utc':now(),'question_id':q,'eligible':True,'formal_record':rec,'original_approval_content_sha256':fp}
