"""Frozen question Ana122; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Ana122:

    def __init__(self):
        self.id = 'Ana122'
        self.source_dataset = 'MathVista'
        self.source_key = 'testmini/874'
        self.question = 'For the step function shown, what is the value of y at x=-2.5?'
        self.answer = '2'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'Analytics'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'Analytics' / 'dataset_generator/scenes/Ana122.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Analytics' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('Analytics', self.id, variant, output_path)
        with Canvas(ANALYTICS, xlim=[-8.0, 8.0], ylim=[-8.0, 8.0], axes_position=[0.12, 0.12, 0.8, 0.8], coordinate_axes=True) as c:
            c.line([[-8.0, 7.0], [-7.0, 7.0]], id='curve_001', solid_capstyle='butt')
            c.point([[-8.0, 7.0]], id='point_001', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-7.0, 7.0]], id='point_002', clip_on=False)
            c.line([[-7.0, 6.0], [-6.0, 6.0]], id='curve_002', solid_capstyle='butt')
            c.point([[-7.0, 6.0]], id='point_003', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-6.0, 6.0]], id='point_004', clip_on=False)
            c.line([[-6.0, 5.0], [-5.0, 5.0]], id='curve_003', solid_capstyle='butt')
            c.point([[-6.0, 5.0]], id='point_005', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-5.0, 5.0]], id='point_006', clip_on=False)
            c.line([[-5.0, 4.0], [-4.0, 4.0]], id='curve_004', solid_capstyle='butt')
            c.point([[-5.0, 4.0]], id='point_007', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-4.0, 4.0]], id='point_008', clip_on=False)
            c.line([[-4.0, 3.0], [-3.0, 3.0]], id='curve_005', solid_capstyle='butt')
            c.point([[-4.0, 3.0]], id='point_009', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-3.0, 3.0]], id='point_010', clip_on=False)
            c.line([[-3.0, 2.0], [-2.0, 2.0]], id='curve_006', solid_capstyle='butt')
            c.point([[-3.0, 2.0]], id='point_011', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-2.0, 2.0]], id='point_012', clip_on=False)
            c.line([[-2.0, 1.0], [-1.0, 1.0]], id='curve_007', solid_capstyle='butt')
            c.point([[-2.0, 1.0]], id='point_013', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[-1.0, 1.0]], id='point_014', clip_on=False)
            c.line([[-1.0, 0.0], [0.0, 0.0]], id='curve_008', solid_capstyle='butt')
            c.point([[-1.0, 0.0]], id='point_015', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[0.0, 0.0]], id='point_016', clip_on=False)
            c.line([[0.0, -1.0], [1.0, -1.0]], id='curve_009', solid_capstyle='butt')
            c.point([[0.0, -1.0]], id='point_017', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[1.0, -1.0]], id='point_018', clip_on=False)
            c.line([[1.0, -2.0], [2.0, -2.0]], id='curve_010', solid_capstyle='butt')
            c.point([[1.0, -2.0]], id='point_019', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[2.0, -2.0]], id='point_020', clip_on=False)
            c.line([[2.0, -3.0], [3.0, -3.0]], id='curve_011', solid_capstyle='butt')
            c.point([[2.0, -3.0]], id='point_021', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[3.0, -3.0]], id='point_022', clip_on=False)
            c.line([[3.0, -4.0], [4.0, -4.0]], id='curve_012', solid_capstyle='butt')
            c.point([[3.0, -4.0]], id='point_023', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[4.0, -4.0]], id='point_024', clip_on=False)
            c.line([[4.0, -5.0], [5.0, -5.0]], id='curve_013', solid_capstyle='butt')
            c.point([[4.0, -5.0]], id='point_025', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[5.0, -5.0]], id='point_026', clip_on=False)
            c.line([[5.0, -6.0], [6.0, -6.0]], id='curve_014', solid_capstyle='butt')
            c.point([[5.0, -6.0]], id='point_027', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[6.0, -6.0]], id='point_028', clip_on=False)
            c.line([[6.0, -7.0], [7.0, -7.0]], id='curve_015', solid_capstyle='butt')
            c.point([[6.0, -7.0]], id='point_029', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[7.0, -7.0]], id='point_030', clip_on=False)
            c.line([[7.0, -8.0], [8.0, -8.0]], id='curve_016', solid_capstyle='butt')
            c.point([[7.0, -8.0]], id='point_031', clip_on=False, facecolors=[[1.0, 1.0, 1.0, 1.0]])
            c.point([[8.0, -8.0]], id='point_032', clip_on=False)
            c.point([[-8.0, 8.0]], id='point_033', clip_on=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Ana122().draw(sys.argv[1] if len(sys.argv) > 1 else None))
