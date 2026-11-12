"""Frozen question Plane65; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane65:

    def __init__(self):
        self.id = 'Plane65'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/822'
        self.question = 'Find the perimeter of the parallelogram. Round to the nearest tenth if necessary.\nChoices:\nA: 22\nB: 40\nC: 44\nD: 48'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '22', 'B': '40', 'C': '44', 'D': '48'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane65.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.42436593748415596, 17.457569062484154], ylim=[-4.2126955594708475, 13.669239440497464], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment1', [[0.0, 0.0], [12.0, 0.0]]), ('segment2', [[12.0, 0.0], [17.0, 8.660254037844386]]), ('segment3', [[17.0, 8.660254037844386], [5.000000000000001, 8.660254037844386]]), ('segment4', [[5.000000000000001, 8.660254037844386], [0.0, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[0.574907889659475, 0.0], [0.574907889659475, 0.10090989965016366], [0.5483397871062882, 0.2000634082393573], [0.4978848372812064, 0.28745394482973746], [0.4474298874561246, 0.37484448142011767], [0.3748444814201177, 0.4474298874561245], [0.2874539448297376, 0.49788483728120636]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc5', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.line([[12.0, 0.0], [12.0, 8.660254037844386]], id='segment11', linestyle=(0, [4, 3]))
            c.line([[11.676614312066546, 0.0], [11.676614312066546, 0.3233856879334547]], id='right_angle12', zorder=3)
            c.line([[11.676614312066546, 0.3233856879334547], [12.0, 0.3233856879334547]], id='right_angle12', zorder=3)
            c.text('60°', [0.0, 0.0], id='anglelabel6', rotation_mode='default', offset_pt=[27.71281292110204, 16.0], annotation_clip=None)
            c.text('12 m', [11.0, 8.660254037844386], id='text15', rotation_mode='default', offset_pt=[0, 16], annotation_clip=None)
            c.text('10 m', [2.5000000000000004, 4.330127018922193], id='text17', rotation_mode='default', offset_pt=[-28, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane65().draw(sys.argv[1] if len(sys.argv) > 1 else None))
