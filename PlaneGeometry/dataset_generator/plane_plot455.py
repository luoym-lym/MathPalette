"""Frozen question Plane455; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane455:

    def __init__(self):
        self.id = 'Plane455'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2548'
        self.question = 'The $16$ squares on a piece of paper are numbered as shown in the diagram.  The paper is folded in half four times in the following sequence:\n\nfold the top half over the bottom half\nfold the bottom half over the top half\nfold the right half over the left half\nfold the left half over the right half.\n\nWhich numbered square is on top after step $4$?'
        self.answer = '9'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane455.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1006848411530239, 4.107928209374783], ylim=[-0.10792820937478131, 4.100684841153026]) as c:
            for object_id, points in [('o0', [[0, 0], [0, 4]]), ('o1', [[0, 0], [4, 0]]), ('o2', [[1, 0], [1, 4]]), ('o3', [[0, 1], [4, 1]]), ('o4', [[2, 0], [2, 4]]), ('o5', [[0, 2], [4, 2]]), ('o6', [[3, 0], [3, 4]]), ('o7', [[0, 3], [4, 3]]), ('o8', [[4, 0], [4, 4]]), ('o9', [[0, 4], [4, 4]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('t0', '1', [0.5, 3.5]), ('t1', '2', [1.5, 3.5]), ('t2', '3', [2.5, 3.5]), ('t3', '4', [3.5, 3.5]), ('t4', '5', [0.5, 2.5]), ('t5', '6', [1.5, 2.5]), ('t6', '7', [2.5, 2.5]), ('t7', '8', [3.5, 2.5]), ('t8', '9', [0.5, 1.5]), ('t9', '10', [1.5, 1.5]), ('t10', '11', [2.5, 1.5]), ('t11', '12', [3.5, 1.5]), ('t12', '13', [0.5, 0.5]), ('t13', '14', [1.5, 0.5]), ('t14', '15', [2.5, 0.5]), ('t15', '16', [3.5, 0.5])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, 0], vertex=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane455().draw(sys.argv[1] if len(sys.argv) > 1 else None))
