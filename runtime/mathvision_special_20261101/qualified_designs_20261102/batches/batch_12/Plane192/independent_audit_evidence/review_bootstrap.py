"""Independent review isolation; never changes frozen inputs."""
from pathlib import Path
import os
import sys
import importlib.util

OWN = Path(__file__).resolve().parent
ROOT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
BASE = ROOT / 'runtime/mathvision_special_20261101'
for key, relative in {
    'TEMP': 'temp', 'TMP': 'temp', 'TMPDIR': 'temp',
    'MPLCONFIGDIR': 'mplconfig', 'XDG_CACHE_HOME': 'cache',
    'PYTHONPYCACHEPREFIX': 'pycache', 'NUMBA_CACHE_DIR': 'numba_cache',
    'UV_CACHE_DIR': 'uv_cache', 'PIP_CACHE_DIR': 'pip_cache',
}.items():
    path = OWN / relative
    path.mkdir(exist_ok=True)
    os.environ[key] = str(path)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['MPLBACKEND'] = 'Agg'
sys.dont_write_bytecode = True

def check_write(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Independent review write outside own directory: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(path)
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check_write(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check_write(args[0]); check_write(args[1])
    elif event in ('socket.connect', 'socket.bind', 'subprocess.Popen', 'os.system'):
        raise PermissionError('Network/subprocess prohibited in independent review: ' + event)

sys.addaudithook(guard)
spec = importlib.util.spec_from_file_location('review_shared_runtime_isolation', BASE / 'runtime_isolation.py')
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)
ISOLATION = shared.install(OWN / 'render_tmp', guard_writes=True)
sys.path.insert(0, str(ROOT / 'PlaneGeometry/workbench'))
