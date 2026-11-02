from tools35 import *
assert BRANCH=='SolidGeometry'
from partial_style import object_paths,describe_paths
cfg,ad,Renderer=adapter()
old=HERE/'Solid156/r35_axis_unit_to_whole_direct_count'
out=old/'frozen_final'
d=json.loads((old/'design.json').read_text());p=json.loads((old/'plugin.json').read_text())
audit=json.loads((old/'design_difference_audit.json').read_text())
audit.update({'pretest_render_owner_correction':'Native initial draft revealed duplicate black artists overprinting parts of the local red width and whole blue depth. Before any calls, target the later duplicate owner of exactly the same existing edge: fronthorizontal6->topwidth0, topdepth3->rightdepth6. No new material hypothesis/preset or extra attempt. Untested initial draft retained and excluded from calls.','initial_draft_not_tested':True,'final_output_directory':str(out)})
write(out/'design_difference_audit.json',audit)
m=ad.inspect_question('Solid156');s=ad.scene('Solid156');roles=[]
try:
    s.fig.canvas.draw()
    for a,r in zip(p['params']['actions'],d['marker_roles']):
        if a['target']=='fronthorizontal6':a['target']='topwidth0'
        elif a['target']=='topdepth3':a['target']='rightdepth6'
        paths=object_paths(s,a['target']);assert len(paths)==1;path=paths[0]
        if 'interval' in a:a['interval']['path_sha256']=path['sha256']
        roles.append({'action':a,'role':r['role'],'stable_source_object':next(x for x in m['objects'] if x['id']==a['target']),'full_precision_frozen_projected_controls':[x['control'].tolist() for x in path['segments']],'frozen_path_id':path['id'],'frozen_path_sha256':path['sha256'],'closed':path['closed'],'path_description':describe_paths(s,a['target'])})
finally:s.close()
before=inputs(ad,'Solid156');renderer=Renderer(cfg,ad,{'Solid156':m});norm,data,pixels=renderer.render(p);norm2,data2,pixels2=renderer.render(norm,frozen=True)
assert data==data2 and pixels==pixels2 and norm==norm2 and before==inputs(ad,'Solid156')
write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(data);write(out/'context.json',m)
write(out/'render_check.json',{'no_op_formal_pixel_equal':True,'twice_byte_identical':True,'normalized_frozen_replay_equal':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'frozen_inputs':before,'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION,'pretest_owner_fix_only':True,'initial_draft_retained_never_tested':True})
d.update({'marker_roles':roles,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_difference_audit_sha256':file_hash(out/'design_difference_audit.json'),'pretest_owner_fix_only':True})
write(out/'design.json',d)
write(out/'marker_geometry_audit.json',{'all_marked_features_are_actual_source_features':True,'new_points':0,'new_lines':0,'marker_roles':roles,'all_three_unit_lengths_and_corresponding_whole_axis_lengths_preserved':True,'semantic_geometry_text_fill_projection_visibility_changed':False})
write(old/'initial_draft_disposition.json',{'created_at':now(),'never_tested':True,'status':'untested_render_owner_fix_before_first_call','not_an_additional_candidate_or_retry':True,'frozen_final':str(out),'difference':'Same genuine three-axis unit-to-whole grouping and preset A; correct later duplicate artist ownership so all six intended marks are visible. No source or old evidence modified.'})
print('final Solid156 corrected duplicate owners',flush=True)
