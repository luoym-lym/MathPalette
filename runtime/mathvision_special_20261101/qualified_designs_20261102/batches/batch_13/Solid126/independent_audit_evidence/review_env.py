from pathlib import Path
import sys, os
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
assert (ROOT / 'MATHPALETTE_PROTOCOL.md').is_file()
for var, leaf in [('TEMP','temp'),('TMP','temp'),('MPLCONFIGDIR','mpl'),('XDG_CACHE_HOME','cache')]:
    os.environ[var] = str(OUT / leaf)
    (OUT / leaf).mkdir(exist_ok=True)
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ['MPLBACKEND']='Agg'
sys.dont_write_bytecode=True
WRITES=[]
BLOCKED=[]
def check(path):
    if isinstance(path,int) or path is None: return
    resolved=Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OUT):
        BLOCKED.append(str(resolved))
        raise PermissionError('Independent review write outside own directory: '+str(resolved))
    WRITES.append(str(resolved))
def guard(event,args):
    if event=='open':
        path, mode, flags=args
        if flags & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): check(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]);check(args[1])
    elif event in ('socket.connect','socket.getaddrinfo','subprocess.Popen','os.system','os.startfile'):
        BLOCKED.append(event)
        raise PermissionError('Offline independent review blocks '+event)
sys.addaudithook(guard)
sys.path.insert(0,str(ROOT))
import importlib.util
spec=importlib.util.spec_from_file_location('review_runtime_isolation',ROOT/'runtime/mathvision_special_20261101/runtime_isolation.py')
isolation=importlib.util.module_from_spec(spec)
spec.loader.exec_module(isolation)
ISOLATION=isolation.install(OUT/'render_tmp',guard_writes=False)
ISOLATION.update(own_directory_guard_installed_before_project_import=True,network_and_child_processes_blocked=True,own_root=str(OUT))
import json,hashlib
from datetime import datetime, timezone
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def save(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def stamp():return datetime.now(timezone.utc).isoformat()
