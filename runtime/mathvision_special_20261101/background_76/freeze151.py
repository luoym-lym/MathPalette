import bootstrap
from bootstrap import OWNROOT,PROJECT,BASE
import json,sys,hashlib,difflib
from datetime import datetime,timezone
sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
from runtime_isolation import install
isolation=install(OWNROOT/'render_tmp')
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from workbench_io import load_config,environment_versions,pixel_hash
from dataset_tools.catalog import content,digest,read,rows

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8',newline='\n') as f:json.dump(obj,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')

qid='Solid151';name='face_center_inventory_to_core_confusion';out=OWNROOT/qid/name
out.mkdir(exist_ok=False)
cfg=load_config();cfg['runtime_dir']=str(OWNROOT/'render_state');cfg['output_dir']=str(OWNROOT/'render_output')
ad=RendererAdapter(cfg);meta=ad.inspect_question(qid);paths=read(OWNROOT/qid/'paths.json')
objects={o['id']:o for o in meta['objects']}
proof=read(OWNROOT/qid/'primary_cube_identity_audit.json')
actions=[];roles=[]
for row,i,role in [(0,0,'source'),(0,1,'source'),(0,3,'source'),(0,4,'source'),(1,4,'receiver')]:
    assert [1,1] in proof['patterns'][f'{row}{i}']
    for edge,color in [(2,'#DC2626'),(1,'#2563EB')]:
        oid=f'gridh{row}{i}{edge}';p=paths[oid][0]
        assert not p['closed'] and len(p['controls'])==1
        a={'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':1/3,'end':2/3,'wrap':False}}
        actions.append(a)
        controls=p['controls'][0];start=[controls[0][j]+(controls[1][j]-controls[0][j])/3 for j in [0,1]];end=[controls[0][j]+2*(controls[1][j]-controls[0][j])/3 for j in [0,1]]
        roles.append({'index':len(actions),'action':a,'role':f'{role}: '+('one of all four given black face-center cubies' if role=='source' else 'the black face-center cubie in option E')+f'; exact existing {"upper" if edge==2 else "lower"} one-unit center-cell boundary span. Red-upper/blue-lower identifies the same interior-of-a-face position, not a corner/edge or the unseen core.','information_necessity':'This span is one half of the open two-edge locator of this actual unit cell. The four source pairs enumerate the complete given black face-center inventory; the receiver pair invites extending that class to the sixth face. No whole pattern or wrong option outline is highlighted.','native_original_object':objects[oid],'actual_path':p,'exact_projected_endpoints':[start,end],'original_fill_black':True,'does_not_assert_same_cubie_or_equal_color_as_new_given':True,'no_new_geometry_or_closed_partition':True})
hyp='Use open red-upper/blue-lower unit spans to locate all four given black face-center cubies and the black face center of E. Test extending the observed black-center class to the missing face, overlooking that a face-center cubie is distinct from the fully hidden interior cubie: E needs16 exterior black cubies, which a free interior cannot reduce to15. The immutable wrong preset is E.'
old=BASE/'background_16/Solid151/checkerboard_corner_binding'
save(out/'design_difference_audit.json',{'question_id':qid,'created_before_any_new_solver_call':True,'old_design_path':str(old/'design.json'),'old_design_sha256':sha(old/'design.json'),'old_plugin_sha256':sha(old/'plugin.json'),'old_png_sha256':sha(old/'candidate.png'),'old_immutable_preset':'C','old_complete_finals':['B','C'],'old_result':'miss; not reused or relabeled','new_information_feature':'All four printed black face-center cubies, their single-face multiplicity, and a fifth proposed black face center versus the unseen interior cubie.','old_information_feature':'Four corners of the checkerboard source face matched to C, ignoring corner-incidence multiplicity.','substantive_difference':'Different cubie position class and counting multiplicity (face centers occur once, corners three times); different source patterns (00/01/03/04 instead of02); different receiver E instead ofC. Center inventory/core-confusion is frozen before any outputs, and E was not either old observed final. No old contour/PNG is copied, cropped, recolored, renamed or repeated.','new_wrong_answer':'E','new_wrong_geometric_hypothesis':hyp,'why_it_is_not_isolated_wrong_option_salience':'Four actual source center cells are paired with one actual receiver center cell. Every marked interval locates that same position class; no receiver outline or letter is emphasized.','new_paint_printed_identity_assessment':'The problem counts black/white unit cubes, not transported printed cards. Thin open overlays of preexisting grid edges leave all cell interiors and all black/white membership intact. No added face, piece, fill, fold or text. The marks do not purport to paint or identify a physical cubie across different faces.','local_primary_only':True,'new_independent_parent_review_required_if_two_hits':True})
save(out/'marker_path_bindings.json',roles)
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':hyp,'intent':hyp,'params':{'actions':actions}}
renderer=PluginRenderer(cfg,ad,{qid:meta})
norm,png,pixel=renderer.render(plugin)
again,png2,pixel2=renderer.render(norm,frozen=True)
assert norm==again and png==png2 and pixel==pixel2
save(out/'plugin.json',norm)
(out/'candidate.png').write_bytes(png)
assert sha(out/'candidate.png')!=sha(old/'candidate.png')
save(out/'context.json',meta)
save(out/'render_check.json',{'dedicated_bridge_adapter':str(BASE/'delivery_bridge_adapter.py'),'adapter_sha256':sha(BASE/'delivery_bridge_adapter.py'),'plugin_renderer':str(PROJECT/'SolidGeometry/workbench/render_plugins.py'),'plugin_renderer_sha256':sha(PROJECT/'SolidGeometry/workbench/render_plugins.py'),'schema_sha256':sha(PROJECT/'SolidGeometry/workbench/plugin.schema.json'),'normalization_and_frozen_normalization_equal':True,'two_renders_byte_identical':True,'candidate_png_sha256':sha(out/'candidate.png'),'candidate_pixel_sha256':pixel,'fresh_noop_formal_pixels_equal':True,'no_op_pixel_sha256':meta['original_pixel_sha256'],'isolation':isolation,'strict_ownroot_write_guard':True,'environment':environment_versions(),'source_fingerprints':read(OWNROOT/qid/'eligibility_start.json')['content']})
save(out/'design.json',{'question_id':qid,'design_id':name,'created_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':'E','correct_answer':'A','hypothesis':hyp,'design_difference_audit_sha256':sha(out/'design_difference_audit.json'),'marker_path_bindings_sha256':sha(out/'marker_path_bindings.json'),'candidate_png_sha256':sha(out/'candidate.png'),'candidate_pixel_sha256':pixel,'plugin_sha256':sha(out/'plugin.json'),'primary_math_audit':str(OWNROOT/qid/'primary_cube_identity_audit.json'),'primary_math_audit_sha256':sha(OWNROOT/qid/'primary_cube_identity_audit.json'),'approval_status':'PRIMARY UNREVIEWED research candidate; no original approval/Pass/Collect or delivery.','native_candidate_view_pending':True})
print(json.dumps({'candidate':str(out),'png_sha256':sha(out/'candidate.png'),'marker_count':len(actions),'frozen_wrong_preset':'E','new_api_calls':0}))
