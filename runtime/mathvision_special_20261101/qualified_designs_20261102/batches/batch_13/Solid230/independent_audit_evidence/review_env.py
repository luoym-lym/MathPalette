"""Independent read-only review bootstrap; no solver/network execution."""
from pathlib import Path
import os
import sys
import json
import hashlib
from datetime import datetime, timezone

OWN = Path(__file__).resolve().parent
ROOT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
SHARED = ROOT / 'runtime/mathvision_special_20261101'
CAND = SHARED / 'background_37/Solid230/r37_equal_value_face_identity'
TEST = CAND / 'tests/quicktest3_20261101T184030_b75026c0c918'
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
for key, name in {'TEMP':'temp', 'TMP':'temp', 'TMPDIR':'temp', 'MPLCONFIGDIR':'mpl_cache', 'XDG_CACHE_HOME':'cache'}.items():
    folder = OWN / name
    folder.mkdir(exist_ok=True)
    os.environ[key] = str(folder)

def owncheck(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Independent review write outside assigned directory: ' + str(resolved))

def guard(event, args):
    if event == 'open' and args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
        owncheck(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        owncheck(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        owncheck(args[0]); owncheck(args[1])
    elif event in ('socket.connect','socket.connect_ex','socket.getaddrinfo','subprocess.Popen','os.system','os.startfile','os.posix_spawn'):
        raise PermissionError('No network or child process permitted in independent review: ' + event)
sys.addaudithook(guard)

def now():
    return datetime.now(timezone.utc).isoformat()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def rows(path):
    path = Path(path)
    return [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()] if path.exists() else []

def sha(data):
    return hashlib.sha256(data).hexdigest()

def fh(path):
    return sha(Path(path).read_bytes())

def canonical(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',',':'), allow_nan=False).encode('utf-8'))

def write(name, value):
    path = OWN / name
    owncheck(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False)
        f.write('\n')

def rel(path):
    return str(Path(path).resolve().relative_to(ROOT)).replace('\\','/')

# The narrow guard above is installed BEFORE importing this shared project helper.
sys.path.insert(0, str(SHARED))
from runtime_isolation import install
ISOLATION = install(OWN / 'render_tmp')
sys.path.insert(0, str(ROOT / 'SolidGeometry/workbench'))
