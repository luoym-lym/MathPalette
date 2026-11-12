"""Frozen question Plane52; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane52:

    def __init__(self):
        self.id = 'Plane52'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/678'
        self.question = 'Find x\nChoices:\nA: 21\nB: 34\nC: 58\nD: 67'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '21', 'B': '34', 'C': '58', 'D': '67'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane52.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.47443426817329737, 19.342396532286504], ylim=[-5.671821672379161, 14.145009128080641], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [13.567972864081408, 8.47998304005088], [18.867962264113206, 0.0], [0.0, 0.0]], [1, 2, 2, 79], id='polygon_1', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[13.264069527320238, 8.290043454575148], [13.45400911279597, 7.986140117813977]], id='right_angle_2', zorder=3)
            c.line([[13.45400911279597, 7.986140117813977], [13.75791244955714, 8.17607970328971]], id='right_angle_2', zorder=3)
            c.path([[18.44587429638936, 0.6753407483581574], [18.33134021967819, 0.6037569504136777], [18.236877049641365, 0.5041994901043351], [18.171402253272056, 0.3860667431768509], [18.105927456902744, 0.26793399624936676], [18.071568279398225, 0.13506403983383472], [18.071568279398225, 9.753013442414068e-17]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_3', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('x°', [18.867962264113206, 0.0], id='angle_label_4', rotation_mode='default', offset_pt=[-34.98569924987271, 19.390741295717813], annotation_clip=None)
            c.text('16', [6.783986432040704, 4.23999152002544], id='label_5', rotation_mode='default', offset_pt=[-6, 16], annotation_clip=None)
            c.text('10', [16.217967564097307, 4.23999152002544], id='label_6', rotation_mode='default', offset_pt=[15, 7], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane52().draw(sys.argv[1] if len(sys.argv) > 1 else None))
