"""Deterministic scene-only renderer; python -X utf8 -B render.py --output path.png."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True); args=parser.parse_args()
    root=Path(__file__).resolve().parent
    scene=json.loads((root/'scene.json').read_text(encoding='utf-8'))
    out=Path(args.output).resolve()
    if out in {(root/'scene.json').resolve(),(root/'render.py').resolve(),(root/'baseline.png').resolve()}:
        raise ValueError('Output must be a new path, not frozen inputs or baseline')
    if out.suffix.lower() not in ('.png','.svg'): raise ValueError('PNG or SVG required')
    with matplotlib.rc_context({'savefig.bbox':None,'svg.hashsalt':'Plane200-staged','svg.fonttype':'path'}):
        fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white')
        ax=fig.add_axes(scene['view']['layout']['axes_position']);ax.set_aspect('equal');ax.set_axis_off()
        ax.set_xlim(*scene['view']['xlim']);ax.set_ylim(*scene['view']['ylim']);ax.set_autoscale_on(False)
        for obj in scene['objects']:
            if obj['type']=='circle': patch=Circle(obj['center'],obj['radius'],edgecolor='black',facecolor='none',linewidth=1,antialiased=True)
            elif obj['type']=='polygon': patch=Polygon(obj['points'],closed=True,edgecolor='black',facecolor='none',linewidth=1,joinstyle='miter',antialiased=True)
            else: raise ValueError('Unknown object '+obj['type'])
            patch.set_gid(obj['id']);ax.add_patch(patch)
        fig.savefig(out,dpi=100,facecolor='white',transparent=False,bbox_inches=None,metadata={'Date':None} if out.suffix.lower()=='.svg' else {'Software':'Plane200 staged renderer'})
        plt.close(fig)
if __name__=='__main__': main()
