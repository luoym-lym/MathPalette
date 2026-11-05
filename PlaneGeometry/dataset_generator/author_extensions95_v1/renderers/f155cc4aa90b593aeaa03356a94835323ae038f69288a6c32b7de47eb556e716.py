"""Draw only frozen vector geometry; importing this module writes nothing."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.path import Path as MPath
from matplotlib.patches import PathPatch

HERE = Path(__file__).resolve().parent


def make_figure(scene):
    matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 16,
                                'svg.fonttype': 'path', 'svg.hashsalt': 'Plane226.AuthorDesigned.v1',
                                'path.simplify': False, 'lines.scale_dashes': False})
    fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
    ax = fig.add_axes([.05, .05, .9, .9])
    ax.set(xlim=scene['view']['xlim'], ylim=scene['view']['ylim'], aspect='equal')
    ax.set_autoscale_on(False)
    ax.set_axis_off()
    artists = []
    for obj in scene['objects']:
        if obj['type'] == 'segment':
            a, b = [scene['points'][p] for p in obj['points']]
            artist, = ax.plot([a[0], b[0]], [a[1], b[1]], color='black', linewidth=1,
                              solid_capstyle='round', antialiased=True, zorder=2)
        elif obj['type'] == 'symbol_path':
            path = MPath(obj['vertices'], obj['codes'])
            fill = PathPatch(path, facecolor='black', edgecolor='none', zorder=1)
            fill.set_gid(obj['id'] + '__semantic_fill')
            ax.add_patch(fill)
            artist = PathPatch(path, facecolor='none', edgecolor='black', linewidth=1,
                               antialiased=True, joinstyle='round', zorder=2)
            ax.add_patch(artist)
        else:
            raise ValueError('Unknown frozen object: ' + obj['type'])
        artist.set_gid(obj['id'])
        artists.append(artist)
    for label in scene['labels']:
        artist = ax.text(*label['anchor'], label['text'], ha='center', va='center',
                         fontfamily='DejaVu Sans', fontsize=16, color='black', clip_on=False)
        artist.set_gid(label['id'])
        artists.append(artist)
    fig.canvas.draw()
    return fig, artists


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='baseline.png')
    args = parser.parse_args()
    output = Path(args.output)
    if not output.is_absolute():
        output = HERE / output
    if output.suffix.lower() not in ('.png', '.svg'):
        parser.error('output must be PNG or SVG')
    scene = json.loads((HERE / 'scene.json').read_text(encoding='utf-8'))
    fig, _ = make_figure(scene)
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        metadata = {'Date': None} if output.suffix.lower() == '.svg' else {'Software': 'MathPalette staged Author Designed'}
        fig.savefig(output, dpi=100, facecolor='white', transparent=False,
                    bbox_inches=None, pad_inches=0, metadata=metadata)
    finally:
        plt.close(fig)
    print(json.dumps({'output': str(output), 'objects': len(scene['objects'])}))


if __name__ == '__main__':
    main()
