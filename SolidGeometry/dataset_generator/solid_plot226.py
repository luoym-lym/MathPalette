"""Frozen question Solid226; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid226:

    def __init__(self):
        self.id = 'Solid226'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2547'
        self.question = 'All six sides of a rectangular solid were rectangles.  A one-foot cube was cut out of the rectangular solid as shown.  The total number of square feet in the surface of the new solid is how many more or less than that of the original solid?\n\nChoices:\nA:$2\\text{ less}$\nB:$1\\text{ less}$\nC:$\\text{the same}$\nD:$1\\text{ more}$\nE:$2\\text{ more}$'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': '$2\\text{ less}$', 'B': '$1\\text{ less}$', 'C': '$\\text{the same}$', 'D': '$1\\text{ more}$', 'E': '$2\\text{ more}$'}
        self.query = self.question
        self.points = {'0_0': [0, 0, 0],
         '1_0': [1, 0, 0],
         '0_1': [0, 9, 0],
         '1_1': [1, 9, 0],
         '0_2': [0, 9, 3],
         '1_2': [1, 9, 3],
         '0_3': [0, 5, 3],
         '1_3': [1, 5, 3],
         '0_4': [0, 5, 2],
         '1_4': [1, 5, 2],
         '0_5': [0, 4, 2],
         '1_5': [1, 4, 2],
         '0_6': [0, 4, 3],
         '1_6': [1, 4, 3],
         '0_7': [0, 0, 3],
         '1_7': [1, 0, 3],
         'width': [0.5, 0, 0],
         'height': [1, 0, 1.5],
         'length': [1, 4.5, 0],
         'notchw': [0.5, 5, 2],
         'notchdepth': [1, 5, 2.5],
         'notchl': [1, 4.5, 2],
         'blockp22': [0.0, 0.0, 0.0],
         'blockp23': [1.0, 0.0, 0.0],
         'blockp24': [0.0, 0.0, 3.0],
         'blockp25': [1.0, 0.0, 3.0],
         'blockp26': [0.0, 4.0, 3.0],
         'blockp27': [1.0, 4.0, 3.0],
         'blockp28': [0.0, 0.0, 3.0],
         'blockp29': [0.0, 4.0, 3.0],
         'blockp30': [0.0, 5.0, 3.0],
         'blockp31': [0.0, 9.0, 3.0],
         'blockp32': [1.0, 0.0, 0.0],
         'blockp33': [1.0, 9.0, 0.0],
         'blockp34': [1.0, 0.0, 3.0],
         'blockp35': [1.0, 4.0, 3.0],
         'blockp36': [1.0, 5.0, 3.0],
         'blockp37': [1.0, 9.0, 3.0],
         'blockp38': [0.0, 0.0, 0.0],
         'blockp39': [0.0, 0.0, 3.0],
         'blockp40': [1.0, 0.0, 0.0],
         'blockp41': [1.0, 0.0, 3.0],
         'blockp42': [1.0, 4.0, 0.0],
         'blockp43': [1.0, 4.0, 3.0],
         'blockp44': [0.20000000000000018, 5.0, 2.0],
         'blockp45': [1.0, 5.0, 2.0],
         'blockp46': [1.0, 4.0, 2.0],
         'blockp47': [1.0, 5.0, 2.0],
         'blockp48': [1.0, 5.0, 0.0],
         'blockp49': [1.0, 5.0, 3.0],
         'blockp50': [0.0, 5.0, 3.0],
         'blockp51': [1.0, 5.0, 3.0],
         'blockp52': [0.0, 9.0, 3.0],
         'blockp53': [1.0, 9.0, 3.0],
         'blockp54': [0.0, 5.0, 2.5],
         'blockp55': [0.0, 5.0, 3.0],
         'blockp56': [1.0, 9.0, 0.0],
         'blockp57': [1.0, 9.0, 3.0],
         'blockp58': [0.0, 0.0, 0.0],
         'blockp59': [1.0, 0.0, 0.0],
         'blockp60': [0.0, 0.0, 3.0],
         'blockp61': [1.0, 0.0, 3.0],
         'blockp62': [0.0, 4.0, 3.0],
         'blockp63': [1.0, 4.0, 3.0],
         'blockp64': [0.0, 0.0, 3.0],
         'blockp65': [0.0, 4.0, 3.0],
         'blockp66': [0.0, 5.0, 3.0],
         'blockp67': [0.0, 9.0, 3.0],
         'blockp68': [1.0, 0.0, 0.0],
         'blockp69': [1.0, 9.0, 0.0],
         'blockp70': [1.0, 0.0, 3.0],
         'blockp71': [1.0, 4.0, 3.0],
         'blockp72': [1.0, 5.0, 3.0],
         'blockp73': [1.0, 9.0, 3.0],
         'blockp74': [0.0, 0.0, 0.0],
         'blockp75': [0.0, 0.0, 3.0],
         'blockp76': [1.0, 0.0, 0.0],
         'blockp77': [1.0, 0.0, 3.0],
         'blockp78': [1.0, 4.0, 2],
         'blockp79': [1.0, 4.0, 3.0],
         'blockp80': [0.20000000000000018, 5.0, 2.0],
         'blockp81': [1.0, 5.0, 2.0],
         'blockp82': [1.0, 4.0, 2.0],
         'blockp83': [1.0, 5.0, 2.0],
         'blockp84': [1.0, 5.0, 2],
         'blockp85': [1.0, 5.0, 3.0],
         'blockp86': [0.0, 5.0, 3.0],
         'blockp87': [1.0, 5.0, 3.0],
         'blockp88': [0.0, 9.0, 3.0],
         'blockp89': [1.0, 9.0, 3.0],
         'blockp90': [0.0, 5.0, 2.5],
         'blockp91': [0.0, 5.0, 3.0],
         'blockp92': [1.0, 9.0, 0.0],
         'blockp93': [1.0, 9.0, 3.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid226.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.20154224187449366, 8.418123033084179], ylim=[-0.7464753940660165, 7.873189880892656], projection=[[1, 0.8, 0], [0, 0.5, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['blockp58'], self.points['blockp59']])), ('line_1', c.project([self.points['blockp60'], self.points['blockp61']])), ('line_2', c.project([self.points['blockp62'], self.points['blockp63']])), ('line_3', c.project([self.points['blockp64'], self.points['blockp65']])), ('line_4', c.project([self.points['blockp66'], self.points['blockp67']])), ('line_5', c.project([self.points['blockp68'], self.points['blockp69']])), ('line_6', c.project([self.points['blockp70'], self.points['blockp71']])), ('line_7', c.project([self.points['blockp72'], self.points['blockp73']])), ('line_8', c.project([self.points['blockp74'], self.points['blockp75']])), ('line_9', c.project([self.points['blockp76'], self.points['blockp77']])), ('line_10', c.project([self.points['blockp78'], self.points['blockp79']])), ('line_11', c.project([self.points['blockp80'], self.points['blockp81']])), ('line_12', c.project([self.points['blockp82'], self.points['blockp83']])), ('line_13', c.project([self.points['blockp84'], self.points['blockp85']])), ('line_14', c.project([self.points['blockp86'], self.points['blockp87']])), ('line_15', c.project([self.points['blockp88'], self.points['blockp89']])), ('line_16', c.project([self.points['blockp90'], self.points['blockp91']])), ('line_17', c.project([self.points['blockp92'], self.points['blockp93']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('1′', c.project(self.points['width']), offset_pt=[0, -18], vertex=False, id='label_0')
            c.text('3′', c.project(self.points['height']), offset_pt=[18, 0], vertex=False, id='label_1')
            c.text('9′', c.project(self.points['length']), offset_pt=[0, -20], vertex=False, id='label_2')
            c.text('1′', c.project(self.points['notchw']), offset_pt=[0, 15], vertex=False, id='label_3')
            c.text('1′', c.project(self.points['notchdepth']), offset_pt=[17, 0], vertex=False, id='label_4')
            c.text('1′', c.project(self.points['notchl']), offset_pt=[0, -20], vertex=False, id='label_5')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid226().draw(sys.argv[1] if len(sys.argv) > 1 else None))
