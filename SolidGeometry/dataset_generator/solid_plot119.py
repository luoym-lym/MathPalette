"""Frozen question Solid119; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid119:

    def __init__(self):
        self.id = 'Solid119'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:640'
        self.question = 'Four bricks have the same size, as shown. Which of the cubes shown below can be made with these four bricks?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('A_edge0', [[0.0, 0.0], [0.0, 1.0]]),
         ('A_edge1', [[0.0, 0.0], [1.0, 0.0]]),
         ('A_edge2', [[0.0, 1.0], [0.0, 2.0]]),
         ('A_edge3', [[0.0, 1.0], [1.0, 1.0]]),
         ('A_edge4', [[0.0, 2.0], [0.35, 2.35]]),
         ('A_edge5', [[0.0, 2.0], [1.0, 2.0]]),
         ('A_edge6', [[0.35, 2.35], [0.7, 2.7]]),
         ('A_edge7', [[0.35, 2.35], [1.35, 2.35]]),
         ('A_edge8', [[0.7, 2.7], [1.7, 2.7]]),
         ('A_edge9', [[1.0, 0.0], [2.0, 0.0]]),
         ('A_edge10', [[1.0, 1.0], [2.0, 1.0]]),
         ('A_edge11', [[1.0, 2.0], [2.0, 2.0]]),
         ('A_edge12', [[1.35, 2.35], [1.7, 2.7]]),
         ('A_edge13', [[1.35, 2.35], [2.35, 2.35]]),
         ('A_edge14', [[1.7, 2.7], [2.7, 2.7]]),
         ('A_edge15', [[2.0, 0.0], [2.0, 1.0]]),
         ('A_edge16', [[2.0, 0.0], [2.35, 0.35]]),
         ('A_edge17', [[2.0, 1.0], [2.0, 2.0]]),
         ('A_edge18', [[2.0, 1.0], [2.35, 1.35]]),
         ('A_edge19', [[2.0, 2.0], [2.35, 2.35]]),
         ('A_edge20', [[2.35, 0.35], [2.35, 1.35]]),
         ('A_edge21', [[2.35, 0.35], [2.7, 0.7]]),
         ('A_edge22', [[2.35, 1.35], [2.35, 2.35]]),
         ('A_edge23', [[2.35, 2.35], [2.7, 2.7]]),
         ('A_edge24', [[2.7, 0.7], [2.7, 1.7]]),
         ('A_edge25', [[2.7, 1.7], [2.7, 2.7]])]
        self._geometry_02 = [('B_edge0', [[6.0, 0.0], [6.0, 1.0]]),
         ('B_edge1', [[6.0, 0.0], [7.0, 0.0]]),
         ('B_edge2', [[6.0, 1.0], [6.0, 2.0]]),
         ('B_edge3', [[6.0, 1.0], [7.0, 1.0]]),
         ('B_edge4', [[6.0, 2.0], [6.35, 2.35]]),
         ('B_edge5', [[6.0, 2.0], [7.0, 2.0]]),
         ('B_edge6', [[6.35, 2.35], [6.7, 2.7]]),
         ('B_edge7', [[6.7, 2.7], [7.7, 2.7]]),
         ('B_edge8', [[7.0, 0.0], [7.0, 1.0]]),
         ('B_edge9', [[7.0, 0.0], [8.0, 0.0]]),
         ('B_edge10', [[7.0, 1.0], [7.0, 2.0]]),
         ('B_edge11', [[7.0, 1.0], [8.0, 1.0]]),
         ('B_edge12', [[7.0, 2.0], [7.35, 2.35]]),
         ('B_edge13', [[7.0, 2.0], [8.0, 2.0]]),
         ('B_edge14', [[7.35, 2.35], [7.7, 2.7]]),
         ('B_edge15', [[7.7, 2.7], [8.7, 2.7]]),
         ('B_edge16', [[8.0, 0.0], [8.0, 1.0]]),
         ('B_edge17', [[8.0, 0.0], [8.35, 0.35]]),
         ('B_edge18', [[8.0, 1.0], [8.0, 2.0]]),
         ('B_edge19', [[8.0, 1.0], [8.35, 1.35]]),
         ('B_edge20', [[8.0, 2.0], [8.35, 2.35]]),
         ('B_edge21', [[8.35, 0.35], [8.7, 0.7]]),
         ('B_edge22', [[8.35, 1.35], [8.7, 1.7]]),
         ('B_edge23', [[8.35, 2.35], [8.7, 2.7]]),
         ('B_edge24', [[8.7, 0.7], [8.7, 1.7]]),
         ('B_edge25', [[8.7, 1.7], [8.7, 2.7]])]
        self._geometry_03 = [('C_edge0', [[12.0, 0.0], [12.0, 1.0]]),
         ('C_edge1', [[12.0, 0.0], [13.0, 0.0]]),
         ('C_edge2', [[12.0, 1.0], [12.0, 2.0]]),
         ('C_edge3', [[12.0, 2.0], [12.35, 2.35]]),
         ('C_edge4', [[12.0, 2.0], [13.0, 2.0]]),
         ('C_edge5', [[12.35, 2.35], [12.7, 2.7]]),
         ('C_edge6', [[12.35, 2.35], [13.35, 2.35]]),
         ('C_edge7', [[12.7, 2.7], [13.7, 2.7]]),
         ('C_edge8', [[13.0, 0.0], [13.0, 1.0]]),
         ('C_edge9', [[13.0, 0.0], [14.0, 0.0]]),
         ('C_edge10', [[13.0, 1.0], [13.0, 2.0]]),
         ('C_edge11', [[13.0, 2.0], [13.35, 2.35]]),
         ('C_edge12', [[13.0, 2.0], [14.0, 2.0]]),
         ('C_edge13', [[13.35, 2.35], [14.35, 2.35]]),
         ('C_edge14', [[13.7, 2.7], [14.7, 2.7]]),
         ('C_edge15', [[14.0, 0.0], [14.0, 1.0]]),
         ('C_edge16', [[14.0, 0.0], [14.35, 0.35]]),
         ('C_edge17', [[14.0, 1.0], [14.0, 2.0]]),
         ('C_edge18', [[14.0, 2.0], [14.35, 2.35]]),
         ('C_edge19', [[14.35, 0.35], [14.35, 1.35]]),
         ('C_edge20', [[14.35, 0.35], [14.7, 0.7]]),
         ('C_edge21', [[14.35, 1.35], [14.35, 2.35]]),
         ('C_edge22', [[14.35, 1.35], [14.7, 1.7]]),
         ('C_edge23', [[14.35, 2.35], [14.7, 2.7]]),
         ('C_edge24', [[14.7, 0.7], [14.7, 1.7]]),
         ('C_edge25', [[14.7, 1.7], [14.7, 2.7]])]
        self._geometry_04 = [('D_edge0', [[18.0, 0.0], [18.0, 1.0]]),
         ('D_edge1', [[18.0, 0.0], [19.0, 0.0]]),
         ('D_edge2', [[18.0, 1.0], [18.0, 2.0]]),
         ('D_edge3', [[18.0, 2.0], [18.35, 2.35]]),
         ('D_edge4', [[18.0, 2.0], [19.0, 2.0]]),
         ('D_edge5', [[18.35, 2.35], [18.7, 2.7]]),
         ('D_edge6', [[18.35, 2.35], [19.35, 2.35]]),
         ('D_edge7', [[18.7, 2.7], [19.7, 2.7]]),
         ('D_edge8', [[19.0, 0.0], [19.0, 1.0]]),
         ('D_edge9', [[19.0, 0.0], [20.0, 0.0]]),
         ('D_edge10', [[19.0, 1.0], [19.0, 2.0]]),
         ('D_edge11', [[19.0, 2.0], [19.35, 2.35]]),
         ('D_edge12', [[19.0, 2.0], [20.0, 2.0]]),
         ('D_edge13', [[19.35, 2.35], [20.35, 2.35]]),
         ('D_edge14', [[19.7, 2.7], [20.7, 2.7]]),
         ('D_edge15', [[20.0, 0.0], [20.0, 1.0]]),
         ('D_edge16', [[20.0, 0.0], [20.35, 0.35]]),
         ('D_edge17', [[20.0, 1.0], [20.0, 2.0]]),
         ('D_edge18', [[20.0, 2.0], [20.35, 2.35]]),
         ('D_edge19', [[20.35, 0.35], [20.35, 1.35]]),
         ('D_edge20', [[20.35, 0.35], [20.7, 0.7]]),
         ('D_edge21', [[20.35, 1.35], [20.35, 2.35]]),
         ('D_edge22', [[20.35, 1.35], [20.7, 1.7]]),
         ('D_edge23', [[20.35, 2.35], [20.7, 2.7]]),
         ('D_edge24', [[20.7, 0.7], [20.7, 1.7]]),
         ('D_edge25', [[20.7, 1.7], [20.7, 2.7]])]
        self._geometry_05 = [('E_edge0', [[24.0, 0.0], [24.0, 1.0]]),
         ('E_edge1', [[24.0, 0.0], [25.0, 0.0]]),
         ('E_edge2', [[24.0, 1.0], [24.0, 2.0]]),
         ('E_edge3', [[24.0, 1.0], [25.0, 1.0]]),
         ('E_edge4', [[24.0, 2.0], [24.35, 2.35]]),
         ('E_edge5', [[24.0, 2.0], [25.0, 2.0]]),
         ('E_edge6', [[24.35, 2.35], [24.7, 2.7]]),
         ('E_edge7', [[24.7, 2.7], [25.7, 2.7]]),
         ('E_edge8', [[25.0, 0.0], [25.0, 1.0]]),
         ('E_edge9', [[25.0, 0.0], [26.0, 0.0]]),
         ('E_edge10', [[25.0, 1.0], [25.0, 2.0]]),
         ('E_edge11', [[25.0, 1.0], [26.0, 1.0]]),
         ('E_edge12', [[25.0, 2.0], [25.35, 2.35]]),
         ('E_edge13', [[25.0, 2.0], [26.0, 2.0]]),
         ('E_edge14', [[25.35, 2.35], [25.7, 2.7]]),
         ('E_edge15', [[25.7, 2.7], [26.7, 2.7]]),
         ('E_edge16', [[26.0, 0.0], [26.0, 1.0]]),
         ('E_edge17', [[26.0, 0.0], [26.35, 0.35]]),
         ('E_edge18', [[26.0, 1.0], [26.0, 2.0]]),
         ('E_edge19', [[26.0, 1.0], [26.35, 1.35]]),
         ('E_edge20', [[26.0, 2.0], [26.35, 2.35]]),
         ('E_edge21', [[26.35, 0.35], [26.7, 0.7]]),
         ('E_edge22', [[26.35, 1.35], [26.7, 1.7]]),
         ('E_edge23', [[26.35, 2.35], [26.7, 2.7]]),
         ('E_edge24', [[26.7, 0.7], [26.7, 1.7]]),
         ('E_edge25', [[26.7, 1.7], [26.7, 2.7]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid119.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.6581721375345975, 27.406006795109725], ylim=[-11.16067676688808, 16.90350216575624], axes_position=[0.05, 0.05000000000000006, 0.9, 0.8999999999999999], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('brick0_front_0_fill', [[6.0, 6.0], [8.0, 6.0], [8.0, 7.0], [6.0, 7.0], [6.0, 6.0]], [1, 2, 2, 2, 79]), ('brick0_right_0_fill', [[8.0, 6.0], [8.35, 6.35], [8.35, 7.35], [8.0, 7.0], [8.0, 6.0]], [1, 2, 2, 2, 79]), ('brick0_top_0_fill', [[6.0, 7.0], [8.0, 7.0], [8.35, 7.35], [6.35, 7.35], [6.0, 7.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('brick0_edge0', [[6.0, 6.0], [6.0, 7.0]]), ('brick0_edge1', [[6.0, 6.0], [7.0, 6.0]]), ('brick0_edge2', [[6.0, 7.0], [6.35, 7.35]]), ('brick0_edge3', [[6.0, 7.0], [7.0, 7.0]]), ('brick0_edge4', [[6.35, 7.35], [7.35, 7.35]]), ('brick0_edge5', [[7.0, 6.0], [8.0, 6.0]]), ('brick0_edge6', [[7.0, 7.0], [8.0, 7.0]]), ('brick0_edge7', [[7.35, 7.35], [8.35, 7.35]]), ('brick0_edge8', [[8.0, 6.0], [8.0, 7.0]]), ('brick0_edge9', [[8.0, 6.0], [8.35, 6.35]]), ('brick0_edge10', [[8.0, 7.0], [8.35, 7.35]]), ('brick0_edge11', [[8.35, 6.35], [8.35, 7.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('brick1_front_0_fill', [[9.5, 6.0], [11.5, 6.0], [11.5, 7.0], [9.5, 7.0], [9.5, 6.0]], [1, 2, 2, 2, 79]), ('brick1_right_0_fill', [[11.5, 6.0], [11.85, 6.35], [11.85, 7.35], [11.5, 7.0], [11.5, 6.0]], [1, 2, 2, 2, 79]), ('brick1_top_0_fill', [[9.5, 7.0], [11.5, 7.0], [11.85, 7.35], [9.85, 7.35], [9.5, 7.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('brick1_edge0', [[9.5, 6.0], [9.5, 7.0]]), ('brick1_edge1', [[9.5, 6.0], [10.5, 6.0]]), ('brick1_edge2', [[9.5, 7.0], [9.85, 7.35]]), ('brick1_edge3', [[9.5, 7.0], [10.5, 7.0]]), ('brick1_edge4', [[9.85, 7.35], [10.85, 7.35]]), ('brick1_edge5', [[10.5, 6.0], [11.5, 6.0]]), ('brick1_edge6', [[10.5, 7.0], [11.5, 7.0]]), ('brick1_edge7', [[10.85, 7.35], [11.85, 7.35]]), ('brick1_edge8', [[11.5, 6.0], [11.5, 7.0]]), ('brick1_edge9', [[11.5, 6.0], [11.85, 6.35]]), ('brick1_edge10', [[11.5, 7.0], [11.85, 7.35]]), ('brick1_edge11', [[11.85, 6.35], [11.85, 7.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('brick2_front_0_fill', [[13.0, 6.0], [15.0, 6.0], [15.0, 7.0], [13.0, 7.0], [13.0, 6.0]], [1, 2, 2, 2, 79]), ('brick2_right_0_fill', [[15.0, 6.0], [15.35, 6.35], [15.35, 7.35], [15.0, 7.0], [15.0, 6.0]], [1, 2, 2, 2, 79]), ('brick2_top_0_fill', [[13.0, 7.0], [15.0, 7.0], [15.35, 7.35], [13.35, 7.35], [13.0, 7.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('brick2_edge0', [[13.0, 6.0], [13.0, 7.0]]), ('brick2_edge1', [[13.0, 6.0], [14.0, 6.0]]), ('brick2_edge2', [[13.0, 7.0], [13.35, 7.35]]), ('brick2_edge3', [[13.0, 7.0], [14.0, 7.0]]), ('brick2_edge4', [[13.35, 7.35], [14.35, 7.35]]), ('brick2_edge5', [[14.0, 6.0], [15.0, 6.0]]), ('brick2_edge6', [[14.0, 7.0], [15.0, 7.0]]), ('brick2_edge7', [[14.35, 7.35], [15.35, 7.35]]), ('brick2_edge8', [[15.0, 6.0], [15.0, 7.0]]), ('brick2_edge9', [[15.0, 6.0], [15.35, 6.35]]), ('brick2_edge10', [[15.0, 7.0], [15.35, 7.35]]), ('brick2_edge11', [[15.35, 6.35], [15.35, 7.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('brick3_front_0_fill', [[16.5, 6.0], [18.5, 6.0], [18.5, 7.0], [16.5, 7.0], [16.5, 6.0]], [1, 2, 2, 2, 79]), ('brick3_right_0_fill', [[18.5, 6.0], [18.85, 6.35], [18.85, 7.35], [18.5, 7.0], [18.5, 6.0]], [1, 2, 2, 2, 79]), ('brick3_top_0_fill', [[16.5, 7.0], [18.5, 7.0], [18.85, 7.35], [16.85, 7.35], [16.5, 7.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('brick3_edge0', [[16.5, 6.0], [16.5, 7.0]]), ('brick3_edge1', [[16.5, 6.0], [17.5, 6.0]]), ('brick3_edge2', [[16.5, 7.0], [16.85, 7.35]]), ('brick3_edge3', [[16.5, 7.0], [17.5, 7.0]]), ('brick3_edge4', [[16.85, 7.35], [17.85, 7.35]]), ('brick3_edge5', [[17.5, 6.0], [18.5, 6.0]]), ('brick3_edge6', [[17.5, 7.0], [18.5, 7.0]]), ('brick3_edge7', [[17.85, 7.35], [18.85, 7.35]]), ('brick3_edge8', [[18.5, 6.0], [18.5, 7.0]]), ('brick3_edge9', [[18.5, 6.0], [18.85, 6.35]]), ('brick3_edge10', [[18.5, 7.0], [18.85, 7.35]]), ('brick3_edge11', [[18.85, 6.35], [18.85, 7.35]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[0.0, 0.0], [2.0, 0.0], [2.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='A_front_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 1.0], [2.0, 1.0], [2.0, 2.0], [0.0, 2.0], [0.0, 1.0]], [1, 2, 2, 2, 79], id='A_front_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [2.35, 0.35], [2.35, 1.35], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='A_right_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 1.0], [2.35, 1.35], [2.35, 2.35], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79], id='A_right_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.35, 0.35], [2.7, 0.7], [2.7, 2.7], [2.35, 2.35], [2.35, 0.35]], [1, 2, 2, 2, 79], id='A_right_2_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.0, 2.0], [2.0, 2.0], [2.35, 2.35], [0.35, 2.35], [0.0, 2.0]], [1, 2, 2, 2, 79], id='A_top_0_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[0.35, 2.35], [1.35, 2.35], [1.7, 2.7], [0.7, 2.7], [0.35, 2.35]], [1, 2, 2, 2, 79], id='A_top_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.35, 2.35], [2.35, 2.35], [2.7, 2.7], [1.7, 2.7], [1.35, 2.35]], [1, 2, 2, 2, 79], id='A_top_2_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[6.0, 0.0], [7.0, 0.0], [7.0, 1.0], [6.0, 1.0], [6.0, 0.0]], [1, 2, 2, 2, 79], id='B_front_0_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 1.0], [7.0, 1.0], [7.0, 2.0], [6.0, 2.0], [6.0, 1.0]], [1, 2, 2, 2, 79], id='B_front_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, vertices, codes in [('B_front_2_fill', [[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79]), ('B_front_3_fill', [[7.0, 1.0], [8.0, 1.0], [8.0, 2.0], [7.0, 2.0], [7.0, 1.0]], [1, 2, 2, 2, 79]), ('B_right_0_fill', [[8.0, 0.0], [8.7, 0.7], [8.7, 1.7], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79]), ('B_right_1_fill', [[8.0, 1.0], [8.7, 1.7], [8.7, 2.7], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.0, 2.0], [7.0, 2.0], [7.7, 2.7], [6.7, 2.7], [6.0, 2.0]], [1, 2, 2, 2, 79], id='B_top_0_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[7.0, 2.0], [8.0, 2.0], [8.7, 2.7], [7.7, 2.7], [7.0, 2.0]], [1, 2, 2, 2, 79], id='B_top_1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[12.0, 0.0], [13.0, 0.0], [13.0, 2.0], [12.0, 2.0], [12.0, 0.0]], [1, 2, 2, 2, 79], id='C_front_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, vertices, codes in [('C_front_1_fill', [[13.0, 0.0], [14.0, 0.0], [14.0, 2.0], [13.0, 2.0], [13.0, 0.0]], [1, 2, 2, 2, 79]), ('C_right_0_fill', [[14.0, 0.0], [14.35, 0.35], [14.35, 2.35], [14.0, 2.0], [14.0, 0.0]], [1, 2, 2, 2, 79]), ('C_right_1_fill', [[14.35, 0.35], [14.7, 0.7], [14.7, 1.7], [14.35, 1.35], [14.35, 0.35]], [1, 2, 2, 2, 79]), ('C_right_2_fill', [[14.35, 1.35], [14.7, 1.7], [14.7, 2.7], [14.35, 2.35], [14.35, 1.35]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.0, 2.0], [13.0, 2.0], [13.35, 2.35], [12.35, 2.35], [12.0, 2.0]], [1, 2, 2, 2, 79], id='C_top_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[13.0, 2.0], [14.0, 2.0], [14.35, 2.35], [13.35, 2.35], [13.0, 2.0]], [1, 2, 2, 2, 79], id='C_top_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.35, 2.35], [14.35, 2.35], [14.7, 2.7], [12.7, 2.7], [12.35, 2.35]], [1, 2, 2, 2, 79], id='C_top_2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[18.0, 0.0], [19.0, 0.0], [19.0, 2.0], [18.0, 2.0], [18.0, 0.0]], [1, 2, 2, 2, 79], id='D_front_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, vertices, codes in [('D_front_1_fill', [[19.0, 0.0], [20.0, 0.0], [20.0, 2.0], [19.0, 2.0], [19.0, 0.0]], [1, 2, 2, 2, 79]), ('D_right_0_fill', [[20.0, 0.0], [20.35, 0.35], [20.35, 2.35], [20.0, 2.0], [20.0, 0.0]], [1, 2, 2, 2, 79]), ('D_right_1_fill', [[20.35, 0.35], [20.7, 0.7], [20.7, 1.7], [20.35, 1.35], [20.35, 0.35]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[20.35, 1.35], [20.7, 1.7], [20.7, 2.7], [20.35, 2.35], [20.35, 1.35]], [1, 2, 2, 2, 79], id='D_right_2_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[18.0, 2.0], [19.0, 2.0], [19.35, 2.35], [18.35, 2.35], [18.0, 2.0]], [1, 2, 2, 2, 79], id='D_top_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[19.0, 2.0], [20.0, 2.0], [20.35, 2.35], [19.35, 2.35], [19.0, 2.0]], [1, 2, 2, 2, 79], id='D_top_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[18.35, 2.35], [20.35, 2.35], [20.7, 2.7], [18.7, 2.7], [18.35, 2.35]], [1, 2, 2, 2, 79], id='D_top_2_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_04:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[24.0, 0.0], [25.0, 0.0], [25.0, 1.0], [24.0, 1.0], [24.0, 0.0]], [1, 2, 2, 2, 79], id='E_front_0_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[25.0, 0.0], [26.0, 0.0], [26.0, 1.0], [25.0, 1.0], [25.0, 0.0]], [1, 2, 2, 2, 79], id='E_front_1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[24.0, 1.0], [25.0, 1.0], [25.0, 2.0], [24.0, 2.0], [24.0, 1.0]], [1, 2, 2, 2, 79], id='E_front_2_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[25.0, 1.0], [26.0, 1.0], [26.0, 2.0], [25.0, 2.0], [25.0, 1.0]], [1, 2, 2, 2, 79], id='E_front_3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[26.0, 0.0], [26.7, 0.7], [26.7, 1.7], [26.0, 1.0], [26.0, 0.0]], [1, 2, 2, 2, 79], id='E_right_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[26.0, 1.0], [26.7, 1.7], [26.7, 2.7], [26.0, 2.0], [26.0, 1.0]], [1, 2, 2, 2, 79], id='E_right_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[24.0, 2.0], [25.0, 2.0], [25.7, 2.7], [24.7, 2.7], [24.0, 2.0]], [1, 2, 2, 2, 79], id='E_top_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[25.0, 2.0], [26.0, 2.0], [26.7, 2.7], [25.7, 2.7], [25.0, 2.0]], [1, 2, 2, 2, 79], id='E_top_1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_05:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('label0', 'A', [1.3, -1.4]), ('label1', 'B', [7.3, -1.4]), ('label2', 'C', [13.3, -1.4]), ('label3', 'D', [19.3, -1.4]), ('label4', 'E', [25.3, -1.4])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid119().draw(sys.argv[1] if len(sys.argv) > 1 else None))
