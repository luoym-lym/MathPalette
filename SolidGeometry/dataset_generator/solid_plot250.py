"""Frozen question Solid250; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid250:

    def __init__(self):
        self.id = 'Solid250'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid254'
        self.question = 'Each diagram is a flat sheet consisting of four identical squares in a row and four triangular flaps. The dashed lines are hinges; fold each hinge through 90 degrees toward the same side of the sheet. The triangular flaps must together cover the remaining two square faces exactly, without overlap. Which diagram CANNOT form a closed cube?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid250.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[0.0, 100.0], ylim=[0.0, 100.0], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[8.0, 74.0], [8.0, 78.2]], id='o0e0', solid_capstyle='butt')
            c.line([[8.0, 74.0], [12.2, 74.0]], id='o0e1', solid_capstyle='butt')
            c.line([[8.0, 78.2], [12.2, 78.2]], id='o0e2', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o0e3', [[8.0, 78.2], [12.2, 82.4]]), ('o0e4', [[12.2, 69.8], [12.2, 74.0]]), ('o0e5', [[12.2, 69.8], [16.4, 74.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[12.2, 74.0], [12.2, 78.2]], id='o0e6', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[12.2, 74.0], [16.4, 74.0]], id='o0e7', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[12.2, 78.2], [12.2, 82.4]], id='o0e8', solid_capstyle='butt')
            c.line([[12.2, 78.2], [16.4, 78.2]], id='o0e9', solid_capstyle='butt')
            c.line([[16.4, 74.0], [16.4, 78.2]], id='o0e10', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[16.4, 74.0], [20.6, 74.0]], id='o0e11', solid_capstyle='butt')
            c.line([[16.4, 78.2], [16.4, 82.4]], id='o0e12', solid_capstyle='butt')
            c.line([[16.4, 78.2], [20.6, 78.2]], id='o0e13', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o0e14', [[16.4, 82.4], [20.6, 78.2]]), ('o0e15', [[20.6, 69.8], [20.6, 74.0]]), ('o0e16', [[20.6, 69.8], [24.8, 74.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[20.6, 74.0], [20.6, 78.2]], id='o0e17', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[20.6, 74.0], [24.8, 74.0]], id='o0e18', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o0e19', [[20.6, 78.2], [24.8, 78.2]]), ('o0e20', [[24.8, 74.0], [24.8, 78.2]]), ('o1e0', [[55.0, 74.0], [55.0, 78.2]]), ('o1e1', [[55.0, 74.0], [59.2, 69.8]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[55.0, 74.0], [59.2, 74.0]], id='o1e2', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[55.0, 78.2], [59.2, 78.2]], id='o1e3', solid_capstyle='butt')
            c.line([[59.2, 69.8], [59.2, 74.0]], id='o1e4', solid_capstyle='butt')
            c.line([[59.2, 74.0], [59.2, 78.2]], id='o1e5', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[59.2, 74.0], [63.4, 74.0]], id='o1e6', solid_capstyle='butt')
            c.line([[59.2, 78.2], [59.2, 82.4]], id='o1e7', solid_capstyle='butt')
            c.line([[59.2, 78.2], [63.4, 78.2]], id='o1e8', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[59.2, 82.4], [63.4, 78.2]], id='o1e9', solid_capstyle='butt')
            c.line([[63.4, 74.0], [63.4, 78.2]], id='o1e10', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o1e11', [[63.4, 74.0], [67.6, 74.0]]), ('o1e12', [[63.4, 78.2], [67.6, 78.2]]), ('o1e13', [[67.6, 69.8], [67.6, 74.0]]), ('o1e14', [[67.6, 69.8], [71.8, 74.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[67.6, 74.0], [67.6, 78.2]], id='o1e15', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[67.6, 74.0], [71.8, 74.0]], id='o1e16', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[67.6, 78.2], [67.6, 82.4]], id='o1e17', solid_capstyle='butt')
            c.line([[67.6, 78.2], [71.8, 78.2]], id='o1e18', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o1e19', [[67.6, 82.4], [71.8, 78.2]]), ('o1e20', [[71.8, 74.0], [71.8, 78.2]]), ('o2e0', [[8.0, 46.0], [8.0, 50.2]]), ('o2e1', [[8.0, 46.0], [12.2, 41.8]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[8.0, 46.0], [12.2, 46.0]], id='o2e2', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[8.0, 50.2], [12.2, 50.2]], id='o2e3', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[8.0, 50.2], [12.2, 54.4]], id='o2e4', solid_capstyle='butt')
            c.line([[12.2, 41.8], [12.2, 46.0]], id='o2e5', solid_capstyle='butt')
            c.line([[12.2, 46.0], [12.2, 50.2]], id='o2e6', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o2e7', [[12.2, 46.0], [16.4, 46.0]]), ('o2e8', [[12.2, 50.2], [12.2, 54.4]]), ('o2e9', [[12.2, 50.2], [16.4, 50.2]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[16.4, 46.0], [16.4, 50.2]], id='o2e10', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[16.4, 46.0], [20.6, 46.0]], id='o2e11', solid_capstyle='butt')
            c.line([[16.4, 50.2], [20.6, 50.2]], id='o2e12', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o2e13', [[16.4, 50.2], [20.6, 54.4]]), ('o2e14', [[20.6, 41.8], [20.6, 46.0]]), ('o2e15', [[20.6, 41.8], [24.8, 46.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[20.6, 46.0], [20.6, 50.2]], id='o2e16', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[20.6, 46.0], [24.8, 46.0]], id='o2e17', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o2e18', [[20.6, 50.2], [20.6, 54.4]]), ('o2e19', [[20.6, 50.2], [24.8, 50.2]]), ('o2e20', [[24.8, 46.0], [24.8, 50.2]]), ('o3e0', [[55.0, 46.0], [55.0, 50.2]]), ('o3e1', [[55.0, 46.0], [59.2, 46.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[55.0, 50.2], [59.2, 50.2]], id='o3e2', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o3e3', [[55.0, 50.2], [59.2, 54.4]]), ('o3e4', [[59.2, 41.8], [59.2, 46.0]]), ('o3e5', [[59.2, 41.8], [63.4, 46.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[59.2, 46.0], [59.2, 50.2]], id='o3e6', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[59.2, 46.0], [63.4, 46.0]], id='o3e7', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[59.2, 50.2], [59.2, 54.4]], id='o3e8', solid_capstyle='butt')
            c.line([[59.2, 50.2], [63.4, 50.2]], id='o3e9', solid_capstyle='butt')
            c.line([[63.4, 46.0], [63.4, 50.2]], id='o3e10', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[63.4, 46.0], [67.6, 46.0]], id='o3e11', solid_capstyle='butt')
            c.line([[63.4, 50.2], [67.6, 50.2]], id='o3e12', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o3e13', [[63.4, 50.2], [67.6, 54.4]]), ('o3e14', [[67.6, 41.8], [67.6, 46.0]]), ('o3e15', [[67.6, 41.8], [71.8, 46.0]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[67.6, 46.0], [67.6, 50.2]], id='o3e16', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[67.6, 46.0], [71.8, 46.0]], id='o3e17', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            for object_id, points in [('o3e18', [[67.6, 50.2], [67.6, 54.4]]), ('o3e19', [[67.6, 50.2], [71.8, 50.2]]), ('o3e20', [[71.8, 46.0], [71.8, 50.2]]), ('o4e0', [[31.0, 18.0], [31.0, 22.2]]), ('o4e1', [[31.0, 18.0], [35.2, 13.8]])]:
                c.line(points, id=object_id, solid_capstyle='butt')
            c.line([[31.0, 18.0], [35.2, 18.0]], id='o4e2', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[31.0, 22.2], [35.2, 22.2]], id='o4e3', solid_capstyle='butt')
            c.line([[35.2, 13.8], [35.2, 18.0]], id='o4e4', solid_capstyle='butt')
            c.line([[35.2, 18.0], [35.2, 22.2]], id='o4e5', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[35.2, 18.0], [39.4, 18.0]], id='o4e6', solid_capstyle='butt')
            c.line([[35.2, 22.2], [35.2, 26.4]], id='o4e7', solid_capstyle='butt')
            c.line([[35.2, 22.2], [39.4, 22.2]], id='o4e8', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[35.2, 26.4], [39.4, 22.2]], id='o4e9', solid_capstyle='butt')
            c.line([[39.4, 18.0], [39.4, 22.2]], id='o4e10', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[39.4, 18.0], [43.6, 13.8]], id='o4e11', solid_capstyle='butt')
            c.line([[39.4, 18.0], [43.6, 18.0]], id='o4e12', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[39.4, 22.2], [43.6, 22.2]], id='o4e13', solid_capstyle='butt')
            c.line([[43.6, 13.8], [43.6, 18.0]], id='o4e14', solid_capstyle='butt')
            c.line([[43.6, 18.0], [43.6, 22.2]], id='o4e15', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[43.6, 18.0], [47.8, 18.0]], id='o4e16', solid_capstyle='butt')
            c.line([[43.6, 22.2], [43.6, 26.4]], id='o4e17', solid_capstyle='butt')
            c.line([[43.6, 22.2], [47.8, 22.2]], id='o4e18', linestyle=(0.0, [4.0, 3.0]), solid_capstyle='butt')
            c.line([[43.6, 26.4], [47.8, 22.2]], id='o4e19', solid_capstyle='butt')
            c.line([[47.8, 18.0], [47.8, 22.2]], id='o4e20', solid_capstyle='butt')
            for object_id, text, anchor in [(None, 'A', [5, 87]), (None, 'B', [52, 87]), (None, 'C', [5, 59]), (None, 'D', [52, 59]), (None, 'E', [28, 31])]:
                c.text(text, anchor, id=object_id, zorder=3, fontsize=18.0, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid250().draw(sys.argv[1] if len(sys.argv) > 1 else None))
