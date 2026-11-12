"""Frozen question Solid249; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid249:

    def __init__(self):
        self.id = 'Solid249'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid249'
        self.question = 'A square sheet occupies -4 ≤ x ≤ 4, -4 ≤ y ≤ 4. It was folded once in half along one of the lines listed below, and two small circular holes were punched through both layers at distinct points away from the fold. The sheet is completely unfolded and shown. Which line was the fold?\nA: x=0\nB: y=0\nC: y=x\nD: y=-x\nE: x=1'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'x=0', 'B': 'y=0', 'C': 'y=x', 'D': 'y=-x', 'E': 'x=1'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid249.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-5.0, 5.0], ylim=[-5.0, 5.0], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('bottom', [[-4, -4], [4, -4]]), ('right', [[4, -4], [4, 4]]), ('top', [[4, 4], [-4, 4]]), ('left', [[-4, 4], [-4, -4]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('hole0', [-2, 1], 0.14), ('hole1', [2, 1], 0.14), ('hole2', [-1, -2], 0.14), ('hole3', [1, -2], 0.14)]:
                c.circle(center, radius, id=object_id, zorder=1, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid249().draw(sys.argv[1] if len(sys.argv) > 1 else None))
