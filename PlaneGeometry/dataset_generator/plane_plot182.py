"""Frozen question Plane182; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane182:

    def __init__(self):
        self.id = 'Plane182'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:254'
        self.question = 'An equilateral triangle is being rolled around a unit square as shown. How long is the path that the point shown covers, if the point and the triangle are both back at the start for the first time?\nChoices:\nA:$4 \\pi$\nB:$\\frac{28}{3} \\pi$\nC:$8 \\pi$\nD:$\\frac{14}{3} \\pi$\nE:$\\frac{21}{2} \\pi$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$4 \\pi$', 'B': '$\\frac{28}{3} \\pi$', 'C': '$8 \\pi$', 'D': '$\\frac{14}{3} \\pi$', 'E': '$\\frac{21}{2} \\pi$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane182.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-0.16507686668682142, 6.820494610532217), ylim=(-2.5159772895354453, 4.469594187683594), axes_position=(0.050000000000000114, 0.05, 0.8999999999999998, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('o0', [[0.0, 0.0], [1.0, 0.0]]), ('o1', [[1.0, 0.0], [1.0, 1.0]]), ('o2', [[1.0, 1.0], [0.0, 1.0]]), ('o3', [[0.0, 1.0], [0.0, 0.0]]), ('o4', [[1.9659258262890682, 0.7411809548974793], [1.0, 1.0]]), ('o5', [[1.0, 1.0], [1.7071067811865475, 1.7071067811865475]]), ('o6', [[1.7071067811865475, 1.7071067811865475], [1.9659258262890682, 0.7411809548974793]])]:
                c.line(points, id=object_id)
            c.point([[1.7071067811865475, 1.7071067811865475]], id='o7')
            for object_id, points in [('o8', [[1.5, 1.8660254037844388], [1.0, 1.0]]), ('o9', [[1.0, 1.0], [0.5, 1.8660254037844386]]), ('o10', [[0.5, 1.8660254037844386], [1.5, 1.8660254037844388]])]:
                c.line(points, id=object_id)
            c.point([[0.5, 1.8660254037844386]], id='o11')
            for object_id, points in [('o12', [[1.0, 0.0], [1.0, 1.0]]), ('o13', [[1.0, 1.0], [1.8660254037844386, 0.5]]), ('o14', [[1.8660254037844386, 0.5], [1.0, 0.0]])]:
                c.line(points, id=object_id)
            c.point([[1.8660254037844386, 0.5]], id='o15')
            c.path([[1.3570831958986451, 0.8700323455362459], [1.3818206497911942, 0.9379979415208239], [1.3866470138049805, 1.0116340267455473], [1.3709924827055746, 1.0822470532964792], [1.355337951606169, 1.1528600798474111], [1.3198438259783383, 1.2175573277234377], [1.268700576850888, 1.268700576850888], [1.2175573277234377, 1.3198438259783383], [1.1528600798474111, 1.355337951606169], [1.0822470532964792, 1.3709924827055746], [1.0116340267455473, 1.3866470138049805], [0.9379979415208239, 1.3818206497911942], [0.8700323455362459, 1.3570831958986451]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='o16', facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[0.8700323455362459, 1.3570831958986451], [0.9951081851902789, 1.3642966787494326], [0.9704827348708308, 1.431954547446018], [0.8700323455362459, 1.3570831958986451]], [1, 2, 2, 79], id='o17', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[0.8700323455362459, 1.3570831958986451], [0.9951081851902789, 1.3642966787494326], [0.9704827348708308, 1.431954547446018], [0.8700323455362459, 1.3570831958986451]], [1, 2, 2, 79], id='o17', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('o18', [[4.0, 0.0], [5.0, 0.0]]), ('o19', [[5.0, 0.0], [5.0, 1.0]]), ('o20', [[5.0, 1.0], [4.0, 1.0]]), ('o21', [[4.0, 1.0], [4.0, 0.0]]), ('o22', [[4.0, 1.0], [4.258819045102521, 1.9659258262890682]]), ('o23', [[4.258819045102521, 1.9659258262890682], [3.2928932188134525, 1.7071067811865475]]), ('o24', [[3.2928932188134525, 1.7071067811865475], [4.0, 1.0]]), ('o25', [[4.0, 1.0], [3.133974596215561, 1.5]]), ('o26', [[3.133974596215561, 1.5], [3.1339745962155616, 0.5]]), ('o27', [[3.1339745962155616, 0.5], [4.0, 1.0]]), ('o28', [[4.0, 1.0], [5.0, 1.0]]), ('o29', [[5.0, 1.0], [4.5, 1.8660254037844386]]), ('o30', [[4.5, 1.8660254037844386], [4.0, 1.0]])]:
                c.line(points, id=object_id)
            c.point([[4.0, 1.0]], id='o31')
            c.path([[4.19, 1.3290896534380867], [4.132237000915026, 1.3624391365089963], [4.06669896614182, 1.38], [4.0, 1.38], [3.9333010338581804, 1.38], [3.867762999084974, 1.3624391365089965], [3.81, 1.3290896534380867], [3.7522370009150263, 1.295740170367177], [3.704259829632823, 1.2477629990849737], [3.6709103465619135, 1.19], [3.6375608634910037, 1.1322370009150262], [3.62, 1.0666989661418196], [3.62, 1.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='o32', facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[3.62, 1.0], [3.656, 1.12], [3.584, 1.12], [3.62, 1.0]], [1, 2, 2, 79], id='o33', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[3.62, 1.0], [3.656, 1.12], [3.584, 1.12], [3.62, 1.0]], [1, 2, 2, 79], id='o33', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[2.25, 0.5], [2.75, 0.5]], id='o34')
            c.path([[2.75, 0.5], [2.63, 0.536], [2.63, 0.464], [2.75, 0.5]], [1, 2, 2, 79], id='o35', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[2.75, 0.5], [2.63, 0.536], [2.63, 0.464], [2.75, 0.5]], [1, 2, 2, 79], id='o35', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[5.3, 0.5], [5.8, 0.5]], id='o36')
            c.path([[5.8, 0.5], [5.68, 0.536], [5.68, 0.464], [5.8, 0.5]], [1, 2, 2, 79], id='o37', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.8, 0.5], [5.68, 0.536], [5.68, 0.464], [5.8, 0.5]], [1, 2, 2, 79], id='o37', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            for object_id, points in [('o38', [[6.0, 0.5]]), ('o39', [[6.3, 0.5]]), ('o40', [[6.6, 0.5]])]:
                c.point(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane182().draw(sys.argv[1] if len(sys.argv) > 1 else None))
