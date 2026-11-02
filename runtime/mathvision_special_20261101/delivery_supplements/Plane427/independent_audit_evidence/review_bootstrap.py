"""Independent offline review. No project imports before install of strict guard."""
import os
import sys
from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[3]
TASK = PROJECT / 'runtime/mathvision_special_20261101'
CAND = TASK / 'background_41/Plane427/r41_isosceles_base_angle_frame'
TEST = CAND / 'tests/quicktest3_20261101T190252_5a8fad5d15a9'
sys.dont_write_bytecode = True
for key, child in [('TEMP','temp'), ('TMP','temp'), ('MPLCONFIGDIR','mplconfig'), ('XDG_CACHE_HOME','cache')]:
    os.environ[key] = str(OWN / child)
    (OWN / child).mkdir(exist_ok=True)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['MPLBACKEND'] = 'Agg'
WRITE_EVENTS = []

def check(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Independent review write outside own root blocked: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check(path)
            WRITE_EVENTS.append(str(path))
    elif event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.unlink', 'os.chmod', 'os.utime', 'os.truncate'):
        check(args[0])
    elif event in ('os.rename', 'os.replace', 'os.link', 'os.symlink'):
        check(args[0]); check(args[1])
    elif event in ('socket.connect', 'socket.connect_ex', 'socket.bind', 'subprocess.Popen', 'os.system', 'os.spawn'):
        raise PermissionError('Offline independent review forbids network and child processes: ' + event)

sys.addaudithook(guard)

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def write(name, obj):
    path = OWN / name
    check(path)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def route_runtime():
    import importlib.util
    sys.path.insert(0, str(PROJECT))
    spec = importlib.util.spec_from_file_location('readonly_runtime_isolation', TASK / 'runtime_isolation.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.install(OWN / 'temp/scenes', guard_writes=True)

def tracked_paths():
    paths = set()
    for name in ['AGENTS.md','MATHPALETTE_PROTOCOL.md','requirements.txt','question_bank.jsonl','.env', '.git/HEAD', '.git/index', '.git/config', 'PlaneGeometry/dataset.jsonl','PlaneGeometry/REDRAW_PROTOCOL.md']:
        p=PROJECT/name
        if p.is_file(): paths.add(p)
    formal=next(json.loads(line) for line in (PROJECT/'PlaneGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if json.loads(line).get('id')=='Plane427')
    for name in [formal[k] for k in ['image','original_image','script','scene']] + formal['runtime_dependencies'] + ['dataset_generator/common_renderer.py','dataset_generator/protocol.json']:
        paths.add(PROJECT/'PlaneGeometry'/name)
    for directory in [PROJECT/'provenance', PROJECT/'dataset_tools', PROJECT/'PlaneGeometry/workbench', TASK/'background_41', TASK/'background_20/Plane427']:
        for p in directory.rglob('*'):
            if p.is_file() and '__pycache__' not in p.parts: paths.add(p)
    for directory in [TASK/'background_20', PROJECT/'PlaneGeometry/special_variant']:
        paths.update(p for p in directory.glob('*') if p.is_file())
    paths.update((PROJECT/'PlaneGeometry/special_variant/Plane427').rglob('*'))
    for p in TASK.glob('Plane427*'): 
        if p.is_file(): paths.add(p)
    paths.add(TASK/'runtime_isolation.py')
    paths.add(TASK/'harness/quicktest3_isolated.py')
    return sorted(p for p in paths if p.is_file())

def inventory():
    result = {}
    for path in tracked_paths():
        stat = path.stat()
        rel = path.relative_to(PROJECT).as_posix()
        entry = {'size': stat.st_size, 'mtime_ns': stat.st_mtime_ns}
        try:
            entry['sha256'] = sha(path)
        except OSError as exc:
            entry['read_error'] = str(exc)
        result[rel] = entry
    return result

if __name__ == '__main__':
    baseline = inventory()
    write('read_only_baseline_manifest.json', {'created_at': datetime.now(timezone.utc).isoformat(), 'files': baseline})
    write('isolation_setup.json', {'own_root':str(OWN), 'project':str(PROJECT), 'environment':{key:os.environ[key] for key in ['TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME','PYTHONDONTWRITEBYTECODE','MPLBACKEND']}, 'strict_guard_installed_before_project_imports':True, 'network_child_processes_forbidden':True, 'baseline_files':len(baseline), 'baseline_bytes':sum(x['size'] for x in baseline.values())})
    print(json.dumps({'project': str(PROJECT), 'baseline_files':len(baseline), 'bytes':sum(x['size'] for x in baseline.values())}))
