"""Frozen scene renderer; importing this module has no output side effect."""
from __future__ import annotations
import argparse,json
from pathlib import Path

def render(output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.path import Path as MPath
    from matplotlib.patches import PathPatch,Circle,FancyArrowPatch
    root=Path(__file__).resolve().parent
    scene=json.loads((root/'scene.json').read_text(encoding='utf-8'))
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path','svg.hashsalt':scene['id']})
    fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
    ax=fig.add_axes(scene['view']['layout']['axes_position']);ax.set_aspect('equal');ax.set_xlim(scene['view']['xlim']);ax.set_ylim(scene['view']['ylim']);ax.set_autoscale_on(False);ax.axis('off')
    for o in scene['objects']:
        if o['type']=='compound_fill':
            vertices=[];codes=[]
            for loop in o['loops']:
                vertices.extend(loop+[loop[0]]);codes.extend([MPath.MOVETO]+[MPath.LINETO]*(len(loop)-1)+[MPath.CLOSEPOLY])
            artist=PathPatch(MPath(vertices,codes),facecolor=o['fill_color'],edgecolor='none',zorder=1,antialiased=True);ax.add_patch(artist)
        elif o['type']=='segment':
            a,b=[scene['points'][k] for k in o['points']]
            artist,=ax.plot([a[0],b[0]],[a[1],b[1]],color='black',linewidth=1,solid_capstyle='round',dash_capstyle='butt',antialiased=True,zorder=3)
            if o['linestyle']=='dashed':artist.set_dashes([4,3])
        elif o['type']=='circle':
            artist=Circle(o['center'],o['radius'],fill=False,edgecolor='black',linewidth=1,zorder=3);ax.add_patch(artist)
        elif o['type']=='arrow':
            artist=FancyArrowPatch(o['start'],o['end'],arrowstyle='->',mutation_scale=10,color='black',linewidth=1,zorder=2);ax.add_patch(artist)
        else:raise ValueError(o['type'])
        artist.set_gid(o['id'])
    for t in scene['labels']:
        artist=ax.text(*t['anchor'],t['text'],ha=t['ha'],va=t['va'],fontsize=t['fontsize'],color='black');artist.set_gid(t['id'])
    output=Path(output)
    if not output.is_absolute():output=root/output
    fig.savefig(output,dpi=100,facecolor='white',transparent=False,metadata={'Creator':'MathPalette staged original renderer'} if output.suffix.lower()=='.svg' else {'Software':'MathPalette staged original renderer'})
    plt.close(fig)
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='baseline.png');args=parser.parse_args();print(render(args.output))
