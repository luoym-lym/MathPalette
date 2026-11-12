"""Collected question Plane539; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane539:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self.id = 'Plane539'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane177/extension_05'
        self.question = 'The billiard ball meets the board under $45^{\\circ}$ as shown. Which pocket will it fall into?\nChoices:\nA: Pocket A\nB: Pocket B\nC: Pocket C\nD: Pocket D\nE: None of the pockets (the motion continues forever)'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'Pocket A', 'B': 'Pocket B', 'C': 'Pocket C', 'D': 'Pocket D', 'E': 'None of the pockets (the motion continues forever)'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.63358687, 8.6052304], ylim=[-1.59068696, 7.64813031], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[8.0, 0.21], [8.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [7.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [7.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [8.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [8.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [8.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [8.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [8.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [8, 0], 0.21), ('pocket_B', [8, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3, facecolor=[0.0, 0.0, 0.0, 0.0])
            c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
            c.line([[0.0, 3.0], [2.4, 5.4]], id='outgoing_path')
            c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0])
            c.path([[2.4, 5.4], [2.124228355, 5.251507576], [2.251507576, 5.124228355], [2.4, 5.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=[0.0, 0.0, 0.0, 1.0], capstyle='butt')
            c.path([[0.28879377957563435, 3.2887937795756343], [0.25086972791630474, 3.326717831234964], [0.20584422862895232, 3.3568029080204234], [0.15629406725281378, 3.3773272568801955], [0.10674390587667519, 3.3978516057399677], [0.053632708196761865, 3.4084160798048484], [2.5008272242665867e-17, 3.4084160798048484]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.text('A', [8, 0], id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, -15], annotation_clip=False)
            c.text('B', [8, 6], id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 15], annotation_clip=False)
            c.text('C', [0, 6], id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, 15], annotation_clip=False)
            c.text('D', [0, 0], id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, -15], annotation_clip=False)
            c.text('45°', [0, 3], id='angle_label', clip_on=True, rotation_mode='default', offset_pt=[15.3073373, 36.9551813], annotation_clip=False)
            c.text('P', [0, 3], id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-17, 0], annotation_clip=False)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane539_C01.png'
        with Canvas(PLANE, xlim=(-0.63358687, 8.6052304), ylim=(-1.59068696, 7.64813031), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[8.0, 0.21], [8.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [7.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [7.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [8.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [8.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [8.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [8.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [8.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [8, 0], 0.21), ('pocket_B', [8, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3)
            c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
            c.line([[0.0, 3.0], [2.4, 5.4]], id='outgoing_path')
            c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[2.4, 5.4], [2.124228355, 5.251507576], [2.251507576, 5.124228355], [2.4, 5.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
            c.path([[0.28879377957563435, 3.2887937795756343], [0.25086972791630474, 3.326717831234964], [0.20584422862895232, 3.3568029080204234], [0.15629406725281378, 3.3773272568801955], [0.10674390587667519, 3.3978516057399677], [0.053632708196761865, 3.4084160798048484], [2.5008272242665867e-17, 3.4084160798048484]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
            c.text('A', (8, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
            c.text('B', (8, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
            c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
            c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
            c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
            c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
            c.line([[0, 3], [3, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [8, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane539_C02.png'
        with Canvas(PLANE, xlim=(-0.63358687, 8.6052304), ylim=(-1.59068696, 7.64813031), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[8.0, 0.21], [8.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [7.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [7.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [8.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [8.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [8.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [8.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [8.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [8, 0], 0.21), ('pocket_B', [8, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3)
            c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
            c.line([[0.0, 3.0], [2.4, 5.4]], id='outgoing_path')
            c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[2.4, 5.4], [2.124228355, 5.251507576], [2.251507576, 5.124228355], [2.4, 5.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
            c.path([[0.28879377957563435, 3.2887937795756343], [0.25086972791630474, 3.326717831234964], [0.20584422862895232, 3.3568029080204234], [0.15629406725281378, 3.3773272568801955], [0.10674390587667519, 3.3978516057399677], [0.053632708196761865, 3.4084160798048484], [2.5008272242665867e-17, 3.4084160798048484]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
            c.text('A', (8, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
            c.text('B', (8, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
            c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
            c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
            c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
            c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
            c.line([[0, 3], [3, 6]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [8, 0]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane539_C03.png'
        with Canvas(PLANE, xlim=(-0.63358687, 8.6052304), ylim=(-1.59068696, 7.64813031), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[8.0, 0.21], [8.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [7.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [7.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [8.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [8.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [8.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [8.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [8.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [8, 0], 0.21), ('pocket_B', [8, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3)
            c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
            c.line([[0.0, 3.0], [2.4, 5.4]], id='outgoing_path')
            c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[2.4, 5.4], [2.124228355, 5.251507576], [2.251507576, 5.124228355], [2.4, 5.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
            c.path([[0.28879377957563435, 3.2887937795756343], [0.25086972791630474, 3.326717831234964], [0.20584422862895232, 3.3568029080204234], [0.15629406725281378, 3.3773272568801955], [0.10674390587667519, 3.3978516057399677], [0.053632708196761865, 3.4084160798048484], [2.5008272242665867e-17, 3.4084160798048484]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
            c.text('A', (8, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
            c.text('B', (8, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
            c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
            c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
            c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
            c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
            c.line([[0, 3], [3, 6]], zorder=9, color='#16A34A', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane539_C04.png'
        with Canvas(PLANE, xlim=(-0.63358687, 8.6052304), ylim=(-1.59068696, 7.64813031), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[8.0, 0.21], [8.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [7.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [7.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [8.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [8.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [8.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [8.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [8.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [8, 0], 0.21), ('pocket_B', [8, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3)
            c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
            c.line([[0.0, 3.0], [2.4, 5.4]], id='outgoing_path')
            c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[2.4, 5.4], [2.124228355, 5.251507576], [2.251507576, 5.124228355], [2.4, 5.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
            c.path([[0.28879377957563435, 3.2887937795756343], [0.25086972791630474, 3.326717831234964], [0.20584422862895232, 3.3568029080204234], [0.15629406725281378, 3.3773272568801955], [0.10674390587667519, 3.3978516057399677], [0.053632708196761865, 3.4084160798048484], [2.5008272242665867e-17, 3.4084160798048484]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
            c.text('A', (8, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
            c.text('B', (8, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
            c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
            c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
            c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
            c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
            c.line([[0, 3], [3, 6]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane539_C05.png'
        with Canvas(PLANE, xlim=(-0.63358687, 8.6052304), ylim=(-1.59068696, 7.64813031), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[8.0, 0.21], [8.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [7.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [7.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [8.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [8.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [8.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [8.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [8.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [8, 0], 0.21), ('pocket_B', [8, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3)
            c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
            c.line([[0.0, 3.0], [2.4, 5.4]], id='outgoing_path')
            c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[2.4, 5.4], [2.124228355, 5.251507576], [2.251507576, 5.124228355], [2.4, 5.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
            c.path([[0.28879377957563435, 3.2887937795756343], [0.25086972791630474, 3.326717831234964], [0.20584422862895232, 3.3568029080204234], [0.15629406725281378, 3.3773272568801955], [0.10674390587667519, 3.3978516057399677], [0.053632708196761865, 3.4084160798048484], [2.5008272242665867e-17, 3.4084160798048484]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
            c.text('A', (8, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
            c.text('B', (8, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
            c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
            c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
            c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
            c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
            c.line([[0, 3], [3, 6]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane539_C06.png'
        with Canvas(PLANE, xlim=(-0.63358687, 8.6052304), ylim=(-1.59068696, 7.64813031), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('rail_left_0', [[0.0, 0.21], [0.0, 5.79]]), ('rail_right_0', [[8.0, 0.21], [8.0, 5.79]]), ('rail_bottom_0', [[0.21, 0.0], [7.79, 0.0]]), ('rail_top_0', [[0.21, 6.0], [7.79, 6.0]]), ('grid_v_1', [[1.0, 0.0], [1.0, 6.0]]), ('grid_v_2', [[2.0, 0.0], [2.0, 6.0]]), ('grid_v_3', [[3.0, 0.0], [3.0, 6.0]]), ('grid_v_4', [[4.0, 0.0], [4.0, 6.0]]), ('grid_v_5', [[5.0, 0.0], [5.0, 6.0]]), ('grid_v_6', [[6.0, 0.0], [6.0, 6.0]]), ('grid_v_7', [[7.0, 0.0], [7.0, 6.0]]), ('grid_h_1', [[0.0, 1.0], [8.0, 1.0]]), ('grid_h_2', [[0.0, 2.0], [8.0, 2.0]]), ('grid_h_3', [[0.0, 3.0], [8.0, 3.0]]), ('grid_h_4', [[0.0, 4.0], [8.0, 4.0]]), ('grid_h_5', [[0.0, 5.0], [8.0, 5.0]])]:
                c.line(points, id=object_id)
            for object_id, center, radius in [('pocket_A', [8, 0], 0.21), ('pocket_B', [8, 6], 0.21), ('pocket_C', [0, 6], 0.21), ('pocket_D', [0, 0], 0.21)]:
                c.circle(center, radius, id=object_id, zorder=3)
            c.line([[1.5, 1.5], [0.0, 3.0]], id='incoming_path')
            c.line([[0.0, 3.0], [2.4, 5.4]], id='outgoing_path')
            c.circle([1.5, 1.5], 0.09, id='ball_symbol', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0))
            c.path([[2.4, 5.4], [2.124228355, 5.251507576], [2.251507576, 5.124228355], [2.4, 5.4]], [1, 2, 2, 79], id='outgoing_arrowhead', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
            c.path([[0.28879377957563435, 3.2887937795756343], [0.25086972791630474, 3.326717831234964], [0.20584422862895232, 3.3568029080204234], [0.15629406725281378, 3.3773272568801955], [0.10674390587667519, 3.3978516057399677], [0.053632708196761865, 3.4084160798048484], [2.5008272242665867e-17, 3.4084160798048484]], [1, 4, 4, 4, 4, 4, 4], id='incidence_arc', zorder=4, capstyle='butt', fill=False)
            c.text('A', (8, 0), id='label_A', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, -15), annotation_clip=False)
            c.text('B', (8, 6), id='label_B', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(16, 15), annotation_clip=False)
            c.text('C', (0, 6), id='label_C', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, 15), annotation_clip=False)
            c.text('D', (0, 0), id='label_D', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16, -15), annotation_clip=False)
            c.text('45°', (0, 3), id='angle_label', clip_on=True, rotation_mode='default', offset_pt=(15.3073373, 36.9551813), annotation_clip=False)
            c.text('P', (0, 3), id='label_P', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-17, 0), annotation_clip=False)
            c.line([[0, 3], [3, 6]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3, 6], [8, 0]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.point([[3.0, 6.0]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane539')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane539().draw(args.output, variant=args.variant))
