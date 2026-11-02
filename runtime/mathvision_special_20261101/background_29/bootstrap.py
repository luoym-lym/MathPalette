from pathlib import Path
import os,sys
sys.dont_write_bytecode=True
OWN=Path(__file__).resolve().parent
ROOT=OWN.parents[2]
HISTORY=OWN.parent
for key,name in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    p=OWN/name;p.mkdir(parents=True,exist_ok=True);os.environ[key]=str(p)
sys.path.insert(0,str(HISTORY))
from runtime_isolation import install
ISOLATION=install(OWN/'render_tmp')
def _own(path):
    if path is None or isinstance(path,int):return
    resolved=Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):raise PermissionError('background_29 write outside own root: '+str(resolved))
def _guard(event,args):
    if event=='open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):_own(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):_own(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):_own(args[0]);_own(args[1])
sys.addaudithook(_guard)
