"""Unit43 environment and strict write isolation, before any project import."""
import os
import sys
from pathlib import Path

OWN = Path(__file__).resolve().parent
PROJECT = OWN.parents[2]
SHARED = OWN.parent
sys.dont_write_bytecode = True
for variable, leaf in {"TEMP": "tmp", "TMP": "tmp", "MPLCONFIGDIR": "mplcache", "XDG_CACHE_HOME": "cache"}.items():
    directory = OWN / leaf
    directory.mkdir(parents=True, exist_ok=True)
    os.environ[variable] = str(directory)

def check_write(path):
    if isinstance(path, int) or path is None:
        return
    resolved = Path(os.fsdecode(path)).resolve()
    if not resolved.is_relative_to(OWN):
        raise PermissionError("background_43 write outside own unit blocked: " + str(resolved))

def audit(event, args):
    if event == "open":
        path, mode, flags = args
        if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
            check_write(path)
    elif event in ("os.mkdir", "os.remove", "os.rmdir", "os.unlink", "os.chmod", "os.utime", "os.truncate"):
        check_write(args[0])
    elif event in ("os.rename", "os.replace", "os.link", "os.symlink"):
        check_write(args[0]); check_write(args[1])

sys.addaudithook(audit)
sys.path.insert(0, str(PROJECT))
sys.path.insert(0, str(SHARED))
from runtime_isolation import install
ISOLATION = install(OWN / "render_tmp")

def renderer():
    sys.path.insert(0, str(PROJECT / "PlaneGeometry/workbench"))
    from mathvision_adapter import RendererAdapter
    from workbench_io import load_config
    config = load_config()
    adapter = RendererAdapter(config)
    return adapter, config
