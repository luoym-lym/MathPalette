"""Frozen question Solid179; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid179:

    def __init__(self):
        self.id = 'Solid179'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1650'
        self.question = 'The faces of a cube are painted black, white or grey. Each face is only painted one colour and opposite faces are painted the same colour. Which of the following is a possible net for the cube?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid179.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.7940267233846363, 32.850074649202696], ylim=[-16.961778133088924, 16.682323239498412], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell0_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell1_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell2_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79], id='A_cell3_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[1.0, 1.0], [2.0, 1.0], [2.0, 2.0], [1.0, 2.0], [1.0, 1.0]], [1, 2, 2, 2, 79], id='A_cell1_1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[2.0, -1.0], [3.0, -1.0], [3.0, 0.0], [2.0, 0.0], [2.0, -1.0]], [1, 2, 2, 2, 79], id='A_cell2_-1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('A_netedge0', [[0.0, 0.0], [0.0, 1.0]]), ('A_netedge1', [[0.0, 0.0], [1.0, 0.0]]), ('A_netedge2', [[0.0, 1.0], [1.0, 1.0]]), ('A_netedge3', [[1.0, 0.0], [1.0, 1.0]]), ('A_netedge4', [[1.0, 0.0], [2.0, 0.0]]), ('A_netedge5', [[1.0, 1.0], [1.0, 2.0]]), ('A_netedge6', [[1.0, 1.0], [2.0, 1.0]]), ('A_netedge7', [[1.0, 2.0], [2.0, 2.0]]), ('A_netedge8', [[2.0, -1.0], [2.0, 0.0]]), ('A_netedge9', [[2.0, -1.0], [3.0, -1.0]]), ('A_netedge10', [[2.0, 0.0], [2.0, 1.0]]), ('A_netedge11', [[2.0, 0.0], [3.0, 0.0]]), ('A_netedge12', [[2.0, 1.0], [2.0, 2.0]]), ('A_netedge13', [[2.0, 1.0], [3.0, 1.0]]), ('A_netedge14', [[3.0, -1.0], [3.0, 0.0]]), ('A_netedge15', [[3.0, 0.0], [3.0, 1.0]]), ('A_netedge16', [[3.0, 0.0], [4.0, 0.0]]), ('A_netedge17', [[3.0, 1.0], [4.0, 1.0]]), ('A_netedge18', [[4.0, 0.0], [4.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell0_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell1_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell2_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.0, 0.0], [11.0, 0.0], [11.0, 1.0], [10.0, 1.0], [10.0, 0.0]], [1, 2, 2, 2, 79], id='B_cell3_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79], id='B_cell1_1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[10.0, -1.0], [11.0, -1.0], [11.0, 0.0], [10.0, 0.0], [10.0, -1.0]], [1, 2, 2, 2, 79], id='B_cell3_-1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('B_netedge0', [[7.0, 0.0], [7.0, 1.0]]), ('B_netedge1', [[7.0, 0.0], [8.0, 0.0]]), ('B_netedge2', [[7.0, 1.0], [8.0, 1.0]]), ('B_netedge3', [[8.0, 0.0], [8.0, 1.0]]), ('B_netedge4', [[8.0, 0.0], [9.0, 0.0]]), ('B_netedge5', [[8.0, 1.0], [8.0, 2.0]]), ('B_netedge6', [[8.0, 1.0], [9.0, 1.0]]), ('B_netedge7', [[8.0, 2.0], [9.0, 2.0]]), ('B_netedge8', [[9.0, 0.0], [9.0, 1.0]]), ('B_netedge9', [[9.0, 0.0], [10.0, 0.0]]), ('B_netedge10', [[9.0, 1.0], [9.0, 2.0]]), ('B_netedge11', [[9.0, 1.0], [10.0, 1.0]]), ('B_netedge12', [[10.0, -1.0], [10.0, 0.0]]), ('B_netedge13', [[10.0, -1.0], [11.0, -1.0]]), ('B_netedge14', [[10.0, 0.0], [10.0, 1.0]]), ('B_netedge15', [[10.0, 0.0], [11.0, 0.0]]), ('B_netedge16', [[10.0, 1.0], [11.0, 1.0]]), ('B_netedge17', [[11.0, -1.0], [11.0, 0.0]]), ('B_netedge18', [[11.0, 0.0], [11.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[14.0, 0.0], [15.0, 0.0], [15.0, 1.0], [14.0, 1.0], [14.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell0_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[15.0, 0.0], [16.0, 0.0], [16.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell1_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell2_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.0, 0.0], [18.0, 0.0], [18.0, 1.0], [17.0, 1.0], [17.0, 0.0]], [1, 2, 2, 2, 79], id='C_cell3_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.0, 1.0], [18.0, 1.0], [18.0, 2.0], [17.0, 2.0], [17.0, 1.0]], [1, 2, 2, 2, 79], id='C_cell3_1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[17.0, -1.0], [18.0, -1.0], [18.0, 0.0], [17.0, 0.0], [17.0, -1.0]], [1, 2, 2, 2, 79], id='C_cell3_-1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('C_netedge0', [[14.0, 0.0], [14.0, 1.0]]), ('C_netedge1', [[14.0, 0.0], [15.0, 0.0]]), ('C_netedge2', [[14.0, 1.0], [15.0, 1.0]]), ('C_netedge3', [[15.0, 0.0], [15.0, 1.0]]), ('C_netedge4', [[15.0, 0.0], [16.0, 0.0]]), ('C_netedge5', [[15.0, 1.0], [16.0, 1.0]]), ('C_netedge6', [[16.0, 0.0], [16.0, 1.0]]), ('C_netedge7', [[16.0, 0.0], [17.0, 0.0]]), ('C_netedge8', [[16.0, 1.0], [17.0, 1.0]]), ('C_netedge9', [[17.0, -1.0], [17.0, 0.0]]), ('C_netedge10', [[17.0, -1.0], [18.0, -1.0]]), ('C_netedge11', [[17.0, 0.0], [17.0, 1.0]]), ('C_netedge12', [[17.0, 0.0], [18.0, 0.0]]), ('C_netedge13', [[17.0, 1.0], [17.0, 2.0]]), ('C_netedge14', [[17.0, 1.0], [18.0, 1.0]]), ('C_netedge15', [[17.0, 2.0], [18.0, 2.0]]), ('C_netedge16', [[18.0, -1.0], [18.0, 0.0]]), ('C_netedge17', [[18.0, 0.0], [18.0, 1.0]]), ('C_netedge18', [[18.0, 1.0], [18.0, 2.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell0_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [22.0, 1.0], [22.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell1_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[23.0, 0.0], [24.0, 0.0], [24.0, 1.0], [23.0, 1.0], [23.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell2_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[24.0, 0.0], [25.0, 0.0], [25.0, 1.0], [24.0, 1.0], [24.0, 0.0]], [1, 2, 2, 2, 79], id='D_cell3_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[22.0, 1.0], [23.0, 1.0], [23.0, 2.0], [22.0, 2.0], [22.0, 1.0]], [1, 2, 2, 2, 79], id='D_cell1_1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[22.0, -1.0], [23.0, -1.0], [23.0, 0.0], [22.0, 0.0], [22.0, -1.0]], [1, 2, 2, 2, 79], id='D_cell1_-1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('D_netedge0', [[21.0, 0.0], [21.0, 1.0]]), ('D_netedge1', [[21.0, 0.0], [22.0, 0.0]]), ('D_netedge2', [[21.0, 1.0], [22.0, 1.0]]), ('D_netedge3', [[22.0, -1.0], [22.0, 0.0]]), ('D_netedge4', [[22.0, -1.0], [23.0, -1.0]]), ('D_netedge5', [[22.0, 0.0], [22.0, 1.0]]), ('D_netedge6', [[22.0, 0.0], [23.0, 0.0]]), ('D_netedge7', [[22.0, 1.0], [22.0, 2.0]]), ('D_netedge8', [[22.0, 1.0], [23.0, 1.0]]), ('D_netedge9', [[22.0, 2.0], [23.0, 2.0]]), ('D_netedge10', [[23.0, -1.0], [23.0, 0.0]]), ('D_netedge11', [[23.0, 0.0], [23.0, 1.0]]), ('D_netedge12', [[23.0, 0.0], [24.0, 0.0]]), ('D_netedge13', [[23.0, 1.0], [23.0, 2.0]]), ('D_netedge14', [[23.0, 1.0], [24.0, 1.0]]), ('D_netedge15', [[24.0, 0.0], [24.0, 1.0]]), ('D_netedge16', [[24.0, 0.0], [25.0, 0.0]]), ('D_netedge17', [[24.0, 1.0], [25.0, 1.0]]), ('D_netedge18', [[25.0, 0.0], [25.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.path([[28.0, 0.0], [29.0, 0.0], [29.0, 1.0], [28.0, 1.0], [28.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell0_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[29.0, 0.0], [30.0, 0.0], [30.0, 1.0], [29.0, 1.0], [29.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell1_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[30.0, 0.0], [31.0, 0.0], [31.0, 1.0], [30.0, 1.0], [30.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell2_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8, 0.8, 0.8, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[31.0, 0.0], [32.0, 0.0], [32.0, 1.0], [31.0, 1.0], [31.0, 0.0]], [1, 2, 2, 2, 79], id='E_cell3_0_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[31.0, 1.0], [32.0, 1.0], [32.0, 2.0], [31.0, 2.0], [31.0, 1.0]], [1, 2, 2, 2, 79], id='E_cell3_1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[29.0, -1.0], [30.0, -1.0], [30.0, 0.0], [29.0, 0.0], [29.0, -1.0]], [1, 2, 2, 2, 79], id='E_cell1_-1_fill', alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('E_netedge0', [[28.0, 0.0], [28.0, 1.0]]), ('E_netedge1', [[28.0, 0.0], [29.0, 0.0]]), ('E_netedge2', [[28.0, 1.0], [29.0, 1.0]]), ('E_netedge3', [[29.0, -1.0], [29.0, 0.0]]), ('E_netedge4', [[29.0, -1.0], [30.0, -1.0]]), ('E_netedge5', [[29.0, 0.0], [29.0, 1.0]]), ('E_netedge6', [[29.0, 0.0], [30.0, 0.0]]), ('E_netedge7', [[29.0, 1.0], [30.0, 1.0]]), ('E_netedge8', [[30.0, -1.0], [30.0, 0.0]]), ('E_netedge9', [[30.0, 0.0], [30.0, 1.0]]), ('E_netedge10', [[30.0, 0.0], [31.0, 0.0]]), ('E_netedge11', [[30.0, 1.0], [31.0, 1.0]]), ('E_netedge12', [[31.0, 0.0], [31.0, 1.0]]), ('E_netedge13', [[31.0, 0.0], [32.0, 0.0]]), ('E_netedge14', [[31.0, 1.0], [31.0, 2.0]]), ('E_netedge15', [[31.0, 1.0], [32.0, 1.0]]), ('E_netedge16', [[31.0, 2.0], [32.0, 2.0]]), ('E_netedge17', [[32.0, 0.0], [32.0, 1.0]]), ('E_netedge18', [[32.0, 1.0], [32.0, 2.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('label0', 'A', [2.0, -2.0]), ('label1', 'B', [9.0, -2.0]), ('label2', 'C', [16.0, -2.0]), ('label3', 'D', [23.0, -2.0]), ('label4', 'E', [30.0, -2.0])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid179().draw(sys.argv[1] if len(sys.argv) > 1 else None))
