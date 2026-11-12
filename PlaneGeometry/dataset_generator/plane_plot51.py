"""Frozen question Plane51; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane51:

    def __init__(self):
        self.id = 'Plane51'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/665'
        self.question = 'Find $h$ in the triangle.\nChoices:\nA: 4.62\nB: 5.66\nC: 6.93\nD: 8'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '4.62', 'B': '5.66', 'C': '6.93', 'D': '8'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane51.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.1787583482784414, 7.4274645414726255], ylim=[-1.8096266822882634, 5.7965962074628035], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [6.928203230275509, 0.0], [6.928203230275509, 4.0], [0.0, 0.0]], [1, 2, 2, 79], id='polygon_1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[6.790648562853796, 0.0], [6.790648562853796, 0.13755466742171343]], id='right_angle_2', zorder=3)
            c.line([[6.790648562853796, 0.13755466742171343], [6.928203230275509, 0.13755466742171343]], id='right_angle_2', zorder=3)
            c.path([[6.6767153534388255, 3.8548034066104138], [6.7022007815082985, 3.8106613503414453], [6.738864580616954, 3.7739975512327892], [6.783006636885922, 3.7485121231633167], [6.827148693154891, 3.7230266950938447], [6.877232374136564, 3.709606813220827], [6.928203230275509, 3.709606813220827]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_3', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('60°', [6.928203230275509, 4.0], id='angle_label_4', rotation_mode='default', offset_pt=[-20.000000000000004, -34.64101615137755], annotation_clip=None)
            c.text('4', [6.928203230275509, 2.0], id='label_5', rotation_mode='default', offset_pt=[17, 0], annotation_clip=None)
            c.text('h', [3.4641016151377544, 2.0], id='label_6', rotation_mode='default', offset_pt=[-10, 15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane51().draw(sys.argv[1] if len(sys.argv) > 1 else None))
