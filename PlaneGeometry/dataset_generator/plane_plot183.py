"""Frozen question Plane183; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane183:

    def __init__(self):
        self.id = 'Plane183'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:257'
        self.question = 'Equal regular pentagonal plates are glued together along their sides to form a complete ring, as shown. How many plates make up the ring?'
        self.answer = '10'
        self.answer_type = 'number'
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane183.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-2.3611891194201107, 3.1945834217222835], ylim=[-3.1703710110724246, 2.3854015300699696], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            for object_id, vertices, codes in [('pentagon0', [[2.6653521280029184, 1.5388417685876266], [1.7518066703603177, 1.9455784116634267], [1.0826760640014594, 1.2024335861860327], [1.5826760640014594, 0.33640818240159387], [2.560823664735265, 0.5443198732193534], [2.6653521280029184, 1.5388417685876266]], [1, 2, 2, 2, 2, 79]), ('pentagon1', [[3.0608236647352647, -0.32170553056508533], [2.5608236647352647, 0.5443198732193533], [1.5826760640014594, 0.3364081824015941], [1.4781476007338057, -0.6581137129666794], [2.3916930583764064, -1.0648503560424794], [3.0608236647352647, -0.32170553056508533]], [1, 2, 2, 2, 2, 79]), ('pentagon2', [[2.287164595108753, -2.0593722514107533], [2.391693058376407, -1.0648503560424798], [1.478147600733806, -0.6581137129666795], [0.8090169943749478, -1.4012585384440737], [1.309016994374948, -2.2672839422285125], [2.287164595108753, -2.0593722514107533]], [1, 2, 2, 2, 2, 79]), ('pentagon3', [[0.6398863880160897, -3.010428767705906], [1.3090169943749477, -2.267283942228512], [0.8090169943749477, -1.4012585384440737], [-0.16913060635885763, -1.6091702292618328], [-0.27365906962651126, -2.6036921246301064], [0.6398863880160897, -3.010428767705906]], [1, 2, 2, 2, 2, 79])]:
                c.path(vertices, codes, id=object_id, facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.circle([0.0, 0.0], 2.2270327288232137, id='ring_guide', facecolor=[0.0, 0.0, 0.0, 0], linestyle=(0, [4, 3]), fill=False)
            c.path([[1.543483468517011, 1.9755687499566976], [1.4975052285163466, 2.0114908880012927], [1.450286951725064, 2.045796974189288], [1.4019149107268425, 2.0784243278196395], [1.3535428697286207, 2.1110516814499913], [1.3040465426859835, 2.141980419251016], [1.2535163644116072, 2.1711540312799267]], [1, 4, 4, 4, 4, 4, 4], id='continuation0', facecolor=[0.0, 0.0, 0.0, 0], linestyle=(0, [4, 3]), capstyle='butt', fill=False)
            c.path([[-0.8984401784713351, -2.340516684217219], [-0.8167220729747107, -2.371885325928603], [-0.7334171779920828, -2.3989527271010727], [-0.6488678169147908, -2.4216076601223007], [-0.5643184558374987, -2.4442625931435282], [-0.4786405999367156, -2.4624739836050584], [-0.39218632377181006, -2.4761669957490997]], [1, 4, 4, 4, 4, 4, 4], id='continuation1', facecolor=[0.0, 0.0, 0.0, 0], linestyle=(0, [4, 3]), capstyle='butt', fill=False)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane183().draw(sys.argv[1] if len(sys.argv) > 1 else None))
