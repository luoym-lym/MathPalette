from tools33 import *
q='Plane325';old=HERE/q/'r33_dihedral_arm_orbit_local_completion';vid='r33_dihedral_arm_outer_corner_semantic_repair';out=HERE/q/vid
d=read(old/'design.json');orbit=d['extra_certificate']['orbit'];ctx=read(HERE/q/'context.json');snaps={p['id']:p['xy'] for p in ctx['snap_points']}
acts=[];roles=[];segments=[]
for x,y in orbit:
    corner=(x if x<4 else x+1,y if y<4 else y+1)
    pairs=[(corner,(corner[0],corner[1]+(1 if y<4 else -1))),(corner,(corner[0]+(1 if x<4 else -1),corner[1]))]
    for a,b in pairs:
        assert list(a) in snaps.values() and list(b) in snaps.values()
        acts.append({'type':'add_line','id':f'r33_arm_boundary_{len(acts)}','endpoints':[list(a),list(b)],'color':'#DC2626','linestyle':'solid'})
        roles.append(f'Outer-corner side {a}-{b} of actual arm cell ({x},{y}). Together the two sides locate this cell without covering its semantic gray/white interior. The full 8-cell D4 orbit is necessary to preserve all possible original reflection axes under an ink-as-design reading.')
        segments.append((a,b))
ss={tuple(sorted(v)) for v in segments}
fs={'vertical':lambda x,y:(9-x,y),'horizontal':lambda x,y:(x,9-y),'rising_diagonal':lambda x,y:(y,x),'falling_diagonal':lambda x,y:(9-y,9-x)}
inv={name:{tuple(sorted(f(*p) for p in edge)) for edge in segments}==ss for name,f in fs.items()}
assert all(inv.values())
# Prove every overlay is already an original polygon edge, rather than a new grid edge.
original=set()
for o in ctx['objects']:
    pts=[tuple(p) for p in o['geometry']['points']]
    for a,b in zip(pts,pts[1:]+pts[:1]):original.add(tuple(sorted((a,b))))
assert ss<=original
audit={'stage':'material_refinement','created_at':now(),'question_id':q,'variant_id':vid,'pre_call':True,'old_design_sha256':file_hash(old/'design.json'),'old_png_sha256':file_hash(old/'candidate.png'),'old_calls':0,'old_disposition':'HELD before API; do not promote or test. Actual native view and edge sampling show many intended red outline edges are completely covered by later native cell artists, so intended D4 outline invariance does not hold visibly.','visible_old_problem_evidence':str(old/'visible_annotation_edge_audit.json'),'new_information_correspondence':d['hypothesis'],'concrete_semantic_repair':'Use the complete D4 orbit of 16 actual exterior staircase edges as explicit 1 pt overlays. These form eight visible congruent outer-corner Ls. This repairs the actual ink footprint and retains every original possible axis even if color is intrinsic content. It is not justified by palette, pixel hash or width changes. No old model response exists.','unchanged_predeclared_wrong_rationale':'Only the highlighted orbit requires 1 horizontal addition, whereas the full gray design requires at least 3 over all axes.','expected_wrong_answer':'1','all_reflections_preserved':inv,'all_overlay_segments_already_original_edges':True,'exact_segments':segments,'source_geometry_fill_text_unchanged':True}
write(out/'design_difference_audit.json',audit);write(HERE/'design_difference_audit_repair.json',audit)
write(old/'precall_hold.json',{'created_at':now(),'reason':audit['old_disposition'],'actual_edge_audit_sha256':file_hash(old/'visible_annotation_edge_audit.json'),'calls':0,'replacement':str(out),'frozen_old_design_and_png_unchanged':True})
cfg,ad=adapter();fresh=ad.inspect_question(q);assert fresh==ctx;assert eligibility(q)['eligible']
write(out/'fresh_context.json',fresh);write(out/'eligibility_design.json',eligibility(q))
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':d['hypothesis'],'intent':d['hypothesis'],'params':{'actions':acts}}
write(out/'plugin_submitted.json',plugin)
pr=PluginRenderer(cfg,ad,{q:fresh});normalized,png,digest=pr.render(plugin);n2,png2,digest2=pr.render(normalized,frozen=True)
assert normalized==n2==pr.normalize(normalized) and png==png2 and digest==digest2
write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png);(out/'repeat.png').write_bytes(png2);(out/'no_op.png').write_bytes((old/'no_op.png').read_bytes())
assert pixel_hash(out/'no_op.png')==pixel_hash(ad.original_paths[q])
write(out/'marker_bindings.json',[{'action_index':i,'action':a,'useful_role':roles[i],'original_edge_verified':True,'endpoint_exact_snap_ids':[[k for k,v in snaps.items() if v==p] for p in a['endpoints']]} for i,a in enumerate(normalized['params']['actions'])])
nd={**d,'variant_id':vid,'created_at':now(),'material_difference':audit['concrete_semantic_repair'],'per_marker_roles':roles,'human_semantics_precheck':'The actual exterior L footprint is a complete D4 orbit; literal colored-picture and annotation-only readings have the same possible axes and minimum 3. All fills remain unchanged.','extra_certificate':audit,'image_sha256':file_hash(out/'candidate.png'),'pixel_sha256':digest,'plugin_sha256':file_hash(out/'plugin.json'),'design_difference_audit_sha256':file_hash(out/'design_difference_audit.json')}
write(out/'design.json',nd)
write(out/'render_check.json',{'schema_and_actual_default_normalization_passed':True,'normalization_idempotent':True,'frozen_draw_passed':True,'no_op_pixel_equal_formal':True,'twice_byte_identical':True,'fresh_context_identical':True,'native_image_view_pending':True,'all_overlay_segments_already_original_edges':True,'all_four_axis_invariance':inv,'image_sha256':nd['image_sha256'],'plugin_sha256':nd['plugin_sha256'],'schema_sha256':file_hash(ROOT/'PlaneGeometry/workbench/plugin.schema.json')})
print(vid,len(acts),'actions',inv,flush=True)
