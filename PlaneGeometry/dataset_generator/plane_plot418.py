"""Frozen question Plane418; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane418:

    def __init__(self):
        self.id = 'Plane418'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1793'
        self.question = 'What is the largest number of " $\\mathrm{T}$ " shaped pieces, as shown, that can be placed on the $4 \\times 5$ grid in the diagram, without any overlap of the pieces?'
        self.answer = '4'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane418.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.2354418878386193, 9.751259098392648), ylim=(-3.0012534155693373, 6.985447570661931), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='piece0', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [1.0, 2.0], [1.0, 3.0], [0.0, 3.0], [0.0, 2.0]], [1, 2, 2, 2, 79], id='piece0', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='piece1', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [1.0, 3.0], [1.0, 2.0]], [1, 2, 2, 2, 79], id='piece1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='piece2', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.0, 2.0], [3.0, 2.0], [3.0, 3.0], [2.0, 3.0], [2.0, 2.0]], [1, 2, 2, 2, 79], id='piece2', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='piece3', alpha=0.45, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='piece3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, vertices, codes in [('board0', [[4.5, 0.0], [5.5, 0.0], [5.5, 1.0], [4.5, 1.0], [4.5, 0.0]], [1, 2, 2, 2, 79]), ('board1', [[4.5, 1.0], [5.5, 1.0], [5.5, 2.0], [4.5, 2.0], [4.5, 1.0]], [1, 2, 2, 2, 79]), ('board2', [[4.5, 2.0], [5.5, 2.0], [5.5, 3.0], [4.5, 3.0], [4.5, 2.0]], [1, 2, 2, 2, 79]), ('board3', [[4.5, 3.0], [5.5, 3.0], [5.5, 4.0], [4.5, 4.0], [4.5, 3.0]], [1, 2, 2, 2, 79]), ('board4', [[5.5, 0.0], [6.5, 0.0], [6.5, 1.0], [5.5, 1.0], [5.5, 0.0]], [1, 2, 2, 2, 79]), ('board5', [[5.5, 1.0], [6.5, 1.0], [6.5, 2.0], [5.5, 2.0], [5.5, 1.0]], [1, 2, 2, 2, 79]), ('board6', [[5.5, 2.0], [6.5, 2.0], [6.5, 3.0], [5.5, 3.0], [5.5, 2.0]], [1, 2, 2, 2, 79]), ('board7', [[5.5, 3.0], [6.5, 3.0], [6.5, 4.0], [5.5, 4.0], [5.5, 3.0]], [1, 2, 2, 2, 79]), ('board8', [[6.5, 0.0], [7.5, 0.0], [7.5, 1.0], [6.5, 1.0], [6.5, 0.0]], [1, 2, 2, 2, 79]), ('board9', [[6.5, 1.0], [7.5, 1.0], [7.5, 2.0], [6.5, 2.0], [6.5, 1.0]], [1, 2, 2, 2, 79]), ('board10', [[6.5, 2.0], [7.5, 2.0], [7.5, 3.0], [6.5, 3.0], [6.5, 2.0]], [1, 2, 2, 2, 79]), ('board11', [[6.5, 3.0], [7.5, 3.0], [7.5, 4.0], [6.5, 4.0], [6.5, 3.0]], [1, 2, 2, 2, 79]), ('board12', [[7.5, 0.0], [8.5, 0.0], [8.5, 1.0], [7.5, 1.0], [7.5, 0.0]], [1, 2, 2, 2, 79]), ('board13', [[7.5, 1.0], [8.5, 1.0], [8.5, 2.0], [7.5, 2.0], [7.5, 1.0]], [1, 2, 2, 2, 79]), ('board14', [[7.5, 2.0], [8.5, 2.0], [8.5, 3.0], [7.5, 3.0], [7.5, 2.0]], [1, 2, 2, 2, 79]), ('board15', [[7.5, 3.0], [8.5, 3.0], [8.5, 4.0], [7.5, 4.0], [7.5, 3.0]], [1, 2, 2, 2, 79]), ('board16', [[8.5, 0.0], [9.5, 0.0], [9.5, 1.0], [8.5, 1.0], [8.5, 0.0]], [1, 2, 2, 2, 79]), ('board17', [[8.5, 1.0], [9.5, 1.0], [9.5, 2.0], [8.5, 2.0], [8.5, 1.0]], [1, 2, 2, 2, 79]), ('board18', [[8.5, 2.0], [9.5, 2.0], [9.5, 3.0], [8.5, 3.0], [8.5, 2.0]], [1, 2, 2, 2, 79]), ('board19', [[8.5, 3.0], [9.5, 3.0], [9.5, 4.0], [8.5, 4.0], [8.5, 3.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane418().draw(sys.argv[1] if len(sys.argv) > 1 else None))
