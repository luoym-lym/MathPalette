"""Frozen question Plane35; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane35:

    def __init__(self):
        self.id = 'Plane35'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/271'
        self.question = 'Find y\nChoices:\nA: 3\nB: 4.5\nC: 5\nD: 6'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '3', 'B': '4.5', 'C': '5', 'D': '6'}
        self.query = self.question
        self._geometry_01 = [('o1', [[-3.0, 10.0], [21.0, 10.0]]),
         ('o3', [[21.0, 10.0], [20.559646170927522, 9.823858468371007]]),
         ('o5', [[21.0, 10.0], [20.559646170927522, 10.176141531628993]]),
         ('o7', [[-3.0, 10.0], [-2.5596461709275204, 9.823858468371007]]),
         ('o9', [[-3.0, 10.0], [-2.5596461709275204, 10.176141531628993]]),
         ('o10', [[-3.0, 5.0], [21.0, 5.0]]),
         ('o12', [[21.0, 5.0], [20.559646170927522, 4.823858468371008]]),
         ('o14', [[21.0, 5.0], [20.559646170927522, 5.176141531628992]]),
         ('o16', [[-3.0, 5.0], [-2.5596461709275204, 4.823858468371008]]),
         ('o18', [[-3.0, 5.0], [-2.5596461709275204, 5.176141531628992]]),
         ('o19', [[-3.0, 0.0], [21.0, 0.0]]),
         ('o21', [[21.0, 0.0], [20.559646170927522, -0.17614153162899185]]),
         ('o23', [[21.0, 0.0], [20.559646170927522, 0.17614153162899185]]),
         ('o25', [[-3.0, 0.0], [-2.5596461709275204, -0.17614153162899185]]),
         ('o27', [[-3.0, 0.0], [-2.5596461709275204, 0.17614153162899185]]),
         ('o28', [[-3.4641016151377553, -2.0], [20.784609690826528, 12.0]]),
         ('o30', [[20.784609690826528, 12.0], [20.491322854010505, 11.627280044411554]]),
         ('o32', [[20.784609690826528, 12.0], [20.315181322381513, 11.932366126515968]]),
         ('o34', [[-3.4641016151377553, -2.0], [-2.9946732466927415, -1.9323661265159673]]),
         ('o36', [[-3.4641016151377553, -2.0], [-3.1708147783217333, -1.6272800444115532]]),
         ('o37', [[18.0, -3.0], [18.0, 13.0]]),
         ('o39', [[18.0, 13.0], [18.176141531628993, 12.55964617092752]]),
         ('o41', [[18.0, 13.0], [17.823858468371007, 12.55964617092752]]),
         ('o43', [[18.0, -3.0], [18.176141531628993, -2.5596461709275204]]),
         ('o45', [[18.0, -3.0], [17.823858468371007, -2.5596461709275204]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane35.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.145860412297038, 23.393800932556452], ylim=[-8.777306501981766, 18.762354842871726], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            for object_id, points in [('o46', [[12.979260255356621, 7.68527537659431], [13.145273838888002, 7.39773141517138]]), ('o46', [[12.835488274645158, 7.60226858482862], [13.001501858176539, 7.31472462340569]]), ('o47', [[4.319006217512237, 2.6852753765943094], [4.485019801043616, 2.39773141517138]]), ('o47', [[4.1752342368007715, 2.60226858482862], [4.341247820332151, 2.3147246234056906]]), ('o48', [[17.83398641646862, 7.5], [18.16601358353138, 7.5]]), ('o49', [[17.83398641646862, 2.5], [18.16601358353138, 2.5]])]:
                c.line(points, id=object_id, zorder=3)
            c.line([[16.920508075688776, 10.69282032302755], [8.260254037844387, 5.692820323027551]], id='dim0_line', linestyle=(0, [4, 3]))
            c.line([[17.320508075688775, 10.0], [16.920508075688776, 10.69282032302755]], id='dim0_start')
            c.line([[8.660254037844387, 5.0], [8.260254037844387, 5.692820323027551]], id='dim0_end')
            c.line([[9.060254037844388, 4.307179676972449], [0.4, -0.692820323027551]], id='dim1_line', linestyle=(0, [4, 3]))
            c.line([[8.660254037844387, 5.0], [9.060254037844388, 4.307179676972449]], id='dim1_start')
            c.line([[0.0, 0.0], [0.4, -0.692820323027551]], id='dim1_end')
            c.line([[19.4, 10.0], [19.4, 5.0]], id='dim2_line', linestyle=(0, [4, 3]))
            c.line([[18.0, 10.0], [19.4, 10.0]], id='dim2_start')
            c.line([[18.0, 5.0], [19.4, 5.0]], id='dim2_end')
            c.line([[19.4, 5.0], [19.4, 0.0]], id='dim3_line', linestyle=(0, [4, 3]))
            c.line([[18.0, 5.0], [19.4, 5.0]], id='dim3_start')
            c.line([[18.0, 0.0], [19.4, 0.0]], id='dim3_end')
            c.text('20 − 5x', [12.590381056766581, 8.19282032302755], id='t51', rotation_mode='default', offset_pt=[-12.0, 20.784609690826528], annotation_clip=None)
            c.text('2x + 6', [4.730127018922194, 1.807179676972449], id='t53', rotation_mode='default', offset_pt=[12.0, -20.784609690826528], annotation_clip=None)
            c.text('y', [19.4, 7.5], id='t55', rotation_mode='default', offset_pt=[38, 0], annotation_clip=None)
            c.text('$\\frac{3}{5}y + 2$', [19.4, 2.5], id='t57', rotation_mode='default', offset_pt=[38, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane35().draw(sys.argv[1] if len(sys.argv) > 1 else None))
