"""Frozen question Solid169; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid169:

    def __init__(self):
        self.id = 'Solid169'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1524'
        self.question = 'The diagram shows a cube with edges of length $12 \\mathrm{~cm}$. What is the length of the route shown from point $P$ to point $Q$?\nChoices:\nA:$40 \\mathrm{~cm}$\nB:$48 \\mathrm{~cm}$\nC:$50 \\mathrm{~cm}$\nD:$60 \\mathrm{~cm}$\nE:more information is needed'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$40 \\mathrm{~cm}$', 'B': '$48 \\mathrm{~cm}$', 'C': '$50 \\mathrm{~cm}$', 'D': '$60 \\mathrm{~cm}$', 'E': 'more information is needed'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid169.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-1.2926063415559366, 17.51608175331024), ylim=(-1.4423440474330844, 17.36634404743309), axes_position=(0.05, 0.050000000000000114, 0.9, 0.8999999999999998), coordinate_axes=False) as c:
            for object_id, points in [('cube000_cube100', [[0.0, 0.0], [12.0, 0.0]]), ('cube000_cube001', [[0.0, 0.0], [0.0, 12.0]]), ('cube001_cube101', [[0.0, 12.0], [12.0, 12.0]]), ('cube001_cube011', [[0.0, 12.0], [4.199999999999999, 16.2]]), ('cube011_cube111', [[4.199999999999999, 16.2], [16.2, 16.2]]), ('cube100_cube110', [[12.0, 0.0], [16.2, 4.199999999999999]]), ('cube100_cube101', [[12.0, 0.0], [12.0, 12.0]]), ('cube101_cube111', [[12.0, 12.0], [16.2, 16.2]]), ('cube110_cube111', [[16.2, 4.199999999999999], [16.2, 16.2]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[12.0, 0.0], [16.2, 4.199999999999999], [16.2, 16.2], [12.0, 12.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='rightface', alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('route0', [[0.0, 12.0], [0.0, 0.0]]), ('arrow0wing0', [[0.0, 0.0], [-0.276, 0.78]]), ('arrow0wing1', [[0.0, 0.0], [0.276, 0.78]]), ('route1', [[0.0, 0.0], [8.64, 0.0]]), ('arrow1wing0', [[8.64, 0.0], [7.860000000000001, -0.276]]), ('arrow1wing1', [[8.64, 0.0], [7.86, 0.276]]), ('route2', [[8.64, 0.0], [8.64, 12.0]]), ('arrow2wing0', [[8.64, 12.0], [8.916, 11.219999999999999]]), ('arrow2wing1', [[8.64, 12.0], [8.364, 11.22]]), ('route3', [[8.64, 12.0], [12.0, 12.0]]), ('arrow3wing0', [[12.0, 12.0], [11.22, 11.724]]), ('arrow3wing1', [[12.0, 12.0], [11.219999999999999, 12.276]]), ('route4', [[12.0, 12.0], [16.2, 16.2]]), ('arrow4wing0', [[15.864, 15.864], [15.50761818228198, 15.117295239067007]]), ('arrow4wing1', [[15.864, 15.864], [15.117295239067007, 15.50761818228198]]), ('route5', [[16.2, 16.2], [16.2, 4.199999999999999]]), ('arrow5wing0', [[16.2, 4.199999999999999], [15.924, 4.98]]), ('arrow5wing1', [[16.2, 4.199999999999999], [16.476, 4.979999999999999]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.text('P', (0.0, 12.0), id='start', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-18, 8), annotation_clip=None)
            c.text('Q', (16.2, 4.199999999999999), id='end', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(17, -4), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid169().draw(sys.argv[1] if len(sys.argv) > 1 else None))
