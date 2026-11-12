"""Frozen question Solid21; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid21:

    def __init__(self):
        self.id = 'Solid21'
        self.source_dataset = 'SOLIDGEO'
        self.source_key = '1932'
        self.question = 'A cubic object slides down a slope, and its cross-section is shown in the figure. Square $DEFH$ has side length 2 meters, the slope angle is $\\angle A = 30^\\circ$, $\\angle B = 90^\\circ$, and $BC = 6$ meters. Find $AE$, in meters, when $DC^2 = AE^2 + BC^2$. (Hint: Connect $DC$.)'
        self.answer = '14/3 m'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'o1_world_0': [0.0, 0.0, 0.0],
         'o1_world_1': [10.392304845413264, 0.0, 0.0],
         'o1_world_2': [10.392304845413264, 6.0, 0.0],
         'o1_world_3': [0.0, 0.0, 0.0],
         'o2_world_0': [2.8971143170299736, 3.982050807568877, 0.0],
         'o2_world_1': [3.8971143170299736, 2.25, 0.0],
         'o2_world_2': [5.629165124598851, 3.25, 0.0],
         'o2_world_3': [4.629165124598851, 4.982050807568877, 0.0],
         'o2_world_4': [2.8971143170299736, 3.982050807568877, 0.0],
         'o10_world_0': [3.0274990747593105, 2.556217782649107, 0.0],
         'o10_world_1': [1.2954482671904333, 1.556217782649107, 0.0],
         'o11_world_0': [1.2954482671904333, 1.556217782649107, 0.0],
         'o11_world_1': [1.4419546181365428, 1.8024613391789284, 0.0],
         'o12_world_0': [1.2954482671904333, 1.556217782649107, 0.0],
         'o12_world_1': [1.581954618136543, 1.5599742261192857, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid21.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.720883096449703, 11.028991027606146], ylim=[-2.818538081278315, 8.931336042777534], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('o1', c.project([self.points['o1_world_0'], self.points['o1_world_1'], self.points['o1_world_2'], self.points['o1_world_3']])), ('o2', c.project([self.points['o2_world_0'], self.points['o2_world_1'], self.points['o2_world_2'], self.points['o2_world_3'], self.points['o2_world_4']])), ('o10', c.project([self.points['o10_world_0'], self.points['o10_world_1']])), ('o11', c.project([self.points['o11_world_0'], self.points['o11_world_1']])), ('o12', c.project([self.points['o12_world_0'], self.points['o12_world_1']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project([0.0, 0.0, 0.0]), offset_pt=[-12, -12], vertex=True, id='l3')
            c.text('B', c.project([10.392304845413264, 0.0, 0.0]), offset_pt=[10, -12], vertex=True, id='l4')
            c.text('C', c.project([10.392304845413264, 6.0, 0.0]), offset_pt=[8, 14], vertex=True, id='l5')
            c.text('D', c.project([2.8971143170299736, 3.982050807568877, 0.0]), offset_pt=[-16, 6], vertex=True, id='l6')
            c.text('E', c.project([3.8971143170299736, 2.25, 0.0]), offset_pt=[0, -15], vertex=True, id='l7')
            c.text('F', c.project([5.629165124598851, 3.25, 0.0]), offset_pt=[10, -12], vertex=True, id='l8')
            c.text('H', c.project([4.629165124598851, 4.982050807568877, 0.0]), offset_pt=[0, 15], vertex=True, id='l9')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid21().draw(sys.argv[1] if len(sys.argv) > 1 else None))
