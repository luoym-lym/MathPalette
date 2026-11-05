"""Draw only the frozen scene; importing this module creates no output images."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
from datetime import datetime, timezone

import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from matplotlib import ft2font
import PIL
from PIL import Image
import numpy

HERE = Path(__file__).resolve().parent


def dependencies():
    return {'python': platform.python_version(), 'matplotlib': matplotlib.__version__,
            'pillow': PIL.__version__, 'numpy': numpy.__version__,
            'freetype': ft2font.__freetype_version__, 'font': 'DejaVu Sans'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def make_figure(scene):
    matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 16,
                               'svg.fonttype': 'path', 'svg.hashsalt': 'Plane159-originals-v1',
                               'path.simplify': False})
    fig = Figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
    FigureCanvasAgg(fig)
    ax = fig.add_axes(scene['view']['layout']['axes_position'])
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(scene['view']['xlim'])
    ax.set_ylim(scene['view']['ylim'])
    ax.set_autoscale_on(False)
    ax.axis('off')
    points = scene['points']
    artists = []
    for obj in scene['objects']:
        coords = [points[p] for p in obj['points']]
        if obj['type'] == 'polygon':
            artist = Polygon(coords, closed=True, facecolor=obj['semantic_color'],
                             edgecolor='none', linewidth=0, antialiased=False,
                             zorder=1)
            ax.add_patch(artist)
        elif obj['type'] == 'segment':
            artist = Line2D([p[0] for p in coords], [p[1] for p in coords],
                            color='black', linewidth=1, solid_capstyle='round',
                            antialiased=True, zorder=2)
            ax.add_line(artist)
        else:
            raise ValueError(f"Unsupported object: {obj['type']}")
        artist.set_gid(obj['id'])
        artists.append(artist)
    for label in scene['labels']:
        artist = ax.text(*label['anchor'], label['text'], ha='center', va='center',
                         color='black', fontsize=16, fontfamily='DejaVu Sans',
                         fontstyle='normal', zorder=3, clip_on=False)
        artist.set_gid(label['id'])
        artists.append(artist)
    return fig, ax, artists


def draw(scene_path, output_path):
    scene = json.loads(Path(scene_path).read_text(encoding='utf-8'))
    fig, ax, artists = make_figure(scene)
    target = Path(output_path)
    if not target.is_absolute():
        target = HERE / target
    metadata = {'Creator': 'MathPalette staged Author Designed renderer'}
    if target.suffix.lower() == '.svg':
        metadata['Date'] = None
    fig.savefig(target, dpi=100, facecolor='white', transparent=False,
                bbox_inches=None, pad_inches=0, metadata=metadata)
    fig.clear()
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='baseline.png')
    parser.add_argument('--svg')
    parser.add_argument('--record')
    args = parser.parse_args()
    started = datetime.now(timezone.utc).isoformat()
    target = draw(HERE / 'scene.json', args.output)
    if args.svg:
        draw(HERE / 'scene.json', args.svg)
    if args.record:
        with Image.open(target) as im:
            rgba = im.convert('RGBA')
            fingerprint = hashlib.sha256(rgba.tobytes()).hexdigest()
            size = list(im.size)
            alpha = list(rgba.getchannel('A').getextrema())
        record = {'started_utc': started, 'completed_utc': datetime.now(timezone.utc).isoformat(),
                  'pid': os.getpid(), 'output': target.name,
                  'scene_sha256': sha(HERE / 'scene.json'), 'renderer_sha256': sha(__file__),
                  'file_sha256': sha(target), 'decoded_rgba_sha256': fingerprint,
                  'size': size, 'alpha_extrema': alpha, 'dependencies': dependencies(),
                  'invocation': ['python', '-X', 'utf8', '-B', 'render.py', *os.sys.argv[1:]],
                  'write_isolation': {k: os.environ.get(k) for k in
                                      ['PYTHONDONTWRITEBYTECODE', 'MPLCONFIGDIR', 'TEMP', 'TMP']}}
        (HERE / args.record).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': target.name, 'pid': os.getpid(), 'rendered': True}))


if __name__ == '__main__':
    main()
