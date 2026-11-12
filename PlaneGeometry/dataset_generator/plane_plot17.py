"""Frozen question Plane17; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane17:

    def __init__(self):
        self.id = 'Plane17'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/6'
        self.question = 'As shown in the figure, if CB = 4.0, DB = 7.0, and D is the midpoint of AC, then the length of AC is ()\nChoices:\nA: 6cm\nB: 7cm\nC: 4cm\nD: 5cm'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '6cm', 'B': '7cm', 'C': '4cm', 'D': '5cm'}
        self.query = self.question
        self.points = {'A': [0.0, 0.0], 'D': [3.0, 0.0], 'C': [6.0, 0.0], 'B': [10.0, 0.0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane17.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.40073898862842494, 10.364505870290245], ylim=[-5.5530335319908275, 5.212211326927843]) as c:
            for object_id, points in [('o1', [self.points['A']]), ('o2', [self.points['D']]), ('o3', [self.points['C']]), ('o4', [self.points['B']])]:
                c.point(points, id=object_id, filled=True)
            c.line([self.points['A'], self.points['B']], id='o5')
            for object_id, text, anchor in [('l1', 'A', self.points['A']), ('l2', 'D', self.points['D']), ('l3', 'C', self.points['C']), ('l4', 'B', self.points['B'])]:
                c.text(text, anchor, id=object_id, offset_pt=[0, -14], vertex=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane17().draw(sys.argv[1] if len(sys.argv) > 1 else None))
