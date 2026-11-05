"""Frozen-scene renderer. Importing this module has no output side effects."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def draw(output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    root = Path(__file__).resolve().parent
    scene = json.loads((root/'scene.json').read_text(encoding='utf-8'))
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,
                         'svg.fonttype':'path','svg.hashsalt':'Plane456-author-originals-v1',
                         'lines.antialiased':True,'patch.antialiased':True})
    fig = plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
    ax = fig.add_axes(scene['view']['layout']['axes_position'],aspect='equal')
    ax.set_xlim(scene['view']['xlim'])
    ax.set_ylim(scene['view']['ylim'])
    ax.set_autoscale_on(False)
    ax.axis('off')
    points = {k:tuple(float(Fraction(v)) for v in p) for k,p in scene['points'].items()}
    for obj in scene['objects']:
        vertices = [points[p] for p in obj['points']]
        if obj['type'] == 'polygon' and obj['role'] == 'semantic_fill':
            artist = Polygon(vertices,closed=True,facecolor='#E8E8E8',edgecolor='none',
                             linewidth=0,antialiased=True,zorder=1)
            ax.add_patch(artist)
        elif obj['type'] == 'segment':
            artist, = ax.plot([p[0] for p in vertices],[p[1] for p in vertices],
                              color='black',linewidth=1,solid_capstyle='round',
                              antialiased=True,zorder=2)
        else:
            raise ValueError(obj)
        artist.set_gid(obj['id'])
    for label in scene['labels']:
        artist = ax.annotate(label['text'],points[label['anchor']],xytext=label['offset_pt'],
                             textcoords='offset points',ha=label.get('ha','center'),
                             va=label.get('va','center'),fontsize=label.get('font_size_pt',16),
                             fontstyle=label.get('font_style','normal'),color='black',
                             annotation_clip=False,zorder=5)
        artist.set_gid(label['id'])
    output = Path(output)
    if not output.is_absolute():
        output = root/output
    fig.savefig(output,dpi=100,facecolor='white',transparent=False,
                metadata={'Date':None} if output.suffix.lower()=='.svg' else {'Software':'MathPalette frozen original renderer'})
    plt.close(fig)
    print(str(output))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='baseline.png')
    args=parser.parse_args()
    draw(args.output)


if __name__=='__main__':
    main()
