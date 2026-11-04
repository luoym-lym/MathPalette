"""Frozen Author designed question; importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT = Path(__file__).resolve().parent

def _renderer():
    path = ROOT / 'mathverse_renderers/plane_arrows/common_renderer.py'
    spec = importlib.util.spec_from_file_location('_authored_extension_renderer', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def build_scene():
    return _renderer().render_scene(json.loads((ROOT / 'scenes/Plane494.json').read_text(encoding='utf-8')))

class Plane494:
    def __init__(self):
        attributes = {'id': 'Plane494', 'source_dataset': 'Author Designed', 'source_key': 'authored-extension:Plane148:ext03', 'question': 'Every available piece has the T shape at the top and consists of four unit squares. Which of the five 20-square shapes below CANNOT be made using exactly 5 whole pieces, without gaps or overlap? Pieces may be rotated or turned over.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E', 'answer': 'E', 'answer_type': 'choice', 'choices': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}}
        for key, value in attributes.items():
            setattr(self, key, value)
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = ROOT / 'scenes/Plane494.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def build_scene(self):
        return build_scene()

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        destination = Path(output_path) if output_path else ROOT.parents[1] / '.runtime/author_designed_redraw/Plane494.png'
        return _renderer().draw(self.scene_path, destination)

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)

if __name__ == '__main__':
    import sys
    print(Plane494().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
