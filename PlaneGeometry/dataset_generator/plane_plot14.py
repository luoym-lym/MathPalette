"""Frozen question Plane14; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane14:

    def __init__(self):
        self.id = 'Plane14'
        self.source_dataset = 'MathVerse'
        self.source_key = 's3824'
        self.question = 'In the figure above, PQRS is a rectangle. The area of triangle RST is 7 and PT=2/5*PS. What is the area of PQRS?'
        self.answer = '70/3'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'P': [0, 0], 'S': [5, 0], 'R': [5, 4.666666666666667], 'Q': [0, 4.666666666666667], 'T': [2, 0]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane14.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.3435293515906661, 5.326576192945103], ylim=[-0.4999833278234398, 5.170122216712329]) as c:
            c.path([self.points['P'], self.points['S'], self.points['R'], self.points['Q'], self.points['P']], [1, 2, 2, 2, 79], id='rectangle')
            c.line([self.points['R'], self.points['T']], id='RT')
            c.line([self.points['P'], self.points['T']], id='PT')
            c.text('P', self.points['P'], offset_pt=[-12.0, -12.0], vertex=True, id='v_P')
            c.text('Q', self.points['Q'], offset_pt=[-12.0, 12.0], vertex=True, id='v_Q')
            c.text('R', self.points['R'], offset_pt=[12.0, 12.0], vertex=True, id='v_R')
            c.text('S', self.points['S'], offset_pt=[12.0, -12.0], vertex=True, id='v_S')
            c.text('T', self.points['T'], offset_pt=[0.0, -15.0], vertex=True, id='v_T')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane14().draw(sys.argv[1] if len(sys.argv) > 1 else None))
