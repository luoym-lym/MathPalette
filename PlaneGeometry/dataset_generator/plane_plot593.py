"""Frozen question Plane593; unified protocol 2.0.0. Original metadata and PNG retained."""
from pathlib import Path
import sys
import json
import numpy as np
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from dataset_tools.drawing import Canvas, ANALYTICS, PLANE, SOLID, VectorPath, VectorTransform, VectorBox

class Plane593:

    def __init__(self):
        self.id = 'Plane593'
        self.source_dataset = 'Author Designed'
        self.source_key = 'author-extensions95-v1:Plane416/extension_04'
        self.question = 'A square is folded exactly in half twice until a triangle is obtained. The indicated corner of the triangle is then cut off perpendicular to a side, as shown.\nWhich of the following will be seen when the triangle is unfolded?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E'
        self.answer = 'E'
        self.answer_type = 'choice'
        self.choices = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        self.query = self.question
        self.subject = 'PlaneGeometry'
        self.level = None
        self.scene_path = _PROJECT_ROOT / 'PlaneGeometry' / 'dataset_generator/scenes/Plane593.json'

    def draw(self, output_path=None, *, variant=None, _canvas=False):
        if output_path is None and (not _canvas):
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'PlaneGeometry' / (self.id + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if _canvas:
                raise ValueError('Canvas capture is for the original only')
            from dataset_tools.unified_replay import draw_slot
            return draw_slot('PlaneGeometry', self.id, variant, output_path)
        with Canvas(PLANE, xlim=(0.14433146853146717, 12.387268531468534), ylim=(1.0699814685314673, 13.312918531468533), axes_position=(0.05, 0.05, 0.9, 0.9), coordinate_axes=False) as c:
            c.path([[1.55, 12.420000000000002], [0.42999999999999994, 11.3], [1.55, 10.18], [2.67, 11.3], [1.55, 12.420000000000002]], [1, 2, 2, 2, 79], id='stage0.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_e30b3cfff1ad0408b4341f72df95c468694bbae024a84000', [[1.55, 12.420000000000002], [0.42999999999999994, 11.3]]), ('native_fa3d5923d6e73d42cfa93aacf848c770a0f284124b25a8df', [[0.42999999999999994, 11.3], [1.55, 10.18]]), ('native_9fbeff668d55822e9e2d3c1a59bc6d2bd051c7560b9c4ad8', [[1.55, 10.18], [2.67, 11.3]]), ('native_28204176e89279289999fb8ec2ca0c094df413a6bdd1e9ae', [[2.67, 11.3], [1.55, 12.420000000000002]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[1.55, 12.554400000000001], [1.55, 10.0456]], id='native_f24009ffb5790ab9303fef2cefd41061f45d8708cffc9fe2', zorder=3, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.path([[148.76372711686383, 532.4001551800953], [262.43003447488684, 532.4001551800953], [374.54351684853503, 532.4001551800953]], [1, 3, 3], coordinates='pixels', id='fold1.order', joinstyle='round', simplify=False)
            c.path([[368.9879612929795, 535.1779329578732], [374.54351684853503, 532.4001551800953], [368.9879612929795, 529.6223774023175]], [1, 2, 2], coordinates='pixels', id='fold1.order', joinstyle='round', simplify=False)
            c.path([[6.725, 12.420000000000002], [5.6049999999999995, 11.3], [6.725, 10.18], [6.725, 12.420000000000002]], [1, 2, 2, 79], id='stage1.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_e9cec39d712e37ba7208b9592b1ab0d3ae97630ea1b6a6c0', [[6.725, 12.420000000000002], [5.6049999999999995, 11.3]]), ('native_10b1ea4a49671837a717789ce899389d1f7ffb2ce517fdfe', [[5.6049999999999995, 11.3], [6.725, 10.18]]), ('native_35614df00315fc313ce17fd4f6f40655183a1108a8c136af', [[6.725, 10.18], [6.725, 12.420000000000002]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[5.470599999999999, 11.3], [6.8594, 11.3]], id='native_f63db172532e1d21682ac3acf4d74eb2ff5d5b85907d4e95', zorder=3, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.path([[440.9289144090946, 532.4001551800953], [554.5952217671177, 532.4001551800953], [666.7087041407657, 532.4001551800953]], [1, 3, 3], coordinates='pixels', id='fold2.order', joinstyle='round', simplify=False)
            c.path([[661.1531485852101, 535.1779329578732], [666.7087041407657, 532.4001551800953], [661.1531485852101, 529.6223774023175]], [1, 2, 2], coordinates='pixels', id='fold2.order', joinstyle='round', simplify=False)
            c.path([[11.9, 12.420000000000002], [10.780000000000001, 11.3], [11.9, 11.3], [11.9, 12.420000000000002]], [1, 2, 2, 79], id='stage2.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_9880c34e08bb89e7fee0754052ba58e362949fa9f4edb4d1', [[11.9, 12.420000000000002], [10.780000000000001, 11.3]]), ('native_e1669ea8a921da712885e614c63c40d88fc7f272f222371b', [[10.780000000000001, 11.3], [11.9, 11.3]]), ('native_d50495698914ebb67073b24004b5b5eb8f21b2d052b9321b', [[11.9, 11.3], [11.9, 12.420000000000002]]), ('cut1.right0', [[11.678592718045843, 12.028], [11.678592718045843, 11.806592718045843]]), ('cut1.right1', [[11.678592718045843, 11.806592718045843], [11.9, 11.806592718045843]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.line([[12.101600000000001, 12.028], [11.3064, 12.028]], id='native_c1f2a61200296a35c87487ba8c98b4eb6c970b216cb4a4bc', zorder=3, linestyle=(0.0, [4.0, 3.0]), simplify=False)
            c.circle([10.892, 12.1064], 0.0504, id='cut1.scissor.ring-1', zorder=3, fill=False)
            c.line([[10.9368, 12.0896], [11.228, 11.955200000000001]], id='cut1.scissor.blade-1', zorder=3, simplify=False)
            c.circle([10.892, 11.9496], 0.0504, id='cut1.scissor.ring1', zorder=3, fill=False)
            c.line([[10.9368, 11.9664], [11.228, 12.100800000000001]], id='cut1.scissor.blade1', zorder=3, simplify=False)
            c.path([[2.6, 8.24], [1.26, 6.9], [2.6, 5.5600000000000005], [3.9400000000000004, 6.9], [2.6, 8.24], [2.6, 6.4042], [2.1042, 6.9], [2.6, 7.3958], [3.0958, 6.9], [2.6, 6.4042]], [1, 2, 2, 2, 79, 1, 2, 2, 2, 79], id='optionA.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_c987d0510a9f268fb515a42f775ca41bf8e25b48d80b1fea', [[2.6, 8.24], [1.26, 6.9]]), ('native_db3bf85800c6c7b5e5dc0949a173fe30bd44f055bb399737', [[1.26, 6.9], [2.6, 5.5600000000000005]]), ('native_36fa3537c6f65faf553c37af957660b41d98a3de3daabd42', [[2.6, 5.5600000000000005], [3.9400000000000004, 6.9]]), ('native_5e520442723c40affb44149241c3bf1937befebefcf7f709', [[3.9400000000000004, 6.9], [2.6, 8.24]]), ('native_0537c97f081a5e08b1d4eaff99f27ee0f69004bfacbf214e', [[2.6, 6.4042], [2.1042, 6.9]]), ('native_87a781cce1ce93c2de2c4d6846f0a989b9e6096d82e4ca86', [[2.1042, 6.9], [2.6, 7.3958]]), ('native_aa1f1a1ea09e1b59844ca741617fc27bbe24187e7521fdd2', [[2.6, 7.3958], [3.0958, 6.9]]), ('native_f997b21ea3f5d3657d6bfef4e6afbc0d5947f47c009565ce', [[3.0958, 6.9], [2.6, 6.4042]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[6.231, 7.771000000000001], [5.829, 7.369000000000001], [5.829, 6.431], [6.231, 6.029], [7.1690000000000005, 6.029], [7.571000000000001, 6.431], [7.571000000000001, 7.369000000000001], [7.1690000000000005, 7.771000000000001], [6.231, 7.771000000000001]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='optionB.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_95596bcf7d4aae6ac68772ffc57025ae723c91ef6859b4f2', [[6.231, 7.771000000000001], [5.829, 7.369000000000001]]), ('native_ee3052b757c0ca3d1ff8fd6da4f10037f975958ec2524ef8', [[5.829, 7.369000000000001], [5.829, 6.431]]), ('native_f64526fb7db1b715d246e31a164a10f1e3222fbb6ea5feb8', [[5.829, 6.431], [6.231, 6.029]]), ('native_9e91c9d32e59bd7bf53ed6710a4b4d16c0da7a717f030237', [[6.231, 6.029], [7.1690000000000005, 6.029]]), ('native_ccedc3af55a4f51402bba254375c4f0f510a40aaf8f2be0c', [[7.1690000000000005, 6.029], [7.571000000000001, 6.431]]), ('native_b5d2071aa929589bce9e99de540bb67dc866fb98e56d3c85', [[7.571000000000001, 6.431], [7.571000000000001, 7.369000000000001]]), ('native_81b5122101b22169eefc06900449eacfa6b800484921df3e', [[7.571000000000001, 7.369000000000001], [7.1690000000000005, 7.771000000000001]]), ('native_c903fed97c25b601b6c12e7d47f6e7b719beaeb97aa94101', [[7.1690000000000005, 7.771000000000001], [6.231, 7.771000000000001]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[9.929, 6.431], [10.8, 5.5600000000000005], [11.671000000000001, 6.431], [11.671000000000001, 7.369000000000001], [10.8, 8.24], [9.929, 7.369000000000001], [9.929, 6.431]], [1, 2, 2, 2, 2, 2, 79], id='optionC.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_b7d522009e97233ee4406d35566a7a30ad5055581e8de878', [[9.929, 6.431], [10.8, 5.5600000000000005]]), ('native_f309630ef51c1c5470af496e01674dd426bdde84df6d684a', [[10.8, 5.5600000000000005], [11.671000000000001, 6.431]]), ('native_f5d6a3cb5281e9a71c493fe4f4d7b868495bedf1da20ff6e', [[11.671000000000001, 6.431], [11.671000000000001, 7.369000000000001]]), ('native_dca4e42c30408267a584e152b50c44e3170ba2728ca61e02', [[11.671000000000001, 7.369000000000001], [10.8, 8.24]]), ('native_ba09656caaad2b13f93b627eae82bc797bf915019c2af25d', [[10.8, 8.24], [9.929, 7.369000000000001]]), ('native_1655b70be69b06ea92ca0fe99d24349017581c129568c539', [[9.929, 7.369000000000001], [9.929, 6.431]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[4.2815, 3.7714999999999996], [3.3100000000000005, 2.8], [4.2815, 1.8284999999999998], [4.65, 2.1969999999999996], [5.0185, 1.8284999999999998], [5.99, 2.8], [5.0185, 3.7714999999999996], [4.65, 3.403], [4.2815, 3.7714999999999996]], [1, 2, 2, 2, 2, 2, 2, 2, 79], id='optionD.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_d8a0a93e8c8293c2d9075327c65e23ab4b4dc53f040764ce', [[4.2815, 3.7714999999999996], [3.3100000000000005, 2.8]]), ('native_659ab5433cde158ee718a4ee3ab2d313434c9f2e9293e800', [[3.3100000000000005, 2.8], [4.2815, 1.8284999999999998]]), ('native_e62c0bb8be9ddc46e6e202de5f7635ff0555cc1163e6d562', [[4.2815, 1.8284999999999998], [4.65, 2.1969999999999996]]), ('native_303402cf94c1372ad7c4dc21084e32e899ac6af65716eeea', [[4.65, 2.1969999999999996], [5.0185, 1.8284999999999998]]), ('native_c7337331a5512239a64161123966fc1aeeaa6985b29da23f', [[5.0185, 1.8284999999999998], [5.99, 2.8]]), ('native_60b391ed8d086acc2eda7a33391ac48cd67b9368e659298b', [[5.99, 2.8], [5.0185, 3.7714999999999996]]), ('native_ea6ba4b278f20543ad8ae4034c1c36e99e0531d971d3462c', [[5.0185, 3.7714999999999996], [4.65, 3.403]]), ('native_f1edf3c197477ca33cf06d27fb574c37295ee523d020bbac', [[4.65, 3.403], [4.2815, 3.7714999999999996]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            c.path([[8.281, 3.671], [7.41, 2.8], [8.281, 1.9289999999999998], [9.219, 1.9289999999999998], [10.09, 2.8], [9.219, 3.671], [8.281, 3.671]], [1, 2, 2, 2, 2, 2, 79], id='optionE.fill', zorder=1, edgecolor='none', facecolor=(0.6, 0.6, 0.6, 1.0), capstyle='butt', simplify=False)
            for object_id, points in [('native_54c79e42dac6476c3bc7408e53e388a483ad99507d8271ab', [[8.281, 3.671], [7.41, 2.8]]), ('native_b41711649d60505d2d0a3b2878f18e1bf6c6a7f57203d2dc', [[7.41, 2.8], [8.281, 1.9289999999999998]]), ('native_76c97f7da23991bf7c4d14c9036580277c37e1bb18772ceb', [[8.281, 1.9289999999999998], [9.219, 1.9289999999999998]]), ('native_692986c88415cb440036ce6f92c274f4a25ce2a02d6c904f', [[9.219, 1.9289999999999998], [10.09, 2.8]]), ('native_7eb5723e63f31fd7dba757ea6ddff5732864cb78901346d7', [[10.09, 2.8], [9.219, 3.671]]), ('native_074cd57041c5c971abd1c207f992da10e1ce25a03202a735', [[9.219, 3.671], [8.281, 3.671]])]:
                c.line(points, id=object_id, zorder=3, simplify=False)
            for object_id, text, anchor in [('optionA.label', 'A', (0.8800000000000001, 6.9)), ('optionB.label', 'B', (4.98, 6.9)), ('optionC.label', 'C', (9.08, 6.9)), ('optionD.label', 'D', (2.9300000000000006, 2.8)), ('optionE.label', 'E', (7.03, 2.8))]:
                c.text(text, anchor, id=object_id, zorder=3, rotation_mode='default')
            return c if _canvas else c.save(output_path)

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8-sig'))

    def build_scene(self):
        canvas = self.draw(_canvas=True)
        return (canvas.fig, canvas.ax)
if __name__ == '__main__':
    print(Plane593().draw(sys.argv[1] if len(sys.argv) > 1 else None))
