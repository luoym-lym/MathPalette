"""Frozen question Solid47; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid47:

    def __init__(self):
        self.id = 'Solid47'
        self.source_dataset = 'MathVerse'
        self.source_key = 'testmini:3264'
        self.question = 'Find the volume of the following hemisphere.\n\nRound your answer to three decimal places.'
        self.answer = '452.389 units³'
        self.answer_type = 'number'
        self.query = self.question
        self.points = {'O': [0.0, 0.0, 0.0], 'R': [6.0, 0.0, 0.0], 'U': [0.0, 0.0, 6.0], 'D': [0.0, 0.0, -6.0], 'radius_value_anchor': [0.0, 0.0, 3.0]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid47.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-6.293333981467244, 6.293333981467244], ylim=[-3.9786988028289048, 8.607969160105583], projection=[[1, 0, 0], [0, 0.2279775235351884, 0.9736663950053749]], origin=[0, 0, 0], offset=[0, 0]) as c:
            t = np.radians(np.linspace(0.0, 180.0, 362))
            xyz = np.asarray(self.points['O']) + 6.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 0.2279775235351884, 0.9736663950053749]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='sphere_contour')
            t = np.radians(np.linspace(0.0, 180.0, 362))
            xyz = np.asarray(self.points['O']) + 6.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), linestyle=(0, [4, 3]), clip_on=False, id='base_rim')
            t = np.radians(np.linspace(180.0, 360.0, 362))
            xyz = np.asarray(self.points['O']) + 6.0 * (np.cos(t)[:, None] * np.array([1.0, 0.0, 0.0]) + np.sin(t)[:, None] * np.array([0.0, 1.0, 0.0]))
            c.line(c.project(xyz), clip_on=False, zorder=3, id='base_rim')
            c.line(c.project([self.points['O'], self.points['U']]), id='vertical_radius', linestyle=(0, [4, 3]), clip_on=False)
            c.line(c.project([self.points['O'], self.points['R']]), id='horizontal_radius', linestyle=(0, [4, 3]), clip_on=False)
            c.text('6', c.project(self.points['radius_value_anchor']), offset_pt=[-12, 0], vertex=False, ha='right', id='radius_value')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid47().draw(sys.argv[1] if len(sys.argv) > 1 else None))
