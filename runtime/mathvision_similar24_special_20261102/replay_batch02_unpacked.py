"""Exact offline replay of the delivered ZIP under an own-runtime write guard."""
import os
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OWN = HERE/'batch_02_verification'
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key] = '1'
for key, suffix in [('MPLCONFIGDIR','mpl'),('TEMP','tmp'),('TMP','tmp'),('XDG_CACHE_HOME','cache')]:
    path = OWN/suffix
    path.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(path)

def check_write(path):
    if isinstance(path, int):
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError('Replay write outside own verification root: '+str(resolved))

def guard(event, args):
    if event == 'open':
        path, mode, flags = args
        if (isinstance(mode,str) and any(x in mode for x in 'wax+')) or (isinstance(flags,int) and flags & (os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC)):
            check_write(path)
    elif event in ('os.mkdir','os.rmdir','os.remove','os.chmod','os.utime'):
        check_write(args[0])
    elif event in ('os.rename','os.link','os.symlink'):
        check_write(args[0]);check_write(args[1])

sys.addaudithook(guard)
import runpy
script = OWN/'unpacked/batch_02/replay_candidate.py'
sys.argv = [str(script), 'Plane321', '--output', str(OWN/'reproduced/Plane321.png')]
runpy.run_path(str(script), run_name='__main__')
