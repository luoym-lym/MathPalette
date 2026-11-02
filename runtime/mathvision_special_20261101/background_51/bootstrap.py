"""background_51 isolation, installed before any project import."""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
BASE = HERE.parent
sys.dont_write_bytecode = True
for key, name in {'TEMP': 'tmp', 'TMP': 'tmp', 'TMPDIR': 'tmp',
                  'MPLCONFIGDIR': 'mpl_cache', 'XDG_CACHE_HOME': 'cache'}.items():
    target = HERE / name
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def own_guard(event, args):
    def check(path):
        if path is None or isinstance(path, int):
            return
        resolved = Path(os.fsdecode(path)).resolve()
        if not resolved.is_relative_to(HERE):
            raise PermissionError('background_51 write outside own directory: ' + str(resolved))
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check(args[0])
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check(args[0]); check(args[1])
sys.addaudithook(own_guard)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(BASE))
from runtime_isolation import install
ISOLATION = install(HERE / 'render_tmp')
