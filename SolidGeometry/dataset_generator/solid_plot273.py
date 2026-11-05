"""User-approved frozen original; importing this module writes no files."""
from pathlib import Path
import importlib.util
import json
import sys
ROOT = Path(__file__).resolve().parent
ITEM = ROOT / 'author_extensions95_v1/items/Solid273'

def _engine():
    path = ROOT / 'author_extensions95_v1/engine.py'
    spec = importlib.util.spec_from_file_location('_extensions95_Solid273', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

def build_scene():
    return _engine().capture(ITEM)

def draw_original(output_path):
    target = Path(output_path).resolve()
    if target.suffix.lower() not in ('.png', '.svg'):
        raise ValueError('Use a PNG or SVG output')
    if target.is_relative_to(ROOT.parent):
        raise ValueError('Redraw outside formal source directories')
    data = _engine().render(ITEM, vector=target.suffix.lower() == '.svg')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return str(target)

class Solid273:
    def __init__(self):
        row = next(json.loads(line) for line in (ROOT.parent / 'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines()
                   if line.strip() and json.loads(line)['id'] == 'Solid273')
        for key, value in row.items():
            setattr(self, key, value)
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None

    def get_scene(self):
        return json.loads((ROOT / 'scenes/Solid273.json').read_text(encoding='utf-8'))

    def build_scene(self):
        return build_scene()

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        if output_path is None:
            raise ValueError('An explicit output path is required')
        return draw_original(output_path)

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Provide a PNG or SVG output path')
    print(draw_original(sys.argv[1]))
