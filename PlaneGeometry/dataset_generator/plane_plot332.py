"""Frozen question Plane332; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane332:

    def __init__(self):
        self.id = 'Plane332'
        self.source_dataset = 'MathVision'
        self.source_key = 'test:1080'
        self.question = 'The figure on the left consists of two rectangles. Two side lengths are marked: 11 and 13. The figure is cut into three parts along the two lines drawn inside. These can be put together to make the triangle shown on the right. How long is the side marked $\\mathrm{x}$?'
        self.answer = '37'
        self.answer_type = 'number'
        self.query = self.question
        self._geometry_01 = [[12.007159430468196, 31.288115032529195],
         [12.904299664274845, 31.446305061228408],
         [13.751677815290172, 31.8136569834676],
         [14.48041319156199, 32.36030992241925],
         [15.209148567833807, 32.9069628613709],
         [15.79894571979796, 33.6176924056604],
         [16.201861900889593, 34.43472559672979],
         [16.604778081981223, 35.25175878779919],
         [16.809591982931998, 36.1523410614246],
         [16.79965492900087, 37.06326693066626],
         [16.78971787506974, 37.97419279990792],
         [16.565306615517752, 38.87009276763717],
         [16.144662832433685, 39.6781419567632],
         [15.724019049349618, 40.48619114588922],
         [15.118857769836639, 41.18388519872987],
         [14.378370641833252, 41.71451077063137],
         [13.637883513829863, 42.245136342532874],
         [12.782693275916683, 42.59391538801723],
         [11.882315639901517, 42.73249676071301],
         [10.981938003886352, 42.871078133408794],
         [10.06144869615143, 42.79560230988451],
         [9.195671383527673, 42.512204481310455],
         [8.329894070903915, 42.2288066527364],
         [7.54294085272708, 41.745379514491034],
         [6.8987806691180245, 41.101219330881975]]
        self._geometry_02 = [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane332.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=[-4.941782307929103, 89.36364913000871], ylim=[-25.796044031696518, 68.5093874062413], axes_position=[0.05, 0.05, 0.9, 0.9], coordinate_axes=False) as c:
            c.path([[0.0, 0.0], [24.0, 0.0], [24.0, 26.0], [11.0, 26.0], [11.0, 37.0], [0.0, 37.0], [0.0, 0.0]], [1, 2, 2, 2, 2, 2, 79], id='o0', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            c.line([[0.0, 0.0], [11.0, 37.0]], id='o1')
            c.line([[0.0, 0.0], [24.0, 13.0]], id='o2')
            c.point([[11.0, 37.0]], id='o3')
            c.point([[24.0, 13.0]], id='o4')
            c.path(self._geometry_01, self._geometry_02, id='o5', facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[12.007159430468196, 31.288115032529195], [13.669675924121194, 31.07354824029018], [13.496027746454264, 32.058355993302385], [12.007159430468196, 31.288115032529195]], [1, 2, 2, 79], id='o6', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[12.007159430468196, 31.288115032529195], [13.669675924121194, 31.07354824029018], [13.496027746454264, 32.058355993302385], [12.007159430468196, 31.288115032529195]], [1, 2, 2, 79], id='o6', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[24.461925436562588, 7.7201681001137485], [25.782161579116025, 7.83567379576437], [27.012224214856783, 8.442273558311935], [27.907569885093658, 9.419371899637001], [28.802915555330532, 10.396470240962067], [29.3, 11.674720769863152], [29.3, 13.0], [29.3, 14.325279230136848], [28.802915555330532, 15.603529759037933], [27.907569885093658, 16.580628100363], [27.012224214856783, 17.557726441688065], [25.782161579116025, 18.16432620423563], [24.461925436562588, 18.27983189988625]], [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], id='o7', facecolor=[0.0, 0.0, 0.0, 0], capstyle='butt', fill=False)
            c.path([[24.461925436562588, 18.27983189988625], [26.01225908213555, 17.642285362444124], [26.099414824883212, 18.638480060535873], [24.461925436562588, 18.27983189988625]], [1, 2, 2, 79], id='o8', zorder=1, edgecolor=[0.0, 0.0, 0.0, 0.0], facecolor=[0.0, 0.0, 0.0, 1.0], linewidth=0.0, capstyle='butt')
            c.path([[24.461925436562588, 18.27983189988625], [26.01225908213555, 17.642285362444124], [26.099414824883212, 18.638480060535873], [24.461925436562588, 18.27983189988625]], [1, 2, 2, 79], id='o8', facecolor=[0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 0], capstyle='butt', fill=False)
            c.path([[39.0, 0.0], [50.0, 37.0], [87.0, 26.0], [39.0, 0.0]], [1, 2, 2, 79], id='o9', facecolor=[0.0, 0.0, 0.0, 0.0], capstyle='butt')
            for object_id, points in [('o10', [[50.0, 37.0], [50.0, 26.0]]), ('o11', [[50.0, 26.0], [87.0, 26.0]]), ('o12', [[63.0, 13.0], [63.0, 26.0]])]:
                c.line(points, id=object_id)
            c.point([[50.0, 37.0]], id='o13')
            c.point([[63.0, 13.0]], id='o14')
            for object_id, text, anchor in [('t0', '11', [5.5, 39.0]), ('t1', '13', [17.5, 28.0]), ('t2', 'x', [-2.0, 18.5])]:
                c.text(text, anchor, id=object_id, rotation_mode='default', offset_pt=[0, 0], annotation_clip=None)
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane332().draw(sys.argv[1] if len(sys.argv) > 1 else None))
