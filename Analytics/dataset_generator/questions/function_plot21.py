"""Frozen question Ana21; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana21:

    def __init__(self):
        self.id = 'Ana21'
        self.source_dataset = 'MathVerse'
        self.source_key = 's2164'
        self.question = 'Find the coordinates of the midpoint of the rectangle diagonals.'
        self.answer = '(2,2)'
        self.answer_type = 'expression'
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
            c.line([[-2, 6], [6, 6], [6, -2], [-2, -2], [-2, 6]], id='curve_001', solid_capstyle='projecting')
            return c if _canvas else c.save(output_path)

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana21().draw(sys.argv[1] if len(sys.argv) > 1 else None))
