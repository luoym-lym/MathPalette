"""Render only frozen cubic outlines. Importing this module writes no files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def draw(output: Path, svg: Path | None = None) -> None:
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt
    from matplotlib.path import Path as MplPath
    from matplotlib.patches import PathPatch

    scene = json.loads((HERE / 'scene.json').read_text(encoding='utf-8'))
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 16,
                         'svg.fonttype': 'path', 'svg.hashsalt': scene['id'],
                         'path.simplify': False})
    fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
    ax = fig.add_axes(scene['view']['layout']['axes_position'])
    ax.set_xlim(scene['view']['xlim'])
    ax.set_ylim(scene['view']['ylim'])
    ax.set_aspect('equal', adjustable='box')
    ax.set_axis_off()
    ax.set_autoscale_on(False)
    for obj in scene['objects']:
        dx, dy = obj['display_translation']
        vertices, codes = [], []
        for edge in obj['edges']:
            for segment in edge['segments']:
                if not vertices:
                    vertices.append((segment[0][0] + dx, segment[0][1] + dy))
                    codes.append(MplPath.MOVETO)
                for x, y in segment[1:]:
                    vertices.append((x + dx, y + dy))
                    codes.append(MplPath.CURVE4)
        vertices.append(vertices[0])
        codes.append(MplPath.CLOSEPOLY)
        artist = PathPatch(MplPath(vertices, codes), facecolor='none',
                           edgecolor='black', linewidth=1, antialiased=True,
                           capstyle='round', joinstyle='round')
        artist.set_gid(obj['id'])
        ax.add_patch(artist)
    for label in scene['labels']:
        artist = ax.text(*label['anchor'], label['text'], ha='center', va='center',
                         fontsize=16, color='black', fontstyle='normal')
        artist.set_gid(label['id'])
    output = output if output.is_absolute() else HERE / output
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=100, facecolor='white', transparent=False,
                metadata={'Software': 'MathPalette staged cubic renderer'})
    if svg:
        svg = svg if svg.is_absolute() else HERE / svg
        svg.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(svg, facecolor='white', transparent=False,
                    metadata={'Date': None, 'Creator': 'MathPalette staged cubic renderer'})
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('baseline.png'))
    parser.add_argument('--svg', type=Path)
    args = parser.parse_args()
    draw(args.output, args.svg)
