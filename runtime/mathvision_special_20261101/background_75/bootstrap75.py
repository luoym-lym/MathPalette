"""Own-process environment and strict own-root write isolation. No solver configuration."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
for name, leaf in {'TEMP':'tmp', 'TMP':'tmp', 'MPLCONFIGDIR':'mpl_cache', 'XDG_CACHE_HOME':'cache'}.items():
    target = OWN / leaf
    target.mkdir(exist_ok=True)
    os.environ[name] = str(target)
sys.dont_write_bytecode = True

def check(path):
    if isinstance(path, int) or path is None:
        return
    target = Path(os.fsdecode(path)).resolve()
    if not target.is_relative_to(OWN):
        raise PermissionError('background_75 strict ownroot write guard: ' + str(target))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(OWN.parent))
import runtime_isolation
ROUTING = runtime_isolation.install(OWN / 'bridge_tmp', guard_writes=True)

