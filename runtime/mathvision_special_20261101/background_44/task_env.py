"""Own-directory isolation; import before any project modules."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
BASE = OWN.parent
sys.dont_write_bytecode = True
for variable, folder in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp',
                         'MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = OWN / folder
    target.mkdir(parents=True, exist_ok=True)
    os.environ[variable] = str(target)

def _check(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('background_44 write outside own directory: ' + str(resolved))

def _guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            _check(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        _check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        _check(args[0]); _check(args[1])

sys.addaudithook(_guard)
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(PROJECT))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')
