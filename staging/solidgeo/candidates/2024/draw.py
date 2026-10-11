"""Reproduce this candidate; no writes occur on import."""
from pathlib import Path
import importlib.util

HERE = Path(__file__).resolve().parent

def draw(output_path=None):
    helper = HERE.parents[1] / 'shared/runtime.py'
    spec = importlib.util.spec_from_file_location('_candidate_runtime', helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    output = output_path or HERE.parents[3] / '.runtime/solidgeo-reproduced' / (HERE.name + '.png')
    return module.draw(HERE / 'scene.json', output, 'views')

if __name__ == '__main__':
    import sys
    print(draw(sys.argv[1] if len(sys.argv) > 1 else None))
