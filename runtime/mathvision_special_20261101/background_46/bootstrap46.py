from pathlib import Path
import os, sys, json, hashlib
OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
TASK = OWN.parent
sys.dont_write_bytecode = True
for var, sub in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    dst = OWN / sub
    dst.mkdir(parents=True, exist_ok=True)
    os.environ[var] = str(dst)
def check_write(path):
    if path is None or isinstance(path, int): return
    p = Path(os.fsdecode(path)).resolve()
    if not p.is_relative_to(OWN):
        raise PermissionError('background_46 write outside own root blocked: ' + str(p))
def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
sys.addaudithook(guard)
sys.path[:0] = [str(PROJECT), str(TASK)]
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, value):
    p=Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:
        json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False); f.write('\n')
