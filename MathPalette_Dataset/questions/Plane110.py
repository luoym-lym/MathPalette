"""Collected question Plane110; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane110:
    variants = ('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08')

    def __init__(self):
        self.id = 'Plane110'
        self.source_dataset = 'Author Designed'
        self.source_key = 'intersection-counting:unequal_circles_four_crossings'
        self.question = 'How many points of intersection are shown in the figure?'
        self.answer = 4
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'center_0': [-0.85, 0.35],
         'center_1': [0.9, 0.05],
         'center_2': [1.65, 1.4],
         'crossing_1': [0.15902991149963308, -1.0181588495854723],
         'crossing_2': [0.557108074225981, 1.303963766318224],
         'crossing_3': [1.002249241804092, 1.3459726434421708],
         'crossing_4': [1.9463356638562852, 0.8214801867465081]}

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-2.662790697674419, 2.412790697674419], ylim=[-2.1877906976744192, 2.8877906976744185]) as c:
            for object_id, center, radius in [('curve_0', self.points['center_0'], 1.7), ('curve_1', self.points['center_1'], 1.3), ('curve_2', self.points['center_2'], 0.65)]:
                c.circle(center, radius, id=object_id)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C01.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C02.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C03.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.9463356638562852, 0.8214801867465081]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]])
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C04.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]], edgecolors=[[0.08627450980392157, 0.6392156862745098, 0.2901960784313726, 1.0]])
            return c.save(output_path)

    def draw_C05(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C05.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            c.point([[0.557108074225981, 1.303963766318224]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            c.point([[1.9463356638562852, 0.8214801867465081]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C06(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C06.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            c.point([[0.15902991149963308, -1.0181588495854723]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            c.point([[1.9463356638562852, 0.8214801867465081]], zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C07(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C07.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]]), (None, [[0.85, 0.35]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]])
            return c.save(output_path)

    def draw_C08(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane110_C08.png'
        with Canvas(PLANE, xlim=(-2.662790697674419, 2.412790697674419), ylim=(-2.1877906976744192, 2.8877906976744185), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, center, radius in [('curve_0', [-0.85, 0.35], 1.7), ('curve_1', [0.9, 0.05], 1.3), ('curve_2', [1.65, 1.4], 0.65)]:
                c.circle(center, radius, id=object_id, fill=False)
            for object_id, points in [(None, [[0.15902991149963308, -1.0181588495854723]]), (None, [[0.557108074225981, 1.303963766318224]]), (None, [[1.002249241804092, 1.3459726434421708]]), (None, [[1.9463356638562852, 0.8214801867465081]]), (None, [[-0.8499999999999999, 2.05]])]:
                c.point(points, id=object_id, zorder=10, s=[50], facecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]], edgecolors=[[0.9176470588235294, 0.34509803921568627, 0.047058823529411764, 1.0]])
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane110')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08'))
    args = parser.parse_args()
    print(Plane110().draw(args.output, variant=args.variant))
