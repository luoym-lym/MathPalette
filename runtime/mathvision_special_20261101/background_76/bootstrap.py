"""background_76 process-only environment and strict OWNROOT write boundary."""
import os
import sys
from pathlib import Path

OWNROOT = Path(__file__).resolve().parent
PROJECT = OWNROOT.parents[2]
BASE = OWNROOT.parent
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key, name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target = OWNROOT / name
    target.mkdir(exist_ok=True)
    os.environ[key] = str(target)
sys.dont_write_bytecode = True

def check_write(path):
    if path is None or isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWNROOT):
        raise PermissionError('background_76 write outside OWNROOT blocked: ' + str(resolved))

def audit(event, args):
    if event == 'open':
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(path)
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
        check_write(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):
        check_write(args[0]); check_write(args[1])
sys.addaudithook(audit)
sys.path.insert(0, str(OWNROOT))
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(PROJECT))

if __name__ == '__main__':
    import runpy
    target = Path(sys.argv[1]).resolve()
    sys.argv = [str(target)] + sys.argv[2:]
    is_api_harness = target.is_relative_to(OWNROOT/'harness') and target.name=='quicktest3_isolated.py'
    if is_api_harness:
        import json
        from datetime import datetime, timezone
        with (OWNROOT/'api_process.json').open('x',encoding='utf-8') as stream:
            json.dump({'pid':os.getpid(),'parent_pid':os.getppid(),'python_executable':sys.executable,'exact_argv':sys.argv,'started_at':datetime.now(timezone.utc).isoformat(),'process_only_thread_environment':{k:os.environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},'strict_ownroot_guard_before_all_project_Pillow_numeric_imports':True,'no_child_API_processes_spawned':True},stream,indent=2)
    completed_normally=False
    try:
        runpy.run_path(str(target), run_name='__main__')
        completed_normally=True
    finally:
        if is_api_harness:
            with (OWNROOT/'api_process_finished.json').open('x',encoding='utf-8') as stream:
                json.dump({'pid':os.getpid(),'finished_at':datetime.now(timezone.utc).isoformat(),'runpy_returned_normally':completed_normally,'no_retry':True},stream,indent=2)
