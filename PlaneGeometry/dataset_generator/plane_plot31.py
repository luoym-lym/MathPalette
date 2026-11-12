"""Frozen question Plane31; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane31:

    def __init__(self):
        self.id = 'Plane31'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/242'
        self.question = 'Find $m \\angle A$ of quadrilateral ABCD\nChoices:\nA: 45\nB: 90\nC: 135\nD: 180'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '45', 'B': '90', 'C': '135', 'D': '180'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane31.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.5309369144471829, 8.502379330624867], ylim=[-2.466102100425641, 6.56721414464641], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[4.0, 4.0], [8.0, 4.0], [8.0, 0.0], [0.0, 0.0], [4.0, 4.0]], [1, 2, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('o2', [[7.836637076007811, 4.0], [7.836637076007811, 3.8366370760078117]]), ('o2', [[7.836637076007811, 3.8366370760078117], [8.0, 3.8366370760078117]]), ('o3', [[8.0, 0.1633629239921884], [7.836637076007811, 0.1633629239921884]]), ('o3', [[7.836637076007811, 0.1633629239921884], [7.836637076007811, 0.0]])]:
                c.line(points, id=object_id, zorder=3)
            c.path([[3.794639944267842, 3.794639944267842], [3.835251464828462, 3.7540284237072217], [3.887011490897287, 3.7263621133763314], [3.9433412880939867, 3.71515742006192], [3.9996710852906867, 3.703952726747508], [4.0580785525762275, 3.709705360166999], [4.11114006128805, 3.7316841567154135], [4.164201569999872, 3.753662953263828], [4.209569612290011, 3.7908955433527636], [4.241477879246925, 3.838649639557149], [4.273386146203838, 3.8864037357615344], [4.290422975986113, 3.942566636834577], [4.290422975986113, 4.0]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='o4', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[0.2904229759861127, 0.0], [0.2904229759861127, 0.03813799577171656], [0.28291062241003223, 0.07590514758355874], [0.26831584328458646, 0.11114006128804967], [0.2537210641591407, 0.1463749749925406], [0.23232769116320282, 0.1783924203011135], [0.20536005573215815, 0.20536005573215813]], [1, 4, 4, 4, 4, 4, 4], id='o5', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('D', [0.0, 0.0], id='l1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -7], annotation_clip=None)
            c.text('C', [8.0, 0.0], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, -10], annotation_clip=None)
            c.text('B', [8.0, 4.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, 10], annotation_clip=None)
            c.text('A', [4.0, 4.0], id='l4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-8, 13], annotation_clip=None)
            c.text('3x°', [4.0, 4.0], id='l5', rotation_mode='default', offset_pt=[14.924653862238506, -36.031301767940185], annotation_clip=None)
            c.text('x°', [0.0, 0.0], id='l6', rotation_mode='default', offset_pt=[34.183542702917606, 14.15928699750832], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane31().draw(sys.argv[1] if len(sys.argv) > 1 else None))
