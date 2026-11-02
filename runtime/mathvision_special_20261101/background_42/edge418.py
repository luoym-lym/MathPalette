from env42 import *
from math42 import scene,segments,covered
from fractions import Fraction as F
q='Plane418';out=HERE/q/'r42_local_corner_fit_to_area_bound_exact_edge_overlay';sc=scene(q);segs=segments(sc)
bindings=[]
targets=[['piece0','piece1','piece2'],['piece0'],['board3','board7','board11'],['board3']]
for a,ids in zip(read(out/'plugin.json')['params']['actions'],targets):
    start,end=[tuple(F(str(c)) for c in p) for p in a['endpoints']];assert covered(start,end,segs)
    objects=[o for o in sc['objects'] if o['id'] in ids];pts={p:sc['points'][p] for o in objects for p in o['points']}
    bindings.append({'action':a,'entire_overlay_exactly_covered_by_original_edges':True,'native_original_objects':objects,'fullprecision_original_points':pts,'captured_path_fingerprints':{i:read(HERE/q/'local_path_diagnostic.json')['after_png_serialization'][i] for i in ids}})
write(out/'exact_original_edge_binding.json',{'question_id':q,'created_at_before_API':now(),'source_scene_sha256':file_hash(ROOT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items/Plane418/scene.json'),'bindings':bindings,'no_added_topological_edge':True,'no_hidden_original_edge':True,'source_to_board_translation':[4.5,1],'no_complete_T_or_partition_on_board':True})
