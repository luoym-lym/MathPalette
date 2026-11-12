"""Frozen question Plane43; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane43:

    def __init__(self):
        self.id = 'Plane43'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/403'
        self.question = 'Find TX if $E X=24$ and $D E=7$\nChoices:\nA: 7\nB: 24\nC: 25\nD: 32'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '7', 'B': '24', 'C': '25', 'D': '32'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane43.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-27.325163687128732, 9.341441245311334], ylim=[-18.26385802177559, 18.402746910664476], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 7.0, id='o1', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('o2', [[-25.0, 0.0], [-1.96, 6.72]]), ('o3', [[-25.0, 0.0], [-1.96, -6.72]]), ('o4', [[-25.0, 0.0], [7.0, 0.0]]), ('o5', [[0.0, 0.0], [-1.96, 6.72]]), ('o6', [[0.0, 0.0], [-1.96, -6.72]])]:
                c.line(points, id=object_id)
            for object_id, points in [('o7', [[-2.5965730022993068, 6.534332874329369], [-2.4109058766286755, 5.897759872030062]]), ('o7', [[-2.4109058766286755, 5.897759872030062], [-1.774332874329369, 6.083426997700693]]), ('o9', [[-2.5965730022993068, -6.534332874329369], [-2.4109058766286755, -5.897759872030062]]), ('o9', [[-2.4109058766286755, -5.897759872030062], [-1.774332874329369, -6.083426997700693]])]:
                c.line(points, id=object_id, zorder=3)
            c.point([[0.0, 0.0]], id='o11')
            c.text('X', [-25.0, 0.0], id='v12', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 0], annotation_clip=None)
            c.text('A', [-1.96, 6.72], id='v13', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 14], annotation_clip=None)
            c.text('E', [-1.96, -6.72], id='v14', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            c.text('D', [0.0, 0.0], id='v15', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[10, 13], annotation_clip=None)
            c.text('Q', [-7.0, 0.0], id='v16', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-8, -15], annotation_clip=None)
            c.text('T', [7.0, 0.0], id='v17', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane43().draw(sys.argv[1] if len(sys.argv) > 1 else None))
