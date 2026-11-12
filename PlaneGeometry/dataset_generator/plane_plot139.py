"""Frozen question Plane139; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane139:

    def __init__(self):
        self.id = 'Plane139'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:929'
        self.question = 'As shown in the figure, passing point C is the tangent of circle O, then the value of OD is ()\nChoices:\nA:1\nB:√{3}\nC:2\nD:2√{3}'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '1', 'B': '√{3}', 'C': '2', 'D': '2√{3}'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane139.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.2597762837481525, 7.681779441757497], ylim=[-5.912574021658118, 6.028981703847531], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([0.0, 0.0], 3.4641016151377544, id='o0', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            for object_id, points in [('o1', [[-3.4641016151377544, 0.0], [6.928203230275509, 0.0]]), ('o2', [[-3.4641016151377544, 0.0], [1.7320508075688772, 3.0]]), ('o3', [[1.7320508075688772, 3.0], [6.928203230275509, 0.0]]), ('o4', [[0.0, 0.0], [-0.8660254037844386, 1.5]])]:
                c.line(points, id=object_id)
            c.line([[-0.7580469268104654, 1.3129757917571723], [-0.5710227185676376, 1.4209542687311454]], id='o5', zorder=3)
            c.line([[-0.5710227185676376, 1.4209542687311454], [-0.6790011955416109, 1.6079784769739733]], id='o5', zorder=3)
            c.path([[6.595715748954926, 0.19196173684261905], [6.578940043574038, 0.1629053627901146], [6.566045375819531, 0.13177488101488824], [6.5573616317243255, 0.09936670685165602], [6.54867788762912, 0.06695853268842379], [6.544279756590271, 0.03355141076177585], [6.544279756590271, 4.7017065316616e-17]], [1, 4, 4, 4, 4, 4, 4], id='o6', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('30°', [6.928203230275509, 0.0], id='l0', rotation_mode='default', offset_pt=[-58.103657427720265, 10.245242482348885], annotation_clip=None)
            c.text('6', [4.330127018922193, 1.5], id='l1', rotation_mode='default', offset_pt=[4, 16], annotation_clip=None)
            c.text('O', [0.0, 0.0], id='l2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            c.text('A', [-3.4641016151377544, 0.0], id='l3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 0], annotation_clip=None)
            c.text('B', [3.4641016151377544, 0.0], id='l4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8.24105610394364, -17.673001847214675], annotation_clip=None)
            c.text('C', [1.7320508075688772, 3.0], id='l5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 15], annotation_clip=None)
            c.text('D', [-0.8660254037844386, 1.5], id='l6', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-9, 12], annotation_clip=None)
            c.text('E', [6.928203230275509, 0.0], id='l7', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane139().draw(sys.argv[1] if len(sys.argv) > 1 else None))
