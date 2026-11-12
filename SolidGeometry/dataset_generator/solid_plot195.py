"""Frozen question Solid195; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid195:

    def __init__(self):
        self.id = 'Solid195'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1855'
        self.question = 'Three circular hoops are joined together so that they intersect at rightangles as shown. A path starts at an intersection and follows the outside of the hoops by repeating this procedure: travel along a quarter-circle, turn $90^{\\circ}$ to the right, travel along a quarter-circle and turn $90^{\\circ}$ to the left. How many quarter-circles does the path traverse before first returning to its starting point?'
        self.answer = '6'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid195.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.0321944190087855, 1.0321957562126474], ylim=[-1.032193501975734, 1.0321966732456989], projection=[[0.8048180192965595, 0.5623095011990213, 0.1899367807373569], [-0.3789810417695135, 0.24059103781466168, 0.8935822975543766]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0.0, 69.35642709904208, 140))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop0arc0')
            t = np.radians(np.linspace(72.22121607469619, 139.69028557829014, 136))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop0arc1')
            t = np.radians(np.linspace(142.55507455394425, 360.0, 436))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop0arc2')
            t = np.radians(np.linspace(0.0, 19.939108185297634, 41))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([0.0, 1.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop1arc3')
            t = np.radians(np.linspace(22.803897160951752, 314.6825678821456, 585))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([0.0, 1.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop1arc4')
            t = np.radians(np.linspace(317.54735685779974, 360.0, 86))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([0.0, 1.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop1arc5')
            t = np.radians(np.linspace(0.0, 207.61129352931815, 417))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop2arc6')
            t = np.radians(np.linspace(210.47608250497225, 236.04379601731353, 53))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop2arc7')
            t = np.radians(np.linspace(238.9085849929677, 360.0, 244))
            xyz = np.asarray([0, 0, 0]) + 1 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.0, 1.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='hoop2arc8')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid195().draw(sys.argv[1] if len(sys.argv) > 1 else None))
