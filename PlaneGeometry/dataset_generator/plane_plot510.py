"""Frozen question Plane510; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane510:

    def __init__(self):
        self.id = 'Plane510'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Plane517'
        self.question = 'The black dots shown lie on a triangular lattice. What is the smallest number of dots that must be removed so that no three remaining dots are vertices of an equilateral triangle? Count triangles of every size and orientation. The colored dashed lines are only markings; only black dots can be triangle vertices.'
        self.answer = '5'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane510.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.13447171824973303, 4.134471718249733], ylim=[-1.2684463144652944, 3.0004971220341714], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('dot01', [[0.0, 0.0]]), ('dot02', [[1.0, 0.0]]), ('dot03', [[2.0, 0.0]]), ('dot04', [[3.0, 0.0]]), ('dot05', [[0.5, 0.8660254037844386]]), ('dot06', [[1.5, 0.8660254037844386]]), ('dot07', [[2.5, 0.8660254037844386]]), ('dot08', [[3.5, 0.8660254037844386]]), ('dot09', [[1.0, 1.7320508075688772]]), ('dot10', [[2.0, 1.7320508075688772]]), ('dot11', [[3.0, 1.7320508075688772]]), ('dot12', [[4.0, 1.7320508075688772]])]:
                c.point(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane510().draw(sys.argv[1] if len(sys.argv) > 1 else None))
