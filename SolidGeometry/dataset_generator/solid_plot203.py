"""Frozen question Solid203; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid203:

    def __init__(self):
        self.id = 'Solid203'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1943'
        self.question = 'The diagram shows a net of an octahedron. When this is folded to form the octahedron, which of the labelled line segments will coincide with the line segment labelled $x$?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid203.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-0.7464591045963274, 6.6172477514564), ylim=(-3.2488407261341443, 4.114866129918583), axes_position=(0.05, 0.05000000000000006, 0.9, 0.8999999999999999), coordinate_axes=False) as c:
            for object_id, vertices, codes in [('face40', [[5.528452523744346, -0.5562422413460985], [5.40952674073674, 0.065], [6.445253957014124, 0.35], [5.528452523744346, -0.5562422413460985]], [1, 2, 2, 79]), ('face39', [[5.528452523744346, -0.5562422413460985], [4.554746042985876, 0.35], [5.40952674073674, 0.065], [5.528452523744346, -0.5562422413460985]], [1, 2, 2, 79]), ('face38', [[5.471547476255654, 1.2562422413460985], [5.40952674073674, 0.065], [6.445253957014124, 0.35], [5.471547476255654, 1.2562422413460985]], [1, 2, 2, 79]), ('face37', [[5.471547476255654, 1.2562422413460985], [4.554746042985876, 0.35], [5.40952674073674, 0.065], [5.471547476255654, 1.2562422413460985]], [1, 2, 2, 79]), ('face7', [[2.0, 0.0], [3.0, 0.0], [2.5, -0.8660254037844386], [2.0, 0.0]], [1, 2, 2, 79]), ('face6', [[2.0, 0.0], [2.5, 0.8660254037844386], [3.0, 0.0], [2.0, 0.0]], [1, 2, 2, 79]), ('face5', [[1.5, 0.8660254037844386], [2.0, 0.0], [2.5, 0.8660254037844386], [1.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face4', [[1.0, 0.0], [1.5, 0.8660254037844386], [2.0, 0.0], [1.0, 0.0]], [1, 2, 2, 79]), ('face3', [[0.5, 0.8660254037844386], [1.0, 0.0], [1.5, 0.8660254037844386], [0.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face2', [[0.5, 0.8660254037844386], [0.0, 0.0], [1.0, 0.0], [0.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face1', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386], [0.0, 0.0], [-0.5, 0.8660254037844386]], [1, 2, 2, 79]), ('face0', [[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772], [0.5, 0.8660254037844386], [-0.5, 0.8660254037844386]], [1, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            for object_id, points in [('line_8', [[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]]), ('line_9', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('line_10', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('line_11', [[0.0, 0.0], [1.0, 0.0]]), ('line_12', [[2.0, 0.0], [3.0, 0.0]]), ('line_13', [[-0.5, 0.8660254037844386], [0.0, 0.0]]), ('line_14', [[1.0, 0.0], [2.0, 0.0]]), ('line_15', [[1.5, 0.8660254037844386], [2.5, 0.8660254037844386]]), ('line_16', [[0.5, 0.8660254037844386], [0.0, 0.0]]), ('line_17', [[2.0, 0.0], [2.5, 0.8660254037844386]]), ('line_18', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('line_19', [[1.0, 0.0], [1.5, 0.8660254037844386]]), ('line_20', [[3.0, 0.0], [2.5, -0.8660254037844386]]), ('line_21', [[1.5, 0.8660254037844386], [2.0, 0.0]]), ('line_22', [[0.5, 0.8660254037844386], [1.5, 0.8660254037844386]]), ('line_23', [[2.0, 0.0], [2.5, -0.8660254037844386]]), ('line_24', [[2.5, 0.8660254037844386], [3.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[6.445253957014124, 0.35], [5.59047325926326, 0.635]], id='line_25', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('line_26', [[6.445253957014124, 0.35], [5.40952674073674, 0.065]]), ('line_27', [[6.445253957014124, 0.35], [5.471547476255654, 1.2562422413460985]]), ('line_28', [[6.445253957014124, 0.35], [5.528452523744346, -0.5562422413460985]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[4.554746042985876, 0.35], [5.59047325926326, 0.635]], id='line_29', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, points in [('line_30', [[4.554746042985876, 0.35], [5.40952674073674, 0.065]]), ('line_31', [[4.554746042985876, 0.35], [5.471547476255654, 1.2562422413460985]]), ('line_32', [[4.554746042985876, 0.35], [5.528452523744346, -0.5562422413460985]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[5.59047325926326, 0.635], [5.471547476255654, 1.2562422413460985]], id='line_33', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[5.59047325926326, 0.635], [5.528452523744346, -0.5562422413460985]], id='line_34', clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[5.40952674073674, 0.065], [5.471547476255654, 1.2562422413460985]], id='line_35', zorder=3, clip_on=False)
            c.line([[5.40952674073674, 0.065], [5.528452523744346, -0.5562422413460985]], id='line_36', zorder=3, clip_on=False)
            c.text('C', (-0.25, 1.299038105676658), id='label_0', rotation_mode='default', offset_pt=(-18, 6), annotation_clip=None)
            c.text('D', (-0.25, 0.4330127018922193), id='label_1', rotation_mode='default', offset_pt=(-18, 0), annotation_clip=None)
            c.text('E', (0.5, 0.0), id='label_2', rotation_mode='default', offset_pt=(0, -18), annotation_clip=None)
            c.text('B', (2.0, 0.8660254037844386), id='label_3', rotation_mode='default', offset_pt=(0, 18), annotation_clip=None)
            c.text('A', (2.75, 0.4330127018922193), id='label_4', rotation_mode='default', offset_pt=(18, 3), annotation_clip=None)
            c.text('x', (2.75, -0.4330127018922193), id='label_5', rotation_mode='default', offset_pt=(18, -3), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid203().draw(sys.argv[1] if len(sys.argv) > 1 else None))
