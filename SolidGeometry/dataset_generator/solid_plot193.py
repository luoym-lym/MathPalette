"""Frozen question Solid193; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid193:

    def __init__(self):
        self.id = 'Solid193'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1843'
        self.question = 'One face of a cardboard cube is cut along its diagonals, as shown.\nWhich of the following are not nets for this cube?\nChoices:\nA:1 and 3\nB:1 and 5\nC:2 and 4\nD:2 and 4\nE:3 and 5'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': '1 and 3', 'B': '1 and 5', 'C': '2 and 4', 'D': '2 and 4', 'E': '3 and 5'}
        self.query = self.question
        self._geometry_01 = [('net1_netedge0', [[0.0, 0.0], [0.0, 1.0]]),
         ('net1_netedge1', [[0.0, 0.0], [1.0, 0.0]]),
         ('net1_netedge2', [[0.0, 1.0], [1.0, 1.0]]),
         ('net1_netedge3', [[1.0, 0.0], [1.0, 1.0]]),
         ('net1_netedge4', [[1.0, 0.0], [2.0, 0.0]]),
         ('net1_netedge5', [[1.0, 1.0], [2.0, 1.0]]),
         ('net1_netedge6', [[2.0, 0.0], [2.0, 1.0]]),
         ('net1_netedge7', [[2.0, 0.0], [3.0, 0.0]]),
         ('net1_netedge8', [[2.0, 1.0], [2.0, 2.0]]),
         ('net1_netedge9', [[2.0, 1.0], [3.0, 1.0]]),
         ('net1_netedge10', [[2.0, 2.0], [3.0, 2.0]]),
         ('net1_netedge11', [[3.0, 0.0], [3.0, 1.0]]),
         ('net1_netedge12', [[3.0, 0.0], [4.0, 0.0]]),
         ('net1_netedge13', [[3.0, 1.0], [3.0, 2.0]]),
         ('net1_netedge14', [[3.0, 1.0], [4.0, 1.0]]),
         ('net1_netedge15', [[4.0, 0.0], [4.0, 1.0]]),
         ('net0triangle0side0', [[0.0, 0.0], [0.5, -0.5]]),
         ('net0triangle0side1', [[1.0, 0.0], [0.5, -0.5]]),
         ('net0triangle1side0', [[1.0, 0.0], [1.5, -0.5]]),
         ('net0triangle1side1', [[2.0, 0.0], [1.5, -0.5]]),
         ('net0triangle2side0', [[2.0, 0.0], [2.5, -0.5]]),
         ('net0triangle2side1', [[3.0, 0.0], [2.5, -0.5]]),
         ('net0triangle3side0', [[3.0, 0.0], [3.5, -0.5]]),
         ('net0triangle3side1', [[4.0, 0.0], [3.5, -0.5]])]
        self._geometry_02 = [('net2_netedge0', [[7.0, 0.0], [7.0, 1.0]]),
         ('net2_netedge1', [[7.0, 0.0], [8.0, 0.0]]),
         ('net2_netedge2', [[7.0, 1.0], [8.0, 1.0]]),
         ('net2_netedge3', [[8.0, -1.0], [8.0, 0.0]]),
         ('net2_netedge4', [[8.0, -1.0], [9.0, -1.0]]),
         ('net2_netedge5', [[8.0, 0.0], [8.0, 1.0]]),
         ('net2_netedge6', [[8.0, 0.0], [9.0, 0.0]]),
         ('net2_netedge7', [[8.0, 1.0], [8.0, 2.0]]),
         ('net2_netedge8', [[8.0, 1.0], [9.0, 1.0]]),
         ('net2_netedge9', [[8.0, 2.0], [9.0, 2.0]]),
         ('net2_netedge10', [[9.0, -1.0], [9.0, 0.0]]),
         ('net2_netedge11', [[9.0, 0.0], [9.0, 1.0]]),
         ('net2_netedge12', [[9.0, 0.0], [10.0, 0.0]]),
         ('net2_netedge13', [[9.0, 1.0], [9.0, 2.0]]),
         ('net2_netedge14', [[9.0, 1.0], [10.0, 1.0]]),
         ('net2_netedge15', [[10.0, 0.0], [10.0, 1.0]]),
         ('net1triangle0side0', [[7.0, 0.0], [6.5, 0.5]]),
         ('net1triangle0side1', [[7.0, 1.0], [6.5, 0.5]]),
         ('net1triangle1side0', [[10.0, 0.0], [10.5, 0.5]]),
         ('net1triangle1side1', [[10.0, 1.0], [10.5, 0.5]]),
         ('net1triangle2side0', [[8.0, 2.0], [8.5, 2.5]]),
         ('net1triangle2side1', [[9.0, 2.0], [8.5, 2.5]]),
         ('net1triangle3side0', [[8.0, -1.0], [8.5, -1.5]]),
         ('net1triangle3side1', [[9.0, -1.0], [8.5, -1.5]])]
        self._geometry_03 = [('net3_netedge0', [[14.0, 0.0], [14.0, 1.0]]),
         ('net3_netedge1', [[14.0, 0.0], [15.0, 0.0]]),
         ('net3_netedge2', [[14.0, 1.0], [15.0, 1.0]]),
         ('net3_netedge3', [[15.0, 0.0], [15.0, 1.0]]),
         ('net3_netedge4', [[15.0, 0.0], [16.0, 0.0]]),
         ('net3_netedge5', [[15.0, 1.0], [16.0, 1.0]]),
         ('net3_netedge6', [[16.0, -1.0], [16.0, 0.0]]),
         ('net3_netedge7', [[16.0, -1.0], [17.0, -1.0]]),
         ('net3_netedge8', [[16.0, 0.0], [16.0, 1.0]]),
         ('net3_netedge9', [[16.0, 0.0], [17.0, 0.0]]),
         ('net3_netedge10', [[16.0, 1.0], [16.0, 2.0]]),
         ('net3_netedge11', [[16.0, 1.0], [17.0, 1.0]]),
         ('net3_netedge12', [[16.0, 2.0], [17.0, 2.0]]),
         ('net3_netedge13', [[17.0, -1.0], [17.0, 0.0]]),
         ('net3_netedge14', [[17.0, 0.0], [17.0, 1.0]]),
         ('net3_netedge15', [[17.0, 1.0], [17.0, 2.0]]),
         ('net2triangle0side0', [[14.0, 0.0], [13.5, 0.5]]),
         ('net2triangle0side1', [[14.0, 1.0], [13.5, 0.5]]),
         ('net2triangle1side0', [[17.0, 0.0], [17.5, 0.5]]),
         ('net2triangle1side1', [[17.0, 1.0], [17.5, 0.5]]),
         ('net2triangle2side0', [[16.0, 2.0], [16.5, 2.5]]),
         ('net2triangle2side1', [[17.0, 2.0], [16.5, 2.5]]),
         ('net2triangle3side0', [[16.0, -1.0], [16.5, -1.5]]),
         ('net2triangle3side1', [[17.0, -1.0], [16.5, -1.5]])]
        self._geometry_04 = [('net4_netedge0', [[21.0, 0.0], [21.0, 1.0]]),
         ('net4_netedge1', [[21.0, 0.0], [22.0, 0.0]]),
         ('net4_netedge2', [[21.0, 1.0], [22.0, 1.0]]),
         ('net4_netedge3', [[22.0, 0.0], [22.0, 1.0]]),
         ('net4_netedge4', [[22.0, 0.0], [23.0, 0.0]]),
         ('net4_netedge5', [[22.0, 1.0], [23.0, 1.0]]),
         ('net4_netedge6', [[23.0, -1.0], [23.0, 0.0]]),
         ('net4_netedge7', [[23.0, -1.0], [24.0, -1.0]]),
         ('net4_netedge8', [[23.0, 0.0], [23.0, 1.0]]),
         ('net4_netedge9', [[23.0, 0.0], [24.0, 0.0]]),
         ('net4_netedge10', [[23.0, 1.0], [23.0, 2.0]]),
         ('net4_netedge11', [[23.0, 1.0], [24.0, 1.0]]),
         ('net4_netedge12', [[23.0, 2.0], [24.0, 2.0]]),
         ('net4_netedge13', [[24.0, -1.0], [24.0, 0.0]]),
         ('net4_netedge14', [[24.0, 0.0], [24.0, 1.0]]),
         ('net4_netedge15', [[24.0, 1.0], [24.0, 2.0]]),
         ('net3triangle0side0', [[21.0, 0.0], [20.5, 0.5]]),
         ('net3triangle0side1', [[21.0, 1.0], [20.5, 0.5]]),
         ('net3triangle1side0', [[24.0, -1.0], [24.5, -0.5]]),
         ('net3triangle1side1', [[24.0, 0.0], [24.5, -0.5]]),
         ('net3triangle2side0', [[24.0, 0.0], [24.5, 0.5]]),
         ('net3triangle2side1', [[24.0, 1.0], [24.5, 0.5]]),
         ('net3triangle3side0', [[24.0, 1.0], [24.5, 1.5]]),
         ('net3triangle3side1', [[24.0, 2.0], [24.5, 1.5]])]
        self._geometry_05 = [('net5_netedge0', [[28.0, 0.0], [28.0, 1.0]]),
         ('net5_netedge1', [[28.0, 0.0], [29.0, 0.0]]),
         ('net5_netedge2', [[28.0, 1.0], [29.0, 1.0]]),
         ('net5_netedge3', [[29.0, 0.0], [29.0, 1.0]]),
         ('net5_netedge4', [[29.0, 0.0], [30.0, 0.0]]),
         ('net5_netedge5', [[29.0, 1.0], [29.0, 2.0]]),
         ('net5_netedge6', [[29.0, 1.0], [30.0, 1.0]]),
         ('net5_netedge7', [[29.0, 2.0], [30.0, 2.0]]),
         ('net5_netedge8', [[30.0, 0.0], [30.0, 1.0]]),
         ('net5_netedge9', [[30.0, 0.0], [31.0, 0.0]]),
         ('net5_netedge10', [[30.0, 1.0], [30.0, 2.0]]),
         ('net5_netedge11', [[30.0, 1.0], [31.0, 1.0]]),
         ('net5_netedge12', [[31.0, 0.0], [31.0, 1.0]]),
         ('net5_netedge13', [[31.0, 0.0], [32.0, 0.0]]),
         ('net5_netedge14', [[31.0, 1.0], [32.0, 1.0]]),
         ('net5_netedge15', [[32.0, 0.0], [32.0, 1.0]]),
         ('net4triangle0side0', [[28.0, 0.0], [28.5, -0.5]]),
         ('net4triangle0side1', [[29.0, 0.0], [28.5, -0.5]]),
         ('net4triangle1side0', [[29.0, 0.0], [29.5, -0.5]]),
         ('net4triangle1side1', [[30.0, 0.0], [29.5, -0.5]]),
         ('net4triangle2side0', [[30.0, 0.0], [30.5, -0.5]]),
         ('net4triangle2side1', [[31.0, 0.0], [30.5, -0.5]]),
         ('net4triangle3side0', [[29.0, 2.0], [29.5, 2.5]]),
         ('net4triangle3side1', [[30.0, 2.0], [29.5, 2.5]])]
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid193.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-2.03173138611918, 32.86513203707223], ylim=[-13.847462372377759, 21.049401050813646], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('givenfront_fill', [[15.0, 6.0], [17.0, 6.0], [17.0, 8.0], [15.0, 8.0], [15.0, 6.0]], [1, 2, 2, 2, 79]), ('giventop_fill', [[15.0, 8.0], [17.0, 8.0], [17.7, 8.7], [15.7, 8.7], [15.0, 8.0]], [1, 2, 2, 2, 79]), ('givenright_fill', [[17.0, 6.0], [17.7, 6.7], [17.7, 8.7], [17.0, 8.0], [17.0, 6.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('givenedge0', [[15.0, 6.0], [15.0, 8.0]]), ('givenedge1', [[15.0, 6.0], [17.0, 6.0]]), ('givenedge2', [[15.0, 8.0], [15.7, 8.7]]), ('givenedge3', [[15.0, 8.0], [17.0, 8.0]]), ('givenedge4', [[15.7, 8.7], [17.7, 8.7]]), ('givenedge5', [[17.0, 6.0], [17.0, 8.0]]), ('givenedge6', [[17.0, 6.0], [17.7, 6.7]]), ('givenedge7', [[17.0, 8.0], [17.7, 8.7]]), ('givenedge8', [[17.7, 6.7], [17.7, 8.7]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[15.0, 6.0], [17.0, 8.0]], id='cutdiagonal0', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[15.0, 8.0], [17.0, 6.0]], id='cutdiagonal1', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            for object_id, vertices, codes in [('net1_cell0_0_fill', [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]], [1, 2, 2, 2, 79]), ('net1_cell1_0_fill', [[1.0, 0.0], [2.0, 0.0], [2.0, 1.0], [1.0, 1.0], [1.0, 0.0]], [1, 2, 2, 2, 79]), ('net1_cell2_0_fill', [[2.0, 0.0], [3.0, 0.0], [3.0, 1.0], [2.0, 1.0], [2.0, 0.0]], [1, 2, 2, 2, 79]), ('net1_cell3_0_fill', [[3.0, 0.0], [4.0, 0.0], [4.0, 1.0], [3.0, 1.0], [3.0, 0.0]], [1, 2, 2, 2, 79]), ('net1_cell2_1_fill', [[2.0, 1.0], [3.0, 1.0], [3.0, 2.0], [2.0, 2.0], [2.0, 1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_01:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('net2_cell0_0_fill', [[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79]), ('net2_cell1_0_fill', [[8.0, 0.0], [9.0, 0.0], [9.0, 1.0], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79]), ('net2_cell2_0_fill', [[9.0, 0.0], [10.0, 0.0], [10.0, 1.0], [9.0, 1.0], [9.0, 0.0]], [1, 2, 2, 2, 79]), ('net2_cell1_1_fill', [[8.0, 1.0], [9.0, 1.0], [9.0, 2.0], [8.0, 2.0], [8.0, 1.0]], [1, 2, 2, 2, 79]), ('net2_cell1_-1_fill', [[8.0, -1.0], [9.0, -1.0], [9.0, 0.0], [8.0, 0.0], [8.0, -1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_02:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('net3_cell0_0_fill', [[14.0, 0.0], [15.0, 0.0], [15.0, 1.0], [14.0, 1.0], [14.0, 0.0]], [1, 2, 2, 2, 79]), ('net3_cell1_0_fill', [[15.0, 0.0], [16.0, 0.0], [16.0, 1.0], [15.0, 1.0], [15.0, 0.0]], [1, 2, 2, 2, 79]), ('net3_cell2_0_fill', [[16.0, 0.0], [17.0, 0.0], [17.0, 1.0], [16.0, 1.0], [16.0, 0.0]], [1, 2, 2, 2, 79]), ('net3_cell2_1_fill', [[16.0, 1.0], [17.0, 1.0], [17.0, 2.0], [16.0, 2.0], [16.0, 1.0]], [1, 2, 2, 2, 79]), ('net3_cell2_-1_fill', [[16.0, -1.0], [17.0, -1.0], [17.0, 0.0], [16.0, 0.0], [16.0, -1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_03:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('net4_cell0_0_fill', [[21.0, 0.0], [22.0, 0.0], [22.0, 1.0], [21.0, 1.0], [21.0, 0.0]], [1, 2, 2, 2, 79]), ('net4_cell1_0_fill', [[22.0, 0.0], [23.0, 0.0], [23.0, 1.0], [22.0, 1.0], [22.0, 0.0]], [1, 2, 2, 2, 79]), ('net4_cell2_0_fill', [[23.0, 0.0], [24.0, 0.0], [24.0, 1.0], [23.0, 1.0], [23.0, 0.0]], [1, 2, 2, 2, 79]), ('net4_cell2_1_fill', [[23.0, 1.0], [24.0, 1.0], [24.0, 2.0], [23.0, 2.0], [23.0, 1.0]], [1, 2, 2, 2, 79]), ('net4_cell2_-1_fill', [[23.0, -1.0], [24.0, -1.0], [24.0, 0.0], [23.0, 0.0], [23.0, -1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_04:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('net5_cell0_0_fill', [[28.0, 0.0], [29.0, 0.0], [29.0, 1.0], [28.0, 1.0], [28.0, 0.0]], [1, 2, 2, 2, 79]), ('net5_cell1_0_fill', [[29.0, 0.0], [30.0, 0.0], [30.0, 1.0], [29.0, 1.0], [29.0, 0.0]], [1, 2, 2, 2, 79]), ('net5_cell2_0_fill', [[30.0, 0.0], [31.0, 0.0], [31.0, 1.0], [30.0, 1.0], [30.0, 0.0]], [1, 2, 2, 2, 79]), ('net5_cell3_0_fill', [[31.0, 0.0], [32.0, 0.0], [32.0, 1.0], [31.0, 1.0], [31.0, 0.0]], [1, 2, 2, 2, 79]), ('net5_cell1_1_fill', [[29.0, 1.0], [30.0, 1.0], [30.0, 2.0], [29.0, 2.0], [29.0, 1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, alpha=1.0, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in self._geometry_05:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, text, anchor in [('label0', '1', [-1.0, 0.5]), ('label1', '2', [6.0, 0.5]), ('label2', '3', [13.0, 0.5]), ('label3', '4', [20.0, 0.5]), ('label4', '5', [27.0, 0.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid193().draw(sys.argv[1] if len(sys.argv) > 1 else None))
