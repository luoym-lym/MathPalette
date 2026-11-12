"""Frozen question Plane534; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane534:

    def __init__(self):
        self.id = 'Plane534'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane159/extension_05'
        self.question = 'A pattern consists of white, grey and black squares.\nFirst, exchange black and white at the same time: every black square becomes white and every white square becomes black, while grey squares stay grey. Then replace all grey squares with black squares. Finally, replace all white squares with grey squares. Which picture shows the resulting pattern?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self._geometry_01 = [('initial_edge_000', [[0.5, 8.5], [-0.5, 8.5]]),
         ('initial_edge_001', [[0.5, 8.5], [0.5, 9.5]]),
         ('initial_edge_002', [[0.5, 9.5], [-0.5, 9.5]]),
         ('initial_edge_003', [[-0.5, 9.5], [-0.5, 8.5]]),
         ('initial_edge_004', [[-0.5, 7.5], [-1.5, 7.5]]),
         ('initial_edge_005', [[-0.5, 8.5], [-0.5, 7.5]]),
         ('initial_edge_006', [[-0.5, 8.5], [-1.5, 8.5]]),
         ('initial_edge_007', [[-1.5, 8.5], [-1.5, 7.5]]),
         ('initial_edge_008', [[0.5, 7.5], [-0.5, 7.5]]),
         ('initial_edge_009', [[0.5, 8.5], [0.5, 7.5]]),
         ('initial_edge_010', [[1.5, 7.5], [0.5, 7.5]]),
         ('initial_edge_011', [[1.5, 7.5], [1.5, 8.5]]),
         ('initial_edge_012', [[1.5, 8.5], [0.5, 8.5]]),
         ('initial_edge_013', [[-2.5, 6.5], [-1.5, 6.5]]),
         ('initial_edge_014', [[-1.5, 7.5], [-1.5, 6.5]]),
         ('initial_edge_015', [[-1.5, 7.5], [-2.5, 7.5]]),
         ('initial_edge_016', [[-2.5, 7.5], [-2.5, 6.5]]),
         ('initial_edge_017', [[-0.5, 6.5], [-1.5, 6.5]]),
         ('initial_edge_018', [[-0.5, 7.5], [-0.5, 6.5]]),
         ('initial_edge_019', [[0.5, 6.5], [-0.5, 6.5]]),
         ('initial_edge_020', [[0.5, 7.5], [0.5, 6.5]]),
         ('initial_edge_021', [[1.5, 6.5], [0.5, 6.5]]),
         ('initial_edge_022', [[1.5, 7.5], [1.5, 6.5]]),
         ('initial_edge_023', [[1.5, 6.5], [2.5, 6.5]]),
         ('initial_edge_024', [[2.5, 6.5], [2.5, 7.5]]),
         ('initial_edge_025', [[2.5, 7.5], [1.5, 7.5]]),
         ('initial_edge_026', [[-1.5, 5.5], [-0.5, 5.5]]),
         ('initial_edge_027', [[-0.5, 6.5], [-0.5, 5.5]]),
         ('initial_edge_028', [[-1.5, 6.5], [-1.5, 5.5]]),
         ('initial_edge_029', [[0.5, 5.5], [-0.5, 5.5]]),
         ('initial_edge_030', [[0.5, 6.5], [0.5, 5.5]]),
         ('initial_edge_031', [[0.5, 5.5], [1.5, 5.5]]),
         ('initial_edge_032', [[1.5, 5.5], [1.5, 6.5]]),
         ('initial_edge_033', [[-0.5, 4.5], [0.5, 4.5]]),
         ('initial_edge_034', [[0.5, 4.5], [0.5, 5.5]]),
         ('initial_edge_035', [[-0.5, 5.5], [-0.5, 4.5]])]
        self._geometry_02 = [('A_edge_000', [[-6.5, 1.5], [-7.5, 1.5]]),
         ('A_edge_001', [[-6.5, 1.5], [-6.5, 2.5]]),
         ('A_edge_002', [[-6.5, 2.5], [-7.5, 2.5]]),
         ('A_edge_003', [[-7.5, 2.5], [-7.5, 1.5]]),
         ('A_edge_004', [[-7.5, 0.5], [-8.5, 0.5]]),
         ('A_edge_005', [[-7.5, 1.5], [-7.5, 0.5]]),
         ('A_edge_006', [[-7.5, 1.5], [-8.5, 1.5]]),
         ('A_edge_007', [[-8.5, 1.5], [-8.5, 0.5]]),
         ('A_edge_008', [[-6.5, 0.5], [-7.5, 0.5]]),
         ('A_edge_009', [[-6.5, 1.5], [-6.5, 0.5]]),
         ('A_edge_010', [[-5.5, 0.5], [-6.5, 0.5]]),
         ('A_edge_011', [[-5.5, 0.5], [-5.5, 1.5]]),
         ('A_edge_012', [[-5.5, 1.5], [-6.5, 1.5]]),
         ('A_edge_013', [[-9.5, -0.5], [-8.5, -0.5]]),
         ('A_edge_014', [[-8.5, 0.5], [-8.5, -0.5]]),
         ('A_edge_015', [[-8.5, 0.5], [-9.5, 0.5]]),
         ('A_edge_016', [[-9.5, 0.5], [-9.5, -0.5]]),
         ('A_edge_017', [[-7.5, -0.5], [-8.5, -0.5]]),
         ('A_edge_018', [[-7.5, 0.5], [-7.5, -0.5]]),
         ('A_edge_019', [[-6.5, -0.5], [-7.5, -0.5]]),
         ('A_edge_020', [[-6.5, 0.5], [-6.5, -0.5]]),
         ('A_edge_021', [[-5.5, -0.5], [-6.5, -0.5]]),
         ('A_edge_022', [[-5.5, 0.5], [-5.5, -0.5]]),
         ('A_edge_023', [[-5.5, -0.5], [-4.5, -0.5]]),
         ('A_edge_024', [[-4.5, -0.5], [-4.5, 0.5]]),
         ('A_edge_025', [[-4.5, 0.5], [-5.5, 0.5]]),
         ('A_edge_026', [[-8.5, -1.5], [-7.5, -1.5]]),
         ('A_edge_027', [[-7.5, -0.5], [-7.5, -1.5]]),
         ('A_edge_028', [[-8.5, -0.5], [-8.5, -1.5]]),
         ('A_edge_029', [[-6.5, -1.5], [-7.5, -1.5]]),
         ('A_edge_030', [[-6.5, -0.5], [-6.5, -1.5]]),
         ('A_edge_031', [[-6.5, -1.5], [-5.5, -1.5]]),
         ('A_edge_032', [[-5.5, -1.5], [-5.5, -0.5]]),
         ('A_edge_033', [[-7.5, -2.5], [-6.5, -2.5]]),
         ('A_edge_034', [[-6.5, -2.5], [-6.5, -1.5]]),
         ('A_edge_035', [[-7.5, -1.5], [-7.5, -2.5]])]
        self._geometry_03 = [('B_edge_000', [[0.5, 1.5], [-0.5, 1.5]]),
         ('B_edge_001', [[0.5, 1.5], [0.5, 2.5]]),
         ('B_edge_002', [[0.5, 2.5], [-0.5, 2.5]]),
         ('B_edge_003', [[-0.5, 2.5], [-0.5, 1.5]]),
         ('B_edge_004', [[-0.5, 0.5], [-1.5, 0.5]]),
         ('B_edge_005', [[-0.5, 1.5], [-0.5, 0.5]]),
         ('B_edge_006', [[-0.5, 1.5], [-1.5, 1.5]]),
         ('B_edge_007', [[-1.5, 1.5], [-1.5, 0.5]]),
         ('B_edge_008', [[0.5, 0.5], [-0.5, 0.5]]),
         ('B_edge_009', [[0.5, 1.5], [0.5, 0.5]]),
         ('B_edge_010', [[1.5, 0.5], [0.5, 0.5]]),
         ('B_edge_011', [[1.5, 0.5], [1.5, 1.5]]),
         ('B_edge_012', [[1.5, 1.5], [0.5, 1.5]]),
         ('B_edge_013', [[-2.5, -0.5], [-1.5, -0.5]]),
         ('B_edge_014', [[-1.5, 0.5], [-1.5, -0.5]]),
         ('B_edge_015', [[-1.5, 0.5], [-2.5, 0.5]]),
         ('B_edge_016', [[-2.5, 0.5], [-2.5, -0.5]]),
         ('B_edge_017', [[-0.5, -0.5], [-1.5, -0.5]]),
         ('B_edge_018', [[-0.5, 0.5], [-0.5, -0.5]]),
         ('B_edge_019', [[0.5, -0.5], [-0.5, -0.5]]),
         ('B_edge_020', [[0.5, 0.5], [0.5, -0.5]]),
         ('B_edge_021', [[1.5, -0.5], [0.5, -0.5]]),
         ('B_edge_022', [[1.5, 0.5], [1.5, -0.5]]),
         ('B_edge_023', [[1.5, -0.5], [2.5, -0.5]]),
         ('B_edge_024', [[2.5, -0.5], [2.5, 0.5]]),
         ('B_edge_025', [[2.5, 0.5], [1.5, 0.5]]),
         ('B_edge_026', [[-1.5, -1.5], [-0.5, -1.5]]),
         ('B_edge_027', [[-0.5, -0.5], [-0.5, -1.5]]),
         ('B_edge_028', [[-1.5, -0.5], [-1.5, -1.5]]),
         ('B_edge_029', [[0.5, -1.5], [-0.5, -1.5]]),
         ('B_edge_030', [[0.5, -0.5], [0.5, -1.5]]),
         ('B_edge_031', [[0.5, -1.5], [1.5, -1.5]]),
         ('B_edge_032', [[1.5, -1.5], [1.5, -0.5]]),
         ('B_edge_033', [[-0.5, -2.5], [0.5, -2.5]]),
         ('B_edge_034', [[0.5, -2.5], [0.5, -1.5]]),
         ('B_edge_035', [[-0.5, -1.5], [-0.5, -2.5]])]
        self._geometry_04 = [('C_edge_000', [[7.5, 1.5], [6.5, 1.5]]),
         ('C_edge_001', [[7.5, 1.5], [7.5, 2.5]]),
         ('C_edge_002', [[7.5, 2.5], [6.5, 2.5]]),
         ('C_edge_003', [[6.5, 2.5], [6.5, 1.5]]),
         ('C_edge_004', [[6.5, 0.5], [5.5, 0.5]]),
         ('C_edge_005', [[6.5, 1.5], [6.5, 0.5]]),
         ('C_edge_006', [[6.5, 1.5], [5.5, 1.5]]),
         ('C_edge_007', [[5.5, 1.5], [5.5, 0.5]]),
         ('C_edge_008', [[7.5, 0.5], [6.5, 0.5]]),
         ('C_edge_009', [[7.5, 1.5], [7.5, 0.5]]),
         ('C_edge_010', [[8.5, 0.5], [7.5, 0.5]]),
         ('C_edge_011', [[8.5, 0.5], [8.5, 1.5]]),
         ('C_edge_012', [[8.5, 1.5], [7.5, 1.5]]),
         ('C_edge_013', [[4.5, -0.5], [5.5, -0.5]]),
         ('C_edge_014', [[5.5, 0.5], [5.5, -0.5]]),
         ('C_edge_015', [[5.5, 0.5], [4.5, 0.5]]),
         ('C_edge_016', [[4.5, 0.5], [4.5, -0.5]]),
         ('C_edge_017', [[6.5, -0.5], [5.5, -0.5]]),
         ('C_edge_018', [[6.5, 0.5], [6.5, -0.5]]),
         ('C_edge_019', [[7.5, -0.5], [6.5, -0.5]]),
         ('C_edge_020', [[7.5, 0.5], [7.5, -0.5]]),
         ('C_edge_021', [[8.5, -0.5], [7.5, -0.5]]),
         ('C_edge_022', [[8.5, 0.5], [8.5, -0.5]]),
         ('C_edge_023', [[8.5, -0.5], [9.5, -0.5]]),
         ('C_edge_024', [[9.5, -0.5], [9.5, 0.5]]),
         ('C_edge_025', [[9.5, 0.5], [8.5, 0.5]]),
         ('C_edge_026', [[5.5, -1.5], [6.5, -1.5]]),
         ('C_edge_027', [[6.5, -0.5], [6.5, -1.5]]),
         ('C_edge_028', [[5.5, -0.5], [5.5, -1.5]]),
         ('C_edge_029', [[7.5, -1.5], [6.5, -1.5]]),
         ('C_edge_030', [[7.5, -0.5], [7.5, -1.5]]),
         ('C_edge_031', [[7.5, -1.5], [8.5, -1.5]]),
         ('C_edge_032', [[8.5, -1.5], [8.5, -0.5]]),
         ('C_edge_033', [[6.5, -2.5], [7.5, -2.5]]),
         ('C_edge_034', [[7.5, -2.5], [7.5, -1.5]]),
         ('C_edge_035', [[6.5, -1.5], [6.5, -2.5]])]
        self._geometry_05 = [('D_edge_000', [[-3.0, -5.5], [-4.0, -5.5]]),
         ('D_edge_001', [[-3.0, -5.5], [-3.0, -4.5]]),
         ('D_edge_002', [[-3.0, -4.5], [-4.0, -4.5]]),
         ('D_edge_003', [[-4.0, -4.5], [-4.0, -5.5]]),
         ('D_edge_004', [[-4.0, -6.5], [-5.0, -6.5]]),
         ('D_edge_005', [[-4.0, -5.5], [-4.0, -6.5]]),
         ('D_edge_006', [[-4.0, -5.5], [-5.0, -5.5]]),
         ('D_edge_007', [[-5.0, -5.5], [-5.0, -6.5]]),
         ('D_edge_008', [[-3.0, -6.5], [-4.0, -6.5]]),
         ('D_edge_009', [[-3.0, -5.5], [-3.0, -6.5]]),
         ('D_edge_010', [[-2.0, -6.5], [-3.0, -6.5]]),
         ('D_edge_011', [[-2.0, -6.5], [-2.0, -5.5]]),
         ('D_edge_012', [[-2.0, -5.5], [-3.0, -5.5]]),
         ('D_edge_013', [[-6.0, -7.5], [-5.0, -7.5]]),
         ('D_edge_014', [[-5.0, -6.5], [-5.0, -7.5]]),
         ('D_edge_015', [[-5.0, -6.5], [-6.0, -6.5]]),
         ('D_edge_016', [[-6.0, -6.5], [-6.0, -7.5]]),
         ('D_edge_017', [[-4.0, -7.5], [-5.0, -7.5]]),
         ('D_edge_018', [[-4.0, -6.5], [-4.0, -7.5]]),
         ('D_edge_019', [[-3.0, -7.5], [-4.0, -7.5]]),
         ('D_edge_020', [[-3.0, -6.5], [-3.0, -7.5]]),
         ('D_edge_021', [[-2.0, -7.5], [-3.0, -7.5]]),
         ('D_edge_022', [[-2.0, -6.5], [-2.0, -7.5]]),
         ('D_edge_023', [[-2.0, -7.5], [-1.0, -7.5]]),
         ('D_edge_024', [[-1.0, -7.5], [-1.0, -6.5]]),
         ('D_edge_025', [[-1.0, -6.5], [-2.0, -6.5]]),
         ('D_edge_026', [[-5.0, -8.5], [-4.0, -8.5]]),
         ('D_edge_027', [[-4.0, -7.5], [-4.0, -8.5]]),
         ('D_edge_028', [[-5.0, -7.5], [-5.0, -8.5]]),
         ('D_edge_029', [[-3.0, -8.5], [-4.0, -8.5]]),
         ('D_edge_030', [[-3.0, -7.5], [-3.0, -8.5]]),
         ('D_edge_031', [[-3.0, -8.5], [-2.0, -8.5]]),
         ('D_edge_032', [[-2.0, -8.5], [-2.0, -7.5]]),
         ('D_edge_033', [[-4.0, -9.5], [-3.0, -9.5]]),
         ('D_edge_034', [[-3.0, -9.5], [-3.0, -8.5]]),
         ('D_edge_035', [[-4.0, -8.5], [-4.0, -9.5]])]
        self._geometry_06 = [('E_edge_000', [[4.0, -5.5], [3.0, -5.5]]),
         ('E_edge_001', [[4.0, -5.5], [4.0, -4.5]]),
         ('E_edge_002', [[4.0, -4.5], [3.0, -4.5]]),
         ('E_edge_003', [[3.0, -4.5], [3.0, -5.5]]),
         ('E_edge_004', [[3.0, -6.5], [2.0, -6.5]]),
         ('E_edge_005', [[3.0, -5.5], [3.0, -6.5]]),
         ('E_edge_006', [[3.0, -5.5], [2.0, -5.5]]),
         ('E_edge_007', [[2.0, -5.5], [2.0, -6.5]]),
         ('E_edge_008', [[4.0, -6.5], [3.0, -6.5]]),
         ('E_edge_009', [[4.0, -5.5], [4.0, -6.5]]),
         ('E_edge_010', [[5.0, -6.5], [4.0, -6.5]]),
         ('E_edge_011', [[5.0, -6.5], [5.0, -5.5]]),
         ('E_edge_012', [[5.0, -5.5], [4.0, -5.5]]),
         ('E_edge_013', [[1.0, -7.5], [2.0, -7.5]]),
         ('E_edge_014', [[2.0, -6.5], [2.0, -7.5]]),
         ('E_edge_015', [[2.0, -6.5], [1.0, -6.5]]),
         ('E_edge_016', [[1.0, -6.5], [1.0, -7.5]]),
         ('E_edge_017', [[3.0, -7.5], [2.0, -7.5]]),
         ('E_edge_018', [[3.0, -6.5], [3.0, -7.5]]),
         ('E_edge_019', [[4.0, -7.5], [3.0, -7.5]]),
         ('E_edge_020', [[4.0, -6.5], [4.0, -7.5]]),
         ('E_edge_021', [[5.0, -7.5], [4.0, -7.5]]),
         ('E_edge_022', [[5.0, -6.5], [5.0, -7.5]]),
         ('E_edge_023', [[5.0, -7.5], [6.0, -7.5]]),
         ('E_edge_024', [[6.0, -7.5], [6.0, -6.5]]),
         ('E_edge_025', [[6.0, -6.5], [5.0, -6.5]]),
         ('E_edge_026', [[2.0, -8.5], [3.0, -8.5]]),
         ('E_edge_027', [[3.0, -7.5], [3.0, -8.5]]),
         ('E_edge_028', [[2.0, -7.5], [2.0, -8.5]]),
         ('E_edge_029', [[4.0, -8.5], [3.0, -8.5]]),
         ('E_edge_030', [[4.0, -7.5], [4.0, -8.5]]),
         ('E_edge_031', [[4.0, -8.5], [5.0, -8.5]]),
         ('E_edge_032', [[5.0, -8.5], [5.0, -7.5]]),
         ('E_edge_033', [[3.0, -9.5], [4.0, -9.5]]),
         ('E_edge_034', [[4.0, -9.5], [4.0, -8.5]]),
         ('E_edge_035', [[3.0, -8.5], [3.0, -9.5]])]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane534.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-10.454773620915823, 10.454773620915823], ylim=[-10.92371487970228, 9.985832362129367], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[-0.5, 8.5], [0.5, 8.5], [0.5, 9.5], [-0.5, 9.5], [-0.5, 8.5]], [1, 2, 2, 2, 79], id='initial_cell_r1c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.5, 7.5], [-0.5, 7.5], [-0.5, 8.5], [-1.5, 8.5], [-1.5, 7.5]], [1, 2, 2, 2, 79], id='initial_cell_r2c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, 7.5], [0.5, 7.5], [0.5, 8.5], [-0.5, 8.5], [-0.5, 7.5]], [1, 2, 2, 2, 79], id='initial_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, 7.5], [1.5, 7.5], [1.5, 8.5], [0.5, 8.5], [0.5, 7.5]], [1, 2, 2, 2, 79], id='initial_cell_r2c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.5, 6.5], [-1.5, 6.5], [-1.5, 7.5], [-2.5, 7.5], [-2.5, 6.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.5, 6.5], [-0.5, 6.5], [-0.5, 7.5], [-1.5, 7.5], [-1.5, 6.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, 6.5], [0.5, 6.5], [0.5, 7.5], [-0.5, 7.5], [-0.5, 6.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, 6.5], [1.5, 6.5], [1.5, 7.5], [0.5, 7.5], [0.5, 6.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[1.5, 6.5], [2.5, 6.5], [2.5, 7.5], [1.5, 7.5], [1.5, 6.5]], [1, 2, 2, 2, 79], id='initial_cell_r3c5_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-1.5, 5.5], [-0.5, 5.5], [-0.5, 6.5], [-1.5, 6.5], [-1.5, 5.5]], [1, 2, 2, 2, 79], id='initial_cell_r4c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, 5.5], [0.5, 5.5], [0.5, 6.5], [-0.5, 6.5], [-0.5, 5.5]], [1, 2, 2, 2, 79], id='initial_cell_r4c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[0.5, 5.5], [1.5, 5.5], [1.5, 6.5], [0.5, 6.5], [0.5, 5.5]], [1, 2, 2, 2, 79], id='initial_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-0.5, 4.5], [0.5, 4.5], [0.5, 5.5], [-0.5, 5.5], [-0.5, 4.5]], [1, 2, 2, 2, 79], id='initial_cell_r5c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id)
            c.path([[-7.5, 1.5], [-6.5, 1.5], [-6.5, 2.5], [-7.5, 2.5], [-7.5, 1.5]], [1, 2, 2, 2, 79], id='A_cell_r1c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-8.5, 0.5], [-7.5, 0.5], [-7.5, 1.5], [-8.5, 1.5], [-8.5, 0.5]], [1, 2, 2, 2, 79], id='A_cell_r2c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-7.5, 0.5], [-6.5, 0.5], [-6.5, 1.5], [-7.5, 1.5], [-7.5, 0.5]], [1, 2, 2, 2, 79], id='A_cell_r2c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-6.5, 0.5], [-5.5, 0.5], [-5.5, 1.5], [-6.5, 1.5], [-6.5, 0.5]], [1, 2, 2, 2, 79], id='A_cell_r2c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-9.5, -0.5], [-8.5, -0.5], [-8.5, 0.5], [-9.5, 0.5], [-9.5, -0.5]], [1, 2, 2, 2, 79], id='A_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-8.5, -0.5], [-7.5, -0.5], [-7.5, 0.5], [-8.5, 0.5], [-8.5, -0.5]], [1, 2, 2, 2, 79], id='A_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-7.5, -0.5], [-6.5, -0.5], [-6.5, 0.5], [-7.5, 0.5], [-7.5, -0.5]], [1, 2, 2, 2, 79], id='A_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-6.5, -0.5], [-5.5, -0.5], [-5.5, 0.5], [-6.5, 0.5], [-6.5, -0.5]], [1, 2, 2, 2, 79], id='A_cell_r3c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-5.5, -0.5], [-4.5, -0.5], [-4.5, 0.5], [-5.5, 0.5], [-5.5, -0.5]], [1, 2, 2, 2, 79], id='A_cell_r3c5_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-8.5, -1.5], [-7.5, -1.5], [-7.5, -0.5], [-8.5, -0.5], [-8.5, -1.5]], [1, 2, 2, 2, 79], id='A_cell_r4c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-7.5, -1.5], [-6.5, -1.5], [-6.5, -0.5], [-7.5, -0.5], [-7.5, -1.5]], [1, 2, 2, 2, 79], id='A_cell_r4c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-6.5, -1.5], [-5.5, -1.5], [-5.5, -0.5], [-6.5, -0.5], [-6.5, -1.5]], [1, 2, 2, 2, 79], id='A_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-7.5, -2.5], [-6.5, -2.5], [-6.5, -1.5], [-7.5, -1.5], [-7.5, -2.5]], [1, 2, 2, 2, 79], id='A_cell_r5c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id)
            for object_id, vertices, codes in [('B_cell_r1c3_fill', [[-0.5, 1.5], [0.5, 1.5], [0.5, 2.5], [-0.5, 2.5], [-0.5, 1.5]], [1, 2, 2, 2, 79]), ('B_cell_r2c2_fill', [[-1.5, 0.5], [-0.5, 0.5], [-0.5, 1.5], [-1.5, 1.5], [-1.5, 0.5]], [1, 2, 2, 2, 79]), ('B_cell_r2c3_fill', [[-0.5, 0.5], [0.5, 0.5], [0.5, 1.5], [-0.5, 1.5], [-0.5, 0.5]], [1, 2, 2, 2, 79]), ('B_cell_r2c4_fill', [[0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5], [0.5, 0.5]], [1, 2, 2, 2, 79]), ('B_cell_r3c1_fill', [[-2.5, -0.5], [-1.5, -0.5], [-1.5, 0.5], [-2.5, 0.5], [-2.5, -0.5]], [1, 2, 2, 2, 79]), ('B_cell_r3c2_fill', [[-1.5, -0.5], [-0.5, -0.5], [-0.5, 0.5], [-1.5, 0.5], [-1.5, -0.5]], [1, 2, 2, 2, 79]), ('B_cell_r3c3_fill', [[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5], [-0.5, -0.5]], [1, 2, 2, 2, 79]), ('B_cell_r3c4_fill', [[0.5, -0.5], [1.5, -0.5], [1.5, 0.5], [0.5, 0.5], [0.5, -0.5]], [1, 2, 2, 2, 79]), ('B_cell_r3c5_fill', [[1.5, -0.5], [2.5, -0.5], [2.5, 0.5], [1.5, 0.5], [1.5, -0.5]], [1, 2, 2, 2, 79]), ('B_cell_r4c2_fill', [[-1.5, -1.5], [-0.5, -1.5], [-0.5, -0.5], [-1.5, -0.5], [-1.5, -1.5]], [1, 2, 2, 2, 79]), ('B_cell_r4c3_fill', [[-0.5, -1.5], [0.5, -1.5], [0.5, -0.5], [-0.5, -0.5], [-0.5, -1.5]], [1, 2, 2, 2, 79]), ('B_cell_r4c4_fill', [[0.5, -1.5], [1.5, -1.5], [1.5, -0.5], [0.5, -0.5], [0.5, -1.5]], [1, 2, 2, 2, 79]), ('B_cell_r5c3_fill', [[-0.5, -2.5], [0.5, -2.5], [0.5, -1.5], [-0.5, -1.5], [-0.5, -2.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id)
            c.path([[6.5, 1.5], [7.5, 1.5], [7.5, 2.5], [6.5, 2.5], [6.5, 1.5]], [1, 2, 2, 2, 79], id='C_cell_r1c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('C_cell_r2c2_fill', [[5.5, 0.5], [6.5, 0.5], [6.5, 1.5], [5.5, 1.5], [5.5, 0.5]], [1, 2, 2, 2, 79]), ('C_cell_r2c3_fill', [[6.5, 0.5], [7.5, 0.5], [7.5, 1.5], [6.5, 1.5], [6.5, 0.5]], [1, 2, 2, 2, 79]), ('C_cell_r2c4_fill', [[7.5, 0.5], [8.5, 0.5], [8.5, 1.5], [7.5, 1.5], [7.5, 0.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[4.5, -0.5], [5.5, -0.5], [5.5, 0.5], [4.5, 0.5], [4.5, -0.5]], [1, 2, 2, 2, 79], id='C_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[5.5, -0.5], [6.5, -0.5], [6.5, 0.5], [5.5, 0.5], [5.5, -0.5]], [1, 2, 2, 2, 79], id='C_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[6.5, -0.5], [7.5, -0.5], [7.5, 0.5], [6.5, 0.5], [6.5, -0.5]], [1, 2, 2, 2, 79], id='C_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[7.5, -0.5], [8.5, -0.5], [8.5, 0.5], [7.5, 0.5], [7.5, -0.5]], [1, 2, 2, 2, 79], id='C_cell_r3c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[8.5, -0.5], [9.5, -0.5], [9.5, 0.5], [8.5, 0.5], [8.5, -0.5]], [1, 2, 2, 2, 79], id='C_cell_r3c5_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[5.5, -1.5], [6.5, -1.5], [6.5, -0.5], [5.5, -0.5], [5.5, -1.5]], [1, 2, 2, 2, 79], id='C_cell_r4c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[6.5, -1.5], [7.5, -1.5], [7.5, -0.5], [6.5, -0.5], [6.5, -1.5]], [1, 2, 2, 2, 79], id='C_cell_r4c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[7.5, -1.5], [8.5, -1.5], [8.5, -0.5], [7.5, -0.5], [7.5, -1.5]], [1, 2, 2, 2, 79], id='C_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[6.5, -2.5], [7.5, -2.5], [7.5, -1.5], [6.5, -1.5], [6.5, -2.5]], [1, 2, 2, 2, 79], id='C_cell_r5c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_04:
                c.line(points, id=object_id)
            c.path([[-4.0, -5.5], [-3.0, -5.5], [-3.0, -4.5], [-4.0, -4.5], [-4.0, -5.5]], [1, 2, 2, 2, 79], id='D_cell_r1c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('D_cell_r2c2_fill', [[-5.0, -6.5], [-4.0, -6.5], [-4.0, -5.5], [-5.0, -5.5], [-5.0, -6.5]], [1, 2, 2, 2, 79]), ('D_cell_r2c3_fill', [[-4.0, -6.5], [-3.0, -6.5], [-3.0, -5.5], [-4.0, -5.5], [-4.0, -6.5]], [1, 2, 2, 2, 79]), ('D_cell_r2c4_fill', [[-3.0, -6.5], [-2.0, -6.5], [-2.0, -5.5], [-3.0, -5.5], [-3.0, -6.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-6.0, -7.5], [-5.0, -7.5], [-5.0, -6.5], [-6.0, -6.5], [-6.0, -7.5]], [1, 2, 2, 2, 79], id='D_cell_r3c1_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-5.0, -7.5], [-4.0, -7.5], [-4.0, -6.5], [-5.0, -6.5], [-5.0, -7.5]], [1, 2, 2, 2, 79], id='D_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-4.0, -7.5], [-3.0, -7.5], [-3.0, -6.5], [-4.0, -6.5], [-4.0, -7.5]], [1, 2, 2, 2, 79], id='D_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-3.0, -7.5], [-2.0, -7.5], [-2.0, -6.5], [-3.0, -6.5], [-3.0, -7.5]], [1, 2, 2, 2, 79], id='D_cell_r3c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-2.0, -7.5], [-1.0, -7.5], [-1.0, -6.5], [-2.0, -6.5], [-2.0, -7.5]], [1, 2, 2, 2, 79], id='D_cell_r3c5_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-5.0, -8.5], [-4.0, -8.5], [-4.0, -7.5], [-5.0, -7.5], [-5.0, -8.5]], [1, 2, 2, 2, 79], id='D_cell_r4c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-4.0, -8.5], [-3.0, -8.5], [-3.0, -7.5], [-4.0, -7.5], [-4.0, -8.5]], [1, 2, 2, 2, 79], id='D_cell_r4c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-3.0, -8.5], [-2.0, -8.5], [-2.0, -7.5], [-3.0, -7.5], [-3.0, -8.5]], [1, 2, 2, 2, 79], id='D_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[-4.0, -9.5], [-3.0, -9.5], [-3.0, -8.5], [-4.0, -8.5], [-4.0, -9.5]], [1, 2, 2, 2, 79], id='D_cell_r5c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_05:
                c.line(points, id=object_id)
            c.path([[3.0, -5.5], [4.0, -5.5], [4.0, -4.5], [3.0, -4.5], [3.0, -5.5]], [1, 2, 2, 2, 79], id='E_cell_r1c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[2.0, -6.5], [3.0, -6.5], [3.0, -5.5], [2.0, -5.5], [2.0, -6.5]], [1, 2, 2, 2, 79], id='E_cell_r2c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, vertices, codes in [('E_cell_r2c3_fill', [[3.0, -6.5], [4.0, -6.5], [4.0, -5.5], [3.0, -5.5], [3.0, -6.5]], [1, 2, 2, 2, 79]), ('E_cell_r2c4_fill', [[4.0, -6.5], [5.0, -6.5], [5.0, -5.5], [4.0, -5.5], [4.0, -6.5]], [1, 2, 2, 2, 79]), ('E_cell_r3c1_fill', [[1.0, -7.5], [2.0, -7.5], [2.0, -6.5], [1.0, -6.5], [1.0, -7.5]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[2.0, -7.5], [3.0, -7.5], [3.0, -6.5], [2.0, -6.5], [2.0, -7.5]], [1, 2, 2, 2, 79], id='E_cell_r3c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[3.0, -7.5], [4.0, -7.5], [4.0, -6.5], [3.0, -6.5], [3.0, -7.5]], [1, 2, 2, 2, 79], id='E_cell_r3c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[4.0, -7.5], [5.0, -7.5], [5.0, -6.5], [4.0, -6.5], [4.0, -7.5]], [1, 2, 2, 2, 79], id='E_cell_r3c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[5.0, -7.5], [6.0, -7.5], [6.0, -6.5], [5.0, -6.5], [5.0, -7.5]], [1, 2, 2, 2, 79], id='E_cell_r3c5_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[2.0, -8.5], [3.0, -8.5], [3.0, -7.5], [2.0, -7.5], [2.0, -8.5]], [1, 2, 2, 2, 79], id='E_cell_r4c2_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[3.0, -8.5], [4.0, -8.5], [4.0, -7.5], [3.0, -7.5], [3.0, -8.5]], [1, 2, 2, 2, 79], id='E_cell_r4c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[4.0, -8.5], [5.0, -8.5], [5.0, -7.5], [4.0, -7.5], [4.0, -8.5]], [1, 2, 2, 2, 79], id='E_cell_r4c4_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            c.path([[3.0, -9.5], [4.0, -9.5], [4.0, -8.5], [3.0, -8.5], [3.0, -9.5]], [1, 2, 2, 2, 79], id='E_cell_r5c3_fill', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.6, 0.6, 0.6, 1.0], linewidth=0.0, capstyle='butt', antialiased=False)
            for object_id, points in self._geometry_06:
                c.line(points, id=object_id)
            for object_id, text, anchor in [('A_label', '(A)', [-7, -3.1]), ('B_label', '(B)', [0, -3.1]), ('C_label', '(C)', [7, -3.1]), ('D_label', '(D)', [-3.5, -10.1]), ('E_label', '(E)', [3.5, -10.1])]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane534().draw(sys.argv[1] if len(sys.argv) > 1 else None))
