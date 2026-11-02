"""background_74: process-local environment and strict OWNROOT write guard."""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PROJECT = HERE.parents[2]
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, name in {'TEMP':'tmp', 'TMP':'tmp', 'TMPDIR':'tmp', 'MPLCONFIGDIR':'mpl_cache', 'XDG_CACHE_HOME':'cache'}.items():
    target = HERE / name
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def check(path):
    if path is None or isinstance(path, int):
        return
    target = Path(os.fsdecode(path)).resolve()
    if not target.is_relative_to(HERE):
        raise PermissionError('background_74 write outside OWNROOT blocked: ' + str(target))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check(args[0]); check(args[1])
sys.addaudithook(guard)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(BASE))

