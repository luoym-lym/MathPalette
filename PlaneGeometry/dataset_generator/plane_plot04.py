"""Frozen question Plane04; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane04:

    def __init__(self):
        self.id = 'Plane04'
        self.source_dataset = 'MathVerse'
        self.source_key = 's274'
        self.question = 'As shown in the figure, and the radial OM bisects angle AOC, then the degree of angle CON is ()\nChoices:\nA:65°\nB:55°\nC:45°\nD:35°'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '65°', 'B': '55°', 'C': '45°', 'D': '35°'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane04.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.774754567346212, 5.735402715494361], ylim=[-5.705888826605471, 5.804268456235103], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('AB', [[-5.0, 0.0], [5.0, 0.0]]), ('CD', [[-1.7101007166283435, 4.698463103929543], [1.7101007166283448, -4.698463103929542]]), ('OM', [[0.0, 0.0], [-4.0957602214449595, 2.86788218175523]]), ('ON', [[0.0, 0.0], [2.8678821817552302, 4.095760221444959]])]:
                c.line(points, id=object_id)
            c.line([[-0.17051086639769034, 0.11939299399833142], [-0.051117872399358874, 0.2899038603960218]], id='right_MON', zorder=3)
            c.line([[-0.051117872399358874, 0.2899038603960218], [0.11939299399833146, 0.17051086639769034]], id='right_MON', zorder=3)
            c.path([[-0.30059400409908826, 0.8258752386856952], [-0.47005631843500784, 0.7641960004375578], [-0.6164971256876939, 0.6518280168911469], [-0.7199347692346924, 0.5041037524373997], [-0.8233724127816907, 0.3563794879836526], [-0.8788780718475554, 0.18033802818861183], [-0.8788780718475554, 1.0763152175289063e-16]], [1, 4, 4, 4, 4, 4, 4], id='arc_AOC70', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('A', [-5.0, 0.0], id='v_A', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15.0, -3.0], annotation_clip=None)
            c.text('B', [5.0, 0.0], id='v_B', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15.0, -3.0], annotation_clip=None)
            c.text('C', [-1.7101007166283435, 4.698463103929543], id='v_C', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12.0, 15.0], annotation_clip=None)
            c.text('D', [1.7101007166283448, -4.698463103929542], id='v_D', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0.0, -15.0], annotation_clip=None)
            c.text('M', [-4.0957602214449595, 2.86788218175523], id='v_M', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-18.0, 12.0], annotation_clip=None)
            c.text('N', [2.8678821817552302, 4.095760221444959], id='v_N', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[15.0, 12.0], annotation_clip=None)
            c.text('O', [0.0, 0.0], id='v_O', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-15, -40], annotation_clip=None)
            c.text('70°', [0.0, 0.0], id='given_AOC', rotation_mode='default', offset_pt=[-67.46120840403677, 23.767966253672533], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane04().draw(sys.argv[1] if len(sys.argv) > 1 else None))
