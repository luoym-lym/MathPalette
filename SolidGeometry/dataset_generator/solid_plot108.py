"""Frozen question Solid108; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid108:

    def __init__(self):
        self.id = 'Solid108'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:391'
        self.question = 'A regular tetrahedron has one marked face. This face is placed on the triangle labeled START. The tetrahedron is then rolled around an edge onto each successive adjacent triangle in the diagram. On which triangle does the marked face touch the diagram again for the first time?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid108.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.509582697579563, 3.1162445192849892], ylim=[-1.450219115500551, 3.175608101364001], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('netedge0', [[0.0, -2.220446049250313e-16], [1.0000000000000004, -2.220446049250313e-16]]), ('netedge1', [[1.0000000000000004, -2.220446049250313e-16], [0.5000000000000001, 0.8660254037844387]]), ('netedge2', [[0.5000000000000001, 0.8660254037844387], [0.0, -2.220446049250313e-16]]), ('netedge3', [[0.5000000000000001, 0.8660254037844387], [1.5, 0.8660254037844385]]), ('netedge4', [[1.5, 0.8660254037844385], [1.0000000000000004, -2.220446049250313e-16]]), ('netedge5', [[1.5, 0.8660254037844385], [1.0000000000000004, 1.7320508075688772]]), ('netedge6', [[1.0000000000000004, 1.7320508075688772], [0.5000000000000001, 0.8660254037844387]]), ('netedge7', [[1.0000000000000004, 1.7320508075688772], [2.0, 1.7320508075688772]]), ('netedge8', [[2.0, 1.7320508075688772], [1.5, 0.8660254037844385]]), ('netedge9', [[1.5, 0.8660254037844385], [2.5000000000000004, 0.8660254037844384]]), ('netedge10', [[2.5000000000000004, 0.8660254037844384], [2.0, 1.7320508075688772]]), ('netedge11', [[2.5000000000000004, 0.8660254037844384], [2.0, -2.220446049250313e-16]]), ('netedge12', [[2.0, -2.220446049250313e-16], [1.5, 0.8660254037844385]]), ('netedge13', [[2.0, -2.220446049250313e-16], [3.0, 0.0]]), ('netedge14', [[3.0, 0.0], [2.5000000000000004, 0.8660254037844384]]), ('tetraLB', [[-1.3999999999999997, 0.8600000000000001], [-0.6199999999999999, 0.38]]), ('tetraBR', [[-0.6199999999999999, 0.38], [-0.4000000000000001, 1.1799999999999997]]), ('tetraRT', [[-0.4000000000000001, 1.1799999999999997], [-0.82, 1.7199999999999998]]), ('tetraTL', [[-0.82, 1.7199999999999998], [-1.3999999999999997, 0.8600000000000001]]), ('tetraTB', [[-0.82, 1.7199999999999998], [-0.6199999999999999, 0.38]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-1.3999999999999997, 0.8600000000000001], [-0.4000000000000001, 1.1799999999999997]], id='tetraLR', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.path([[-1.3999999999999997, 0.8600000000000001], [-0.6199999999999999, 0.38], [-0.4000000000000001, 1.1799999999999997], [-1.3999999999999997, 0.8600000000000001]], [1, 2, 2, 79], id='marked_face', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, text, anchor in [('name0', 'START', [0.5000000000000001, 0.28867513459481264]), ('name2', 'A', [1.0, 1.1547005383792517]), ('name3', 'B', [1.5, 1.4433756729740645]), ('name4', 'C', [2.0000000000000004, 1.1547005383792515]), ('name5', 'D', [2.0, 0.577350269189626]), ('name6', 'E', [2.5000000000000004, 0.28867513459481264])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid108().draw(sys.argv[1] if len(sys.argv) > 1 else None))
