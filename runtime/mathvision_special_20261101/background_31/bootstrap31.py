"""Unit31 isolation; import this before all project/third-party modules."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
SHARED = OWN.parent
sys.dont_write_bytecode = True
for key, name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache','PYTHONPYCACHEPREFIX':'pycache'}.items():
    target = OWN / name
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('background_31 write outside own root blocked: '+str(resolved))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(guard)
sys.path.insert(0, str(SHARED))
sys.path.insert(0, str(PROJECT))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')

import hashlib
import json
from datetime import datetime, timezone

def stamp():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path, value):
    path = Path(path)
    check_write(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False)
        f.write('\n')

IDS = ['Plane232','Plane255','Plane285','Plane294','Plane297','Plane302','Plane319','Plane327']
