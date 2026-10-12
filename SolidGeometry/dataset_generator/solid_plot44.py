"""Frozen-scene redraw using the canonical SolidGeometry renderer."""
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parent

def _renderer():
    spec = importlib.util.spec_from_file_location("_solid_question_renderer", ROOT / "common_renderer.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def build_scene():
    scene = json.loads((ROOT / "scenes" / "Solid44.json").read_text(encoding="utf-8"))
    fig, _ = _renderer().render_scene(scene)
    return fig, fig.axes[0]

class Solid44:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'Find the volume of the sphere figure shown.\n\nRound your answer to two decimal places.', 'answer': '113.10 cm³', 'answer_type': 'number', 'subject': 'SolidGeometry', 'id': 'Solid44'})
        self.query = self.question
        self.level = None
        self.scene_path = ROOT / "scenes" / "Solid44.json"

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))

    def build_scene(self):
        return build_scene()

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        destination = Path(output_path) if output_path else ROOT.parents[1] / ".runtime" / "mathverse_redraw" / "Solid44.png"
        return _renderer().draw(self.scene_path, destination)

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)

if __name__ == "__main__":
    import sys
    print(Solid44().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
