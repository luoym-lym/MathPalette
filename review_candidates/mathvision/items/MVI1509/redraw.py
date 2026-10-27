"""Portable MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
HERE = Path(__file__).resolve().parent
def draw(output_path=None):
    package = HERE.parents[1]
    spec = importlib.util.spec_from_file_location("mathvision_native_runtime", package / "shared/runtime.py")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    destination = Path(output_path) if output_path else package.parents[1] / ".runtime/mathvision_redraw" / (HERE.name + ".png")
    return module.draw(HERE, package / "shared/native", destination)
if __name__ == "__main__":
    import sys
    print(draw(sys.argv[1] if len(sys.argv) > 1 else None))
