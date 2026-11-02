import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
BASE = HERE.parent
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[variable] = '1'
for variable, leaf in {'TEMP': 'tmp', 'TMP': 'tmp', 'MPLCONFIGDIR': 'mpl_cache', 'XDG_CACHE_HOME': 'cache'}.items():
    target = HERE / leaf
    target.mkdir(exist_ok=True)
    os.environ[variable] = str(target)
sys.dont_write_bytecode = True

def own_path(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(HERE):
        raise PermissionError('background_60 write outside own root: ' + str(resolved))

def write_guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            own_path(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        own_path(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        own_path(args[0]); own_path(args[1])

sys.addaudithook(write_guard)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(HERE / 'render_tmp')
