"""Frozen native3D renderer with explicitly categorical source-material fills."""
from pathlib import Path
import sys,io,importlib.util
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('upper_solid_base',ROOT/'SolidGeometry/dataset_generator/common_renderer.py');base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
PROTOCOL_PATH=base.PROTOCOL_PATH
MATERIALS={'gray':('#BBBBBB',None),'dark':('#555555',None),'black':('#000000',None),'crosshatch':('#FFFFFF','xx'),'stars':('#FFFFFF','**')}
def image_bytes(scene,check_layout=True):
 fig,checks=base.render_scene(scene,check_layout=check_layout)
 faces=[o for o in scene['objects'] if o['type']=='face']
 assert len(fig.axes[0].patches)==len(faces)
 for ob,patch in zip(faces,fig.axes[0].patches):
  color,hatch=MATERIALS[ob['source_material']];patch.set_facecolor(color);patch.set_alpha(1)
  if hatch:patch.set_hatch(hatch);patch.set_edgecolor('#000000');patch.set_linewidth(0)
 try:
  out=io.BytesIO();fig.savefig(out,format='png',dpi=100,facecolor='white',transparent=False,bbox_inches=None,pad_inches=0,metadata={'Software':'MathPalette native solid categorical materials'});return out.getvalue(),checks
 finally:base.plt.close(fig)
def draw(scene_path,output_path):
 data,checks=image_bytes(base.read_json(scene_path));Path(output_path).write_bytes(data);return checks
