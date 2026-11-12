"""Frozen question Plane09; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane09:

    def __init__(self):
        self.id = 'Plane09'
        self.source_dataset = 'MathVerse'
        self.source_key = 's1649'
        self.question = 'A rally car starts at point P and races to point Q. Here the car turns west and races to point R. At point R the car must turn to head directly back to point P.\n\nWhat is the compass bearing of R from P? Give your answer to one decimal place.'
        self.answer = '\\[S 23.5 ^\\circ W\\]'
        self.answer_type = 'text'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane09.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-14.196813092161928, 14.243109388458226], ylim=[-11.960701981050818, 16.479220499569337], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('horizontal_through_P', [[-13.5, 9.55], [13.5, 9.55]]), ('PQ', [[0.0, 9.55], [0.0, -9.55]]), ('QR', [[0.0, -9.55], [-8.3, -9.55]]), ('PR', [[0.0, 9.55], [-8.3, -9.55]]), ('north', [[0.0, -9.55], [0.0, 14.0]])]:
                c.line(points, id=object_id)
            c.line([[0.0, -9.035678485231841], [-0.5143215147681596, -9.035678485231841]], id='right_Q', zorder=3)
            c.line([[-0.5143215147681596, -9.035678485231841], [-0.5143215147681596, -9.55]], id='right_Q', zorder=3)
            c.path([[-7.385650640412162, -9.55], [-7.385650640412162, -9.3718625600646], [-7.437708883534423, -9.197548968862371], [-7.535396561216597, -9.048585667556974], [-7.633084238898771, -8.899622366251577], [-7.772207478110156, -8.782404564420432], [-7.935585586268342, -8.711407794906664]], [1, 4, 4, 4, 4, 4, 4], id='angle_a_arc', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('P', [0.0, 9.55], id='v_P', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-13.5, 10.5], annotation_clip=None)
            c.text('Q', [0.0, -9.55], id='v_Q', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[12.0, -12.0], annotation_clip=None)
            c.text('R', [-8.3, -9.55], id='v_R', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12.0, -12.0], annotation_clip=None)
            c.text('N', [0.0, 14.0], id='v_N', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0.0, 12.0], annotation_clip=None)
            c.text('h km', [-4.15, 0.0], id='hkm', rotation_mode='default', offset_pt=[-42, -20], annotation_clip=None)
            c.text('a°', [-8.3, -9.55], id='adeg', rotation_mode='default', offset_pt=[35.67901012088426, 23.397706751694347], annotation_clip=None)
            c.text('191 km', [0.0, 0.0], id='given191', rotation_mode='default', offset_pt=[37.33333333333333, 0.0], annotation_clip=None)
            c.text('83 km', [-4.15, -9.55], id='given83', rotation_mode='default', offset_pt=[0.0, -14.666666666666666], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane09().draw(sys.argv[1] if len(sys.argv) > 1 else None))
