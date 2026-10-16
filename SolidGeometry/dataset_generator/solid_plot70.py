"""Frozen original Solid70; redraw with the canonical solid renderer."""
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parent


def _renderer():
    spec = importlib.util.spec_from_file_location("_solid70_renderer", ROOT / "common_renderer.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_scene():
    scene = json.loads((ROOT / "scenes" / "Solid70.json").read_text(encoding="utf-8"))
    fig, _ = _renderer().render_scene(scene)
    return fig, fig.axes[0]


class Solid70:
    def __init__(self):
        self.__dict__.update({'id': 'Solid70', 'source_dataset': 'Author designed', 'question': 'The pyramid shown has a square base and volume 480. Each marked point is the midpoint of the edge on which it lies. Find the volume of the part containing vertex A after the pyramid is cut along the shaded plane.', 'answer': 60, 'answer_type': 'number', 'subject': 'SolidGeometry'})
        self.query = self.question
        self.level = None
        self.scene_path = ROOT / "scenes" / "Solid70.json"

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))

    def build_scene(self):
        return build_scene()

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        target = Path(output_path) if output_path else ROOT.parents[1] / ".runtime" / "reproduced" / "SolidGeometry" / "Solid70.png"
        return _renderer().draw(self.scene_path, target)

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)


if __name__ == "__main__":
    import sys
    print(Solid70().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
