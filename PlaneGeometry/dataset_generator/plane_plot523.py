"""Frozen question Plane523; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane523:

    def __init__(self):
        self.id = 'Plane523'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-expand24:Plane348/extension_03'
        self.question = 'A square piece of paper is folded in half by moving its left half onto its right half, then folded in half by moving its bottom half onto its top half. The resulting four-layer square is shown, with A at the intersection of the two folded edges and B, C, D in counterclockwise order. Make one straight cut joining the midpoint of AD to the midpoint of AB. Make another straight cut joining the midpoint of DC to the midpoint of BC. Each cut stops at those endpoints. The dashed segments in the figure are cuts, not fold lines; cut through every layer only along those segments. Unfold every resulting piece as far as possible. How many resulting pieces are squares? Pieces are counted separately; a shape with a hole is not a square.'
        self.answer = '1'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane523.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.075, 1.075], ylim=[-0.071, 1.079], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('edge_AB', [[0, 0], [1, 0]]), ('edge_BC', [[1, 0], [1, 1]]), ('edge_CD', [[1, 1], [0, 1]]), ('edge_DA', [[0, 1], [0, 0]])]:
                c.line(points, id=object_id)
            c.line([[0.0, 0.5], [0.5, 0.0]], id='cut_1', linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.5, 1.0], [1.0, 0.5]], id='cut_2', linestyle=(0.0, [4.0, 3.0]))
            c.text('A', [0, 0], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='top', rotation_mode='default', offset_pt=[-8, -8], annotation_clip=None)
            c.text('B', [1, 0], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='top', rotation_mode='default', offset_pt=[8, -8], annotation_clip=None)
            c.text('C', [1, 1], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', va='bottom', rotation_mode='default', offset_pt=[8, 8], annotation_clip=None)
            c.text('D', [0, 1], zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', va='bottom', rotation_mode='default', offset_pt=[-8, 8], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane523().draw(sys.argv[1] if len(sys.argv) > 1 else None))
