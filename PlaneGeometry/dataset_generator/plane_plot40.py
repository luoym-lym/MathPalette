"""Frozen question Plane40; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane40:

    def __init__(self):
        self.id = 'Plane40'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/386'
        self.question = 'Find x\nChoices:\nA: 5\nB: 10\nC: 10 \\sqrt { 3 }\nD: 20'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '5', 'B': '10', 'C': '10 \\sqrt { 3 }', 'D': '20'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane40.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.909113027293621, 14.098491726631732], ylim=[-1.2488589894492357, 17.758745764476117], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 17.32050807568877], [0.0, 0.0], [10.0, 0.0], [0.0, 17.32050807568877]], [1, 2, 2, 79], id='o1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.34374285217602274], [0.34374285217602274, 0.34374285217602274]], id='o2', zorder=3)
            c.line([[0.34374285217602274, 0.34374285217602274], [0.34374285217602274, 0.0]], id='o2', zorder=3)
            c.path([[-2.385460307333839e-16, 16.02192396746824], [0.11348440981064327, 16.02192396746824], [0.2264807765576725, 16.03680022136879], [0.3360982988749456, 16.066172147950002], [0.44571582119221864, 16.095544074531215], [0.5510116722807641, 16.13915904411371], [0.6492920541102654, 16.19590124901903]], [1, 4, 4, 4, 4, 4, 4], id='o10', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('x', [0.0, 8.660254037844386], id='t5', rotation_mode='default', offset_pt=[-17, 0], annotation_clip=None)
            c.text('10', [5.0, 0.0], id='t7', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('20', [5.0, 8.660254037844386], id='t9', rotation_mode='default', offset_pt=[22, 0], annotation_clip=None)
            c.text('y°', [0.0, 17.32050807568877], id='a11', rotation_mode='default', offset_pt=[16.823237931663847, -62.78517870878943], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane40().draw(sys.argv[1] if len(sys.argv) > 1 else None))
