"""Frozen question Plane585; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane585:

    def __init__(self):
        self.id = 'Plane585'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane366/extension_01'
        self.question = 'The two bold lines are rotations of each other. Endpoints need not keep their order. Which option lists exactly the marked points that could be the centre of this rotation?\nChoices:\nA: Only X\nB: Only T\nC: X and T\nD: Y and Z\nE: X, Y, Z and T'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'Only X', 'B': 'Only T', 'C': 'X and T', 'D': 'Y and Z', 'E': 'X, Y, Z and T'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane585.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1860465116279073, 8.186046511627907], ylim=[-1.1860465116279073, 7.186046511627907], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('grid_vertical_0', [[0, 0], [0, 6]]), ('grid_vertical_1', [[1, 0], [1, 6]]), ('grid_vertical_2', [[2, 0], [2, 6]]), ('grid_vertical_3', [[3, 0], [3, 6]]), ('grid_vertical_4', [[4, 0], [4, 6]]), ('grid_vertical_5', [[5, 0], [5, 6]]), ('grid_vertical_6', [[6, 0], [6, 6]]), ('grid_vertical_7', [[7, 0], [7, 6]]), ('grid_vertical_8', [[8, 0], [8, 6]]), ('grid_horizontal_0', [[0, 0], [8, 0]]), ('grid_horizontal_1', [[0, 1], [8, 1]]), ('grid_horizontal_2', [[0, 2], [8, 2]]), ('grid_horizontal_3', [[0, 3], [8, 3]]), ('grid_horizontal_4', [[0, 4], [8, 4]]), ('grid_horizontal_5', [[0, 5], [8, 5]]), ('grid_horizontal_6', [[0, 6], [8, 6]])]:
                c.line(points, id=object_id, zorder=1, color='#AAAAAA')
            c.line([[1, 5], [4, 5]], id='given_segment_AB', zorder=3)
            c.line([[4, 1], [7, 1]], id='given_segment_CD', zorder=3)
            for object_id, center, radius in [('point_marker_X', [3, 3], 0.05046834625322997), ('point_marker_Y', [5, 3], 0.05046834625322997), ('point_marker_Z', [4, 4], 0.05046834625322997), ('point_marker_T', [4, 3], 0.05046834625322997)]:
                c.circle(center, radius, id=object_id, zorder=4, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], fill=False)
            c.text('X', [3, 3], id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-16, 16], annotation_clip=False)
            c.text('Y', [5, 3], id='label_Y', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 16], annotation_clip=False)
            c.text('Z', [4, 4], id='label_Z', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 16], annotation_clip=False)
            c.text('T', [4, 3], id='label_T', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, -16], annotation_clip=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane585().draw(sys.argv[1] if len(sys.argv) > 1 else None))
