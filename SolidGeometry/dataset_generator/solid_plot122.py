"""Frozen question Solid122; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid122:

    def __init__(self):
        self.id = 'Solid122'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:674'
        self.question = 'A pyramid is built from cubes, each with side length $10 \\mathrm{~cm}$. What is the length of the line drawn across the pyramid?\nChoices:\nA:$30 \\mathrm{~cm}$\nB:$60 \\mathrm{~cm}$\nC:$70 \\mathrm{~cm}$\nD:$80 \\mathrm{~cm}$\nE:$90 \\mathrm{~cm}$'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '$30 \\mathrm{~cm}$', 'B': '$60 \\mathrm{~cm}$', 'C': '$70 \\mathrm{~cm}$', 'D': '$80 \\mathrm{~cm}$', 'E': '$90 \\mathrm{~cm}$'}
        self.query = self.question
        self._geometry_01 = [('pyramide0', [[0.0, 0.0], [1.0, -0.05]]),
         ('pyramide1', [[0.0, 1.0], [1.0, 0.95]]),
         ('pyramide2', [[0.3, 1.55], [0.6499999999999999, 1.5325000000000002]]),
         ('pyramide3', [[0.0, 1.0], [0.3, 1.55]]),
         ('pyramide4', [[1.0, 0.95], [1.15, 1.225]]),
         ('pyramide5', [[0.0, 0.0], [0.0, 1.0]]),
         ('pyramide6', [[1.0, -0.05], [1.0, 0.95]]),
         ('pyramide7', [[0.6, 2.1], [0.65, 2.0975]]),
         ('pyramide8', [[0.3, 1.55], [0.6, 2.1]]),
         ('pyramide9', [[0.6, 2.1], [0.6500000000000999, 2.1916666666668503]]),
         ('pyramide10', [[1.0, -0.05], [2.0, -0.1]]),
         ('pyramide11', [[1.0, 0.95], [2.0, 0.9]]),
         ('pyramide12', [[2.0, 0.9], [2.15, 1.175]]),
         ('pyramide13', [[2.0, -0.1], [2.0, 0.9]]),
         ('pyramide14', [[2.0, -0.1], [3.0, -0.15000000000000002]]),
         ('pyramide15', [[2.0, 0.9], [3.0, 0.85]]),
         ('pyramide16', [[2.8, 1.425], [3.3, 1.4]]),
         ('pyramide17', [[3.0, -0.15000000000000002], [3.3, 0.4]]),
         ('pyramide18', [[3.0, 0.85], [3.3, 1.4]]),
         ('pyramide19', [[3.0, -0.15000000000000002], [3.0, 0.85]]),
         ('pyramide20', [[3.3, 0.4], [3.3, 1.4]]),
         ('pyramide21', [[3.1, 1.975], [3.6, 1.9500000000000002]]),
         ('pyramide22', [[3.3, 0.4], [3.6, 0.9500000000000001]]),
         ('pyramide23', [[3.3, 1.4], [3.6, 1.9500000000000002]]),
         ('pyramide24', [[3.6, 0.9500000000000001], [3.6, 1.9500000000000002]]),
         ('pyramide25', [[3.25, 2.5325], [3.9, 2.5]]),
         ('pyramide26', [[3.6, 0.9500000000000001], [3.9, 1.5]]),
         ('pyramide27', [[3.6, 1.9500000000000002], [3.9, 2.5]]),
         ('pyramide28', [[3.9, 1.5], [3.9, 2.5]]),
         ('pyramide29', [[0.65, 1.25], [1.65, 1.2]]),
         ('pyramide30', [[0.65, 2.25], [1.65, 2.2]]),
         ('pyramide31', [[0.95, 2.8], [1.3, 2.7825]]),
         ('pyramide32', [[0.65, 2.25], [0.95, 2.8]]),
         ('pyramide33', [[1.65, 2.2], [1.8, 2.475]]),
         ('pyramide34', [[0.65, 1.25], [0.65, 2.25]]),
         ('pyramide35', [[1.65, 1.2], [1.65, 2.2]]),
         ('pyramide36', [[1.25, 3.35], [1.3, 3.3475]]),
         ('pyramide37', [[0.95, 2.8], [1.25, 3.35]]),
         ('pyramide38', [[1.65, 1.2], [2.65, 1.15]]),
         ('pyramide39', [[1.65, 2.2], [2.65, 2.15]]),
         ('pyramide40', [[2.45, 2.725], [2.95, 2.7]]),
         ('pyramide41', [[2.65, 1.15], [2.95, 1.7000000000000002]]),
         ('pyramide42', [[2.65, 2.15], [2.95, 2.7]]),
         ('pyramide43', [[2.65, 1.15], [2.65, 2.15]]),
         ('pyramide44', [[2.95, 1.7000000000000002], [2.95, 2.7]]),
         ('pyramide45', [[2.6, 3.2825], [3.25, 3.25]]),
         ('pyramide46', [[2.95, 1.7000000000000002], [3.25, 2.25]]),
         ('pyramide47', [[2.95, 2.7], [3.25, 3.25]]),
         ('pyramide48', [[3.25, 2.25], [3.25, 3.25]]),
         ('pyramide49', [[1.3, 2.5], [2.3, 2.45]]),
         ('pyramide50', [[1.3, 3.5], [2.3, 3.45]]),
         ('pyramide51', [[1.6, 4.05], [2.6, 4.0]]),
         ('pyramide52', [[1.3, 3.5], [1.6, 4.05]]),
         ('pyramide53', [[2.3, 2.45], [2.6, 3.0]]),
         ('pyramide54', [[2.3, 3.45], [2.6, 4.0]]),
         ('pyramide55', [[1.3, 2.5], [1.3, 3.5]]),
         ('pyramide56', [[2.3, 2.45], [2.3, 3.45]]),
         ('pyramide57', [[2.6, 3.0], [2.6, 4.0]])]
        self._geometry_02 = [('plan0000', [[5.6, 0.0], [8.6, 0.0]]),
         ('plan0010', [[5.6, 1.0], [6.1, 1.0]]),
         ('plan0012', [[8.1, 1.0], [8.6, 1.0]]),
         ('plan0020', [[5.6, 1.9999999999999998], [6.1, 2.0]]),
         ('plan0022', [[8.1, 2.0], [8.6, 2.0]]),
         ('plan0030', [[5.6, 3.0], [8.6, 3.0]]),
         ('plan0100', [[5.6, 0.0], [5.6, 3.0]]),
         ('plan0110', [[6.6, 0.0], [6.6, 0.5]]),
         ('plan0112', [[6.6, 2.5], [6.6, 3.0]]),
         ('plan0120', [[7.6, 0.0], [7.6, 0.5]]),
         ('plan0122', [[7.6, 2.5], [7.6, 3.0]]),
         ('plan0130', [[8.6, 0.0], [8.6, 3.0]]),
         ('plan1000', [[6.1, 0.49999999999999994], [8.1, 0.5]]),
         ('plan1010', [[6.1, 1.5], [6.6, 1.5]]),
         ('plan1012', [[7.6, 1.5], [8.1, 1.5]]),
         ('plan1020', [[6.1, 2.5], [8.1, 2.5]]),
         ('plan1100', [[6.1, 0.49999999999999994], [6.1, 2.5]]),
         ('plan1110', [[7.1, 0.5], [7.1, 1.0]]),
         ('plan1112', [[7.1, 2.0], [7.1, 2.5]]),
         ('plan1120', [[8.1, 0.5], [8.1, 2.5]]),
         ('plan2000', [[6.6, 1.0], [7.6, 0.9999999999999999]]),
         ('plan2010', [[6.6, 2.0], [7.6, 2.0]]),
         ('plan2100', [[6.6, 1.0], [6.6, 2.0]]),
         ('plan2110', [[7.6, 0.9999999999999999], [7.6, 2.0]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid122.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=(-0.21418436345096392, 8.827205196784298), ylim=(-2.5772051967842966, 6.464184363450965), axes_position=(0.05, 0.050000000000000114, 0.9, 0.8999999999999998), coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, points in [('route1part0', [[0.44999999999999996, 1.8250000000000002], [0.65, 1.815]]), ('route3part0', [[0.95, 2.8], [1.3, 2.7825]]), ('route5part0', [[1.45, 3.775], [2.45, 3.725]]), ('route6part0', [[2.45, 3.725], [2.45, 2.725]]), ('route7part0', [[2.45, 2.725], [2.95, 2.7]]), ('route8part0', [[2.95, 2.7], [2.95, 1.7000000000000002]]), ('route9part0', [[2.95, 1.7000000000000002], [3.45, 1.675]]), ('route10part0', [[3.45, 1.675], [3.45, 0.675]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False, color='#D71920')
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[5.6, 1.5], [8.6, 1.5]], id='planroute', zorder=3, clip_on=False, color='#D71920')
            for object_id, vertices, codes in [('route_ribbon10', [[0.423, 1.7755], [0.65, 1.7641499999999999], [0.6499999999999999, 1.86585], [0.477, 1.8745000000000003], [0.423, 1.7755]], [1, 2, 2, 2, 79]), ('route_ribbon30', [[0.9229999999999999, 2.7505], [1.3, 2.73165], [1.3, 2.8333500000000003], [0.9769999999999999, 2.8495000000000004], [0.9229999999999999, 2.7505]], [1, 2, 2, 2, 79]), ('route_ribbon50', [[1.423, 3.7255000000000003], [2.423, 3.6755], [2.477, 3.7745000000000006], [1.4769999999999999, 3.8245000000000005], [1.423, 3.7255000000000003]], [1, 2, 2, 2, 79]), ('route_ribbon60', [[2.423, 3.6755], [2.423, 2.6755], [2.477, 2.7745], [2.477, 3.7745], [2.423, 3.6755]], [1, 2, 2, 2, 79]), ('route_ribbon70', [[2.423, 2.6755], [2.923, 2.6505], [2.9769999999999994, 2.7495000000000003], [2.477, 2.7745], [2.423, 2.6755]], [1, 2, 2, 2, 79]), ('route_ribbon80', [[2.923, 2.6505], [2.923, 1.6505], [2.977, 1.7495000000000003], [2.977, 2.7495000000000003], [2.923, 2.6505]], [1, 2, 2, 2, 79]), ('route_ribbon90', [[2.923, 1.6505], [3.423, 1.6254999999999997], [3.477, 1.7245], [2.9769999999999994, 1.7495000000000003], [2.923, 1.6505]], [1, 2, 2, 2, 79]), ('route_ribbon100', [[3.423, 1.6255], [3.423, 0.6255], [3.477, 0.7245000000000003], [3.477, 1.7245000000000001], [3.423, 1.6255]], [1, 2, 2, 2, 79]), ('plan_route_ribbon', [[5.6, 1.41], [8.6, 1.41], [8.6, 1.59], [5.6, 1.59], [5.6, 1.41]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.text('Ansicht von oben', (7.1, 3.0), id='planheading', rotation_mode='default', offset_pt=(0, 24), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid122().draw(sys.argv[1] if len(sys.argv) > 1 else None))
