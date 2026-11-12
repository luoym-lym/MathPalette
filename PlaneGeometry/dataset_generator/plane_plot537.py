"""Frozen question Plane537; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane537:

    def __init__(self):
        self.id = 'Plane537'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane177/extension_03'
        self.question = 'The billiard ball meets the board under $45^{\\circ}$ as shown. Which pocket will it fall into?\nChoices:\nA: Pocket A\nB: Pocket B\nC: Pocket C\nD: Pocket D\nE: Pocket E\nF: None of the pockets (the motion continues forever)'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'Pocket A', 'B': 'Pocket B', 'C': 'Pocket C', 'D': 'Pocket D', 'E': 'Pocket E', 'F': 'None of the pockets (the motion continues forever)'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane537.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.9, 12.9], ylim=[-2.9, 10.9], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 7.79]]), ('rail_right_0', [[12.0, 0.21], [12.0, 7.79]]), ('rail_bottom_0', [[0.21, 0.0], [5.79, 0.0]]), ('rail_bottom_1', [[6.21, 0.0], [11.79, 0.0]]), ('rail_top_0', [[0.21, 8.0], [11.79, 8.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 8.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 8.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 8.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 8.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 8.0]]), ('grid_v_6', [[6.0, 0.21], [6.0, 8.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 8.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 8.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 8.0]]), ('grid_v_10', [[10.0, 0.0], [10.0, 8.0]]), ('grid_v_11', [[11.0, 0.0], [11.0, 8.0]]), ('grid_h_1', [[0.0, 1.0], [12.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [12.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [12.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [12.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [12.0, 5.0]]), ('grid_h_6', [[0.0, 6.0], [12.0, 6.0]]), ('grid_h_7', [[0.0, 7.0], [12.0, 7.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [12, 0], 0.21), ('pocket_B', [12, 8], 0.21), ('pocket_C', [0, 8], 0.21), ('pocket_D', [0, 0], 0.21), ('pocket_E', [6.0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3, facecolor=[0.0, 0.0, 0.0, 0.0])
            c.line([[1.3, 0.7], [0.0, 2.0]], id='incoming_path')
            c.line([[0.0, 2.0], [2.7, 4.7]], id='outgoing_path')
            c.circle([1.3, 0.7], 0.09, id='ball_symbol', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0])
            c.path([[2.7, 4.7], [2.424228355, 4.551507576], [2.551507576, 4.424228355], [2.7, 4.7]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0], capstyle='butt')
            c.path([[0.3137240734431056, 2.3137240734431055], [0.2725262055890451, 2.354921941297166], [0.22361385343937426, 2.3876041301339623], [0.16978624506938783, 2.409900255550918], [0.1159586366994014, 2.432196380967874], [0.05826258346006693, 2.443672839506173], [2.7167126138492594e-17, 2.443672839506173]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.text('A', [12, 0], id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, -15], annotation_clip=False)
            c.text('B', [12, 8], id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 15], annotation_clip=False)
            c.text('C', [0, 8], id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, 15], annotation_clip=False)
            c.text('D', [0, 0], id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, -15], annotation_clip=False)
            c.text('E', [6.0, 0], id='label_E', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -20], annotation_clip=False)
            c.text('45°', [0, 2], id='angle_label', clip_on=True, rotation_mode='default', offset_pt=[17, 55], annotation_clip=False)
            c.text('P', [0, 2], id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-17, 0], annotation_clip=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane537().draw(sys.argv[1] if len(sys.argv) > 1 else None))
