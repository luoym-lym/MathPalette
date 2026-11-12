"""Frozen question Solid227; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid227:

    def __init__(self):
        self.id = 'Solid227'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2558'
        self.question = 'Which cylinder has twice the volume of the cylinder shown above?\n\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:None of the above'
        self.answer = 'B'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'None of the above'}
        self.query = self.question
        self.points = {'givenO': [75, 0, 75],
         'givenQ': [75, 0, 70],
         'givenL': [65, 0, 75],
         'givenR': [85, 0, 75],
         'givenl': [65, 0, 70],
         'givenrr': [85, 0, 70],
         'givenend': [82.07106781186548, -7.071067811865475, 75],
         'givenmid': [78.53553390593274, -3.5355339059327373, 75],
         'givenheight': [65, 0, 72.5],
         'givencaption': [75, 0, 108.0],
         'AO': [20, 0, 5],
         'AQ': [20, 0, 0],
         'AL': [0, 0, 5],
         'AR': [40, 0, 5],
         'Al': [0, 0, 0],
         'Arr': [40, 0, 0],
         'Aend': [34.14213562373095, -14.14213562373095, 5],
         'Amid': [27.071067811865476, -7.071067811865475, 5],
         'Aheight': [0, 0, 2.5],
         'Acaption': [20, 0, -12],
         'BO': [65, 0, 10],
         'BQ': [65, 0, 0],
         'BL': [55, 0, 10],
         'BR': [75, 0, 10],
         'Bl': [55, 0, 0],
         'Brr': [75, 0, 0],
         'Bend': [72.07106781186548, -7.071067811865475, 10],
         'Bmid': [68.53553390593274, -3.5355339059327373, 10],
         'Bheight': [55, 0, 5.0],
         'Bcaption': [65, 0, -12],
         'CO': [95, 0, 10],
         'CQ': [95, 0, 0],
         'CL': [90, 0, 10],
         'CR': [100, 0, 10],
         'Cl': [90, 0, 0],
         'Crr': [100, 0, 0],
         'Cend': [98.53553390593274, -3.5355339059327373, 10],
         'Cmid': [96.76776695296637, -1.7677669529663687, 10],
         'Cheight': [90, 0, 5.0],
         'Ccaption': [95, 0, -12],
         'DO': [130, 0, 10],
         'DQ': [130, 0, 0],
         'DL': [110, 0, 10],
         'DR': [150, 0, 10],
         'Dl': [110, 0, 0],
         'Drr': [150, 0, 0],
         'Dend': [144.14213562373095, -14.14213562373095, 10],
         'Dmid': [137.07106781186548, -7.071067811865475, 10],
         'Dheight': [110, 0, 5.0],
         'Dcaption': [130, 0, -12]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid227.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-9.924541217528386, 154.07629337591908], ylim=[-46.396680536749024, 117.60415405669846], projection=[[1, 0, 0], [0, 0.3, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['givenO']) + 10 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_0')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['givenQ']) + 10 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_1', c.project(xyz)), ('line_2', c.project([self.points['givenL'], self.points['givenl']])), ('line_3', c.project([self.points['givenR'], self.points['givenrr']])), ('line_4', c.project([self.points['givenO'], self.points['givenend']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['AO']) + 20 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_5')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['AQ']) + 20 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_6', c.project(xyz)), ('line_7', c.project([self.points['AL'], self.points['Al']])), ('line_8', c.project([self.points['AR'], self.points['Arr']])), ('line_9', c.project([self.points['AO'], self.points['Aend']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['BO']) + 10 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_10')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['BQ']) + 10 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_11', c.project(xyz)), ('line_12', c.project([self.points['BL'], self.points['Bl']])), ('line_13', c.project([self.points['BR'], self.points['Brr']])), ('line_14', c.project([self.points['BO'], self.points['Bend']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['CO']) + 5 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_15')
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['CQ']) + 5 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_16', c.project(xyz)), ('line_17', c.project([self.points['CL'], self.points['Cl']])), ('line_18', c.project([self.points['CR'], self.points['Crr']])), ('line_19', c.project([self.points['CO'], self.points['Cend']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(0, 360, 721))
            xyz = np.asarray(self.points['DO']) + 20 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_20')
            t = np.radians(np.linspace(180, 360, 721))
            xyz = np.asarray(self.points['DQ']) + 20 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_21', c.project(xyz)), ('line_22', c.project([self.points['DL'], self.points['Dl']])), ('line_23', c.project([self.points['DR'], self.points['Drr']])), ('line_24', c.project([self.points['DO'], self.points['Dend']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('10', c.project(self.points['givenO']), offset_pt=[0, 24], vertex=False, id='label_0')
            c.text('5', c.project(self.points['givenheight']), offset_pt=[-15, 0], vertex=False, id='label_1')
            c.text('20', c.project(self.points['AO']), offset_pt=[0, 24], vertex=False, id='label_2')
            c.text('5', c.project(self.points['Aheight']), offset_pt=[-15, 0], vertex=False, id='label_3')
            c.text('(A)', c.project(self.points['Acaption']), offset_pt=[0, 0], vertex=False, id='label_4')
            c.text('10', c.project(self.points['BO']), offset_pt=[0, 24], vertex=False, id='label_5')
            c.text('10', c.project(self.points['Bheight']), offset_pt=[-15, 0], vertex=False, id='label_6')
            c.text('(B)', c.project(self.points['Bcaption']), offset_pt=[0, 0], vertex=False, id='label_7')
            c.text('5', c.project(self.points['CO']), offset_pt=[0, 24], vertex=False, id='label_8')
            c.text('10', c.project(self.points['Cheight']), offset_pt=[-15, 0], vertex=False, id='label_9')
            c.text('(C)', c.project(self.points['Ccaption']), offset_pt=[0, 0], vertex=False, id='label_10')
            c.text('20', c.project(self.points['DO']), offset_pt=[0, 24], vertex=False, id='label_11')
            c.text('10', c.project(self.points['Dheight']), offset_pt=[-15, 0], vertex=False, id='label_12')
            c.text('(D)', c.project(self.points['Dcaption']), offset_pt=[0, 0], vertex=False, id='label_13')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid227().draw(sys.argv[1] if len(sys.argv) > 1 else None))
