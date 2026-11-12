"""Frozen question Solid236; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid236:

    def __init__(self):
        self.id = 'Solid236'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2754'
        self.question = 'In the cube $ABCDEFGH$ with opposite vertices $C$ and $E,$ $J$ and $I$ are the midpoints of edges $\\overline{FB}$ and $\\overline{HD},$ respectively. Let $R$ be the ratio of the area of the cross-section $EJCI$ to the area of one of the faces of the cube. What is $R^2?$\n\nChoices:\nA:$\\frac{5}{4}$\nB:$\\frac{4}{3}$\nC:$\\frac{3}{2}$\nD:$\\frac{25}{16}$\nE:$\\frac{9}{4}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{5}{4}$', 'B': '$\\frac{4}{3}$', 'C': '$\\frac{3}{2}$', 'D': '$\\frac{25}{16}$', 'E': '$\\frac{9}{4}$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid236.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.7716757301905619, 1.2893342318673762], ylim=[-0.1499111882891997, 1.9110987737687384], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.5, 1.75], [-0.5, 1.0], [0.0, 0.0], [1.0, 0.75], [0.5, 1.75]], [1, 2, 2, 2, 79], id='section_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('line_1', [[0.5, 0.75], [-0.5, 0.5]]), ('line_2', [[0.5, 0.75], [1.0, 0.25]]), ('line_3', [[0.5, 0.75], [0.5, 1.75]])]:
                c.line(points, id=object_id, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('line_4', [[-0.5, 0.5], [0.0, 0.0]]), ('line_5', [[0.0, 0.0], [1.0, 0.25]]), ('line_6', [[-0.5, 0.5], [-0.5, 1.5]]), ('line_7', [[0.0, 0.0], [0.0, 1.0]]), ('line_8', [[1.0, 0.25], [1.0, 1.25]]), ('line_9', [[-0.5, 1.5], [0.0, 1.0]]), ('line_10', [[0.0, 1.0], [1.0, 1.25]]), ('line_11', [[1.0, 1.25], [0.5, 1.75]]), ('line_12', [[0.5, 1.75], [-0.5, 1.5]]), ('line_13', [[0.5, 1.75], [-0.5, 1.0]]), ('line_14', [[-0.5, 1.0], [0.0, 0.0]]), ('line_15', [[0.0, 0.0], [1.0, 0.75]]), ('line_16', [[1.0, 0.75], [0.5, 1.75]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('dotA', [[0.5, 0.75]]), ('dotB', [[-0.5, 0.5]]), ('dotC', [[0.0, 0.0]]), ('dotD', [[1.0, 0.25]]), ('dotE', [[0.5, 1.75]]), ('dotF', [[-0.5, 1.5]]), ('dotG', [[0.0, 1.0]]), ('dotH', [[1.0, 1.25]]), ('dotI', [[1.0, 0.75]]), ('dotJ', [[-0.5, 1.0]])]:
                c.line(points, id=object_id, zorder=4, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1, markeredgecolor='black', markerfacecolor='black')
            c.text('A', [0.5, 0.75], id='label_0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[20, -2], annotation_clip=None)
            c.text('B', [-0.5, 0.5], id='label_1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-18, -6], annotation_clip=None)
            c.text('C', [0.0, 0.0], id='label_2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -20], annotation_clip=None)
            c.text('D', [1.0, 0.25], id='label_3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[20, -3], annotation_clip=None)
            c.text('E', [0.5, 1.75], id='label_4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 20], annotation_clip=None)
            c.text('F', [-0.5, 1.5], id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-20, 0], annotation_clip=None)
            c.text('G', [0.0, 1.0], id='label_6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 19], annotation_clip=None)
            c.text('H', [1.0, 1.25], id='label_7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[22, 0], annotation_clip=None)
            c.text('I', [1.0, 0.75], id='label_8', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[20, 0], annotation_clip=None)
            c.text('J', [-0.5, 1.0], id='label_9', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-20, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid236().draw(sys.argv[1] if len(sys.argv) > 1 else None))
