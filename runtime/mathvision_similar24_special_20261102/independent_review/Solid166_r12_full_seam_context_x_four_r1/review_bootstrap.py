"""Independent offline review only; deny writes outside this review root."""
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
OWN = Path(__file__).resolve().parent
PROJECT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = PROJECT / 'runtime/mathvision_similar24_special_20261102'
UNIT = TASK / 'units/u09_octa_nets'
CANDIDATE = UNIT / 'Solid166/r12_full_seam_context_x_four'
OLD = PROJECT / 'runtime/mathvision_special_20261101'
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, folder in {'TEMP':'cache/tmp', 'TMP':'cache/tmp', 'MPLCONFIGDIR':'cache/mpl',
                    'XDG_CACHE_HOME':'cache/xdg', 'PYTHONPYCACHEPREFIX':'cache/pyc'}.items():
    os.environ[key] = str(OWN / folder)

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Independent review strict writeguard: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
    elif event in ('subprocess.Popen', 'os.system', 'os.posix_spawn', 'socket.connect', 'socket.bind'):
        raise PermissionError('Independent offline review forbids subprocess/network: ' + event)

sys.addaudithook(guard)
for folder in ('cache/tmp','cache/mpl','cache/xdg','cache/pyc','cache/bridge'):
    (OWN / folder).mkdir(parents=True, exist_ok=True)
for p in (PROJECT, OLD, PROJECT / 'SolidGeometry/workbench'):
    sys.path.insert(0, str(p))

import json
import hashlib
from datetime import datetime, timezone

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(name, value):
    p = OWN / name
    check_write(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)

def main(action):
    try:
        action()
    except BaseException:
        import traceback
        error = traceback.format_exc()
        save('offline_error_' + now().replace(':', '-') + '.json', {'time':now(), 'error':error})
        raise
