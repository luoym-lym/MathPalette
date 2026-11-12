"""Frozen question Ana255; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana255:

    def __init__(self):
        self.id = 'Ana255'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3882'
        self.question = 'Use the unit grid to classify the relationship between the distinct lines AB and CD: parallel, perpendicular, or neither.'
        self.answer = 'parallel'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana255.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.line([[-7.5, -6.5], [6.5, 7.5]], id='object_000', solid_capstyle='butt')
            c.line([[-7.5, -3.5], [3.5, 7.5]], id='object_001', solid_capstyle='butt')
            for object_id, points in [('object_002', [[-5, -4]]), ('object_003', [[1, 2]]), ('object_004', [[-4, 0]]), ('object_005', [[2, 6]])]:
                c.point(points, id=object_id, filled=True)
            for object_id, text, anchor in [(None, 'A', [-5.25, -3.63]), (None, 'B', [0.75, 2.37]), (None, 'C', [-4.25, 0.37]), (None, 'D', [1.75, 6.37])]:
                c.text(text, anchor, id=object_id, ha='right', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana255().draw(sys.argv[1] if len(sys.argv) > 1 else None))
