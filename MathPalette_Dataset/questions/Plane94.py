"""Collected question Plane94; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane94:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05')

    def __init__(self):
        self.id = 'Plane94'
        self.source_dataset = 'Author Designed'
        self.source_key = 'smooth-curve:02'
        self.question = 'Starting at D, which endpoint is reached along the same smooth curve, without switching curves at any crossing?'
        self.answer = 'A'
        self.answer_type = 'text'
        self.query = self.question
        self.points = {'C': [-1.0, 0.45], 'B': [1.0, 0.45], 'A': [-1.0, -0.45], 'D': [1.0, -0.45], 'J01': [-0.7071067811865475, 0.0], 'J02': [0.7071067811865476, 0.0]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-1.1497850639678173, 1.1497902978469967], ylim=[-1.1411083357346676, 1.1584670260801464]) as c:
            for object_id, vertices, codes in [('CB_s01_C_J01', [[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('CB_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('CB_s03_J02_B', [[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4]), ('AD_s01_A_J01', [[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4]), ('AD_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('AD_s03_J02_D', [[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, capstyle='butt', zorder=1)
            c.text('C', self.points['C'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('B', self.points['B'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            c.text('A', self.points['A'], offset_pt=[-8.0, -0.0], vertex=True, ha='right')
            c.text('D', self.points['D'], offset_pt=[8.0, 0.0], vertex=True, ha='left')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C01.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4], id='CB_s01_C_J01', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            for object_id, vertices, codes in [('CB_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('CB_s03_J02_B', [[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4]), ('AD_s01_A_J01', [[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, zorder=1, capstyle='butt')
            c.path([[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4], id='AD_s02_J01_J02', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4], id='AD_s03_J02_D', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.text('C', (-1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('B', (1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            c.text('A', (-1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('D', (1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C02.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4], id='CB_s01_C_J01', zorder=1, capstyle='butt')
            for object_id, vertices, codes in [('CB_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('CB_s03_J02_B', [[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4]), ('AD_s01_A_J01', [[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=(0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0), capstyle='butt')
            c.path([[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4], id='AD_s02_J01_J02', zorder=1, capstyle='butt')
            c.path([[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4], id='AD_s03_J02_D', zorder=1, capstyle='butt')
            c.text('C', (-1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('B', (1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            c.text('A', (-1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('D', (1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C03.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4], id='CB_s01_C_J01', zorder=1, capstyle='butt')
            for object_id, vertices, codes in [('CB_s02_J01_J02', [[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4]), ('CB_s03_J02_B', [[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4]), ('AD_s01_A_J01', [[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4])]:
                c.path(vertices, codes, id=object_id, zorder=1, linestyle=(0, [3.7, 1.6]), capstyle='butt')
            c.path([[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4], id='AD_s02_J01_J02', zorder=1, capstyle='butt')
            c.path([[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4], id='AD_s03_J02_D', zorder=1, capstyle='butt')
            c.text('C', (-1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('B', (1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            c.text('A', (-1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('D', (1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C04.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4], id='CB_s01_C_J01', zorder=1, capstyle='butt')
            c.path([[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4], id='CB_s02_J01_J02', zorder=1, capstyle='butt')
            c.path([[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4], id='CB_s03_J02_B', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.path([[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4], id='AD_s01_A_J01', zorder=1, capstyle='butt')
            c.path([[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4], id='AD_s02_J01_J02', zorder=1, capstyle='butt')
            c.path([[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4], id='AD_s03_J02_D', zorder=1, edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt')
            c.text('C', (-1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('B', (1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            c.text('A', (-1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('D', (1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane94_C05.png'
        with Canvas(PLANE, xlim=(-1.1497850639678173, 1.1497902978469967), ylim=(-1.1411083357346676, 1.1584670260801464), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-1.0, 0.45], [-0.9023689270621824, 0.27426406871192854], [-0.8047378541243649, 0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4], id='CB_s01_C_J01', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
            c.path([[-0.7071067811865475, 0.0], [-0.23570226039551587, -0.6], [0.2357022603955159, -0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4], id='CB_s02_J01_J02', zorder=1, capstyle='butt')
            c.path([[0.7071067811865476, 0.0], [0.804737854124365, 0.12426406871192856], [0.9023689270621825, 0.27426406871192854], [1.0, 0.45]], [1, 4, 4, 4], id='CB_s03_J02_B', zorder=1, edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
            c.path([[-1.0, -0.45], [-0.9023689270621824, -0.27426406871192854], [-0.8047378541243649, -0.12426406871192855], [-0.7071067811865475, 0.0]], [1, 4, 4, 4], id='AD_s01_A_J01', zorder=1, edgecolor=(0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0), capstyle='butt')
            c.path([[-0.7071067811865475, 0.0], [-0.23570226039551587, 0.6], [0.2357022603955159, 0.5999999999999999], [0.7071067811865476, 0.0]], [1, 4, 4, 4], id='AD_s02_J01_J02', zorder=1, capstyle='butt')
            c.path([[0.7071067811865476, 0.0], [0.804737854124365, -0.12426406871192856], [0.9023689270621825, -0.27426406871192854], [1.0, -0.45]], [1, 4, 4, 4], id='AD_s03_J02_D', zorder=1, edgecolor=(0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0), capstyle='butt')
            c.text('C', (-1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('B', (1.0, 0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            c.text('A', (-1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-8.0, -0.0), annotation_clip=False)
            c.text('D', (1.0, -0.45), zorder=3, clip_on=True, fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(8.0, 0.0), annotation_clip=False)
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane94')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05'))
    args = parser.parse_args()
    print(Plane94().draw(args.output, variant=args.variant))
