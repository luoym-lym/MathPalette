"""Frozen question Plane512; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane512:

    def __init__(self):
        self.id = 'Plane512'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane189/extension_01'
        self.question = 'Which numbers are written inside both the rectangle and the circle but outside the triangle?\nChoices:\nA: 3 and 10\nB: 1 and 3\nC: 2 and 10\nD: 1 and 4\nE: 3, 5, and 10'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '3 and 10', 'B': '1 and 3', 'C': '2 and 10', 'D': '1 and 4', 'E': '3, 5, and 10'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane512.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.0232558139535, 10.0232558139535], ylim=[0.3267441860465, 10.3732558139535], axes_position=[0.05, 0.050000000000000114, 0.9, 0.8999999999999998], coordinate_axes=False) as c:
            c.path([[0.2, 3.2], [9.8, 3.2], [9.8, 6.8], [0.2, 6.8], [0.2, 3.2]], [1, 2, 2, 2, 79], id='rectangle', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', joinstyle='round', fill=False)
            c.circle([5, 5], 4.1, id='circle', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], joinstyle='round', fill=False)
            c.path([[0.9, 0.9], [9.1, 0.9], [5.0, 9.8], [0.9, 0.9]], [1, 2, 2, 79], id='triangle', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', joinstyle='round', fill=False)
            for object_id, text, anchor in [(None, '1', [4.8, 5.0]), (None, '2', [4.3, 2.1]), (None, '3', [8.0, 5.7]), (None, '4', [3.0, 7.6]), (None, '5', [6.6, 4.5]), (None, '6', [6.1, 6.2]), (None, '7', [6.5, 2.7]), (None, '8', [7.7, 7.3]), (None, '9', [2.9, 2.7]), (None, '10', [1.4, 5.2]), (None, '11', [4.8, 7.3]), (None, '12', [8.3, 1.4]), (None, '13', [3.1, 4.5]), (None, '14', [6.2, 8.4]), (None, '15', [1.9, 1.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane512().draw(sys.argv[1] if len(sys.argv) > 1 else None))
