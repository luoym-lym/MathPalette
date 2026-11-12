"""Frozen question Solid251; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid251:

    def __init__(self):
        self.id = 'Solid251'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid256'
        self.question = 'Each pattern consists of six identical squares, joined along complete edges. Fold along the edges shared by adjacent squares, through 90 degrees, to form a cube. Which pattern CANNOT form a cube without overlapping faces?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('o0e0', [[8.0, 74.0], [8.0, 78.2]]),
         ('o0e1', [[8.0, 74.0], [12.2, 74.0]]),
         ('o0e2', [[8.0, 78.2], [8.0, 82.4]]),
         ('o0e3', [[8.0, 78.2], [12.2, 78.2]]),
         ('o0e4', [[8.0, 82.4], [12.2, 82.4]]),
         ('o0e5', [[12.2, 74.0], [12.2, 78.2]]),
         ('o0e6', [[12.2, 78.2], [12.2, 82.4]]),
         ('o0e7', [[12.2, 78.2], [16.4, 78.2]]),
         ('o0e8', [[12.2, 82.4], [12.2, 86.6]]),
         ('o0e9', [[12.2, 82.4], [16.4, 82.4]]),
         ('o0e10', [[12.2, 86.6], [16.4, 86.6]]),
         ('o0e11', [[16.4, 78.2], [16.4, 82.4]]),
         ('o0e12', [[16.4, 82.4], [16.4, 86.6]]),
         ('o0e13', [[16.4, 82.4], [20.6, 82.4]]),
         ('o0e14', [[16.4, 86.6], [16.4, 90.8]]),
         ('o0e15', [[16.4, 86.6], [20.6, 86.6]]),
         ('o0e16', [[16.4, 90.8], [20.6, 90.8]]),
         ('o0e17', [[20.6, 82.4], [20.6, 86.6]]),
         ('o0e18', [[20.6, 86.6], [20.6, 90.8]]),
         ('o1e0', [[55.0, 74.0], [55.0, 78.2]]),
         ('o1e1', [[55.0, 74.0], [59.2, 74.0]]),
         ('o1e2', [[55.0, 78.2], [55.0, 82.4]]),
         ('o1e3', [[55.0, 78.2], [59.2, 78.2]]),
         ('o1e4', [[55.0, 82.4], [55.0, 86.6]]),
         ('o1e5', [[55.0, 82.4], [59.2, 82.4]]),
         ('o1e6', [[55.0, 86.6], [59.2, 86.6]]),
         ('o1e7', [[59.2, 74.0], [59.2, 78.2]]),
         ('o1e8', [[59.2, 78.2], [59.2, 82.4]]),
         ('o1e9', [[59.2, 82.4], [59.2, 86.6]]),
         ('o1e10', [[59.2, 82.4], [63.4, 82.4]]),
         ('o1e11', [[59.2, 86.6], [59.2, 90.8]]),
         ('o1e12', [[59.2, 86.6], [63.4, 86.6]]),
         ('o1e13', [[59.2, 90.8], [63.4, 90.8]]),
         ('o1e14', [[63.4, 82.4], [63.4, 86.6]]),
         ('o1e15', [[63.4, 82.4], [67.6, 82.4]]),
         ('o1e16', [[63.4, 86.6], [63.4, 90.8]]),
         ('o1e17', [[63.4, 86.6], [67.6, 86.6]]),
         ('o1e18', [[67.6, 82.4], [67.6, 86.6]]),
         ('o2e0', [[8.0, 46.0], [8.0, 50.2]]),
         ('o2e1', [[8.0, 46.0], [12.2, 46.0]]),
         ('o2e2', [[8.0, 50.2], [8.0, 54.4]]),
         ('o2e3', [[8.0, 50.2], [12.2, 50.2]]),
         ('o2e4', [[8.0, 54.4], [12.2, 54.4]]),
         ('o2e5', [[12.2, 46.0], [12.2, 50.2]]),
         ('o2e6', [[12.2, 50.2], [12.2, 54.4]]),
         ('o2e7', [[12.2, 50.2], [16.4, 50.2]]),
         ('o2e8', [[12.2, 54.4], [12.2, 58.6]]),
         ('o2e9', [[12.2, 54.4], [16.4, 54.4]]),
         ('o2e10', [[12.2, 58.6], [12.2, 62.8]]),
         ('o2e11', [[12.2, 58.6], [16.4, 58.6]]),
         ('o2e12', [[12.2, 62.8], [16.4, 62.8]]),
         ('o2e13', [[16.4, 50.2], [16.4, 54.4]]),
         ('o2e14', [[16.4, 54.4], [16.4, 58.6]]),
         ('o2e15', [[16.4, 58.6], [16.4, 62.8]]),
         ('o2e16', [[16.4, 58.6], [20.6, 58.6]]),
         ('o2e17', [[16.4, 62.8], [20.6, 62.8]]),
         ('o2e18', [[20.6, 58.6], [20.6, 62.8]]),
         ('o3e0', [[55.0, 46.0], [55.0, 50.2]]),
         ('o3e1', [[55.0, 46.0], [59.2, 46.0]]),
         ('o3e2', [[55.0, 50.2], [55.0, 54.4]]),
         ('o3e3', [[55.0, 50.2], [59.2, 50.2]]),
         ('o3e4', [[55.0, 54.4], [59.2, 54.4]]),
         ('o3e5', [[59.2, 46.0], [59.2, 50.2]]),
         ('o3e6', [[59.2, 50.2], [59.2, 54.4]]),
         ('o3e7', [[59.2, 50.2], [63.4, 50.2]]),
         ('o3e8', [[59.2, 54.4], [59.2, 58.6]]),
         ('o3e9', [[59.2, 54.4], [63.4, 54.4]]),
         ('o3e10', [[59.2, 58.6], [63.4, 58.6]]),
         ('o3e11', [[63.4, 50.2], [63.4, 54.4]]),
         ('o3e12', [[63.4, 50.2], [67.6, 50.2]]),
         ('o3e13', [[63.4, 54.4], [63.4, 58.6]]),
         ('o3e14', [[63.4, 54.4], [67.6, 54.4]]),
         ('o3e15', [[67.6, 50.2], [67.6, 54.4]]),
         ('o3e16', [[67.6, 50.2], [71.8, 50.2]]),
         ('o3e17', [[67.6, 54.4], [71.8, 54.4]]),
         ('o3e18', [[71.8, 50.2], [71.8, 54.4]]),
         ('o4e0', [[31.0, 18.0], [31.0, 22.2]]),
         ('o4e1', [[31.0, 18.0], [35.2, 18.0]]),
         ('o4e2', [[31.0, 22.2], [31.0, 26.4]]),
         ('o4e3', [[31.0, 22.2], [35.2, 22.2]]),
         ('o4e4', [[31.0, 26.4], [35.2, 26.4]]),
         ('o4e5', [[35.2, 18.0], [35.2, 22.2]]),
         ('o4e6', [[35.2, 22.2], [35.2, 26.4]]),
         ('o4e7', [[35.2, 22.2], [39.4, 22.2]]),
         ('o4e8', [[35.2, 26.4], [39.4, 26.4]]),
         ('o4e9', [[39.4, 22.2], [39.4, 26.4]]),
         ('o4e10', [[39.4, 22.2], [43.6, 22.2]]),
         ('o4e11', [[39.4, 26.4], [39.4, 30.6]]),
         ('o4e12', [[39.4, 26.4], [43.6, 26.4]]),
         ('o4e13', [[39.4, 30.6], [43.6, 30.6]]),
         ('o4e14', [[43.6, 22.2], [43.6, 26.4]]),
         ('o4e15', [[43.6, 22.2], [47.8, 22.2]]),
         ('o4e16', [[43.6, 26.4], [43.6, 30.6]]),
         ('o4e17', [[43.6, 26.4], [47.8, 26.4]]),
         ('o4e18', [[47.8, 22.2], [47.8, 26.4]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid251.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[0.0, 100.0], ylim=[0.0, 100.0], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, solid_capstyle='butt')
            for object_id, text, anchor in [(None, 'A', [5, 87]), (None, 'B', [52, 87]), (None, 'C', [5, 59]), (None, 'D', [52, 59]), (None, 'E', [28, 31])]:
                c.text(text, anchor, id=object_id, zorder=3, fontsize=18.0, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid251().draw(sys.argv[1] if len(sys.argv) > 1 else None))
