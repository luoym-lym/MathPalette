"""Collected question Plane365; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane365:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane365'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1338'
        self.question = 'A triangle is folded along the dashed line as shown. The area of the triangle is 1.5 times the area of the resulting figure, and the total area of the grey parts is 1. Determine the area of the starting triangle.'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-0.216645832396126, 8.737173700342762], ylim=[-3.7308160163694444, 5.223003516369444], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [3.1622776601683795, 0.0], [2.2135943621178655, 1.8973665961010275], [0.0, 0.0]], [1, 2, 2, 79], id='o0', zorder=1, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[2.2099931049490764, -0.4269074841227312], [1.5121734126066786, 1.9210836785522905]], id='o1', linestyle=(0.0, [4.0, 3.0]))
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', zorder=3, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=4, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=5, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=6, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=7, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[4.7, 0.0], [6.783116797250459, 0.0]], id='o5', linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.7, 0.0], [6.360195771588399, 1.4230249470757708]], id='o6', linestyle=(0.0, [4.0, 3.0]))
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane365_C01.png'
        with Canvas(PLANE, xlim=(-0.216645832396126, 8.737173700342762), ylim=(-3.7308160163694444, 5.223003516369444), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [3.1622776601683795, 0.0], [2.2135943621178655, 1.8973665961010275], [0.0, 0.0]], [1, 2, 2, 79], id='o0', zorder=1, capstyle='butt')
            c.line([[2.2099931049490764, -0.4269074841227312], [1.5121734126066786, 1.9210836785522905]], id='o1', linestyle=(0.0, [4.0, 3.0]))
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', zorder=3, capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=4, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=5, capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=6, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=7, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=1.5, capstyle='butt', fill=False)
            c.line([[4.7, 0.0], [6.783116797250459, 0.0]], id='o5', linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.7, 0.0], [6.360195771588399, 1.4230249470757708]], id='o6', linestyle=(0.0, [4.0, 3.0]))
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane365_C02.png'
        with Canvas(PLANE, xlim=(-0.216645832396126, 8.737173700342762), ylim=(-3.7308160163694444, 5.223003516369444), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [3.1622776601683795, 0.0], [2.2135943621178655, 1.8973665961010275], [0.0, 0.0]], [1, 2, 2, 79], id='o0', zorder=1, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), linewidth=2.0, capstyle='butt')
            c.line([[2.2099931049490764, -0.4269074841227312], [1.5121734126066786, 1.9210836785522905]], id='o1', linestyle=(0.0, [4.0, 3.0]))
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', zorder=3, capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=4, edgecolor='none', facecolor=(0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45), linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=5, capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=6, edgecolor='none', facecolor=(1.0, 1.0, 1.0, 1.0), linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=7, capstyle='butt', fill=False)
            c.line([[4.7, 0.0], [6.783116797250459, 0.0]], id='o5', color='#16A34A', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.7, 0.0], [6.360195771588399, 1.4230249470757708]], id='o6', color='#16A34A', linewidth=1.5, linestyle=(0.0, [4.0, 3.0]))
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane365')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane365().draw(args.output, variant=args.variant))
