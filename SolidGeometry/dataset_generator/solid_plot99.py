"""Frozen question Solid99; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid99:

    def __init__(self):
        self.id = 'Solid99'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:308'
        self.question = 'The diagram shows an object made up of 12 dice glued-together. The object is dipped into some colour so that the entire outside is coloured in this new colour. How many of the small dice will have exactly four faces coloured in?'
        self.answer = '10'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid99.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-0.16188353051526327, 6.6717248580346435], ylim=[-1.2967248580346435, 5.536883530515263], projection=[[1, 0.5, 0], [0, 0.25, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('chaine0', c.project([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])), ('chaine1', c.project([[1.0, 0.0, 1.0], [2.0, 0.0, 1.0]])), ('chaine2', c.project([[2.0, 0.0, 1.0], [2.0, 1.0, 1.0]])), ('chaine3', c.project([[1.0, 0.0, 0.0], [1.0, 0.0, 1.0]])), ('chaine4', c.project([[2.0, 0.0, 0.0], [2.0, 0.0, 1.0]])), ('chaine5', c.project([[1.0, 0.0, 2.0], [2.0, 0.0, 2.0]])), ('chaine6', c.project([[2.0, 0.0, 2.0], [2.0, 1.0, 2.0]])), ('chaine7', c.project([[1.0, 0.0, 1.0], [1.0, 0.0, 2.0]])), ('chaine8', c.project([[2.0, 0.0, 1.0], [2.0, 0.0, 2.0]])), ('chaine9', c.project([[2.0, 1.0, 1.0], [2.0, 1.0, 2.0]])), ('chaine10', c.project([[1.0, 0.0, 3.0], [2.0, 0.0, 3.0]])), ('chaine11', c.project([[2.0, 0.0, 3.0], [2.0, 1.0, 3.0]])), ('chaine12', c.project([[1.0, 0.0, 2.0], [1.0, 0.0, 3.0]])), ('chaine13', c.project([[2.0, 0.0, 2.0], [2.0, 0.0, 3.0]])), ('chaine14', c.project([[2.0, 1.0, 2.0], [2.0, 1.0, 3.0]])), ('chaine15', c.project([[1.0, 0.0, 4.0], [2.0, 0.0, 4.0]])), ('chaine16', c.project([[1.0, 1.0, 4.0], [2.0, 1.0, 4.0]])), ('chaine17', c.project([[1.0, 0.0, 4.0], [1.0, 1.0, 4.0]])), ('chaine18', c.project([[2.0, 0.0, 4.0], [2.0, 1.0, 4.0]])), ('chaine19', c.project([[1.0, 0.0, 3.0], [1.0, 0.0, 4.0]])), ('chaine20', c.project([[2.0, 0.0, 3.0], [2.0, 0.0, 4.0]])), ('chaine21', c.project([[2.0, 1.0, 3.0], [2.0, 1.0, 4.0]])), ('chaine22', c.project([[0.0, 0.0, 2.0], [1.0, 0.0, 2.0]])), ('chaine23', c.project([[0.0, 0.0, 3.0], [1.0, 0.0, 3.0]])), ('chaine24', c.project([[0.0, 0.0, 2.0], [0.0, 0.0, 3.0]])), ('chaine25', c.project([[0.0, 0.0, 4.0], [1.0, 0.0, 4.0]])), ('chaine26', c.project([[0.0, 1.0, 4.0], [1.0, 1.0, 4.0]])), ('chaine27', c.project([[0.0, 0.0, 4.0], [0.0, 1.0, 4.0]])), ('chaine28', c.project([[0.0, 0.0, 3.0], [0.0, 0.0, 4.0]])), ('chaine29', c.project([[2.0, 0.0, 0.0], [3.0, 0.0, 0.0]])), ('chaine30', c.project([[2.0, 0.0, 1.0], [3.0, 0.0, 1.0]])), ('chaine31', c.project([[2.0, 1.0, 1.0], [3.0, 1.0, 1.0]])), ('chaine32', c.project([[3.0, 0.0, 1.0], [3.0, 1.0, 1.0]])), ('chaine33', c.project([[3.0, 0.0, 0.0], [3.0, 0.0, 1.0]])), ('chaine34', c.project([[3.0, 0.0, 0.0], [4.0, 0.0, 0.0]])), ('chaine35', c.project([[3.0, 0.0, 1.0], [4.0, 0.0, 1.0]])), ('chaine36', c.project([[3.0, 1.0, 1.0], [4.0, 1.0, 1.0]])), ('chaine37', c.project([[4.0, 0.0, 1.0], [4.0, 1.0, 1.0]])), ('chaine38', c.project([[4.0, 0.0, 0.0], [4.0, 0.0, 1.0]])), ('chaine39', c.project([[4.0, 0.0, 0.0], [5.0, 0.0, 0.0]])), ('chaine40', c.project([[4.0, 0.0, 1.0], [5.0, 0.0, 1.0]])), ('chaine41', c.project([[4.0, 1.0, 1.0], [5.0, 1.0, 1.0]])), ('chaine42', c.project([[5.0, 0.0, 0.0], [5.0, 1.0, 0.0]])), ('chaine43', c.project([[5.0, 0.0, 1.0], [5.0, 1.0, 1.0]])), ('chaine44', c.project([[5.0, 0.0, 0.0], [5.0, 0.0, 1.0]])), ('chaine45', c.project([[5.0, 1.0, 0.0], [5.0, 1.0, 1.0]])), ('chaine46', c.project([[4.0, 2.0, 1.0], [5.0, 2.0, 1.0]])), ('chaine47', c.project([[4.0, 1.0, 1.0], [4.0, 2.0, 1.0]])), ('chaine48', c.project([[5.0, 1.0, 0.0], [5.0, 2.0, 0.0]])), ('chaine49', c.project([[5.0, 1.0, 1.0], [5.0, 2.0, 1.0]])), ('chaine50', c.project([[5.0, 2.0, 0.0], [5.0, 2.0, 1.0]])), ('chaine51', c.project([[5.0, 2.0, 0.0], [5.0, 3.0, 0.0]])), ('chaine52', c.project([[5.0, 2.0, 1.0], [5.0, 3.0, 1.0]])), ('chaine53', c.project([[5.0, 3.0, 0.0], [5.0, 3.0, 1.0]])), ('chaine54', c.project([[4.0, 2.0, 2.0], [5.0, 2.0, 2.0]])), ('chaine55', c.project([[4.0, 3.0, 2.0], [5.0, 3.0, 2.0]])), ('chaine56', c.project([[4.0, 2.0, 2.0], [4.0, 3.0, 2.0]])), ('chaine57', c.project([[5.0, 2.0, 2.0], [5.0, 3.0, 2.0]])), ('chaine58', c.project([[4.0, 2.0, 1.0], [4.0, 2.0, 2.0]])), ('chaine59', c.project([[5.0, 2.0, 1.0], [5.0, 2.0, 2.0]])), ('chaine60', c.project([[5.0, 3.0, 1.0], [5.0, 3.0, 2.0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid99().draw(sys.argv[1] if len(sys.argv) > 1 else None))
