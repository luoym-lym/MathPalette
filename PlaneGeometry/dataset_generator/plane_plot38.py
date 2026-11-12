"""Frozen question Plane38; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane38:

    def __init__(self):
        self.id = 'Plane38'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/333'
        self.question = 'Find tan X\nChoices:\nA: \\frac { 5 } { 12 }\nB: \\frac { 12 } { 13 }\nC: \\frac { 17 } { 12 }\nD: \\frac { 12 } { 5 }'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '\\frac { 5 } { 12 }', 'B': '\\frac { 12 } { 13 }', 'C': '\\frac { 17 } { 12 }', 'D': '\\frac { 12 } { 5 }'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane38.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.8587701720806296, 12.303482729614544], ylim=[-3.8883294824811467, 9.273923419214027], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 5.0], [0.0, 0.0], [12.0, 0.0], [0.0, 5.0]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.23803264072799435], [0.23803264072799435, 0.23803264072799435]], id='o2', zorder=3)
            c.line([[0.23803264072799435, 0.23803264072799435], [0.23803264072799435, 0.0]], id='o2', zorder=3)
            c.text('X', [0.0, 5.0], id='v4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-11, 8], annotation_clip=None)
            c.text('5', [0.0, 2.5], id='t6', rotation_mode='default', offset_pt=[-17, 0], annotation_clip=None)
            c.text('13', [6.0, 2.5], id='t8', rotation_mode='default', offset_pt=[5, 15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane38().draw(sys.argv[1] if len(sys.argv) > 1 else None))
