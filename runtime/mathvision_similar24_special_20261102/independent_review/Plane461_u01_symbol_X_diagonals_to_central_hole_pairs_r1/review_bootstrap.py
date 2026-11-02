"""Independent Plane461 review: own-root writes only; no network or children."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = PROJECT / 'runtime/mathvision_similar24_special_20261102'
UNIT = TASK / 'units/u01_fold_locations'
CAND = UNIT / 'Plane461/u01_symbol_X_diagonals_to_central_hole_pairs'
REF = TASK / 'references/Plane217'
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
sys.dont_write_bytecode = True

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('INDEPENDENT REVIEW OWN-ROOT WRITE GUARD: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        if args[2] & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
    elif event in ('socket.connect','socket.bind','subprocess.Popen','os.system','os.spawn'):
        raise PermissionError('Review forbids network/process launch: ' + event)

sys.addaudithook(guard)
for key, sub in (('TEMP','temp'),('TMP','temp'),('MPLCONFIGDIR','mpl'),('XDG_CACHE_HOME','cache')):
    target = OWN / 'ownruntime' / sub
    target.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(target)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(PROJECT / 'runtime/mathvision_special_20261101'))

import hashlib
import json
from datetime import datetime, timezone

def now():
    return datetime.now(timezone.utc).isoformat()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(part)
    return h.hexdigest()

def save(path, value):
    target = Path(path)
    check_write(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def bridge():
    import runtime_isolation
    return runtime_isolation.install(OWN / 'ownruntime/bridge', guard_writes=True)

def snapshot():
    paths = set(p for root in (UNIT,REF) for p in root.rglob('*') if p.is_file())
    assignment = read(UNIT / 'assignment.json')
    target = next(q for q in assignment['questions'] if q['question_id'] == 'Plane461')
    paths.update(PROJECT / p for p in target['frozen_source_files_sha256'])
    paths.update(PROJECT / p for p in read(REF / 'reference.json')['frozen_source_files_sha256'])
    paths.update(PROJECT / p for p in ('AGENTS.md','MATHPALETTE_PROTOCOL.md','PlaneGeometry/REDRAW_PROTOCOL.md','PlaneGeometry/dataset_generator/protocol.json','PlaneGeometry/workbench/README.md','PlaneGeometry/workbench/agent_prompt.md','PlaneGeometry/workbench/plugin.schema.json','runtime/mathvision_special_20261101/runtime_isolation.py'))
    paths.update(TASK / p for p in ('task.json','reference_style_summary.json','history_index.json','parent_review_preflight.json','parent_imitation_priority_20261102.txt'))
    paths.update(p for p in (TASK/'parent_audits/native_u01_u04').rglob('*') if p.is_file())
    return {str(p.relative_to(PROJECT)).replace('\\','/'): sha(p) for p in sorted(paths)}

if __name__ == '__main__':
    state = {'created_at_utc': now(), 'pid': os.getpid(), 'python': sys.version,
             'strict_guard_installed_before_project_numeric_imports': True,
             'network_and_child_processes_blocked': True,
             'environment': {k: os.environ[k] for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS','TEMP','TMP','MPLCONFIGDIR','XDG_CACHE_HOME')}}
    save(OWN/'environment.json', state)
    save(OWN/'scoped_before.json', snapshot())
    print(json.dumps({'environment': state, 'scoped_files':len(read(OWN/'scoped_before.json'))}))
