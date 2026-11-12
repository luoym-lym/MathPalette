"""Frozen question Plane27; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane27:

    def __init__(self):
        self.id = 'Plane27'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/160'
        self.question = 'Find x.\nChoices:\nA: 10\nB: 11\nC: 12\nD: 13'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '10', 'B': '11', 'C': '12', 'D': '13'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane27.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.439266104775542, 11.637396264275424], ylim=[-3.309714390988895, 11.76694797806207], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-3.0781812899310186, 8.457233587073176], [11.276311449430901, 4.104241719908025], [0.0, 0.0], [-3.0781812899310186, 8.457233587073176]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[-0.09325307842041967, 0.2562107272547342], [0.16295764883431452, 0.3494638056751539]], id='o2', zorder=3)
            c.line([[0.16295764883431452, 0.3494638056751539], [0.2562107272547342, 0.09325307842041967]], id='o2', zorder=3)
            c.text('9', [-1.5390906449655093, 4.228616793536588], id='l1', rotation_mode='default', offset_pt=[-20, 0], annotation_clip=None)
            c.text('15', [4.099065079749941, 6.2807376534906005], id='l2', rotation_mode='default', offset_pt=[0, 16], annotation_clip=None)
            c.text('x', [5.638155724715451, 2.0521208599540124], id='l3', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane27().draw(sys.argv[1] if len(sys.argv) > 1 else None))
