"""Collected question Solid126; construction on the shared drawing protocol."""
from pathlib import Path
import sys
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))
from MathPalette_Dataset.drawing import Canvas, SOLID

class Solid126:
    variants = ('C01', 'C02', 'C03', 'C04')

    def _draw_base(self, c, hi=None):
        _hi = hi or {}
        _ov = {j: s for idxs, s in _hi.get(0, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('ring0e0part0', [[0.0, 0.0], [12.0, 0.0]]), ('ring0e1part0', [[12.0, 0.0], [12.0, 8.0]]), ('ring0e2part0', [[12.0, 8.0], [9.0, 8.0]]), ('ring0e3part0', [[9.0, 8.0], [9.0, 5.0]]), ('ring0e4part0', [[9.0, 5.0], [0.0, 5.0]]), ('ring0e5part0', [[0.0, 5.0], [0.0, 0.0]]), ('ring1e2part0', [[9.9, 11.9], [6.9, 11.9]]), ('ring1e3part0', [[6.9, 11.9], [6.9, 8.9]]), ('ring1e4part0', [[6.9, 8.9], [-2.0999999999999996, 8.9]]), ('ring1e5part0', [[-2.0999999999999996, 8.9], [-2.0999999999999996, 3.9000000000000004]]), ('depth0part0', [[0.0, 0.0], [-2.0999999999999996, 3.9000000000000004]]), ('depth2part0', [[12.0, 8.0], [9.9, 11.9]]), ('depth3part0', [[9.0, 8.0], [6.9, 11.9]]), ('depth4part0', [[9.0, 5.0], [6.9, 8.9]]), ('depth5part0', [[0.0, 5.0], [-2.0999999999999996, 8.9]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, **_ov[i]) if i in _ov else c.line(points, id=object_id, zorder=3, clip_on=False)
        _defs = [{}, {}, {}, {'color': '#DC2626'}, {}, {}]
        _ov = {j: s for idxs, s in _hi.get(1, ()) for j in idxs}
        for i, (object_id, points) in enumerate([('removed0', [[-2.0999999999999996, 8.9], [-2.0999999999999996, 11.9]]), ('removed1', [[-2.0999999999999996, 11.9], [6.9, 11.9]]), ('removed2', [[-2.0999999999999996, 11.9], [0.0, 8.0]]), ('removed3', [[0.0, 8.0], [9.0, 8.0]]), ('removed4', [[0.0, 5.0], [0.0, 8.0]]), ('width_range', [[0.0, -0.4884211055324671], [12.0, -0.4884211055324671]])]):
            c.line(points, id=object_id, zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]), **_ov.get(i, _defs[i]))
        c.line([[0.0, 0.0], [0.0, -0.4884211055324671]], id='width_start', zorder=3, clip_on=False)
        c.line([[12.0, 0.0], [12.0, -0.4884211055324671]], id='width_end', zorder=3, clip_on=False)
        c.text('12', (6.0, -0.4884211055324671), id='removed4', offset_pt=(0, -12))
        c.line([[12.558195549179963, 0.0], [12.558195549179963, 8.0]], id='height_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[12.0, 0.0], [12.558195549179963, 0.0]], id='height_start', zorder=3, clip_on=False)
        c.line([[12.0, 8.0], [12.558195549179963, 8.0]], id='height_end', zorder=3, clip_on=False)
        c.text('8', (12.558195549179963, 4.0), id='removed4', ha='left', offset_pt=(12, 0))
        c.line([[-0.45353388370871944, -0.24421055276623355], [-2.553533883708719, 3.655789447233767]], id='depth_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[0.0, 0.0], [-0.45353388370871944, -0.24421055276623355]], id='depth_start', zorder=3, clip_on=False)
        c.line([[-2.0999999999999996, 3.9000000000000004], [-2.553533883708719, 3.655789447233767]], id='depth_end', zorder=3, clip_on=False)
        c.text('6', (-1.503533883708719, 1.7057894472337667), id='removed4', ha='right', offset_pt=(-8, -3))
        c.line([[-2.5884211055324666, 3.9000000000000004], [-2.5884211055324666, 8.9]], id='lowheight_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[-2.0999999999999996, 3.9000000000000004], [-2.5884211055324666, 3.9000000000000004]], id='lowheight_start', zorder=3, clip_on=False)
        c.line([[-2.0999999999999996, 8.9], [-2.5884211055324666, 8.9]], id='lowheight_end', zorder=3, clip_on=False)
        c.text('5', (-2.5884211055324666, 6.4), id='removed4', ha='right', offset_pt=(-10, 0))
        c.line([[9.0, 7.476691672643785], [12.0, 7.476691672643785]], id='uprightwidth_range', zorder=3, clip_on=False, linestyle=(0.0, [4.0, 3.0]))
        c.line([[9.0, 8.0], [9.0, 7.476691672643785]], id='uprightwidth_start', zorder=3, clip_on=False)
        c.line([[12.0, 8.0], [12.0, 7.476691672643785]], id='uprightwidth_end', zorder=3, clip_on=False)
        c.text('3', (10.5, 7.476691672643785), id='removed4', offset_pt=(0, -12))

    def draw(self, output_path=None, *, variant=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / (self.__class__.__name__ + ('_' + variant if variant else '') + '.png')
        if variant is not None:
            if variant not in self.variants:
                raise ValueError('Unknown Special variant: ' + str(variant))
            return getattr(self, 'draw_' + variant)(output_path)
        with Canvas(SOLID, xlim=(-3.6498573279191975, 13.712257033774353), ylim=(-3.237633646886379, 14.12448071480717)) as c:
            self._draw_base(c, hi={1: [({3}, {})]})
            return c.save(output_path)

    def draw_C01(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid126_C01.png'
        with Canvas(SOLID, xlim=(-3.6498573279191975, 13.712257033774353), ylim=(-3.237633646886379, 14.12448071480717)) as c:
            self._draw_base(c, hi={0: [({4, 8, 14}, {'color': '#DC2626'}), ({12}, {'color': '#2563EB'})], 1: [({1}, {'color': '#DC2626'}), ({2}, {'color': '#2563EB'})]})
            return c.save(output_path)

    def draw_C02(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid126_C02.png'
        with Canvas(SOLID, xlim=(-3.6498573279191975, 13.712257033774353), ylim=(-3.237633646886379, 14.12448071480717)) as c:
            self._draw_base(c, hi={0: [({12}, {'color': '#DC2626'}), ({13, 14}, {'color': '#2563EB'})], 1: [({2}, {'color': '#DC2626'}), ({3}, {})]})
            return c.save(output_path)

    def draw_C03(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid126_C03.png'
        with Canvas(SOLID, xlim=(-3.6498573279191975, 13.712257033774353), ylim=(-3.237633646886379, 14.12448071480717)) as c:
            self._draw_base(c, hi={0: [({12}, {'color': '#DC2626'})], 1: [({1, 2}, {'color': '#DC2626'})]})
            return c.save(output_path)

    def draw_C04(self, output_path=None):
        if output_path is None:
            output_path = _PROJECT_ROOT / '.runtime/reproduced' / 'Solid126_C04.png'
        with Canvas(SOLID, xlim=(-3.6498573279191975, 13.712257033774353), ylim=(-3.237633646886379, 14.12448071480717)) as c:
            self._draw_base(c, hi={0: [({2}, {'color': '#DC2626'})]})
            return c.save(output_path)
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solid126')
    parser.add_argument('output', nargs='?')
    parser.add_argument('--variant', choices=('C01', 'C02', 'C03', 'C04'))
    args = parser.parse_args()
    print(Solid126().draw(args.output, variant=args.variant))
