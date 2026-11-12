"""Collected question Plane555; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane555:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self.id = 'Plane555'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane236/extension_01'
        self.question = 'If a laser beam hits a mirror it changes its direction as shown. Each solid mirror has mirrored sides on both sides; dashed lines do not reflect. At which letter does the laser beam end?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.8406572712600444, 4.331849554748036), ylim=(-0.5701048804875137, 4.602401945520566), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 4.0]]), ('boundary_3', [[4.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [4.0, 2.0]]), ('grid_row_3', [[0.0, 3.0], [4.0, 3.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 3.34], [1.34, 2.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r3', [[1.66, 2.66], [2.34, 3.34]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.52338247203549, 515.471674605677], [137.37373229568803, 515.471674605677], [218.67125713496569, 515.471674605677]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[212.00459046829903, 518.8050079390104], [218.67125713496569, 515.471674605677], [212.00459046829903, 512.1383412723436], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (1, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('C', (4, 2), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('D', (3, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (4, 3), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane555_C01.png'
        with Canvas(PLANE, xlim=(-0.8406572712600444, 4.331849554748036), ylim=(-0.5701048804875137, 4.602401945520566), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 4.0]]), ('boundary_3', [[4.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[1.0, 0.0], [1.0, 4.0]], id='grid_column_1', zorder=1, color='#2563EB', linewidth=3.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('grid_column_2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [4.0, 2.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 3.34], [1.34, 2.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r3', [[1.66, 2.66], [2.34, 3.34]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.52338247203549, 515.471674605677], [137.37373229568803, 515.471674605677], [218.67125713496569, 515.471674605677]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[212.00459046829903, 518.8050079390104], [218.67125713496569, 515.471674605677], [212.00459046829903, 512.1383412723436], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (1, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('C', (4, 2), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('D', (3, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (4, 3), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[1.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane555_C02.png'
        with Canvas(PLANE, xlim=(-0.8406572712600444, 4.331849554748036), ylim=(-0.5701048804875137, 4.602401945520566), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 4.0]]), ('boundary_3', [[4.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[1.0, 0.0], [1.0, 4.0]], id='grid_column_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[2.0, 0.0], [2.0, 4.0]], id='grid_column_2', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [4.0, 2.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 3.34], [1.34, 2.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r3', [[1.66, 2.66], [2.34, 3.34]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.52338247203549, 515.471674605677], [137.37373229568803, 515.471674605677], [218.67125713496569, 515.471674605677]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[212.00459046829903, 518.8050079390104], [218.67125713496569, 515.471674605677], [212.00459046829903, 512.1383412723436], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (1, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('C', (4, 2), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('D', (3, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (4, 3), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[2.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane555_C03.png'
        with Canvas(PLANE, xlim=(-0.8406572712600444, 4.331849554748036), ylim=(-0.5701048804875137, 4.602401945520566), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 4.0]]), ('boundary_3', [[4.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 3.34], [1.34, 2.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r3', [[1.66, 2.66], [2.34, 3.34]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.52338247203549, 515.471674605677], [137.37373229568803, 515.471674605677], [218.67125713496569, 515.471674605677]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[212.00459046829903, 518.8050079390104], [218.67125713496569, 515.471674605677], [212.00459046829903, 512.1383412723436], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (1, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('C', (4, 2), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('D', (3, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (4, 3), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane555_C04.png'
        with Canvas(PLANE, xlim=(-0.8406572712600444, 4.331849554748036), ylim=(-0.5701048804875137, 4.602401945520566), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 4.0]]), ('boundary_3', [[4.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[1.0, 0.0], [1.0, 4.0]], id='grid_column_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[2.0, 0.0], [2.0, 4.0]], id='grid_column_2', zorder=1, color='#16A34A', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [4.0, 2.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 3.34], [1.34, 2.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r3', [[1.66, 2.66], [2.34, 3.34]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.52338247203549, 515.471674605677], [137.37373229568803, 515.471674605677], [218.67125713496569, 515.471674605677]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[212.00459046829903, 518.8050079390104], [218.67125713496569, 515.471674605677], [212.00459046829903, 512.1383412723436], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (1, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('C', (4, 2), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('D', (3, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (4, 3), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[2.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane555_C05.png'
        with Canvas(PLANE, xlim=(-0.8406572712600444, 4.331849554748036), ylim=(-0.5701048804875137, 4.602401945520566), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 4.0]]), ('boundary_3', [[4.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [4.0, 2.0]], id='grid_row_2', zorder=1, color='#16A34A', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 3.34], [1.34, 2.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r3', [[1.66, 2.66], [2.34, 3.34]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.52338247203549, 515.471674605677], [137.37373229568803, 515.471674605677], [218.67125713496569, 515.471674605677]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[212.00459046829903, 518.8050079390104], [218.67125713496569, 515.471674605677], [212.00459046829903, 512.1383412723436], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (1, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('C', (4, 2), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('D', (3, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (4, 3), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane555_C06.png'
        with Canvas(PLANE, xlim=(-0.8406572712600444, 4.331849554748036), ylim=(-0.5701048804875137, 4.602401945520566), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [4.0, 0.0]]), ('boundary_2', [[4.0, 0.0], [4.0, 4.0]]), ('boundary_3', [[4.0, 4.0], [0.0, 4.0]]), ('boundary_4', [[0.0, 4.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 4.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 4.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 4.0]]), ('grid_row_1', [[0.0, 1.0], [4.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [4.0, 2.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 3.0], [4.0, 3.0]], id='grid_row_3', zorder=1, color='#EA580C', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c1_r3', [[0.66, 3.34], [1.34, 2.66]]), ('mirror_c2_r1', [[1.66, 1.34], [2.34, 0.66]]), ('mirror_c2_r3', [[1.66, 2.66], [2.34, 3.34]]), ('mirror_c3_r1', [[2.66, 0.66], [3.34, 1.34]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c3_r3', [[2.66, 2.66], [3.34, 3.34]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.52338247203549, 515.471674605677], [137.37373229568803, 515.471674605677], [218.67125713496569, 515.471674605677]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[212.00459046829903, 518.8050079390104], [218.67125713496569, 515.471674605677], [212.00459046829903, 512.1383412723436], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (1, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (2, 0), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('C', (4, 2), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.text('D', (3, 4), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (4, 3), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane555')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane555().draw(args.output, variant=args.variant))
