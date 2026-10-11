"""Frozen MathVista analytic review candidates; no formal dataset writes."""
import json,sys,hashlib,shutil,platform
from pathlib import Path
import numpy as np
import matplotlib
from PIL import Image
ROOT=Path(__file__).resolve().parent
REPO=ROOT/'vendor'
sys.path.insert(0,str(REPO/'Analytics/dataset_generator'))
from common_renderer import open_canvas,plot_curve,scatter_points,label,fill_region,fill_polygon,finalize
ROWS={r['pid']:r for r in json.load(open(ROOT.parent/'special_source.json'))}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
SCENES={
'409':{'objects':[{'type':'circle','center':[0,0],'radius':5,'samples':1441}], 'labels':[], 'constraints':['Circle center at origin; intercepts ±5 read from source grid.'],'caveats':['Source cyan curve/grid and cream background normalized to protocol black/gray on white.']},
'671':{'objects':[{'type':'semicircle','center':[3,0],'radius':3,'theta_deg':[0,180],'samples':721},{'type':'region','x_interval':[3,6],'upper':'sqrt(9-(x-3)^2)','lower':0,'samples':721}], 'labels':[{'xy':[3.1,4],'text':r'$f(x)=\sqrt{9-(x-3)^2}$'}], 'constraints':['Semicircle center (3,0), radius 3, upper branch; shaded region is x=3 to x=6.'],'caveats':['Original wording asks size of semicircle, although only right half is shaded; original wording and shading retained without reinterpretation.']},
'926':{'objects':[{'type':'semicircle','center':[3,0],'radius':3,'theta_deg':[0,180],'samples':721},{'type':'region','x_interval':[3,6],'upper':'sqrt(9-(x-3)^2)','lower':0,'samples':721}], 'labels':[{'xy':[3.1,4],'text':r'$f(x)=\sqrt{9-(x-3)^2}$'}], 'constraints':['Semicircle center (3,0), radius 3, upper branch; shaded region is x=3 to x=6.'],'caveats':[]},
'706':{'objects':[{'type':'points','points':{'A':[8,2],'B':[8,8],'C':[2,8],'D':[-8,2],'E':[-2,-8],'source_dot':[8,-2]},'filled':True}], 'labels':[{'xy':[7.6,2.5],'text':'A'},{'xy':[7.6,7.5],'text':'B'},{'xy':[1.6,7.5],'text':'C'},{'xy':[-7.6,2.5],'text':'D'},{'xy':[-2.5,-7.5],'text':'E'}], 'constraints':['Coordinates read from grid, including unlabeled input point (8,-2); every labeled answer candidate retained.'],'caveats':['Source axes extend to about ±11. Protocol fixed window ±8 puts five points on boundary. Markers rendered unclipped and labels placed inward; coordinates unchanged.']},
'767':{'objects':[{'type':'circle','center':[0,0],'radius':5,'samples':1441},{'type':'line','equation':'3*x-4*y=25','points':[[-7/3,-8],[8,-.25]]},{'type':'points','points':{'P':[3,-4]},'filled':True}], 'labels':[{'xy':[3.4,6.25],'text':r'$x^2+y^2=25$'},{'xy':[4.4,-4.8],'text':r'$(3,-4)$'}], 'constraints':['3²+(-4)²=25; tangent 3x-4y=25 passes through (3,-4); radius (3,-4) orthogonal to tangent direction (4,3).'],'caveats':['Source blue point/tangent normalized black. Tangent clipped to fixed protocol viewport, rather than source image edges.']}
}
def draw_scene(scene,out):
 fig,ax=open_canvas()
 for o in scene['objects']:
  if o['type'] in ('circle','semicircle'):
   t=np.linspace(*(np.deg2rad(o.get('theta_deg',[0,360]))),o['samples']); c=o['center'];r=o['radius'];plot_curve(ax,c[0]+r*np.cos(t),c[1]+r*np.sin(t))
  elif o['type']=='polygon':
   p=np.array(o['points']);
   if o.get('semantic_fill'):fill_polygon(ax,p[:,0],p[:,1])
   q=np.vstack([p,p[0]]);plot_curve(ax,q[:,0],q[:,1])
  elif o['type']=='region':
   x=np.linspace(*o['x_interval'],o['samples']);fill_region(ax,x,np.sqrt(np.maximum(0,9-(x-3)**2)),0)
  elif o['type']=='points':
   p=np.array(list(o['points'].values()));scatter_points(ax,p[:,0],p[:,1]);ax.collections[-1].set_clip_on(False)
  elif o['type']=='line':
   p=np.array(o['points']);plot_curve(ax,p[:,0],p[:,1])
 for l in scene['labels']:label(ax,*l['xy'],l['text'])
 return finalize(fig,out)
def main():
 manifest=[]
 for pid,geom in SCENES.items():
  d=ROOT/pid;d.mkdir(exist_ok=True);r=ROWS[pid];shutil.copy2('/workspace/shared/mathvista_testmini_geometry/'+r['image'],d/'original.jpg')
  scene={'id':'MathVista_'+pid,'status':'review_candidate','subject':'Analytics','source_dataset':'MathVista testmini / '+r['metadata']['source'],'source_image':'original.jpg','view':{'xlim':[-8,8],'ylim':[-8,8],'aspect':'equal'},'protocol_version':'1.0.0','sampling':'frozen deterministic linspace; no random sampling',**geom}
  (d/'scene.json').write_text(json.dumps(scene,ensure_ascii=False,indent=2));(d/'source.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
  draw_scene(scene,d/'redraw.png');draw_scene(scene,d/'repeat.png');assert sha(d/'redraw.png')==sha(d/'repeat.png');(d/'repeat.png').unlink()
  (d/'redraw.py').write_text("import sys,json\nfrom pathlib import Path\nP=Path(__file__).resolve().parent\nsys.path.insert(0,str(P.parent))\nfrom build_analytic import draw_scene\nif __name__=='__main__': draw_scene(json.loads((P/'scene.json').read_text()),P/'redraw.png')\n")
  im=Image.open(d/'redraw.png').convert('RGBA');assert im.size==(768,768) and im.getextrema()[3]==(255,255)
  report={'source_sha256':sha(d/'original.jpg'),'scene_sha256':sha(d/'scene.json'),'image_sha256':sha(d/'redraw.png'),'renderer_sha256':sha(REPO/'Analytics/dataset_generator/common_renderer.py'),'protocol_sha256':sha(REPO/'Analytics/dataset_generator/protocol.json'),'reproduction_script_sha256':sha(d/'redraw.py'),'repeat_render_identical':True,'size':[768,768],'opaque':True,'visual_qa':'pending','dependencies':{'python':platform.python_version(),'numpy':np.__version__,'matplotlib':matplotlib.__version__},'constraint_checks':scene['constraints']}
  (d/'redraw_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
  manifest.append({'pid':pid,'category':'analytic','status':'rendered_pending_visual_qa','source_image':f'{pid}/original.jpg','output_image':f'{pid}/redraw.png','scene':f'{pid}/scene.json','caveats':scene['caveats'],'QA':report})
 pid='512';d=ROOT/pid;d.mkdir(exist_ok=True);shutil.copy2('/workspace/shared/mathvista_testmini_geometry/images/512.jpg',d/'original.jpg');(d/'source.json').write_text(json.dumps(ROWS[pid],ensure_ascii=False,indent=2))
 reason='Original figure specifies an isosceles right triangle with equal legs a, but no numerical a or axis scale. Rendering with mandatory integer ticks on fixed [-8,8] axes would introduce an unsupported metric scale. Need user-approved symbolic-axis exception or missing numerical a; official answer 0.24 is not used to infer a.'
 report={'pid':pid,'status':'blocked_protocol_scale_conflict','source_inspected':True,'reason':reason,'original_sha256':sha(d/'original.jpg'),'required_decision':'Permit symbolic unnumbered axes, or provide missing length a.'};(d/'redraw_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));manifest.append({'pid':pid,'category':'analytic','status':report['status'],'source_image':f'{pid}/original.jpg','output_image':None,'scene':None,'caveats':[reason],'QA':report})
 (ROOT/'analytic_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
