"""Frozen We-Math spatial original, admitted under explicit user batch permission."""
from pathlib import Path
import json
import importlib.util
import platform
import sys
import numpy as np
import matplotlib
from matplotlib import ft2font
import PIL
_HELPERS = Path(__file__).resolve().parent
_RENDERER = _HELPERS / "wemath_renderers" / 'd3157feec547354e32e1f74cc258e481a7886a62c87cc4de2086d3353b67e3e2' / "common_renderer.py"
_SPEC = importlib.util.spec_from_file_location("_wemath_frozen_Solid326", _RENDERER)
_RENDER = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_RENDER)
_SCENE_PATH = _HELPERS / "scenes" / "Solid326.json"

class Solid326:
    def __init__(self):
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3978'
        self.question = 'The rectangle indicates a cutting plane that does not pass through the vertex of a right circular cone. Using the spatial relationships shown, classify the complete conic formed by continuing the intersection beyond the display rims. Answer circle, ellipse, parabola, or hyperbola.'
        self.answer = 'parabola'
        self.answer_type = 'text'
        self.id = 'Solid326'
        self.query = 'The rectangle indicates a cutting plane that does not pass through the vertex of a right circular cone. Using the spatial relationships shown, classify the complete conic formed by continuing the intersection beyond the display rims. Answer circle, ellipse, parabola, or hyperbola.'
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = str(_SCENE_PATH)

    def get_scene(self):
        return json.loads(_SCENE_PATH.read_text(encoding="utf-8"))

    def build_scene(self):
        fig, _ = _RENDER.render_scene(self.get_scene())
        return fig, fig.axes[0]

    def draw(self, num=0, output_path=None):
        actual = (platform.python_version(), np.__version__, matplotlib.__version__, PIL.__version__, ft2font.__freetype_version__)
        if actual != ("3.13.9", "2.5.3", "3.11.2", "12.3.0", "2.14.3"):
            raise RuntimeError(f"Frozen rendering environment required; got {actual}")
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        target = Path(output_path).resolve() if output_path else _HELPERS.parents[1] / ".runtime" / "reproduced" / "SolidGeometry" / f"{self.id}.png"
        if target.is_relative_to(_HELPERS.parent):
            raise ValueError("Render outside formal source directories")
        return _RENDER.draw(_SCENE_PATH, target)

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)

def draw(num=0, output_path=None):
    return Solid326().draw(num=num, output_path=output_path)

if __name__ == "__main__":
    print(draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
