"""Collected question Plane100; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane100:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane100'
        self.source_dataset = 'Author Designed'
        self.source_key = 'shortest-path:equal'
        self.question = 'Find the length of the shortest path from A to B that stays outside the interiors of both disks.'
        self.answer = '2*sqrt(3) + 2 + pi/3'
        self.answer_type = 'number'
        self.query = self.question

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=[-3.465, 3.465], ylim=[-3.155, 3.775], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.circle([-1.0, 0.0], 1.0, id='left_circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.circle([1.0, 0.0], 1.0, id='right_circle', facecolor=[0.0, 0.0, 0.0, 0], fill=False)
            c.line([[-3.0, 0.0], [3.0, 0.0]], id='AB_baseline')
            for object_id, points in [('L_dot', [[-1.0, 0.0]]), ('R_dot', [[1.0, 0.0]]), ('A_dot', [[-3.0, 0.0]]), ('B_dot', [[3.0, 0.0]])]:
                c.point(points, id=object_id)
            c.line([[-1.0, 0.0], [-0.5, 0.8660254037844386]], id='L_radius')
            c.line([[1.0, 0.0], [0.5, 0.8660254037844386]], id='R_radius')
            c.line([[-3.0, 1.35], [-1.0, 1.35]], id='AL_dimension_line', linestyle=(0, [4, 3]))
            c.line([[-3.0, 0.0], [-3.0, 1.35]], id='AL_connector_0')
            c.line([[-1.0, 0.0], [-1.0, 1.35]], id='AL_connector_1')
            c.line([[3.0, 1.35], [1.0, 1.35]], id='BR_dimension_line', linestyle=(0, [4, 3]))
            c.line([[3.0, 0.0], [3.0, 1.35]], id='BR_connector_0')
            c.line([[1.0, 0.0], [1.0, 1.35]], id='BR_connector_1')
            c.text('A', [-3.0, 0.0], id='A_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=[-10, 0], annotation_clip=None)
            c.text('B', [3.0, 0.0], id='B_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=[10, 0], annotation_clip=None)
            c.text('L', [-1.0, 0.0], id='L_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('R', [1.0, 0.0], id='R_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=[0, -14], annotation_clip=None)
            c.text('1', [-0.75, 0.4330127018922193], id='L_radius_value', rotation_mode='default', offset_pt=[10, 0], annotation_clip=None)
            c.text('1', [0.75, 0.4330127018922193], id='R_radius_value', rotation_mode='default', offset_pt=[-10, 0], annotation_clip=None)
            c.text('2', [-2.0, 1.35], id='AL_value', rotation_mode='default', offset_pt=[0, 12], annotation_clip=None)
            c.text('2', [2.0, 1.35], id='BR_value', rotation_mode='default', offset_pt=[0, 12], annotation_clip=None)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane100_C01.png'
        with Canvas(PLANE, xlim=(-3.465, 3.465), ylim=(-3.155, 3.775), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-1.0000000000000004, -0.9999999999999994], [-0.7347969000000005, -0.9999999999999994], [-0.4804201292151471, -0.8946336915882411], [-0.292893218813453, -0.707106781186547], [-0.10569590944575816, -0.5199094718188522], [-0.00037064165877173373, -0.266097088846597], [-9.76375587264278e-07, -0.0013982781181797884]], [1, 4, 4, 4, 4, 4, 4], id='left_circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[-9.76375587264278e-07, -0.0013982781181797884], [-3.2550052937591694e-07, -0.0009322190599104047], [-5.551115123125783e-16, -0.00046612625245355614], [-5.551115123125783e-16, 4.440892098500626e-16], [-5.551115123125783e-16, 0.2652031000000004], [-0.10536630841175887, 0.5195798707848538], [-0.292893218813453, 0.7071067811865479], [-0.4804201292151471, 0.894633691588242], [-0.7347969000000005, 1.0000000000000004], [-1.0000000000000004, 1.0000000000000004], [-1.2652031000000004, 1.0000000000000004], [-1.5195798707848538, 0.894633691588242], [-1.707106781186548, 0.7071067811865479], [-1.894633691588242, 0.5195798707848538], [-2.0000000000000004, 0.2652031000000004], [-2.0000000000000004, 4.440892098500626e-16], [-2.0000000000000004, -0.2652030999999995], [-1.894633691588242, -0.5195798707848529], [-1.707106781186548, -0.707106781186547], [-1.6366894772468337, -0.7775240851262614], [-1.556846072192505, -0.8363564113628689], [-1.4705428850906872, -0.8823750703084405]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='left_circle', capstyle='butt', fill=False)
            c.path([[-1.4705428850906872, -0.8823750703084405], [-1.3270137848206565, -0.9589077794226348], [-1.165617993742708, -0.9999999999999994], [-1.0000000000000004, -0.9999999999999994]], [1, 4, 4, 4], id='left_circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[0.9999999999999996, -0.9999999999999994], [1.2108581980535933, -0.9999999999999994], [1.4148724746258095, -0.9333921288349698], [1.583884547163879, -0.8118399290314013]], [1, 4, 4, 4], id='right_circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[1.583884547163879, -0.8118399290314013], [1.627444364114917, -0.7805120392899936], [1.6686791324973251, -0.7455344298757689], [1.707106781186547, -0.707106781186547], [1.8946336915882411, -0.5195798707848529], [1.9999999999999996, -0.2652030999999995], [1.9999999999999996, 4.440892098500626e-16], [1.9999999999999996, 0.2652031000000004], [1.8946336915882411, 0.5195798707848538], [1.707106781186547, 0.7071067811865479], [1.519579870784853, 0.894633691588242], [1.2652030999999995, 1.0000000000000004], [0.9999999999999996, 1.0000000000000004], [0.7347968999999996, 1.0000000000000004], [0.4804201292151462, 0.894633691588242], [0.2928932188134521, 0.7071067811865479], [0.10839225394842292, 0.5226058163215187], [0.003421786571719641, 0.27339497197010215], [8.220595310017335e-05, 0.012829307641072842]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='right_circle', capstyle='butt', fill=False)
            c.path([[8.220595310017335e-05, 0.012829307641072842], [2.7434483072161064e-05, 0.00855584755612775], [-3.3306690738754696e-16, 0.004279333216954324], [-3.3306690738754696e-16, 4.440892098500626e-16], [-3.3306690738754696e-16, -0.2652030999999995], [0.10536630841175798, -0.5195798707848529], [0.2928932188134521, -0.707106781186547], [0.4804201292151462, -0.8946336915882411], [0.7347968999999996, -0.9999999999999994], [0.9999999999999996, -0.9999999999999994]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='right_circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.line([[-3.0, 0.0], [3.0, 0.0]], id='AB_baseline')
            for object_id, points in [('L_dot', [[-1.0, 0.0]]), ('R_dot', [[1.0, 0.0]]), ('A_dot', [[-3.0, 0.0]]), ('B_dot', [[3.0, 0.0]])]:
                c.point(points, id=object_id)
            c.line([[-1.0, 0.0], [-0.5, 0.8660254037844386]], id='L_radius')
            c.line([[1.0, 0.0], [0.5, 0.8660254037844386]], id='R_radius')
            c.line([[-3.0, 1.35], [-1.0, 1.35]], id='AL_dimension_line', linestyle=(0, [4, 3]))
            c.line([[-3.0, 0.0], [-3.0, 1.35]], id='AL_connector_0')
            c.line([[-1.0, 0.0], [-1.0, 1.35]], id='AL_connector_1')
            c.line([[3.0, 1.35], [1.0, 1.35]], id='BR_dimension_line', linestyle=(0, [4, 3]))
            c.line([[3.0, 0.0], [3.0, 1.35]], id='BR_connector_0')
            c.line([[1.0, 0.0], [1.0, 1.35]], id='BR_connector_1')
            c.text('A', (-3.0, 0.0), id='A_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-10, 0), annotation_clip=None)
            c.text('B', (3.0, 0.0), id='B_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(10, 0), annotation_clip=None)
            c.text('L', (-1.0, 0.0), id='L_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -14), annotation_clip=None)
            c.text('R', (1.0, 0.0), id='R_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -14), annotation_clip=None)
            c.text('1', (-0.75, 0.4330127018922193), id='L_radius_value', rotation_mode='default', offset_pt=(10, 0), annotation_clip=None)
            c.text('1', (0.75, 0.4330127018922193), id='R_radius_value', rotation_mode='default', offset_pt=(-10, 0), annotation_clip=None)
            c.text('2', (-2.0, 1.35), id='AL_value', rotation_mode='default', offset_pt=(0, 12), annotation_clip=None)
            c.text('2', (2.0, 1.35), id='BR_value', rotation_mode='default', offset_pt=(0, 12), annotation_clip=None)
            c.line([[-3.0, 0.0], [-1.4649816176470583, -0.9002022058823531]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            c.line([[3.0, 0.0], [1.5003676470588232, -0.8789705882352941]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane100_C02.png'
        with Canvas(PLANE, xlim=(-3.465, 3.465), ylim=(-3.155, 3.775), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[-1.0000000000000004, -0.9999999999999994], [-0.7347969000000005, -0.9999999999999994], [-0.4804201292151471, -0.8946336915882411], [-0.292893218813453, -0.707106781186547], [-0.10536630841175887, -0.5195798707848529], [-5.551115123125783e-16, -0.2652030999999995], [-5.551115123125783e-16, 4.440892098500626e-16], [-5.551115123125783e-16, 0.2652031000000004], [-0.10536630841175887, 0.5195798707848538], [-0.292893218813453, 0.7071067811865479], [-0.47665482943334414, 0.8908683918064391], [-0.7246087324147968, 0.9957356359562922], [-0.9840387335100125, 0.999872751021975]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='left_circle', capstyle='butt', fill=False)
            c.path([[-0.9840387335100125, 0.999872751021975], [-0.989354488651806, 0.9999575210585543], [-0.9946750619821743, 1.0000000000000004], [-1.0000000000000004, 1.0000000000000004], [-1.2652031000000004, 1.0000000000000004], [-1.5195798707848538, 0.894633691588242], [-1.707106781186548, 0.7071067811865479], [-1.894633691588242, 0.5195798707848538], [-2.0000000000000004, 0.2652031000000004], [-2.0000000000000004, 4.440892098500626e-16], [-2.0000000000000004, -0.000479785589970417], [-1.999999655143059, -0.0009595357460835653], [-1.9999989655665806, -0.0014392501366154616]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='left_circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[-1.9999989655665806, -0.0014392501366154616], [-1.999618489423211, -0.266123280016511], [-1.894294431944058, -0.5199191304290369], [-1.707106781186548, -0.707106781186547], [-1.5195798707848538, -0.8946336915882411], [-1.2652031000000004, -0.9999999999999994], [-1.0000000000000004, -0.9999999999999994]], [1, 4, 4, 4, 4, 4, 4], id='left_circle', capstyle='butt', fill=False)
            c.path([[0.9999999999999996, -0.9999999999999994], [1.2652030999999995, -0.9999999999999994], [1.519579870784853, -0.8946336915882411], [1.707106781186547, -0.707106781186547], [1.8946336915882411, -0.5195798707848529], [1.9999999999999996, -0.2652030999999995], [1.9999999999999996, 4.440892098500626e-16], [1.9999999999999996, 0.0019088305481497873], [1.9999945414244544, 0.0038171002307170656], [1.9999836329262533, 0.0057247881577802]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='right_circle', capstyle='butt', fill=False)
            c.path([[1.9999836329262533, 0.0057247881577802], [1.9984789707824635, 0.26886145033304704], [1.8932839445635088, 0.5209296178095862], [1.707106781186547, 0.7071067811865479], [1.5207265073254004, 0.8934870550476945], [1.2683113830013817, 0.9987084000008649], [1.0048635397306118, 0.9999881872126535]], [1, 4, 4, 4, 4, 4, 4], id='right_circle', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), capstyle='butt', fill=False)
            c.path([[1.0048635397306118, 0.9999881872126535], [1.003242773126053, 0.9999960606359013], [1.0016215889467543, 1.0000000000000004], [0.9999999999999996, 1.0000000000000004], [0.7347968999999996, 1.0000000000000004], [0.4804201292151462, 0.894633691588242], [0.2928932188134521, 0.7071067811865479], [0.10536630841175798, 0.5195798707848538], [-3.3306690738754696e-16, 0.2652031000000004], [-3.3306690738754696e-16, 4.440892098500626e-16], [-3.3306690738754696e-16, -0.2652030999999995], [0.10536630841175798, -0.5195798707848529], [0.2928932188134521, -0.707106781186547], [0.4804201292151462, -0.8946336915882411], [0.7347968999999996, -0.9999999999999994], [0.9999999999999996, -0.9999999999999994]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='right_circle', capstyle='butt', fill=False)
            c.path([[-3.0, 4.440892098500626e-16], [-1.995772058823529, 4.440892098500626e-16]], [1, 2], id='AB_baseline', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), joinstyle='round', fill=False)
            c.path([[-1.9957720588235293, 4.440892098500626e-16], [2.0028492647058824, 4.440892098500626e-16]], [1, 2], id='AB_baseline', joinstyle='round', fill=False)
            c.path([[2.0028492647058824, 4.440892098500626e-16], [2.999999999999999, 4.440892098500626e-16]], [1, 2], id='AB_baseline', edgecolor=(0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0), joinstyle='round', fill=False)
            for object_id, points in [('L_dot', [[-1.0, 0.0]]), ('R_dot', [[1.0, 0.0]]), ('A_dot', [[-3.0, 0.0]]), ('B_dot', [[3.0, 0.0]])]:
                c.point(points, id=object_id)
            c.line([[-1.0, 0.0], [-0.5, 0.8660254037844386]], id='L_radius')
            c.line([[1.0, 0.0], [0.5, 0.8660254037844386]], id='R_radius')
            c.line([[-3.0, 1.35], [-1.0, 1.35]], id='AL_dimension_line', linestyle=(0, [4, 3]))
            c.line([[-3.0, 0.0], [-3.0, 1.35]], id='AL_connector_0')
            c.line([[-1.0, 0.0], [-1.0, 1.35]], id='AL_connector_1')
            c.line([[3.0, 1.35], [1.0, 1.35]], id='BR_dimension_line', linestyle=(0, [4, 3]))
            c.line([[3.0, 0.0], [3.0, 1.35]], id='BR_connector_0')
            c.line([[1.0, 0.0], [1.0, 1.35]], id='BR_connector_1')
            c.text('A', (-3.0, 0.0), id='A_label', fontsize=18.0, fontstyle='italic', ha='right', rotation_mode='default', offset_pt=(-10, 0), annotation_clip=None)
            c.text('B', (3.0, 0.0), id='B_label', fontsize=18.0, fontstyle='italic', ha='left', rotation_mode='default', offset_pt=(10, 0), annotation_clip=None)
            c.text('L', (-1.0, 0.0), id='L_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -14), annotation_clip=None)
            c.text('R', (1.0, 0.0), id='R_label', fontsize=18.0, fontstyle='italic', rotation_mode='default', offset_pt=(0, -14), annotation_clip=None)
            c.text('1', (-0.75, 0.4330127018922193), id='L_radius_value', rotation_mode='default', offset_pt=(10, 0), annotation_clip=None)
            c.text('1', (0.75, 0.4330127018922193), id='R_radius_value', rotation_mode='default', offset_pt=(-10, 0), annotation_clip=None)
            c.text('2', (-2.0, 1.35), id='AL_value', rotation_mode='default', offset_pt=(0, 12), annotation_clip=None)
            c.text('2', (2.0, 1.35), id='BR_value', rotation_mode='default', offset_pt=(0, 12), annotation_clip=None)
            c.line([[-0.997886029411764, 1.017720588235293], [1.0049632352941176, 1.0106433823529404]], zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane100')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane100().draw(args.output, variant=args.variant))
