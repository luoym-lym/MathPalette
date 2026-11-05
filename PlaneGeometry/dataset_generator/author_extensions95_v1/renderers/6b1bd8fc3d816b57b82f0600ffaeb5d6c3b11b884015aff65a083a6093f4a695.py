"""Draw this original solely from scene.json; importing this module writes nothing.

python -X utf8 -B render.py --output baseline.png
python -X utf8 -B render.py --output baseline.svg
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import platform

HERE = Path(__file__).resolve().parent


def render(output, svg_output=None):
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.lines import Line2D
    from matplotlib.patches import Polygon
    import numpy
    import PIL
    from matplotlib import ft2font

    scene = json.loads((HERE / 'scene.json').read_text(encoding='utf-8'))
    allowed = {'cell_fill', 'grid_edge'}
    assert all(obj['role'] in allowed for obj in scene['objects'])
    assert all(c['type'] == 'square_grid_board' for c in scene['constraints'])
    assert len(scene['labels']) == 5
    style = {'font.family': 'DejaVu Sans', 'font.size': 16,
             'svg.fonttype': 'path', 'svg.hashsalt': 'MathPalette-Plane300-originals-20261105',
             'path.simplify': False, 'text.antialiased': True,
             'lines.antialiased': True, 'patch.antialiased': True,
             'savefig.transparent': False}
    with matplotlib.rc_context(style):
        fig = Figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
        FigureCanvasAgg(fig)
        ax = fig.add_axes(scene['view']['layout']['axes_position'])
        ax.set_xlim(scene['view']['xlim'])
        ax.set_ylim(scene['view']['ylim'])
        ax.set_aspect('equal', adjustable='box')
        ax.set_autoscale_on(False)
        ax.set_axis_off()
        for obj in scene['objects']:
            coordinates = [scene['points'][key] for key in obj['points']]
            if obj['role'] == 'cell_fill':
                artist = Polygon(coordinates, closed=True, facecolor=obj['fill_color'],
                                 edgecolor='none', linewidth=0, zorder=1)
                ax.add_patch(artist)
            else:
                artist = Line2D([p[0] for p in coordinates], [p[1] for p in coordinates],
                                color='#000000', linewidth=1.0, solid_capstyle='butt',
                                antialiased=True, zorder=2)
                ax.add_line(artist)
            artist.set_gid(obj['id'])
        for label in scene['labels']:
            artist = ax.text(*label['anchor'], label['text'], ha='center', va='center',
                             fontsize=16, color='#000000', family='DejaVu Sans',
                             clip_on=False, zorder=3)
            artist.set_gid(label['id'])
        for destination in [output, svg_output]:
            if destination is None:
                continue
            path = Path(destination)
            if not path.is_absolute():
                path = HERE / path
            path.parent.mkdir(parents=True, exist_ok=True)
            suffix = path.suffix.lower()
            if suffix not in ('.png', '.svg'):
                raise ValueError('Only PNG and SVG outputs are supported')
            metadata = ({'Date': None, 'Creator': 'MathPalette frozen original renderer'}
                        if suffix == '.svg' else {'Software': 'MathPalette frozen original renderer'})
            fig.savefig(path, format=suffix[1:], dpi=100, facecolor='white',
                        transparent=False, bbox_inches=None, metadata=metadata)
        fig.clear()
    return {'pid': os.getpid(), 'scene_sha256': hashlib.sha256((HERE / 'scene.json').read_bytes()).hexdigest(),
            'objects_drawn': len(scene['objects']), 'labels_drawn': len(scene['labels']),
            'dependencies': {'python': platform.python_version(), 'matplotlib': matplotlib.__version__,
                             'numpy': numpy.__version__, 'Pillow': PIL.__version__,
                             'FreeType': ft2font.__freetype_version__}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='baseline.png')
    parser.add_argument('--svg-output')
    args = parser.parse_args()
    print(json.dumps(render(args.output, args.svg_output), sort_keys=True))


if __name__ == '__main__':
    main()
