"""Collected question Plane556; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane556:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06')

    def __init__(self):
        self.id = 'Plane556'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane236/extension_02'
        self.question = 'If a laser beam hits a mirror it changes its direction as shown. Each solid mirror has mirrored sides on both sides; dashed lines do not reflect. At which letter does the laser beam end?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
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
        with Canvas(PLANE, xlim=(-0.8693559656263625, 5.390103818198229), ylim=(-1.6062200539493332, 4.653239729875258), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 3.0]]), ('boundary_3', [[5.0, 3.0], [0.0, 3.0]]), ('boundary_4', [[0.0, 3.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 3.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 3.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 3.0]]), ('grid_column_4', [[4.0, 0.0], [4.0, 3.0]]), ('grid_row_1', [[0.0, 1.0], [5.0, 1.0]]), ('grid_row_2', [[0.0, 2.0], [5.0, 2.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c2_r1', [[1.66, 0.66], [2.34, 1.34]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c4_r1', [[3.66, 0.66], [4.34, 1.34]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.892612303016406, 436.6163616948369], [123.35602844436198, 436.6163616948369], [190.26661960133268, 436.6163616948369]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[183.59995293466602, 439.9496950281702], [190.26661960133268, 436.6163616948369], [183.59995293466602, 433.28302836150357], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (3, 3), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('C', (3, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (4, 3), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (5, 2), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane556_C01.png'
        with Canvas(PLANE, xlim=(-0.8693559656263625, 5.390103818198229), ylim=(-1.6062200539493332, 4.653239729875258), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 3.0]]), ('boundary_3', [[5.0, 3.0], [0.0, 3.0]]), ('boundary_4', [[0.0, 3.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[1.0, 0.0], [1.0, 3.0]], id='grid_column_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[2.0, 0.0], [2.0, 3.0]], id='grid_column_2', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[3.0, 0.0], [3.0, 3.0]], id='grid_column_3', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[4.0, 0.0], [4.0, 3.0]], id='grid_column_4', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 1.0], [5.0, 1.0]], id='grid_row_1', zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [5.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c2_r1', [[1.66, 0.66], [2.34, 1.34]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c4_r1', [[3.66, 0.66], [4.34, 1.34]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.892612303016406, 436.6163616948369], [123.35602844436198, 436.6163616948369], [190.26661960133268, 436.6163616948369]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[183.59995293466602, 439.9496950281702], [190.26661960133268, 436.6163616948369], [183.59995293466602, 433.28302836150357], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (3, 3), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('C', (3, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (4, 3), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (5, 2), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[3.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane556_C02.png'
        with Canvas(PLANE, xlim=(-0.8693559656263625, 5.390103818198229), ylim=(-1.6062200539493332, 4.653239729875258), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 3.0]]), ('boundary_3', [[5.0, 3.0], [0.0, 3.0]]), ('boundary_4', [[0.0, 3.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 3.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 3.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 3.0]]), ('grid_column_4', [[4.0, 0.0], [4.0, 3.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 1.0], [5.0, 1.0]], id='grid_row_1', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [5.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c2_r1', [[1.66, 0.66], [2.34, 1.34]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c4_r1', [[3.66, 0.66], [4.34, 1.34]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.892612303016406, 436.6163616948369], [123.35602844436198, 436.6163616948369], [190.26661960133268, 436.6163616948369]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[183.59995293466602, 439.9496950281702], [190.26661960133268, 436.6163616948369], [183.59995293466602, 433.28302836150357], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (3, 3), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('C', (3, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (4, 3), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (5, 2), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[5.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane556_C03.png'
        with Canvas(PLANE, xlim=(-0.8693559656263625, 5.390103818198229), ylim=(-1.6062200539493332, 4.653239729875258), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 3.0]]), ('boundary_3', [[5.0, 3.0], [0.0, 3.0]]), ('boundary_4', [[0.0, 3.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[1.0, 0.0], [1.0, 3.0]], id='grid_column_1', zorder=1, color='#2563EB', linewidth=3.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('grid_column_2', [[2.0, 0.0], [2.0, 3.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 3.0]]), ('grid_column_4', [[4.0, 0.0], [4.0, 3.0]]), ('grid_row_1', [[0.0, 1.0], [5.0, 1.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [5.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c2_r1', [[1.66, 0.66], [2.34, 1.34]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c4_r1', [[3.66, 0.66], [4.34, 1.34]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.892612303016406, 436.6163616948369], [123.35602844436198, 436.6163616948369], [190.26661960133268, 436.6163616948369]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[183.59995293466602, 439.9496950281702], [190.26661960133268, 436.6163616948369], [183.59995293466602, 433.28302836150357], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (3, 3), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('C', (3, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (4, 3), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (5, 2), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[2.0, 0.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane556_C04.png'
        with Canvas(PLANE, xlim=(-0.8693559656263625, 5.390103818198229), ylim=(-1.6062200539493332, 4.653239729875258), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 3.0]]), ('boundary_3', [[5.0, 3.0], [0.0, 3.0]]), ('boundary_4', [[0.0, 3.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 3.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 3.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 3.0]]), ('grid_column_4', [[4.0, 0.0], [4.0, 3.0]]), ('grid_row_1', [[0.0, 1.0], [5.0, 1.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [5.0, 2.0]], id='grid_row_2', zorder=1, color='#2563EB', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c2_r1', [[1.66, 0.66], [2.34, 1.34]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c4_r1', [[3.66, 0.66], [4.34, 1.34]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.892612303016406, 436.6163616948369], [123.35602844436198, 436.6163616948369], [190.26661960133268, 436.6163616948369]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[183.59995293466602, 439.9496950281702], [190.26661960133268, 436.6163616948369], [183.59995293466602, 433.28302836150357], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (3, 3), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('C', (3, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (4, 3), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (5, 2), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane556_C05.png'
        with Canvas(PLANE, xlim=(-0.8693559656263625, 5.390103818198229), ylim=(-1.6062200539493332, 4.653239729875258), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 3.0]]), ('boundary_3', [[5.0, 3.0], [0.0, 3.0]]), ('boundary_4', [[0.0, 3.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 3.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 3.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 3.0]]), ('grid_column_4', [[4.0, 0.0], [4.0, 3.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 1.0], [5.0, 1.0]], id='grid_row_1', zorder=1, color='#EA580C', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [5.0, 2.0]], id='grid_row_2', zorder=1, color='#16A34A', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c2_r1', [[1.66, 0.66], [2.34, 1.34]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c4_r1', [[3.66, 0.66], [4.34, 1.34]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.892612303016406, 436.6163616948369], [123.35602844436198, 436.6163616948369], [190.26661960133268, 436.6163616948369]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[183.59995293466602, 439.9496950281702], [190.26661960133268, 436.6163616948369], [183.59995293466602, 433.28302836150357], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (3, 3), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('C', (3, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (4, 3), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (5, 2), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[5.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane556_C06.png'
        with Canvas(PLANE, xlim=(-0.8693559656263625, 5.390103818198229), ylim=(-1.6062200539493332, 4.653239729875258), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('boundary_1', [[0.0, 0.0], [5.0, 0.0]]), ('boundary_2', [[5.0, 0.0], [5.0, 3.0]]), ('boundary_3', [[5.0, 3.0], [0.0, 3.0]]), ('boundary_4', [[0.0, 3.0], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, points in [('grid_column_1', [[1.0, 0.0], [1.0, 3.0]]), ('grid_column_2', [[2.0, 0.0], [2.0, 3.0]]), ('grid_column_3', [[3.0, 0.0], [3.0, 3.0]]), ('grid_column_4', [[4.0, 0.0], [4.0, 3.0]])]:
                c.line(points, id=object_id, zorder=1, color='#999999', linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 1.0], [5.0, 1.0]], id='grid_row_1', zorder=1, color='#DC2626', linewidth=2.0, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.line([[0.0, 2.0], [5.0, 2.0]], id='grid_row_2', zorder=1, color='#DC2626', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            for object_id, points in [('mirror_c1_r1', [[0.66, 1.34], [1.34, 0.66]]), ('mirror_c1_r2', [[0.66, 2.34], [1.34, 1.66]]), ('mirror_c2_r1', [[1.66, 0.66], [2.34, 1.34]]), ('mirror_c2_r2', [[1.66, 1.66], [2.34, 2.34]]), ('mirror_c3_r1', [[2.66, 1.34], [3.34, 0.66]]), ('mirror_c3_r2', [[2.66, 2.34], [3.34, 1.66]]), ('mirror_c4_r1', [[3.66, 0.66], [4.34, 1.34]]), ('mirror_c4_r2', [[3.66, 2.34], [4.34, 1.66]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[54.892612303016406, 436.6163616948369], [123.35602844436198, 436.6163616948369], [190.26661960133268, 436.6163616948369]], [1, 3, 3], coordinates='pixels', id='incident_arrow', zorder=4, joinstyle='round', simplify=False)
            c.path([[183.59995293466602, 439.9496950281702], [190.26661960133268, 436.6163616948369], [183.59995293466602, 433.28302836150357], [0.0, 0.0]], [1, 2, 2, 79], coordinates='pixels', id='incident_arrow', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), joinstyle='round', simplify=False)
            c.text('A', (2, 0), id='exit_label_A', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('B', (3, 3), id='exit_label_B', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('C', (3, 0), id='exit_label_C', fontsize=18.0, rotation_mode='default', offset_pt=(0, -15), annotation_clip=None)
            c.text('D', (4, 3), id='exit_label_D', fontsize=18.0, rotation_mode='default', offset_pt=(0, 15), annotation_clip=None)
            c.text('E', (5, 2), id='exit_label_E', fontsize=18.0, rotation_mode='default', offset_pt=(15, 0), annotation_clip=None)
            c.point([[5.0, 2.0]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane556')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06'))
    args = parser.parse_args()
    print(Plane556().draw(args.output, variant=args.variant))
