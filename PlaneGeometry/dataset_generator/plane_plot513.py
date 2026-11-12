"""Frozen question Plane513; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane513:

    def __init__(self):
        self.id = 'Plane513'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane189/extension_02'
        self.question = 'Which numbers are written inside both the left circle and the right circle but outside the rectangle?\nChoices:\nA: 1 and 4\nB: 2 and 15\nC: 4 and 15\nD: 1 and 3\nE: 4, 5, and 15'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '1 and 4', 'B': '2 and 15', 'C': '4 and 15', 'D': '1 and 3', 'E': '4, 5, and 15'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane513.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.0232558139535, 10.0232558139535], ylim=[-0.0232558139535, 10.0232558139535], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([3.5, 5], 3.3, id='left_circle', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], joinstyle='round', fill=False)
            c.circle([6.5, 5], 3.3, id='right_circle', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], joinstyle='round', fill=False)
            c.path([[0.9, 3.7], [9.1, 3.7], [9.1, 6.3], [0.9, 6.3], [0.9, 3.7]], [1, 2, 2, 2, 79], id='rectangle', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', joinstyle='round', fill=False)
            for object_id, text, anchor in [(None, '1', [1.4, 3.2]), (None, '2', [7.9, 4.9]), (None, '3', [8.6, 3.2]), (None, '4', [5.0, 3.0]), (None, '5', [6.2, 7.8]), (None, '6', [2.1, 4.9]), (None, '7', [6.2, 5.7]), (None, '8', [8.6, 6.8]), (None, '9', [2.9, 2.7]), (None, '10', [1.7, 7.1]), (None, '11', [4.5, 5.0]), (None, '12', [3.8, 7.8]), (None, '13', [6.0, 4.2]), (None, '14', [7.1, 2.7]), (None, '15', [5.0, 7.1])]:
                c.text(text, anchor, id=object_id, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane513().draw(sys.argv[1] if len(sys.argv) > 1 else None))
