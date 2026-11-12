"""Frozen question Plane271; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane271:

    def __init__(self):
        self.id = 'Plane271'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:814'
        self.question = 'Both the figures on the right were made out of the same 5 pieces. The rectangle has dimensions $5 \\mathrm{~cm} \\times 10 \\mathrm{~cm}$. The other pieces are quarter circles with 2 different sized radii. What is the difference between the perimeters of the two figures?\nChoices:\nA:$2.5 \\mathrm{~cm}$\nB:$5 \\mathrm{~cm}$\nC:$10 \\mathrm{~cm}$\nD:$15 \\mathrm{~cm}$\nE:$20 \\mathrm{~cm}$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$2.5 \\mathrm{~cm}$', 'B': '$5 \\mathrm{~cm}$', 'C': '$10 \\mathrm{~cm}$', 'D': '$15 \\mathrm{~cm}$', 'E': '$20 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane271.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-6.270995846360126, 46.27099584636012), ylim=(-23.739270864245327, 28.802720828474925), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [10.0, 0.0], [10.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='left_rectangle', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.0, 0.0], [10.0, 0.0], [10.0, 5.0], [0.0, 5.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='left_rectangle', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, vertices, codes in [('left_large_up', [[10.0, 5.0], [10.0, 7.651147734913025], [8.94571235314983, 10.196423270581118], [7.0710678118654755, 12.071067811865476], [5.196423270581121, 13.94571235314983], [2.6511477349130255, 15.0], [6.123233995736766e-16, 15.0], [0.0, 5.0], [0.0, 5.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79]), ('left_large_down', [[0.0, 1.2246467991473533e-15], [0.0, -2.6511477349130237], [1.0542876468501685, -5.196423270581119], [2.9289321881345227, -7.071067811865475], [4.803576729418878, -8.94571235314983], [7.348852265086974, -10.0], [9.999999999999998, -10.0], [10.0, 0.0], [10.0, 0.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79]), ('left_small_left', [[3.061616997868383e-16, 5.0], [-1.325573867456512, 5.0], [-2.5982116352905593, 4.472856176574915], [-3.5355339059327373, 3.5355339059327378], [-4.472856176574915, 2.5982116352905607], [-5.0, 1.325573867456513], [-5.0, 6.123233995736766e-16], [0.0, 0.0], [0.0, 0.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79]), ('left_small_right', [[9.999999999999998, 0.0], [11.325573867456512, 0.0], [12.598211635290559, 0.5271438234250843], [13.535533905932738, 1.4644660940672614], [14.472856176574915, 2.401788364709439], [15.0, 3.674426132543487], [15.0, 4.999999999999999], [10.0, 5.0], [10.0, 5.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            c.path([[30.0, -5.0], [40.0, -5.0], [40.0, 0.0], [30.0, 0.0], [30.0, -5.0]], [1, 2, 2, 2, 79], id='right_rectangle', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[30.0, -5.0], [40.0, -5.0], [40.0, 0.0], [30.0, 0.0], [30.0, -5.0]], [1, 2, 2, 2, 79], id='right_rectangle', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, vertices, codes in [('right_large_right', [[45.0, 0.0], [45.0, 2.6511477349130246], [43.94571235314983, 5.196423270581119], [42.071067811865476, 7.071067811865475], [40.19642327058112, 8.94571235314983], [37.651147734913025, 10.0], [35.0, 10.0], [35.0, 0.0], [35.0, 0.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79]), ('right_large_left', [[35.0, 10.0], [32.348852265086975, 10.0], [29.803576729418882, 8.94571235314983], [27.928932188134524, 7.0710678118654755], [26.05428764685017, 5.196423270581121], [25.0, 2.651147734913026], [25.0, 1.2246467991473533e-15], [35.0, 0.0], [35.0, 0.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79]), ('right_small_left', [[25.0, 6.123233995736766e-16], [25.0, -1.3255738674565118], [25.527143823425085, -2.5982116352905593], [26.464466094067262, -3.5355339059327373], [27.40178836470944, -4.472856176574915], [28.674426132543488, -5.0], [30.0, -5.0], [30.0, 0.0], [30.0, 0.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79]), ('right_small_right', [[40.0, -5.0], [41.32557386745651, -5.0], [42.59821163529056, -4.472856176574916], [43.53553390593274, -3.5355339059327386], [44.472856176574915, -2.598211635290561], [45.0, -1.3255738674565134], [45.0, -1.2246467991473533e-15], [40.0, 0.0], [40.0, 0.0]], [1, 4, 4, 4, 4, 4, 4, 2, 79])]:
                c.path(vertices, codes, id=object_id, capstyle='butt')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane271().draw(sys.argv[1] if len(sys.argv) > 1 else None))
