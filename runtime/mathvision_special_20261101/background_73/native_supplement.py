from bootstrap import HERE,TASK,PROJECT
from audit import read,save,sha,stamp
from pathlib import Path
import json

base=PROJECT/'SolidGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'
p=base/'Solid212/scene.json'
native=read(p)
snapshot={'source':str(p),'sha256':sha(p),'analytic_models':native['analytic_models'],'ambiguities':native['ambiguities'],'separate_frozen_projection':native['projection'],'separate_frozen_visibility':native['visibility']}
out=HERE/'Solid212/analytic_model_full_snapshot.json'
if out.exists():assert read(out)==snapshot
else:save(out,snapshot)
print('Solid212 ANALYTIC',json.dumps(native['analytic_models'],ensure_ascii=False))
p=base/'Solid222/scene.json'
native=read(p)
semantics=native['semantic_models'][0]
visible=semantics['visible_shaded_squares']
forced=set()
for face,a,b in visible:
    if face=='front':
        forced.update(((a,0,b),(a,2,b)))
    elif face=='right':
        forced.update(((0,a,b),(2,a,b)))
    elif face=='top':
        forced.update(((a,b,0),(a,b,2)))
    else:raise ValueError(face)
proof=read(HERE/'Solid222/primary_math_native_and_skip.json')
assert sorted(forced)==[tuple(x) for x in proof['all_shaded_cube_identities']]
assert sorted(forced)==[tuple(x) for x in semantics['counted_unit_cubes']]
assert len(forced)==20
save(HERE/'Solid222/native_visible_face_to_cube_identity_audit.json',{'time':stamp(),'source':str(p),'sha256':sha(p),'actual_visible_shaded_faces':visible,'opposite_rule':semantics['opposite_faces_same_pattern'],'independently_reconstructed_cube_union':sorted(forced),'count':len(forced),'matches_independent27cube_proof':True,'no_extra_paint_or_unseen_geometry_invented':True})
print('Solid222 actual native face membership independently reconstructs20')
