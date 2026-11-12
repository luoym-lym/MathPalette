"""Frozen question Plane402; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane402:

    def __init__(self):
        self.id = 'Plane402'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1689'
        self.question = 'A rectangular strip of paper of dimensions $4 \\times 13$ is folded as shown in the diagram. Two rectangles are formed with areas $P$ and $Q$ where $P=2 Q$. What is the value of $x$?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane402.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.4534998113942716, 26.71565503370404], ylim=[-10.606278811438045, 17.562876033660263], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [13.0, 0.0], [13.0, 4.0], [0.0, 4.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[16.0, 0.0], [22.0, 0.0], [22.0, 4.0], [16.0, 4.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('o2', [[22.0, 4.0], [22.0, 7.0]]), ('o3', [[22.0, 7.0], [26.0, 7.0]]), ('o4', [[26.0, 7.0], [26.0, 4.0]]), ('o5', [[22.0, 0.0], [26.0, 4.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('o6', [[22.0, 4.0], [26.0, 4.0]]), ('o7', [[22.0, 0.0], [26.0, 0.0]]), ('o8', [[26.0, 0.0], [26.0, 4.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.path([[23.132055155490384, 0.0], [23.132055155490384, 0.14866012093859496], [23.10277235316804, 0.2958747094938349], [23.045882587831446, 0.43321875252965536], [22.988992822494858, 0.5705627955654758], [22.905602456732133, 0.6953652975167488], [22.800483877124442, 0.8004838771244416]], [1, 4, 4, 4, 4, 4, 4], id='o9', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.line([[16.0, 5.0], [22.0, 5.0]], id='o10', linestyle=(0.0, [4.0, 3.0]))
            c.line([[16.0, 4.0], [16.0, 5.0]], id='o11')
            c.line([[22.0, 4.0], [22.0, 5.0]], id='o12')
            for object_id, text, anchor in [('t0', '13', [6.5, 4.7]), ('t1', '4', [-0.6, 2.0]), ('t2', 'P', [19.0, 2.0]), ('t3', 'Q', [24.0, 5.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            c.text('45°', [22.0, 0.0], id='a45', rotation_mode='default', offset_pt=[31.411904105383748, 13.01123670041305], annotation_clip=None)
            c.text('x', [19.0, 5.7], id='t5', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane402().draw(sys.argv[1] if len(sys.argv) > 1 else None))
