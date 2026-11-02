"""Read-only review bootstrap; every Python write is confined to this review root."""
from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parent
PROJECT = next(p for p in ROOT.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
sys.dont_write_bytecode = True
for key, folder in [('TEMP', 'tmp'), ('TMP', 'tmp'), ('TMPDIR', 'tmp'),
                    ('MPLCONFIGDIR', 'mpl_cache'), ('XDG_CACHE_HOME', 'cache'),
                    ('PYTHONPYCACHEPREFIX', 'pycache')]:
    location = ROOT / folder
    location.mkdir(exist_ok=True)
    os.environ[key] = str(location)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(ROOT):
        raise PermissionError('Independent review write outside assigned root blocked: ' + str(resolved))

def strict_guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(path)
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check_write(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check_write(args[0])
        check_write(args[1])
    elif event == 'subprocess.Popen':
        raise PermissionError('Review does not launch subprocesses')

sys.addaudithook(strict_guard)
sys.path.insert(0, str(PROJECT / 'runtime/mathvision_special_20261101'))
import runtime_isolation
ISOLATION = runtime_isolation.install(ROOT / 'render_tmp', guard_writes=True)
ISOLATION['strict_review_root'] = str(ROOT)
ISOLATION['strict_guard_installed_before_project_imports'] = True

if __name__ == '__main__':
    import runpy
    runpy.run_path(sys.argv[1], run_name='__main__')
