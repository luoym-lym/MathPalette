"""Frozen question Plane454; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane454:

    def __init__(self):
        self.id = 'Plane454'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2544'
        self.question = 'How many different patterns can be made by shading exactly two of the nine squares? Patterns that can be matched by flips and/or turns are not considered different. For example, the patterns shown below are not considered different.'
        self.answer = '8'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane454.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.4461004190626472, 18.476069870638703], ylim=[-7.97605910318401, 10.946111186517342], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='c0_00', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[0.0, 1.0], [1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='c0_01', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='c0_02', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='c0_02', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='c0_10', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='c0_11', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='c0_12', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='c0_12', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('c0_20', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('c0_21', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79]), ('c0_22', [[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 1.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='c1_00', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[5.0, 0.0], [6.0, 0.0], [6.0, 1.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='c1_00', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[5.0, 1.0], [6.0, 1.0], [6.0, 2.0], [5.0, 2.0], [5.0, 1.0]], [1, 2, 2, 2, 79], id='c1_01', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[5.0, 2.0], [6.0, 2.0], [6.0, 3.0], [5.0, 3.0], [5.0, 2.0]], [1, 2, 2, 2, 79], id='c1_02', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='c1_10', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='c1_10', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('c1_11', [[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79]), ('c1_12', [[6.0, 2.0], [7.0, 2.0], [7.0, 3.0], [6.0, 3.0], [6.0, 2.0]], [1, 2, 2, 2, 79]), ('c1_20', [[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79]), ('c1_21', [[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79]), ('c1_22', [[7.0, 2.0], [8.0, 2.0], [8.0, 3.0], [7.0, 3.0], [7.0, 2.0]], [1, 2, 2, 2, 79]), ('c2_00', [[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79]), ('c2_01', [[10.0, 1.0], [11.0, 1.0], [11.0, 2.0], [10.0, 2.0], [10.0, 1.0]], [1, 2, 2, 2, 79]), ('c2_02', [[10.0, 2.0], [11.0, 2.0], [11.0, 3.0], [10.0, 3.0], [10.0, 2.0]], [1, 2, 2, 2, 79]), ('c2_10', [[11.0, 0.0], [12.0, 0.0], [12.0, 1.0], [11.0, 1.0], [11.0, 0.0]], [1, 2, 2, 2, 79]), ('c2_11', [[11.0, 1.0], [12.0, 1.0], [12.0, 2.0], [11.0, 2.0], [11.0, 1.0]], [1, 2, 2, 2, 79]), ('c2_12', [[11.0, 2.0], [12.0, 2.0], [12.0, 3.0], [11.0, 3.0], [11.0, 2.0]], [1, 2, 2, 2, 79]), ('c2_20', [[12.0, 0.0], [13.0, 0.0], [13.0, 1.0], [12.0, 1.0], [12.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [12.0, 1.0]], [1, 2, 2, 2, 79], id='c2_21', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 1.0], [13.0, 1.0], [13.0, 2.0], [12.0, 2.0], [12.0, 1.0]], [1, 2, 2, 2, 79], id='c2_21', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[12.0, 2.0], [13.0, 2.0], [13.0, 3.0], [12.0, 3.0], [12.0, 2.0]], [1, 2, 2, 2, 79], id='c2_22', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 2.0], [13.0, 2.0], [13.0, 3.0], [12.0, 3.0], [12.0, 2.0]], [1, 2, 2, 2, 79], id='c2_22', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[15.0, 0.0], [16.0, 0.0], [16.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='c3_00', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79], id='c3_01', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[15.0, 1.0], [16.0, 1.0], [16.0, 2.0], [15.0, 2.0], [15.0, 1.0]], [1, 2, 2, 2, 79], id='c3_01', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[15.0, 2.0], [16.0, 2.0], [16.0, 3.0], [15.0, 3.0], [15.0, 2.0]], [1, 2, 2, 2, 79], id='c3_02', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[15.0, 2.0], [16.0, 2.0], [16.0, 3.0], [15.0, 3.0], [15.0, 2.0]], [1, 2, 2, 2, 79], id='c3_02', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, vertices, codes in [('c3_10', [[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79]), ('c3_11', [[16.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 2, 79]), ('c3_12', [[16.0, 2.0], [17.0, 2.0], [17.0, 3.0], [16.0, 3.0], [16.0, 2.0]], [1, 2, 2, 2, 79]), ('c3_20', [[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79]), ('c3_21', [[17.0, 1.0], [18.0, 1.0], [18.0, 2.0], [17.0, 2.0], [17.0, 1.0]], [1, 2, 2, 2, 79]), ('c3_22', [[17.0, 2.0], [18.0, 2.0], [18.0, 3.0], [17.0, 3.0], [17.0, 2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane454().draw(sys.argv[1] if len(sys.argv) > 1 else None))
