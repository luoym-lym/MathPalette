"""Frozen question Plane497; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane497:

    def __init__(self):
        self.id = 'Plane497'
        self.source_dataset = 'Author Designed'
        self.source_key = 'authored-extension:Plane152:ext03'
        self.question = 'The entire unequal-step pattern shown is continued by repeating its full unit once more. Which labeled point lies on that continuation?\nChoices:\nA:A\nB:B'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B'}
        self.query = self.question
        self._geometry_01 = [('grid_v_0', [[-1.0, -0.5], [-1.0, 5.5]]),
         ('grid_v_1', [[0.0, -0.5], [0.0, 5.5]]),
         ('grid_v_2', [[1.0, -0.5], [1.0, 5.5]]),
         ('grid_v_3', [[2.0, -0.5], [2.0, 5.5]]),
         ('grid_v_4', [[3.0, -0.5], [3.0, 5.5]]),
         ('grid_v_5', [[4.0, -0.5], [4.0, 5.5]]),
         ('grid_v_6', [[5.0, -0.5], [5.0, 5.5]]),
         ('grid_v_7', [[6.0, -0.5], [6.0, 5.5]]),
         ('grid_v_8', [[7.0, -0.5], [7.0, 5.5]]),
         ('grid_v_9', [[8.0, -0.5], [8.0, 5.5]]),
         ('grid_v_10', [[9.0, -0.5], [9.0, 5.5]]),
         ('grid_v_11', [[10.0, -0.5], [10.0, 5.5]]),
         ('grid_v_12', [[11.0, -0.5], [11.0, 5.5]]),
         ('grid_v_13', [[12.0, -0.5], [12.0, 5.5]]),
         ('grid_v_14', [[13.0, -0.5], [13.0, 5.5]]),
         ('grid_v_15', [[14.0, -0.5], [14.0, 5.5]]),
         ('grid_v_16', [[15.0, -0.5], [15.0, 5.5]]),
         ('grid_v_17', [[16.0, -0.5], [16.0, 5.5]]),
         ('grid_v_18', [[17.0, -0.5], [17.0, 5.5]]),
         ('grid_v_19', [[18.0, -0.5], [18.0, 5.5]]),
         ('grid_v_20', [[19.0, -0.5], [19.0, 5.5]]),
         ('grid_v_21', [[20.0, -0.5], [20.0, 5.5]]),
         ('grid_v_22', [[21.0, -0.5], [21.0, 5.5]]),
         ('grid_v_23', [[22.0, -0.5], [22.0, 5.5]]),
         ('grid_v_24', [[23.0, -0.5], [23.0, 5.5]]),
         ('grid_v_25', [[24.0, -0.5], [24.0, 5.5]]),
         ('grid_v_26', [[25.0, -0.5], [25.0, 5.5]]),
         ('grid_v_27', [[26.0, -0.5], [26.0, 5.5]]),
         ('grid_v_28', [[27.0, -0.5], [27.0, 5.5]]),
         ('grid_v_29', [[28.0, -0.5], [28.0, 5.5]]),
         ('grid_v_30', [[29.0, -0.5], [29.0, 5.5]]),
         ('grid_v_31', [[30.0, -0.5], [30.0, 5.5]]),
         ('grid_v_32', [[31.0, -0.5], [31.0, 5.5]]),
         ('grid_h_0', [[-0.5, 0.0], [31.0, 0.0]]),
         ('grid_h_1', [[-0.5, 1.0], [31.0, 1.0]]),
         ('grid_h_2', [[-0.5, 2.0], [31.0, 2.0]]),
         ('grid_h_3', [[-0.5, 3.0], [31.0, 3.0]]),
         ('grid_h_4', [[-0.5, 4.0], [31.0, 4.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane497.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.722205988063724, 31.772842562137793], ylim=[-14.284649057032848, 19.21039949316867], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=1, color='#A8A8A8', linewidth=0.5)
            for object_id, points in [('pattern_1', [[0, 0], [0, 4]]), ('pattern_2', [[0, 4], [4, 4]]), ('pattern_3', [[4, 4], [4, 0]]), ('pattern_4', [[4, 0], [5, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_42', [[0.0, 0.0]]), ('corner_43', [[0.0, 4.0]]), ('corner_44', [[4.0, 4.0]]), ('corner_45', [[4.0, 0.0]]), ('corner_46', [[5.0, 0.0]])]:
                c.point(points, id=object_id, s=[24])
            for object_id, points in [('pattern_5', [[5, 0], [5, 2]]), ('pattern_6', [[5, 2], [7, 2]]), ('pattern_7', [[7, 2], [7, 0]]), ('pattern_8', [[7, 0], [8, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_51', [[5.0, 0.0]]), ('corner_52', [[5.0, 2.0]]), ('corner_53', [[7.0, 2.0]]), ('corner_54', [[7.0, 0.0]]), ('corner_55', [[8.0, 0.0]])]:
                c.point(points, id=object_id, s=[24])
            for object_id, points in [('pattern_9', [[8, 0], [8, 1]]), ('pattern_10', [[8, 1], [9, 1]]), ('pattern_11', [[9, 1], [9, 0]]), ('pattern_12', [[9, 0], [10, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_60', [[8.0, 0.0]]), ('corner_61', [[8.0, 1.0]]), ('corner_62', [[9.0, 1.0]]), ('corner_63', [[9.0, 0.0]]), ('corner_64', [[10.0, 0.0]])]:
                c.point(points, id=object_id, s=[24])
            for object_id, points in [('pattern_13', [[10, 0], [10, 4]]), ('pattern_14', [[10, 4], [14, 4]]), ('pattern_15', [[14, 4], [14, 0]]), ('pattern_16', [[14, 0], [15, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_69', [[10.0, 0.0]]), ('corner_70', [[10.0, 4.0]]), ('corner_71', [[14.0, 4.0]]), ('corner_72', [[14.0, 0.0]]), ('corner_73', [[15.0, 0.0]])]:
                c.point(points, id=object_id, s=[24])
            for object_id, points in [('pattern_17', [[15, 0], [15, 2]]), ('pattern_18', [[15, 2], [17, 2]]), ('pattern_19', [[17, 2], [17, 0]]), ('pattern_20', [[17, 0], [18, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_78', [[15.0, 0.0]]), ('corner_79', [[15.0, 2.0]]), ('corner_80', [[17.0, 2.0]]), ('corner_81', [[17.0, 0.0]]), ('corner_82', [[18.0, 0.0]])]:
                c.point(points, id=object_id, s=[24])
            for object_id, points in [('pattern_21', [[18, 0], [18, 1]]), ('pattern_22', [[18, 1], [19, 1]]), ('pattern_23', [[19, 1], [19, 0]]), ('pattern_24', [[19, 0], [20, 0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('corner_87', [[18.0, 0.0]]), ('corner_88', [[18.0, 1.0]]), ('corner_89', [[19.0, 1.0]]), ('corner_90', [[19.0, 0.0]]), ('corner_91', [[20.0, 0.0]])]:
                c.point(points, id=object_id, s=[24])
            c.line([[-0.5, 5.0], [31.0, 5.0]], id='grid_h_5', zorder=1, color='#A8A8A8', linewidth=0.5)
            c.point([[22.0, 2.0]], id='choice_A', s=[24])
            c.point([[27.0, 1.0]], id='choice_B', s=[24])
            c.text('A', [22, 2], clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            c.text('B', [27, 1], clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane497().draw(sys.argv[1] if len(sys.argv) > 1 else None))
