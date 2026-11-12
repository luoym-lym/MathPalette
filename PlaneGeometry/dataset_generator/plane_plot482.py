"""Frozen question Plane482; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane482:

    def __init__(self):
        self.id = 'Plane482'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2792'
        self.question = 'Each square in a $3 \\times 3$ grid is randomly filled with one of the $4$ gray-and-white tiles shown below on the right.\nWhat is the probability that the tiling will contain a large gray diamond in one of the smaller $2\\times 2$ grids? Below is an example of one such tiling.\nChoices:\nA:$\\frac{1}{1024}$\nB:$\\frac{1}{256}$\nC:$\\frac{1}{64}$\nD:$\\frac{1}{16}$\nE:$\\frac{1}{4}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$\\frac{1}{1024}$', 'B': '$\\frac{1}{256}$', 'C': '$\\frac{1}{64}$', 'D': '$\\frac{1}{16}$', 'E': '$\\frac{1}{4}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane482.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.2081801955625684, 8.622165939631394], ylim=[-0.4221609148192029, 8.40818522037476], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('blank00', [[0.0, 5.0], [1.0, 5.0], [1.0, 6.0], [0.0, 6.0], [0.0, 5.0]], [1, 2, 2, 2, 79]), ('blank01', [[0.0, 6.0], [1.0, 6.0], [1.0, 7.0], [0.0, 7.0], [0.0, 6.0]], [1, 2, 2, 2, 79]), ('blank02', [[0.0, 7.0], [1.0, 7.0], [1.0, 8.0], [0.0, 8.0], [0.0, 7.0]], [1, 2, 2, 2, 79]), ('blank10', [[1.0, 5.0], [2.0, 5.0], [2.0, 6.0], [1.0, 6.0], [1.0, 5.0]], [1, 2, 2, 2, 79]), ('blank11', [[1.0, 6.0], [2.0, 6.0], [2.0, 7.0], [1.0, 7.0], [1.0, 6.0]], [1, 2, 2, 2, 79]), ('blank12', [[1.0, 7.0], [2.0, 7.0], [2.0, 8.0], [1.0, 8.0], [1.0, 7.0]], [1, 2, 2, 2, 79]), ('blank20', [[2.0, 5.0], [3.0, 5.0], [3.0, 6.0], [2.0, 6.0], [2.0, 5.0]], [1, 2, 2, 2, 79]), ('blank21', [[2.0, 6.0], [3.0, 6.0], [3.0, 7.0], [2.0, 7.0], [2.0, 6.0]], [1, 2, 2, 2, 79]), ('blank22', [[2.0, 7.0], [3.0, 7.0], [3.0, 8.0], [2.0, 8.0], [2.0, 7.0]], [1, 2, 2, 2, 79]), ('tile0', [[6.0, 6.7], [7.0, 6.7], [7.0, 7.7], [6.0, 7.7], [6.0, 6.7]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 6.7], [6.0, 7.7], [7.0, 7.7], [6.0, 6.7]], [1, 2, 2, 79], id='graytile0', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 6.7], [6.0, 7.7], [7.0, 7.7], [6.0, 6.7]], [1, 2, 2, 79], id='graytile0', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.4, 6.7], [8.4, 6.7], [8.4, 7.7], [7.4, 7.7], [7.4, 6.7]], [1, 2, 2, 2, 79], id='tile1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[7.4, 7.7], [8.4, 7.7], [8.4, 6.7], [7.4, 7.7]], [1, 2, 2, 79], id='graytile1', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[7.4, 7.7], [8.4, 7.7], [8.4, 6.7], [7.4, 7.7]], [1, 2, 2, 79], id='graytile1', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.0, 5.3], [7.0, 5.3], [7.0, 6.3], [6.0, 6.3], [6.0, 5.3]], [1, 2, 2, 2, 79], id='tile2', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[6.0, 5.3], [7.0, 5.3], [7.0, 6.3], [6.0, 5.3]], [1, 2, 2, 79], id='graytile2', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 5.3], [7.0, 5.3], [7.0, 6.3], [6.0, 5.3]], [1, 2, 2, 79], id='graytile2', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[7.4, 5.3], [8.4, 5.3], [8.4, 6.3], [7.4, 6.3], [7.4, 5.3]], [1, 2, 2, 2, 79], id='tile3', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[7.4, 5.3], [8.4, 5.3], [7.4, 6.3], [7.4, 5.3]], [1, 2, 2, 79], id='graytile3', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[7.4, 5.3], [8.4, 5.3], [7.4, 6.3], [7.4, 5.3]], [1, 2, 2, 79], id='graytile3', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.5, 2.0], [3.5, 2.0], [3.5, 3.0], [2.5, 3.0], [2.5, 2.0]], [1, 2, 2, 2, 79], id='eg00', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.5, 3.0], [3.5, 3.0], [3.5, 2.0], [2.5, 3.0]], [1, 2, 2, 79], id='eggray00', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 3.0], [3.5, 3.0], [3.5, 2.0], [2.5, 3.0]], [1, 2, 2, 79], id='eggray00', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.5, 2.0], [4.5, 2.0], [4.5, 3.0], [3.5, 3.0], [3.5, 2.0]], [1, 2, 2, 2, 79], id='eg01', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.5, 2.0], [4.5, 2.0], [4.5, 3.0], [3.5, 2.0]], [1, 2, 2, 79], id='eggray01', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.5, 2.0], [4.5, 2.0], [4.5, 3.0], [3.5, 2.0]], [1, 2, 2, 79], id='eggray01', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.5, 2.0], [5.5, 2.0], [5.5, 3.0], [4.5, 3.0], [4.5, 2.0]], [1, 2, 2, 2, 79], id='eg02', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[4.5, 3.0], [5.5, 3.0], [5.5, 2.0], [4.5, 3.0]], [1, 2, 2, 79], id='eggray02', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[4.5, 3.0], [5.5, 3.0], [5.5, 2.0], [4.5, 3.0]], [1, 2, 2, 79], id='eggray02', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.5, 1.0], [3.5, 1.0], [3.5, 2.0], [2.5, 2.0], [2.5, 1.0]], [1, 2, 2, 2, 79], id='eg10', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.5, 1.0], [3.5, 1.0], [2.5, 2.0], [2.5, 1.0]], [1, 2, 2, 79], id='eggray10', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 1.0], [3.5, 1.0], [2.5, 2.0], [2.5, 1.0]], [1, 2, 2, 79], id='eggray10', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.5, 1.0], [4.5, 1.0], [4.5, 2.0], [3.5, 2.0], [3.5, 1.0]], [1, 2, 2, 2, 79], id='eg11', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.5, 1.0], [4.5, 1.0], [4.5, 2.0], [3.5, 1.0]], [1, 2, 2, 79], id='eggray11', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.5, 1.0], [4.5, 1.0], [4.5, 2.0], [3.5, 1.0]], [1, 2, 2, 79], id='eggray11', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.5, 1.0], [5.5, 1.0], [5.5, 2.0], [4.5, 2.0], [4.5, 1.0]], [1, 2, 2, 2, 79], id='eg12', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[4.5, 1.0], [5.5, 1.0], [4.5, 2.0], [4.5, 1.0]], [1, 2, 2, 79], id='eggray12', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[4.5, 1.0], [5.5, 1.0], [4.5, 2.0], [4.5, 1.0]], [1, 2, 2, 79], id='eggray12', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[2.5, 0.0], [3.5, 0.0], [3.5, 1.0], [2.5, 1.0], [2.5, 0.0]], [1, 2, 2, 2, 79], id='eg20', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[2.5, 1.0], [3.5, 1.0], [3.5, 0.0], [2.5, 1.0]], [1, 2, 2, 79], id='eggray20', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[2.5, 1.0], [3.5, 1.0], [3.5, 0.0], [2.5, 1.0]], [1, 2, 2, 79], id='eggray20', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[3.5, 0.0], [4.5, 0.0], [4.5, 1.0], [3.5, 1.0], [3.5, 0.0]], [1, 2, 2, 2, 79], id='eg21', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[3.5, 1.0], [4.5, 1.0], [4.5, 0.0], [3.5, 1.0]], [1, 2, 2, 79], id='eggray21', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[3.5, 1.0], [4.5, 1.0], [4.5, 0.0], [3.5, 1.0]], [1, 2, 2, 79], id='eggray21', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[4.5, 0.0], [5.5, 0.0], [5.5, 1.0], [4.5, 1.0], [4.5, 0.0]], [1, 2, 2, 2, 79], id='eg22', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.path([[4.5, 0.0], [4.5, 1.0], [5.5, 1.0], [4.5, 0.0]], [1, 2, 2, 79], id='eggray22', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[4.5, 0.0], [4.5, 1.0], [5.5, 1.0], [4.5, 0.0]], [1, 2, 2, 79], id='eggray22', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane482().draw(sys.argv[1] if len(sys.argv) > 1 else None))
