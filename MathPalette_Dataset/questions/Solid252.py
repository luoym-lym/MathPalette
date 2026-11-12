"""Collected question Solid252; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid252:
    variants = ('C01',)

    def __init__(self):
        self.id = 'Solid252'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Solid259'
        self.question = 'The diagram is a net of a regular octahedron. When the net is folded, which labelled edge A, B, C, D, or E coincides with edge x? Give the letter.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-1.574038105676658, 2.074038105676658], ylim=[-1.3910254037844387, 2.257050807568877], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.line([[-1.0, 1.7320508075688772], [-0.5, 0.8660254037844386]], id='edge00', zorder=1)
            c.text('C', [-0.9145448267190434, 1.204038105676658], zorder=2, rotation_mode='default')
            c.line([[-1.0, 1.7320508075688772], [0.0, 1.7320508075688772]], id='edge01', zorder=1)
            c.text('x', [-0.5, 1.9220508075688771], zorder=2, rotation_mode='default')
            c.line([[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]], id='edge02', zorder=1)
            c.line([[-0.5, 0.8660254037844386], [0.0, 0.0]], id='edge03', zorder=1)
            c.text('E', [-0.41454482671904336, 0.3380127018922193], zorder=2, rotation_mode='default')
            for object_id, points in [('edge04', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge05', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('edge06', [[0.0, 1.7320508075688772], [1.0, 1.7320508075688772]]), ('edge07', [[-0.5, -0.8660254037844386], [0.0, 0.0]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('D', [-0.41454482671904336, -0.3380127018922193], zorder=2, rotation_mode='default')
            c.line([[-0.5, -0.8660254037844386], [0.5, -0.8660254037844386]], id='edge08', zorder=1)
            c.text('A', [0.0, -1.0560254037844385], zorder=2, rotation_mode='default')
            for object_id, points in [('edge09', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge10', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge11', [[0.0, 0.0], [1.0, 0.0]]), ('edge12', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge13', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge14', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge15', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('B', [1.0, -1.0560254037844385], zorder=2, rotation_mode='default')
            c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge16', zorder=1)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid252_C01.png'
        with Canvas(SOLID, xlim=(-1.574038105676658, 2.074038105676658), ylim=(-1.3910254037844387, 2.257050807568877), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.line([[-1.0, 1.7320508075688772], [-0.5, 0.8660254037844386]], id='edge00', zorder=1)
            c.text('C', (-0.9145448267190434, 1.204038105676658), zorder=2, rotation_mode='default')
            c.line([[-1.0, 1.7320508075688772], [0.0, 1.7320508075688772]], id='edge01', zorder=1, color='#EA580C', linewidth=2.0)
            c.text('x', (-0.5, 1.9220508075688771), zorder=2, rotation_mode='default')
            c.line([[-0.5, 0.8660254037844386], [0.0, 1.7320508075688772]], id='edge02', zorder=1)
            c.line([[-0.5, 0.8660254037844386], [0.0, 0.0]], id='edge03', zorder=1)
            c.text('E', (-0.41454482671904336, 0.3380127018922193), zorder=2, rotation_mode='default')
            for object_id, points in [('edge04', [[-0.5, 0.8660254037844386], [0.5, 0.8660254037844386]]), ('edge05', [[0.0, 1.7320508075688772], [0.5, 0.8660254037844386]]), ('edge06', [[0.0, 1.7320508075688772], [1.0, 1.7320508075688772]])]:
                c.line(points, id=object_id, zorder=1)
            c.line([[-0.5, -0.8660254037844386], [0.0, 0.0]], id='edge07', zorder=1, color='#EA580C', linewidth=2.0)
            c.text('D', (-0.41454482671904336, -0.3380127018922193), zorder=2, rotation_mode='default')
            c.line([[-0.5, -0.8660254037844386], [0.5, -0.8660254037844386]], id='edge08', zorder=1)
            c.text('A', (0.0, -1.0560254037844385), zorder=2, rotation_mode='default')
            for object_id, points in [('edge09', [[0.0, 0.0], [0.5, 0.8660254037844386]]), ('edge10', [[0.0, 0.0], [0.5, -0.8660254037844386]]), ('edge11', [[0.0, 0.0], [1.0, 0.0]]), ('edge12', [[0.5, 0.8660254037844386], [1.0, 1.7320508075688772]]), ('edge13', [[0.5, 0.8660254037844386], [1.0, 0.0]]), ('edge14', [[0.5, -0.8660254037844386], [1.0, 0.0]]), ('edge15', [[0.5, -0.8660254037844386], [1.5, -0.8660254037844386]])]:
                c.line(points, id=object_id, zorder=1)
            c.text('B', (1.0, -1.0560254037844385), zorder=2, rotation_mode='default')
            c.line([[1.0, 0.0], [1.5, -0.8660254037844386]], id='edge16', zorder=1)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid252')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Solid252().draw(args.output, variant=args.variant))
