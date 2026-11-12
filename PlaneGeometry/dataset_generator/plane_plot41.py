"""Frozen question Plane41; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane41:

    def __init__(self):
        self.id = 'Plane41'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/375'
        self.question = 'Find the length of $AC$ in the isosceles triangle ABC. \nChoices:\nA: 1.5\nB: 7\nC: 11\nD: 12.5'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '1.5', 'B': '7', 'C': '11', 'D': '12.5'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane41.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-7.136510716315021, 7.108888237438094], ylim=[-5.472469693831432, 8.772929259921684], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-6.25, 3.152380053229623], [6.25, 3.152380053229623], [0.0, 0.0], [-6.25, 3.152380053229623]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[-3.1636723154969526, 1.4995171737941846], [-3.0863276845030474, 1.6528628794354383]], id='o2', zorder=3)
            c.line([[3.0863276845030474, 1.6528628794354383], [3.1636723154969526, 1.4995171737941846]], id='o3', zorder=3)
            c.text('A', [-6.25, 3.152380053229623], id='v4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13, 0], annotation_clip=None)
            c.text('B', [6.25, 3.152380053229623], id='v5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[13, 0], annotation_clip=None)
            c.text('C', [0.0, 0.0], id='v6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('9x − 1', [0.0, 3.152380053229623], id='t8', rotation_mode='default', offset_pt=[0, 17], annotation_clip=None)
            c.text('4x + 1', [-3.125, 1.5761900266148114], id='t10', rotation_mode='default', offset_pt=[-18, -16], annotation_clip=None)
            c.text('5x − 0.5', [3.125, 1.5761900266148114], id='t12', rotation_mode='default', offset_pt=[25, -16], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane41().draw(sys.argv[1] if len(sys.argv) > 1 else None))
