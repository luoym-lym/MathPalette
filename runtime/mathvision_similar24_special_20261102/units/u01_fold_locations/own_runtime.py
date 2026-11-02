"""Unit-local environment and strict filesystem isolation (no renderer edits)."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[3]
OLD = PROJECT / 'runtime/mathvision_special_20261101'
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
for name, sub in (('TEMP','temp'),('TMP','temp'),('MPLCONFIGDIR','mpl'),('XDG_CACHE_HOME','cache')):
    local = OWN / 'ownruntime' / sub
    local.mkdir(parents=True, exist_ok=True)
    os.environ[name] = str(local)
sys.dont_write_bytecode = True

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('STRICT UNIT WRITE GUARD: ' + str(resolved))

def audit(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
            check_write(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(audit)
sys.path.insert(0, str(OLD))
sys.path.insert(0, str(PROJECT))
import runtime_isolation
ISOLATION = runtime_isolation.install(OWN / 'ownruntime' / 'bridge', guard_writes=True)

import hashlib
import json
from datetime import datetime, timezone

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path, value):
    target = Path(path)
    check_write(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def now():
    return datetime.now(timezone.utc).isoformat()

if __name__ == '__main__':
    assignment = read(OWN/'assignment.json')
    save(OWN/'checkpoint.json', {'updated_at_utc':now(),'stage':'READING_REFERENCES_HISTORY',
        'question_ids':assignment['question_ids'],'questions':{q:{'status':'in_progress','calls':0} for q in assignment['question_ids']},
        'new_model_calls':0,'own_process_ids':[],'scope':'PRIMARY only; no delivery or formal writes',
        'initial_assignment_sha256':sha(OWN/'assignment.json'),'initial_brief_sha256':sha(OWN/'brief.txt'),
        'isolation':ISOLATION,'strict_write_root':str(OWN)})
    save(OWN/'second_review_queue.json', [])
    print(json.dumps({'own_root':str(OWN),'isolation':ISOLATION,'python':sys.version,'pid':os.getpid()},ensure_ascii=False))
