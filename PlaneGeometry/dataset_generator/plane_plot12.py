"""Frozen question Plane12; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane12:

    def __init__(self):
        self.id = 'Plane12'
        self.source_dataset = 'MathVerse'
        self.source_key = 's1924'
        self.question = 'Consider the adjacent figure:\n\nSolve for the exact value of x.'
        self.answer = '\\[\\frac{\\sqrt{30}}{2}\\]'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane12.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.06904249274962493, 2.810913655212171], ylim=[-0.7075537901329733, 2.1724023578288225], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('AB', [[0.0, 0.0], [0.0, 1.5811388300841895]]), ('BC', [[0.0, 1.5811388300841895], [2.738612787525831, 0.0]]), ('AC', [[0.0, 0.0], [2.738612787525831, 0.0]])]:
                c.line(points, id=object_id)
            c.line([[0.0, 0.05208254029155446], [0.05208254029155446, 0.05208254029155446]], id='rightA', zorder=3)
            c.line([[0.05208254029155446, 0.05208254029155446], [0.05208254029155446, 0.0]], id='rightA', zorder=3)
            c.path([[2.658426471106075, 0.046295591370270624], [2.6543806585705365, 0.03928803850081865], [2.6512708395043156, 0.03178027113462152], [2.6491765728300916, 0.023964361501819874], [2.647082306155868, 0.016148451869018223], [2.6460216047852896, 0.008091625071077278], [2.6460216047852896, 1.1339149557247152e-17]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_C30', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('30°', [2.738612787525831, 0.0], id='C30', rotation_mode='default', offset_pt=[-55.06227482358146, 10.205189427560272], annotation_clip=None)
            c.text('√10', [1.3693063937629155, 0.7905694150420948], id='hyp', rotation_mode='default', offset_pt=[18, 18], annotation_clip=None)
            c.text('x', [1.3693063937629155, 0.0], id='x', rotation_mode='default', offset_pt=[0.0, -16.0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane12().draw(sys.argv[1] if len(sys.argv) > 1 else None))
