"""Frozen question Solid56; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid56:

    def __init__(self):
        self.id = 'Solid56'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3399'
        self.question = 'In the right triangular prism shown, X is the midpoint of EF. Find angle BXC to two decimal places.'
        self.answer = '10.74°'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid56.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.9460443714934073, 15.64980054161806], ylim=[-3.8985319542209655, 12.697312958890501], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[3.75, 8.25], [3.75, 5.25]], id='edge_0_0', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[3.75, 5.25], [0.0, 0.0]], id='edge_1_0', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_2_0', [[0.0, 0.0], [3.75, 8.25]]), ('edge_3_0', [[13.75, 8.25], [13.75, 5.25]]), ('edge_4_0', [[13.75, 5.25], [10.0, 0.0]]), ('edge_5_0', [[10.0, 0.0], [13.75, 8.25]]), ('edge_6_0', [[3.75, 8.25], [13.75, 8.25]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[3.75, 5.25], [13.75, 5.25]], id='edge_7_0', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [10.0, 0.0]], id='edge_8_0', zorder=3, clip_on=False)
            c.line([[5.0, 0.0]], id='midpoint', zorder=4, color=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765], linewidth=1.5, linestyle='None', solid_capstyle='projecting', marker='o', markersize=6.0, markeredgewidth=1.0, markeredgecolor='#000000', markerfacecolor='#000000')
            for object_id, points in [('equal_EX_0', [[2.348437735134516, -0.14832734070291964], [2.3715622648654837, 0.14832734070291964]]), ('equal_EX_1', [[2.6284377351345163, -0.14832734070291964], [2.651562264865484, 0.14832734070291964]]), ('equal_XF_0', [[7.3484377351345165, -0.14832734070291964], [7.371562264865484, 0.14832734070291964]]), ('equal_XF_1', [[7.628437735134516, -0.14832734070291964], [7.6515622648654835, 0.14832734070291964]]), ('left_right', [[3.75, 5.85], [3.6, 5.64], [3.6, 5.04]]), ('right_right', [[13.75, 5.85], [13.6, 5.64], [13.6, 5.04]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[3.75, 9.117034721701586], [13.75, 9.117034721701586]], id='length_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[3.75, 8.25], [3.75, 9.117034721701586]], id='length_start', zorder=3, clip_on=False)
            c.line([[13.75, 8.25], [13.75, 9.117034721701586]], id='length_end', zorder=3, clip_on=False)
            c.text('10', [8.75, 9.117034721701586], rotation_mode='default', offset_pt=[0, 14], annotation_clip=None)
            c.line([[14.58368723240537, 5.25], [14.58368723240537, 8.25]], id='height_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[13.75, 5.25], [14.58368723240537, 5.25]], id='height_start', zorder=3, clip_on=False)
            c.line([[13.75, 8.25], [14.58368723240537, 8.25]], id='height_end', zorder=3, clip_on=False)
            c.text('3', [14.58368723240537, 6.75], rotation_mode='default', offset_pt=[17, 0], annotation_clip=None)
            c.line([[10.759807110189074, -0.542719364420767], [14.509807110189074, 4.707280635579233]], id='depth_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[10.0, 0.0], [10.759807110189074, -0.542719364420767]], id='depth_start', zorder=3, clip_on=False)
            c.line([[13.75, 5.25], [14.509807110189074, 4.707280635579233]], id='depth_end', zorder=3, clip_on=False)
            c.text('15', [12.634807110189074, 2.0822806355792327], rotation_mode='default', offset_pt=[18, -14], annotation_clip=None)
            c.text('A', [3.75, 8.25], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-10, 12], annotation_clip=None)
            c.text('B', [13.75, 8.25], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8, 12], annotation_clip=None)
            c.text('C', [13.75, 5.25], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[34.2732, -14.280500000000002], annotation_clip=None)
            c.text('D', [3.75, 5.25], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-26.364, -10.985000000000001], annotation_clip=None)
            c.text('E', [0.0, 0.0], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -8], annotation_clip=None)
            c.text('F', [10.0, 0.0], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[21.970000000000002, -26.364], annotation_clip=None)
            c.text('X', [5.0, 0.0], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid56().draw(sys.argv[1] if len(sys.argv) > 1 else None))
