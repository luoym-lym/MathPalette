"""Own-root environment and write guard; execute before project imports."""
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True
OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
SHARED = OWN.parent
for variable, folder in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = OWN / folder
    target.mkdir(parents=True, exist_ok=True)
    os.environ[variable] = str(target)

def own_path(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('background_53 write outside own root blocked: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            own_path(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        own_path(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        own_path(args[0]); own_path(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(SHARED))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')
sys.path.insert(0, str(PROJECT / 'SolidGeometry/workbench'))

