"""Frozen question Ana49; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana49:

    def __init__(self):
        self.id = 'Ana49'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:2364'
        self.question = 'A cake maker has rectangular boxes. She often receives orders for cakes in the shape of an ellipse, and wants to determine the largest possible cake that can be made to fit inside the rectangular box.\n\nState the coordinates of the center of the cake in the form $(a, b)$.'
        self.answer = '(4,2)'
        self.answer_type = 'expression'
        self.query = self.question
        self._geometry_01 = [[4.0, 0.0],
         [5.0608124, 0.0],
         [6.078319483139413, 0.21073261682351663],
         [6.82842712474619, 0.5857864376269049],
         [7.578534766352966, 0.9608402584302931],
         [8.0, 1.4695938],
         [8.0, 2.0],
         [8.0, 2.5304062],
         [7.578534766352966, 3.0391597415697067],
         [6.82842712474619, 3.414213562373095],
         [6.078319483139413, 3.789267383176483],
         [5.0608124, 4.0],
         [4.0, 4.0],
         [2.9391876, 4.0],
         [1.9216805168605862, 3.789267383176483],
         [1.1715728752538097, 3.414213562373095],
         [0.42146523364703325, 3.0391597415697067],
         [0.0, 2.5304062],
         [0.0, 2.0],
         [0.0, 1.4695938],
         [0.42146523364703325, 0.9608402584302931],
         [1.1715728752538097, 0.5857864376269049],
         [1.9216805168605862, 0.21073261682351663],
         [2.9391876, 0.0],
         [4.0, 0.0],
         [4.0, 0.0]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana49.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8.0, 8.0], ylim=[-8.0, 8.0], axes_position=[0.12, 0.12, 0.8, 0.8], coordinate_axes=True) as c:
            c.line([[0.0, 0.0], [8.0, 0.0], [8.0, 4.0], [0.0, 4.0], [0.0, 0.0]], id='curve_001', solid_capstyle='butt')
            c.path(self._geometry_01, self._geometry_02, id='curve_002', alpha=1.0, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana49().draw(sys.argv[1] if len(sys.argv) > 1 else None))
