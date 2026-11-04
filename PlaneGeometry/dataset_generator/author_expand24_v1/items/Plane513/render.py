"""Render the neighboring frozen scene; import has no drawing side effects."""
from pathlib import Path
import argparse,json,os
os.environ.setdefault('MPLCONFIGDIR',str(Path(__file__).resolve().parent.parent/'mplconfig'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Circle

def main():
 parser=argparse.ArgumentParser(); parser.add_argument('--output',required=True); a=parser.parse_args()
 s=json.loads(Path(__file__).with_name('scene.json').read_text(encoding='utf-8'))
 plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'svg.fonttype':'path','path.simplify':False})
 fig=plt.figure(figsize=(7.68,7.68),dpi=100,facecolor='white'); ax=fig.add_axes(s['view']['layout']['axes_position']); ax.set_aspect('equal',adjustable='box'); ax.set_xlim(*s['view']['xlim']); ax.set_ylim(*s['view']['ylim']); ax.set_axis_off()
 for o in s['objects']:
  kw=dict(fill=False,edgecolor='black',linewidth=1,antialiased=True,joinstyle='round',zorder=2)
  ax.add_patch(Polygon(o['points'],closed=True,**kw) if o['type']=='polygon' else Circle(o['center'],o['radius'],**kw))
 for t in s['labels']: ax.text(*t['anchor'],t['text'],ha='center',va='center',fontsize=16,color='black',zorder=5)
 fig.savefig(a.output,dpi=100,facecolor='white'); plt.close(fig)
if __name__=='__main__': main()
