"""Frozen-scene renderer; importing this file has no file-writing side effects."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Arc
import numpy as np


def render(scene_path: Path, output: Path) -> None:
    scene = json.loads(scene_path.read_text(encoding='utf-8'))
    with matplotlib.rc_context({'font.family': 'DejaVu Sans', 'font.size': 16,
                               'svg.fonttype': 'path', 'svg.hashsalt': 'Plane180-author-folds'}):
        fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
        ax = fig.add_axes(scene['view']['layout']['axes_position'])
        ax.set_aspect('equal')
        ax.set_xlim(scene['view']['xlim'])
        ax.set_ylim(scene['view']['ylim'])
        ax.set_autoscale_on(False)
        ax.axis('off')
        points = scene['points']
        for ob in scene['objects']:
            typ = ob['type']
            if typ == 'polygon':
                artist = Polygon([points[p] for p in ob['points']], closed=True,
                                 facecolor=ob.get('fill', 'white'), edgecolor='none',
                                 zorder=ob['zorder'], antialiased=True)
                ax.add_patch(artist)
            elif typ == 'segment':
                coords = np.array([points[p] for p in ob['points']])
                style = (0, (4, 3)) if ob.get('linestyle') == 'dashed' else '-'
                artist, = ax.plot(coords[:, 0], coords[:, 1], color='black',
                                  linewidth=1, linestyle=style, solid_capstyle='round',
                                  dash_capstyle='butt', antialiased=True, zorder=ob['zorder'])
            elif typ == 'angle_arc':
                a, v, b = [np.array(points[p]) for p in ob['points']]
                aa = np.degrees(np.arctan2(*(a-v)[::-1])) % 360
                bb = np.degrees(np.arctan2(*(b-v)[::-1])) % 360
                sweep = (bb-aa) % 360
                if (sweep > 180) != ob.get('reflex', False):
                    aa, bb = bb, aa
                    sweep = (bb-aa) % 360
                pixels_per_unit = ax.get_window_extent().width / np.diff(ax.get_xlim())[0]
                radius = ob['radius_pt'] * fig.dpi / 72 / pixels_per_unit
                artist = Arc(v, 2*radius, 2*radius, theta1=aa, theta2=aa+sweep,
                             linewidth=1, color='black', zorder=ob['zorder'])
                ax.add_patch(artist)
            else:
                raise ValueError(f'Unsupported object {typ}')
            artist.set_gid(ob['id'])
        for label in scene['labels']:
            pos = np.array(label['position'])
            artist = ax.text(*pos, label['text'], fontsize=label.get('font_size',16),
                             fontstyle='italic' if label['type']=='point_name' else 'normal',
                             ha='center', va='center', color='black', zorder=100, clip_on=False)
            artist.set_gid(label['id'])
        metadata = {'Date': None} if output.suffix.lower()=='.svg' else {'Software':'MathPalette staged folding renderer'}
        fig.savefig(output, dpi=100, facecolor='white', transparent=False,
                    bbox_inches=None, metadata=metadata)
        plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='baseline.png')
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    out = Path(args.output)
    if not out.is_absolute():
        out = here / out
    render(here/'scene.json', out)


if __name__ == '__main__':
    main()
