"""Frozen question Ana280; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana280:

    def __init__(self):
        self.id = 'Ana280'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/5409'
        self.question = 'The three straight graphs show velocity v against time t for cars a, b, and c. Which car has the greatest acceleration at t=2?'
        self.answer = 'c'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana280.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='t', ylabel='v') as c:
            for object_id, points in [('object_000', [[0, 1.5], [6, 4.5]]), ('object_001', [[0, 1], [6, 1]]), ('object_002', [[0, 2], [6, 6.5]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            for object_id, text, anchor in [(None, 'a', [6.3, 4.5]), (None, 'b', [6.3, 1]), (None, 'c', [6.3, 6.5])]:
                c.text(text, anchor, id=object_id, ha='left')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana280().draw(sys.argv[1] if len(sys.argv) > 1 else None))
