"""Own-directory caches and write guard, installed before project imports."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
ROOT = OWN.parent
sys.dont_write_bytecode = True
for key, name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = OWN / name
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def _check(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('background_47 write outside own directory: ' + str(resolved))

def _guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            _check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        _check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        _check(args[0]); _check(args[1])

sys.addaudithook(_guard)
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(PROJECT))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')

def dump(path, data):
    import json
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')

def sha(path):
    import hashlib
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
