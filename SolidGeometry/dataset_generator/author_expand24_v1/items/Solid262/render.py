"""Render only the frozen scene. Example: python -X utf8 -B render.py --output baseline.png"""
import argparse,json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
 s=json.loads((Path(__file__).resolve().parent/'scene.json').read_text(encoding='utf8'))
 plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','path.simplify':False})
 fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white');ax=fig.add_axes([.05,.05,.9,.9]);ax.set_xlim(*s['view']['xlim']);ax.set_ylim(*s['view']['ylim']);ax.set_aspect('equal');ax.axis('off')
 for g in s['groups']:
  for f in g['faces']:
   xy=[g['points'][v]['xy'] for v in f['vertices']]
   ax.add_patch(Polygon(xy,closed=True,facecolor=f['fill'],edgecolor='black',linewidth=1,joinstyle='round',antialiased=True))
 for l in s['labels']:ax.text(*l['xy'],l['text'],fontsize=16,ha='center',va='center',color='black')
 fig.savefig(a.output,dpi=100,facecolor='white',metadata={'Software':'MathPalette stage one'});plt.close(fig)
if __name__=='__main__':main()
