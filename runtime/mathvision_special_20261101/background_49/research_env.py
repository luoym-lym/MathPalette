"""Strict background_49 runtime routing; install before project imports."""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[2]
SHARED = ROOT.parent
for _name, _sub in [('TEMP', 'temp'), ('TMP', 'temp'), ('TMPDIR', 'temp'),
                     ('MPLCONFIGDIR', 'mplconfig'), ('XDG_CACHE_HOME', 'cache')]:
    _path = ROOT / _sub
    _path.mkdir(parents=True, exist_ok=True)
    os.environ[_name] = str(_path)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
sys.dont_write_bytecode = True

def _check(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(ROOT):
        raise PermissionError('background_49 write outside assigned root: ' + str(resolved))

def _guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            _check(path)
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        _check(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        _check(args[0])
        _check(args[1])

sys.addaudithook(_guard)
sys.path.insert(0, str(SHARED))
sys.path.insert(0, str(PROJECT))
from runtime_isolation import install
ISOLATION = install(ROOT / 'render_tmp')

if __name__ == '__main__':
    import json
    print(json.dumps({'root': str(ROOT), 'project': str(PROJECT), 'isolation': ISOLATION,
                      'strict_own_root_guard': True, 'pid': os.getpid()}))
