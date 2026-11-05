"""Data-driven local renderer. Importing this file creates no files or figures."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def make_figure(scene):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 16,
        'svg.fonttype': 'path', 'svg.hashsalt': scene['id'],
        'lines.antialiased': True, 'path.simplify': False,
    })
    fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
    ax = fig.add_axes([.05, .05, .90, .90])
    ax.set(xlim=scene['view']['xlim'], ylim=scene['view']['ylim'], aspect='equal')
    ax.set_autoscale_on(False)
    ax.set_axis_off()
    matrix = np.asarray(scene['projection']['matrix'], dtype=float)
    origin = np.asarray(scene['projection']['origin'], dtype=float)
    offset = np.asarray(scene['projection']['offset'], dtype=float)
    pts = {k: np.asarray(v, dtype=float) for k, v in scene['points'].items()}
    project = lambda xyz: (np.asarray(xyz) - origin) @ matrix.T + offset
    artists = []
    # Visibility is frozen in the scene. No artist order infers visibility.
    objects = sorted(scene['objects'], key=lambda o: o['visibility'] != 'hidden')
    for obj in objects:
        if obj['type'] == 'segment':
            xyz = [pts[k] for k in obj['points']]
        elif obj['type'] == 'circular_arc':
            theta = np.deg2rad(np.linspace(*obj['domain_deg'], obj['samples']))
            xyz = (pts[obj['center']] + obj['radius'] * (
                np.cos(theta)[:, None] * np.asarray(obj['u']) +
                np.sin(theta)[:, None] * np.asarray(obj['v'])))
        else:
            raise ValueError(f"Unsupported object: {obj['type']}")
        xy = project(xyz)
        line, = ax.plot(xy[:, 0], xy[:, 1], color='black', linewidth=1,
                        linestyle=(0, (4, 3)) if obj['visibility'] == 'hidden' else '-',
                        solid_capstyle='round', dash_capstyle='butt',
                        clip_on=False, zorder=2 if obj['role'] != 'angle_marker' else 3)
        line.set_gid(obj['id'])
        artists.append(line)
    for label in scene['labels']:
        artist = ax.annotate(label['text'], project(pts[label['point']]),
                             xytext=label['offset_pt'], textcoords='offset points',
                             ha=label['ha'], va=label['va'], fontsize=18,
                             fontstyle='italic', color='black', clip_on=False)
        artist.set_gid(label['id'])
        artists.append(artist)
    return fig, ax, artists


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='baseline.png')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    scene = json.loads((root / 'scene.json').read_text(encoding='utf-8'))
    destination = Path(args.output)
    if not destination.is_absolute():
        destination = root / destination
    if destination.suffix.lower() not in {'.png', '.svg'}:
        parser.error('Only PNG or SVG output is supported.')
    fig, _, _ = make_figure(scene)
    metadata = {'Date': None, 'Creator': 'MathPalette local staged renderer'} if destination.suffix.lower() == '.svg' else {'Software': 'MathPalette local staged renderer'}
    fig.savefig(destination, dpi=100, facecolor='white', transparent=False,
                metadata=metadata)
    import matplotlib.pyplot as plt
    plt.close(fig)
    print(json.dumps({'output': str(destination), 'scene': str(root / 'scene.json')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
