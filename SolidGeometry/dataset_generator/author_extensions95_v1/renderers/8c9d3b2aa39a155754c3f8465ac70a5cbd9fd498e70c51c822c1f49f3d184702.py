"""Draw only frozen vector objects; import has no filesystem side effects."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent

def draw(output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    scene=json.loads((HERE/'scene.json').read_text(encoding='utf-8'))
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path',
                         'svg.hashsalt':scene['id'],'hatch.linewidth':0.6,'path.simplify':False})
    fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
    ax=fig.add_axes([.05,.05,.90,.90])
    ax.set(xlim=scene['view']['xlim'],ylim=scene['view']['ylim'],aspect='equal')
    ax.set_axis_off(); ax.set_autoscale_on(False)
    matrix=scene['projection']['matrix']
    offsets={m['id']:m['display_offset_2d'] for m in scene['models']}
    def xy(point,model):
        return [sum(matrix[i][j]*point[j] for j in range(3))+offsets[model][i] for i in range(2)]
    for obj in scene['objects']:
        ps=[xy(p,obj['model_id']) for p in obj['points']]
        if obj['type']=='face':
            material=scene['materials'][obj['material']]
            patch=Polygon(ps,closed=True,facecolor=material['fill'],edgecolor='black' if material.get('hatch') else 'none',
                          linewidth=0,hatch=material.get('hatch'),antialiased=False,zorder=1)
            patch.set_gid(obj['id']);ax.add_patch(patch)
        elif obj['type']=='segment':
            artist,=ax.plot(*zip(*ps),color='black',linewidth=1.,solid_capstyle='round',antialiased=True,zorder=2)
            artist.set_gid(obj['id'])
        else:raise ValueError(obj['type'])
    for label in scene['labels']:
        artist=ax.text(*label['position_2d'],label['text'],ha='center',va='top',color='black',fontsize=16,zorder=3)
        artist.set_gid(label['id'])
    output=Path(output)
    if not output.is_absolute():output=HERE/output
    metadata={'Date':None,'Creator':'MathPalette task-local frozen cube renderer'} if output.suffix.lower()=='.svg' else {'Software':'MathPalette task-local frozen cube renderer'}
    fig.savefig(output,dpi=100,facecolor='white',transparent=False,metadata=metadata)
    plt.close(fig)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='baseline.png')
    args=parser.parse_args();draw(args.output)

if __name__=='__main__':main()
