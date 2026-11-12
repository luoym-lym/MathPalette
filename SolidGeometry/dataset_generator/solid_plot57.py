"""Frozen question Solid57; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid57:

    def __init__(self):
        self.id = 'Solid57'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3409'
        self.question = 'PABCD is a right pyramid on square base ABCD. M is the center of the base and N is the midpoint of CD. Find angle PNM to two decimal places.'
        self.answer = '69.30°'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid57.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.8910865147388751, 13.696149737706826], ylim=[-1.310250880288196, 13.276985372157505], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[0.0, 0.0], [8.0, 0.0]], id='edge_0_0', zorder=3, clip_on=False)
            c.line([[8.0, 0.0], [12.4, 2.8]], id='edge_1_0', zorder=3, clip_on=False)
            c.line([[12.4, 2.8], [4.4, 2.8]], id='edge_2_0', clip_on=False, linestyle=(0, [4, 3]))
            c.line([[4.4, 2.8], [0.0, 0.0]], id='edge_3_0', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('edge_4_0', [[0.0, 0.0], [6.2, 11.983005244258363]]), ('edge_5_0', [[8.0, 0.0], [6.2, 11.983005244258363]]), ('edge_6_0', [[12.4, 2.8], [6.2, 11.983005244258363]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[4.4, 2.8], [6.2, 11.983005244258363]], id='edge_7_0', clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('diagonal_AC', [[0.0, 0.0], [12.4, 2.8]]), ('diagonal_BD', [[8.0, 0.0], [4.4, 2.8]]), ('height', [[6.2, 1.4], [6.2, 11.983005244258363]]), ('PN', [[6.2, 11.983005244258363], [10.2, 1.4]]), ('MN', [[6.2, 1.4], [10.2, 1.4]]), ('altitude_right', [[6.65, 1.4], [6.65, 1.8499999999999999], [6.2, 1.8499999999999999]]), ('equal_AB_0', [[3.9727460899599314, -0.15892215075312818], [4.027253910040069, 0.15892215075312818]]), ('equal_BC_0', [[10.280531323828974, 1.2734507768401837], [10.119468676171026, 1.5265492231598161]]), ('equal_CD_0', [[8.42725391004007, 2.958922150753128], [8.372746089959932, 2.641077849246872]]), ('equal_DA_0', [[2.119468676171026, 1.5265492231598161], [2.280531323828974, 1.2734507768401837]]), ('mid_CN_0', [[11.301968676171027, 2.279049223159816], [11.463031323828973, 2.0259507768401837]]), ('mid_CN_1', [[11.136968676171026, 2.174049223159816], [11.298031323828972, 1.9209507768401837]]), ('mid_NB_0', [[9.101968676171026, 0.879049223159816], [9.263031323828972, 0.6259507768401839]]), ('mid_NB_1', [[8.936968676171027, 0.7740492231598161], [9.098031323828973, 0.5209507768401839]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[6.783030142125532, 12.376644013379009], [12.983030142125532, 3.1936387691206454]], id='slant_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[6.2, 11.983005244258363], [6.783030142125532, 12.376644013379009]], id='slant_start', zorder=3, clip_on=False)
            c.line([[12.4, 2.8], [12.983030142125532, 3.1936387691206454]], id='slant_end', zorder=3, clip_on=False)
            c.text('12', [9.883030142125532, 7.785141391249827], rotation_mode='default', offset_pt=[20, 0], annotation_clip=None)
            c.text('A', [0.0, 0.0], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -12], annotation_clip=None)
            c.text('D', [8.0, 0.0], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, -12], annotation_clip=None)
            c.text('C', [12.4, 2.8], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[26.364, 0.0], annotation_clip=None)
            c.text('B', [4.4, 2.8], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-26.364, 0.0], annotation_clip=None)
            c.text('M', [6.2, 1.4], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15.600000000000001, -15.600000000000001], annotation_clip=None)
            c.text('P', [6.2, 11.983005244258363], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('N', [10.2, 1.4], fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, -10], annotation_clip=None)
            c.text('8', [4.0, 0.0], rotation_mode='default', offset_pt=[0, -20], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid57().draw(sys.argv[1] if len(sys.argv) > 1 else None))
