"""Collected question Solid78; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid78:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Solid78'
        self.source_dataset = 'Author Designed'
        self.source_key = 'solid82:net-edge-endpoint-identification'
        self.question = 'The figure shows a net of a square pyramid. After folding, which of the following edges has no endpoint in common with edge AB?\nChoices:\nA: Edge DE\nB: Edge CD\nC: Edge CE\nD: None of these three edges'
        self.answer = 'A'
        self.answer_type = 'choice'
        self.choices = {'A': 'Edge DE', 'B': 'Edge CD', 'C': 'Edge CE', 'D': 'None of these three edges'}
        self.query = self.question
        self.points = {'v00': [0.0, 0.0, 0.0],
         'v01': [1.0, 0.0, 0.0],
         'v02': [0.5, 1.118033988749895, 0.0],
         'v03': [1.6666666666666665, 0.7453559924999298, 0.0],
         'v04': [1.5555555555555556, 1.7391639824998364, 0.0],
         'v05': [0.7407407407407409, 2.3188853099997817, 0.0],
         'v06': [1.0, -1.0, 0.0],
         'v07': [0.0, -1.0, 0.0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=[-1.0690872749445486, 2.6044840987074416], ylim=[-1.0909815619277845, 2.5825898117242057], projection=[[1, 0, 0], [0, 1, 0]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('edge_v00_v01', c.project([self.points['v00'], self.points['v01']])), ('edge_v01_v02', c.project([self.points['v01'], self.points['v02']])), ('edge_v00_v02', c.project([self.points['v00'], self.points['v02']])), ('edge_v01_v03', c.project([self.points['v01'], self.points['v03']])), ('edge_v02_v03', c.project([self.points['v02'], self.points['v03']])), ('edge_v03_v04', c.project([self.points['v03'], self.points['v04']])), ('edge_v02_v04', c.project([self.points['v02'], self.points['v04']])), ('edge_v04_v05', c.project([self.points['v04'], self.points['v05']])), ('edge_v02_v05', c.project([self.points['v02'], self.points['v05']])), ('edge_v01_v06', c.project([self.points['v01'], self.points['v06']])), ('edge_v06_v07', c.project([self.points['v06'], self.points['v07']])), ('edge_v00_v07', c.project([self.points['v00'], self.points['v07']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('A', c.project(self.points['v00']), offset_pt=[-16.625578163355026, 3.548260240480185], vertex=True, id='label_A')
            c.text('B', c.project(self.points['v01']), offset_pt=[15.880930102366165, -6.065975526142535], vertex=True, id='label_B')
            c.text('C', c.project(self.points['v05']), offset_pt=[-6.262662537244549, 15.80439995522113], vertex=True, id='label_C')
            c.text('D', c.project(self.points['v04']), offset_pt=[14.651577535536417, 8.621558775544282], vertex=True, id='label_D')
            c.text('E', c.project(self.points['v02']), offset_pt=[-16.193848855066566, 5.172935265326576], vertex=True, id='label_E')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid78_C01.png'
        with Canvas(SOLID, xlim=(-1.0690872749445486, 2.6044840987074416), ylim=(-1.0909815619277845, 2.5825898117242057), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('edge_v00_v01', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v01_v02', [[1.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v00_v02', [[0.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v01_v03', [[1.0, 0.0], [1.6666666666666665, 0.7453559924999298]]), ('edge_v02_v03', [[0.5, 1.118033988749895], [1.6666666666666665, 0.7453559924999298]]), ('edge_v03_v04', [[1.6666666666666665, 0.7453559924999298], [1.5555555555555556, 1.7391639824998364]]), ('edge_v02_v04', [[0.5, 1.118033988749895], [1.5555555555555556, 1.7391639824998364]]), ('edge_v04_v05', [[1.5555555555555556, 1.7391639824998364], [0.7407407407407409, 2.3188853099997817]]), ('edge_v02_v05', [[0.5, 1.118033988749895], [0.7407407407407409, 2.3188853099997817]]), ('edge_v01_v06', [[1.0, 0.0], [1.0, -1.0]]), ('edge_v06_v07', [[1.0, -1.0], [0.0, -1.0]]), ('edge_v00_v07', [[0.0, 0.0], [0.0, -1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.625578163355026, 3.548260240480185), annotation_clip=None)
            c.text('B', (1.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15.880930102366165, -6.065975526142535), annotation_clip=None)
            c.text('C', (0.7407407407407409, 2.3188853099997817), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-6.262662537244549, 15.80439995522113), annotation_clip=None)
            c.text('D', (1.5555555555555556, 1.7391639824998364), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14.651577535536417, 8.621558775544282), annotation_clip=None)
            c.text('E', (0.5, 1.118033988749895), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.193848855066566, 5.172935265326576), annotation_clip=None)
            c.point([[0.0, 0.0]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            c.point([[1.0, 0.0]], zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
            c.point([[0.7407407407407409, 2.3188853099997817]], zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            c.point([[0.5, 1.118033988749895]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            c.point([[1.5555555555555556, 1.7391639824998364]], zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            c.line([[0.0, 0.0], [1.5555555555555556, 1.7391639824998364]], zorder=9, color='#EA580C', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid78_C02.png'
        with Canvas(SOLID, xlim=(-1.0690872749445486, 2.6044840987074416), ylim=(-1.0909815619277845, 2.5825898117242057), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('edge_v00_v01', [[0.0, 0.0], [1.0, 0.0]]), ('edge_v01_v02', [[1.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v00_v02', [[0.0, 0.0], [0.5, 1.118033988749895]]), ('edge_v01_v03', [[1.0, 0.0], [1.6666666666666665, 0.7453559924999298]]), ('edge_v02_v03', [[0.5, 1.118033988749895], [1.6666666666666665, 0.7453559924999298]]), ('edge_v03_v04', [[1.6666666666666665, 0.7453559924999298], [1.5555555555555556, 1.7391639824998364]]), ('edge_v02_v04', [[0.5, 1.118033988749895], [1.5555555555555556, 1.7391639824998364]]), ('edge_v04_v05', [[1.5555555555555556, 1.7391639824998364], [0.7407407407407409, 2.3188853099997817]]), ('edge_v02_v05', [[0.5, 1.118033988749895], [0.7407407407407409, 2.3188853099997817]]), ('edge_v01_v06', [[1.0, 0.0], [1.0, -1.0]]), ('edge_v06_v07', [[1.0, -1.0], [0.0, -1.0]]), ('edge_v00_v07', [[0.0, 0.0], [0.0, -1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.text('A', (0.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.625578163355026, 3.548260240480185), annotation_clip=None)
            c.text('B', (1.0, 0.0), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(15.880930102366165, -6.065975526142535), annotation_clip=None)
            c.text('C', (0.7407407407407409, 2.3188853099997817), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-6.262662537244549, 15.80439995522113), annotation_clip=None)
            c.text('D', (1.5555555555555556, 1.7391639824998364), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(14.651577535536417, 8.621558775544282), annotation_clip=None)
            c.text('E', (0.5, 1.118033988749895), fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(-16.193848855066566, 5.172935265326576), annotation_clip=None)
            for object_id, points in [(None, [[0.5, 1.118033988749895]]), (None, [[1.5555555555555556, 1.7391639824998364]]), (None, [[0.0, 0.0]]), (None, [[1.0, 0.0]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            c.line([[1.5555555555555556, 1.7391639824998364], [0.0, 0.0]], zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid78')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Solid78().draw(args.output, variant=args.variant))
