"""Frozen question Plane10; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane10:

    def __init__(self):
        self.id = 'Plane10'
        self.source_dataset = 'MathVerse'
        self.source_key = 's1784'
        self.question = '\\[Consider the following diagram:Find the size of \\angle ACD.\\]'
        self.answer = '35°'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane10.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.0098945313096621, 15.169047985582093], ylim=[-4.308344121588192, 11.870598395303563], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('AB', [[10.648976575756894, 0.0], [0.0, 0.0]]), ('BC', [[0.0, 0.0], [10.648976575756894, 7.456493672563599]]), ('AC', [[10.648976575756894, 0.0], [10.648976575756894, 7.456493672563599]]), ('CD', [[10.648976575756894, 7.456493672563599], [14.15238261627931, 2.453111318983227]]), ('DA', [[14.15238261627931, 2.453111318983227], [10.648976575756894, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('rightA', [[10.356388639615188, 0.0], [10.356388639615188, 0.29258793614170564]]), ('rightA', [[10.356388639615188, 0.29258793614170564], [10.648976575756894, 0.29258793614170564]]), ('rightC', [[10.40930256973212, 7.2886721268321315], [10.577124115463587, 7.048998120807356]]), ('rightC', [[10.577124115463587, 7.048998120807356], [10.816798121488361, 7.216819666538823]]), ('rightD', [[13.984561070547842, 2.6927853250080025], [13.744887064523068, 2.5249637792765354]]), ('rightD', [[13.744887064523068, 2.5249637792765354], [13.912708610254535, 2.28528977325176]])]:
                c.line(points, id=object_id, zorder=3)
            c.path([[0.5201563309185878, 0.0], [0.5201563309185878, 0.05306028186136628], [0.5120374443151054, 0.10580953513341952], [0.49608190983606126, 0.1564140253560832], [0.480126375357017, 0.2070185155787469], [0.45652124920364706, 0.25488497627643075], [0.4260871218218225, 0.29834941463371906]], [1, 4, 4, 4, 4, 4, 4], id='arc35', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('A', [10.648976575756894, 0.0], id='v_A', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0.0, -15.0], annotation_clip=None)
            c.text('B', [0.0, 0.0], id='v_B', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13.5, -13.5], annotation_clip=None)
            c.text('C', [10.648976575756894, 7.456493672563599], id='v_C', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0.0, 15.0], annotation_clip=None)
            c.text('D', [14.15238261627931, 2.453111318983227], id='v_D', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13.5, 0.0], annotation_clip=None)
            c.text('13', [5.324488287878447, 3.7282468362817993], id='BC13', rotation_mode='default', offset_pt=[-12.0, 13.333333333333332], annotation_clip=None)
            c.text('35°', [0.0, 0.0], id='given_B', rotation_mode='default', offset_pt=[46.90709311020858, 10.18452826350942], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane10().draw(sys.argv[1] if len(sys.argv) > 1 else None))
