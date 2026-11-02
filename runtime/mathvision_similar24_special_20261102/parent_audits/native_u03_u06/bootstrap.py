"""Read-only source audit; all new writes confined to this new audit directory."""
from pathlib import Path
import os, sys
sys.dont_write_bytecode = True
OWN = Path(__file__).resolve().parent
ROOT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = ROOT / 'runtime/mathvision_similar24_special_20261102'
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
for name, sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl','XDG_CACHE_HOME':'cache'}.items():
    p = OWN / sub
    p.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(p)
def guard(event, args):
    if event == 'open':
        if not args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
            return
        paths = [args[0]]
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        paths = [args[0]]
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        paths = args[:2]
    else:
        return
    for p in paths:
        if p is None or isinstance(p,int):
            continue
        if not Path(os.fsdecode(p)).resolve().is_relative_to(OWN):
            raise PermissionError('native_u03_u06 audit writes outside OWN: '+str(p))
sys.addaudithook(guard)
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(TASK))
import json, hashlib
from datetime import datetime, timezone
def now():
    return datetime.now(timezone.utc).isoformat()
def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(262144), b''):
            h.update(block)
    return h.hexdigest()
def save(name, data):
    path = OWN / name
    assert path.resolve().is_relative_to(OWN)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')
