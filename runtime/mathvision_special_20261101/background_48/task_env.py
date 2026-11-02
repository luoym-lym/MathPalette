"""background_48 strict write isolation, installed before project imports."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
sys.dont_write_bytecode = True
for name, subdir in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    target = OWN / subdir
    target.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(target)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def check_write(value):
    if value is None or isinstance(value, int):
        return
    path = Path(os.fsdecode(value)).resolve()
    if not path.is_relative_to(OWN):
        raise PermissionError('background_48 write blocked: ' + str(path))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
            check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(OWN.parent))
sys.path.insert(0, str(PROJECT))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')
sys.path.insert(0, str(PROJECT / 'PlaneGeometry/workbench'))
