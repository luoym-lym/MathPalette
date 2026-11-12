"""Collected question Plane509; construction on the shared drawing protocol."""
from pathlib import Path
import sys
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane509:
    variants = ('C01', 'C02')

    def __init__(self):
        self.id = 'Plane509'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-promote15:Plane513'
        self.question = 'Six points are numbered as shown. Draw one triangle by connecting the three odd-numbered points, and a second triangle by connecting the three even-numbered points. Which choice shows the resulting two triangles? All choices preserve the source points’ relative positions and orientation.\nChoices:\nA: A\nB: B\nC: C\nD: D\nE: E'
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
        with Canvas(PLANE, xlim=[0.0, 8.0], ylim=[0.0, 8.0], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('source_dot3', [[3.172, 7.35]]), ('source_dot2', [[4.2875, 7.5915]]), ('source_dot4', [[5.15, 6.7865]]), ('source_dot5', [[4.7475, 5.4985]]), ('source_dot1', [[3.632, 5.2915]]), ('source_dot6', [[2.8155, 6.2805]])]:
                c.point(points, id=object_id, zorder=3, linewidths=[0])
            c.line([[0.7524, 4.384], [2.18, 3.9773], [1.0844, 2.8983], [0.7524, 4.384]], id='option0_0', solid_capstyle='projecting')
            c.line([[1.5575, 4.5583], [1.8895, 3.0477], [0.4951, 3.6121], [1.5575, 4.5583]], id='option0_1', solid_capstyle='projecting')
            for object_id, points in [('option0_dot0', [[0.7524, 4.384]]), ('option0_dot1', [[1.5575, 4.5583]]), ('option0_dot2', [[2.18, 3.9773]]), ('option0_dot3', [[1.8895, 3.0477]]), ('option0_dot4', [[1.0844, 2.8983]]), ('option0_dot5', [[0.4951, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[3.4024, 4.384], [4.5395, 3.0477], [3.7344, 2.8983], [3.4024, 4.384]], id='option1_0', solid_capstyle='projecting')
            c.line([[4.2075, 4.5583], [4.83, 3.9773], [3.1451, 3.6121], [4.2075, 4.5583]], id='option1_1', solid_capstyle='projecting')
            for object_id, points in [('option1_dot0', [[3.4024, 4.384]]), ('option1_dot1', [[4.2075, 4.5583]]), ('option1_dot2', [[4.83, 3.9773]]), ('option1_dot3', [[4.5395, 3.0477]]), ('option1_dot4', [[3.7344, 2.8983]]), ('option1_dot5', [[3.1451, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[6.0524, 4.384], [7.48, 3.9773], [5.7951, 3.6121], [6.0524, 4.384]], id='option2_0', solid_capstyle='projecting')
            c.line([[6.8575, 4.5583], [7.1895, 3.0477], [6.3844, 2.8983], [6.8575, 4.5583]], id='option2_1', solid_capstyle='projecting')
            for object_id, points in [('option2_dot0', [[6.0524, 4.384]]), ('option2_dot1', [[6.8575, 4.5583]]), ('option2_dot2', [[7.48, 3.9773]]), ('option2_dot3', [[7.1895, 3.0477]]), ('option2_dot4', [[6.3844, 2.8983]]), ('option2_dot5', [[5.7951, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[2.0524, 2.104], [3.1895, 0.7677], [1.7951, 1.3321], [2.0524, 2.104]], id='option3_0', solid_capstyle='projecting')
            c.line([[2.8575, 2.2783], [3.48, 1.6973], [2.3844, 0.6183], [2.8575, 2.2783]], id='option3_1', solid_capstyle='projecting')
            for object_id, points in [('option3_dot0', [[2.0524, 2.104]]), ('option3_dot1', [[2.8575, 2.2783]]), ('option3_dot2', [[3.48, 1.6973]]), ('option3_dot3', [[3.1895, 0.7677]]), ('option3_dot4', [[2.3844, 0.6183]]), ('option3_dot5', [[1.7951, 1.3321]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[4.7524, 2.104], [5.5575, 2.2783], [6.18, 1.6973], [4.7524, 2.104]], id='option4_0', solid_capstyle='projecting')
            c.line([[5.8895, 0.7677], [5.0844, 0.6183], [4.4951, 1.3321], [5.8895, 0.7677]], id='option4_1', solid_capstyle='projecting')
            for object_id, points in [('option4_dot0', [[4.7524, 2.104]]), ('option4_dot1', [[5.5575, 2.2783]]), ('option4_dot2', [[6.18, 1.6973]]), ('option4_dot3', [[5.8895, 0.7677]]), ('option4_dot4', [[5.0844, 0.6183]]), ('option4_dot5', [[4.4951, 1.3321]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            for object_id, text, anchor in [(None, '3', [2.96462, 7.58042]), (None, '2', [4.36198, 7.89242]), (None, '4', [5.4461, 6.87829]), (None, '5', [4.94152, 5.25672]), (None, '1', [3.53666, 4.99653]), (None, '6', [2.50794, 6.24168]), (None, '(A)', [1.35, 2.6]), (None, '(B)', [4, 2.6]), (None, '(C)', [6.65, 2.6]), (None, '(D)', [2.65, 0.31999999999999984]), (None, '(E)', [5.35, 0.31999999999999984])]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane509_C01.png'
        with Canvas(PLANE, xlim=(0.0, 8.0), ylim=(0.0, 8.0), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.point([[3.172, 7.35]], id='source_dot3', zorder=3, facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], linewidths=[0])
            c.point([[4.2875, 7.5915]], id='source_dot2', zorder=3, facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], linewidths=[0])
            c.point([[5.15, 6.7865]], id='source_dot4', zorder=3, facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], linewidths=[0])
            c.point([[4.7475, 5.4985]], id='source_dot5', zorder=3, facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], linewidths=[0])
            c.point([[3.632, 5.2915]], id='source_dot1', zorder=3, facecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], edgecolors=[[0.8627450980392157, 0.14901960784313725, 0.14901960784313725, 1.0]], linewidths=[0])
            c.point([[2.8155, 6.2805]], id='source_dot6', zorder=3, facecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], edgecolors=[[0.1450980392156863, 0.38823529411764707, 0.9215686274509803, 1.0]], linewidths=[0])
            c.line([[0.7524, 4.384], [2.18, 3.9773], [1.0844, 2.8983], [0.7524, 4.384]], id='option0_0', solid_capstyle='projecting')
            c.line([[1.5575, 4.5583], [1.8895, 3.0477], [0.4951, 3.6121], [1.5575, 4.5583]], id='option0_1', solid_capstyle='projecting')
            for object_id, points in [('option0_dot0', [[0.7524, 4.384]]), ('option0_dot1', [[1.5575, 4.5583]]), ('option0_dot2', [[2.18, 3.9773]]), ('option0_dot3', [[1.8895, 3.0477]]), ('option0_dot4', [[1.0844, 2.8983]]), ('option0_dot5', [[0.4951, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[3.4024, 4.384], [4.5395, 3.0477], [3.7344, 2.8983], [3.4024, 4.384]], id='option1_0', solid_capstyle='projecting')
            c.line([[4.2075, 4.5583], [4.83, 3.9773], [3.1451, 3.6121], [4.2075, 4.5583]], id='option1_1', solid_capstyle='projecting')
            for object_id, points in [('option1_dot0', [[3.4024, 4.384]]), ('option1_dot1', [[4.2075, 4.5583]]), ('option1_dot2', [[4.83, 3.9773]]), ('option1_dot3', [[4.5395, 3.0477]]), ('option1_dot4', [[3.7344, 2.8983]]), ('option1_dot5', [[3.1451, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[6.0524, 4.384], [7.48, 3.9773], [5.7951, 3.6121], [6.0524, 4.384]], id='option2_0', color='#DC2626', linewidth=1.5, solid_capstyle='projecting')
            c.line([[6.8575, 4.5583], [7.1895, 3.0477], [6.3844, 2.8983], [6.8575, 4.5583]], id='option2_1', color='#2563EB', linewidth=1.5, solid_capstyle='projecting')
            for object_id, points in [('option2_dot0', [[6.0524, 4.384]]), ('option2_dot1', [[6.8575, 4.5583]]), ('option2_dot2', [[7.48, 3.9773]]), ('option2_dot3', [[7.1895, 3.0477]]), ('option2_dot4', [[6.3844, 2.8983]]), ('option2_dot5', [[5.7951, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[2.0524, 2.104], [3.1895, 0.7677], [1.7951, 1.3321], [2.0524, 2.104]], id='option3_0', solid_capstyle='projecting')
            c.line([[2.8575, 2.2783], [3.48, 1.6973], [2.3844, 0.6183], [2.8575, 2.2783]], id='option3_1', solid_capstyle='projecting')
            for object_id, points in [('option3_dot0', [[2.0524, 2.104]]), ('option3_dot1', [[2.8575, 2.2783]]), ('option3_dot2', [[3.48, 1.6973]]), ('option3_dot3', [[3.1895, 0.7677]]), ('option3_dot4', [[2.3844, 0.6183]]), ('option3_dot5', [[1.7951, 1.3321]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[4.7524, 2.104], [5.5575, 2.2783], [6.18, 1.6973], [4.7524, 2.104]], id='option4_0', solid_capstyle='projecting')
            c.line([[5.8895, 0.7677], [5.0844, 0.6183], [4.4951, 1.3321], [5.8895, 0.7677]], id='option4_1', solid_capstyle='projecting')
            for object_id, points in [('option4_dot0', [[4.7524, 2.104]]), ('option4_dot1', [[5.5575, 2.2783]]), ('option4_dot2', [[6.18, 1.6973]]), ('option4_dot3', [[5.8895, 0.7677]]), ('option4_dot4', [[5.0844, 0.6183]]), ('option4_dot5', [[4.4951, 1.3321]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            for object_id, text, anchor in [(None, '3', (2.96462, 7.58042)), (None, '2', (4.36198, 7.89242)), (None, '4', (5.4461, 6.87829)), (None, '5', (4.94152, 5.25672)), (None, '1', (3.53666, 4.99653)), (None, '6', (2.50794, 6.24168)), (None, '(A)', (1.35, 2.6)), (None, '(B)', (4, 2.6)), (None, '(C)', (6.65, 2.6)), (None, '(D)', (2.65, 0.31999999999999984)), (None, '(E)', (5.35, 0.31999999999999984))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane509_C02.png'
        with Canvas(PLANE, xlim=(0.0, 8.0), ylim=(0.0, 8.0), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            for object_id, points in [('source_dot3', [[3.172, 7.35]]), ('source_dot2', [[4.2875, 7.5915]]), ('source_dot4', [[5.15, 6.7865]]), ('source_dot5', [[4.7475, 5.4985]]), ('source_dot1', [[3.632, 5.2915]]), ('source_dot6', [[2.8155, 6.2805]])]:
                c.point(points, id=object_id, zorder=3, linewidths=[0])
            c.line([[0.7524, 4.384], [2.18, 3.9773], [1.0844, 2.8983], [0.7524, 4.384]], id='option0_0', color='#DC2626', linewidth=1.5, solid_capstyle='projecting')
            c.line([[1.5575, 4.5583], [1.8895, 3.0477], [0.4951, 3.6121], [1.5575, 4.5583]], id='option0_1', color='#2563EB', linewidth=1.5, solid_capstyle='projecting')
            for object_id, points in [('option0_dot0', [[0.7524, 4.384]]), ('option0_dot1', [[1.5575, 4.5583]]), ('option0_dot2', [[2.18, 3.9773]]), ('option0_dot3', [[1.8895, 3.0477]]), ('option0_dot4', [[1.0844, 2.8983]]), ('option0_dot5', [[0.4951, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[3.4024, 4.384], [4.5395, 3.0477], [3.7344, 2.8983], [3.4024, 4.384]], id='option1_0', solid_capstyle='projecting')
            c.line([[4.2075, 4.5583], [4.83, 3.9773], [3.1451, 3.6121], [4.2075, 4.5583]], id='option1_1', solid_capstyle='projecting')
            for object_id, points in [('option1_dot0', [[3.4024, 4.384]]), ('option1_dot1', [[4.2075, 4.5583]]), ('option1_dot2', [[4.83, 3.9773]]), ('option1_dot3', [[4.5395, 3.0477]]), ('option1_dot4', [[3.7344, 2.8983]]), ('option1_dot5', [[3.1451, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[6.0524, 4.384], [7.48, 3.9773], [5.7951, 3.6121], [6.0524, 4.384]], id='option2_0', solid_capstyle='projecting')
            c.line([[6.8575, 4.5583], [7.1895, 3.0477], [6.3844, 2.8983], [6.8575, 4.5583]], id='option2_1', solid_capstyle='projecting')
            for object_id, points in [('option2_dot0', [[6.0524, 4.384]]), ('option2_dot1', [[6.8575, 4.5583]]), ('option2_dot2', [[7.48, 3.9773]]), ('option2_dot3', [[7.1895, 3.0477]]), ('option2_dot4', [[6.3844, 2.8983]]), ('option2_dot5', [[5.7951, 3.6121]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[2.0524, 2.104], [3.1895, 0.7677], [1.7951, 1.3321], [2.0524, 2.104]], id='option3_0', solid_capstyle='projecting')
            c.line([[2.8575, 2.2783], [3.48, 1.6973], [2.3844, 0.6183], [2.8575, 2.2783]], id='option3_1', solid_capstyle='projecting')
            for object_id, points in [('option3_dot0', [[2.0524, 2.104]]), ('option3_dot1', [[2.8575, 2.2783]]), ('option3_dot2', [[3.48, 1.6973]]), ('option3_dot3', [[3.1895, 0.7677]]), ('option3_dot4', [[2.3844, 0.6183]]), ('option3_dot5', [[1.7951, 1.3321]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            c.line([[4.7524, 2.104], [5.5575, 2.2783], [6.18, 1.6973], [4.7524, 2.104]], id='option4_0', solid_capstyle='projecting')
            c.line([[5.8895, 0.7677], [5.0844, 0.6183], [4.4951, 1.3321], [5.8895, 0.7677]], id='option4_1', solid_capstyle='projecting')
            for object_id, points in [('option4_dot0', [[4.7524, 2.104]]), ('option4_dot1', [[5.5575, 2.2783]]), ('option4_dot2', [[6.18, 1.6973]]), ('option4_dot3', [[5.8895, 0.7677]]), ('option4_dot4', [[5.0844, 0.6183]]), ('option4_dot5', [[4.4951, 1.3321]])]:
                c.point(points, id=object_id, zorder=3, s=[12], linewidths=[0])
            for object_id, text, anchor in [(None, '3', (2.96462, 7.58042)), (None, '2', (4.36198, 7.89242)), (None, '4', (5.4461, 6.87829)), (None, '5', (4.94152, 5.25672)), (None, '1', (3.53666, 4.99653)), (None, '6', (2.50794, 6.24168)), (None, '(A)', (1.35, 2.6)), (None, '(B)', (4, 2.6)), (None, '(C)', (6.65, 2.6)), (None, '(D)', (2.65, 0.31999999999999984)), (None, '(E)', (5.35, 0.31999999999999984))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            for object_id, points in [(None, [[3.172, 7.35], [5.15, 6.7865]]), (None, [[5.15, 6.7865], [3.632, 5.2915]]), (None, [[3.632, 5.2915], [3.172, 7.35]])]:
                c.line(points, id=object_id, zorder=9, color='#DC2626', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            for object_id, points in [(None, [[4.2875, 7.5915], [4.7475, 5.4985]]), (None, [[4.7475, 5.4985], [2.8155, 6.2805]]), (None, [[2.8155, 6.2805], [4.2875, 7.5915]])]:
                c.line(points, id=object_id, zorder=9, color='#2563EB', linestyle=(0.0, [3.7, 1.6]), solid_capstyle='butt')
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane509')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02'))
    args = parser.parse_args()
    print(Plane509().draw(args.output, variant=args.variant))
