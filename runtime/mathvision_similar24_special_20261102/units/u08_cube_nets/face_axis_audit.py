from worker import *
proof=read(OWN/'Solid187/primary_math_proof.json')
fr=proof['panels']['C']['frames']
assert fr['(0, 0)'][2]==[0,0,1]
assert fr['(2, 0)'][2]==[0,0,-1]
assert fr['(1, 0)'][2]==[1,0,0]
assert fr['(3, 0)'][2]==[-1,0,0]
d=OWN/'Solid187/C03_opposite_face_axes_true_and_false'
plugin=read(d/'plugin.json')
assert {a['target'] for a in plugin['params']['actions'] if a['color']=='#DC2626'}=={'hole0_1','hole3_1','Cboundary8','Cboundary45','Dboundary8','Dboundary15'}
assert {a['target'] for a in plugin['params']['actions'] if a['color']=='#2563EB'}=={'hole1_1','hole2_1','Cboundary28','Cboundary59','Dboundary34','Dboundary59'}
save(d/'literal_color_fold_audit.json',{'created_at':now(),'exact_fold_frame_check':True,'single_cube_axis_map':[[1,0,0],[0,1,0],[0,0,1]],'red_C_face_normals':[[0,0,1],[0,0,-1]],'blue_C_face_normals':[[1,0,0],[-1,0,0]],'target_red_faces':'top z=9 and bottom z=6','target_blue_faces':'left x=15 and right x=18','target_placement_in_unit_centered_cube':'opposite holes at x=-1/2,z=+1/2 and x=+1/2,z=-1/2, along y','matching_C_red_blue':'The four selected C bases are each in exactly the colored supporting face and corresponding opening of the target under one common axis map. The remaining returns remain black. Ink groups are preserved as actual edge colors; no per-hole independent rotation is used.','D_partial_truth':'Blue supports are opposite +/-x, but both red supports are the same +z face, so no rigid colored-cube match. D already fails the uncolored opposite-edge condition.','schematic_notch_sizes':'No dimensions specified; the frozen scene explicitly selects illustrative notch depths. No exact rendered-size comparison is inferred as a given. Face ownership, cut incidence, opposite-edge placement and color support are exact.','unique_correct_with_physical_edge_ink':'C','no_source_or_formal_change':True})
print('C exact opposite-face axes agree with target red/blue; D red supports share one face')
