"""Frozen question Solid185; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid185:

    def __init__(self):
        self.id = 'Solid185'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1717'
        self.question = "The diagram on the right shows a cube of side $18 \\mathrm{~cm}$. A path across the cube's surface runs from $\\mathrm{X}$ to $\\mathrm{Y}$ along the route shown. What is the length of this path?\nChoices:\nA:$54 \\mathrm{~cm}$\nB:$72 \\mathrm{~cm}$\nC:$80 \\mathrm{~cm}$\nD:$88 \\mathrm{~cm}$\nE:$90 \\mathrm{~cm}$"
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$54 \\mathrm{~cm}$', 'B': '$72 \\mathrm{~cm}$', 'C': '$80 \\mathrm{~cm}$', 'D': '$88 \\mathrm{~cm}$', 'E': '$90 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid185.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-2.0202808012156144, 26.306790067914356), ylim=(-2.2205354345649813, 26.10653543456499), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('cube000_cube100', [[0.0, 0.0], [18.0, 0.0]]), ('cube000_cube001', [[0.0, 0.0], [0.0, 18.0]]), ('cube001_cube101', [[0.0, 18.0], [18.0, 18.0]]), ('cube001_cube011', [[0.0, 18.0], [6.3, 24.3]]), ('cube011_cube111', [[6.3, 24.3], [24.3, 24.3]]), ('cube100_cube110', [[18.0, 0.0], [24.3, 6.3]]), ('cube100_cube101', [[18.0, 0.0], [18.0, 18.0]]), ('cube101_cube111', [[18.0, 18.0], [24.3, 24.3]]), ('cube110_cube111', [[24.3, 6.3], [24.3, 24.3]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[18.0, 0.0], [24.3, 6.3], [24.3, 24.3], [18.0, 18.0], [18.0, 0.0]], [1, 2, 2, 2, 79], id='rightface', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('route0', [[0.0, 18.0], [0.0, 0.0]]), ('arrow0wing0', [[0.0, 0.0], [-0.4139999999999999, 1.1700000000000002]]), ('arrow0wing1', [[0.0, 0.0], [0.41400000000000003, 1.17]]), ('route1', [[0.0, 0.0], [11.700000000000001, 0.0]]), ('arrow1wing0', [[11.700000000000001, 0.0], [10.530000000000001, -0.41400000000000003]]), ('arrow1wing1', [[11.700000000000001, 0.0], [10.530000000000001, 0.4139999999999999]]), ('route2', [[11.700000000000001, 0.0], [11.700000000000001, 18.0]]), ('arrow2wing0', [[11.700000000000001, 18.0], [12.114000000000003, 16.830000000000002]]), ('arrow2wing1', [[11.700000000000001, 18.0], [11.286000000000001, 16.83]]), ('route3', [[11.700000000000001, 18.0], [18.0, 18.0]]), ('arrow3wing0', [[18.0, 18.0], [16.83, 17.586]]), ('arrow3wing1', [[18.0, 18.0], [16.830000000000002, 18.414]]), ('route4', [[18.0, 18.0], [24.3, 24.3]]), ('arrow4wing0', [[23.796, 23.796], [23.26142727342297, 22.67594285860051]]), ('arrow4wing1', [[23.796, 23.796], [22.67594285860051, 23.26142727342297]]), ('route5', [[24.3, 24.3], [24.3, 6.3]]), ('arrow5wing0', [[24.3, 6.3], [23.886, 7.47]]), ('arrow5wing1', [[24.3, 6.3], [24.714, 7.47]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.text('X', (0.0, 18.0), id='start', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-18, 8), annotation_clip=None)
            c.text('Y', (24.3, 6.3), id='end', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(17, -4), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid185().draw(sys.argv[1] if len(sys.argv) > 1 else None))
