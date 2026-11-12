"""Frozen question Plane89; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane89:

    def __init__(self):
        self.id = 'Plane89'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:349'
        self.question = 'As shown in the figure, BD is the angular bisector of triangle ABC, then the degree of angle CDE is ()\nChoices:\nA:35°\nB:40°\nC:45°\nD:50°'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '35°', 'B': '40°', 'C': '45°', 'D': '50°'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane89.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5461426101712581, 8.559345644902944], ylim=[-2.865604193804801, 6.239884061269402], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment_0', [[5.039230767231746, 3.5285073699939673], [0.0, 0.0]]), ('segment_1', [[0.0, 0.0], [8.0, 0.0]]), ('segment_2', [[8.0, 0.0], [5.039230767231746, 3.5285073699939673]]), ('segment_3', [[0.0, 0.0], [6.32627562117904, 1.9946670414723904]]), ('segment_4', [[5.039230767231746, 3.5285073699939673], [6.151764867541411, 0.0]]), ('segment_5', [[6.32627562117904, 1.9946670414723904], [6.151764867541411, 0.0]])]:
                c.line(points, id=object_id)
            c.path([[0.49400435411643884, 0.0], [0.49400435411643884, 0.05039256222042025], [0.4862936619758377, 0.1004897334819263], [0.4711403262642774, 0.1485499742631758], [0.455986990552717, 0.1966102150444253], [0.4335686628191309, 0.24207008661618973], [0.4046646765621439, 0.2833492569760072]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_6', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[7.788306748028501, 0.25228619356498516], [7.751468289204487, 0.22137505635261562], [7.72184337570702, 0.18276711741449075], [7.701520004689507, 0.13918350761935078], [7.681196633671994, 0.09559989782421081], [7.6706637639223745, 0.04808919267663482], [7.6706637639223745, 4.0332056735570166e-17]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_7', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.line([[5.545981159298853, 1.9213004604184096], [5.388934383877427, 1.8717838023306843]], id='right_angle_8', zorder=3)
            c.line([[5.388934383877427, 1.8717838023306843], [5.438451041965152, 1.7147370269092586]], id='right_angle_8', zorder=3)
            c.text('B', [0.0, 0.0], id='label_0', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13, -10], annotation_clip=None)
            c.text('C', [8.0, 0.0], id='label_1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13, -10], annotation_clip=None)
            c.text('A', [5.039230767231746, 3.5285073699939673], id='label_2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 17], annotation_clip=None)
            c.text('D', [6.32627562117904, 1.9946670414723904], id='label_3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15, 5], annotation_clip=None)
            c.text('E', [6.151764867541411, 0.0], id='label_4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('F', [5.595497817386578, 1.7642536849969839], id='label_5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-10.500000000000009, -18.186533479473205], annotation_clip=None)
            c.text('35°', [0.0, 0.0], id='label_6', rotation_mode='default', offset_pt=[35, -30], annotation_clip=None)
            c.text('50°', [8.0, 0.0], id='label_7', rotation_mode='default', offset_pt=[-45.3153893518325, 21.130913087034962], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane89().draw(sys.argv[1] if len(sys.argv) > 1 else None))
