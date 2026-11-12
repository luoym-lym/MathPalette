"""Frozen question Solid232; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid232:

    def __init__(self):
        self.id = 'Solid232'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2648'
        self.question = 'Fourteen white cubes are put together to form the figure on the right. The complete surface of the figure, including the bottom, is painted red. The figure is then separated into individual cubes. How many of the individual cubes have exactly four red faces?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'blockp0': [0.30000000000000004, 1.0, 1.0],
         'blockp1': [1.9928057553956835, 1.0, 1.0],
         'blockp2': [3.3000000000000003, 1.0, 1.0],
         'blockp3': [4.0, 1.0, 1.0],
         'blockp4': [1.0, 0.0, 1.0],
         'blockp5': [1.0, 3.0, 1.0],
         'blockp6': [1.0, 1.0, 0.305],
         'blockp7': [1.0, 1.0, 2.0],
         'blockp8': [0.0, 3.0, 0.0],
         'blockp9': [4.0, 3.0, 0.0],
         'blockp10': [0.0, 3.0, 1.0],
         'blockp11': [4.0, 3.0, 1.0],
         'blockp12': [0.0, 3.0, 0.0],
         'blockp13': [0.0, 3.0, 2.0],
         'blockp14': [1.0, 3.0, 0.0],
         'blockp15': [1.0, 3.0, 2.0],
         'blockp16': [1.0, 0.0, 1.0],
         'blockp17': [2.3, 0.0, 1.0],
         'blockp18': [2.0, 0.0, 1.0],
         'blockp19': [2.0, 0.5611510791366903, 1.0],
         'blockp20': [2.0, 2.0, 1.0],
         'blockp21': [2.0, 3.0, 1.0],
         'blockp22': [1.0, 2.0, 1.0],
         'blockp23': [2.3, 2.0, 1.0],
         'blockp24': [2.0, 3.0, 0.0],
         'blockp25': [2.0, 3.0, 1.0],
         'blockp26': [3.0, 3.0, 0.0],
         'blockp27': [3.0, 3.0, 2.0],
         'blockp28': [4.0, 0.0, 0.0],
         'blockp29': [4.0, 3.0, 0.0],
         'blockp30': [4.0, 0.0, 1.0],
         'blockp31': [4.0, 3.0, 1.0],
         'blockp32': [4.0, 0.0, 0.0],
         'blockp33': [4.0, 0.0, 2.0],
         'blockp34': [4.0, 1.0, 0.0],
         'blockp35': [4.0, 1.0, 2.0],
         'blockp36': [4.0, 2.0, 0.0],
         'blockp37': [4.0, 2.0, 2.0],
         'blockp38': [4.0, 3.0, 0.0],
         'blockp39': [4.0, 3.0, 2.0],
         'blockp40': [0.0, 0.0, 2.0],
         'blockp41': [1.0, 0.0, 2.0],
         'blockp42': [3.0, 0.0, 2.0],
         'blockp43': [4.0, 0.0, 2.0],
         'blockp44': [0.0, 1.0, 2.0],
         'blockp45': [1.0, 1.0, 2.0],
         'blockp46': [3.0, 1.0, 2.0],
         'blockp47': [4.0, 1.0, 2.0],
         'blockp48': [0.0, 0.0, 2.0],
         'blockp49': [0.0, 1.0, 2.0],
         'blockp50': [0.0, 2.0, 2.0],
         'blockp51': [0.0, 3.0, 2.0],
         'blockp52': [1.0, 0.0, 2.0],
         'blockp53': [1.0, 1.0, 2.0],
         'blockp54': [1.0, 2.0, 2.0],
         'blockp55': [1.0, 3.0, 2.0],
         'blockp56': [0.0, 1.0, 1.305],
         'blockp57': [0.0, 1.0, 2.0],
         'blockp58': [1.0, 0.0, 1.0],
         'blockp59': [1.0, 0.0, 2.0],
         'blockp60': [0.0, 2.0, 2.0],
         'blockp61': [1.0, 2.0, 2.0],
         'blockp62': [3.0, 2.0, 2.0],
         'blockp63': [4.0, 2.0, 2.0],
         'blockp64': [0.0, 3.0, 2.0],
         'blockp65': [1.0, 3.0, 2.0],
         'blockp66': [3.0, 3.0, 2.0],
         'blockp67': [4.0, 3.0, 2.0],
         'blockp68': [1.0, 2.0, 1.0],
         'blockp69': [1.0, 2.0, 2.0],
         'blockp70': [3.0, 0.0, 2.0],
         'blockp71': [3.0, 1.0, 2.0],
         'blockp72': [3.0, 2.0, 2.0],
         'blockp73': [3.0, 3.0, 2.0],
         'blockp74': [4.0, 0.0, 2.0],
         'blockp75': [4.0, 1.0, 2.0],
         'blockp76': [4.0, 2.0, 2.0],
         'blockp77': [4.0, 3.0, 2.0],
         'blockp78': [3.0, 1.0, 1.3050000000000002],
         'blockp79': [3.0, 1.0, 2.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid232.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.252259470759285, 4.164593961781123], ylim=[-3.5849662089073546, 2.831887223633054], projection=[[1, -0.7, 0], [-0.35, -0.45, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['blockp0'], self.points['blockp1']])), ('line_1', c.project([self.points['blockp2'], self.points['blockp3']])), ('line_2', c.project([self.points['blockp4'], self.points['blockp5']])), ('line_3', c.project([self.points['blockp6'], self.points['blockp7']])), ('line_4', c.project([self.points['blockp8'], self.points['blockp9']])), ('line_5', c.project([self.points['blockp10'], self.points['blockp11']])), ('line_6', c.project([self.points['blockp12'], self.points['blockp13']])), ('line_7', c.project([self.points['blockp14'], self.points['blockp15']])), ('line_8', c.project([self.points['blockp16'], self.points['blockp17']])), ('line_9', c.project([self.points['blockp18'], self.points['blockp19']])), ('line_10', c.project([self.points['blockp20'], self.points['blockp21']])), ('line_11', c.project([self.points['blockp22'], self.points['blockp23']])), ('line_12', c.project([self.points['blockp24'], self.points['blockp25']])), ('line_13', c.project([self.points['blockp26'], self.points['blockp27']])), ('line_14', c.project([self.points['blockp28'], self.points['blockp29']])), ('line_15', c.project([self.points['blockp30'], self.points['blockp31']])), ('line_16', c.project([self.points['blockp32'], self.points['blockp33']])), ('line_17', c.project([self.points['blockp34'], self.points['blockp35']])), ('line_18', c.project([self.points['blockp36'], self.points['blockp37']])), ('line_19', c.project([self.points['blockp38'], self.points['blockp39']])), ('line_20', c.project([self.points['blockp40'], self.points['blockp41']])), ('line_21', c.project([self.points['blockp42'], self.points['blockp43']])), ('line_22', c.project([self.points['blockp44'], self.points['blockp45']])), ('line_23', c.project([self.points['blockp46'], self.points['blockp47']])), ('line_24', c.project([self.points['blockp48'], self.points['blockp49']])), ('line_25', c.project([self.points['blockp50'], self.points['blockp51']])), ('line_26', c.project([self.points['blockp52'], self.points['blockp53']])), ('line_27', c.project([self.points['blockp54'], self.points['blockp55']])), ('line_28', c.project([self.points['blockp56'], self.points['blockp57']])), ('line_29', c.project([self.points['blockp58'], self.points['blockp59']])), ('line_30', c.project([self.points['blockp60'], self.points['blockp61']])), ('line_31', c.project([self.points['blockp62'], self.points['blockp63']])), ('line_32', c.project([self.points['blockp64'], self.points['blockp65']])), ('line_33', c.project([self.points['blockp66'], self.points['blockp67']])), ('line_34', c.project([self.points['blockp68'], self.points['blockp69']])), ('line_35', c.project([self.points['blockp70'], self.points['blockp71']])), ('line_36', c.project([self.points['blockp72'], self.points['blockp73']])), ('line_37', c.project([self.points['blockp74'], self.points['blockp75']])), ('line_38', c.project([self.points['blockp76'], self.points['blockp77']])), ('line_39', c.project([self.points['blockp78'], self.points['blockp79']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid232().draw(sys.argv[1] if len(sys.argv) > 1 else None))
