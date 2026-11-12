"""Frozen question Plane314; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane314:

    def __init__(self):
        self.id = 'Plane314'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:986'
        self.question = 'The arrangement shown consists of square tiles of different sizes. The smallest tile has a perimeter of $80 \\mathrm{~cm}$. What is the length of the path shown along the edges of the tiles?\nChoices:\nA:$380 \\mathrm{~cm}$\nB:$400 \\mathrm{~cm}$\nC:$420 \\mathrm{~cm}$\nD:$440 \\mathrm{~cm}$\nE:$1680 \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$380 \\mathrm{~cm}$', 'B': '$400 \\mathrm{~cm}$', 'C': '$420 \\mathrm{~cm}$', 'D': '$440 \\mathrm{~cm}$', 'E': '$1680 \\mathrm{~cm}$'}
        self.query = self.question
        self._geometry_01 = [[0.12, 0.88],
         [0.175692651, 0.88],
         [0.2291117728648192, 0.892643957009411],
         [0.26849242404917495, 0.9151471862576143],
         [0.30787307523353075, 0.9376504155058176],
         [0.32999999999999996, 0.968175628],
         [0.32999999999999996, 1.0],
         [0.32999999999999996, 1.031824372],
         [0.30787307523353075, 1.0623495844941824],
         [0.26849242404917495, 1.0848528137423856],
         [0.2291117728648192, 1.107356042990589],
         [0.175692651, 1.12],
         [0.12, 1.12],
         [0.06430734899999999, 1.12],
         [0.01088822713518077, 1.107356042990589],
         [-0.028492424049174986, 1.0848528137423856],
         [-0.06787307523353076, 1.0623495844941824],
         [-0.09, 1.031824372],
         [-0.09, 1.0],
         [-0.09, 0.968175628],
         [-0.06787307523353076, 0.9376504155058176],
         [-0.028492424049174986, 0.9151471862576143],
         [0.01088822713518077, 0.892643957009411],
         [0.06430734899999999, 0.88],
         [0.12, 0.88],
         [0.12, 0.88]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self._geometry_03 = [[0.03, 1.0374999999999999],
         [0.03596706975, 1.0374999999999999],
         [0.0416905470926592, 1.0393439103972058],
         [0.04590990257669732, 1.0426256313292352],
         [0.05012925806073544, 1.045907352261265],
         [0.0525, 1.05035894575],
         [0.0525, 1.055],
         [0.0525, 1.0596410542499999],
         [0.05012925806073544, 1.064092647738735],
         [0.04590990257669732, 1.0673743686707646],
         [0.0416905470926592, 1.0706560896027941],
         [0.03596706975, 1.0725],
         [0.03, 1.0725],
         [0.024032930249999997, 1.0725],
         [0.018309452907340797, 1.0706560896027941],
         [0.01409009742330268, 1.0673743686707646],
         [0.00987074193926456, 1.064092647738735],
         [0.0075, 1.0596410542499999],
         [0.0075, 1.055],
         [0.0075, 1.05035894575],
         [0.00987074193926456, 1.045907352261265],
         [0.01409009742330268, 1.0426256313292352],
         [0.018309452907340797, 1.0393439103972058],
         [0.024032930249999997, 1.0374999999999999],
         [0.03, 1.0374999999999999],
         [0.03, 1.0374999999999999]]
        self._geometry_04 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 79]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane314.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.26747776780862687, 7.191554607031674), ylim=(-1.2360245996826928, 6.223007775157608), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            c.path([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='tile0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='tile0', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='tile1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [1.0, 2.0], [0.0, 2.0], [0.0, 1.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='tile1', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 0.0], [3.0, 2.0], [1.0, 2.0], [1.0, 0.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='tile2', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [3.0, 2.0], [1.0, 2.0], [1.0, 0.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='tile2', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[3.0, 2.0], [3.0, 5.0], [0.0, 5.0], [0.0, 2.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='tile3', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.0, 2.0], [3.0, 5.0], [0.0, 5.0], [0.0, 2.0], [3.0, 2.0]], [1, 2, 2, 2, 79], id='tile3', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='tile4', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.0, 0.0], [5.0, 2.0], [3.0, 2.0], [3.0, 0.0], [5.0, 0.0]], [1, 2, 2, 2, 79], id='tile4', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='tile5', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 2.0], [4.0, 3.0], [3.0, 3.0], [3.0, 2.0], [4.0, 2.0]], [1, 2, 2, 2, 79], id='tile5', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='tile6', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 3.0], [4.0, 4.0], [3.0, 4.0], [3.0, 3.0], [4.0, 3.0]], [1, 2, 2, 2, 79], id='tile6', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='tile7', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[4.0, 4.0], [4.0, 5.0], [3.0, 5.0], [3.0, 4.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='tile7', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[7.0, 0.0], [7.0, 2.0], [5.0, 2.0], [5.0, 0.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='tile8', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 0.0], [7.0, 2.0], [5.0, 2.0], [5.0, 0.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='tile8', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.path([[7.0, 2.0], [7.0, 5.0], [4.0, 5.0], [4.0, 2.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='tile9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[7.0, 2.0], [7.0, 5.0], [4.0, 5.0], [4.0, 2.0], [7.0, 2.0]], [1, 2, 2, 2, 79], id='tile9', edgecolor=(0.6, 0.6, 0.6, 1.0), facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('thick_snake0', [[0.0, 1.0], [1.0, 1.0]]), ('thick_snake1', [[1.0, 1.0], [1.0, 2.0]]), ('thick_snake2', [[1.0, 2.0], [3.0, 2.0]]), ('thick_snake3', [[3.0, 2.0], [3.0, 0.0]]), ('thick_snake4', [[3.0, 0.0], [5.0, 0.0]]), ('thick_snake5', [[5.0, 0.0], [5.0, 2.0]]), ('thick_snake6', [[5.0, 2.0], [7.0, 2.0]]), ('thick_snake7', [[7.0, 2.0], [7.0, 5.0]]), ('thick_snake8', [[7.0, 5.0], [3.0, 5.0]]), ('thick_snake9', [[3.0, 5.0], [3.0, 4.0]]), ('thick_snake10', [[3.0, 4.0], [4.0, 4.0]])]:
                c.line(points, id=object_id)
            c.path(self._geometry_01, self._geometry_02, id='snake_head', zorder=4, facecolor=(0.0, 0.0, 0.0, 1.0), capstyle='butt')
            c.path(self._geometry_03, self._geometry_04, id='snake_eye', zorder=4, facecolor=(1.0, 1.0, 1.0, 1.0), capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane314().draw(sys.argv[1] if len(sys.argv) > 1 else None))
