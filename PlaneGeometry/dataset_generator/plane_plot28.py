"""Frozen question Plane28; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane28:

    def __init__(self):
        self.id = 'Plane28'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/206'
        self.question = "Find the scale factor from $Q$ to $Q'$.\nChoices:\nA: 2\nB: 3\nC: 4\nD: 5"
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '2', 'B': '3', 'C': '4', 'D': '5'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane28.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-24.365726613809485, 1.6445944784264643], ylim=[-6.453977123679971, 19.55634396855598], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.point([[0.0, 0.0]], id='o1')
            c.path([[-5.0, 0.0], [-7.2, 2.8], [-4.5, 5.2], [-0.3, 4.0], [-5.0, 0.0]], [1, 2, 2, 2, 79], id='o2', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[-15.0, 0.0], [-21.6, 8.399999999999999], [-13.5, 15.600000000000001], [-0.8999999999999999, 12.0], [-15.0, 0.0]], [1, 2, 2, 2, 79], id='o3', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.0], [-16.5, 0.0]], id='o4', linestyle=(0, [4, 3]))
            c.line([[-16.05, -0.18000000000000002], [-16.5, 0.0]], id='o5')
            c.line([[-16.05, 0.18000000000000002], [-16.5, 0.0]], id='o6')
            c.line([[0.0, 0.0], [-23.759999999999998, 9.239999999999998]], id='o7', linestyle=(0, [4, 3]))
            c.line([[-23.405838224814307, 8.909138341602839], [-23.759999999999998, 9.239999999999998]], id='o8')
            c.line([[-23.275357570798523, 9.244660023357705], [-23.759999999999998, 9.239999999999998]], id='o9')
            c.line([[0.0, 0.0], [-14.85, 17.16]], id='o10', linestyle=(0, [4, 3]))
            c.line([[-14.691640827845777, 16.70193627889274], [-14.85, 17.16]], id='o11')
            c.line([[-14.419420102159176, 16.93751190689076], [-14.85, 17.16]], id='o12')
            c.line([[0.0, 0.0], [-0.9899999999999999, 13.2]], id='o13', linestyle=(0, [4, 3]))
            c.line([[-1.1358403990711867, 12.7377981198667], [-0.9899999999999999, 13.2]], id='o14')
            c.line([[-0.7768486475113423, 12.764722501233688], [-0.9899999999999999, 13.2]], id='o15')
            c.line([[-15.0, -1.7], [-5.0, -1.7]], id='o16', linestyle=(0, [4, 3]))
            c.line([[-15.0, 0.0], [-15.0, -1.7]], id='o17')
            c.line([[-5.0, 0.0], [-5.0, -1.7]], id='o18')
            c.line([[-5.0, -1.7], [0.0, -1.7]], id='o19', linestyle=(0, [4, 3]))
            c.line([[-5.0, 0.0], [-5.0, -1.7]], id='o20')
            c.line([[0.0, 0.0], [0.0, -1.7]], id='o21')
            c.line([[-15.0, -3.1], [0.0, -3.1]], id='o22', linestyle=(0, [4, 3]))
            c.line([[-15.0, 0.0], [-15.0, -3.1]], id='o23')
            c.line([[0.0, 0.0], [0.0, -3.1]], id='o24')
            c.text('C', [0.0, 0.0], id='l1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13, -5], annotation_clip=None)
            c.text('Q', [-5.0, 0.0], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13, -11], annotation_clip=None)
            c.text('Q′', [-15.0, 0.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, -27], annotation_clip=None)
            for object_id, text, anchor in [('l4', 'x', [-10.0, -1.7]), ('l5', '5', [-2.5, -1.7]), ('l6', '15', [-7.5, -3.1])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane28().draw(sys.argv[1] if len(sys.argv) > 1 else None))
