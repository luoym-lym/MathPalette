"""Frozen question Plane57; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane57:

    def __init__(self):
        self.id = 'Plane57'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/744'
        self.question = 'If RL = 5, RT = 9, and WS = 6, find RW.\nChoices:\nA: 5.4\nB: 6\nC: 6.6\nD: 7.5'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '5.4', 'B': '6', 'C': '6.6', 'D': '7.5'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane57.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.9045890944270978, 14.434807884170919], ylim=[-4.739529265581494, 10.599867713016524], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('segment6', [[0.0, 0.0], [6.894399988070802, 5.785088487178854]]), ('segment7', [[6.894399988070802, 5.785088487178854], [13.5, 0.0]]), ('segment8', [[13.5, 0.0], [0.0, 0.0]]), ('segment9', [[3.83022221559489, 3.2139380484326963], [7.5, 0.0]])]:
                c.line(points, id=object_id)
            for object_id, points in [('parallel_mark10', [[10.132030707268294, 3.0520493111855345], [10.197199994035401, 2.892544243589427]]), ('parallel_mark10', [[10.030494367898251, 2.936111854733406], [10.197199994035401, 2.892544243589427]]), ('parallel_mark11', [[5.599941821030339, 1.766474091812456], [5.665111107797445, 1.6069690242163481]]), ('parallel_mark11', [[5.498405481660295, 1.6505366353603277], [5.665111107797445, 1.6069690242163481]])]:
                c.line(points, id=object_id, zorder=3)
            c.text('R', [0.0, 0.0], id='label1', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-12, -10], annotation_clip=None)
            c.text('T', [6.894399988070802, 5.785088487178854], id='label2', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, 14], annotation_clip=None)
            c.text('L', [3.83022221559489, 3.2139380484326963], id='label3', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[-14, 7], annotation_clip=None)
            c.text('S', [13.5, 0.0], id='label4', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[14, -6], annotation_clip=None)
            c.text('W', [7.5, 0.0], id='label5', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -15], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane57().draw(sys.argv[1] if len(sys.argv) > 1 else None))
