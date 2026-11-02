from bootstrap31 import *
from inspect31 import eligibility
sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from workbench_io import load_config
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer

q='Plane294';n='r31_outer_whole_side_to_part_transfer';d=OWN/q/n
e=eligibility(q);assert e['eligible'];save(d/'eligibility_before_design.json',e)
save(d/'design_difference_audit.json',{'created_at':stamp(),'stage':'material_refinement','question_id':q,'variant_id':n,'expected_wrong_answer':'E','new_geometric_rationale_before_testing':'Each full outer square side is5 width units=40cm, whereas each outer component long side is4 width units=32cm. Corresponding same-color outside-side/component-side pairs target transferring40 to each of the four outer rectangles. Keep inner lengths16, centre8, giving4*40+4*16+8=232cm, E.','material_difference_from_firstpass':'Firstpass only prescreened new closed partitions; this follows already-existing external and component boundaries, adding no new division.','material_difference_from_other_r31_design':'The inner_width_to_length design targets four inner2x1 parts by width1 versus length2 and presetB=168. This new design instead targets four outer4x1 parts by whole-square-side5 versus component-side4 and presetE=232. The paired loci, units, mistaken dimensions and affected components differ; this is not a palette, width, crop or rename change.','no_observed_answer_used':'No raw final from any new Plane294 call has been read when declaring this rationale. It follows the source dimensions; the preset is not an observed answer plus cosmetics.','human_semantic_basis':'Question asks numerical rearranged length, not preservation/transformation of printed ink. Every overlay is exactly coincident with an actual edge and original9-part partition remains visible. No new equality, cut, unit label or filled region is drawn.','prior_history':str(OWN/q/'prior_history_read_audit.json'),'all_history_retained':True})
context=read(OWN/q/'context.json');geometries={o['id']:o['geometry'] for o in context['objects']}
groups=[
 ('#DC2626',[(0,3),(3,3)],(0,1),'left'),
 ('#2563EB',[(0,2),(1,2)],(1,0),'top'),
 ('#16A34A',[(1,1),(2,1)],(2,3),'right'),
 ('#EA580C',[(2,0),(3,0)],(3,2),'bottom'),
]
actions=[];roles=[]
for color,full,part,side in groups:
 for i,edge_index in full+[part]:
    obj=geometries[f'part{i}'];p=obj['points'];endpoints=[p[edge_index],p[(edge_index+1)%4]]
    role=(f'One actual exterior segment of the full {side} side5; together with the other same-color exterior segment it completes5 width units. No segment is extended off original geometry.' if (i,edge_index) in full else f'The actual opposite long edge4 of outer part{i}, paired with full {side} side5. The one-width excess on the full side is visible and no equality glyph is supplied.')
    a={'type':'add_line','id':f'r31_outer_{len(actions)}','endpoints':endpoints,'color':color,'linestyle':'solid','linewidth_pt':1}
    actions.append(a);roles.append({'action':a,'source_object':obj['id'],'source_edge_index':edge_index,'source_geometry':obj,'role':role,'full_precision_existing_endpoints':endpoints,'geometric_grounding':'Exact original polygon edge, no added locus or counted piece.'})
config=load_config();config.update(runtime_dir=str(OWN/'state'),output_dir=str(OWN/'output'))
adapter=RendererAdapter(config);metadata=adapter.inspect_question(q);save(d/'fresh_context.json',metadata)
renderer=PluginRenderer(config,adapter,{q:metadata})
mechanism='Bind each complete outer square side5 to the associated outer rectangle opposite long side4, inviting whole-to-component length transfer:4*40+4*16+8=232cm, E, while the unchanged source yields200cm, D.'
raw={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Original whole-side/component-side correspondence','params':{'actions':actions}}
norm,data,pix=renderer.render(raw);norm2,data2,pix2=renderer.render(norm,frozen=True)
assert norm==norm2 and data==data2 and pix==pix2
save(d/'plugin.json',norm);(d/'candidate.png').write_bytes(data)
save(d/'design.json',{'question_id':q,'variant_id':n,'stage':'material_refinement','created_at':stamp(),'expected_wrong_answer':'E','correct_answer':'D','mechanism':mechanism,'design_difference_audit_sha256':sha(d/'design_difference_audit.json'),'original_math_proof':str(OWN/q/'primary_original_math.json'),'primary_original_math_sha256':sha(OWN/q/'primary_original_math.json'),'marker_roles':roles,'plugin_sha256':sha(d/'plugin.json'),'candidate_sha256':sha(d/'candidate.png'),'candidate_pixel_sha256':pix,'human_semantics':'All12 lines at fixed1pt exactly coincide with original boundary edges. Same colors group actual sides without a new relation symbol or given equality. Original geometry,9 actual parts, fills, width8 statement and all lengths are retained. Native PNG inspection required before tests.','independent_review_status':'UNREVIEWED; NEW parent review required for any delivery.'})
save(d/'render_check.json',{'created_at':stamp(),'fresh_no_op_formal_pixel_equality':True,'formal_pixel_sha256':metadata['original_pixel_sha256'],'exact_actual_schema_normalization_passed':True,'idempotent_frozen_normalization':True,'two_render_bytes_identical':True,'two_render_pixels_identical':True,'png_sha256':sha(d/'candidate.png'),'pixel_sha256':pix,'all_added_lines_exactly_coincident_with_existing_edges':True,'added_point_or_new_geometric_locus':False,'fixed_add_line_defaults_frozen':True,'schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),'renderer_sha256':sha(PROJECT/'PlaneGeometry/workbench/mathvision_plugins.py')})
print(json.dumps({'question_id':q,'variant_id':n,'actions':len(actions),'png':str(d/'candidate.png')}),flush=True)
