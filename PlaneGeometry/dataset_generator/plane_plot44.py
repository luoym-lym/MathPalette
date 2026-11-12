"""Frozen question Plane44; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane44:

    def __init__(self):
        self.id = 'Plane44'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/408'
        self.question = 'Find z.\nChoices:\nA: 6\nB: 6 \\sqrt { 2 }\nC: 6 \\sqrt { 3 }\nD: 6 \\sqrt { 5 }'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '6', 'B': '6 \\sqrt { 2 }', 'C': '6 \\sqrt { 3 }', 'D': '6 \\sqrt { 5 }'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane44.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.0053056346200648, 13.985566040622267], ylim=[-4.184164534085818, 10.806707141156513], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 6.708203932499369], [0.0, 0.0], [13.416407864998739, 0.0], [0.0, 6.708203932499369]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.0], [2.6832815729997477, 5.366563145999495]], id='o2')
            for object_id, points in [('o3', [[0.0, 0.27110228000655257], [0.27110228000655257, 0.27110228000655257]]), ('o3', [[0.27110228000655257, 0.27110228000655257], [0.27110228000655257, 0.0]]), ('o5', [[2.4408003222198142, 5.487803771389462], [2.3195596968298475, 5.245322520609529]]), ('o5', [[2.3195596968298475, 5.245322520609529], [2.562040947609781, 5.124081895219562]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[0.1975328229839187, 7.103269578467207], [2.8808143959836663, 5.761628791967333]], id='protocol_dim0', linestyle=(0, [4, 3]))
            c.line([[0.0, 6.708203932499369], [0.1975328229839187, 7.103269578467207]], id='protocol_dim0_start')
            c.line([[2.6832815729997477, 5.366563145999495], [2.8808143959836663, 5.761628791967333]], id='protocol_dim0_end')
            c.line([[2.8808143959836663, 5.761628791967333], [13.613940687982657, 0.3950656459678373]], id='protocol_dim1', linestyle=(0, [4, 3]))
            c.line([[2.6832815729997477, 5.366563145999495], [2.8808143959836663, 5.761628791967333]], id='protocol_dim1_start')
            c.line([[13.416407864998739, 0.0], [13.613940687982657, 0.3950656459678373]], id='protocol_dim1_end')
            c.text('3', [1.5391736094837924, 6.43244918521727], id='t8', rotation_mode='default', offset_pt=[9.838699100999078, 19.677398201998148], annotation_clip=None)
            c.text('12', [8.24737754198316, 3.078347218967585], id='t10', rotation_mode='default', offset_pt=[9.838699100999074, 19.677398201998148], annotation_clip=None)
            c.text('x', [1.3416407864998738, 2.6832815729997477], id='t12', rotation_mode='default', offset_pt=[15, -1], annotation_clip=None)
            c.text('y', [0.0, 3.3541019662496847], id='t14', rotation_mode='default', offset_pt=[-17, 0], annotation_clip=None)
            c.text('z', [6.708203932499369, 0.0], id='t16', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane44().draw(sys.argv[1] if len(sys.argv) > 1 else None))
