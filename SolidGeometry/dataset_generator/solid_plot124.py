"""Frozen question Solid124; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid124:

    def __init__(self):
        self.id = 'Solid124'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:722'
        self.question = 'A cube has side length $12 \\mathrm{~cm}$. Find the length of the route shown on its surface from point $M$ to point $N$.\nChoices:\nA:40 cm\nB:48 cm\nC:50 cm\nD:60 cm\nE:It is impossible to determine'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '40 cm', 'B': '48 cm', 'C': '50 cm', 'D': '60 cm', 'E': 'It is impossible to determine'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid124.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-1.3878500351672205, 17.51042560697598), ylim=(-1.4871378210715989, 17.411137821071602), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('cube000_cube100', [[0.0, 0.0], [12.0, 0.0]]), ('cube000_cube001', [[0.0, 0.0], [0.0, 12.0]]), ('cube001_cube101', [[0.0, 12.0], [12.0, 12.0]]), ('cube001_cube011', [[0.0, 12.0], [4.199999999999999, 16.2]]), ('cube011_cube111', [[4.199999999999999, 16.2], [16.2, 16.2]]), ('cube100_cube110', [[12.0, 0.0], [16.2, 4.199999999999999]]), ('cube100_cube101', [[12.0, 0.0], [12.0, 12.0]]), ('cube101_cube111', [[12.0, 12.0], [16.2, 16.2]]), ('cube110_cube111', [[16.2, 4.199999999999999], [16.2, 16.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[12.0, 0.0], [16.2, 4.199999999999999], [16.2, 16.2], [12.0, 12.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='rightface', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('route0', [[0.0, 12.0], [0.0, 0.0]]), ('arrow0wing0', [[0.0, 0.0], [-0.276, 0.78]]), ('arrow0wing1', [[0.0, 0.0], [0.276, 0.78]]), ('route1', [[0.0, 0.0], [8.0, 0.0]]), ('arrow1wing0', [[8.0, 0.0], [7.220000000000001, -0.276]]), ('arrow1wing1', [[8.0, 0.0], [7.22, 0.276]]), ('route2', [[8.0, 0.0], [8.0, 12.0]]), ('arrow2wing0', [[8.0, 12.0], [8.276, 11.219999999999999]]), ('arrow2wing1', [[8.0, 12.0], [7.724, 11.22]]), ('route3', [[8.0, 12.0], [12.0, 12.0]]), ('arrow3wing0', [[12.0, 12.0], [11.22, 11.724]]), ('arrow3wing1', [[12.0, 12.0], [11.219999999999999, 12.276]]), ('route4', [[12.0, 12.0], [16.2, 16.2]]), ('arrow4wing0', [[15.864, 15.864], [15.50761818228198, 15.117295239067007]]), ('arrow4wing1', [[15.864, 15.864], [15.117295239067007, 15.50761818228198]]), ('route5', [[16.2, 16.2], [16.2, 4.199999999999999]]), ('arrow5wing0', [[16.2, 4.199999999999999], [15.924, 4.98]]), ('arrow5wing1', [[16.2, 4.199999999999999], [16.476, 4.979999999999999]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.text('M', (0.0, 12.0), id='start', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-18, 8), annotation_clip=None)
            c.text('N', (16.2, 4.199999999999999), id='end', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(17, -4), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid124().draw(sys.argv[1] if len(sys.argv) > 1 else None))
