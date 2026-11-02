import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
TASK = HERE.parent
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, directory in {'TEMP':'temp', 'TMP':'temp', 'MPLCONFIGDIR':'mpl', 'XDG_CACHE_HOME':'cache'}.items():
    os.environ[key] = str(HERE / directory)

def check(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(HERE):
        raise PermissionError('background_69 write outside OWNROOT blocked: ' + str(resolved))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])

sys.addaudithook(guard)
for path in (PROJECT, PROJECT / 'SolidGeometry/workbench', TASK):
    sys.path.insert(0, str(path))

def renderer_setup():
    from runtime_isolation import install
    return install(HERE / 'temp' / 'render')
