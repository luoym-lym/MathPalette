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
    return _renderer().render_scene(json.loads((ROOT / 'scenes/Plane498.json').read_text(encoding='utf-8')))

class Plane498:
    def __init__(self):
        attributes = {'id': 'Plane498', 'source_dataset': 'Author designed', 'source_key': 'authored-extension:Plane157:ext02', 'question': 'The floor of a rectangular room is covered completely with congruent rectangular tiles, as shown. The marked short side of one tile is 3 m. How long is the room in the direction indicated by the question mark? Give the length in metres.\nChoices:\nA:12\nB:15', 'answer': 'B', 'answer_type': 'choice', 'choices': {'A': '12', 'B': '15'}}
        for key, value in attributes.items():
            setattr(self, key, value)
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = ROOT / 'scenes/Plane498.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def build_scene(self):
        return build_scene()

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        destination = Path(output_path) if output_path else ROOT.parents[1] / '.runtime/author_designed_redraw/Plane498.png'
        return _renderer().draw(self.scene_path, destination)

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)

if __name__ == '__main__':
    import sys
    print(Plane498().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
