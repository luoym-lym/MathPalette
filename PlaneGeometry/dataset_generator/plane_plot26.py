"""Frozen question Plane26; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane26:

    def __init__(self):
        self.id = 'Plane26'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/114'
        self.question = 'In the figure, KL is tangent to $\\odot M$ at K. Find the value of x.\nChoices:\nA: 6.00\nB: 9.45\nC: 18.9\nD: 37.8'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '6.00', 'B': '9.45', 'C': '18.9', 'D': '37.8'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane26.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-10.143941358383497, 18.03872895816873], ylim=[-14.955196342938567, 13.227473973613659], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.point([[0.0, 0.0]], id='o1')
            c.circle([0.0, 0.0], 9.45, id='o2', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('o3', [[0.0, 0.0], [8.183940065762945, 4.724999999999999]]), ('o4', [[0.0, 0.0], [16.683940065762947, -9.997431864335457]]), ('o5', [[8.183940065762945, 4.724999999999999], [16.683940065762947, -9.997431864335457]])]:
                c.line(points, id=object_id)
            c.line([[7.742553556058521, 4.47016537980548], [7.99738817625304, 4.028778870101056]], id='o6', zorder=3)
            c.line([[7.99738817625304, 4.028778870101056], [8.438774685957464, 4.283613490295575]], id='o6', zorder=3)
            c.line([[-0.71960949152029, -1.2009005702862787], [7.386469357912091, -6.058264638048234]], id='o7', linestyle=(0, [4, 3]))
            c.line([[0.0, 0.0], [-0.71960949152029, -1.2009005702862787]], id='o8')
            c.line([[8.10607884943238, -4.857364067761956], [7.386469357912091, -6.058264638048234]], id='o9')
            c.line([[7.386469357912091, -6.058264638048234], [15.964330574242657, -11.198332434621737]], id='o10', linestyle=(0, [4, 3]))
            c.line([[8.10607884943238, -4.857364067761956], [7.386469357912091, -6.058264638048234]], id='o11')
            c.line([[16.683940065762947, -9.997431864335457], [15.964330574242657, -11.198332434621737]], id='o12')
            c.text('M', [0.0, 0.0], id='l1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, 7], annotation_clip=None)
            c.text('K', [8.183940065762945, 4.724999999999999], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[6, 15], annotation_clip=None)
            c.text('L', [16.683940065762947, -9.997431864335457], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8, -13], annotation_clip=None)
            c.text('x', [4.0919700328814725, 2.3624999999999994], id='l4', rotation_mode='default', offset_pt=[0, 14], annotation_clip=None)
            c.text('17', [12.433940065762947, -2.636215932167729], id='l5', rotation_mode='default', offset_pt=[18, 2], annotation_clip=None)
            c.text('x', [3.3334299331959003, -3.6295826041672568], id='l6', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('10', [11.675399966077373, -8.628298536334986], id='l7', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane26().draw(sys.argv[1] if len(sys.argv) > 1 else None))
