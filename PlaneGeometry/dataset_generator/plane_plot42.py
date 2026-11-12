"""Frozen question Plane42; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane42:

    def __init__(self):
        self.id = 'Plane42'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/388'
        self.question = 'Express the ratio of $\\tan M$ as a decimal to the nearest hundredth.\nChoices:\nA: 0.38\nB: 0.42\nC: 0.92\nD: 2.40'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '0.38', 'B': '0.42', 'C': '0.92', 'D': '2.40'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane42.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.1387217150934745, 38.79322797412936], ylim=[-28.247156712343973, 13.684792976878859], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [36.0, 0.0], [0.0, -15.0], [0.0, 0.0]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.7583179558959569, 0.0], [0.7583179558959569, -0.7583179558959569]], id='o2', zorder=3)
            c.line([[0.7583179558959569, -0.7583179558959569], [0.0, -0.7583179558959569]], id='o2', zorder=3)
            c.text('P', [0.0, 0.0], id='v4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-7, 14], annotation_clip=None)
            c.text('M', [36.0, 0.0], id='v5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            c.text('N', [0.0, -15.0], id='v6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-5, -14], annotation_clip=None)
            c.text('36', [18.0, 0.0], id='t8', rotation_mode='default', offset_pt=[0, 17], annotation_clip=None)
            c.text('15', [0.0, -7.5], id='t10', rotation_mode='default', offset_pt=[-18, 0], annotation_clip=None)
            c.text('39', [18.0, -7.5], id='t12', rotation_mode='default', offset_pt=[0, -18], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane42().draw(sys.argv[1] if len(sys.argv) > 1 else None))
