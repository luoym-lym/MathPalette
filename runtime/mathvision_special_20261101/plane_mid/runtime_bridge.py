"""Install the shared runtime-only renderer routing and write audit guard."""
from pathlib import Path
import sys

def isolate_native_temporary_files(directory):
    sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
    from runtime_isolation import install
    return install(directory)

