"""Collected question Plane427; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, PLANE

class Plane427:
    variants = ('C01',)

    def _draw_base(self, c, kw=None, custom=None):
        _kw = kw or {}
        c.path([[3.2678342100901627, 5.032023407672544], [0.0, 0.0], [5.991777208527443, -0.314015737457663], [3.2678342100901627, 5.032023407672544]], [1, 2, 2, 79], id='o0', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        if custom and 1 in custom:
            custom[1](c)
        else:
            c.path([[3.2678342100901627, 5.032023407672544], [0.0, 0.0], [5.991777208527443, -0.314015737457663], [3.2678342100901627, 5.032023407672544]], [1, 2, 2, 79], id='o0', capstyle='butt', fill=False)
        c.path([[5.991777208527443, -0.314015737457663], [11.837997597238854, -1.663722063520853], [10.083767368902434, 4.07410647225736], [5.991777208527443, -0.314015737457663]], [1, 2, 2, 79], id='o1', alpha=1, zorder=1, edgecolor='none', linewidth=0.0, capstyle='butt')
        if custom and 3 in custom:
            custom[3](c)
        else:
            c.path([[5.991777208527443, -0.314015737457663], [11.837997597238854, -1.663722063520853], [10.083767368902434, 4.07410647225736], [5.991777208527443, -0.314015737457663]], [1, 2, 2, 79], id='o1', capstyle='butt', fill=False)
        c.line([[0.0, 0.0], [10.083767368902434, 4.07410647225736]], id='o2', linestyle=(0.0, [1.0, 1.65]), **_kw.get(4, {}))
        c.path([[6.451230562919279, 0.17868766350802368], [6.35013217093734, 0.27296343921544053], [6.222425620059838, 0.3338763393492824], [6.085536302129011, 0.3531148783531217], [5.948646984198185, 0.37235341735696104], [5.8090976977912065, 0.3490008756741668], [5.685929760524422, 0.28624367707500686]], [1, 4, 4, 4, 4, 4, 4], id='o3', zorder=3, capstyle='butt', fill=False)
        c.path([[0.5746610791164577, 0.23217814692978084], [0.5509769726548714, 0.2907983674677647], [0.5184620708684249, 0.3454510037453481], [0.47824669678869325, 0.3942361535599471], [0.4380313227089616, 0.44302130337454615], [0.3905869450364467, 0.48536702945805854], [0.33756288361699105, 0.5198012575660242]], [1, 4, 4, 4, 4, 4, 4], id='o4', zorder=3, capstyle='butt', fill=False)
        c.text('S', (0.0, 0.0), id='lS', fontsize=18.0, fontstyle='italic', offset_pt=(-10, -15))
        c.text('T', (5.991777208527443, -0.314015737457663), id='lT', fontsize=18.0, fontstyle='italic', offset_pt=(-3, -16))
        c.text('R', (3.2678342100901627, 5.032023407672544), id='lR', fontsize=18.0, fontstyle='italic', offset_pt=(0, 16))
        c.text('V', (10.083767368902434, 4.07410647225736), id='lV', fontsize=18.0, fontstyle='italic', offset_pt=(12, 14))
        c.text('U', (11.837997597238854, -1.663722063520853), id='lU', fontsize=18.0, fontstyle='italic', offset_pt=(14, 0))
        c.text('70°', (5.991777208527443, -0.314015737457663), id='a70', offset_pt=(5.8452702403227494, 41.591258887145955))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(PLANE, xlim=(-0.7152349574038777, 12.695553545906007), ylim=(-4.766068655660694, 8.64471984764919)) as c:
            self._draw_base(c)
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Plane427_C01.png'
        with Canvas(PLANE, xlim=(-0.7152349574038777, 12.695553545906007), ylim=(-4.766068655660694, 8.64471984764919)) as c:

            def _slot_1(c):
                c.path([[3.2678342100901627, 5.032023407672545], [-2.220446049250313e-16, 8.881784197001252e-16]], [1, 2], id='o0', capstyle='butt', fill=False)
                c.path([[-2.220446049250313e-16, 8.881784197001252e-16], [5.991777208527443, -0.3140157374576621]], [1, 2], id='o0', edgecolor='#DC2626', capstyle='butt', fill=False)
                c.path([[5.991777208527443, -0.3140157374576621], [3.2678342100901627, 5.032023407672545]], [1, 2], id='o0', capstyle='butt', fill=False)

            def _slot_3(c):
                c.path([[5.991777208527443, -0.3140157374576621], [11.837997597238854, -1.663722063520852], [10.083767368902434, 4.074106472257358]], [1, 2, 2], id='o1', capstyle='butt', fill=False)
                c.path([[10.083767368902434, 4.074106472257358], [10.083767368902434, 4.074106472257361], [5.991777208527443, -0.3140157374576621]], [1, 2, 2], id='o1', edgecolor='#DC2626', capstyle='butt', fill=False)
            self._draw_base(c, custom={1: _slot_1, 3: _slot_3}, kw={4: {'color': '#2563EB'}})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Plane427')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01',))
    args = parser.parse_args()
    print(Plane427().draw(args.output, variant=args.variant))
