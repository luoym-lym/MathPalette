"""Frozen question Solid230; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid230:

    def __init__(self):
        self.id = 'Solid230'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2615'
        self.question = 'Three dice with faces numbered 1 through 6 are stacked as shown. Seven of the eighteen faces are visible, leaving eleven faces hidden (back, bottom, between). The total number of dots NOT visible in this view is'
        self.answer = '41'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'blockp0': [0.0, 0.0, 0.0],
         'blockp1': [1.0, 0.0, 0.0],
         'blockp2': [0.0, 0.0, 1.0],
         'blockp3': [1.0, 0.0, 1.0],
         'blockp4': [1.0, 0.0, 0.0],
         'blockp5': [1.0, 1.0, 0.0],
         'blockp6': [1.0, 0.0, 1.0],
         'blockp7': [1.0, 1.0, 1.0],
         'blockp8': [0.0, 0.0, 0.0],
         'blockp9': [0.0, 0.0, 3.0],
         'blockp10': [1.0, 0.0, 0.0],
         'blockp11': [1.0, 0.0, 3.0],
         'blockp12': [1.0, 1.0, 0.0],
         'blockp13': [1.0, 1.0, 3.0],
         'blockp14': [0.0, 0.0, 2.0],
         'blockp15': [1.0, 0.0, 2.0],
         'blockp16': [1.0, 0.0, 2.0],
         'blockp17': [1.0, 1.0, 2.0],
         'blockp18': [0.0, 0.0, 3.0],
         'blockp19': [1.0, 0.0, 3.0],
         'blockp20': [0.0, 1.0, 3.0],
         'blockp21': [1.0, 1.0, 3.0],
         'blockp22': [0.0, 0.0, 3.0],
         'blockp23': [0.0, 1.0, 3.0],
         'blockp24': [1.0, 0.0, 3.0],
         'blockp25': [1.0, 1.0, 3.0],
         'front0pip0': [0.25, 0, 0.25],
         'front0pip1': [0.25, 0, 0.75],
         'front0pip2': [0.75, 0, 0.25],
         'front0pip3': [0.75, 0, 0.75],
         'front0pip4': [0.5, 0, 0.5],
         'front1pip0': [0.25, 0, 1.25],
         'front1pip1': [0.25, 0, 1.75],
         'front1pip2': [0.75, 0, 1.25],
         'front1pip3': [0.75, 0, 1.75],
         'front2pip0': [0.25, 0, 2.75],
         'front2pip1': [0.75, 0, 2.25],
         'right0pip0': [1, 0.5, 0.5],
         'right1pip0': [1, 0.25, 1.25],
         'right1pip1': [1, 0.5, 1.25],
         'right1pip2': [1, 0.75, 1.25],
         'right1pip3': [1, 0.25, 1.75],
         'right1pip4': [1, 0.5, 1.75],
         'right1pip5': [1, 0.75, 1.75],
         'right2pip0': [1, 0.25, 2.25],
         'right2pip1': [1, 0.5, 2.5],
         'right2pip2': [1, 0.75, 2.75],
         'top3pip0': [0.5, 0.5, 3]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid230.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.0900172594615878, 2.591783890356679], ylim=[-0.09443915839900519, 3.587361991419262], projection=[[1, 0.5, 0], [0, 0.5, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('line_0', c.project([self.points['blockp0'], self.points['blockp1']])), ('line_1', c.project([self.points['blockp2'], self.points['blockp3']])), ('line_2', c.project([self.points['blockp4'], self.points['blockp5']])), ('line_3', c.project([self.points['blockp6'], self.points['blockp7']])), ('line_4', c.project([self.points['blockp8'], self.points['blockp9']])), ('line_5', c.project([self.points['blockp10'], self.points['blockp11']])), ('line_6', c.project([self.points['blockp12'], self.points['blockp13']])), ('line_7', c.project([self.points['blockp14'], self.points['blockp15']])), ('line_8', c.project([self.points['blockp16'], self.points['blockp17']])), ('line_9', c.project([self.points['blockp18'], self.points['blockp19']])), ('line_10', c.project([self.points['blockp20'], self.points['blockp21']])), ('line_11', c.project([self.points['blockp22'], self.points['blockp23']])), ('line_12', c.project([self.points['blockp24'], self.points['blockp25']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('front0pip0', c.project([self.points['front0pip0']])), ('front0pip1', c.project([self.points['front0pip1']])), ('front0pip2', c.project([self.points['front0pip2']])), ('front0pip3', c.project([self.points['front0pip3']])), ('front0pip4', c.project([self.points['front0pip4']])), ('front1pip0', c.project([self.points['front1pip0']])), ('front1pip1', c.project([self.points['front1pip1']])), ('front1pip2', c.project([self.points['front1pip2']])), ('front1pip3', c.project([self.points['front1pip3']])), ('front2pip0', c.project([self.points['front2pip0']])), ('front2pip1', c.project([self.points['front2pip1']])), ('right0pip0', c.project([self.points['right0pip0']])), ('right1pip0', c.project([self.points['right1pip0']])), ('right1pip1', c.project([self.points['right1pip1']])), ('right1pip2', c.project([self.points['right1pip2']])), ('right1pip3', c.project([self.points['right1pip3']])), ('right1pip4', c.project([self.points['right1pip4']])), ('right1pip5', c.project([self.points['right1pip5']])), ('right2pip0', c.project([self.points['right2pip0']])), ('right2pip1', c.project([self.points['right2pip1']])), ('right2pip2', c.project([self.points['right2pip2']])), ('top3pip0', c.project([self.points['top3pip0']]))]:
                c.point(points, id=object_id, filled=True)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid230().draw(sys.argv[1] if len(sys.argv) > 1 else None))
