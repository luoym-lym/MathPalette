from design_tools import *
q='Solid226';g=[
named(q,['line_2','line_10'],RED,'Existing open two-edge motif identifying one new vertical unit cut face',2),
named(q,['line_13','line_14'],BLUE,'Existing open two-edge motif identifying the opposite new vertical unit cut face',2),
named(q,['line_11','line_12'],GREEN,'Existing visible open two-edge motif identifying the unit cut floor; one boundary is genuinely partly occluded',2)]
save(q,'three_new_face_visibility_binding','E',g,'Distinguish the three newly exposed cut faces by red/blue/green open edge motifs. Target counting3 new unit faces but only the removed top unit face, overlooking the removed front/back unit patches; wrong increase2,choiceE.','The original block is1x9x3. The one-foot removed cube spans the full1-foot thickness at an interior top location. It removes3 exterior unit patches:top,front,back. It exposes3 unit faces:floor and two side walls. Net0,choiceC. Original full thickness1 and all cut dimensions1 remain readable. Each mark follows an existing cut edge and all original hidden/visible intervals are preserved.','No added cut or contour. Each L is on an actual newly exposed unit face; none completes a new closed boundary. This is a face-visibility counting hypothesis, without a separately drawn old-surface counterpart; any causal inference is limited. Preserve labels1,3,9.')
q='Solid196';s=AD.scenes[q];M=np.array(s['projection']['matrix']);orig=np.array(s['projection']['origin']);off=np.array(s['projection']['offset']);g=[]
items=[]
for x in [.5,1.5]:
    for z in [.5,1.5]:items.append((f'front_{int(x*2)}_{int(z*2)}',[x,0,z],RED,'One of4 front unit faces'))
for x in [.5,1.5]:items.append((f'top_{int(x*2)}',[x,.5,2],BLUE,'One of2 upward unit faces'))
for z in [.5,1.5]:items.append((f'right_{int(z*2)}',[2,.5,z],GREEN,'One of2 right unit faces'))
for ident,w,col,role in items:
    xy=(M@(np.array(w)-orig)+off).tolist();a={'type':'add_point','id':ident,'xy':xy,'color':col}
    g.append(([a],[{'action':a,'world_face_center':w,'role':role+'; one-to-one marker to exposed visible unit square. Target omission of8 equally exposed opposite faces.','coordinate_basis':'Exact existing unit face center projected affinely; no fill or area change.'}]))
save(q,'visible_face_unit_binding','32',g,'Place one marker per visible unit face:4 red front,2 blue top,2 green right. Target using8 marked visible squares as the entire surface rather than doubling for opposite exposed faces;8*(24/6)=32.','Cuboid is2x1x2 small-cube units, four cubes. Each unit face area4cm2. Front/back4each, top/bottom2each,left/right2each give16faces,total64cm2. The8 markers cover only three visible directions, while rear,bottom,left remain equally exposed. Point annotations do not change cube shape or count.','Small point at center of each visible unit square. No new lines, fills or relation symbols. Every point maps to a real unit face, but no hidden-face correspondence is drawn; useful visible-count scaffold with limited evidence of causal omission.')
