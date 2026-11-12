"""Frozen question Plane327; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane327:

    def __init__(self):
        self.id = 'Plane327'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1047'
        self.question = 'The star shown in the picture is made by fitting together 12 congruent equilateral triangles. The perimeter of the star is $36 \\mathrm{~cm}$. What is the perimeter of the grey hexagon?\nChoices:\nA:$6 \\mathrm{~cm}$\nB:$12 \\mathrm{~cm}$\nC:$18 \\mathrm{~cm}$\nD:$24 \\mathrm{~cm}$\nE:$30 \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$6 \\mathrm{~cm}$', 'B': '$12 \\mathrm{~cm}$', 'C': '$18 \\mathrm{~cm}$', 'D': '$24 \\mathrm{~cm}$', 'E': '$30 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane327.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.8186437668909106, 1.8240564256645628], ylim=[-1.8213500962777365, 1.821350096277737], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[1.0, 0.0], [0.5000000000000001, 0.8660254037844386], [-0.4999999999999998, 0.8660254037844387], [-1.0, 1.2246467991473532e-16], [-0.5000000000000004, -0.8660254037844384], [0.5000000000000001, -0.8660254037844386], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='hexagon', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [0.5000000000000001, 0.8660254037844386], [-0.4999999999999998, 0.8660254037844387], [-1.0, 1.2246467991473532e-16], [-0.5000000000000004, -0.8660254037844384], [0.5000000000000001, -0.8660254037844386], [1.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='hexagon', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            for object_id, points in [('spoke0', [[0.0, 0.0], [1.0, 0.0]]), ('outer0a', [[1.0, 0.0], [1.5, 0.8660254037844386]]), ('outer0b', [[1.5, 0.8660254037844386], [0.5000000000000001, 0.8660254037844386]]), ('spoke1', [[0.0, 0.0], [0.5000000000000001, 0.8660254037844386]]), ('outer1a', [[0.5000000000000001, 0.8660254037844386], [3.3306690738754696e-16, 1.7320508075688772]]), ('outer1b', [[3.3306690738754696e-16, 1.7320508075688772], [-0.4999999999999998, 0.8660254037844387]]), ('spoke2', [[0.0, 0.0], [-0.4999999999999998, 0.8660254037844387]]), ('outer2a', [[-0.4999999999999998, 0.8660254037844387], [-1.4999999999999998, 0.8660254037844388]]), ('outer2b', [[-1.4999999999999998, 0.8660254037844388], [-1.0, 1.2246467991473532e-16]]), ('spoke3', [[0.0, 0.0], [-1.0, 1.2246467991473532e-16]]), ('outer3a', [[-1.0, 1.2246467991473532e-16], [-1.5000000000000004, -0.8660254037844383]]), ('outer3b', [[-1.5000000000000004, -0.8660254037844383], [-0.5000000000000004, -0.8660254037844384]]), ('spoke4', [[0.0, 0.0], [-0.5000000000000004, -0.8660254037844384]]), ('outer4a', [[-0.5000000000000004, -0.8660254037844384], [-3.3306690738754696e-16, -1.732050807568877]]), ('outer4b', [[-3.3306690738754696e-16, -1.732050807568877], [0.5000000000000001, -0.8660254037844386]]), ('spoke5', [[0.0, 0.0], [0.5000000000000001, -0.8660254037844386]]), ('outer5a', [[0.5000000000000001, -0.8660254037844386], [1.5, -0.8660254037844386]]), ('outer5b', [[1.5, -0.8660254037844386], [1.0, 0.0]])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane327().draw(sys.argv[1] if len(sys.argv) > 1 else None))
