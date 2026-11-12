"""Frozen question Plane447; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane447:

    def __init__(self):
        self.id = 'Plane447'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2302'
        self.question = 'A rectangular piece of paper $6$ inches wide is folded as in the diagram so that one corner touches the opposite side. The length in inches of the crease $L$ in terms of angle $\\theta$ is\nChoices:\nA:$3\\sec ^2\\theta\\csc\\theta$\nB:$6\\sin\\theta\\sec\\theta$\nC:$3\\sec\\theta\\csc\\theta$\nD:$6\\sec\\theta\\csc ^2\\theta$\nE:$\\text{None of these}$'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': '$3\\sec ^2\\theta\\csc\\theta$',
         'B': '$6\\sin\\theta\\sec\\theta$',
         'C': '$3\\sec\\theta\\csc\\theta$',
         'D': '$6\\sec\\theta\\csc ^2\\theta$',
         'E': '$\\text{None of these}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane447.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(-1.0969837533590239, 7.107409039016953), ylim=(-1.074562266077856, 7.129830526298121), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('o0', [[0.0, 0.0], [0.0, 6.92820323027551]]), ('o1', [[0.0, 6.92820323027551], [6.0, 6.92820323027551]]), ('o2', [[0.0, 0.0], [2.0, 0.0]]), ('o3', [[0.0, 3.4641016151377544], [6.0, 6.92820323027551]]), ('o4', [[0.0, 3.4641016151377544], [2.0, 0.0]]), ('o5', [[2.0, 0.0], [6.0, 6.92820323027551]])]:
                c.line(points, id=object_id)
            c.line([[2.0, 0.0], [6.0, 0.0]], id='o6', linestyle=(0.0, [1.0, 1.65]))
            c.line([[6.0, 0.0], [6.0, 6.92820323027551]], id='o7', linestyle=(0.0, [1.0, 1.65]))
            c.path([[5.546640299900456, 6.142961195598911], [5.615263293436004, 6.103341691808565], [5.688784746792836, 6.072888108702784], [5.765323750664542, 6.052379544425878], [5.8418627545362485, 6.031870980148971], [5.920760992419307, 6.021483830076422], [6.0, 6.021483830076422]], [1, 4, 4, 4, 4, 4, 4], id='o8', zorder=3, facecolor=(0.0, 0.0, 0.0, 0), capstyle='butt', fill=False)
            c.path([[5.585, 6.209402145134426], [5.765, 6.179402145134426], [5.705, 6.059402145134426], [5.585, 6.209402145134426]], [1, 2, 2, 79], id='o9', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
            c.path([[5.585, 6.209402145134426], [5.765, 6.179402145134426], [5.705, 6.059402145134426], [5.585, 6.209402145134426]], [1, 2, 2, 79], id='o9', facecolor=(0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0), capstyle='butt', fill=False)
            c.line([[0.0, -0.5], [6.0, -0.5]], id='dimline', linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 0.0], [0.0, -0.5]], id='dimleft')
            c.line([[6.0, 0.0], [6.0, -0.5]], id='dimright')
            c.text('L', (3.7, 3.4), id='t0', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            c.text('$\\theta$', (6.0, 6.92820323027551), id='theta', rotation_mode='default', offset_pt=(-18.117333157176454, -67.61480784023477), annotation_clip=None)
            c.text('6″', (3.0, -0.82), id='t2', rotation_mode='default', offset_pt=(0, 0), annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane447().draw(sys.argv[1] if len(sys.argv) > 1 else None))
