"""Frozen question Plane532; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane532:

    def __init__(self):
        self.id = 'Plane532'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane159/extension_03'
        self.question = 'A pattern consists of white, grey and black squares.\nFirst, in the top row only, replace all black squares with white squares. Then replace all white squares with grey squares. Finally, in the bottom row only, replace all grey squares with white squares. Which picture shows the resulting pattern?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('initial_edge_000', [[-0.5, 5.5], [-1.5, 5.5]]),
         ('initial_edge_001', [[-0.5, 6.5], [-0.5, 5.5]]),
         ('initial_edge_002', [[-0.5, 6.5], [-1.5, 6.5]]),
         ('initial_edge_003', [[-1.5, 6.5], [-1.5, 5.5]]),
         ('initial_edge_004', [[0.5, 5.5], [-0.5, 5.5]]),
         ('initial_edge_005', [[0.5, 6.5], [0.5, 5.5]]),
         ('initial_edge_006', [[0.5, 6.5], [-0.5, 6.5]]),
         ('initial_edge_007', [[1.5, 5.5], [0.5, 5.5]]),
         ('initial_edge_008', [[1.5, 5.5], [1.5, 6.5]]),
         ('initial_edge_009', [[1.5, 6.5], [0.5, 6.5]]),
         ('initial_edge_010', [[-0.5, 4.5], [-1.5, 4.5]]),
         ('initial_edge_011', [[-0.5, 5.5], [-0.5, 4.5]]),
         ('initial_edge_012', [[-1.5, 5.5], [-1.5, 4.5]]),
         ('initial_edge_013', [[0.5, 4.5], [-0.5, 4.5]]),
         ('initial_edge_014', [[0.5, 5.5], [0.5, 4.5]]),
         ('initial_edge_015', [[1.5, 4.5], [0.5, 4.5]]),
         ('initial_edge_016', [[1.5, 4.5], [1.5, 5.5]]),
         ('initial_edge_017', [[-1.5, 3.5], [-0.5, 3.5]]),
         ('initial_edge_018', [[-0.5, 4.5], [-0.5, 3.5]]),
         ('initial_edge_019', [[-1.5, 4.5], [-1.5, 3.5]]),
         ('initial_edge_020', [[-0.5, 3.5], [0.5, 3.5]]),
         ('initial_edge_021', [[0.5, 4.5], [0.5, 3.5]]),
         ('initial_edge_022', [[0.5, 3.5], [1.5, 3.5]]),
         ('initial_edge_023', [[1.5, 3.5], [1.5, 4.5]])]
        self._geometry_02 = [('A_edge_000', [[-5.5, 0.5], [-6.5, 0.5]]),
         ('A_edge_001', [[-5.5, 1.5], [-5.5, 0.5]]),
         ('A_edge_002', [[-5.5, 1.5], [-6.5, 1.5]]),
         ('A_edge_003', [[-6.5, 1.5], [-6.5, 0.5]]),
         ('A_edge_004', [[-4.5, 0.5], [-5.5, 0.5]]),
         ('A_edge_005', [[-4.5, 1.5], [-4.5, 0.5]]),
         ('A_edge_006', [[-4.5, 1.5], [-5.5, 1.5]]),
         ('A_edge_007', [[-3.5, 0.5], [-4.5, 0.5]]),
         ('A_edge_008', [[-3.5, 0.5], [-3.5, 1.5]]),
         ('A_edge_009', [[-3.5, 1.5], [-4.5, 1.5]]),
         ('A_edge_010', [[-5.5, -0.5], [-6.5, -0.5]]),
         ('A_edge_011', [[-5.5, 0.5], [-5.5, -0.5]]),
         ('A_edge_012', [[-6.5, 0.5], [-6.5, -0.5]]),
         ('A_edge_013', [[-4.5, -0.5], [-5.5, -0.5]]),
         ('A_edge_014', [[-4.5, 0.5], [-4.5, -0.5]]),
         ('A_edge_015', [[-3.5, -0.5], [-4.5, -0.5]]),
         ('A_edge_016', [[-3.5, -0.5], [-3.5, 0.5]]),
         ('A_edge_017', [[-6.5, -1.5], [-5.5, -1.5]]),
         ('A_edge_018', [[-5.5, -0.5], [-5.5, -1.5]]),
         ('A_edge_019', [[-6.5, -0.5], [-6.5, -1.5]]),
         ('A_edge_020', [[-5.5, -1.5], [-4.5, -1.5]]),
         ('A_edge_021', [[-4.5, -0.5], [-4.5, -1.5]]),
         ('A_edge_022', [[-4.5, -1.5], [-3.5, -1.5]]),
         ('A_edge_023', [[-3.5, -1.5], [-3.5, -0.5]])]
        self._geometry_03 = [('B_edge_000', [[-0.5, 0.5], [-1.5, 0.5]]),
         ('B_edge_001', [[-0.5, 1.5], [-0.5, 0.5]]),
         ('B_edge_002', [[-0.5, 1.5], [-1.5, 1.5]]),
         ('B_edge_003', [[-1.5, 1.5], [-1.5, 0.5]]),
         ('B_edge_004', [[0.5, 0.5], [-0.5, 0.5]]),
         ('B_edge_005', [[0.5, 1.5], [0.5, 0.5]]),
         ('B_edge_006', [[0.5, 1.5], [-0.5, 1.5]]),
         ('B_edge_007', [[1.5, 0.5], [0.5, 0.5]]),
         ('B_edge_008', [[1.5, 0.5], [1.5, 1.5]]),
         ('B_edge_009', [[1.5, 1.5], [0.5, 1.5]]),
         ('B_edge_010', [[-0.5, -0.5], [-1.5, -0.5]]),
         ('B_edge_011', [[-0.5, 0.5], [-0.5, -0.5]]),
         ('B_edge_012', [[-1.5, 0.5], [-1.5, -0.5]]),
         ('B_edge_013', [[0.5, -0.5], [-0.5, -0.5]]),
         ('B_edge_014', [[0.5, 0.5], [0.5, -0.5]]),
         ('B_edge_015', [[1.5, -0.5], [0.5, -0.5]]),
         ('B_edge_016', [[1.5, -0.5], [1.5, 0.5]]),
         ('B_edge_017', [[-1.5, -1.5], [-0.5, -1.5]]),
         ('B_edge_018', [[-0.5, -0.5], [-0.5, -1.5]]),
         ('B_edge_019', [[-1.5, -0.5], [-1.5, -1.5]]),
         ('B_edge_020', [[-0.5, -1.5], [0.5, -1.5]]),
         ('B_edge_021', [[0.5, -0.5], [0.5, -1.5]]),
         ('B_edge_022', [[0.5, -1.5], [1.5, -1.5]]),
         ('B_edge_023', [[1.5, -1.5], [1.5, -0.5]])]
        self._geometry_04 = [('C_edge_000', [[4.5, 0.5], [3.5, 0.5]]),
         ('C_edge_001', [[4.5, 1.5], [4.5, 0.5]]),
         ('C_edge_002', [[4.5, 1.5], [3.5, 1.5]]),
         ('C_edge_003', [[3.5, 1.5], [3.5, 0.5]]),
         ('C_edge_004', [[5.5, 0.5], [4.5, 0.5]]),
         ('C_edge_005', [[5.5, 1.5], [5.5, 0.5]]),
         ('C_edge_006', [[5.5, 1.5], [4.5, 1.5]]),
         ('C_edge_007', [[6.5, 0.5], [5.5, 0.5]]),
         ('C_edge_008', [[6.5, 0.5], [6.5, 1.5]]),
         ('C_edge_009', [[6.5, 1.5], [5.5, 1.5]]),
         ('C_edge_010', [[4.5, -0.5], [3.5, -0.5]]),
         ('C_edge_011', [[4.5, 0.5], [4.5, -0.5]]),
         ('C_edge_012', [[3.5, 0.5], [3.5, -0.5]]),
         ('C_edge_013', [[5.5, -0.5], [4.5, -0.5]]),
         ('C_edge_014', [[5.5, 0.5], [5.5, -0.5]]),
         ('C_edge_015', [[6.5, -0.5], [5.5, -0.5]]),
         ('C_edge_016', [[6.5, -0.5], [6.5, 0.5]]),
         ('C_edge_017', [[3.5, -1.5], [4.5, -1.5]]),
         ('C_edge_018', [[4.5, -0.5], [4.5, -1.5]]),
         ('C_edge_019', [[3.5, -0.5], [3.5, -1.5]]),
         ('C_edge_020', [[4.5, -1.5], [5.5, -1.5]]),
         ('C_edge_021', [[5.5, -0.5], [5.5, -1.5]]),
         ('C_edge_022', [[5.5, -1.5], [6.5, -1.5]]),
         ('C_edge_023', [[6.5, -1.5], [6.5, -0.5]])]
        self._geometry_05 = [('D_edge_000', [[-3.0, -4.5], [-4.0, -4.5]]),
         ('D_edge_001', [[-3.0, -3.5], [-3.0, -4.5]]),
         ('D_edge_002', [[-3.0, -3.5], [-4.0, -3.5]]),
         ('D_edge_003', [[-4.0, -3.5], [-4.0, -4.5]]),
         ('D_edge_004', [[-2.0, -4.5], [-3.0, -4.5]]),
         ('D_edge_005', [[-2.0, -3.5], [-2.0, -4.5]]),
         ('D_edge_006', [[-2.0, -3.5], [-3.0, -3.5]]),
         ('D_edge_007', [[-1.0, -4.5], [-2.0, -4.5]]),
         ('D_edge_008', [[-1.0, -4.5], [-1.0, -3.5]]),
         ('D_edge_009', [[-1.0, -3.5], [-2.0, -3.5]]),
         ('D_edge_010', [[-3.0, -5.5], [-4.0, -5.5]]),
         ('D_edge_011', [[-3.0, -4.5], [-3.0, -5.5]]),
         ('D_edge_012', [[-4.0, -4.5], [-4.0, -5.5]]),
         ('D_edge_013', [[-2.0, -5.5], [-3.0, -5.5]]),
         ('D_edge_014', [[-2.0, -4.5], [-2.0, -5.5]]),
         ('D_edge_015', [[-1.0, -5.5], [-2.0, -5.5]]),
         ('D_edge_016', [[-1.0, -5.5], [-1.0, -4.5]]),
         ('D_edge_017', [[-4.0, -6.5], [-3.0, -6.5]]),
         ('D_edge_018', [[-3.0, -5.5], [-3.0, -6.5]]),
         ('D_edge_019', [[-4.0, -5.5], [-4.0, -6.5]]),
         ('D_edge_020', [[-3.0, -6.5], [-2.0, -6.5]]),
         ('D_edge_021', [[-2.0, -5.5], [-2.0, -6.5]]),
         ('D_edge_022', [[-2.0, -6.5], [-1.0, -6.5]]),
         ('D_edge_023', [[-1.0, -6.5], [-1.0, -5.5]])]
        self._geometry_06 = [('E_edge_000', [[2.0, -4.5], [1.0, -4.5]]),
         ('E_edge_001', [[2.0, -3.5], [2.0, -4.5]]),
         ('E_edge_002', [[2.0, -3.5], [1.0, -3.5]]),
         ('E_edge_003', [[1.0, -3.5], [1.0, -4.5]]),
         ('E_edge_004', [[3.0, -4.5], [2.0, -4.5]]),
         ('E_edge_005', [[3.0, -3.5], [3.0, -4.5]]),
         ('E_edge_006', [[3.0, -3.5], [2.0, -3.5]]),
         ('E_edge_007', [[4.0, -4.5], [3.0, -4.5]]),
         ('E_edge_008', [[4.0, -4.5], [4.0, -3.5]]),
         ('E_edge_009', [[4.0, -3.5], [3.0, -3.5]]),
         ('E_edge_010', [[2.0, -5.5], [1.0, -5.5]]),
         ('E_edge_011', [[2.0, -4.5], [2.0, -5.5]]),
         ('E_edge_012', [[1.0, -4.5], [1.0, -5.5]]),
         ('E_edge_013', [[3.0, -5.5], [2.0, -5.5]]),
         ('E_edge_014', [[3.0, -4.5], [3.0, -5.5]]),
         ('E_edge_015', [[4.0, -5.5], [3.0, -5.5]]),
         ('E_edge_016', [[4.0, -5.5], [4.0, -4.5]]),
         ('E_edge_017', [[1.0, -6.5], [2.0, -6.5]]),
         ('E_edge_018', [[2.0, -5.5], [2.0, -6.5]]),
         ('E_edge_019', [[1.0, -5.5], [1.0, -6.5]]),
         ('E_edge_020', [[2.0, -6.5], [3.0, -6.5]]),
         ('E_edge_021', [[3.0, -5.5], [3.0, -6.5]]),
         ('E_edge_022', [[3.0, -6.5], [4.0, -6.5]]),
         ('E_edge_023', [[4.0, -6.5], [4.0, -5.5]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane532.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-7.25433271655383, 7.254332716553834], ylim=[-7.671557263466881, 6.837108169640783], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-1.5, 5.5], [-0.5, 5.5], [-0.5, 6.5], [-1.5, 6.5], [-1.5, 5.5]], [1, 2, 2, 2, 79], id='initial_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, 5.5], [0.5, 5.5], [0.5, 6.5], [-0.5, 6.5], [-0.5, 5.5]], [1, 2, 2, 2, 79], id='initial_cell_r1c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, 5.5], [1.5, 5.5], [1.5, 6.5], [0.5, 6.5], [0.5, 5.5]], [1, 2, 2, 2, 79], id='initial_cell_r1c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.5, 4.5], [-0.5, 4.5], [-0.5, 5.5], [-1.5, 5.5], [-1.5, 4.5]], [1, 2, 2, 2, 79], id='initial_cell_r2c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, 4.5], [0.5, 4.5], [0.5, 5.5], [-0.5, 5.5], [-0.5, 4.5]], [1, 2, 2, 2, 79], id='initial_cell_r2c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, 4.5], [1.5, 4.5], [1.5, 5.5], [0.5, 5.5], [0.5, 4.5]], [1, 2, 2, 2, 79], id='initial_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.5, 3.5], [-0.5, 3.5], [-0.5, 4.5], [-1.5, 4.5], [-1.5, 3.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, 3.5], [0.5, 3.5], [0.5, 4.5], [-0.5, 4.5], [-0.5, 3.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, 3.5], [1.5, 3.5], [1.5, 4.5], [0.5, 4.5], [0.5, 3.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[-6.5, 0.5], [-5.5, 0.5], [-5.5, 1.5], [-6.5, 1.5], [-6.5, 0.5]], [1, 2, 2, 2, 79], id='A_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('A_cell_r1c2_fill', [[-5.5, 0.5], [-4.5, 0.5], [-4.5, 1.5], [-5.5, 1.5], [-5.5, 0.5]], [1, 2, 2, 2, 79]), ('A_cell_r1c3_fill', [[-4.5, 0.5], [-3.5, 0.5], [-3.5, 1.5], [-4.5, 1.5], [-4.5, 0.5]], [1, 2, 2, 2, 79]), ('A_cell_r2c1_fill', [[-6.5, -0.5], [-5.5, -0.5], [-5.5, 0.5], [-6.5, 0.5], [-6.5, -0.5]], [1, 2, 2, 2, 79]), ('A_cell_r2c2_fill', [[-5.5, -0.5], [-4.5, -0.5], [-4.5, 0.5], [-5.5, 0.5], [-5.5, -0.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-4.5, -0.5], [-3.5, -0.5], [-3.5, 0.5], [-4.5, 0.5], [-4.5, -0.5]], [1, 2, 2, 2, 79], id='A_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-6.5, -1.5], [-5.5, -1.5], [-5.5, -0.5], [-6.5, -0.5], [-6.5, -1.5]], [1, 2, 2, 2, 79], id='A_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-5.5, -1.5], [-4.5, -1.5], [-4.5, -0.5], [-5.5, -0.5], [-5.5, -1.5]], [1, 2, 2, 2, 79], id='A_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-4.5, -1.5], [-3.5, -1.5], [-3.5, -0.5], [-4.5, -0.5], [-4.5, -1.5]], [1, 2, 2, 2, 79], id='A_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('B_cell_r1c1_fill', [[-1.5, 0.5], [-0.5, 0.5], [-0.5, 1.5], [-1.5, 1.5], [-1.5, 0.5]], [1, 2, 2, 2, 79]), ('B_cell_r1c2_fill', [[-0.5, 0.5], [0.5, 0.5], [0.5, 1.5], [-0.5, 1.5], [-0.5, 0.5]], [1, 2, 2, 2, 79]), ('B_cell_r1c3_fill', [[0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5], [0.5, 0.5]], [1, 2, 2, 2, 79]), ('B_cell_r2c1_fill', [[-1.5, -0.5], [-0.5, -0.5], [-0.5, 0.5], [-1.5, 0.5], [-1.5, -0.5]], [1, 2, 2, 2, 79]), ('B_cell_r2c2_fill', [[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, -0.5], [1.5, -0.5], [1.5, 0.5], [0.5, 0.5], [0.5, -0.5]], [1, 2, 2, 2, 79], id='B_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.5, -1.5], [-0.5, -1.5], [-0.5, -0.5], [-1.5, -0.5], [-1.5, -1.5]], [1, 2, 2, 2, 79], id='B_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, -1.5], [0.5, -1.5], [0.5, -0.5], [-0.5, -0.5], [-0.5, -1.5]], [1, 2, 2, 2, 79], id='B_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, -1.5], [1.5, -1.5], [1.5, -0.5], [0.5, -0.5], [0.5, -1.5]], [1, 2, 2, 2, 79], id='B_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id)
            c.path([[3.5, 0.5], [4.5, 0.5], [4.5, 1.5], [3.5, 1.5], [3.5, 0.5]], [1, 2, 2, 2, 79], id='C_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('C_cell_r1c2_fill', [[4.5, 0.5], [5.5, 0.5], [5.5, 1.5], [4.5, 1.5], [4.5, 0.5]], [1, 2, 2, 2, 79]), ('C_cell_r1c3_fill', [[5.5, 0.5], [6.5, 0.5], [6.5, 1.5], [5.5, 1.5], [5.5, 0.5]], [1, 2, 2, 2, 79]), ('C_cell_r2c1_fill', [[3.5, -0.5], [4.5, -0.5], [4.5, 0.5], [3.5, 0.5], [3.5, -0.5]], [1, 2, 2, 2, 79]), ('C_cell_r2c2_fill', [[4.5, -0.5], [5.5, -0.5], [5.5, 0.5], [4.5, 0.5], [4.5, -0.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[5.5, -0.5], [6.5, -0.5], [6.5, 0.5], [5.5, 0.5], [5.5, -0.5]], [1, 2, 2, 2, 79], id='C_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[3.5, -1.5], [4.5, -1.5], [4.5, -0.5], [3.5, -0.5], [3.5, -1.5]], [1, 2, 2, 2, 79], id='C_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[4.5, -1.5], [5.5, -1.5], [5.5, -0.5], [4.5, -0.5], [4.5, -1.5]], [1, 2, 2, 2, 79], id='C_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[5.5, -1.5], [6.5, -1.5], [6.5, -0.5], [5.5, -0.5], [5.5, -1.5]], [1, 2, 2, 2, 79], id='C_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_04:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('D_cell_r1c1_fill', [[-4.0, -4.5], [-3.0, -4.5], [-3.0, -3.5], [-4.0, -3.5], [-4.0, -4.5]], [1, 2, 2, 2, 79]), ('D_cell_r1c2_fill', [[-3.0, -4.5], [-2.0, -4.5], [-2.0, -3.5], [-3.0, -3.5], [-3.0, -4.5]], [1, 2, 2, 2, 79]), ('D_cell_r1c3_fill', [[-2.0, -4.5], [-1.0, -4.5], [-1.0, -3.5], [-2.0, -3.5], [-2.0, -4.5]], [1, 2, 2, 2, 79]), ('D_cell_r2c1_fill', [[-4.0, -5.5], [-3.0, -5.5], [-3.0, -4.5], [-4.0, -4.5], [-4.0, -5.5]], [1, 2, 2, 2, 79]), ('D_cell_r2c2_fill', [[-3.0, -5.5], [-2.0, -5.5], [-2.0, -4.5], [-3.0, -4.5], [-3.0, -5.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.0, -5.5], [-1.0, -5.5], [-1.0, -4.5], [-2.0, -4.5], [-2.0, -5.5]], [1, 2, 2, 2, 79], id='D_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-4.0, -6.5], [-3.0, -6.5], [-3.0, -5.5], [-4.0, -5.5], [-4.0, -6.5]], [1, 2, 2, 2, 79], id='D_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-3.0, -6.5], [-2.0, -6.5], [-2.0, -5.5], [-3.0, -5.5], [-3.0, -6.5]], [1, 2, 2, 2, 79], id='D_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.0, -6.5], [-1.0, -6.5], [-1.0, -5.5], [-2.0, -5.5], [-2.0, -6.5]], [1, 2, 2, 2, 79], id='D_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_05:
                c.line(points, id=object_id)
            c.path([[1.0, -4.5], [2.0, -4.5], [2.0, -3.5], [1.0, -3.5], [1.0, -4.5]], [1, 2, 2, 2, 79], id='E_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('E_cell_r1c2_fill', [[2.0, -4.5], [3.0, -4.5], [3.0, -3.5], [2.0, -3.5], [2.0, -4.5]], [1, 2, 2, 2, 79]), ('E_cell_r1c3_fill', [[3.0, -4.5], [4.0, -4.5], [4.0, -3.5], [3.0, -3.5], [3.0, -4.5]], [1, 2, 2, 2, 79]), ('E_cell_r2c1_fill', [[1.0, -5.5], [2.0, -5.5], [2.0, -4.5], [1.0, -4.5], [1.0, -5.5]], [1, 2, 2, 2, 79]), ('E_cell_r2c2_fill', [[2.0, -5.5], [3.0, -5.5], [3.0, -4.5], [2.0, -4.5], [2.0, -5.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[3.0, -5.5], [4.0, -5.5], [4.0, -4.5], [3.0, -4.5], [3.0, -5.5]], [1, 2, 2, 2, 79], id='E_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[1.0, -6.5], [2.0, -6.5], [2.0, -5.5], [1.0, -5.5], [1.0, -6.5]], [1, 2, 2, 2, 79], id='E_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[2.0, -6.5], [3.0, -6.5], [3.0, -5.5], [2.0, -5.5], [2.0, -6.5]], [1, 2, 2, 2, 79], id='E_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[3.0, -6.5], [4.0, -6.5], [4.0, -5.5], [3.0, -5.5], [3.0, -6.5]], [1, 2, 2, 2, 79], id='E_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_06:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('A_label', '(A)', [-5, -2.1]), ('B_label', '(B)', [0, -2.1]), ('C_label', '(C)', [5, -2.1]), ('D_label', '(D)', [-2.5, -7.1]), ('E_label', '(E)', [2.5, -7.1])]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane532().draw(sys.argv[1] if len(sys.argv) > 1 else None))
