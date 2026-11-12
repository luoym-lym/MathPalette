"""Frozen question Plane540; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane540:

    def __init__(self):
        self.id = 'Plane540'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane180/extension_01'
        self.question = 'A strip of paper is folded three times as shown. Determine $\\beta$ if $\\alpha=72^{\\circ}$.\nChoices:\nA:$72^{\\circ}$\nB:$108^{\\circ}$\nC:$126^{\\circ}$\nD:$144^{\\circ}$\nE:$36^{\\circ}$'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': '$72^{\\circ}$', 'B': '$108^{\\circ}$', 'C': '$126^{\\circ}$', 'D': '$144^{\\circ}$', 'E': '$36^{\\circ}$'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane540.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-7.7489771748492675, 8.142495693367787], ylim=[-8.292958656330748, 7.598514211886305], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-4.831884232758545, -0.22526087989656407], [-5.516644924491056, -0.002768643946602367], [-3.168115767241455, 7.225260879896564], [-2.4833550755089444, 7.002768643946602], [-4.831884232758545, -0.22526087989656407]], [1, 2, 2, 2, 79], id='s0_whole_strip_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, points in [('s0_whole_strip_edge0', [[-4.831884232758545, -0.22526087989656407], [-5.516644924491056, -0.002768643946602367]]), ('s0_whole_strip_edge1', [[-5.516644924491056, -0.002768643946602367], [-3.168115767241455, 7.225260879896564]]), ('s0_whole_strip_edge2', [[-3.168115767241455, 7.225260879896564], [-2.4833550755089444, 7.002768643946602]]), ('s0_whole_strip_edge3', [[-2.4833550755089444, 7.002768643946602], [-4.831884232758545, -0.22526087989656407]])]:
                c.line(points, id=object_id)
            c.line([[-4.378526400725776, 3.5], [-3.621473599274224, 3.5]], id='s0_next_crease', zorder=80, linestyle=(0.0, [4.0, 3.0]))
            c.path([[-3.835680145501991, 3.5], [-3.835680145501991, 3.614620060228482], [-3.871982573897757, 3.726347446461615], [-3.9393545549169335, 3.8190770230827367], [-4.00672653593611, 3.911806599703859], [-4.101767527350385, 3.980857921870122], [-4.210777682528827, 4.0162774683770035]], [1, 4, 4, 4, 4, 4, 4], id='alpha_arc', zorder=90, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[3.168115767241455, -0.22526087989656407], [2.4833550755089444, -0.002768643946602367], [3.621473599274224, 3.5], [4.378526400725776, 3.5], [3.168115767241455, -0.22526087989656407]], [1, 2, 2, 2, 79], id='s1_lower_after_first_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.line([[3.168115767241455, -0.22526087989656407], [2.4833550755089444, -0.002768643946602367]], id='s1_lower_after_first_edge0')
            c.line([[2.4833550755089444, -0.002768643946602367], [3.621473599274224, 3.5]], id='s1_lower_after_first_edge1')
            c.line([[3.621473599274224, 3.5], [4.378526400725776, 3.5]], id='s1_lower_after_first_edge2', linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.378526400725776, 3.5], [3.168115767241455, -0.22526087989656407]], id='s1_lower_after_first_edge3')
            c.path([[3.621473599274224, 3.5], [4.831884232758545, -0.22526087989656407], [5.516644924491056, -0.002768643946602367], [4.378526400725776, 3.5], [3.621473599274224, 3.5]], [1, 2, 2, 2, 79], id='s1_upper_after_first_fill', zorder=11, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, points in [('s1_upper_after_first_edge0', [[3.621473599274224, 3.5], [4.831884232758545, -0.22526087989656407]]), ('s1_upper_after_first_edge1', [[4.831884232758545, -0.22526087989656407], [5.516644924491056, -0.002768643946602367]]), ('s1_upper_after_first_edge2', [[5.516644924491056, -0.002768643946602367], [4.378526400725776, 3.5]])]:
                c.line(points, id=object_id, zorder=12)
            c.line([[4.378526400725776, 3.5], [3.621473599274224, 3.5]], id='s1_upper_after_first_edge3', zorder=12, linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.378526400725776, 3.5], [4.0, 2.335015528100076]], id='s1_next_crease', zorder=80, linestyle=(0.0, [4.0, 3.0]))
            c.path([[3.168115767241455, -7.925260879896564], [2.4833550755089444, -7.7027686439466025], [3.621473599274224, -4.2], [4.378526400725776, -4.2], [3.168115767241455, -7.925260879896564]], [1, 2, 2, 2, 79], id='s2_lower_after_first_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.line([[3.168115767241455, -7.925260879896564], [2.4833550755089444, -7.7027686439466025]], id='s2_lower_after_first_edge0')
            c.line([[2.4833550755089444, -7.7027686439466025], [3.621473599274224, -4.2]], id='s2_lower_after_first_edge1')
            c.line([[3.621473599274224, -4.2], [4.378526400725776, -4.2]], id='s2_lower_after_first_edge2', linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.378526400725776, -4.2], [3.168115767241455, -7.925260879896564]], id='s2_lower_after_first_edge3')
            c.path([[4.0, -5.364984471899924], [1.8220988039330002, -6.94732231263634], [1.3988934222824194, -6.364830076686378], [4.378526400725776, -4.2], [4.0, -5.364984471899924]], [1, 2, 2, 2, 79], id='s2_upper_folded_fill', zorder=11, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, points in [('s2_upper_folded_edge0', [[4.0, -5.364984471899924], [1.8220988039330002, -6.94732231263634]]), ('s2_upper_folded_edge1', [[1.8220988039330002, -6.94732231263634], [1.3988934222824194, -6.364830076686378]]), ('s2_upper_folded_edge2', [[1.3988934222824194, -6.364830076686378], [4.378526400725776, -4.2]])]:
                c.line(points, id=object_id, zorder=12)
            c.line([[4.378526400725776, -4.2], [4.0, -5.364984471899924]], id='s2_upper_folded_edge3', zorder=12, linestyle=(0.0, [4.0, 3.0]))
            c.path([[3.621473599274224, -4.2], [4.0, -5.364984471899924], [4.378526400725776, -4.2], [3.621473599274224, -4.2]], [1, 2, 2, 79], id='s2_upper_fixed_fill', zorder=21, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.line([[3.621473599274224, -4.2], [4.0, -5.364984471899924]], id='s2_upper_fixed_edge0', zorder=22)
            c.line([[4.0, -5.364984471899924], [4.378526400725776, -4.2]], id='s2_upper_fixed_edge1', zorder=22, linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.378526400725776, -4.2], [3.621473599274224, -4.2]], id='s2_upper_fixed_edge2', zorder=22, linestyle=(0.0, [4.0, 3.0]))
            c.line([[3.621473599274224, -4.2], [4.0, -5.364984471899924]], id='s2_next_crease', zorder=80, linestyle=(0.0, [4.0, 3.0]))
            c.path([[-4.0, -5.364984471899924], [-6.177901196066999, -6.94732231263634], [-6.60110657771758, -6.364830076686378], [-3.6214735992742235, -4.2], [-4.0, -5.364984471899924]], [1, 2, 2, 2, 79], id='s3_upper_folded_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, points in [('s3_upper_folded_edge0', [[-4.0, -5.364984471899924], [-6.177901196066999, -6.94732231263634]]), ('s3_upper_folded_edge1', [[-6.177901196066999, -6.94732231263634], [-6.60110657771758, -6.364830076686378]]), ('s3_upper_folded_edge2', [[-6.60110657771758, -6.364830076686378], [-3.6214735992742235, -4.2]])]:
                c.line(points, id=object_id)
            c.line([[-3.6214735992742235, -4.2], [-4.0, -5.364984471899924]], id='s3_upper_folded_edge3', linestyle=(0.0, [4.0, 3.0]))
            c.path([[-1.822098803933002, -6.9473223126363415], [-1.3988934222824208, -6.36483007668638], [-4.378526400725776, -4.2], [-4.0, -5.364984471899924], [-1.822098803933002, -6.9473223126363415]], [1, 2, 2, 2, 79], id='s3_lower_folded_fill', zorder=11, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.line([[-1.822098803933002, -6.9473223126363415], [-1.3988934222824208, -6.36483007668638]], id='s3_lower_folded_edge0', zorder=12)
            c.line([[-1.3988934222824208, -6.36483007668638], [-4.378526400725776, -4.2]], id='s3_lower_folded_edge1', zorder=12)
            c.line([[-4.378526400725776, -4.2], [-4.0, -5.364984471899924]], id='s3_lower_folded_edge2', zorder=12, linestyle=(0.0, [4.0, 3.0]))
            c.line([[-4.0, -5.364984471899924], [-1.822098803933002, -6.9473223126363415]], id='s3_lower_folded_edge3', zorder=12)
            c.path([[-4.378526400725776, -4.2], [-4.0, -5.364984471899924], [-3.621473599274224, -4.2], [-4.378526400725776, -4.2]], [1, 2, 2, 79], id='s3_upper_fixed_fill', zorder=21, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.line([[-4.378526400725776, -4.2], [-4.0, -5.364984471899924]], id='s3_upper_fixed_edge0', zorder=22)
            c.line([[-4.0, -5.364984471899924], [-3.621473599274224, -4.2]], id='s3_upper_fixed_edge1', zorder=22, linestyle=(0.0, [4.0, 3.0]))
            c.line([[-3.621473599274224, -4.2], [-4.378526400725776, -4.2]], id='s3_upper_fixed_edge2', zorder=22, linestyle=(0.0, [4.0, 3.0]))
            c.path([[-4.378526400725776, -4.2], [-3.621473599274224, -4.2], [-4.0, -5.364984471899924], [-4.378526400725776, -4.2]], [1, 2, 2, 79], id='s3_lower_fixed_fill', zorder=31, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            c.line([[-4.378526400725776, -4.2], [-3.621473599274224, -4.2]], id='s3_lower_fixed_edge0', zorder=32, linestyle=(0.0, [4.0, 3.0]))
            c.line([[-3.621473599274224, -4.2], [-4.0, -5.364984471899924]], id='s3_lower_fixed_edge1', zorder=32)
            c.line([[-4.0, -5.364984471899924], [-4.378526400725776, -4.2]], id='s3_lower_fixed_edge2', zorder=32, linestyle=(0.0, [4.0, 3.0]))
            c.path([[-4.465005483797599, -5.702830731634587], [-4.411692427823901, -5.776209858001853], [-4.341759634501864, -5.835938106058713], [-4.260943927554953, -5.877115765467049], [-4.180128220608042, -5.918293424875383], [-4.090701588319489, -5.939762859783933], [-4.000000000000001, -5.939762859783933], [-3.909298411680513, -5.939762859783933], [-3.8198717793919603, -5.918293424875383], [-3.7390560724450492, -5.877115765467049], [-3.6582403654981377, -5.835938106058713], [-3.5883075721761015, -5.776209858001854], [-3.5349945162024032, -5.702830731634588]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='beta_arc', zorder=90, facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[-0.65, 3.075], [-0.65, 2.925], [0.44000000000000006, 2.925], [0.44000000000000006, 2.83], [0.65, 3.0], [0.44000000000000006, 3.17], [0.44000000000000006, 3.075], [-0.65, 3.075]], [1, 2, 2, 2, 2, 2, 2, 79], id='arrow_01_fill', zorder=80, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, points in [('arrow_01_edge0', [[-0.65, 3.075], [-0.65, 2.925]]), ('arrow_01_edge1', [[-0.65, 2.925], [0.44000000000000006, 2.925]]), ('arrow_01_edge2', [[0.44000000000000006, 2.925], [0.44000000000000006, 2.83]]), ('arrow_01_edge3', [[0.44000000000000006, 2.83], [0.65, 3.0]]), ('arrow_01_edge4', [[0.65, 3.0], [0.44000000000000006, 3.17]]), ('arrow_01_edge5', [[0.44000000000000006, 3.17], [0.44000000000000006, 3.075]]), ('arrow_01_edge6', [[0.44000000000000006, 3.075], [-0.65, 3.075]])]:
                c.line(points, id=object_id, zorder=81)
            c.path([[6.875, -0.2], [6.725, -0.2], [6.725, -1.24], [6.63, -1.24], [6.8, -1.45], [6.97, -1.24], [6.875, -1.24], [6.875, -0.2]], [1, 2, 2, 2, 2, 2, 2, 79], id='arrow_12_fill', zorder=80, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, points in [('arrow_12_edge0', [[6.875, -0.2], [6.725, -0.2]]), ('arrow_12_edge1', [[6.725, -0.2], [6.725, -1.24]]), ('arrow_12_edge2', [[6.725, -1.24], [6.63, -1.24]]), ('arrow_12_edge3', [[6.63, -1.24], [6.8, -1.45]]), ('arrow_12_edge4', [[6.8, -1.45], [6.97, -1.24]]), ('arrow_12_edge5', [[6.97, -1.24], [6.875, -1.24]]), ('arrow_12_edge6', [[6.875, -1.24], [6.875, -0.2]])]:
                c.line(points, id=object_id, zorder=81)
            c.path([[0.65, -5.425], [0.65, -5.2749999999999995], [-0.44000000000000006, -5.2749999999999995], [-0.44000000000000006, -5.18], [-0.65, -5.35], [-0.44000000000000006, -5.52], [-0.44000000000000006, -5.425], [0.65, -5.425]], [1, 2, 2, 2, 2, 2, 2, 79], id='arrow_23_fill', zorder=80, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], capstyle='butt')
            for object_id, points in [('arrow_23_edge0', [[0.65, -5.425], [0.65, -5.2749999999999995]]), ('arrow_23_edge1', [[0.65, -5.2749999999999995], [-0.44000000000000006, -5.2749999999999995]]), ('arrow_23_edge2', [[-0.44000000000000006, -5.2749999999999995], [-0.44000000000000006, -5.18]]), ('arrow_23_edge3', [[-0.44000000000000006, -5.18], [-0.65, -5.35]]), ('arrow_23_edge4', [[-0.65, -5.35], [-0.44000000000000006, -5.52]]), ('arrow_23_edge5', [[-0.44000000000000006, -5.52], [-0.44000000000000006, -5.425]]), ('arrow_23_edge6', [[-0.44000000000000006, -5.425], [0.65, -5.425]])]:
                c.line(points, id=object_id, zorder=81)
            c.text('A', [-4.998526400725776, 3.5], id='s0_A_label', zorder=100, fontsize=18.0, fontstyle='italic', rotation_mode='default')
            c.text('B', [-3.001473599274224, 3.5], id='s0_B_label', zorder=100, fontsize=18.0, fontstyle='italic', rotation_mode='default')
            c.text('α', [-3.85266535438206, 3.8820604139901076], id='alpha_label', zorder=100, rotation_mode='default')
            for object_id, text, anchor in [('s1_A_label', 'A', [3.441473599274224, 3.92]), ('s1_B_label', 'B', [4.558526400725776, 3.92]), ('s2_A_label', 'A', [3.441473599274224, -3.45]), ('s2_B_label', 'B', [4.558526400725776, -3.45])]:
                c.text(text, anchor, id=object_id, zorder=100, fontsize=18.0, fontstyle='italic', rotation_mode='default')
            c.text('β', [-4.000000000000001, -6.134984471899925], id='beta_label', zorder=100, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane540().draw(sys.argv[1] if len(sys.argv) > 1 else None))
