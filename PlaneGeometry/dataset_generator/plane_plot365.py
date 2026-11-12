"""Frozen question Plane365; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane365:

    def __init__(self):
        self.id = 'Plane365'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1338'
        self.question = 'A triangle is folded along the dashed line as shown. The area of the triangle is 1.5 times the area of the resulting figure, and the total area of the grey parts is 1. Determine the area of the starting triangle.'
        self.answer = '3'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane365.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-0.216645832396126, 8.737173700342762], ylim=[-3.7308160163694444, 5.223003516369444], axes_position=[0.050000000000000114, 0.05, 0.8999999999999998, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [3.1622776601683795, 0.0], [2.2135943621178655, 1.8973665961010275], [0.0, 0.0]], [1, 2, 2, 79], id='o0', zorder=1, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[2.2099931049490764, -0.4269074841227312], [1.5121734126066786, 1.9210836785522905]], id='o1', linestyle=(0.0, [4.0, 3.0]))
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.862277660168379, 0.0], [6.913594362117866, 1.8973665961010275], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o2', zorder=3, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=4, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.8156862745098039, 0.8156862745098039, 0.8156862745098039, 0.45], linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [6.360195771588399, 1.4230249470757708], [8.528108241992495, 1.137708419923185], [6.783116797250459, 0.0]], [1, 2, 2, 79], id='o3', zorder=5, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=6, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[1.0, 1.0, 1.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[6.783116797250459, 0.0], [7.596968174702602, 0.5306189709315545], [7.20645264532393, 1.3116500296888987], [6.360195771588399, 1.4230249470757708], [6.783116797250459, 0.0]], [1, 2, 2, 2, 79], id='o4', zorder=7, facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.line([[4.7, 0.0], [6.783116797250459, 0.0]], id='o5', linestyle=(0.0, [4.0, 3.0]))
            c.line([[4.7, 0.0], [6.360195771588399, 1.4230249470757708]], id='o6', linestyle=(0.0, [4.0, 3.0]))
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane365().draw(sys.argv[1] if len(sys.argv) > 1 else None))
