"""Family-isolated frozen renderers. No source pixels or cloud paths are used."""
from pathlib import Path
import importlib.util,json,sys,threading
_LOCK=threading.RLock()
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
def draw(family,scene_path,output_path):
 with _LOCK:
  root=Path(__file__).resolve().parent/family
  prior=sys.modules.get('common_renderer')
  try:
   renderer=load('common_renderer',root/'common_renderer.py')
   if family=='analytics_frozen':
    adapter=load('_mathverse_frozen',root/'frozen_renderer.py')
    if Path(output_path).suffix.lower()!='.svg':return adapter.draw(scene_path,output_path)
    fig,checks=adapter.render_scene(json.loads(Path(scene_path).read_text()));fig.savefig(output_path,format='svg',facecolor='#FFFFFF');renderer.plt.close(fig);return checks
   if family=='analytics_functions':
    adapter=load('_mathverse_functions',root/'render.py');fig,ax=adapter.build(json.loads(Path(scene_path).read_text()))
    if Path(output_path).suffix.lower()=='.svg':
     renderer.lock_view(ax);fig.savefig(output_path,format='svg',facecolor='#FFFFFF');renderer.plt.close(fig);return {'image_path':str(output_path)}
    return renderer.finalize(fig,output_path)
   return renderer.draw(scene_path,output_path)
  finally:
   if prior is not None:sys.modules['common_renderer']=prior
   else:sys.modules.pop('common_renderer',None)

def build_scene(family,scene_path):
 """Return a native editable Figure and Axes without saving or closing."""
 with _LOCK:
  root=Path(__file__).resolve().parent/family;prior=sys.modules.get('common_renderer')
  try:
   renderer=load('common_renderer',root/'common_renderer.py');scene=json.loads(Path(scene_path).read_text())
   if family=='analytics_functions':return load('_mathverse_functions',root/'render.py').build(scene)
   if family=='analytics_frozen':fig,checks=load('_mathverse_frozen',root/'frozen_renderer.py').render_scene(scene)
   else:fig,checks=renderer.render_scene(scene)
   return fig,fig.axes[0]
  finally:
   if prior is None:sys.modules.pop('common_renderer',None)
   else:sys.modules['common_renderer']=prior

def finalize(family,fig,output_path):
 root=Path(__file__).resolve().parent/family;renderer=load('_mathverse_finalize_'+family,root/'common_renderer.py')
 if family.startswith('analytics'):
  if Path(output_path).suffix.lower()=='.svg':
   renderer.lock_view(fig.axes[0]);fig.savefig(output_path,format='svg',facecolor='#FFFFFF');renderer.plt.close(fig);return {'image_path':str(output_path)}
  return renderer.finalize(fig,output_path)
 raise ValueError('Editable finalize is only required for Analytics; geometry uses render_scene/image_bytes.')
