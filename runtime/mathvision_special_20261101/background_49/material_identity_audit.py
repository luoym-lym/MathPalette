import research_env as env
import json,sys,math
import numpy as np
from inspect_sources import save,now
sys.path.insert(0,str(env.PROJECT/'SolidGeometry/workbench'))
from delivery_bridge_adapter import RendererAdapter
from workbench_io import load_config
n=json.loads((env.PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Solid163/scene.json').read_text(encoding='utf-8'))
out={}
for view in [0,1]:
 edges=[o for o in n['objects'] if o['id'].startswith(f'cube{view}e')]
 offset=np.min(np.array([p for o in edges for p in o['points']]),axis=0)
 faces=[o for o in n['objects'] if o['type']=='face' and o['id'].startswith(f'black{view}_')]
 cells=[]
 for f in faces:
  local=np.asarray(f['points'])-offset
  center=(local.max(axis=0)+local.min(axis=0))/2
  cell=tuple(min(2,max(0,int(math.floor(v+1e-10)))) for v in center)
  cells.append({'face_id':f['id'],'actual_local_world_quad':local.tolist(),'identified_cell':cell})
 derived=set(x['identified_cell'] for x in cells)
 expected=set(map(tuple,n['two_view_verification']['first_visible_black' if view==0 else 'second_visible_black']))
 assert derived==expected
 out[str(view)]={'native_translation':offset.tolist(),'black_cells_from_actual_face_geometry':sorted(derived),'metadata_agrees':derived==expected,'faces':cells}
adapter=RendererAdapter(load_config());scene=adapter.scene('Solid163')
try:
 scene.fig.canvas.draw()
 actual=[{'id':k,'facecolors':[list(a.get_facecolor()) for a in v if hasattr(a,'get_facecolor')]} for k,v in scene.artists.items() if k.startswith('black')]
 # The immutable formal bridge is the authority for the native displayed material color.
 out['formal_actual_material_artists']=actual
finally:scene.close()
out.update({'checked_at_utc':now(),'actual_source_and_formal_PNG_manually_compared':True,'human_image_check':'Both views show4 physically black boundary cubes each, including repeated faces of the same black corner cube. Source face shading differs from black/white membership and the approved formal PNG uses crisp binary black/white. No candidate for this item was made; original semantic fills unchanged.',
 'geometry_identity_checked_without_trusting_solution_list':True,'unique_compatible_orientation_math':'primary_math_proof.json','no_new_solver_call':True})
save(env.ROOT/'Solid163/material_identity_audit.json',out)
print('Solid163 actual face geometry agrees with the independently enumerated black-cell sets.')
