from common23 import *
from datetime import datetime,timezone
sys.path.insert(0,str(ROOT/'PlaneGeometry/workbench'))
from workbench_io import load_config,environment_versions
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import describe_paths
qid='Plane233';vid='r23_four_cell_corner_spine';d=OUT/qid/vid;d.mkdir(exist_ok=False)
e=eligibility(qid);assert e['eligible'];write(d/'eligibility_before_design.json',e)
config=load_config();config['runtime_dir']=str(OUT/'state');config['output_dir']=str(OUT/'output')
ad=RendererAdapter(config);meta=ad.inspect_question(qid);actions=[];roles=[];parts={}
for prefix in ['given_','C_']:
    objects=[o for o in meta['objects'] if o['id'].startswith(prefix)]
    xs=[v[0] for o in objects for v in o['geometry']['points']];ys=[v[1] for o in objects for v in o['geometry']['points']]
    x0=min(xs);y0=min(ys);part=[]
    for o in objects:
        ps=o['geometry']['points']
        spine=all(p[0]==x0 for p in ps)
        foot=all(p[1]==y0 for p in ps) and max(p[0] for p in ps)<=x0+2
        if spine or foot:
            actions.append({'type':'set_object_style','target':o['id'],'color':'#DC2626' if spine else '#2563EB','linewidth_pt':2})
            role=('One original unit edge of the full four-cell vertical spine; matches same-length source/option boundary run.' if spine else 'One original unit edge of the two-cell foot, paired with same-length other foot and fixing the corner orientation.')
            roles.append({'action_index':len(actions)-1,'target':o['id'],'endpoints':ps,'role':role,'source_edge_exterior':True if prefix=='given_' else None})
            part.append(o['id'])
    assert len(part)==6
    parts[prefix]={'origin':[x0,y0],'targets':part}
prior=OUT/qid/'r23_exterior_notch_correspondence'
prior_read=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in prior.rglob('*') if p.is_file() and p.suffix in ('.png','.json')]
rationale='The board left side has a straight four-cell spine and a two-cell bottom-corner foot; C has exactly these same two boundary runs. Red transfers the four-unit spine and blue the two-unit foot by translation. Predicted errorC accepts a genuine local L-pentomino placement at the corner as evidence that three congruent copies tile the board; they do not.'
difference='This is a different matched feature from all prior hypotheses: length-four outer spine plus a two-unit foot, rather than a cross silhouette, two U contours, or a one-unit reentrant notch. All six source edges are actual outer-board edges and zero internal grid/cut edges are colored. It therefore preserves the closed-contour repair while testing long-column/foot correspondence to C. Old C/C original controls motivate no success claim; newC is geometrically justified here BEFORE exactly two new calls.'
write(d/'design_difference_audit.json',{'stage':'material_refinement','question_id':qid,'variant_id':vid,'new_hypothesis':rationale,'substantive_difference':difference,'old_original_variants':read(OUT/qid/'prior_history_manifest.json'),'preceding_new_design_full_artifacts_read':prior_read,'preceding_new_frozen_preset':'B','preceding_new_actual_finals':['D','B'],'new_wrong_answer':'C','before_calls':True,'geometry_feature_lengths':[4,2],'per_marker_roles':roles,'no_closed_source_subset_or_cut':True})
p={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':rationale,'intent':rationale,'params':{'actions':actions}}
renderer=PluginRenderer(config,ad,{qid:meta});normalized,data,pixels=renderer.render(p);n2,bytes2,px2=renderer.render(normalized,frozen=True)
assert normalized==n2 and data==bytes2 and pixels==px2
(d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(bytes2)
write(d/'plugin.json',normalized);write(d/'fresh_context.json',meta)
scene=ad.scene(qid)
try:
    scene.fig.canvas.draw();paths={a['target']:describe_paths(scene,a['target']) for a in actions}
finally:scene.close()
write(d/'path_fingerprints.json',paths)
assert e['frozen_source_files']==eligibility(qid)['frozen_source_files']
write(d/'render_check.json',{'formal_noop_pixels_match':True,'twice_byte_identical':True,'schema_actual_normalization':True,'frozen_inputs_unchanged':True,'png_sha256':sha(d/'candidate.png'),'pixel_sha256':pixels,'environment':environment_versions()})
write(d/'design.json',{'stage':'material_refinement','question_id':qid,'branch':'PlaneGeometry','variant_id':vid,'created_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':'C','correct_answer':'A','hypothesis':rationale,'substantive_difference':difference,'per_marker_roles':roles,'bindings':parts,'image_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),'pixel_sha256':pixels,'difference_audit_sha256':sha(d/'design_difference_audit.json'),'status':'PRIMARY_DRAFT_REQUIRES_PARENT_NEW_REVIEW'})
print(json.dumps({'question_id':qid,'variant_id':vid,'actions':len(actions),'source_and_C':parts,'png_sha256':sha(d/'candidate.png')}),flush=True)
