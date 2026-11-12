"""Frozen question Plane11; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane11:

    def __init__(self):
        self.id = 'Plane11'
        self.source_dataset = 'MathVerse'
        self.source_key = 's1859'
        self.question = '\\[Consider the adjacent figure:\n\nSolve for the unknown \\theta . Leave your answer in degrees.\\]'
        self.answer = '\\[60^\\circ \\]'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane11.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-5.242030737121753, 8.828332625721753], ylim=[-2.7925409943217536, 11.277822368521754], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('VA', [[0.0, 0.0], [-4.8989794856, 4.8989794856]]), ('VC', [[0.0, 0.0], [8.4852813742, 8.4852813742]]), ('AC', [[-4.8989794856, 4.8989794856], [8.4852813742, 8.4852813742]])]:
                c.line(points, id=object_id)
            c.line([[-0.17992710770445244, 0.17992710770445244], [-2.7755575615628914e-17, 0.35985421540890483]], id='rightV', zorder=3)
            c.line([[-2.7755575615628914e-17, 0.35985421540890483], [0.17992710770445242, 0.17992710770445242]], id='rightV', zorder=3)
            c.path([[-4.579109071903195, 4.579109071903195], [-4.522964266922061, 4.63525387688433], [-4.482578799485225, 4.70520355837215], [-4.462028374571417, 4.781898788266852], [-4.4414779496576084, 4.858594018161554], [-4.441477949657309, 4.939364953035055], [-4.462028374570549, 5.016060182929909]], [1, 4, 4, 4, 4, 4, 4], id='angle_arc_theta', zorder=3, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.text('8√3', [1.7931509442999998, 6.6921304299], id='given_hyp', rotation_mode='default', offset_pt=[-5.333333333333333, 13.333333333333332], annotation_clip=None)
            c.text('12', [4.2426406871, 4.2426406871], id='leg12', rotation_mode='default', offset_pt=[22, -18], annotation_clip=None)
            c.text('θ', [-4.8989794856, 4.8989794856], id='theta', rotation_mode='default', offset_pt=[38.637033051537145, -10.352761804196302], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane11().draw(sys.argv[1] if len(sys.argv) > 1 else None))
