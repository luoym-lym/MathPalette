"""Frozen question Plane56; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane56:

    def __init__(self):
        self.id = 'Plane56'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/737'
        self.question = 'Find the perimeter of the parallelogram.\nChoices:\nA: 32\nB: 39\nC: 46\nD: 78'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '32', 'B': '39', 'C': '46', 'D': '78'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane56.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.7737069181961314, 31.82846397884746], ylim=[-10.70994504201227, 21.89222585503132], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment1', [[0.0, 0.0], [23.0, 0.0]]), ('segment2', [[23.0, 0.0], [31.0, 13.856406460551018]]), ('segment3', [[31.0, 13.856406460551018], [8.000000000000002, 13.856406460551018]]), ('segment4', [[8.000000000000002, 13.856406460551018], [0.0, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[1.048166502605568, 0.0], [1.048166502605568, 0.1839779528112581], [0.999727795057939, 0.3647536704319797], [0.90773881865231, 0.5240832513027839], [0.8157498422466809, 0.6834128321735882], [0.6834128321735883, 0.8157498422466808], [0.5240832513027841, 0.9077388186523099]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc5', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.line([[8.000000000000002, 13.856406460551018], [8.000000000000002, 0.0]], id='segment11', linestyle=(0, [4, 3]))
            c.line([[7.41040634228437, 0.0], [7.41040634228437, 0.589593657715632]], id='right_angle12', zorder=3)
            c.line([[7.41040634228437, 0.589593657715632], [8.000000000000002, 0.589593657715632]], id='right_angle12', zorder=3)
            c.line([[0.0, -0.9782470323512077], [23.0, -0.9782470323512077]], id='protocol_dim0', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, -0.9782470323512077]], id='protocol_dim0_start')
            c.line([[23.0, 0.0], [23.0, -0.9782470323512077]], id='protocol_dim0_end')
            c.text('60°', [0.0, 0.0], id='anglelabel6', rotation_mode='default', offset_pt=[27.71281292110204, 16.0], annotation_clip=None)
            c.text('23 ft', [11.5, -0.9782470323512077], id='text15', rotation_mode='default', offset_pt=[0.0, -22.0], annotation_clip=None)
            c.text('16 ft', [27.0, 6.928203230275509], id='text17', rotation_mode='default', offset_pt=[28, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane56().draw(sys.argv[1] if len(sys.argv) > 1 else None))
