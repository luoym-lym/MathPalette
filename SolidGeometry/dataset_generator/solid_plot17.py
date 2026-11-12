"""Frozen question Solid17; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid17:

    def __init__(self):
        self.id = 'Solid17'
        self.source_dataset = 'SOLIDGEO'
        self.source_key = '1766'
        self.question = 'As shown in the figure, a rectangular piece of cardboard is $3 \\mathrm{cm}$ long and $2 \\mathrm{cm}$ wide. Find the volume of the solid obtained by rotating it as shown.'
        self.answer = '12π cm³'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'o1_world_0': [0.0, 0.0, 0.0],
         'o1_world_1': [2.0, 0.0, 0.0],
         'o1_world_2': [2.0, 3.0, 0.0],
         'o1_world_3': [0.0, 3.0, 0.0],
         'o1_world_4': [0.0, 0.0, 0.0],
         'o2_world_0': [2.0, -0.4, 0.0],
         'o2_world_1': [2.0, 3.5, 0.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid17.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.2482531705462139, 2.819019688956568], ylim=[-0.498697924349806, 3.568574935152976], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            c.line(c.project([self.points['o1_world_0'], self.points['o1_world_1'], self.points['o1_world_2'], self.points['o1_world_3'], self.points['o1_world_4']]), id='o1', clip_on=False, zorder=3)
            c.line(c.project([self.points['o2_world_0'], self.points['o2_world_1']]), id='o2', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.text('3 cm', c.project([0.0, 1.5, 0.0]), offset_pt=[-35, 0], vertex=False, id='l3')
            c.text('2 cm', c.project([1.0, 0.0, 0.0]), offset_pt=[0, -20], vertex=False, id='l4')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid17().draw(sys.argv[1] if len(sys.argv) > 1 else None))
