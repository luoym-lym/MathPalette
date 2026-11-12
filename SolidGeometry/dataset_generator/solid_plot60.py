"""Frozen question Solid60; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid60:

    def __init__(self):
        self.id = 'Solid60'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3504'
        self.question = 'Find the surface area of the triangular prism.'
        self.answer = '768 cm²'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid60.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-7.548080710033014, 26.455525761150398], ylim=[-11.121076724749791, 22.88252974643362], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('edge_0_0', [[0.0, 0.0], [12.0, 0.0]]), ('edge_1_0', [[12.0, 0.0], [6.0, 8.0]]), ('edge_2_0', [[6.0, 8.0], [0.0, 0.0]]), ('edge_4_0', [[25.650000000000002, 6.3], [19.650000000000002, 14.3]]), ('edge_7_0', [[12.0, 0.0], [25.650000000000002, 6.3]]), ('edge_8_0', [[6.0, 8.0], [19.650000000000002, 14.3]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[6.0, 0.0], [6.0, 8.0]], id='triangle_altitude', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            for object_id, points in [('source_right', [[6.6, 0.0], [6.6, 0.6], [6.0, 0.6]]), ('equal_left_0', [[3.2416637431152315, 3.8821267932699457], [2.7583362568847685, 4.117873206730054]]), ('equal_right_0', [[9.257034015062848, 4.165894463905106], [8.742965984937152, 3.8341055360948944]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[0.0, -1.3665286808442403], [12.0, -1.3665286808442403]], id='base_dimension_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [0.0, -1.3665286808442403]], id='base_dimension_start', zorder=3, clip_on=False)
            c.line([[12.0, 0.0], [12.0, -1.3665286808442403]], id='base_dimension_end', zorder=3, clip_on=False)
            c.text('12 cm', [6.0, -1.3665286808442403], rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.line([[-3.907332936120742, 0.0], [-3.907332936120742, 8.0]], id='height_dimension_range', zorder=3, clip_on=False, linestyle=(0, [4, 3]))
            c.line([[6.0, 0.0], [-3.907332936120742, 0.0]], id='height_dimension_start', zorder=3, clip_on=False)
            c.line([[6.0, 8.0], [-3.907332936120742, 8.0]], id='height_dimension_end', zorder=3, clip_on=False)
            c.text('8 cm', [-3.907332936120742, 4.0], rotation_mode='default', offset_pt=[-23.400000000000002, 0.0], annotation_clip=None)
            c.text('10 cm', [9.0, 4.0], rotation_mode='default', offset_pt=[28.730000000000004, 13.520000000000001], annotation_clip=None)
            c.text('21 cm', [18.825, 3.15], rotation_mode='default', offset_pt=[18, -19], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid60().draw(sys.argv[1] if len(sys.argv) > 1 else None))
