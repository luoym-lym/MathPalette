"""Frozen question Plane412; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane412:

    def __init__(self):
        self.id = 'Plane412'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1761'
        self.question = 'The diagram shows squares of three different sizes arranged into a rectangle. The length of each side of the smallest squares is $20 \\mathrm{~cm}$. What is the length of the marked path from $P$ to $Q$?\nChoices:\nA:$380 \\mathrm{~cm}$\nB:$400 \\mathrm{~cm}$\nC:$420 \\mathrm{~cm}$\nD:$440 \\mathrm{~cm}$\nE:$460 \\mathrm{~cm}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$380 \\mathrm{~cm}$', 'B': '$400 \\mathrm{~cm}$', 'C': '$420 \\mathrm{~cm}$', 'D': '$440 \\mathrm{~cm}$', 'E': '$460 \\mathrm{~cm}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane412.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.3741684612807235, 6.385814873317761], ylim=[-0.19366542151364552, 7.566317913084839], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('edge0', [[0.0, 0.0], [0.0, 1.0]]), ('edge1', [[0.0, 0.0], [1.0, 0.0]]), ('edge2', [[0.0, 1.0], [0.0, 2.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            for object_id, points in [('edge3', [[0.0, 2.0], [0.0, 3.0]]), ('edge4', [[0.0, 2.0], [1.0, 2.0]]), ('edge5', [[0.0, 3.0], [0.0, 4.0]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[0.0, 4.0], [0.0, 5.0]], id='edge6', zorder=0.5, color='#999999')
            c.line([[0.0, 4.0], [1.0, 4.0]], id='edge7', zorder=3)
            for object_id, points in [('edge8', [[0.0, 5.0], [0.0, 6.0]]), ('edge9', [[0.0, 6.0], [0.0, 7.0]]), ('edge10', [[0.0, 6.0], [1.0, 6.0]]), ('edge11', [[0.0, 7.0], [1.0, 7.0]]), ('edge12', [[1.0, 0.0], [2.0, 0.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            for object_id, points in [('edge13', [[1.0, 2.0], [2.0, 2.0]]), ('edge14', [[1.0, 4.0], [2.0, 4.0]]), ('edge15', [[1.0, 6.0], [1.0, 7.0]]), ('edge16', [[1.0, 6.0], [2.0, 6.0]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[1.0, 7.0], [2.0, 7.0]], id='edge17', zorder=0.5, color='#999999')
            for object_id, points in [('edge18', [[2.0, 0.0], [2.0, 1.0]]), ('edge19', [[2.0, 0.0], [3.0, 0.0]]), ('edge20', [[2.0, 1.0], [2.0, 2.0]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, points in [('edge21', [[2.0, 2.0], [2.0, 3.0]]), ('edge22', [[2.0, 3.0], [2.0, 4.0]]), ('edge23', [[2.0, 3.0], [3.0, 3.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            c.line([[2.0, 4.0], [2.0, 5.0]], id='edge24', zorder=3)
            c.line([[2.0, 4.0], [3.0, 4.0]], id='edge25', zorder=0.5, color='#999999')
            c.line([[2.0, 5.0], [2.0, 6.0]], id='edge26', zorder=3)
            c.line([[2.0, 6.0], [2.0, 7.0]], id='edge27', zorder=0.5, color='#999999')
            c.line([[2.0, 7.0], [3.0, 7.0]], id='edge28', zorder=0.5, color='#999999')
            c.line([[3.0, 0.0], [4.0, 0.0]], id='edge29', zorder=3)
            for object_id, points in [('edge30', [[3.0, 3.0], [3.0, 4.0]]), ('edge31', [[3.0, 3.0], [4.0, 3.0]]), ('edge32', [[3.0, 4.0], [4.0, 4.0]]), ('edge33', [[3.0, 7.0], [4.0, 7.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            c.line([[4.0, 0.0], [5.0, 0.0]], id='edge34', zorder=3)
            c.line([[4.0, 3.0], [4.0, 4.0]], id='edge35', zorder=3)
            c.line([[4.0, 3.0], [5.0, 3.0]], id='edge36', zorder=0.5, color='#999999')
            c.line([[4.0, 4.0], [5.0, 4.0]], id='edge37', zorder=3)
            c.line([[4.0, 7.0], [5.0, 7.0]], id='edge38', zorder=0.5, color='#999999')
            for object_id, points in [('edge39', [[5.0, 0.0], [5.0, 1.0]]), ('edge40', [[5.0, 1.0], [5.0, 2.0]]), ('edge41', [[5.0, 2.0], [5.0, 3.0]]), ('edge42', [[5.0, 3.0], [5.0, 4.0]])]:
                c.line(points, id=object_id, zorder=3)
            for object_id, points in [('edge43', [[5.0, 4.0], [5.0, 5.0]]), ('edge44', [[5.0, 5.0], [5.0, 6.0]]), ('edge45', [[5.0, 6.0], [5.0, 7.0]])]:
                c.line(points, id=object_id, zorder=0.5, color='#999999')
            c.text('P', [1.0, 7.0], id='Pname', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 17], annotation_clip=None)
            c.text('Q', [4.0, 3.0], id='Qname', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[8, -16], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane412().draw(sys.argv[1] if len(sys.argv) > 1 else None))
