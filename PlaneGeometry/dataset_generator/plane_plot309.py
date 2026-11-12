"""Frozen question Plane309; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane309:

    def __init__(self):
        self.id = 'Plane309'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:962'
        self.question = 'The two-sided mirrors reflect laser beams as shown in the small picture. At which letter does the laser beam leave the larger diagram?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane309.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.6718030319034365, 5.0976061515201465], ylim=[-1.0874483246771285, 6.681960858746454], axes_position=[0.05, 0.050000000000000114, 0.9, 0.8999999999999998], coordinate_axes=False) as c:
            c.path([[0.5, 4.5], [2.5, 4.5], [2.5, 6.5], [0.5, 6.5], [0.5, 4.5]], [1, 2, 2, 2, 79], id='exampleframe', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('examplev0', [[1.0, 4.5], [1.0, 6.5]]), ('examplev1', [[2.0, 4.5], [2.0, 6.5]]), ('exampleh0', [[0.5, 5.0], [2.5, 5.0]]), ('exampleh1', [[0.5, 6.0], [2.5, 6.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('examplemirror01', [[0.8, 6.2], [1.2, 5.8]]), ('examplemirror11', [[1.8, 5.8], [2.2, 6.2]]), ('examplemirror00', [[0.8, 4.8], [1.2, 5.2]]), ('examplemirror10', [[1.8, 5.2], [2.2, 4.8]]), ('example_in', [[0.0, 6.0], [1.0, 6.0]])]:
                c.line(points, id=object_id)
            c.path([[1.0, 6.0], [0.85, 6.07], [0.85, 5.93], [1.0, 6.0]], [1, 2, 2, 79], id='example_inhead', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 6.0], [0.85, 6.07], [0.85, 5.93], [1.0, 6.0]], [1, 2, 2, 79], id='example_inhead', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[1.0, 6.0], [1.0, 5.45]], id='example_down')
            c.path([[1.0, 5.45], [1.07, 5.6000000000000005], [0.9299999999999999, 5.6000000000000005], [1.0, 5.45]], [1, 2, 2, 79], id='example_downhead', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 5.45], [1.07, 5.6000000000000005], [0.9299999999999999, 5.6000000000000005], [1.0, 5.45]], [1, 2, 2, 79], id='example_downhead', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[1.0, 5.45], [1.0, 5.0]], id='example_down_tail')
            c.line([[1.0, 5.0], [0.5, 5.0]], id='example_out')
            c.path([[0.5, 5.0], [0.65, 4.93], [0.65, 5.07], [0.5, 5.0]], [1, 2, 2, 79], id='example_outhead', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.5, 5.0], [0.65, 4.93], [0.65, 5.07], [0.5, 5.0]], [1, 2, 2, 79], id='example_outhead', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[0.5, 5.0], [0.0, 5.0]], id='example_out_tail')
            c.path([[-0.5, -0.5], [3.5, -0.5], [3.5, 2.5], [-0.5, 2.5], [-0.5, -0.5]], [1, 2, 2, 2, 79], id='mainframe', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('mainv0', [[0.0, -0.5], [0.0, 2.5]]), ('mainv1', [[1.0, -0.5], [1.0, 2.5]]), ('mainv2', [[2.0, -0.5], [2.0, 2.5]]), ('mainv3', [[3.0, -0.5], [3.0, 2.5]]), ('mainh0', [[-0.5, 0.0], [3.5, 0.0]]), ('mainh1', [[-0.5, 1.0], [3.5, 1.0]]), ('mainh2', [[-0.5, 2.0], [3.5, 2.0]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('mainmirror00', [[-0.2, 0.2], [0.2, -0.2]]), ('mainmirror10', [[0.8, -0.2], [1.2, 0.2]]), ('mainmirror20', [[1.8, -0.2], [2.2, 0.2]]), ('mainmirror30', [[2.8, -0.2], [3.2, 0.2]]), ('mainmirror01', [[-0.2, 0.8], [0.2, 1.2]]), ('mainmirror11', [[0.8, 0.8], [1.2, 1.2]]), ('mainmirror21', [[1.8, 0.8], [2.2, 1.2]]), ('mainmirror31', [[2.8, 0.8], [3.2, 1.2]]), ('mainmirror02', [[-0.2, 1.8], [0.2, 2.2]]), ('mainmirror12', [[0.8, 2.2], [1.2, 1.8]]), ('mainmirror22', [[1.8, 1.8], [2.2, 2.2]]), ('mainmirror32', [[2.8, 2.2], [3.2, 1.8]]), ('incoming', [[-1.5, 1.0], [-0.5, 1.0]])]:
                c.line(points, id=object_id)
            c.path([[-0.5, 1.0], [-0.65, 1.07], [-0.65, 0.9299999999999999], [-0.5, 1.0]], [1, 2, 2, 79], id='incominghead', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[-0.5, 1.0], [-0.65, 1.07], [-0.65, 0.9299999999999999], [-0.5, 1.0]], [1, 2, 2, 79], id='incominghead', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[-0.5, 1.0], [0.0, 1.0]], id='incoming_tail')
            for object_id, text, anchor in [('label0', 'A', [0.0, -0.85]), ('label1', 'B', [1.0, -0.85]), ('label2', 'C', [2.0, -0.85]), ('label3', 'D', [3.85, 1.0]), ('label4', 'E', [3.85, 2.0])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane309().draw(sys.argv[1] if len(sys.argv) > 1 else None))
