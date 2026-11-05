"""Frozen data renderer; importing this module never writes files."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parent


def render(output: Path, record: Path | None = None) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon
    import numpy as np
    import PIL
    from PIL import Image

    scene = json.loads((ROOT / 'scene.json').read_text(encoding='utf-8'))
    rc = {'font.family': 'DejaVu Sans', 'font.size': 16,
          'svg.fonttype': 'path', 'svg.hashsalt': scene['id'],
          'lines.linewidth': 1.0, 'patch.linewidth': 1.0}
    with matplotlib.rc_context(rc):
        fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
        ax = fig.add_axes(scene['view']['layout']['axes_position'])
        ax.set(xlim=scene['view']['xlim'], ylim=scene['view']['ylim'], aspect='equal')
        ax.set_autoscale_on(False)
        ax.axis('off')
        points = scene['points']
        for obj in scene['objects']:
            kind = obj['type']
            if kind == 'segment':
                a, b = [points[p] for p in obj['points']]
                artist = Line2D([a[0], b[0]], [a[1], b[1]], color='black',
                                linewidth=1, solid_capstyle='round', zorder=obj.get('zorder', 2))
                ax.add_line(artist)
            elif kind == 'circle':
                artist = Circle(points[obj['center']], obj['radius'],
                                edgecolor='black', facecolor=obj['facecolor'],
                                linewidth=1, zorder=obj.get('zorder', 3))
                ax.add_patch(artist)
            elif kind == 'polygon':
                artist = Polygon([points[p] for p in obj['points']], closed=True,
                                 edgecolor='black', facecolor='black', linewidth=1,
                                 zorder=4)
                ax.add_patch(artist)
            elif kind == 'angle_arc':
                # Radius is frozen in page points; conversion preserves the mark size.
                unit_px = ax.bbox.width / (scene['view']['xlim'][1] - scene['view']['xlim'][0])
                radius = obj['radius_pt'] * fig.dpi / 72 / unit_px
                center = points[obj['points'][1]]
                artist = Arc(center, 2 * radius, 2 * radius,
                             theta1=obj['theta1'], theta2=obj['theta2'],
                             edgecolor='black', linewidth=1, zorder=4)
                ax.add_patch(artist)
            else:
                raise ValueError(f'Unsupported object: {kind}')
            artist.set_gid(obj['id'])
        for label in scene['labels']:
            p = points[label['point']]
            artist = ax.annotate(label['text'], p, xytext=label['offset_pt'],
                                 textcoords='offset points', fontsize=label['size_pt'],
                                 fontstyle=label.get('fontstyle', 'normal'),
                                 ha=label.get('ha', 'center'), va=label.get('va', 'center'),
                                 color='black', annotation_clip=False, zorder=5)
            artist.set_gid(label['id'])
        output.parent.mkdir(parents=True, exist_ok=True)
        fmt = output.suffix.lstrip('.').lower()
        assert fmt in {'png', 'svg'}
        fig.savefig(output, format=fmt, dpi=100, facecolor='white', transparent=False,
                    bbox_inches=None,
                    metadata={'Date': None} if fmt == 'svg' else {'Software': 'MathPalette staged originals'})
        plt.close(fig)
    if record:
        sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
        data = {'pid': os.getpid(), 'output': str(output.relative_to(ROOT)),
                'output_sha256': sha(output), 'scene_sha256': sha(ROOT / 'scene.json'),
                'renderer_sha256': sha(Path(__file__)),
                'dependencies': {'python': platform.python_version(),
                                 'matplotlib': matplotlib.__version__, 'numpy': np.__version__,
                                 'Pillow': PIL.__version__,
                                 'FreeType': matplotlib.ft2font.__freetype_version__}}
        if fmt == 'png':
            rgba = np.asarray(Image.open(output).convert('RGBA'))
            yy, xx = np.where(np.any(rgba[:, :, :3] < 245, axis=2))
            data.update({'rgba_sha256': hashlib.sha256(rgba.tobytes()).hexdigest(),
                         'dimensions': [rgba.shape[1], rgba.shape[0]],
                         'opaque': bool(np.all(rgba[:, :, 3] == 255)),
                         'content_bbox_px': [int(xx.min()), int(yy.min()), int(xx.max()), int(yy.max())]})
        record.parent.mkdir(parents=True, exist_ok=True)
        record.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='baseline.png')
    parser.add_argument('--record')
    args = parser.parse_args()
    output = (ROOT / args.output).resolve()
    rec = (ROOT / args.record).resolve() if args.record else None
    render(output, rec)
