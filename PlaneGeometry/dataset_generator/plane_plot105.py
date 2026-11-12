"""Frozen question Plane105; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane105:

    def __init__(self):
        self.id = 'Plane105'
        self.source_dataset = 'Author Designed'
        self.source_key = 'visual-matching:triangle_similarity'
        self.question = 'Which triangle, A, B, or C, is similar to R? All diagrams are drawn to scale. Rotations and reflections are allowed.\nChoices:\nA: Triangle A\nB: Triangle B\nC: Triangle C'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Triangle A', 'B': 'Triangle B', 'C': 'Triangle C'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane105.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-6.451859473037789, 6.951859473037789], ylim=[-7.605858525051677, 5.797860421023901], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-6.0, 2.5], [-2.0, 2.5], [-6.0, 5.5], [-6.0, 2.5]], [1, 2, 2, 79], id='outline_R', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[-5.757600568828205, 2.5], [-5.757600568828205, 2.742399431171795]], id='right_R', zorder=3)
            c.line([[-5.757600568828205, 2.742399431171795], [-6.0, 2.742399431171795]], id='right_R', zorder=3)
            c.path([[1.5, 2.5], [6.5, 2.5], [1.5, 5.5], [1.5, 2.5]], [1, 2, 2, 79], id='outline_A', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[1.742399431171795, 2.5], [1.742399431171795, 2.742399431171795]], id='right_A', zorder=3)
            c.line([[1.742399431171795, 2.742399431171795], [1.5, 2.742399431171795]], id='right_A', zorder=3)
            c.path([[-6.0, -6.0], [-2.0, -6.0], [-6.0, -2.0], [-6.0, -6.0]], [1, 2, 2, 79], id='outline_B', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[-5.757600568828205, -6.0], [-5.757600568828205, -5.757600568828205]], id='right_B', zorder=3)
            c.line([[-5.757600568828205, -5.757600568828205], [-6.0, -5.757600568828205]], id='right_B', zorder=3)
            c.path([[5.875, -1.5], [5.875, -6.5], [2.125, -1.4999999999999998], [5.875, -1.5]], [1, 2, 2, 79], id='outline_C', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[5.875, -1.742399431171795], [5.632600568828205, -1.742399431171795]], id='right_C', zorder=3)
            c.line([[5.632600568828205, -1.742399431171795], [5.632600568828205, -1.5]], id='right_C', zorder=3)
            for object_id, text, anchor in [('name_R', 'R', [-4.0, 2.5]), ('name_A', 'A', [4.0, 2.5]), ('name_B', 'B', [-4.0, -6.0]), ('name_C', 'C', [4.0, -6.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, -22], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane105().draw(sys.argv[1] if len(sys.argv) > 1 else None))
