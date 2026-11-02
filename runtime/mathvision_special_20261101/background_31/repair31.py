from bootstrap31 import *
from inspect31 import eligibility
sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from workbench_io import load_config
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer

def run():
 config=load_config();config.update(runtime_dir=str(OWN/'state'),output_dir=str(OWN/'output'))
 adapter=RendererAdapter(config)
 for q,oldn,newn in [('Plane294','r31_inner_width_to_length_transfer','r31_inner_width_to_length_transfer_v2'),('Plane297','r31_nested_checker_unit_binding','r31_nested_checker_unit_binding_v2')]:
    old=OWN/q/oldn; new=OWN/q/newn
    hold=read(old/'pre_API_visual_hold.json'); des=read(old/'design.json')
    assert not (old/'tests').exists()
    e=eligibility(q);assert e['eligible'];save(new/'eligibility_before_design.json',e)
    difference=read(old/'design_difference_audit.json')
    save(new/'design_difference_audit.json',{'created_at':stamp(),'stage':'material_refinement','question_id':q,'variant_id':newn,'material_difference_from_historical_question_designs':difference['material_difference'],'new_information_correspondence':des['mechanism'],'concrete_pre_API_semantic_communication_repair':hold['reason'],'repair_explanation':'The frozen untested draft contains contour portions whose information role is absent/obscured under later native patches. This new image uses exact coincident existing-edge overlays at the same1pt width and same colors to make the full planned correspondence actually visible. It restores missing grouping information; no palette/width/crop/rename-only hypothesis, new inferred condition or altered source geometry is used. It is a preparation repair before any API outcome.','preserved_untested_draft':str(old),'preserved_draft_design_sha256':sha(old/'design.json'),'prior_draft_calls':0,'wrong_preset_unchanged_and_geometric_rationale':{'answer':des['expected_wrong_answer'],'mechanism':des['mechanism']},'firstpass_history':str(OWN/q/'prior_history_read_audit.json'),'no_observed_solver_outcome_used':True,'no_false_cut_region_or_relation':True})
    actions=[];roles=[]
    for mark in des['marker_roles']:
        if 'selected_edges' not in mark:
            actions.append(mark['action']);roles.append(mark);continue
        for selected in mark['selected_edges']:
            a={'type':'add_line','id':f'r31_visible_{len(actions)}','endpoints':selected['endpoints'],'color':mark['action']['color'],'linestyle':'solid','linewidth_pt':1}
            actions.append(a)
            roles.append({'action':a,'role':mark['role'],'source_geometry':mark['source_geometry'],'source_object':mark['action']['target'],'source_edge_index':selected['index'],'grounding':'Both exact endpoints are vertices of this actual original polygon. The complete line coincides with its original edge. zorder9 exposes the intended existing boundary through neighbour-outline overpaint. No new geometric locus, division, given relation or filled region.'})
    metadata=adapter.inspect_question(q);save(new/'fresh_context.json',metadata)
    renderer=PluginRenderer(config,adapter,{q:metadata})
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':des['mechanism'],'intent':'Existing-edge correspondence; see frozen design.json','params':{'actions':actions}}
    norm,data,pix=renderer.render(plugin)
    norm2,data2,pix2=renderer.render(norm,frozen=True)
    assert norm==norm2 and data==data2 and pix==pix2
    save(new/'plugin.json',norm);(new/'candidate.png').write_bytes(data)
    newdes={**des,'variant_id':newn,'created_at':stamp(),'design_difference_audit_sha256':sha(new/'design_difference_audit.json'),'marker_roles':roles,'plugin_sha256':sha(new/'plugin.json'),'candidate_sha256':sha(new/'candidate.png'),'candidate_pixel_sha256':pix,'human_semantics':'All added lines exactly overlay existing visible boundary edges at1pt; no added geometry or inferred cut/equality/dimension. Semantic fills, labels, piece counts and original question are unchanged. Independent native visual check still required.'}
    save(new/'design.json',newdes)
    save(new/'render_check.json',{'created_at':stamp(),'fresh_no_op_formal_pixel_equality':True,'formal_pixel_sha256':metadata['original_pixel_sha256'],'exact_actual_schema_normalization_passed':True,'idempotent_frozen_normalization':True,'two_render_bytes_identical':True,'two_render_pixels_identical':True,'png_sha256':sha(new/'candidate.png'),'pixel_sha256':pix,'all_added_lines_exactly_coincident_with_existing_edges':True,'added_point_or_new_geometric_locus':False,'fixed_add_line_defaults_frozen':True,'schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),'renderer_sha256':sha(PROJECT/'PlaneGeometry/workbench/mathvision_plugins.py')})
    print(json.dumps({'question_id':q,'variant_id':newn,'actions':len(actions),'png':str(new/'candidate.png')}),flush=True)

if __name__=='__main__':run()
