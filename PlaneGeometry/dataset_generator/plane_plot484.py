"""Frozen question Plane484; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane484:

    def __init__(self):
        self.id = 'Plane484'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2835'
        self.question = 'Two rays with a common endpoint A0 form an angle of $1^o$. Construct a sequence of points $A_0$, $. . . $, $A_n$ such that for all $1 \\le i \\le n$, $|A_{i-1}A_i | = 1$, and $|A_iA_0| > |A_{i-1}A_0|$. Find the largest possible value of $n$.'
        self.answer = '90'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane484.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.7979590628601558, 10.255929051848774), ylim=(-5.517626338927463, 5.536261775781468), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            c.line([[0.0, 0.0], [9.999619230641713, -0.08726535498373934]], id='o0')
            c.path([[9.999619230641713, -0.08726535498373934], [9.89992846707774, -0.051394034126655955], [9.899317609592853, -0.12139136874114793], [9.999619230641713, -0.08726535498373934]], [1, 2, 2, 79], id='o1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.999619230641713, -0.08726535498373934], [9.89992846707774, -0.051394034126655955], [9.899317609592853, -0.12139136874114793], [9.999619230641713, -0.08726535498373934]], [1, 2, 2, 79], id='o1', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[0.0, 0.0], [9.999619230641713, 0.08726535498373934]], id='o2')
            c.path([[9.999619230641713, 0.08726535498373934], [9.899317609592853, 0.12139136874114793], [9.89992846707774, 0.051394034126655955], [9.999619230641713, 0.08726535498373934]], [1, 2, 2, 79], id='o3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[9.999619230641713, 0.08726535498373934], [9.899317609592853, 0.12139136874114793], [9.89992846707774, 0.051394034126655955], [9.999619230641713, 0.08726535498373934]], [1, 2, 2, 79], id='o3', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('o4', [[0.0, 0.0], [0.9999619230641713, 0.008726535498373935]]), ('o5', [[0.9999619230641713, 0.008726535498373935], [1.9996192480397286, -0.017450412809499216]]), ('o6', [[1.9996192480397286, -0.017450412809499216], [2.9986674696215867, 0.026168974555836784]]), ('o7', [[2.9986674696215867, 0.026168974555836784], [3.9968022680434534, -0.03487956497902009]])]:
                c.line(points, id=object_id)
            for object_id, points in [('o8', [[3.9968022680434534, -0.03487956497902009], [4.993719601776581, 0.043579530748824855]]), ('o9', [[4.993719601776581, 0.043579530748824855], [5.989115800143761, -0.05226622177139914]]), ('o10', [[5.989115800143761, -0.05226622177139914], [6.982687655820348, 0.06093699199650759]]), ('o11', [[6.982687655820348, 0.06093699199650759], [7.974132517194158, -0.069589200223544]])]:
                c.line(points, id=object_id, linestyle=(0.0, [4.0, 3.0]))
            c.text('$A_{0}$', (0.0, 0.0), id='lA0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-14, 0), annotation_clip=None)
            c.text('$A_{1}$', (0.9999619230641713, 0.008726535498373935), id='lA1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
            c.text('$A_{2}$', (1.9996192480397286, -0.017450412809499216), id='lA2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
            c.text('$A_{3}$', (2.9986674696215867, 0.026168974555836784), id='lA3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, 16), annotation_clip=None)
            c.text('$A_{4}$', (3.9968022680434534, -0.03487956497902009), id='lA4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -16), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane484().draw(sys.argv[1] if len(sys.argv) > 1 else None))
