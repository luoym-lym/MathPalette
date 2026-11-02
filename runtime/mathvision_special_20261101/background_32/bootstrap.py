import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[2]
sys.dont_write_bytecode = True
for key, leaf in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    directory = ROOT / leaf
    directory.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(directory)

def check_write(path):
    if isinstance(path, int) or path is None:
        return
    p = Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(ROOT):
        raise PermissionError('background_32 write outside own directory: ' + str(p))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(ROOT.parent))
sys.path.insert(0, str(PROJECT))
from runtime_isolation import install
ISOLATION = install(ROOT / 'render_tmp')

import hashlib
import json
from datetime import datetime, timezone

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')

def now():
    return datetime.now(timezone.utc).isoformat()
