"""Frozen question Ana275; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana275:

    def __init__(self):
        self.id = 'Ana275'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3904'
        self.question = 'Read the unit grid. Line n is BP and line m is BC. A line l parallel to m meets n at A, and P is the midpoint of AB. Find an equation of l.'
        self.answer = 'y=4'
        self.answer_type = 'expression'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana275.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8, 8], ylim=[-8, 8], xlabel='x', ylabel='y') as c:
            c.line([[-7.5, -2.0], [7.5, -2.0]], id='object_000', solid_capstyle='butt')
            c.line([[-7.5, -5.375], [7.5, 5.875]], id='object_001', solid_capstyle='butt')
            for object_id, points in [('object_002', [[-3, -2]]), ('object_003', [[3, -2]]), ('object_004', [[1, 1]])]:
                c.point(points, id=object_id, filled=True)
            c.text('B', [-3.25, -1.63], ha='right', va='bottom')
            c.text('C', [3.23, -1.63], ha='left', va='bottom')
            c.text('P', [0.75, 1.37], ha='right', va='bottom')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana275().draw(sys.argv[1] if len(sys.argv) > 1 else None))
