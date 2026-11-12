"""Frozen question Solid126; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid126:

    def __init__(self):
        self.id = 'Solid126'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:754'
        self.question = 'A rectangular section was cut out of a rectangular block as shown in the diagram. Find the decrease percentage of the surface area.\nChoices:\nA:Less than $12.5 \\%$\nB:$12.5 \\%$\nC:More than $12.5 \\%$, but less than $25 \\%$\nD:$25 \\%$\nE:More than $25 \\%$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Less than $12.5 \\%$', 'B': '$12.5 \\%$', 'C': 'More than $12.5 \\%$, but less than $25 \\%$', 'D': '$25 \\%$', 'E': 'More than $25 \\%$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid126.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-3.6498573279191975, 13.712257033774353], ylim=[-3.237633646886379, 14.12448071480717], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('ring0e0part0', [[0.0, 0.0], [12.0, 0.0]]), ('ring0e1part0', [[12.0, 0.0], [12.0, 8.0]]), ('ring0e2part0', [[12.0, 8.0], [9.0, 8.0]]), ('ring0e3part0', [[9.0, 8.0], [9.0, 5.0]]), ('ring0e4part0', [[9.0, 5.0], [0.0, 5.0]]), ('ring0e5part0', [[0.0, 5.0], [0.0, 0.0]]), ('ring1e2part0', [[9.9, 11.9], [6.9, 11.9]]), ('ring1e3part0', [[6.9, 11.9], [6.9, 8.9]]), ('ring1e4part0', [[6.9, 8.9], [-2.0999999999999996, 8.9]]), ('ring1e5part0', [[-2.0999999999999996, 8.9], [-2.0999999999999996, 3.9000000000000004]]), ('depth0part0', [[0.0, 0.0], [-2.0999999999999996, 3.9000000000000004]]), ('depth2part0', [[12.0, 8.0], [9.9, 11.9]]), ('depth3part0', [[9.0, 8.0], [6.9, 11.9]]), ('depth4part0', [[9.0, 5.0], [6.9, 8.9]]), ('depth5part0', [[0.0, 5.0], [-2.0999999999999996, 8.9]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('removed0', [[-2.0999999999999996, 8.9], [-2.0999999999999996, 11.9]]), ('removed1', [[-2.0999999999999996, 11.9], [6.9, 11.9]]), ('removed2', [[-2.0999999999999996, 11.9], [0.0, 8.0]]), ('removed3', [[0.0, 8.0], [9.0, 8.0]]), ('removed4', [[0.0, 5.0], [0.0, 8.0]]), ('width_range', [[0.0, -0.4884211055324671], [12.0, -0.4884211055324671]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [0.0, -0.4884211055324671]], id='width_start', zorder=3, clip_on=False)
            c.line([[12.0, 0.0], [12.0, -0.4884211055324671]], id='width_end', zorder=3, clip_on=False)
            c.text('12', [6.0, -0.4884211055324671], id='removed4', rotation_mode='default', offset_pt=[0, -12], annotation_clip=None)
            c.line([[12.558195549179963, 0.0], [12.558195549179963, 8.0]], id='height_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[12.0, 0.0], [12.558195549179963, 0.0]], id='height_start', zorder=3, clip_on=False)
            c.line([[12.0, 8.0], [12.558195549179963, 8.0]], id='height_end', zorder=3, clip_on=False)
            c.text('8', [12.558195549179963, 4.0], id='removed4', ha='left', rotation_mode='default', offset_pt=[12, 0], annotation_clip=None)
            c.line([[-0.45353388370871944, -0.24421055276623355], [-2.553533883708719, 3.655789447233767]], id='depth_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [-0.45353388370871944, -0.24421055276623355]], id='depth_start', zorder=3, clip_on=False)
            c.line([[-2.0999999999999996, 3.9000000000000004], [-2.553533883708719, 3.655789447233767]], id='depth_end', zorder=3, clip_on=False)
            c.text('6', [-1.503533883708719, 1.7057894472337667], id='removed4', ha='right', rotation_mode='default', offset_pt=[-8, -3], annotation_clip=None)
            c.line([[-2.5884211055324666, 3.9000000000000004], [-2.5884211055324666, 8.9]], id='lowheight_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[-2.0999999999999996, 3.9000000000000004], [-2.5884211055324666, 3.9000000000000004]], id='lowheight_start', zorder=3, clip_on=False)
            c.line([[-2.0999999999999996, 8.9], [-2.5884211055324666, 8.9]], id='lowheight_end', zorder=3, clip_on=False)
            c.text('5', [-2.5884211055324666, 6.4], id='removed4', ha='right', rotation_mode='default', offset_pt=[-10, 0], annotation_clip=None)
            c.line([[9.0, 7.476691672643785], [12.0, 7.476691672643785]], id='uprightwidth_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[9.0, 8.0], [9.0, 7.476691672643785]], id='uprightwidth_start', zorder=3, clip_on=False)
            c.line([[12.0, 8.0], [12.0, 7.476691672643785]], id='uprightwidth_end', zorder=3, clip_on=False)
            c.text('3', [10.5, 7.476691672643785], id='removed4', rotation_mode='default', offset_pt=[0, -12], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid126().draw(sys.argv[1] if len(sys.argv) > 1 else None))
