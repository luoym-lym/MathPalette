"""Render frozen vector outlines. Importing this module never produces images."""
from pathlib import Path
import argparse
import json


def make_figure(scene):
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.patches import Polygon
    matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':16,
                                'svg.fonttype':'path','svg.hashsalt':'Plane248-originals-v1',
                                'path.simplify':False})
    fig=Figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
    FigureCanvasAgg(fig)
    ax=fig.add_axes(scene['view']['layout']['axes_position'])
    ax.set_aspect('equal',adjustable='box')
    ax.set_xlim(scene['view']['xlim']); ax.set_ylim(scene['view']['ylim'])
    ax.set_autoscale_on(False); ax.set_axis_off()
    artists=[]
    for obj in scene['objects']:
        if obj['type']!='polygon':
            raise ValueError('unknown object type')
        patch=Polygon([scene['points'][p] for p in obj['points']],closed=True,
                      facecolor='none',edgecolor='black',linewidth=1.0,
                      antialiased=True,joinstyle='miter',capstyle='round')
        patch.set_gid(obj['id']); ax.add_patch(patch); artists.append(patch)
    for label in scene['labels']:
        a=ax.text(*label['anchor'],label['text'],ha='center',va='center',
                  fontsize=16,fontfamily='DejaVu Sans',fontstyle='normal',
                  color='black',clip_on=False)
        a.set_gid(label['id']); artists.append(a)
    return fig,ax,artists


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='baseline.png')
    args=parser.parse_args()
    root=Path(__file__).resolve().parent
    scene=json.loads((root/'scene.json').read_text(encoding='utf-8'))
    output=Path(args.output)
    if not output.is_absolute():
        output=root/output
    if not output.resolve().is_relative_to(root):
        parser.error('output must remain inside this draft directory')
    output.parent.mkdir(parents=True,exist_ok=True)
    fig,ax,artists=make_figure(scene)
    metadata={'Date':None,'Creator':'MathPalette staged Author Designed renderer'} if output.suffix.lower()=='.svg' else {'Software':'MathPalette staged renderer'}
    fig.savefig(output,dpi=100,facecolor='white',transparent=False,metadata=metadata)
    print(json.dumps({'output':str(output),'size_px':[768,768],'objects':len(scene['objects'])}))


if __name__=='__main__':
    main()
