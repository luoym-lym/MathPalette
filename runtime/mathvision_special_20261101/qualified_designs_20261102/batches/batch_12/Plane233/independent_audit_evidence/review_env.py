"""Review-only isolation. No network, subprocess, or writes outside this directory."""
from pathlib import Path
import os
import sys
import json
import hashlib
import importlib.util

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in OUT.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
BATCH = ROOT / 'runtime/mathvision_special_20261101'
CAND = BATCH / 'background_23/Plane233/r23_four_cell_corner_spine'
TEST = CAND / 'tests/quicktest3_20261101T170529_e04cf4a098e4'
sys.dont_write_bytecode = True
for var, subdir in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl',
                    'XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    dest = OUT / subdir
    dest.mkdir(exist_ok=True)
    os.environ[var] = str(dest)
os.environ['MPLBACKEND'] = 'Agg'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def check_write(path):
    if isinstance(path, int) or path is None:
        return
    dest = Path(os.fsdecode(path)).resolve()
    if not dest.is_relative_to(OUT):
        raise PermissionError('Independent review write outside own directory: ' + str(dest))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
        check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
    elif event in ('subprocess.Popen','os.system','os.startfile','socket.connect','socket.bind'):
        raise PermissionError('Independent audit forbids process launch/network: ' + event)

sys.addaudithook(guard)
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location('shared_runtime_isolation', BATCH / 'runtime_isolation.py')
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)
ISOLATION = shared.install(OUT / 'render_tmp', guard_writes=True)

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()

def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def emit(value):
    print(json.dumps(value, ensure_ascii=False, separators=(',', ':')))
