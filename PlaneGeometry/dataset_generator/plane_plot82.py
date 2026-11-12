"""Frozen question Plane82; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane82:

    def __init__(self):
        self.id = 'Plane82'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:74'
        self.question = 'In the figure, line b is perpendicular to line c. What is the smallest clockwise rotation about A that makes line b parallel to line a?\nChoices:\nA:70°\nB:50°\nC:30°\nD:20°'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '70°', 'B': '50°', 'C': '30°', 'D': '20°'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane82.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.1865353356700465, 3.474862092697566], ylim=[-2.1424405935253006, 5.518956834842312], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment_0', [[-4.0, 0.0], [3.0, 0.0]]), ('segment_1', [[0.44462618632336937, -1.221600407021681], [-1.573292659298076, 4.322586055615179]]), ('segment_2', [[-3.093384195706005, 2.066633547041254], [2.7327100531666275, 4.1871584356604]])]:
                c.line(points, id=object_id)
            c.line([[-1.1562571644305866, 2.771690126417961], [-1.1088694284908225, 2.6414933919643806]], id='right_angle_3', zorder=3)
            c.line([[-1.1088694284908225, 2.6414933919643806], [-0.978672694037242, 2.688881127904145]], id='right_angle_3', zorder=3)
            c.path([[-0.1000407758728355, 0.27485977273533635], [-0.1564395768342255, 0.2543322879370863], [-0.2051765834851426, 0.21693506742052757], [-0.23960169501028264, 0.1677709130140238], [-0.2740268065354227, 0.11860675860752007], [-0.29249966069272565, 0.06001835037740438], [-0.29249966069272565, 3.5820877321903334e-17]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_4', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('A', [-1.0260604299770062, 2.8190778623577253], id='label_0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[18.186533479473205, -10.500000000000009], annotation_clip=None)
            c.text('a', [3.0, 0.0], id='label_1', rotation_mode='default', offset_pt=[16, 0], annotation_clip=None)
            c.text('b', [2.7327100531666275, 4.1871584356604], id='label_2', rotation_mode='default', offset_pt=[12, 8], annotation_clip=None)
            c.text('c', [-1.573292659298076, 4.322586055615179], id='label_3', rotation_mode='default', offset_pt=[10, 14], annotation_clip=None)
            c.text('1: 70°', [0.0, 0.0], id='label_4', rotation_mode='default', offset_pt=[-47.510818568761515, 33.26743330836068], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane82().draw(sys.argv[1] if len(sys.argv) > 1 else None))
