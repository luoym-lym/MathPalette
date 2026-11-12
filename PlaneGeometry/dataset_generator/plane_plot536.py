"""Frozen question Plane536; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane536:

    def __init__(self):
        self.id = 'Plane536'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane177/extension_02'
        self.question = 'The billiard ball meets the board under $45^{\\circ}$ as shown. Which pocket will it fall into?\nChoices:\nA: Pocket A\nB: Pocket B\nC: Pocket C\nD: Pocket D\nE: None of the pockets (the motion continues forever)'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'Pocket A', 'B': 'Pocket B', 'C': 'Pocket C', 'D': 'Pocket D', 'E': 'None of the pockets (the motion continues forever)'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane536.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.79232376, 10.775252], ylim=[-2.69842908, 8.86914668], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [9.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 6.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3, facecolor=[0.0, 0.0, 0.0, 0.0])
            c.line([[0.7, 4.7], [2.0, 6.0]], id='incoming_path')
            c.line([[2.0, 6.0], [4.5, 3.5]], id='outgoing_path')
            c.circle([0.7, 4.7], 0.09, id='ball_symbol', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0])
            c.path([[4.5, 3.5], [4.351507576, 3.775771645], [4.224228355, 3.648492424], [4.5, 3.5]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0], capstyle='butt')
            c.path([[2.361587833878426, 5.638412166121574], [2.4090711131635296, 5.685895445406678], [2.446739506724172, 5.742270180279887], [2.472437272295423, 5.804310074444685], [2.4981350378666733, 5.866349968609483], [2.5113624186599797, 5.9328485024490565], [2.5113624186599797, 6.0]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.text('A', [10, 0], id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, -15], annotation_clip=False)
            c.text('B', [10, 6], id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 15], annotation_clip=False)
            c.text('C', [0, 6], id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, 15], annotation_clip=False)
            c.text('D', [0, 0], id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, -15], annotation_clip=False)
            c.text('45°', [2, 6], id='angle_label', clip_on=True, rotation_mode='default', offset_pt=[65, -17], annotation_clip=False)
            c.text('P', [2, 6], id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 19], annotation_clip=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane536().draw(sys.argv[1] if len(sys.argv) > 1 else None))
