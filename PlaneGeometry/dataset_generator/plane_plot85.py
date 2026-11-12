"""Frozen question Plane85; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane85:

    def __init__(self):
        self.id = 'Plane85'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:164'
        self.question = 'As shown in the figure, the straight line AB parallel CD, then angle C is equal to ()\nChoices:\nA:42°\nB:44°\nC:46°\nD:48°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '42°', 'B': '44°', 'C': '46°', 'D': '48°'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane85.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.2416501933243658, 5.439144041993982], ylim=[-0.9345574830096588, 5.746236752308689], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            for object_id, points in [('segment_0', [[-1.0790097005079768, 5.041987555688496], [2.1580194010159537, 1.9160248886230082]]), ('segment_1', [[2.1580194010159537, 1.9160248886230082], [0.3077356738217405, 0.0]]), ('segment_2', [[0.3077356738217405, 0.0], [5.0, 0.0]]), ('segment_3', [[0.0, 4.0], [5.0, 4.0]])]:
                c.line(points, id=object_id)
            c.line([[2.071109657248999, 1.9999526526001152], [1.987181893271892, 1.9130429088331609]], id='right_angle_4', zorder=3)
            c.line([[1.987181893271892, 1.9130429088331609], [2.0740916370388467, 1.8291151448560539]], id='right_angle_4', zorder=3)
            c.path([[0.32218336397175673, 4.0], [0.32218336397175673, 4.0641929181725915], [0.30299833827995415, 4.126944309692309], [0.2671021139847627, 4.180162650749339], [0.2312058896895712, 4.233380991806369], [0.18021064973989237, 4.274676122886567], [0.12069201243273865, 4.298723213284628], [0.06117337512558493, 4.322770303682688], [-0.004195539062099738, 4.3284893426211095], [-0.06698568795672158, 4.31514288446532], [-0.12977583685134345, 4.30179642630953], [-0.1871671687790984, 4.269983891547046], [-0.23175931671187852, 4.223807370605618]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='angle_arc_5', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('A', [0.0, 4.0], id='label_0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-17.38666487320323, -4.658742811845374], annotation_clip=None)
            c.text('E', [2.1580194010159537, 1.9160248886230082], id='label_1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[16, 0], annotation_clip=None)
            c.text('C', [0.3077356738217405, 0.0], id='label_2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -13], annotation_clip=None)
            c.text('B', [5.0, 4.0], id='label_3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 0], annotation_clip=None)
            c.text('D', [5.0, 0.0], id='label_4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 0], annotation_clip=None)
            c.text('1: 136°', [0.0, 4.0], id='label_5', rotation_mode='default', offset_pt=[20.97796923129107, 51.922295855740096], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane85().draw(sys.argv[1] if len(sys.argv) > 1 else None))
