"""Frozen question Plane250; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane250:

    def __init__(self):
        self.id = 'Plane250'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:718'
        self.question = 'The paths shown lie on a surface paved with identical rectangular tiles; their lengths are indicated.\nWhat is the length, in decimeters, of the path labelled Tin?'
        self.answer = '35'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane250.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-3.457108079393393, 139.55098360435306], ylim=[-72.28796435568137, 70.72012732806508], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('grid0v0', [[0.0, 0.0], [0.0, 9.0]]), ('grid0v1', [[4.0, 0.0], [4.0, 9.0]]), ('grid0v2', [[8.0, 0.0], [8.0, 9.0]]), ('grid0v3', [[12.0, 0.0], [12.0, 9.0]]), ('grid0v4', [[16.0, 0.0], [16.0, 9.0]]), ('grid0v5', [[20.0, 0.0], [20.0, 9.0]]), ('grid0v6', [[24.0, 0.0], [24.0, 9.0]]), ('grid0v7', [[28.0, 0.0], [28.0, 9.0]]), ('grid0h0', [[0.0, 0.0], [28.0, 0.0]]), ('grid0h1', [[0.0, 3.0], [28.0, 3.0]]), ('grid0h2', [[0.0, 6.0], [28.0, 6.0]]), ('grid0h3', [[0.0, 9.0], [28.0, 9.0]])]:
                c.line(points, id=object_id, color='#999999')
            for object_id, points in [('path0_0', [[4.0, 3.0], [8.0, 6.0]]), ('path0_1', [[8.0, 6.0], [12.0, 3.0]]), ('path0_2', [[12.0, 3.0], [16.0, 6.0]]), ('path0_3', [[16.0, 6.0], [20.0, 3.0]]), ('path0_4', [[20.0, 3.0], [24.0, 6.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('grid1v0', [[36.0, 0.0], [36.0, 9.0]]), ('grid1v1', [[40.0, 0.0], [40.0, 9.0]]), ('grid1v2', [[44.0, 0.0], [44.0, 9.0]]), ('grid1v3', [[48.0, 0.0], [48.0, 9.0]]), ('grid1v4', [[52.0, 0.0], [52.0, 9.0]]), ('grid1v5', [[56.0, 0.0], [56.0, 9.0]]), ('grid1v6', [[60.0, 0.0], [60.0, 9.0]]), ('grid1v7', [[64.0, 0.0], [64.0, 9.0]]), ('grid1h0', [[36.0, 0.0], [64.0, 0.0]]), ('grid1h1', [[36.0, 3.0], [64.0, 3.0]]), ('grid1h2', [[36.0, 6.0], [64.0, 6.0]]), ('grid1h3', [[36.0, 9.0], [64.0, 9.0]])]:
                c.line(points, id=object_id, color='#999999')
            for object_id, points in [('path1_0', [[40.0, 3.0], [44.0, 6.0]]), ('path1_1', [[44.0, 6.0], [44.0, 3.0]]), ('path1_2', [[44.0, 3.0], [48.0, 6.0]]), ('path1_3', [[48.0, 6.0], [48.0, 3.0]]), ('path1_4', [[48.0, 3.0], [52.0, 6.0]]), ('path1_5', [[52.0, 6.0], [52.0, 3.0]]), ('path1_6', [[52.0, 3.0], [56.0, 6.0]]), ('path1_7', [[56.0, 6.0], [56.0, 3.0]]), ('path1_8', [[56.0, 3.0], [60.0, 6.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('grid2v0', [[72.0, 0.0], [72.0, 9.0]]), ('grid2v1', [[76.0, 0.0], [76.0, 9.0]]), ('grid2v2', [[80.0, 0.0], [80.0, 9.0]]), ('grid2v3', [[84.0, 0.0], [84.0, 9.0]]), ('grid2v4', [[88.0, 0.0], [88.0, 9.0]]), ('grid2v5', [[92.0, 0.0], [92.0, 9.0]]), ('grid2v6', [[96.0, 0.0], [96.0, 9.0]]), ('grid2v7', [[100.0, 0.0], [100.0, 9.0]]), ('grid2h0', [[72.0, 0.0], [100.0, 0.0]]), ('grid2h1', [[72.0, 3.0], [100.0, 3.0]]), ('grid2h2', [[72.0, 6.0], [100.0, 6.0]]), ('grid2h3', [[72.0, 9.0], [100.0, 9.0]])]:
                c.line(points, id=object_id, color='#999999')
            for object_id, points in [('path2_0', [[76.0, 3.0], [76.0, 6.0]]), ('path2_1', [[76.0, 6.0], [80.0, 6.0]]), ('path2_2', [[80.0, 6.0], [80.0, 3.0]]), ('path2_3', [[80.0, 3.0], [84.0, 3.0]]), ('path2_4', [[84.0, 3.0], [84.0, 6.0]]), ('path2_5', [[84.0, 6.0], [88.0, 6.0]]), ('path2_6', [[88.0, 6.0], [88.0, 3.0]]), ('path2_7', [[88.0, 3.0], [92.0, 3.0]]), ('path2_8', [[92.0, 3.0], [92.0, 6.0]]), ('path2_9', [[92.0, 6.0], [96.0, 6.0]]), ('path2_10', [[96.0, 6.0], [96.0, 3.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('grid3v0', [[108.0, 0.0], [108.0, 9.0]]), ('grid3v1', [[112.0, 0.0], [112.0, 9.0]]), ('grid3v2', [[116.0, 0.0], [116.0, 9.0]]), ('grid3v3', [[120.0, 0.0], [120.0, 9.0]]), ('grid3v4', [[124.0, 0.0], [124.0, 9.0]]), ('grid3v5', [[128.0, 0.0], [128.0, 9.0]]), ('grid3v6', [[132.0, 0.0], [132.0, 9.0]]), ('grid3v7', [[136.0, 0.0], [136.0, 9.0]]), ('grid3h0', [[108.0, 0.0], [136.0, 0.0]]), ('grid3h1', [[108.0, 3.0], [136.0, 3.0]]), ('grid3h2', [[108.0, 6.0], [136.0, 6.0]]), ('grid3h3', [[108.0, 9.0], [136.0, 9.0]])]:
                c.line(points, id=object_id, color='#999999')
            for object_id, points in [('path3_0', [[112.0, 3.0], [116.0, 6.0]]), ('path3_1', [[116.0, 6.0], [116.0, 3.0]]), ('path3_2', [[116.0, 3.0], [120.0, 3.0]]), ('path3_3', [[120.0, 3.0], [120.0, 6.0]]), ('path3_4', [[120.0, 6.0], [124.0, 3.0]]), ('path3_5', [[124.0, 3.0], [124.0, 6.0]]), ('path3_6', [[124.0, 6.0], [128.0, 6.0]]), ('path3_7', [[128.0, 6.0], [128.0, 3.0]]), ('path3_8', [[128.0, 3.0], [132.0, 6.0]])]:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('label0', 'Fin hiked\n25 dm', [14.0, -7.0]), ('label1', 'Pin hiked\n37 dm', [50.0, -7.0]), ('label2', 'Rin hiked\n38 dm', [86.0, -7.0]), ('label3', 'Tin hiked\n? dm', [122.0, -7.0])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane250().draw(sys.argv[1] if len(sys.argv) > 1 else None))
