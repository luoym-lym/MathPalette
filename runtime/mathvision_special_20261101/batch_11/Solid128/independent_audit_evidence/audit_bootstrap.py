"""Read-only independent audit; all writes confined to this new review directory."""
from pathlib import Path
import os
import sys
import json
import hashlib
import datetime

OWN = Path(__file__).resolve().parent
ROOT = OWN.parents[3]
BASE = ROOT / 'runtime/mathvision_special_20261101'
QUESTION = BASE / 'background_35/Solid128'
CANDIDATE = QUESTION / 'r35_corner_ownership_mixed_rims'
TEST = CANDIDATE / 'tests/quicktest3_20261101T175556_f6c06c573d0c'
sys.dont_write_bytecode = True
for key, folder in {'TEMP':'tmp', 'TMP':'tmp', 'TMPDIR':'tmp', 'MPLCONFIGDIR':'mplconfig', 'XDG_CACHE_HOME':'cache', 'PYTHONPYCACHEPREFIX':'pycache'}.items():
    os.environ[key] = str(OWN / folder)
    (OWN / folder).mkdir(exist_ok=True)
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['MPLBACKEND'] = 'Agg'

def enforce_path(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Independent-review write outside assigned directory blocked: ' + str(resolved))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            enforce_path(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        enforce_path(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        enforce_path(args[0]); enforce_path(args[1])
    elif event in ('socket.connect', 'socket.connect_ex', 'socket.bind'):
        raise PermissionError('Independent review makes no network calls or servers')

sys.addaudithook(guard)
sys.path.insert(0, str(BASE))
import runtime_isolation
ISOLATION = runtime_isolation.install(OWN / 'tmp', guard_writes=True)
sys.path.insert(0, str(ROOT))

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()

def write(name, value):
    path = OWN / name
    enforce_path(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

if __name__ == '__main__':
    inputs = read(QUESTION / 'input_fingerprints.json')
    paths = set(QUESTION.rglob('*'))
    paths.update(ROOT / p for p in inputs['files'])
    paths.update(ROOT / p for p in ['SolidGeometry/dataset.jsonl', 'provenance/approvals.json', 'SolidGeometry/special_variant/accepted_index.jsonl', 'SolidGeometry/special_variant/collected_index.jsonl', 'SolidGeometry/workbench/README.md', 'SolidGeometry/workbench/agent_prompt.md', 'dataset_tools/question_review.py'])
    paths.update(BASE / p for p in ['Solid128_r35_corner_ownership_mixed_rims_independent_review_brief.txt','Solid128_r35_corner_ownership_mixed_rims_pre_review_evidence_check.json','annotation_semantics_lessons_20261102.json','runtime_isolation.py','background_35/history_read_audit.json','background_35/second_review_queue.json'])
    entries = {str(p.relative_to(ROOT)): {'sha256':sha(p),'size':p.stat().st_size,'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime, datetime.timezone.utc).isoformat()} for p in sorted(paths) if p.is_file()}
    write('read_only_inputs_before.json', {'created_at':now(), 'scope':'candidate, relevant source/dependencies, protocols, eligibility records and assigned audit context only; no claim about entire shared workspace','files':entries})
    write('isolation.json', {'created_at':now(), 'shared_runtime_isolation':ISOLATION,'stricter_own_directory_write_guard':True,'network_guard':True,'environment':{k:os.environ[k] for k in ['TEMP','TMP','TMPDIR','MPLCONFIGDIR','XDG_CACHE_HOME','PYTHONPYCACHEPREFIX','PYTHONDONTWRITEBYTECODE','MPLBACKEND']},'nested_agents':0,'solver_calls':0,'background_processes_started':0})
    print(json.dumps({'root':str(ROOT),'own':str(OWN),'snapshot_files':len(entries),'isolation':ISOLATION},ensure_ascii=False))
