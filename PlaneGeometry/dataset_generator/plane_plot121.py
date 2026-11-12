"""Frozen question Plane121; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane121:

    def __init__(self):
        self.id = 'Plane121'
        self.source_dataset = 'Author Designed'
        self.source_key = 'structure-count:rectangle-line-regions'
        self.question = 'How many regions is the interior of the rectangle divided into by the three straight segments?'
        self.answer = 7
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'BL': [-4.0, -3.0],
         'BR': [4.0, -3.0],
         'TR': [4.0, 3.0],
         'TL': [-4.0, 3.0],
         'H_L': [-4.0, 2.2],
         'H_R': [4.0, 2.2],
         'A_start': [-4.0, -2.3],
         'A_end': [3.0666666666666664, 3.0],
         'D_start': [-3.125, 3.0],
         'D_end': [4.0, -2.7],
         'I_HA': [2.0, 2.2],
         'I_HD': [-2.125, 2.2],
         'I_AD': [-0.12903225806451613, 0.603225806451613]}
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane121.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.204565030146426, 4.219611326442722], ylim=[-4.219611326442722, 4.204565030146426]) as c:
            for object_id, points in [('frame_bottom', [self.points['BL'], self.points['BR']]), ('frame_right', [self.points['BR'], self.points['TR']]), ('frame_top', [self.points['TR'], self.points['TL']]), ('frame_left', [self.points['TL'], self.points['BL']]), ('cut_horizontal', [self.points['H_L'], self.points['H_R']]), ('cut_ascending', [self.points['A_start'], self.points['A_end']]), ('cut_descending', [self.points['D_start'], self.points['D_end']])]:
                c.line(points, id=object_id)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane121().draw(sys.argv[1] if len(sys.argv) > 1 else None))
