"""Independent review isolation. No solver, service, or approval operations."""
from pathlib import Path
import os
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
BASE = ROOT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
for key, suffix in {'TEMP':'tmp', 'TMP':'tmp', 'TMPDIR':'tmp',
                    'MPLCONFIGDIR':'mplcache', 'XDG_CACHE_HOME':'cache',
                    'PYTHONPYCACHEPREFIX':'pycache'}.items():
    p = HERE / suffix
    p.mkdir(exist_ok=True)
    os.environ[key] = str(p)

def guard(event, args):
    def check(p):
        if isinstance(p, int) or p is None:
            return
        p = Path(os.fsdecode(p)).resolve()
        if not p.is_relative_to(HERE):
            raise PermissionError('Independent review write outside assigned directory: ' + str(p))
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])
    elif event in ('subprocess.Popen','os.system','os.startfile','socket.connect','socket.connect_ex','socket.bind'):
        raise PermissionError('Independent review blocks network and child processes: ' + event)

sys.addaudithook(guard)
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(HERE / 'render_tmp', guard_writes=True)
sys.path.insert(0, str(ROOT / 'PlaneGeometry/workbench'))
