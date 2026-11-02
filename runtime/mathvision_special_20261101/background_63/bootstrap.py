import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PROJECT = BASE.parents[1]
sys.dont_write_bytecode = True
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = HERE / name
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)

def own_guard(event, args):
    def check(path):
        if path is None or isinstance(path, int):
            return
        p = Path(os.fsdecode(path)).resolve()
        if not p.is_relative_to(HERE):
            raise PermissionError('background_63 write outside own directory: '+str(p))
    if event == 'open' and args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
        check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check(args[0]); check(args[1])
sys.addaudithook(own_guard)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(BASE))

import json
import hashlib
from datetime import datetime, timezone
def now(): return datetime.now(timezone.utc).isoformat()
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1048576), b''): h.update(b)
    return h.hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def write(p, value):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:
        json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def rows(p):
    if Path(p).is_file():
        with Path(p).open(encoding='utf-8-sig') as f:
            for line in f:
                if line.strip(): yield json.loads(line)
