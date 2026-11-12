"""Frozen question Plane507; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane507:

    def __init__(self):
        self.id = 'Plane507'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Plane511'
        self.question = 'Six points are numbered as shown. Draw one triangle by connecting the three odd-numbered points, and a second triangle by connecting the three even-numbered points. Which choice shows the resulting two triangles? All choices preserve the source points’ relative positions and orientation.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane507.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[0.0, 8.0], ylim=[0.0, 8.0], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('source_dot1', [[3.0455, 7.166]]), ('source_dot2', [[4.0575, 7.6145]]), ('source_dot5', [[5.058, 6.9245]]), ('source_dot4', [[4.966, 5.7515]]), ('source_dot3', [[3.9195, 5.257]]), ('source_dot6', [[2.896, 6.0735]])]:
                c.point(points, id=object_id, zorder=3, linewidths=[0])
            c.line([[0.6611, 4.2512], [1.3915, 4.5749], [2.1136, 4.0769], [0.6611, 4.2512]], id='option0_0', solid_capstyle='projecting')
            c.line([[2.0472, 3.2303], [1.2919, 2.8734], [0.5532, 3.4627], [2.0472, 3.2303]], id='option0_1', solid_capstyle='projecting')
            for object_id, points in [('option0_dot0', [[0.6611, 4.2512]]), ('option0_dot1', [[1.3915, 4.5749]]), ('option0_dot2', [[2.1136, 4.0769]]), ('option0_dot3', [[2.0472, 3.2303]]), ('option0_dot4', [[1.2919, 2.8734]]), ('option0_dot5', [[0.5532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[3.3111, 4.2512], [4.0415, 4.5749], [4.6972, 3.2303], [3.3111, 4.2512]], id='option1_0', solid_capstyle='projecting')
            c.line([[4.7636, 4.0769], [3.9419, 2.8734], [3.2032, 3.4627], [4.7636, 4.0769]], id='option1_1', solid_capstyle='projecting')
            for object_id, points in [('option1_dot0', [[3.3111, 4.2512]]), ('option1_dot1', [[4.0415, 4.5749]]), ('option1_dot2', [[4.7636, 4.0769]]), ('option1_dot3', [[4.6972, 3.2303]]), ('option1_dot4', [[3.9419, 2.8734]]), ('option1_dot5', [[3.2032, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[5.9611, 4.2512], [7.4136, 4.0769], [6.5919, 2.8734], [5.9611, 4.2512]], id='option2_0', solid_capstyle='projecting')
            c.line([[6.6915, 4.5749], [7.3472, 3.2303], [5.8532, 3.4627], [6.6915, 4.5749]], id='option2_1', solid_capstyle='projecting')
            for object_id, points in [('option2_dot0', [[5.9611, 4.2512]]), ('option2_dot1', [[6.6915, 4.5749]]), ('option2_dot2', [[7.4136, 4.0769]]), ('option2_dot3', [[7.3472, 3.2303]]), ('option2_dot4', [[6.5919, 2.8734]]), ('option2_dot5', [[5.8532, 3.4627]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[1.9611, 1.9712], [2.6915, 2.2949], [2.5919, 0.5934], [1.9611, 1.9712]], id='option3_0', solid_capstyle='projecting')
            c.line([[3.4136, 1.7969], [3.3472, 0.9503], [1.8532, 1.1827], [3.4136, 1.7969]], id='option3_1', solid_capstyle='projecting')
            for object_id, points in [('option3_dot0', [[1.9611, 1.9712]]), ('option3_dot1', [[2.6915, 2.2949]]), ('option3_dot2', [[3.4136, 1.7969]]), ('option3_dot3', [[3.3472, 0.9503]]), ('option3_dot4', [[2.5919, 0.5934]]), ('option3_dot5', [[1.8532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[4.6611, 1.9712], [5.3915, 2.2949], [4.5532, 1.1827], [4.6611, 1.9712]], id='option4_0', solid_capstyle='projecting')
            c.line([[6.1136, 1.7969], [6.0472, 0.9503], [5.2919, 0.5934], [6.1136, 1.7969]], id='option4_1', solid_capstyle='projecting')
            for object_id, points in [('option4_dot0', [[4.6611, 1.9712]]), ('option4_dot1', [[5.3915, 2.2949]]), ('option4_dot2', [[6.1136, 1.7969]]), ('option4_dot3', [[6.0472, 0.9503]]), ('option4_dot4', [[5.2919, 0.5934]]), ('option4_dot5', [[4.5532, 1.1827]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            for object_id, text, anchor in [(None, '1', [2.80001, 7.3553]), (None, '2', [4.07253, 7.92414]), (None, '5', [5.33884, 7.05576]), (None, '4', [5.21968, 5.57332]), (None, '3', [3.89828, 4.94773]), (None, '6', [2.601, 5.97824]), (None, '(A)', [1.35, 2.6]), (None, '(B)', [4, 2.6]), (None, '(C)', [6.65, 2.6]), (None, '(D)', [2.65, 0.31999999999999984]), (None, '(E)', [5.35, 0.31999999999999984])]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane507().draw(sys.argv[1] if len(sys.argv) > 1 else None))
