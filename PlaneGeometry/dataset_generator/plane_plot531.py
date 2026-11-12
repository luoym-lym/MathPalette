"""Frozen question Plane531; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane531:

    def __init__(self):
        self.id = 'Plane531'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane159/extension_02'
        self.question = 'A pattern consists of white, grey and black squares.\nFirst, replace all grey squares with black squares. Then replace all white squares with grey squares. Finally, replace all black squares with white squares. Which picture shows the resulting pattern?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('initial_edge_000', [[-1.0, 7.0], [-2.0, 7.0]]),
         ('initial_edge_001', [[-1.0, 7.0], [-1.0, 8.0]]),
         ('initial_edge_002', [[-1.0, 8.0], [-2.0, 8.0]]),
         ('initial_edge_003', [[-2.0, 8.0], [-2.0, 7.0]]),
         ('initial_edge_004', [[-1.0, 6.0], [-2.0, 6.0]]),
         ('initial_edge_005', [[-1.0, 7.0], [-1.0, 6.0]]),
         ('initial_edge_006', [[-2.0, 7.0], [-2.0, 6.0]]),
         ('initial_edge_007', [[0.0, 6.0], [-1.0, 6.0]]),
         ('initial_edge_008', [[0.0, 6.0], [0.0, 7.0]]),
         ('initial_edge_009', [[0.0, 7.0], [-1.0, 7.0]]),
         ('initial_edge_010', [[-1.0, 5.0], [-2.0, 5.0]]),
         ('initial_edge_011', [[-1.0, 6.0], [-1.0, 5.0]]),
         ('initial_edge_012', [[-2.0, 6.0], [-2.0, 5.0]]),
         ('initial_edge_013', [[0.0, 5.0], [-1.0, 5.0]]),
         ('initial_edge_014', [[0.0, 6.0], [0.0, 5.0]]),
         ('initial_edge_015', [[1.0, 5.0], [0.0, 5.0]]),
         ('initial_edge_016', [[1.0, 5.0], [1.0, 6.0]]),
         ('initial_edge_017', [[1.0, 6.0], [0.0, 6.0]]),
         ('initial_edge_018', [[-2.0, 4.0], [-1.0, 4.0]]),
         ('initial_edge_019', [[-1.0, 5.0], [-1.0, 4.0]]),
         ('initial_edge_020', [[-2.0, 5.0], [-2.0, 4.0]]),
         ('initial_edge_021', [[-1.0, 4.0], [0.0, 4.0]]),
         ('initial_edge_022', [[0.0, 5.0], [0.0, 4.0]]),
         ('initial_edge_023', [[0.0, 4.0], [1.0, 4.0]]),
         ('initial_edge_024', [[1.0, 5.0], [1.0, 4.0]]),
         ('initial_edge_025', [[1.0, 4.0], [2.0, 4.0]]),
         ('initial_edge_026', [[2.0, 4.0], [2.0, 5.0]]),
         ('initial_edge_027', [[2.0, 5.0], [1.0, 5.0]])]
        self._geometry_02 = [('A_edge_000', [[-7.0, 1.0], [-8.0, 1.0]]),
         ('A_edge_001', [[-7.0, 1.0], [-7.0, 2.0]]),
         ('A_edge_002', [[-7.0, 2.0], [-8.0, 2.0]]),
         ('A_edge_003', [[-8.0, 2.0], [-8.0, 1.0]]),
         ('A_edge_004', [[-7.0, 0.0], [-8.0, 0.0]]),
         ('A_edge_005', [[-7.0, 1.0], [-7.0, 0.0]]),
         ('A_edge_006', [[-8.0, 1.0], [-8.0, 0.0]]),
         ('A_edge_007', [[-6.0, 0.0], [-7.0, 0.0]]),
         ('A_edge_008', [[-6.0, 0.0], [-6.0, 1.0]]),
         ('A_edge_009', [[-6.0, 1.0], [-7.0, 1.0]]),
         ('A_edge_010', [[-7.0, -1.0], [-8.0, -1.0]]),
         ('A_edge_011', [[-7.0, 0.0], [-7.0, -1.0]]),
         ('A_edge_012', [[-8.0, 0.0], [-8.0, -1.0]]),
         ('A_edge_013', [[-6.0, -1.0], [-7.0, -1.0]]),
         ('A_edge_014', [[-6.0, 0.0], [-6.0, -1.0]]),
         ('A_edge_015', [[-5.0, -1.0], [-6.0, -1.0]]),
         ('A_edge_016', [[-5.0, -1.0], [-5.0, 0.0]]),
         ('A_edge_017', [[-5.0, 0.0], [-6.0, 0.0]]),
         ('A_edge_018', [[-8.0, -2.0], [-7.0, -2.0]]),
         ('A_edge_019', [[-7.0, -1.0], [-7.0, -2.0]]),
         ('A_edge_020', [[-8.0, -1.0], [-8.0, -2.0]]),
         ('A_edge_021', [[-7.0, -2.0], [-6.0, -2.0]]),
         ('A_edge_022', [[-6.0, -1.0], [-6.0, -2.0]]),
         ('A_edge_023', [[-6.0, -2.0], [-5.0, -2.0]]),
         ('A_edge_024', [[-5.0, -1.0], [-5.0, -2.0]]),
         ('A_edge_025', [[-5.0, -2.0], [-4.0, -2.0]]),
         ('A_edge_026', [[-4.0, -2.0], [-4.0, -1.0]]),
         ('A_edge_027', [[-4.0, -1.0], [-5.0, -1.0]])]
        self._geometry_03 = [('B_edge_000', [[-1.0, 1.0], [-2.0, 1.0]]),
         ('B_edge_001', [[-1.0, 1.0], [-1.0, 2.0]]),
         ('B_edge_002', [[-1.0, 2.0], [-2.0, 2.0]]),
         ('B_edge_003', [[-2.0, 2.0], [-2.0, 1.0]]),
         ('B_edge_004', [[-1.0, 0.0], [-2.0, 0.0]]),
         ('B_edge_005', [[-1.0, 1.0], [-1.0, 0.0]]),
         ('B_edge_006', [[-2.0, 1.0], [-2.0, 0.0]]),
         ('B_edge_007', [[0.0, 0.0], [-1.0, 0.0]]),
         ('B_edge_008', [[0.0, 0.0], [0.0, 1.0]]),
         ('B_edge_009', [[0.0, 1.0], [-1.0, 1.0]]),
         ('B_edge_010', [[-1.0, -1.0], [-2.0, -1.0]]),
         ('B_edge_011', [[-1.0, 0.0], [-1.0, -1.0]]),
         ('B_edge_012', [[-2.0, 0.0], [-2.0, -1.0]]),
         ('B_edge_013', [[0.0, -1.0], [-1.0, -1.0]]),
         ('B_edge_014', [[0.0, 0.0], [0.0, -1.0]]),
         ('B_edge_015', [[1.0, -1.0], [0.0, -1.0]]),
         ('B_edge_016', [[1.0, -1.0], [1.0, 0.0]]),
         ('B_edge_017', [[1.0, 0.0], [0.0, 0.0]]),
         ('B_edge_018', [[-2.0, -2.0], [-1.0, -2.0]]),
         ('B_edge_019', [[-1.0, -1.0], [-1.0, -2.0]]),
         ('B_edge_020', [[-2.0, -1.0], [-2.0, -2.0]]),
         ('B_edge_021', [[-1.0, -2.0], [0.0, -2.0]]),
         ('B_edge_022', [[0.0, -1.0], [0.0, -2.0]]),
         ('B_edge_023', [[0.0, -2.0], [1.0, -2.0]]),
         ('B_edge_024', [[1.0, -1.0], [1.0, -2.0]]),
         ('B_edge_025', [[1.0, -2.0], [2.0, -2.0]]),
         ('B_edge_026', [[2.0, -2.0], [2.0, -1.0]]),
         ('B_edge_027', [[2.0, -1.0], [1.0, -1.0]])]
        self._geometry_04 = [('C_edge_000', [[5.0, 1.0], [4.0, 1.0]]),
         ('C_edge_001', [[5.0, 1.0], [5.0, 2.0]]),
         ('C_edge_002', [[5.0, 2.0], [4.0, 2.0]]),
         ('C_edge_003', [[4.0, 2.0], [4.0, 1.0]]),
         ('C_edge_004', [[5.0, 0.0], [4.0, 0.0]]),
         ('C_edge_005', [[5.0, 1.0], [5.0, 0.0]]),
         ('C_edge_006', [[4.0, 1.0], [4.0, 0.0]]),
         ('C_edge_007', [[6.0, 0.0], [5.0, 0.0]]),
         ('C_edge_008', [[6.0, 0.0], [6.0, 1.0]]),
         ('C_edge_009', [[6.0, 1.0], [5.0, 1.0]]),
         ('C_edge_010', [[5.0, -1.0], [4.0, -1.0]]),
         ('C_edge_011', [[5.0, 0.0], [5.0, -1.0]]),
         ('C_edge_012', [[4.0, 0.0], [4.0, -1.0]]),
         ('C_edge_013', [[6.0, -1.0], [5.0, -1.0]]),
         ('C_edge_014', [[6.0, 0.0], [6.0, -1.0]]),
         ('C_edge_015', [[7.0, -1.0], [6.0, -1.0]]),
         ('C_edge_016', [[7.0, -1.0], [7.0, 0.0]]),
         ('C_edge_017', [[7.0, 0.0], [6.0, 0.0]]),
         ('C_edge_018', [[4.0, -2.0], [5.0, -2.0]]),
         ('C_edge_019', [[5.0, -1.0], [5.0, -2.0]]),
         ('C_edge_020', [[4.0, -1.0], [4.0, -2.0]]),
         ('C_edge_021', [[5.0, -2.0], [6.0, -2.0]]),
         ('C_edge_022', [[6.0, -1.0], [6.0, -2.0]]),
         ('C_edge_023', [[6.0, -2.0], [7.0, -2.0]]),
         ('C_edge_024', [[7.0, -1.0], [7.0, -2.0]]),
         ('C_edge_025', [[7.0, -2.0], [8.0, -2.0]]),
         ('C_edge_026', [[8.0, -2.0], [8.0, -1.0]]),
         ('C_edge_027', [[8.0, -1.0], [7.0, -1.0]])]
        self._geometry_05 = [('D_edge_000', [[-4.0, -5.0], [-5.0, -5.0]]),
         ('D_edge_001', [[-4.0, -5.0], [-4.0, -4.0]]),
         ('D_edge_002', [[-4.0, -4.0], [-5.0, -4.0]]),
         ('D_edge_003', [[-5.0, -4.0], [-5.0, -5.0]]),
         ('D_edge_004', [[-4.0, -6.0], [-5.0, -6.0]]),
         ('D_edge_005', [[-4.0, -5.0], [-4.0, -6.0]]),
         ('D_edge_006', [[-5.0, -5.0], [-5.0, -6.0]]),
         ('D_edge_007', [[-3.0, -6.0], [-4.0, -6.0]]),
         ('D_edge_008', [[-3.0, -6.0], [-3.0, -5.0]]),
         ('D_edge_009', [[-3.0, -5.0], [-4.0, -5.0]]),
         ('D_edge_010', [[-4.0, -7.0], [-5.0, -7.0]]),
         ('D_edge_011', [[-4.0, -6.0], [-4.0, -7.0]]),
         ('D_edge_012', [[-5.0, -6.0], [-5.0, -7.0]]),
         ('D_edge_013', [[-3.0, -7.0], [-4.0, -7.0]]),
         ('D_edge_014', [[-3.0, -6.0], [-3.0, -7.0]]),
         ('D_edge_015', [[-2.0, -7.0], [-3.0, -7.0]]),
         ('D_edge_016', [[-2.0, -7.0], [-2.0, -6.0]]),
         ('D_edge_017', [[-2.0, -6.0], [-3.0, -6.0]]),
         ('D_edge_018', [[-5.0, -8.0], [-4.0, -8.0]]),
         ('D_edge_019', [[-4.0, -7.0], [-4.0, -8.0]]),
         ('D_edge_020', [[-5.0, -7.0], [-5.0, -8.0]]),
         ('D_edge_021', [[-4.0, -8.0], [-3.0, -8.0]]),
         ('D_edge_022', [[-3.0, -7.0], [-3.0, -8.0]]),
         ('D_edge_023', [[-3.0, -8.0], [-2.0, -8.0]]),
         ('D_edge_024', [[-2.0, -7.0], [-2.0, -8.0]]),
         ('D_edge_025', [[-2.0, -8.0], [-1.0, -8.0]]),
         ('D_edge_026', [[-1.0, -8.0], [-1.0, -7.0]]),
         ('D_edge_027', [[-1.0, -7.0], [-2.0, -7.0]])]
        self._geometry_06 = [('E_edge_000', [[2.0, -5.0], [1.0, -5.0]]),
         ('E_edge_001', [[2.0, -5.0], [2.0, -4.0]]),
         ('E_edge_002', [[2.0, -4.0], [1.0, -4.0]]),
         ('E_edge_003', [[1.0, -4.0], [1.0, -5.0]]),
         ('E_edge_004', [[2.0, -6.0], [1.0, -6.0]]),
         ('E_edge_005', [[2.0, -5.0], [2.0, -6.0]]),
         ('E_edge_006', [[1.0, -5.0], [1.0, -6.0]]),
         ('E_edge_007', [[3.0, -6.0], [2.0, -6.0]]),
         ('E_edge_008', [[3.0, -6.0], [3.0, -5.0]]),
         ('E_edge_009', [[3.0, -5.0], [2.0, -5.0]]),
         ('E_edge_010', [[2.0, -7.0], [1.0, -7.0]]),
         ('E_edge_011', [[2.0, -6.0], [2.0, -7.0]]),
         ('E_edge_012', [[1.0, -6.0], [1.0, -7.0]]),
         ('E_edge_013', [[3.0, -7.0], [2.0, -7.0]]),
         ('E_edge_014', [[3.0, -6.0], [3.0, -7.0]]),
         ('E_edge_015', [[4.0, -7.0], [3.0, -7.0]]),
         ('E_edge_016', [[4.0, -7.0], [4.0, -6.0]]),
         ('E_edge_017', [[4.0, -6.0], [3.0, -6.0]]),
         ('E_edge_018', [[1.0, -8.0], [2.0, -8.0]]),
         ('E_edge_019', [[2.0, -7.0], [2.0, -8.0]]),
         ('E_edge_020', [[1.0, -7.0], [1.0, -8.0]]),
         ('E_edge_021', [[2.0, -8.0], [3.0, -8.0]]),
         ('E_edge_022', [[3.0, -7.0], [3.0, -8.0]]),
         ('E_edge_023', [[3.0, -8.0], [4.0, -8.0]]),
         ('E_edge_024', [[4.0, -7.0], [4.0, -8.0]]),
         ('E_edge_025', [[4.0, -8.0], [5.0, -8.0]]),
         ('E_edge_026', [[5.0, -8.0], [5.0, -7.0]]),
         ('E_edge_027', [[5.0, -7.0], [4.0, -7.0]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane531.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-8.854553168734824, 8.854553168734828], ylim=[-9.297636071584577, 8.411470265885075], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-2.0, 7.0], [-1.0, 7.0], [-1.0, 8.0], [-2.0, 8.0], [-2.0, 7.0]], [1, 2, 2, 2, 79], id='initial_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.0, 6.0], [-1.0, 6.0], [-1.0, 7.0], [-2.0, 7.0], [-2.0, 6.0]], [1, 2, 2, 2, 79], id='initial_cell_r2c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.0, 6.0], [0.0, 6.0], [0.0, 7.0], [-1.0, 7.0], [-1.0, 6.0]], [1, 2, 2, 2, 79], id='initial_cell_r2c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.0, 5.0], [-1.0, 5.0], [-1.0, 6.0], [-2.0, 6.0], [-2.0, 5.0]], [1, 2, 2, 2, 79], id='initial_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.0, 5.0], [0.0, 5.0], [0.0, 6.0], [-1.0, 6.0], [-1.0, 5.0]], [1, 2, 2, 2, 79], id='initial_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.0, 5.0], [1.0, 5.0], [1.0, 6.0], [0.0, 6.0], [0.0, 5.0]], [1, 2, 2, 2, 79], id='initial_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.0, 4.0], [-1.0, 4.0], [-1.0, 5.0], [-2.0, 5.0], [-2.0, 4.0]], [1, 2, 2, 2, 79], id='initial_cell_r4c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.0, 4.0], [0.0, 4.0], [0.0, 5.0], [-1.0, 5.0], [-1.0, 4.0]], [1, 2, 2, 2, 79], id='initial_cell_r4c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.0, 4.0], [1.0, 4.0], [1.0, 5.0], [0.0, 5.0], [0.0, 4.0]], [1, 2, 2, 2, 79], id='initial_cell_r4c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[1.0, 4.0], [2.0, 4.0], [2.0, 5.0], [1.0, 5.0], [1.0, 4.0]], [1, 2, 2, 2, 79], id='initial_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[-8.0, 1.0], [-7.0, 1.0], [-7.0, 2.0], [-8.0, 2.0], [-8.0, 1.0]], [1, 2, 2, 2, 79], id='A_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-8.0, 0.0], [-7.0, 0.0], [-7.0, 1.0], [-8.0, 1.0], [-8.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell_r2c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-7.0, 0.0], [-6.0, 0.0], [-6.0, 1.0], [-7.0, 1.0], [-7.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell_r2c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-8.0, -1.0], [-7.0, -1.0], [-7.0, 0.0], [-8.0, 0.0], [-8.0, -1.0]], [1, 2, 2, 2, 79], id='A_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-7.0, -1.0], [-6.0, -1.0], [-6.0, 0.0], [-7.0, 0.0], [-7.0, -1.0]], [1, 2, 2, 2, 79], id='A_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-6.0, -1.0], [-5.0, -1.0], [-5.0, 0.0], [-6.0, 0.0], [-6.0, -1.0]], [1, 2, 2, 2, 79], id='A_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-8.0, -2.0], [-7.0, -2.0], [-7.0, -1.0], [-8.0, -1.0], [-8.0, -2.0]], [1, 2, 2, 2, 79], id='A_cell_r4c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-7.0, -2.0], [-6.0, -2.0], [-6.0, -1.0], [-7.0, -1.0], [-7.0, -2.0]], [1, 2, 2, 2, 79], id='A_cell_r4c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-6.0, -2.0], [-5.0, -2.0], [-5.0, -1.0], [-6.0, -1.0], [-6.0, -2.0]], [1, 2, 2, 2, 79], id='A_cell_r4c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-5.0, -2.0], [-4.0, -2.0], [-4.0, -1.0], [-5.0, -1.0], [-5.0, -2.0]], [1, 2, 2, 2, 79], id='A_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('B_cell_r1c1_fill', [[-2.0, 1.0], [-1.0, 1.0], [-1.0, 2.0], [-2.0, 2.0], [-2.0, 1.0]], [1, 2, 2, 2, 79]), ('B_cell_r2c1_fill', [[-2.0, 0.0], [-1.0, 0.0], [-1.0, 1.0], [-2.0, 1.0], [-2.0, 0.0]], [1, 2, 2, 2, 79]), ('B_cell_r2c2_fill', [[-1.0, 0.0], [0.0, 0.0], [0.0, 1.0], [-1.0, 1.0], [-1.0, 0.0]], [1, 2, 2, 2, 79]), ('B_cell_r3c1_fill', [[-2.0, -1.0], [-1.0, -1.0], [-1.0, 0.0], [-2.0, 0.0], [-2.0, -1.0]], [1, 2, 2, 2, 79]), ('B_cell_r3c2_fill', [[-1.0, -1.0], [0.0, -1.0], [0.0, 0.0], [-1.0, 0.0], [-1.0, -1.0]], [1, 2, 2, 2, 79]), ('B_cell_r3c3_fill', [[0.0, -1.0], [1.0, -1.0], [1.0, 0.0], [0.0, 0.0], [0.0, -1.0]], [1, 2, 2, 2, 79]), ('B_cell_r4c1_fill', [[-2.0, -2.0], [-1.0, -2.0], [-1.0, -1.0], [-2.0, -1.0], [-2.0, -2.0]], [1, 2, 2, 2, 79]), ('B_cell_r4c2_fill', [[-1.0, -2.0], [0.0, -2.0], [0.0, -1.0], [-1.0, -1.0], [-1.0, -2.0]], [1, 2, 2, 2, 79]), ('B_cell_r4c3_fill', [[0.0, -2.0], [1.0, -2.0], [1.0, -1.0], [0.0, -1.0], [0.0, -2.0]], [1, 2, 2, 2, 79]), ('B_cell_r4c4_fill', [[1.0, -2.0], [2.0, -2.0], [2.0, -1.0], [1.0, -1.0], [1.0, -2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id)
            c.path([[4.0, 1.0], [5.0, 1.0], [5.0, 2.0], [4.0, 2.0], [4.0, 1.0]], [1, 2, 2, 2, 79], id='C_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[4.0, 0.0], [5.0, 0.0], [5.0, 1.0], [4.0, 1.0], [4.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell_r2c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('C_cell_r2c2_fill', [[5.0, 0.0], [6.0, 0.0], [6.0, 1.0], [5.0, 1.0], [5.0, 0.0]], [1, 2, 2, 2, 79]), ('C_cell_r3c1_fill', [[4.0, -1.0], [5.0, -1.0], [5.0, 0.0], [4.0, 0.0], [4.0, -1.0]], [1, 2, 2, 2, 79]), ('C_cell_r3c2_fill', [[5.0, -1.0], [6.0, -1.0], [6.0, 0.0], [5.0, 0.0], [5.0, -1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[6.0, -1.0], [7.0, -1.0], [7.0, 0.0], [6.0, 0.0], [6.0, -1.0]], [1, 2, 2, 2, 79], id='C_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[4.0, -2.0], [5.0, -2.0], [5.0, -1.0], [4.0, -1.0], [4.0, -2.0]], [1, 2, 2, 2, 79], id='C_cell_r4c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('C_cell_r4c2_fill', [[5.0, -2.0], [6.0, -2.0], [6.0, -1.0], [5.0, -1.0], [5.0, -2.0]], [1, 2, 2, 2, 79]), ('C_cell_r4c3_fill', [[6.0, -2.0], [7.0, -2.0], [7.0, -1.0], [6.0, -1.0], [6.0, -2.0]], [1, 2, 2, 2, 79]), ('C_cell_r4c4_fill', [[7.0, -2.0], [8.0, -2.0], [8.0, -1.0], [7.0, -1.0], [7.0, -2.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_04:
                c.line(points, id=object_id)
            c.path([[-5.0, -5.0], [-4.0, -5.0], [-4.0, -4.0], [-5.0, -4.0], [-5.0, -5.0]], [1, 2, 2, 2, 79], id='D_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-5.0, -6.0], [-4.0, -6.0], [-4.0, -5.0], [-5.0, -5.0], [-5.0, -6.0]], [1, 2, 2, 2, 79], id='D_cell_r2c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-4.0, -6.0], [-3.0, -6.0], [-3.0, -5.0], [-4.0, -5.0], [-4.0, -6.0]], [1, 2, 2, 2, 79], id='D_cell_r2c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-5.0, -7.0], [-4.0, -7.0], [-4.0, -6.0], [-5.0, -6.0], [-5.0, -7.0]], [1, 2, 2, 2, 79], id='D_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('D_cell_r3c2_fill', [[-4.0, -7.0], [-3.0, -7.0], [-3.0, -6.0], [-4.0, -6.0], [-4.0, -7.0]], [1, 2, 2, 2, 79]), ('D_cell_r3c3_fill', [[-3.0, -7.0], [-2.0, -7.0], [-2.0, -6.0], [-3.0, -6.0], [-3.0, -7.0]], [1, 2, 2, 2, 79]), ('D_cell_r4c1_fill', [[-5.0, -8.0], [-4.0, -8.0], [-4.0, -7.0], [-5.0, -7.0], [-5.0, -8.0]], [1, 2, 2, 2, 79]), ('D_cell_r4c2_fill', [[-4.0, -8.0], [-3.0, -8.0], [-3.0, -7.0], [-4.0, -7.0], [-4.0, -8.0]], [1, 2, 2, 2, 79]), ('D_cell_r4c3_fill', [[-3.0, -8.0], [-2.0, -8.0], [-2.0, -7.0], [-3.0, -7.0], [-3.0, -8.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.0, -8.0], [-1.0, -8.0], [-1.0, -7.0], [-2.0, -7.0], [-2.0, -8.0]], [1, 2, 2, 2, 79], id='D_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_05:
                c.line(points, id=object_id)
            c.path([[1.0, -5.0], [2.0, -5.0], [2.0, -4.0], [1.0, -4.0], [1.0, -5.0]], [1, 2, 2, 2, 79], id='E_cell_r1c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[1.0, -6.0], [2.0, -6.0], [2.0, -5.0], [1.0, -5.0], [1.0, -6.0]], [1, 2, 2, 2, 79], id='E_cell_r2c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('E_cell_r2c2_fill', [[2.0, -6.0], [3.0, -6.0], [3.0, -5.0], [2.0, -5.0], [2.0, -6.0]], [1, 2, 2, 2, 79]), ('E_cell_r3c1_fill', [[1.0, -7.0], [2.0, -7.0], [2.0, -6.0], [1.0, -6.0], [1.0, -7.0]], [1, 2, 2, 2, 79]), ('E_cell_r3c2_fill', [[2.0, -7.0], [3.0, -7.0], [3.0, -6.0], [2.0, -6.0], [2.0, -7.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[3.0, -7.0], [4.0, -7.0], [4.0, -6.0], [3.0, -6.0], [3.0, -7.0]], [1, 2, 2, 2, 79], id='E_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[1.0, -8.0], [2.0, -8.0], [2.0, -7.0], [1.0, -7.0], [1.0, -8.0]], [1, 2, 2, 2, 79], id='E_cell_r4c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('E_cell_r4c2_fill', [[2.0, -8.0], [3.0, -8.0], [3.0, -7.0], [2.0, -7.0], [2.0, -8.0]], [1, 2, 2, 2, 79]), ('E_cell_r4c3_fill', [[3.0, -8.0], [4.0, -8.0], [4.0, -7.0], [3.0, -7.0], [3.0, -8.0]], [1, 2, 2, 2, 79]), ('E_cell_r4c4_fill', [[4.0, -8.0], [5.0, -8.0], [5.0, -7.0], [4.0, -7.0], [4.0, -8.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_06:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('A_label', '(A)', [-6, -2.6]), ('B_label', '(B)', [0, -2.6]), ('C_label', '(C)', [6, -2.6]), ('D_label', '(D)', [-3.0, -8.6]), ('E_label', '(E)', [3.0, -8.6])]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane531().draw(sys.argv[1] if len(sys.argv) > 1 else None))
