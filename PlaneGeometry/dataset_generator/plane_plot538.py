"""Frozen question Plane538; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane538:

    def __init__(self):
        self.id = 'Plane538'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane177/extension_04'
        self.question = 'The billiard ball meets the board under an acute angle $\\theta$ with $\\tan\\theta=1/2$, as shown. Which pocket will it fall into?\nChoices:\nA: Pocket A\nB: Pocket B\nC: Pocket C\nD: Pocket D\nE: None of the pockets (the motion continues forever)'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Pocket A', 'B': 'Pocket B', 'C': 'Pocket C', 'D': 'Pocket D', 'E': 'None of the pockets (the motion continues forever)'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane538.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.79232376, 10.775252], ylim=[-1.80085964, 9.76671612], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 7.79]]), ('rail_right_0', [[10.0, 0.21], [10.0, 7.79]]), ('rail_bottom_0', [[0.21, 0.0], [9.79, 0.0]]), ('rail_top_0', [[0.21, 8.0], [9.79, 8.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 8.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 8.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 8.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 8.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 8.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 8.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 8.0]]), ('grid_v_8', [[8.0, 0.0], [8.0, 8.0]]), ('grid_v_9', [[9.0, 0.0], [9.0, 8.0]]), ('grid_h_1', [[0.0, 1.0], [10.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [10.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [10.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [10.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [10.0, 5.0]]), ('grid_h_6', [[0.0, 6.0], [10.0, 6.0]]), ('grid_h_7', [[0.0, 7.0], [10.0, 7.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [10, 0], 0.21), ('pocket_B', [10, 8], 0.21), ('pocket_C', [0, 8], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3, facecolor=[0.0, 0.0, 0.0, 0.0])
            c.line([[1.4, 1.3], [4.0, 0.0]], id='incoming_path')
            c.line([[4.0, 0.0], [6.8, 1.4]], id='outgoing_path')
            c.circle([1.4, 1.3], 0.09, id='ball_symbol', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0])
            c.path([[6.8, 1.4], [6.491422619, 1.346334369], [6.571921066, 1.185337474], [6.8, 1.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0], capstyle='butt')
            c.path([[4.51136241865998, 0.0], [4.51136241865998, 0.03955951733123343], [4.506771871854895, 0.07898574887883861], [4.497682957212599, 0.1174870091452927], [4.488594042570305, 0.1559882694117468], [4.4750680056869125, 0.19330511788859658], [4.4573764517049685, 0.2286882258524842]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.text('A', [10, 0], id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, -15], annotation_clip=False)
            c.text('B', [10, 8], id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 15], annotation_clip=False)
            c.text('C', [0, 8], id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, 15], annotation_clip=False)
            c.text('D', [0, 0], id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, -15], annotation_clip=False)
            c.text('θ', [4, 0], id='angle_label', clip_on=True, rotation_mode='default', offset_pt=[34, 9], annotation_clip=False)
            c.text('P', [4, 0], id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -20], annotation_clip=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane538().draw(sys.argv[1] if len(sys.argv) > 1 else None))
