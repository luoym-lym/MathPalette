from pathlib import Path
import os,sys
sys.dont_write_bytecode=True
OWN=Path(__file__).resolve().parent
TASK=OWN.parent
ROOT=next(p for p in OWN.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
OLD=ROOT/'runtime/mathvision_special_20261101'
SOURCE=TASK/'units/u02_pieces'
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
for k,v in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache'}.items():
 p=OWN/v;p.mkdir(parents=True,exist_ok=True);os.environ[k]=str(p)
def guard(event,args):
 if event=='open':
  if not args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):return
  ps=[args[0]]
 elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):ps=[args[0]]
 elif event in ('os.rename','os.replace','os.link','os.symlink'):ps=args[:2]
 else:return
 for p in ps:
  if p is None or isinstance(p,int):continue
  if not Path(os.fsdecode(p)).resolve().is_relative_to(OWN):raise PermissionError('recovery_u02 own-runtime write guard: '+str(p))
sys.addaudithook(guard)
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(OLD))
import hashlib,json
from datetime import datetime,timezone
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(262144),b''):h.update(b)
 return h.hexdigest()
def save(p,v):
 p=Path(p)
 if not p.is_absolute():p=OWN/p
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x',encoding='utf-8') as f:json.dump(v,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def eligibility(q):
 from dataset_tools import catalog
 r=next(r for r in catalog.rows(ROOT/'PlaneGeometry/dataset.jsonl') if r['id']==q)
 a=read(ROOT/'provenance/approvals.json')['approvals'][q]
 fp=catalog.digest(catalog.content(ROOT,'PlaneGeometry',r))
 assert r['source_dataset']=='MathVision' and a['reviewer']=='user' and a['instruction'] and fp==a['content_sha256']
 for n in ['accepted_index.jsonl','collected_index.jsonl']:
  assert not any(v.get('question_id',v.get('id'))==q for v in catalog.rows(ROOT/'PlaneGeometry/special_variant'/n))
 assert not any((ROOT/'PlaneGeometry/special_variant'/q/n).exists() for n in ['recipes.json','collection.json'])
 files={r[k] for k in ['image','original_image','scene','script'] if r.get(k)}|set(r.get('runtime_dependencies',[]))
 return {'at_utc':now(),'question_id':q,'eligible':True,'formal_record':r,'approval':a,'current_approval_content_sha256':fp,'source_file_sha256':{str((ROOT/'PlaneGeometry'/n).relative_to(ROOT)).replace('\\','/'):sha(ROOT/'PlaneGeometry'/n) for n in files}}
