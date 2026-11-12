"""Frozen question Solid233; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid233:

    def __init__(self):
        self.id = 'Solid233'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2690'
        self.question = 'A shape is created by joining seven unit cubes, as shown. What is the ratio of the volume in cubic units to the surface area in square units?\n\nChoices:\nA:1 : 6\nB:7 : 36\nC:1 : 5\nD:7 : 30\nE:6 : 25'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '1 : 6', 'B': '7 : 36', 'C': '1 : 5', 'D': '7 : 30', 'E': '6 : 25'}
        self.query = self.question
        self.points = {'blockp0': [-1.0, 0.0, 1.0],
         'blockp1': [2.0, 0.0, 1.0],
         'blockp2': [1.0, -1.0, 1.0],
         'blockp3': [1.0, 2.0, 1.0],
         'blockp4': [1.0, 0.0, -1.0],
         'blockp5': [1.0, 0.0, 2.0],
         'blockp6': [-1.0, 0.0, 0.0],
         'blockp7': [-0.5, 0.0, 0.0],
         'blockp8': [1.0, 0.0, 0.0],
         'blockp9': [2.0, 0.0, 0.0],
         'blockp10': [-1.0, 1.0, 1.0],
         'blockp11': [-0.5, 1.0, 1.0],
         'blockp12': [1.0, 1.0, 1.0],
         'blockp13': [2.0, 1.0, 1.0],
         'blockp14': [-1.0, 0.0, 1.0],
         'blockp15': [-1.0, 1.0, 1.0],
         'blockp16': [-1.0, 0.0, 0.0],
         'blockp17': [-1.0, 0.0, 1.0],
         'blockp18': [2.0, 0.0, 0.0],
         'blockp19': [2.0, 1.0, 0.0],
         'blockp20': [2.0, 0.0, 1.0],
         'blockp21': [2.0, 1.0, 1.0],
         'blockp22': [2.0, 0.0, 0.0],
         'blockp23': [2.0, 0.0, 1.0],
         'blockp24': [2.0, 1.0, 0.0],
         'blockp25': [2.0, 1.0, 1.0],
         'blockp26': [0.0, -1.0, 0.0],
         'blockp27': [1.0, -1.0, 0.0],
         'blockp28': [0.0, -1.0, 1.0],
         'blockp29': [1.0, -1.0, 1.0],
         'blockp30': [0.0, -1.0, 1.0],
         'blockp31': [0.0, 0.0, 1.0],
         'blockp32': [1.0, -1.0, 0.0],
         'blockp33': [1.0, 0.0, 0.0],
         'blockp34': [0.0, -1.0, 0.0],
         'blockp35': [0.0, -1.0, 1.0],
         'blockp36': [1.0, -1.0, 0.0],
         'blockp37': [1.0, -1.0, 1.0],
         'blockp38': [0.5, 2.0, 1.0],
         'blockp39': [1.0, 2.0, 1.0],
         'blockp40': [1.0, 2.0, 0.7300000000000002],
         'blockp41': [1.0, 2.0, 1.0],
         'blockp42': [0.0, 0.0, -1.0],
         'blockp43': [1.0, 0.0, -1.0],
         'blockp44': [1.0, 0.0, -1.0],
         'blockp45': [1.0, 1.0, -1.0],
         'blockp46': [0.0, 0.0, -1.0],
         'blockp47': [0.0, 0.0, -0.27],
         'blockp48': [0.0, 0.0, 1.0],
         'blockp49': [0.0, 0.0, 2.0],
         'blockp50': [1.0, 1.0, -1.0],
         'blockp51': [1.0, 1.0, -0.27],
         'blockp52': [1.0, 1.0, 1.0],
         'blockp53': [1.0, 1.0, 2.0],
         'blockp54': [0.0, 0.0, 2.0],
         'blockp55': [1.0, 0.0, 2.0],
         'blockp56': [0.0, 1.0, 2.0],
         'blockp57': [1.0, 1.0, 2.0],
         'blockp58': [0.0, 0.0, 2.0],
         'blockp59': [0.0, 1.0, 2.0],
         'blockp60': [1.0, 0.0, 2.0],
         'blockp61': [1.0, 1.0, 2.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid233.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.0873619914192616, 2.5944391583990054], ylim=[-1.281783890356679, 2.400017259461588], projection=[[1, 0.5, 0], [-0.1, 0.22, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['blockp0'], self.points['blockp1']])), ('line_1', c.project([self.points['blockp2'], self.points['blockp3']])), ('line_2', c.project([self.points['blockp4'], self.points['blockp5']])), ('line_3', c.project([self.points['blockp6'], self.points['blockp7']])), ('line_4', c.project([self.points['blockp8'], self.points['blockp9']])), ('line_5', c.project([self.points['blockp10'], self.points['blockp11']])), ('line_6', c.project([self.points['blockp12'], self.points['blockp13']])), ('line_7', c.project([self.points['blockp14'], self.points['blockp15']])), ('line_8', c.project([self.points['blockp16'], self.points['blockp17']])), ('line_9', c.project([self.points['blockp18'], self.points['blockp19']])), ('line_10', c.project([self.points['blockp20'], self.points['blockp21']])), ('line_11', c.project([self.points['blockp22'], self.points['blockp23']])), ('line_12', c.project([self.points['blockp24'], self.points['blockp25']])), ('line_13', c.project([self.points['blockp26'], self.points['blockp27']])), ('line_14', c.project([self.points['blockp28'], self.points['blockp29']])), ('line_15', c.project([self.points['blockp30'], self.points['blockp31']])), ('line_16', c.project([self.points['blockp32'], self.points['blockp33']])), ('line_17', c.project([self.points['blockp34'], self.points['blockp35']])), ('line_18', c.project([self.points['blockp36'], self.points['blockp37']])), ('line_19', c.project([self.points['blockp38'], self.points['blockp39']])), ('line_20', c.project([self.points['blockp40'], self.points['blockp41']])), ('line_21', c.project([self.points['blockp42'], self.points['blockp43']])), ('line_22', c.project([self.points['blockp44'], self.points['blockp45']])), ('line_23', c.project([self.points['blockp46'], self.points['blockp47']])), ('line_24', c.project([self.points['blockp48'], self.points['blockp49']])), ('line_25', c.project([self.points['blockp50'], self.points['blockp51']])), ('line_26', c.project([self.points['blockp52'], self.points['blockp53']])), ('line_27', c.project([self.points['blockp54'], self.points['blockp55']])), ('line_28', c.project([self.points['blockp56'], self.points['blockp57']])), ('line_29', c.project([self.points['blockp58'], self.points['blockp59']])), ('line_30', c.project([self.points['blockp60'], self.points['blockp61']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid233().draw(sys.argv[1] if len(sys.argv) > 1 else None))
