"""u06-only environment and strict filesystem isolation; never edits shared code."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[3]
TASK = OWN.parents[1]
OLD = PROJECT / 'runtime/mathvision_special_20261101'
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, leaf in {'TEMP':'tmp', 'TMP':'tmp', 'MPLCONFIGDIR':'mpl_cache', 'XDG_CACHE_HOME':'cache'}.items():
    dest = OWN / 'ownruntime' / leaf
    dest.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(dest)

def check(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('u06 strict writeguard: ' + str(resolved))

def audit(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])

sys.addaudithook(audit)
sys.path.insert(0, str(PROJECT))

def install_render_isolation():
    sys.path.insert(0, str(OLD))
    import runtime_isolation
    return runtime_isolation.install(OWN / 'ownruntime' / 'bridge', guard_writes=True)

def read_json(path):
    import json
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    import hashlib
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def save(path, value, exclusive=False):
    import json
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x' if exclusive else 'w', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')

def now():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat()
