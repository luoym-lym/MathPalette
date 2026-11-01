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
    return _renderer().render_scene(json.loads((ROOT / 'scenes/Plane503.json').read_text(encoding='utf-8')))

class Plane503:
    def __init__(self):
        attributes = {'id': 'Plane503', 'source_dataset': 'Author designed', 'source_key': 'authored-extension:Plane312:ext02', 'question': 'Which pair of the four numbered pieces can be fitted together, without gaps or overlap, to make the six-sided target at the bottom? All pieces and the target are drawn at the same scale. Pieces may be rotated or turned over.\nChoices:\nA: 1 and 2\nB: 1 and 3\nC: 2 and 3\nD: 2 and 4\nE: 1 and 4\nF: 3 and 4', 'answer': 'C', 'answer_type': 'choice', 'choices': {'A': '1 and 2', 'B': '1 and 3', 'C': '2 and 3', 'D': '2 and 4', 'E': '1 and 4', 'F': '3 and 4'}}
        for key, value in attributes.items():
            setattr(self, key, value)
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = ROOT / 'scenes/Plane503.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def build_scene(self):
        return build_scene()

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        destination = Path(output_path) if output_path else ROOT.parents[1] / '.runtime/author_designed_redraw/Plane503.png'
        return _renderer().draw(self.scene_path, destination)

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)

if __name__ == '__main__':
    import sys
    print(Plane503().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
