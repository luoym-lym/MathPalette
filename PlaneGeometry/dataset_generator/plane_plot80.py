"""Frozen question Plane80; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane80:

    def __init__(self):
        self.id = 'Plane80'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:59'
        self.question = 'As shown in the figure, the straight line AB parallel CD, then the degree of angle 2 is ()\nChoices:\nA:20°\nB:25°\nC:30°\nD:40°'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '20°', 'B': '25°', 'C': '30°', 'D': '40°'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane80.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.4970033068099005, 6.184583069939099], ylim=[-1.31396991533407, 6.367616461414929], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment_0', [[0.0, 1.4558809370648094], [4.0, 0.0]]), ('segment_1', [[4.0, 0.0], [5.73505133713641, 4.767014370376838]]), ('segment_2', [[5.73505133713641, 4.767014370376838], [0.0, 1.4558809370648094]]), ('segment_3', [[-1.0, 3.4225924190929065], [5.245721764574973, 3.4225924190929065]]), ('segment_4', [[-1.0, 0.0], [4.0, 0.0]])]:
                c.line(points, id=object_id)
            c.line([[3.869460177333612, 0.0475126098369538], [3.9169727871705655, 0.17805243250334193]], id='right_angle_5', zorder=3)
            c.line([[3.9169727871705655, 0.17805243250334193], [4.047512609836954, 0.13053982266638814]], id='right_angle_5', zorder=3)
            for object_id, vertices, codes in [('angle_arc_6', [[3.6534087932875585, 3.422592419092907], [3.6534087932875585, 3.4441748716436993], [3.650579628960249, 3.4656645082184396], [3.6449936792000823, 3.4865115565319083], [3.639407729439916, 3.507358604845377], [3.6311130393314763, 3.527383758200853], [3.6203218130560804, 3.5460747103858115]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_7', [[5.481071684340642, 4.6203791494665145], [5.498176660767205, 4.590752461233438], [5.520334386564301, 4.564345911911033], [5.5465407308468, 4.542356178089083], [5.5727470751293, 4.5203664442671325], [5.602600098338213, 4.5031307932813425], [5.6347469385917295, 4.491430300303352]], [1, 4, 4, 4, 4, 4, 4]), ('angle_arc_8', [[3.6809026557043847, 0.11614193515699822], [3.6741415066406273, 0.09756583077475793], [3.6690153513244814, 0.0784347586874125], [3.6655826259813487, 0.05896680585716224], [3.662149900638216, 0.039498853026911994], [3.6604236989445127, 0.01976827738277255], [3.6604236989445127, 4.158610301539004e-17]], [1, 4, 4, 4, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('D', [4.0, 0.0], id='label_0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, -12], annotation_clip=None)
            c.text('E', [0.0, 1.4558809370648094], id='label_1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, 0], annotation_clip=None)
            c.text('F', [5.73505133713641, 4.767014370376838], id='label_2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12, 10], annotation_clip=None)
            c.text('B', [5.245721764574973, 3.4225924190929065], id='label_3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13, 0], annotation_clip=None)
            c.text('A', [-1.0, 3.4225924190929065], id='label_4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 0], annotation_clip=None)
            c.text('C', [-1.0, 0.0], id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 0], annotation_clip=None)
            c.text('1', [3.40644421070175, 3.422592419092907], id='label_6', rotation_mode='default', offset_pt=[42.63703305156273, 10.352761804100822], annotation_clip=None)
            c.text('70° − ∠1', [5.73505133713641, 4.767014370376838], id='label_7', rotation_mode='default', offset_pt=[-45, 28], annotation_clip=None)
            c.text('2', [4.0, 0.0], id='label_8', rotation_mode='default', offset_pt=[-64.13404192169585, 9.897946127015032], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane80().draw(sys.argv[1] if len(sys.argv) > 1 else None))
