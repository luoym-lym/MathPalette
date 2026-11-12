"""Frozen question Ana559; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana559:

    def __init__(self):
        self.id = 'Ana559'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author_special20_20261111/Ana559'
        self.question = 'Read the unit grid. Vectors AB and CD are directed from A to B and from C to D, respectively. Find the Cartesian components of AB-CD.'
        self.answer = '(1, 3)'
        self.answer_type = 'expression'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana559.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.line([[-5, -3], [-2, 1]], id='object_000', solid_capstyle='butt')
            c.line([[1, -3], [3, -2]], id='object_001', solid_capstyle='butt')
            for object_id, points in [('object_002', [[-5, -3]]), ('object_003', [[-2, 1]]), ('object_004', [[1, -3]]), ('object_005', [[3, -2]])]:
                c.point(points, id=object_id, filled=True)
            for object_id, text, anchor in [(None, 'A', [-5.4, -3.4]), (None, 'B', [-2.4, 1.4]), (None, 'C', [0.7, -3.5]), (None, 'D', [3.45, -2.1])]:
                c.text(text, anchor, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana559().draw(sys.argv[1] if len(sys.argv) > 1 else None))
