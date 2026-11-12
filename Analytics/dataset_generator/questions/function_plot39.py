"""Frozen question Ana39; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana39:

    def __init__(self):
        self.id = 'Ana39'
        self.source_dataset = 'MathVerse'
        self.source_key = 's2789'
        self.question = '\\[What is the domain of h?\nChoices:\nA:-5 \\leq x \\leq 7\nB:-5 \\leq x \\leq 4\nC:-5 \\leq x \\leq 5\nD:-5 \\leq x \\leq 6\\]'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '-5 \\leq x \\leq 7', 'B': '-5 \\leq x \\leq 4', 'C': '-5 \\leq x \\leq 5', 'D': '-5 \\leq x \\leq 6'}
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8.0, 8.0], ylim=[-8.0, 8.0], axes_position=[0.12, 0.12, 0.8, 0.8], coordinate_axes=True) as c:
            c.line([[-5.0, 4.0], [-3.0, 3.0], [0.0, 7.0], [3.0, 1.0], [4.0, -5.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-5.0, 4.0], [4.0, -5.0]], id='point_001')
            c.text('h', [2, 1.8], id='text_001', rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana39().draw(sys.argv[1] if len(sys.argv) > 1 else None))
