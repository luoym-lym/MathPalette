"""Frozen question Solid205; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid205:

    def __init__(self):
        self.id = 'Solid205'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2021'
        self.question = 'Two identical cylindrical sheets are cut open along the dotted lines and glued together to form one bigger cylindrical sheet, as shown. The smaller sheets each enclose a volume of 100. What volume is enclosed by the larger cylindrical sheet?'
        self.answer = '400'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'0b': [0, 0, 0],
         '0t': [0, 0, 2.5],
         '0l': [-1, 0, 0],
         '0L': [-1, 0, 2.5],
         '0r': [1, 0, 0],
         '0R': [1, 0, 2.5],
         '0s0': [-0.34202014332566855, -0.9396926207859084, 0],
         '0S0': [-0.34202014332566855, -0.9396926207859084, 2.5],
         '1b': [3.7, 0, 0],
         '1t': [3.7, 0, 2.5],
         '1l': [2.7, 0, 0],
         '1L': [2.7, 0, 2.5],
         '1r': [4.7, 0, 0],
         '1R': [4.7, 0, 2.5],
         '1s0': [3.3579798566743317, -0.9396926207859084, 0],
         '1S0': [3.3579798566743317, -0.9396926207859084, 2.5],
         '2b': [9.2, 0, 0],
         '2t': [9.2, 0, 2.5],
         '2l': [7.199999999999999, 0, 0],
         '2L': [7.199999999999999, 0, 2.5],
         '2r': [11.2, 0, 0],
         '2R': [11.2, 0, 2.5],
         '2s0': [8.3547634765186, -1.8126155740733, 0],
         '2S0': [8.3547634765186, -1.8126155740733, 2.5],
         '2s1': [10.045236523481398, 1.8126155740732999, 0],
         '2S1': [10.045236523481398, 1.8126155740732999, 2.5],
         'andlabel': [1.85, 0, 1.25],
         'arrow0': [5.15, 0, 1.25],
         'arrow1': [6.65, 0, 1.25],
         'arrowtip1': [6.4, 0, 1.36],
         'arrowtip2': [6.4, 0, 1.14]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid205.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.3045189415185696, 11.529187923562244], ylim=[-5.166853432540407, 7.666853432540407], projection=[[1, 0, 0], [0, 0.35, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['0t']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_0')
            t = np.radians(np.linspace(0, 180, 721))
            xyz = np.asarray(self.points['0b']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_1')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['0b']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_2', c.project(xyz)), ('line_3', c.project([self.points['0l'], self.points['0L']])), ('line_4', c.project([self.points['0r'], self.points['0R']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['0s0'], self.points['0S0']]), id='line_5', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['1t']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_6')
            t = np.radians(np.linspace(0, 180, 721))
            xyz = np.asarray(self.points['1b']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_7')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['1b']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_8', c.project(xyz)), ('line_9', c.project([self.points['1l'], self.points['1L']])), ('line_10', c.project([self.points['1r'], self.points['1R']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['1s0'], self.points['1S0']]), id='line_11', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['2t']) + 2 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_12')
            t = np.radians(np.linspace(0, 180, 721))
            xyz = np.asarray(self.points['2b']) + 2 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_13')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['2b']) + 2 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_14', c.project(xyz)), ('line_15', c.project([self.points['2l'], self.points['2L']])), ('line_16', c.project([self.points['2r'], self.points['2R']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['2s0'], self.points['2S0']]), id='line_17', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['2s1'], self.points['2S1']]), id='line_18', linestyle=(0, [4, 3]), clip_on=False)
            for object_id, points in [('line_19', c.project([self.points['arrow0'], self.points['arrow1']])), ('line_20', c.project([self.points['arrowtip1'], self.points['arrow1']])), ('line_21', c.project([self.points['arrowtip2'], self.points['arrow1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('and', c.project(self.points['andlabel']), offset_pt=[0, 0], vertex=False, id='label_0')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid205().draw(sys.argv[1] if len(sys.argv) > 1 else None))
