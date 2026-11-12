"""Frozen question Plane192; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane192:

    def __init__(self):
        self.id = 'Plane192'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:432'
        self.question = 'Between two points four routes are drawn. Which route is the shortest?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane192.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-1.6000767144941612, 47.19429423056246], ylim=[-22.44356816034315, 26.350802784713476], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('grid0v0', [[0.0, 0.0], [0.0, 6.0]]), ('grid0v1', [[1.0, 0.0], [1.0, 6.0]]), ('grid0v2', [[2.0, 0.0], [2.0, 6.0]]), ('grid0v3', [[3.0, 0.0], [3.0, 6.0]]), ('grid0v4', [[4.0, 0.0], [4.0, 6.0]]), ('grid0v5', [[5.0, 0.0], [5.0, 6.0]]), ('grid0v6', [[6.0, 0.0], [6.0, 6.0]]), ('grid0v7', [[7.0, 0.0], [7.0, 6.0]]), ('grid0v8', [[8.0, 0.0], [8.0, 6.0]]), ('grid0v9', [[9.0, 0.0], [9.0, 6.0]]), ('grid0v10', [[10.0, 0.0], [10.0, 6.0]]), ('grid0h0', [[0.0, 0.0], [10.0, 0.0]]), ('grid0h1', [[0.0, 1.0], [10.0, 1.0]]), ('grid0h2', [[0.0, 2.0], [10.0, 2.0]]), ('grid0h3', [[0.0, 3.0], [10.0, 3.0]]), ('grid0h4', [[0.0, 4.0], [10.0, 4.0]]), ('grid0h5', [[0.0, 5.0], [10.0, 5.0]]), ('grid0h6', [[0.0, 6.0], [10.0, 6.0]])]:
                c.line(points, id=object_id, color='#AAAAAA')
            c.line([[1.0, 1.0], [5.0, 5.0]], id='route0_0')
            c.line([[5.0, 5.0], [9.0, 1.0]], id='route0_1')
            c.point([[1.0, 1.0]], id='dot0_0')
            c.point([[9.0, 1.0]], id='dot0_1')
            for object_id, points in [('grid1v0', [[12.0, 0.0], [12.0, 6.0]]), ('grid1v1', [[13.0, 0.0], [13.0, 6.0]]), ('grid1v2', [[14.0, 0.0], [14.0, 6.0]]), ('grid1v3', [[15.0, 0.0], [15.0, 6.0]]), ('grid1v4', [[16.0, 0.0], [16.0, 6.0]]), ('grid1v5', [[17.0, 0.0], [17.0, 6.0]]), ('grid1v6', [[18.0, 0.0], [18.0, 6.0]]), ('grid1v7', [[19.0, 0.0], [19.0, 6.0]]), ('grid1v8', [[20.0, 0.0], [20.0, 6.0]]), ('grid1v9', [[21.0, 0.0], [21.0, 6.0]]), ('grid1v10', [[22.0, 0.0], [22.0, 6.0]]), ('grid1h0', [[12.0, 0.0], [22.0, 0.0]]), ('grid1h1', [[12.0, 1.0], [22.0, 1.0]]), ('grid1h2', [[12.0, 2.0], [22.0, 2.0]]), ('grid1h3', [[12.0, 3.0], [22.0, 3.0]]), ('grid1h4', [[12.0, 4.0], [22.0, 4.0]]), ('grid1h5', [[12.0, 5.0], [22.0, 5.0]]), ('grid1h6', [[12.0, 6.0], [22.0, 6.0]])]:
                c.line(points, id=object_id, color='#AAAAAA')
            for object_id, points in [('route1_0', [[13.0, 1.0], [16.0, 4.0]]), ('route1_1', [[16.0, 4.0], [17.0, 3.0]]), ('route1_2', [[17.0, 3.0], [18.0, 4.0]]), ('route1_3', [[18.0, 4.0], [21.0, 1.0]])]:
                c.line(points, id=object_id)
            c.point([[13.0, 1.0]], id='dot1_0')
            c.point([[21.0, 1.0]], id='dot1_1')
            for object_id, points in [('grid2v0', [[24.0, 0.0], [24.0, 6.0]]), ('grid2v1', [[25.0, 0.0], [25.0, 6.0]]), ('grid2v2', [[26.0, 0.0], [26.0, 6.0]]), ('grid2v3', [[27.0, 0.0], [27.0, 6.0]]), ('grid2v4', [[28.0, 0.0], [28.0, 6.0]]), ('grid2v5', [[29.0, 0.0], [29.0, 6.0]]), ('grid2v6', [[30.0, 0.0], [30.0, 6.0]]), ('grid2v7', [[31.0, 0.0], [31.0, 6.0]]), ('grid2v8', [[32.0, 0.0], [32.0, 6.0]]), ('grid2v9', [[33.0, 0.0], [33.0, 6.0]]), ('grid2v10', [[34.0, 0.0], [34.0, 6.0]]), ('grid2h0', [[24.0, 0.0], [34.0, 0.0]]), ('grid2h1', [[24.0, 1.0], [34.0, 1.0]]), ('grid2h2', [[24.0, 2.0], [34.0, 2.0]]), ('grid2h3', [[24.0, 3.0], [34.0, 3.0]]), ('grid2h4', [[24.0, 4.0], [34.0, 4.0]]), ('grid2h5', [[24.0, 5.0], [34.0, 5.0]]), ('grid2h6', [[24.0, 6.0], [34.0, 6.0]])]:
                c.line(points, id=object_id, color='#AAAAAA')
            for object_id, points in [('route2_0', [[25.0, 1.0], [27.0, 3.0]]), ('route2_1', [[27.0, 3.0], [29.0, 1.0]]), ('route2_2', [[29.0, 1.0], [31.0, 3.0]]), ('route2_3', [[31.0, 3.0], [33.0, 1.0]])]:
                c.line(points, id=object_id)
            c.point([[25.0, 1.0]], id='dot2_0')
            c.point([[33.0, 1.0]], id='dot2_1')
            for object_id, points in [('grid3v0', [[36.0, 0.0], [36.0, 6.0]]), ('grid3v1', [[37.0, 0.0], [37.0, 6.0]]), ('grid3v2', [[38.0, 0.0], [38.0, 6.0]]), ('grid3v3', [[39.0, 0.0], [39.0, 6.0]]), ('grid3v4', [[40.0, 0.0], [40.0, 6.0]]), ('grid3v5', [[41.0, 0.0], [41.0, 6.0]]), ('grid3v6', [[42.0, 0.0], [42.0, 6.0]]), ('grid3v7', [[43.0, 0.0], [43.0, 6.0]]), ('grid3v8', [[44.0, 0.0], [44.0, 6.0]]), ('grid3v9', [[45.0, 0.0], [45.0, 6.0]]), ('grid3v10', [[46.0, 0.0], [46.0, 6.0]]), ('grid3h0', [[36.0, 0.0], [46.0, 0.0]]), ('grid3h1', [[36.0, 1.0], [46.0, 1.0]]), ('grid3h2', [[36.0, 2.0], [46.0, 2.0]]), ('grid3h3', [[36.0, 3.0], [46.0, 3.0]]), ('grid3h4', [[36.0, 4.0], [46.0, 4.0]]), ('grid3h5', [[36.0, 5.0], [46.0, 5.0]]), ('grid3h6', [[36.0, 6.0], [46.0, 6.0]])]:
                c.line(points, id=object_id, color='#AAAAAA')
            for object_id, points in [('route3_0', [[37.0, 1.0], [38.0, 2.0]]), ('route3_1', [[38.0, 2.0], [39.0, 1.0]]), ('route3_2', [[39.0, 1.0], [40.0, 2.0]]), ('route3_3', [[40.0, 2.0], [41.0, 1.0]]), ('route3_4', [[41.0, 1.0], [42.0, 2.0]]), ('route3_5', [[42.0, 2.0], [43.0, 1.0]]), ('route3_6', [[43.0, 1.0], [44.0, 2.0]]), ('route3_7', [[44.0, 2.0], [45.0, 1.0]])]:
                c.line(points, id=object_id)
            c.point([[37.0, 1.0]], id='dot3_0')
            c.point([[45.0, 1.0]], id='dot3_1')
            for object_id, text, anchor in [('label0', 'A', [1.0, 5.2]), ('label1', 'B', [13.0, 5.2]), ('label2', 'C', [25.0, 5.2]), ('label3', 'D', [37.0, 5.2]), ('label4', 'E  All routes are equal', [8.0, -1.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane192().draw(sys.argv[1] if len(sys.argv) > 1 else None))
