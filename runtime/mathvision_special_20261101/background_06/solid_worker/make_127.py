from design_tools import *
q='Solid127';rows=json.loads((TASK/q/'available_reflected_cavity_correspondences.json').read_text());actions=[];roles=[]
for target,color,role in [('Ce17',RED,'middle longitudinal edge of the three-cube shaft'),('Ce25',BLUE,'depth edge of the first terminal arm at the opposite shaft end'),('Ce0',GREEN,'transverse cap edge of the second terminal arm')]:
    row=next(r for r in rows if r['map_index']==1 and r['C']==target)
    for group in ['given','C']:
        ident=row[group];actions.append(style(ident,color));roles.append(f'{group}: {role}. This is an exact boundary-feature pair under the frozen determinant -1 map C(x,y,z)→cavity(z,y,x+2). The input member is an actual cavity boundary, not an unrelated outer-frame edge. Matching all three colored roles would require a reflection, not a physical rotation; the trap is to accept local reflected agreement as rotatable fit.')
folder=save_candidate(q,'reflected_cavity_three_feature_frame','C',actions,roles,'Bind the cavity shaft and its two terminal-arm features to the exact reflected three-axis frame on C, encouraging mirror matching to be mistaken for physical rotation.','The missing five unit cells are [(0,0,2),(0,1,2),(1,0,2),(2,0,1),(2,0,2)] in the5x2x3 box. Exhausting24 proper signed-axis rotations proves only E fits. C matches only determinant -1 maps. A/B/D have no congruence even allowing reflection. Marked boundary edges all match the same reflected map and preserve the opposite-arm handedness test.',TASK/q/'cavity_congruence_audit.json')
print(folder)
