"""Frozen-data renderer. Importing this module never writes an image."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Polygon

ROOT=Path(__file__).resolve().parent

def create_figure(scene):
    matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':16,
        'svg.fonttype':'path','svg.hashsalt':'MathPalette-Plane243-author-extensions',
        'path.simplify':False, 'savefig.transparent':False})
    fig=Figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
    FigureCanvasAgg(fig)
    ax=fig.add_axes(scene['view']['layout']['axes_position'])
    ax.set(xlim=scene['view']['xlim'],ylim=scene['view']['ylim'],aspect='equal')
    ax.set_autoscale_on(False); ax.set_axis_off()
    points=scene['points']; artists=[]
    for obj in scene['objects']:
        kind=obj['type']
        if kind=='polygon':
            artist=Polygon([points[k] for k in obj['points']],closed=True,
                fill=False,edgecolor='black',linewidth=1,antialiased=True,
                joinstyle='miter',zorder=2)
            ax.add_patch(artist)
        elif kind=='segment':
            a,b=[points[k] for k in obj['points']]
            artist=Line2D([a[0],b[0]],[a[1],b[1]],color='black',linewidth=1,
                solid_capstyle='butt',antialiased=True,zorder=2)
            ax.add_line(artist)
        elif kind=='point_marker':
            artist=Circle(points[obj['center']],radius=obj['radius'],
                facecolor='black',edgecolor='black',linewidth=1,
                antialiased=True,zorder=4)
            ax.add_patch(artist)
        else:
            raise ValueError(f'Unsupported frozen object: {kind}')
        artist.set_gid(obj['id']); artists.append(artist)
    for label in scene['labels']:
        x,y=points[label['anchor']]
        artist=ax.text(x,y,label['text'],ha='center',va='top',
            fontsize=16,fontfamily='DejaVu Sans',color='black',clip_on=False,zorder=5)
        artist.set_gid(label['id']); artists.append(artist)
    return fig,ax,artists

def render(scene_path,output):
    scene=json.loads(Path(scene_path).read_text(encoding='utf-8'))
    fig,ax,artists=create_figure(scene)
    suffix=Path(output).suffix.lower()
    if suffix not in {'.png','.svg'}: raise ValueError('Use .png or .svg output')
    metadata={'Date':None,'Creator':'MathPalette frozen original renderer'} if suffix=='.svg' else {'Software':'MathPalette frozen original renderer'}
    fig.savefig(output,format=suffix[1:],dpi=100,facecolor='white',
        transparent=False,bbox_inches=None,pad_inches=0,metadata=metadata)
    fig.clear()
    return output

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='baseline.png')
    parser.add_argument('--svg',action='store_true',help='Also export the same scene to SVG')
    args=parser.parse_args()
    output=Path(args.output)
    if not output.is_absolute(): output=ROOT/output
    render(ROOT/'scene.json',output)
    if args.svg: render(ROOT/'scene.json',output.with_suffix('.svg'))
    print(json.dumps({'pid':os.getpid(),'scene':'scene.json','output':str(output),
        'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}))

if __name__=='__main__': main()
