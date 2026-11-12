"""Frozen question Plane08; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane08:

    def __init__(self):
        self.id = 'Plane08'
        self.source_dataset = 'MathVerse'
        self.source_key = 's1189'
        self.question = '\\[Find x.\nChoices:\nA:4\nB:4 \\sqrt { 2 }\nC:4 \\sqrt { 3 }\nD:8\\]'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '4', 'B': '4 \\sqrt { 2 }', 'C': '4 \\sqrt { 3 }', 'D': '8'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane08.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.39529916754120364, 15.852630865304853], ylim=[-10.177872832177307, 6.070057200668749], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('AB', [[0.0, 0.0], [5.656854249492381, -5.656854249492381]]), ('BC', [[5.656854249492381, -5.656854249492381], [15.454813220625095, 0.0]]), ('AC', [[0.0, 0.0], [15.454813220625095, 0.0]]), ('BF', [[5.656854249492381, -5.656854249492381], [5.656854249492381, 0.0]])]:
                c.line(points, id=object_id)
            c.line([[5.656854249492381, -0.29383554023520786], [5.950689789727589, -0.29383554023520786]], id='right_F', zorder=3)
            c.line([[5.950689789727589, -0.29383554023520786], [5.950689789727589, 0.0]], id='right_F', zorder=3)
            c.path([[0.3693744054292054, -0.3693744054292056], [0.41788020792161207, -0.32086860293679886], [0.4563597671636791, -0.26327987283029336], [0.48261091830703134, -0.19990398771210657], [0.5088620694503836, -0.1365281025939198], [0.5223742937514806, -0.06859756373855236], [0.5223742937514806, -1.2794480135992199e-16]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_angle_A', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[14.932438926873614, 6.397240067996099e-17], [14.932438926873614, -0.045650749960179725], [14.938423115788119, -0.09110517751885959], [14.950238399301027, -0.1352004158948619], [14.962053682813934, -0.17929565427086422], [14.979598436972267, -0.2216524377084132], [15.002423811952358, -0.26118714687574035]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_angle_C', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.line([[5.656854249492381, 1.0], [15.454813220625095, 1.0]], id='distance_y_range', linestyle=(0, [4, 3]))
            c.line([[5.656854249492381, 0.0], [5.656854249492381, 1.0]], id='distance_y_start')
            c.line([[15.454813220625095, 0.0], [15.454813220625095, 1.0]], id='distance_y_end')
            c.text('8', [2.8284271247461903, -2.8284271247461903], id='AB8', rotation_mode='default', offset_pt=[-16, -6], annotation_clip=None)
            c.text('45°', [0.0, 0.0], id='angle_A', rotation_mode='default', offset_pt=[38.49820945814589, -10.857617994602972], annotation_clip=None)
            c.text('30°', [15.454813220625095, 0.0], id='angle_C', rotation_mode='default', offset_pt=[-55.06227482358146, -10.205189427560258], annotation_clip=None)
            c.text('x', [5.656854249492381, -2.8284271247461903], id='x', rotation_mode='default', offset_pt=[16, 0], annotation_clip=None)
            c.text('y', [10.555833735058737, 1.0], id='y', rotation_mode='default', offset_pt=[0, 14], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane08().draw(sys.argv[1] if len(sys.argv) > 1 else None))
