"""Frozen vector scene renderer. Importing this module does not write files."""
from __future__ import annotations
import argparse
import json
import os
import platform
from pathlib import Path

HERE = Path(__file__).resolve().parent

def draw(output: Path) -> dict:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    import PIL
    import numpy

    scene = json.loads((HERE / 'scene.json').read_text(encoding='utf-8'))
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 16,
        'svg.fonttype': 'path', 'svg.hashsalt': 'Plane301-author-originals-20261105',
        'path.simplify': False,
    })
    fig = plt.figure(figsize=(7.68, 7.68), dpi=100, facecolor='white')
    ax = fig.add_axes(scene['view']['layout'])
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(scene['view']['xlim'])
    ax.set_ylim(scene['view']['ylim'])
    ax.set_autoscale_on(False)
    ax.axis('off')
    points = scene['points']
    for obj in scene['objects']:
        if obj['type'] == 'segment':
            a, b = (points[k] for k in obj['point_ids'])
            artist, = ax.plot([a[0], b[0]], [a[1], b[1]], color='black',
                             linewidth=1, solid_capstyle='round', antialiased=True,
                             zorder=2)
        elif obj['type'] == 'point_marker':
            p = points[obj['point_id']]
            artist = ax.scatter([p[0]], [p[1]], s=36, c='black',
                                edgecolors='black', linewidths=1, zorder=4)
        else:
            raise ValueError(f"Unsupported object: {obj['type']}")
        artist.set_gid(obj['id'])
    for label in scene['labels']:
        artist = ax.text(*label['position'], label['text'], color='black',
                         fontsize=16, ha='center', va='center', zorder=5,
                         fontfamily='DejaVu Sans', clip_on=False)
        artist.set_gid(label['id'])
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boxes = [a.get_window_extent(renderer) for a in ax.texts]
    for p in points.values():
        xp, yp = ax.transData.transform(p)
        from matplotlib.transforms import Bbox
        # scatter's 6 pt marker plus its 1 pt outline.
        rad = 3.5 * fig.dpi / 72
        boxes.append(Bbox.from_extents(xp-rad, yp-rad, xp+rad, yp+rad))
    from matplotlib.transforms import Bbox
    box = Bbox.union(boxes)
    layout_check = {
        'bbox_pixels_bottom_left_origin': list(map(float,box.extents)),
        'center_offset_px': [float((box.x0+box.x1)/2-384), float((box.y0+box.y1)/2-384)],
        'long_side_fraction': float(max(box.width,box.height)/768),
        'minimum_margin_fraction': float(min(box.x0,box.y0,768-box.x1,768-box.y1)/768),
        'aspect_equal': True, 'linewidth_pt': 1, 'point_area_pt2': 36,
    }
    assert layout_check['minimum_margin_fraction'] >= .05
    assert max(map(abs, layout_check['center_offset_px'])) <= 2
    assert .85 <= layout_check['long_side_fraction'] <= .87
    output = output if output.is_absolute() else HERE/output
    if output.suffix.lower() == '.svg':
        fig.savefig(output, format='svg', facecolor='white', transparent=False,
                    metadata={'Date': '2026-11-05', 'Creator': 'MathPalette staged original renderer'})
    else:
        fig.savefig(output, dpi=100, format='png', facecolor='white', transparent=False,
                    metadata={'Software': 'MathPalette staged original renderer'})
    plt.close(fig)
    info = {'pid': os.getpid(), 'output': output.name, 'layout': layout_check,
            'versions': {'python': platform.python_version(), 'matplotlib': matplotlib.__version__,
                         'numpy': numpy.__version__, 'pillow': PIL.__version__,
                         'freetype': matplotlib.ft2font.__freetype_version__},
            'font_filename': Path(font_manager.findfont('DejaVu Sans')).name}
    return info

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='baseline.png')
    parser.add_argument('--run-record')
    args = parser.parse_args()
    info = draw(Path(args.output))
    if args.run_record:
        path = Path(args.run_record)
        path = path if path.is_absolute() else HERE/path
        path.write_text(json.dumps(info, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(info))

if __name__ == '__main__':
    main()
