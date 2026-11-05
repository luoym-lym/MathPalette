"""Render only frozen vector objects. Importing this module writes nothing."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def create_figure(scene):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':16,
        'svg.fonttype':'path', 'svg.hashsalt':'Solid198-author-originals-v1',
        'lines.antialiased':True, 'patch.antialiased':True})
    fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
    ax=fig.add_axes([.05,.05,.9,.9])
    ax.set_aspect('equal'); ax.set_xlim(scene['view']['xlim']); ax.set_ylim(scene['view']['ylim'])
    ax.set_axis_off(); ax.set_autoscale_on(False)
    matrix=scene['projection']['matrix']
    def project(p):
        return [sum(matrix[i][j]*p[j] for j in range(3)) for i in range(2)]
    for obj in scene['objects']:
        if obj['type']=='face':
            artist=Polygon([project(p) for p in obj['points']],closed=True,
                facecolor=scene['materials'][obj['material']]['fill'],edgecolor='none',
                linewidth=0,antialiased=False,zorder=1)
            artist.set_gid(obj['id']); ax.add_patch(artist)
    for obj in scene['objects']:
        if obj['type']=='segment' and obj['visibility']=='visible':
            p,q=map(project,obj['points'])
            artist,=ax.plot([p[0],q[0]],[p[1],q[1]],color='black',linewidth=1,
                solid_capstyle='round',antialiased=True,zorder=2)
            artist.set_gid(obj['id'])
    for label in scene['labels']:
        artist=ax.text(*label['position_2d'],label['text'],ha='center',va='top',
            color='black',fontfamily='DejaVu Sans',fontsize=16,zorder=3)
        artist.set_gid(label['id'])
    return fig,ax

def draw(scene_path, output):
    import matplotlib.pyplot as plt
    scene=json.loads(Path(scene_path).read_text(encoding='utf-8'))
    fig,_=create_figure(scene)
    out=Path(output)
    if not out.is_absolute(): out=HERE/out
    out.parent.mkdir(parents=True,exist_ok=True)
    metadata={'Date':None} if out.suffix.lower()=='.svg' else {'Software':'MathPalette staged authoring'}
    fig.savefig(out,dpi=100,facecolor='white',transparent=False,metadata=metadata)
    if out.suffix.lower()=='.png':
        fig.savefig(out.with_suffix('.svg'),facecolor='white',transparent=False,metadata={'Date':None})
    plt.close(fig)
    return out

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='baseline.png')
    args=parser.parse_args()
    print(draw(HERE/'scene.json',args.output))

if __name__=='__main__': main()
