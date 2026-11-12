"""Frozen question Solid103; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid103:

    def __init__(self):
        self.id = 'Solid103'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:344'
        self.question = 'Two rectangular blocks and a cube are joined to form a larger rectangular block with volume $280 \\mathrm{~cm}^{3}$. The dark gray cube in the picture has volume $125 \\mathrm{~cm}^{3}$, and the smaller rectangular block has volume $75 \\mathrm{~cm}^{3}$. What is the area of the face marked with the question mark?\nChoices:\nA:$16 \\mathrm{~cm}^{2}$\nB:$18 \\mathrm{~cm}^{2}$\nC:$20 \\mathrm{~cm}^{2}$\nD:$24 \\mathrm{~cm}^{2}$\nE:$56 \\mathrm{~cm}^{2}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$16 \\mathrm{~cm}^{2}$', 'B': '$18 \\mathrm{~cm}^{2}$', 'C': '$20 \\mathrm{~cm}^{2}$', 'D': '$24 \\mathrm{~cm}^{2}$', 'E': '$56 \\mathrm{~cm}^{2}$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid103.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-3.4362056766099185, 8.286141266199621], ylim=[-1.4811734714047713, 10.24117347140477], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('edge0', [[0.0, 0.0], [8.0, 0.96]]), ('edge1', [[0.0, 0.0], [0.0, 5.0]]), ('edge2', [[8.0, 0.96], [8.0, 5.96]]), ('edge3', [[0.0, 5.0], [8.0, 5.96]]), ('edge4', [[0.0, 0.0], [-3.15, 2.8000000000000003]]), ('edge5', [[-3.15, 2.8000000000000003], [-3.15, 7.800000000000001]]), ('edge6', [[-3.15, 7.800000000000001], [4.85, 8.76]]), ('edge7', [[4.85, 8.76], [8.0, 5.96]]), ('edge8', [[-3.15, 7.800000000000001], [0.0, 5.0]]), ('edge9', [[3.0, 0.36], [3.0, 5.36]]), ('edge10', [[3.0, 5.36], [0.75, 7.36]]), ('edge11', [[-2.25, 7.0], [5.75, 7.96]]), ('edge12', [[-2.25, 2.0], [-2.25, 7.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[3.0, 0.36], [8.0, 0.96], [8.0, 5.96], [3.0, 5.36], [3.0, 0.36]], [1, 2, 2, 2, 79], id='cube_front', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 5.36], [8.0, 5.96], [5.75, 7.96], [0.75, 7.36], [3.0, 5.36]], [1, 2, 2, 2, 79], id='cube_top', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            c.text('?', [1.2999999999999998, 7.880000000000001], id='unknown', rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid103().draw(sys.argv[1] if len(sys.argv) > 1 else None))
