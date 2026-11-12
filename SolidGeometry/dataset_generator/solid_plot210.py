"""Frozen question Solid210; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid210:

    def __init__(self):
        self.id = 'Solid210'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:2115'
        self.question = 'Which of the cones listed below can be formed from a $ 252^\\circ$ sector of a circle of radius $ 10$ by aligning the two straight sides?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.points = {'O': [36, 0, 32],
         'L': [26, 0, 32],
         'end': [39.09016994374947, 0, 22.489434837048464],
         'rad': [31, 0, 32],
         'angle': [36, 0, 36],
         'AO': [6, 0, 0],
         'AA': [6, 0, 8],
         'AR': [12, 0, 0],
         'Arad': [9.0, 0, 0],
         'Aheight': [6, 0, 2.24],
         'Acaption': [6, 0, -13],
         'AL': [0.054926409202321835, 0.8100000000000005, 0],
         'AT': [11.945073590797678, 0.81, 0],
         'Aslant': [7.486268397699419, 0.2025, 6.0],
         'BO': [19, 0, 0],
         'BA': [19, 0, 10],
         'BR': [25, 0, 0],
         'Brad': [22.0, 0, 0],
         'Bheight': [19, 0, 2.8000000000000003],
         'Bcaption': [19, 0, -13],
         'BL': [13.035094636123722, 0.6480000000000001, 0],
         'BT': [24.964905363876277, 0.6480000000000001, 0],
         'CO': [33, 0, 0],
         'CA': [33, 0, 7.14142842854285],
         'CR': [40, 0, 0],
         'Crad': [36.5, 0, 0],
         'Cheight': [33, 0, 1.9995999599919982],
         'Ccaption': [33, 0, -13],
         'CL': [26.109814311389755, 1.2350470341127031, 0],
         'CT': [39.890185688610245, 1.2350470341127044, 0],
         'Cslant': [34.72254642215256, 0.3087617585281761, 5.356071321407137],
         'DO': [48, 0, 0],
         'DA': [48, 0, 10],
         'DR': [55, 0, 0],
         'Drad': [51.5, 0, 0],
         'Dheight': [48, 0, 2.8000000000000003],
         'Dcaption': [48, 0, -13],
         'DL': [41.05578830967834, 0.8820000000000016, 0],
         'DT': [54.94421169032166, 0.882, 0],
         'EO': [64, 0, 0],
         'EA': [64, 0, 6],
         'ER': [72, 0, 0],
         'Erad': [68.0, 0, 0],
         'Eheight': [64, 0, 1.6800000000000002],
         'Ecaption': [64, 0, -13],
         'EL': [56.233816896312575, 1.9199999999999975, 0],
         'ET': [71.76618310368742, 1.92, 0],
         'Eslant': [65.94154577592185, 0.48, 4.5]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid210.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.7661267696911978, 73.76292431408643], ylim=[-23.737268556991015, 51.79178252678662], projection=[[1, 0, 0], [0, 0.18, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(-72, 180, 721))
            xyz = np.asarray(self.points['O']) + 10 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            for object_id, points in [('arc_0', c.project(xyz)), ('line_1', c.project([self.points['O'], self.points['L']])), ('line_2', c.project([self.points['O'], self.points['end']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            t = np.radians(np.linspace(-72, 180, 721))
            xyz = np.asarray(self.points['O']) + 1 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 0, 1]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='arc_3')
            t = np.radians(np.linspace(7.758619888586816, 172.24138011141318, 721))
            xyz = np.asarray(self.points['AO']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_4')
            t = np.radians(np.linspace(172.24138011141318, 367.7586198885868, 721))
            xyz = np.asarray(self.points['AO']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_5', c.project(xyz)), ('line_6', c.project([self.points['AA'], self.points['AL']])), ('line_7', c.project([self.points['AA'], self.points['AT']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['AA'], self.points['AO']]), id='line_8', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['AO'], self.points['AR']]), id='line_9', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(6.200037132516383, 173.79996286748363, 721))
            xyz = np.asarray(self.points['BO']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_10')
            t = np.radians(np.linspace(173.79996286748363, 366.2000371325164, 721))
            xyz = np.asarray(self.points['BO']) + 6 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_11', c.project(xyz)), ('line_12', c.project([self.points['BA'], self.points['BL']])), ('line_13', c.project([self.points['BA'], self.points['BT']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['BA'], self.points['BO']]), id='line_14', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['BO'], self.points['BR']]), id='line_15', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(10.162193976196088, 169.83780602380392, 721))
            xyz = np.asarray(self.points['CO']) + 7 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_16')
            t = np.radians(np.linspace(169.83780602380392, 370.1621939761961, 721))
            xyz = np.asarray(self.points['CO']) + 7 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_17', c.project(xyz)), ('line_18', c.project([self.points['CA'], self.points['CL']])), ('line_19', c.project([self.points['CA'], self.points['CT']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['CA'], self.points['CO']]), id='line_20', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['CO'], self.points['CR']]), id='line_21', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(7.2385081759144, 172.7614918240856, 721))
            xyz = np.asarray(self.points['DO']) + 7 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_22')
            t = np.radians(np.linspace(172.7614918240856, 367.2385081759144, 721))
            xyz = np.asarray(self.points['DO']) + 7 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_23', c.project(xyz)), ('line_24', c.project([self.points['DA'], self.points['DL']])), ('line_25', c.project([self.points['DA'], self.points['DT']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['DA'], self.points['DO']]), id='line_26', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['DO'], self.points['DR']]), id='line_27', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            t = np.radians(np.linspace(13.88654036262899, 166.11345963737102, 721))
            xyz = np.asarray(self.points['EO']) + 8 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='arc_28')
            t = np.radians(np.linspace(166.11345963737102, 373.886540362629, 721))
            xyz = np.asarray(self.points['EO']) + 8 * (np.cos(t)[:, None] * np.array([1, 0, 0]) + np.sin(t)[:, None] * np.array([0, 1, 0]))
            for object_id, points in [('arc_29', c.project(xyz)), ('line_30', c.project([self.points['EA'], self.points['EL']])), ('line_31', c.project([self.points['EA'], self.points['ET']]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.line(c.project([self.points['EA'], self.points['EO']]), id='line_32', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.line(c.project([self.points['EO'], self.points['ER']]), id='line_33', linestyle=(0, [4, 3]), clip_on=False, zorder=3)
            c.text('10', c.project(self.points['rad']), offset_pt=[0, -15], vertex=False, id='label_0')
            c.text('252°', c.project(self.points['angle']), offset_pt=[0, 0], vertex=False, id='label_1')
            c.text('6', c.project(self.points['Arad']), offset_pt=[0, -25], vertex=False, id='label_2')
            c.text('(A)', c.project(self.points['Acaption']), offset_pt=[0, 0], vertex=False, id='label_3')
            c.text('10', c.project(self.points['Aslant']), offset_pt=[24, 0], vertex=False, id='label_4')
            c.text('6', c.project(self.points['Brad']), offset_pt=[0, -25], vertex=False, id='label_5')
            c.text('(B)', c.project(self.points['Bcaption']), offset_pt=[0, 0], vertex=False, id='label_6')
            c.text('10', c.project(self.points['Bheight']), offset_pt=[12, 0], vertex=False, id='label_7')
            c.text('7', c.project(self.points['Crad']), offset_pt=[0, -25], vertex=False, id='label_8')
            c.text('(C)', c.project(self.points['Ccaption']), offset_pt=[0, 0], vertex=False, id='label_9')
            c.text('10', c.project(self.points['Cslant']), offset_pt=[24, 0], vertex=False, id='label_10')
            c.text('7', c.project(self.points['Drad']), offset_pt=[0, -25], vertex=False, id='label_11')
            c.text('(D)', c.project(self.points['Dcaption']), offset_pt=[0, 0], vertex=False, id='label_12')
            c.text('10', c.project(self.points['Dheight']), offset_pt=[12, 0], vertex=False, id='label_13')
            c.text('8', c.project(self.points['Erad']), offset_pt=[0, -25], vertex=False, id='label_14')
            c.text('(E)', c.project(self.points['Ecaption']), offset_pt=[0, 0], vertex=False, id='label_15')
            c.text('10', c.project(self.points['Eslant']), offset_pt=[24, 0], vertex=False, id='label_16')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid210().draw(sys.argv[1] if len(sys.argv) > 1 else None))
