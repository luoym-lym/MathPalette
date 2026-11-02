"""Unit u09 only: private environment, unchanged bridge and strict write guard."""
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
OWN = Path(__file__).resolve().parent
PROJECT = next(p for p in OWN.parents if (p / 'MATHPALETTE_PROTOCOL.md').is_file())
TASK = OWN.parent.parent
OLD = PROJECT / 'runtime/mathvision_special_20261101'
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, folder in {'TEMP':'ownruntime/tmp', 'TMP':'ownruntime/tmp',
                    'MPLCONFIGDIR':'ownruntime/mpl', 'XDG_CACHE_HOME':'ownruntime/cache'}.items():
    os.environ[key] = str(OWN / folder)

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN) or resolved in (OWN/'brief.txt', OWN/'assignment.json'):
        raise PermissionError('u09 strict writeguard blocked: ' + str(resolved))

def writeguard(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):
            check_write(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(writeguard)
for folder in ('ownruntime/tmp','ownruntime/mpl','ownruntime/cache','ownruntime/bridge'):
    (OWN/folder).mkdir(parents=True,exist_ok=True)
for p in (PROJECT, OLD, PROJECT/'SolidGeometry/workbench'):
    sys.path.insert(0,str(p))

import json
import hashlib
from datetime import datetime, timezone

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def save(path,value,exclusive=False):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x' if exclusive else 'w',encoding='utf-8',newline='\n') as f:
        json.dump(value,f,ensure_ascii=False,indent=2,allow_nan=False)
        f.write('\n')

def bridge_setup():
    import runtime_isolation
    return runtime_isolation.install(OWN/'ownruntime/bridge',guard_writes=True)

def initial_checkpoint():
    assignment=load(OWN/'assignment.json')
    if not (OWN/'checkpoint.json').exists():
        save(OWN/'checkpoint.json',{
            'unit_id':'u09_octa_nets','phase':'reading_and_primary_mathematics',
            'updated_at':now(),'assigned':['Solid166','Solid240'],
            'own_root':str(OWN),'assignment_sha256':sha(OWN/'assignment.json'),
            'brief_sha256':sha(OWN/'brief.txt'),'new_actual_calls':0,
            'PRIMARY_candidates':[], 'second_review_performed':False,
            'formal_writes_Pass_Collect':False,
            'questions':{q:{'status':'in_progress','reason':'Read references, full history and verify original mathematics before design.'} for q in assignment['question_ids']},
            'own_processes':[], 'errors':[], 'holds':[], 'unworked':[]})
    if not (OWN/'second_review_queue.json').exists():
        save(OWN/'second_review_queue.json',[])

initial_checkpoint()
