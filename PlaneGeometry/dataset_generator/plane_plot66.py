"""Frozen question Plane66; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane66:

    def __init__(self):
        self.id = 'Plane66'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/855'
        self.question = 'Find $x$ so that $a ∥ b$.\nChoices:\nA: 2.5\nB: 14\nC: 15\nD: 16'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '2.5', 'B': '14', 'C': '15', 'D': '16'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane66.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.249627022049503, 8.269158272049502], ylim=[-5.056637643112972, 5.462147650986034], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.line([[-2.0, 0.0], [8.0, 0.0]], id='segment1')
            c.line([[-1.1721933854678213, 2.7615145603573206], [1.1721933854678213, -2.761514560357321]], id='segment2')
            for object_id, points in [('parallel_mark4', [[1.179540507316312, -2.643587592164], [1.1721933854678213, -2.7615145603573206]]), ('parallel_mark4', [[1.0822600840222594, -2.6848806819625355], [1.1721933854678213, -2.7615145603573206]]), ('parallel_mark5', [[-1.179540507316312, 2.6435875921639997], [-1.1721933854678213, 2.76151456035732]]), ('parallel_mark5', [[-1.0822600840222594, 2.684880681962535], [-1.1721933854678213, 2.76151456035732]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[3.8278066145321787, 2.7615145603573206], [6.172193385467821, -2.761514560357321]], id='segment6')
            for object_id, points in [('parallel_mark8', [[6.179540507316313, -2.643587592164], [6.172193385467821, -2.7615145603573206]]), ('parallel_mark8', [[6.082260084022259, -2.6848806819625355], [6.172193385467821, -2.7615145603573206]]), ('parallel_mark9', [[3.820459492683688, 2.6435875921639997], [3.8278066145321787, 2.76151456035732]]), ('parallel_mark9', [[3.917739915977741, 2.684880681962535], [3.8278066145321787, 2.76151456035732]]), ('parallel_mark10', [[7.8943184026361255, 0.05284079868193705], [8.0, 0.0]]), ('parallel_mark10', [[7.8943184026361255, -0.05284079868193705], [8.0, 0.0]]), ('parallel_mark11', [[-1.894318402636126, -0.05284079868193705], [-2.0, 0.0]]), ('parallel_mark11', [[-1.894318402636126, 0.05284079868193705], [-2.0, 0.0]])]:
                c.line(points, id=object_id, zorder=3)
            c.path([[0.16517235919414222, -0.389121693176211], [0.24154617324274905, -0.3567029324947021], [0.30671161510636, -0.3025054065919883], [0.35250554278058244, -0.23331832900791777], [0.39829947045480485, -0.1641312514238472], [0.4227263894554964, -0.0829694854537265], [0.4227263894554964, -1.0353810395235822e-16]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc12', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[4.471592013180629, 6.47113149702239e-17], [4.471592013180629, -0.08728225159381946], [4.493217892141533, -0.17321976542044962], [4.534530298417063, -0.2501058924591575], [4.575842704692594, -0.3269920194978654], [4.6355686566179175, -0.39245762565978676], [4.708352088740103, -0.44063192847572813], [4.781135520862288, -0.48880623129166945], [4.8647337176644205, -0.5182048097431151], [4.951649813891358, -0.526191277044536], [5.038565910118295, -0.534177744345957], [5.12612171278031, -0.5205060091326016], [5.206465448992677, -0.48640211647026377]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='angle_arc14', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('a', [-1.1721933854678213, 2.7615145603573206], id='text3', rotation_mode='default', offset_pt=[-10, 13], annotation_clip=None)
            c.text('b', [3.8278066145321787, 2.7615145603573206], id='text7', rotation_mode='default', offset_pt=[-10, 13], annotation_clip=None)
            c.text('(4x + 11)°', [0.0, 0.0], id='anglelabel13', rotation_mode='default', offset_pt=[79.21915309638098, -52.43401360464552], annotation_clip=None)
            c.text('(8x + 1)°', [5.0, 0.0], id='anglelabel15', rotation_mode='default', offset_pt=[-37.53171500121995, -56.70423590056744], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane66().draw(sys.argv[1] if len(sys.argv) > 1 else None))
