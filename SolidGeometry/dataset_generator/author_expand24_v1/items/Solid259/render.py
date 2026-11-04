import argparse, json, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(HERE / "mplconfig"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    s = json.loads((HERE/'scene.json').read_text(encoding='utf-8'))
    fig = plt.figure(figsize=(7.68,7.68), dpi=100, facecolor='white')
    ax = fig.add_axes([.05,.05,.90,.90]); ax.set_aspect('equal'); ax.axis('off')
    ax.set_xlim(*s['view']['xlim']); ax.set_ylim(*s['view']['ylim']); ax.set_autoscale_on(False)
    def xy(p):
        return [sum(row[i]*(p[i]-s['projection']['origin'][i]) for i in range(3))+s['projection']['offset'][j] for j,row in enumerate(s['projection']['matrix'])]
    for obj in sorted(s['objects'], key=lambda x: x['visibility'] == 'visible'):
        a,b = map(xy,obj['points']); ln, = ax.plot([a[0],b[0]],[a[1],b[1]], color='black', lw=1, solid_capstyle='round', dash_capstyle='butt', antialiased=True)
        if obj['visibility']=='hidden': ln.set_dashes([4,3])
    for pt in s['marked_points']:
        x,y=xy(pt['world_xyz']); ax.scatter([x],[y],s=36,c='black',linewidths=1,zorder=4)
    for label in s['labels']:
        x,y=xy(label['world_xyz']); ax.annotate(label['text'], (x,y), xytext=label['offset_pt'], textcoords='offset points', ha=label['ha'], va=label['va'], family='DejaVu Sans', fontsize=18, fontstyle='italic')
    fig.savefig(args.output, dpi=100, facecolor='white', transparent=False)
    plt.close(fig)
if __name__=='__main__': main()
