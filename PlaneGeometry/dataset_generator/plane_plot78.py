"""Frozen question Plane78; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane78:

    def __init__(self):
        self.id = 'Plane78'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:49'
        self.question = 'As shown in the figure, AB = AC, the perpendicular bisector of AB intersects AC at D, then the degree of angle BDC is ()\nChoices:\nA:72°\nB:36°\nC:60°\nD:82°'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '72°', 'B': '36°', 'C': '60°', 'D': '82°'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane78.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.744957497383824, 4.462879068889988], ylim=[-0.5233977827355298, 8.684438783538283], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment_0', [[0.0, 8.0], [-2.5993575698632503, 0.0]]), ('segment_1', [[-2.5993575698632503, 0.0], [2.5993575698632503, 0.0]]), ('segment_2', [[2.5993575698632503, 0.0], [0.0, 8.0]]), ('segment_3', [[-2.5993575698632503, 0.0], [1.6064913270898178, 3.0557280900008417]]), ('segment_4', [[-3.188689357745563, 4.613776741499453], [2.4783423606962507, 2.7724465170010943]])]:
                c.line(points, id=object_id)
            c.line([[-1.351135996672179, 3.841630986557156], [-1.192766983229335, 3.790173774816602]], id='right_angle_5', zorder=3)
            c.line([[-1.192766983229335, 3.790173774816602], [-1.1413097714887812, 3.948542788259446]], id='right_angle_5', zorder=3)
            c.path([[-0.1029144234811079, 7.683261973114312], [-0.0696776435016931, 7.672462688659641], [-0.034947218603673454, 7.6669619297499345], [-6.117810100889312e-17, 7.6669619297499345], [0.03494721860367333, 7.6669619297499345], [0.06967764350169299, 7.672462688659641], [0.10291442348110778, 7.683261973114312]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_6', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('A', [0.0, 8.0], id='label_0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 17], annotation_clip=None)
            c.text('B', [-2.5993575698632503, 0.0], id='label_1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-11, -12], annotation_clip=None)
            c.text('C', [2.5993575698632503, 0.0], id='label_2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[11, -12], annotation_clip=None)
            c.text('E', [-1.2996787849316251, 4.0], id='label_3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 18], annotation_clip=None)
            c.text('D', [1.6064913270898178, 3.0557280900008417], id='label_4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13, 10], annotation_clip=None)
            c.text('36°', [0.0, 8.0], id='label_5', rotation_mode='default', offset_pt=[0.0, -59.0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane78().draw(sys.argv[1] if len(sys.argv) > 1 else None))
