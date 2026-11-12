"""Frozen question Solid152; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid152:

    def __init__(self):
        self.id = 'Solid152'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1170'
        self.question = 'The diagram shows the net of a box consisting only of rectangles. How big is the volume of the box?\nChoices:\nA:$43 \\mathrm{~cm}^{3}$\nB:$70 \\mathrm{~cm}^{3}$\nC:$80 \\mathrm{~cm}^{3}$\nD:$100 \\mathrm{~cm}^{3}$\nE:$1820 \\mathrm{~cm}^{3}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$43 \\mathrm{~cm}^{3}$',
         'B': '$70 \\mathrm{~cm}^{3}$',
         'C': '$80 \\mathrm{~cm}^{3}$',
         'D': '$100 \\mathrm{~cm}^{3}$',
         'E': '$1820 \\mathrm{~cm}^{3}$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid152.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-5.761331657130331, 31.05244675048308), ylim=(-17.712312408909074, 19.101465998704338), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('netedge0', [[0.0, 0.0], [26.0, 0.0]]), ('netedge1', [[0.0, 2.0], [26.0, 2.0]]), ('netedge2', [[0.0, 0.0], [0.0, 2.0]]), ('netedge3', [[8.0, 0.0], [8.0, 10.0]]), ('netedge4', [[13.0, -5.0], [13.0, 10.0]]), ('netedge5', [[21.0, -5.0], [21.0, 2.0]]), ('netedge6', [[26.0, 0.0], [26.0, 2.0]]), ('netedge7', [[8.0, 10.0], [13.0, 10.0]]), ('netedge8', [[13.0, -5.0], [21.0, -5.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('netfill0', [[0.0, 0.0], [8.0, 0.0], [8.0, 2.0], [0.0, 2.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('netfill1', [[8.0, 0.0], [13.0, 0.0], [13.0, 10.0], [8.0, 10.0], [8.0, 0.0]], [1, 2, 2, 2, 79]), ('netfill2', [[13.0, -5.0], [21.0, -5.0], [21.0, 2.0], [13.0, 2.0], [13.0, -5.0]], [1, 2, 2, 2, 79]), ('netfill3', [[21.0, 0.0], [26.0, 0.0], [26.0, 2.0], [21.0, 2.0], [21.0, 0.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.line([[-0.8876779129922217, 0.0], [-0.8876779129922217, 10.0]], id='height10_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [-0.8876779129922217, 0.0]], id='height10_start', zorder=3, clip_on=False)
            c.line([[0.0, 10.0], [-0.8876779129922217, 10.0]], id='height10_end', zorder=3, clip_on=False)
            c.text('10 cm', (-0.8876779129922217, 5.0), id='netfill3', ha='right', rotation_mode='default', offset_pt=(-6, 0), annotation_clip=None)
            c.line([[26.88767791299222, -5.0], [26.88767791299222, 2.0]], id='height7_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[26.0, -5.0], [26.88767791299222, -5.0]], id='height7_start', zorder=3, clip_on=False)
            c.line([[26.0, 2.0], [26.88767791299222, 2.0]], id='height7_end', zorder=3, clip_on=False)
            c.text('7 cm', (26.88767791299222, -1.5), id='netfill3', ha='left', rotation_mode='default', offset_pt=(6, 0), annotation_clip=None)
            c.line([[0.0, -7.397315941601847], [26.0, -7.397315941601847]], id='width26_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [0.0, -7.397315941601847]], id='width26_start', zorder=3, clip_on=False)
            c.line([[26.0, 0.0], [26.0, -7.397315941601847]], id='width26_end', zorder=3, clip_on=False)
            c.text('26 cm', (13.0, -7.397315941601847), id='netfill3', rotation_mode='default', offset_pt=(0, -13), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid152().draw(sys.argv[1] if len(sys.argv) > 1 else None))
