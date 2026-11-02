import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
SESSION = OWN.parent

def install(render=False):
    sys.dont_write_bytecode = True
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
        os.environ[key] = '1'
    for key, leaf in [('TEMP','tmp'),('TMP','tmp'),('MPLCONFIGDIR','mpl'),('XDG_CACHE_HOME','cache')]:
        p = OWN / leaf
        p.mkdir(parents=True, exist_ok=True)
        os.environ[key] = str(p)
    def check(p):
        if p is None or isinstance(p,int): return
        p = Path(os.fsdecode(p)).resolve()
        if not p.is_relative_to(OWN):
            raise PermissionError('background_62 write outside own root: '+str(p))
    def guard(event,args):
        if event == 'open':
            if args[2] & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC): check(args[0])
        elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
            check(args[0])
        elif event in ('os.rename','os.replace','os.link','os.symlink'):
            check(args[0]); check(args[1])
    sys.addaudithook(guard)
    sys.path.insert(0,str(PROJECT)); sys.path.insert(0,str(SESSION))
    if render:
        from runtime_isolation import install as route
        return route(OWN/'render_tmp')
    return {'own_root':str(OWN),'guard_installed':True,'local_threads':1}
