"""Frozen question Solid140; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid140:

    def __init__(self):
        self.id = 'Solid140'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:969'
        self.question = 'In a box-shaped water tank with dimensions $4 \\mathrm{~m} \\times 2 \\mathrm{~m} \\times 1 \\mathrm{~m}$, the height of the water is $25 \\mathrm{~cm}$. The tank is then turned on its side (see picture on the right). How high is the water in the tank now?\nChoices:\nA:$25 \\mathrm{~cm}$\nB:$50 \\mathrm{~cm}$\nC:$75 \\mathrm{~cm}$\nD:$1 \\mathrm{~m}$\nE:$1.25 \\mathrm{~m}$'
        self.answer = 'D'
        self.answer_type = 'choice'
        self.choices = {'A': '$25 \\mathrm{~cm}$', 'B': '$50 \\mathrm{~cm}$', 'C': '$75 \\mathrm{~cm}$', 'D': '$1 \\mathrm{~m}$', 'E': '$1.25 \\mathrm{~m}$'}
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid140.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-1.8740645773287294, 9.882260487638343], ylim=[-3.770092651606711, 7.986232413360361], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, points in [('leftedge0', [[0.0, 1.2], [4.0, 1.2]]), ('leftedge1', [[0.0, 1.2], [0.0, 2.2]]), ('leftedge2', [[4.0, 1.2], [4.0, 2.2]]), ('leftedge3', [[0.0, 2.2], [4.0, 2.2]]), ('leftedge4', [[0.0, 2.2], [0.7, 2.9000000000000004]]), ('leftedge5', [[0.7, 2.9000000000000004], [4.7, 2.9000000000000004]]), ('leftedge6', [[4.7, 2.9000000000000004], [4.0, 2.2]]), ('leftedge7', [[4.0, 1.2], [4.7, 1.9]]), ('leftedge8', [[4.7, 1.9], [4.7, 2.9000000000000004]]), ('leftedge9', [[0.7, 2.9000000000000004], [0.7, 2.15]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('leftwaterfront', [[0.0, 1.2], [4.0, 1.2], [4.0, 1.45], [0.0, 1.45], [0.0, 1.2]], [1, 2, 2, 2, 79]), ('leftwaterright', [[4.0, 1.2], [4.7, 1.9], [4.7, 2.15], [4.0, 1.45], [4.0, 1.2]], [1, 2, 2, 2, 79]), ('leftwatertop', [[0.0, 1.45], [4.0, 1.45], [4.7, 2.15], [0.7, 2.15], [0.0, 1.45]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('leftlevel0', [[0.0, 1.45], [4.0, 1.45]]), ('leftlevel1', [[4.0, 1.45], [4.7, 2.15]]), ('leftlevel2', [[4.7, 2.15], [0.7, 2.15]]), ('leftlevel3', [[0.7, 2.15], [0.0, 1.45]]), ('rightedge0', [[7.0, 0.0], [8.0, 0.0]]), ('rightedge1', [[7.0, 0.0], [7.0, 4.0]]), ('rightedge2', [[8.0, 0.0], [8.0, 4.0]]), ('rightedge3', [[7.0, 4.0], [8.0, 4.0]]), ('rightedge4', [[7.0, 4.0], [7.7, 4.7]]), ('rightedge5', [[7.7, 4.7], [8.7, 4.7]]), ('rightedge6', [[8.7, 4.7], [8.0, 4.0]]), ('rightedge7', [[8.0, 0.0], [8.7, 0.7]]), ('rightedge8', [[8.7, 0.7], [8.7, 4.7]]), ('rightedge9', [[7.7, 4.7], [7.7, 1.7]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            for object_id, vertices, codes in [('rightwaterfront', [[7.0, 0.0], [8.0, 0.0], [8.0, 1.0], [7.0, 1.0], [7.0, 0.0]], [1, 2, 2, 2, 79]), ('rightwaterright', [[8.0, 0.0], [8.7, 0.7], [8.7, 1.7], [8.0, 1.0], [8.0, 0.0]], [1, 2, 2, 2, 79]), ('rightwatertop', [[7.0, 1.0], [8.0, 1.0], [8.7, 1.7], [7.7, 1.7], [7.0, 1.0]], [1, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 1.0], linewidth=0.0, capstyle='butt')
            for object_id, points in [('rightlevel0', [[7.0, 1.0], [8.0, 1.0]]), ('rightlevel1', [[8.0, 1.0], [8.7, 1.7]]), ('rightlevel2', [[8.7, 1.7], [7.7, 1.7]]), ('rightlevel3', [[7.7, 1.7], [7.0, 1.0]])]:
                c.line(points, id=object_id, zorder=3, clip_on=False)
            c.line([[-0.28347620237671367, 1.2], [-0.28347620237671367, 1.45]], id='waterdepth_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
            c.line([[0.0, 1.2], [-0.28347620237671367, 1.2]], id='waterdepth_start', zorder=3, clip_on=False)
            c.line([[0.0, 1.45], [-0.28347620237671367, 1.45]], id='waterdepth_end', zorder=3, clip_on=False)
            c.text('25 cm', [-0.28347620237671367, 1.325], id='rightlevel3', ha='right', rotation_mode='default', offset_pt=[-7, -22], annotation_clip=None)
            c.text('4 m', [2.0, 1.2], id='leftwidth', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('2 m', [4.35, 1.5499999999999998], id='leftdepth', rotation_mode='default', offset_pt=[20, -8], annotation_clip=None)
            c.text('1 m', [0.0, 1.85], id='leftheight', rotation_mode='default', offset_pt=[-23, 4], annotation_clip=None)
            c.text('1 m', [7.5, 0.0], id='rightwidth', rotation_mode='default', offset_pt=[0, -17], annotation_clip=None)
            c.text('2 m', [8.35, 0.35], id='rightdepth', rotation_mode='default', offset_pt=[22, -6], annotation_clip=None)
            c.text('4 m', [8.7, 2.7], id='rightheight', rotation_mode='default', offset_pt=[25, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid140().draw(sys.argv[1] if len(sys.argv) > 1 else None))
