"""Collected question Ana39; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana39:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Ana39'
        self.source_dataset = 'MathVerse'
        self.source_key = 's2789'
        self.question = '\\[What is the domain of h?\nChoices:\nA:-5 \\leq x \\leq 7\nB:-5 \\leq x \\leq 4\nC:-5 \\leq x \\leq 5\nD:-5 \\leq x \\leq 6\\]'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '-5 \\leq x \\leq 7', 'B': '-5 \\leq x \\leq 4', 'C': '-5 \\leq x \\leq 5', 'D': '-5 \\leq x \\leq 6'}
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(ANALYTICS, xlim=[-8.0, 8.0], ylim=[-8.0, 8.0], axes_position=[0.12, 0.12, 0.8, 0.8], coordinate_axes=True) as c:
            c.line([[-5.0, 4.0], [-3.0, 3.0], [0.0, 7.0], [3.0, 1.0], [4.0, -5.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-5.0, 4.0], [4.0, -5.0]], id='point_001')
            c.text('h', [2, 1.8], id='text_001', rotation_mode='default')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana39_C01.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-5.0, 4.0], [-3.0, 3.0], [0.0, 7.0], [3.0, 1.0], [4.0, -5.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-5.0, 4.0], [4.0, -5.0]], id='point_001')
            c.text('h', (2, 1.8), id='text_001', rotation_mode='default')
            c.line([[-5, 8], [-5, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[5, 8], [5, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Ana39_C02.png'
        with Canvas(ANALYTICS, xlim=(-8.0, 8.0), ylim=(-8.0, 8.0), axes_position=(0.12, 0.12, 0.8, 0.8), coordinate_axes=True) as c:
            c.line([[-5.0, 4.0], [-3.0, 3.0], [0.0, 7.0], [3.0, 1.0], [4.0, -5.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-5.0, 4.0], [4.0, -5.0]], id='point_001')
            c.text('h', (2, 1.8), id='text_001', rotation_mode='default')
            c.line([[-5, 8], [-5, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[7, 8], [7, -8]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Ana39')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Ana39().draw(args.output, variant=args.variant))
