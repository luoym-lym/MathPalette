"""Frozen question Solid303; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Solid303:

    def __init__(self):
        self.id = 'Solid303'
        self.source_dataset = 'We-Math2.0-Standard'
        self.source_key = 'standard/3829'
        self.question = 'In the spatial coordinate diagram, all axis ticks are one unit apart and dashed guides are parallel to the coordinate axes. Find the equation of the plane through A, B and C.'
        self.answer = 'x/2 + y/4 + z/3 = 1'
        self.answer_type = 'expression'
        self.query = self.question
        self.points = {'O': [0, 0, 0], 'A': [2, 0, 0], 'B': [0, 4, 0], 'C': [0, 0, 3]}
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'SolidGeometry' / 'dataset_generator/scenes/Solid303.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'SolidGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('SolidGeometry', self.id, variant, output_path)
        with Canvas(SOLID, xlim=[-5.45576447969006, 5.455764479690062], ylim=[-4.94247842131956, 5.9690505380605625], projection=[[-0.8, 0.8, 0], [-0.45, -0.45, 1]], origin=[0, 0, 0], offset=[0, 0]) as c:
            for object_id, points in [('s0', c.project([[-4.7, -0.0, -0.0], [5.2, 0.0, 0.0]])), ('s1', c.project([[-3.998228037112093, -0.03806176283223858, 0.0403219999381464], [-4.001771962887907, 0.03806176283223858, -0.0403219999381464]])), ('s2', c.project([[-2.998228037112093, -0.03806176283223858, 0.0403219999381464], [-3.001771962887907, 0.03806176283223858, -0.0403219999381464]])), ('s3', c.project([[-1.9982280371120933, -0.03806176283223858, 0.0403219999381464], [-2.001771962887907, 0.03806176283223858, -0.0403219999381464]])), ('s4', c.project([[-0.9982280371120932, -0.03806176283223858, 0.0403219999381464], [-1.0017719628879067, 0.03806176283223858, -0.0403219999381464]])), ('s5', c.project([[1.0017719628879067, -0.03806176283223858, 0.0403219999381464], [0.9982280371120932, 0.03806176283223858, -0.0403219999381464]])), ('s6', c.project([[2.001771962887907, -0.03806176283223858, 0.0403219999381464], [1.9982280371120933, 0.03806176283223858, -0.0403219999381464]])), ('s7', c.project([[3.001771962887907, -0.03806176283223858, 0.0403219999381464], [2.998228037112093, 0.03806176283223858, -0.0403219999381464]])), ('s8', c.project([[4.001771962887907, -0.03806176283223858, 0.0403219999381464], [3.998228037112093, 0.03806176283223858, -0.0403219999381464]])), ('s9', c.project([[5.2, 0.0, 0.0], [5.068846879528111, 0.02681994563193535, 0.11592574982217088]])), ('s10', c.project([[5.2, 0.0, 0.0], [5.06448512472711, 0.12051043875744569, 0.016671596128272063]])), ('s11', c.project([[-0.0, -4.7, -0.0], [0.0, 5.2, 0.0]])), ('s12', c.project([[0.03806176283223858, -4.001771962887907, -0.0403219999381464], [-0.03806176283223858, -3.998228037112093, 0.0403219999381464]])), ('s13', c.project([[0.03806176283223858, -3.001771962887907, -0.0403219999381464], [-0.03806176283223858, -2.998228037112093, 0.0403219999381464]])), ('s14', c.project([[0.03806176283223858, -2.001771962887907, -0.0403219999381464], [-0.03806176283223858, -1.9982280371120933, 0.0403219999381464]])), ('s15', c.project([[0.03806176283223858, -1.0017719628879067, -0.0403219999381464], [-0.03806176283223858, -0.9982280371120932, 0.0403219999381464]])), ('s16', c.project([[0.03806176283223858, 0.9982280371120932, -0.0403219999381464], [-0.03806176283223858, 1.0017719628879067, 0.0403219999381464]])), ('s17', c.project([[0.03806176283223858, 1.9982280371120933, -0.0403219999381464], [-0.03806176283223858, 2.001771962887907, 0.0403219999381464]])), ('s18', c.project([[0.03806176283223858, 2.998228037112093, -0.0403219999381464], [-0.03806176283223858, 3.001771962887907, 0.0403219999381464]])), ('s19', c.project([[0.03806176283223858, 3.998228037112093, -0.0403219999381464], [-0.03806176283223858, 4.001771962887907, 0.0403219999381464]])), ('s20', c.project([[0.0, 5.2, 0.0], [0.12051043875744569, 5.06448512472711, 0.016671596128272057]])), ('s21', c.project([[0.0, 5.2, 0.0], [0.02681994563193535, 5.068846879528111, 0.11592574982217088]])), ('s22', c.project([[-0.0, -0.0, -4.7], [0.0, 0.0, 5.2]])), ('s23', c.project([[-0.04062499999999999, 0.04062499999999999, -4.0], [0.04062499999999999, -0.04062499999999999, -4.0]])), ('s24', c.project([[-0.04062499999999999, 0.04062499999999999, -3.0], [0.04062499999999999, -0.04062499999999999, -3.0]])), ('s25', c.project([[-0.04062499999999999, 0.04062499999999999, -2.0], [0.04062499999999999, -0.04062499999999999, -2.0]])), ('s26', c.project([[-0.04062499999999999, 0.04062499999999999, -1.0], [0.04062499999999999, -0.04062499999999999, -1.0]])), ('s27', c.project([[-0.04062499999999999, 0.04062499999999999, 1.0], [0.04062499999999999, -0.04062499999999999, 1.0]])), ('s28', c.project([[-0.04062499999999999, 0.04062499999999999, 2.0], [0.04062499999999999, -0.04062499999999999, 2.0]])), ('s29', c.project([[-0.04062499999999999, 0.04062499999999999, 3.0], [0.04062499999999999, -0.04062499999999999, 3.0]])), ('s30', c.project([[-0.04062499999999999, 0.04062499999999999, 4.0], [0.04062499999999999, -0.04062499999999999, 4.0]])), ('s31', c.project([[0.0, 0.0, 5.2], [0.0108540925266904, 0.11085409252669037, 5.064768683274021]])), ('s32', c.project([[0.0, 0.0, 5.2], [0.11085409252669037, 0.0108540925266904, 5.064768683274021]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            for object_id, points in [('p_A', c.project([self.points['A']])), ('p_B', c.project([self.points['B']])), ('p_C', c.project([self.points['C']]))]:
                c.point(points, id=object_id, filled=True)
            for object_id, points in [('s36', c.project([[2, 0, 0], [0, 4, 0]])), ('s37', c.project([[0, 4, 0], [0, 0, 3]])), ('s38', c.project([[0, 0, 3], [2, 0, 0]]))]:
                c.line(points, id=object_id, clip_on=False, zorder=3)
            c.text('-4', c.project([-4.0, -0.0, -0.0]), offset_pt=[-3.6234666314352886, 13.522961568046956], vertex=False, id='l0')
            c.text('-2', c.project([-2.0, -0.0, -0.0]), offset_pt=[5.176380902050419, 19.318516525781362], vertex=False, id='l1')
            c.text('2', c.project([2.0, 0.0, 0.0]), offset_pt=[-6.9999999999999964, 12.124355652982143], vertex=False, id='l2')
            c.text('4', c.project([4.0, 0.0, 0.0]), offset_pt=[8.572527594031472e-16, 14.0], vertex=False, id='l3')
            c.text('x', c.project([5.2, 0.0, 0.0]), offset_pt=[-13.073633056868239, -7.353918594488384], vertex=True, id='l4')
            c.text('-4', c.project([-0.0, -4.0, -0.0]), offset_pt=[7.000000000000002, 12.12435565298214], vertex=False, id='l5')
            c.text('-2', c.project([-0.0, -2.0, -0.0]), offset_pt=[7.000000000000002, 12.12435565298214], vertex=False, id='l6')
            c.text('2', c.project([0.0, 2.0, 0.0]), offset_pt=[12.124355652982143, 6.999999999999999], vertex=False, id='l7')
            c.text('4', c.project([0.0, 4.0, 0.0]), offset_pt=[12.124355652982143, 6.999999999999999], vertex=False, id='l8')
            c.text('y', c.project([0.0, 5.2, 0.0]), offset_pt=[13.073633056868239, -7.353918594488384], vertex=True, id='l9')
            c.text('-4', c.project([-0.0, -0.0, -4.0]), offset_pt=[14.0, 0.0], vertex=False, id='l10')
            c.text('-2', c.project([-0.0, -0.0, -2.0]), offset_pt=[14.0, 0.0], vertex=False, id='l11')
            c.text('2', c.project([0.0, 0.0, 2.0]), offset_pt=[-7.000000000000006, -12.124355652982137], vertex=False, id='l12')
            c.text('4', c.project([0.0, 0.0, 4.0]), offset_pt=[-12.0, 0.0], vertex=False, id='l13')
            c.text('z', c.project([0.0, 0.0, 5.2]), offset_pt=[0.0, 15.0], vertex=True, id='l14')
            c.text('O', c.project(self.points['O']), offset_pt=[13.500000000000004, 23.38268590217984], vertex=True, id='l15')
            c.text('A', c.project(self.points['A']), offset_pt=[3.623466631435284, -13.522961568046957], vertex=True, id='l16')
            c.text('B', c.project(self.points['B']), offset_pt=[-3.623466631435301, -13.522961568046954], vertex=True, id='l17')
            c.text('C', c.project(self.points['C']), offset_pt=[12, 12], vertex=True, id='l18')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Solid303().draw(sys.argv[1] if len(sys.argv) > 1 else None))
