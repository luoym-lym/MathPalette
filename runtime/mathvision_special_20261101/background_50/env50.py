import os, sys, json, hashlib
from pathlib import Path
OWN=Path(__file__).resolve().parent
ROOT=OWN.parent
PROJECT=ROOT.parents[1]
sys.dont_write_bytecode=True
for key,name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    p=OWN/name
    p.mkdir(parents=True,exist_ok=True)
    os.environ[key]=str(p)
def guard_path(path):
    if path is None or isinstance(path,int): return
    p=Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(OWN): raise PermissionError('background_50 write outside own directory: '+str(p))
def guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): guard_path(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'): guard_path(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'): guard_path(args[0]); guard_path(args[1])
sys.addaudithook(guard)
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(PROJECT))
from runtime_isolation import install
ISOLATION=install(OWN/'render_tmp')
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
