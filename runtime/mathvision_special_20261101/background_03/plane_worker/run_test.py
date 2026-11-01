import os,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
for variable,name in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mplcache','XDG_CACHE_HOME':'cache'}.items():
    path=HERE/name;path.mkdir(parents=True,exist_ok=True);os.environ[variable]=str(path)
os.environ['PYTHONDONTWRITEBYTECODE']='1';sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101'))
from runtime_isolation import install
install(HERE/'render_tmp')
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101/harness'))
from quicktest3_isolated import run_tests
vid=sys.argv[1]
assert vid in ['v01','v02','original_control']
folder=HERE/'Plane435'/vid
run_tests('PlaneGeometry','Plane435',folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
