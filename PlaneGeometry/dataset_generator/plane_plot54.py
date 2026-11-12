"""Frozen question Plane54; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane54:

    def __init__(self):
        self.id = 'Plane54'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/698'
        self.question = 'In the triangle in the figure above, what is the value of x?\nChoices:\nA: 2*\\sqrt{3}\nB: 6*\\sqrt{2}\nC: 6*\\sqrt{3}\nD: 6\nE: 12'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '2*\\sqrt{3}', 'B': '6*\\sqrt{2}', 'C': '6*\\sqrt{3}', 'D': '6', 'E': '12'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane54.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.15458961686311135, 6.422551196152248], ylim=[-1.6904605541715378, 4.886680258843821], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [6.0, 0.0], [6.0, 3.4641016151377544], [0.0, 0.0]], [1, 2, 2, 79], id='polygon_1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[5.881055757866476, 0.0], [5.881055757866476, 0.11894424213352427]], id='right_angle_2', zorder=3)
            c.line([[5.881055757866476, 0.11894424213352427], [6.0, 0.11894424213352427]], id='right_angle_2', zorder=3)
            c.path([[5.793982529356962, 3.34515737300423], [5.814860050353878, 3.3089964459014847], [5.84489483076373, 3.2789616654916323], [5.881055757866476, 3.2580841444947155], [5.917216684969222, 3.237206623497799], [5.9582449580061665, 3.226213130870706], [6.0, 3.226213130870706]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_3', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('60°', [6.0, 3.4641016151377544], id='angle_label_4', rotation_mode='default', offset_pt=[-19.500000000000004, -33.77499074759311], annotation_clip=None)
            c.text('6', [3.0, 0.0], id='label_5', rotation_mode='default', offset_pt=[0, -16], annotation_clip=None)
            c.text('x', [6.0, 1.7320508075688772], id='label_6', rotation_mode='default', offset_pt=[16, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane54().draw(sys.argv[1] if len(sys.argv) > 1 else None))
