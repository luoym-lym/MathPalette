"""Frozen question Plane588; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane588:

    def __init__(self):
        self.id = 'Plane588'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane366/extension_04'
        self.question = 'The two bold lines are rotations of each other. Endpoints need not keep their order. Which option lists exactly the marked points that could be the centre of this rotation?\nChoices:\nA: Only X\nB: X and Z\nC: Y and T\nD: Only Z\nE: X, Y, Z and T'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'Only X', 'B': 'X and Z', 'C': 'Y and T', 'D': 'Only Z', 'E': 'X, Y, Z and T'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane588.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.20930232558139483, 9.209302325581394], ylim=[-0.7093023255813948, 8.709302325581394], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('grid_vertical_0', [[0, 0], [0, 8]]), ('grid_vertical_1', [[1, 0], [1, 8]]), ('grid_vertical_2', [[2, 0], [2, 8]]), ('grid_vertical_3', [[3, 0], [3, 8]]), ('grid_vertical_4', [[4, 0], [4, 8]]), ('grid_vertical_5', [[5, 0], [5, 8]]), ('grid_vertical_6', [[6, 0], [6, 8]]), ('grid_vertical_7', [[7, 0], [7, 8]]), ('grid_vertical_8', [[8, 0], [8, 8]]), ('grid_vertical_9', [[9, 0], [9, 8]]), ('grid_horizontal_0', [[0, 0], [9, 0]]), ('grid_horizontal_1', [[0, 1], [9, 1]]), ('grid_horizontal_2', [[0, 2], [9, 2]]), ('grid_horizontal_3', [[0, 3], [9, 3]]), ('grid_horizontal_4', [[0, 4], [9, 4]]), ('grid_horizontal_5', [[0, 5], [9, 5]]), ('grid_horizontal_6', [[0, 6], [9, 6]]), ('grid_horizontal_7', [[0, 7], [9, 7]]), ('grid_horizontal_8', [[0, 8], [9, 8]])]:
                c.line(points, id=object_id, zorder=1, color='#AAAAAA')
            c.line([[1, 1], [6, 1]], id='given_segment_AB', zorder=3)
            c.line([[5, 3], [8, 7]], id='given_segment_CD', zorder=3)
            for object_id, center, radius in [('point_marker_X', [6, 2], 0.05677688953488369), ('point_marker_Y', [3, 4], 0.05677688953488369), ('point_marker_Z', [1, 6], 0.05677688953488369), ('point_marker_T', [5, 4], 0.05677688953488369)]:
                c.circle(center, radius, id=object_id, zorder=4, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], fill=False)
            c.text('X', [6, 2], id='label_X', clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, -16], annotation_clip=False)
            for object_id, text, anchor in [('label_Y', 'Y', [3, 4]), ('label_Z', 'Z', [1, 6]), ('label_T', 'T', [5, 4])]:
                c.text(text, anchor, id=object_id, clip_on=True, fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 16], annotation_clip=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane588().draw(sys.argv[1] if len(sys.argv) > 1 else None))
