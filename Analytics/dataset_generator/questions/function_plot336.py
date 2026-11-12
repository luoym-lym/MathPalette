"""Frozen question Ana336; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana336:

    def __init__(self):
        self.id = 'Ana336'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3849'
        self.question = 'Classify triangle ABC by its angles: acute, right, or obtuse. Read positions from the unit grid.'
        self.answer = 'right'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana336.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            for object_id, points in [('object_000', [[-2, -2]]), ('object_001', [[2, -2]]), ('object_002', [[-2, 2]])]:
                c.point(points, id=object_id, filled=True)
            c.line([[-2, -2], [2, -2], [-2, 2], [-2, -2]], id='object_003', solid_capstyle='butt')
            for object_id, text, anchor in [(None, 'A', [-1.78, -1.75]), (None, 'B', [2.22, -1.75]), (None, 'C', [-1.78, 2.25])]:
                c.text(text, anchor, id=object_id, ha='left', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana336().draw(sys.argv[1] if len(sys.argv) > 1 else None))
