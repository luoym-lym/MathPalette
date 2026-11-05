"""Deterministic, scene-driven drawing; importing this module creates no image."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def draw_scene(scene):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib import rc_context
    style = {
        'font.family': 'DejaVu Sans', 'font.size': 16,
        'svg.fonttype': 'path', 'svg.hashsalt': 'Solid188-author-extensions-v1',
        'path.simplify': False, 'text.antialiased': True,
    }
    with rc_context(style):
        fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
        ax = fig.add_axes(scene['view']['layout']['axes_position'])
        ax.set_xlim(scene['view']['xlim'])
        ax.set_ylim(scene['view']['ylim'])
        ax.set_aspect('equal', adjustable='box')
        ax.set_autoscale_on(False)
        ax.set_axis_off()
        projection = scene['projection']
        matrix = projection['matrix']
        origin = projection['origin']
        offset = projection['offset']

        def project(point, panel_name):
            panel = scene['panels'][panel_name]
            delta = [point[i] - origin[i] for i in range(3)]
            xy = [sum(row[i] * delta[i] for i in range(3)) + offset[j]
                  for j, row in enumerate(matrix)]
            return [xy[j] * panel['scale'] + panel['offset'][j] for j in range(2)]

        artists = []
        for obj in scene['objects']:
            if obj['visibility'] == 'omitted':
                continue
            if obj['type'] != 'segment':
                raise ValueError('Unsupported object: ' + obj['type'])
            ends = [project(scene['points'][ref], obj['panel']) for ref in obj['points']]
            line = Line2D([p[0] for p in ends], [p[1] for p in ends],
                          color='black', linewidth=1, linestyle='solid',
                          solid_capstyle='round', antialiased=True, clip_on=False)
            line.set_gid(obj['id'])
            ax.add_line(line)
            artists.append(line)
        for label in scene['labels']:
            artist = ax.text(*label['page_position'], label['text'],
                             fontfamily='DejaVu Sans', fontsize=16, color='black',
                             ha='center', va='center', clip_on=False)
            artist.set_gid(label['id'])
            artists.append(artist)
        fig.canvas.draw()
        return fig, ax, artists


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='baseline.png')
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    output = Path(args.output)
    if not output.is_absolute():
        output = base / output
    scene = json.loads((base / 'scene.json').read_text(encoding='utf-8'))
    fig, _, _ = draw_scene(scene)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() == '.svg':
        fig.savefig(output, format='svg', facecolor='white', transparent=False,
                    metadata={'Date': None})
    else:
        fig.savefig(output, format='png', dpi=100, facecolor='white', transparent=False,
                    metadata={'Software': 'MathPalette staged Solid188 renderer v1'})
        fig.savefig(output.with_suffix('.svg'), format='svg', facecolor='white',
                    transparent=False, metadata={'Date': None})
    import matplotlib.pyplot as plt
    plt.close(fig)


if __name__ == '__main__':
    main()
