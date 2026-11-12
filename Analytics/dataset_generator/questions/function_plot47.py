"""Frozen question Ana47; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana47:

    def __init__(self):
        self.id = 'Ana47'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:2169'
        self.question = 'Determine the equation of the graph.'
        self.answer = 'x²/36+y²/4=1'
        self.answer_type = 'expression'
        self.query = self.question
        self._geometry_01 = [[0.0, -2.0],
         [1.5912186000000001, -2.0],
         [3.117479224709121, -1.7892673831764834],
         [4.242640687119286, -1.4142135623730951],
         [5.36780214952945, -1.039159741569707],
         [6.0, -0.5304062],
         [6.0, 0.0],
         [6.0, 0.5304062],
         [5.36780214952945, 1.039159741569707],
         [4.242640687119286, 1.4142135623730951],
         [3.117479224709121, 1.7892673831764834],
         [1.5912186000000001, 2.0],
         [0.0, 2.0],
         [-1.5912186000000001, 2.0],
         [-3.117479224709121, 1.7892673831764834],
         [-4.242640687119286, 1.4142135623730951],
         [-5.36780214952945, 1.039159741569707],
         [-6.0, 0.5304062],
         [-6.0, 0.0],
         [-6.0, -0.5304062],
         [-5.36780214952945, -1.039159741569707],
         [-4.242640687119286, -1.4142135623730951],
         [-3.117479224709121, -1.7892673831764834],
         [-1.5912186000000001, -2.0],
         [0.0, -2.0],
         [0.0, -2.0]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana47.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8.0, 8.0], ylim=[-8.0, 8.0], axes_position=[0.12, 0.12, 0.8, 0.8], coordinate_axes=True) as c:
            c.path(self._geometry_01, self._geometry_02, id='curve_001', alpha=1.0, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana47().draw(sys.argv[1] if len(sys.argv) > 1 else None))
