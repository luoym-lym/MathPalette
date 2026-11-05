"""Frozen vector scene renderer. Importing this module writes no files."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

def draw(scene_path, output):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    scene=json.loads(Path(scene_path).read_text(encoding='utf-8'))
    with matplotlib.rc_context({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path','svg.hashsalt':'Plane220AuthorOriginals','path.simplify':False,'lines.antialiased':True}):
        fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
        ax=fig.add_axes(scene['view']['layout']['axes_position'])
        ax.set_xlim(scene['view']['xlim']);ax.set_ylim(scene['view']['ylim'])
        ax.set_aspect('equal',adjustable='box');ax.set_autoscale_on(False);ax.axis('off')
        for ob in scene['objects']:
            pts=[scene['points'][pid] for pid in ob['points']]
            if ob['type']=='polygon':
                artist=Polygon(pts,closed=True,facecolor=ob['facecolor'],edgecolor=ob['edgecolor'],linewidth=1,antialiased=True,zorder=1)
                ax.add_patch(artist)
            elif ob['type']=='segment':
                style=(0,(4,3)) if ob.get('dashed') else '-'
                artist=ax.plot([p[0] for p in pts],[p[1] for p in pts],color='#000000',linewidth=1,linestyle=style,solid_capstyle='round',dash_capstyle='butt',antialiased=True,zorder=2)[0]
            else:raise ValueError('Unsupported scene object: '+ob['type'])
            artist.set_gid(ob['id'])
        for label in scene['labels']:
            artist=ax.text(*label['anchor'],label['text'],fontsize=label.get('font_size_pt',16),color='black',ha='center',va='center',clip_on=False,zorder=5)
            artist.set_gid(label['id'])
        output=Path(output)
        metadata={'Date':None,'Creator':'Plane220 frozen local renderer'} if output.suffix.lower()=='.svg' else {'Software':'Plane220 frozen local renderer'}
        fig.savefig(output,dpi=100,facecolor='white',transparent=False,bbox_inches=None,pad_inches=0,metadata=metadata)
        plt.close(fig)

def main():
    base=Path(__file__).resolve().parent
    p=argparse.ArgumentParser();p.add_argument('--output',default='baseline.png');a=p.parse_args()
    output=Path(a.output)
    if not output.is_absolute():output=base/output
    draw(base/'scene.json',output)
    print(str(output))

if __name__=='__main__':main()
