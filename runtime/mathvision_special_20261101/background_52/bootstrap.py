"""Own-root-only runtime guard; no project imports before install()."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
SESSION = OWN.parent

def install():
    sys.dont_write_bytecode = True
    for key, leaf in [('TEMP', 'tmp'), ('TMP', 'tmp'),
                      ('MPLCONFIGDIR', 'mpl'), ('XDG_CACHE_HOME', 'cache')]:
        path = OWN / leaf
        path.mkdir(parents=True, exist_ok=True)
        os.environ[key] = str(path)

    def check(path):
        if path is None or isinstance(path, int):
            return
        resolved = Path(os.fsdecode(path)).resolve()
        if not resolved.is_relative_to(OWN):
            raise PermissionError('background_52 write outside own root: ' + str(resolved))

    def guard(event, args):
        if event == 'open':
            path, mode, flags = args
            if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
                check(path)
        elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink',
                       'os.chmod', 'os.utime', 'os.truncate'):
            check(args[0])
        elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
            check(args[0])
            check(args[1])
    sys.addaudithook(guard)
    sys.path.insert(0, str(PROJECT))
    sys.path.insert(0, str(SESSION))
    from runtime_isolation import install as route_temp
    receipt = route_temp(OWN / 'render_tmp')
    receipt['strict_own_root'] = str(OWN)
    return receipt
