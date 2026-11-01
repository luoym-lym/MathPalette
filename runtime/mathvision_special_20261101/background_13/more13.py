from design13 import *
from partial_style import describe_paths
mode=sys.argv[1]
if mode=='second':
    save('Solid162','white_branch_to_spatial_corner','E',[
        style('maine20',R,'Source white top cell back horizontal terminal edge',3),
        style('maine12',B,'Source white top cell receding edge, separate projected direction',3),
        style('maine35',G,'Source white lower side back vertical edge, third projected direction',3),
        style('Ee17',R,'E upper cube horizontal top edge, false upper terminal counterpart',3),
        style('Ee18',B,'E branch receding edge, false second-direction counterpart',3),
        style('Ee16',G,'E branch vertical edge, false third-direction counterpart',3)],
        'Bind three visible source white boundary directions to the three-dimensional corner branches of E, confusing projected axes with the white piece adjacency and planarity.',
        'White is exactly the planar T cells (0,1,0),(1,1,0),(2,1,0),(1,1,1), forced because the four gray and four dark cells are all visible and fill their quotas. D is planar T; E is a degree-three tripod using three axes and is nonplanar. Directional correspondence of separate visible face boundaries cannot change this planar adjacency. All original material fills and grid lines remain readable.')
    save('Solid103','overall_top_envelope_binding','E',[
        style('edge3',R,'Front full-width top edge: overall width of all three blocks'),
        style('edge6',R,'Back full-width top edge: corresponding same overall width'),
        style('edge7',B,'Right full-depth top edge: overall depth including both front cube and rear strip'),
        style('edge8',B,'Left full-depth top edge: corresponding same overall depth')],
        'Bind the two overall top-envelope dimensions and use the full top area 56 instead of the rear strip face containing the question mark.',
        'The gray cube volume125 forces side5. The small front block shares height5 and depth5, hence width75/25=3. Overall width=3+5=8; total volume280 and height5 give whole top area56 and overall depth7. The rear question-mark strip depth is7-5=2 and width8, giving area16, optionA uniquely. Four recolored envelope edges identify a real larger top region without adding any boundary. The strip-separating line edge11, gray semantic fill, smaller-block seam, and question-mark position remain unchanged and visible; E56 is the intended whole-top error.')
elif mode=='net':
    save('Solid193','cut_seam_false_pairing','B',[
        style('cutdiagonal0',R,'First existing diagonal cut seam on the cube face'),
        style('cutdiagonal1',B,'Second existing diagonal cut seam on the cube face'),
        style('net0triangle0side0',R,'First net1 triangle cut side paired by red to source rising diagonal'),
        style('net0triangle2side1',R,'Separated net1 triangle cut side falsely paired across source rising diagonal'),
        style('net0triangle1side1',B,'Net1 middle triangle cut side paired to source falling diagonal'),
        style('net0triangle3side0',B,'Net1 last triangle cut side, false alternate blue pair'),
        style('net2triangle0side0',R,'Net3 left terminal triangle cut side paired to first source seam'),
        style('net2triangle1side1',R,'Net3 right triangle cut side paired across first source seam'),
        style('net2triangle2side0',B,'Net3 upper triangle cut side falsely treated as missing-face seam'),
        style('net2triangle3side1',B,'Net3 lower triangle cut side falsely treated as matching missing-face seam')],
        'Use two colored diagonal-cut seam correspondences to suggest net1 has an incompatible seam pairing while net3 appears to match; predict invalid1and5, optionB.',
        'The exact independent hinge-fold audit primary_fold_audit.json propagates all five square faces and all four quarter triangles for every net. Nets1,2,4 cover the missing face with four distinct quarters sharing its center. In net3 the upper and lower triangles fold onto occupied square faces; in net5 one triangle folds onto an occupied square. Thus invalid nets3and5 uniquely giveE. C and D repeat2and4 in the unchanged formal source but both are incorrect. Coloring existing cut sides creates no new cut, tab, hinge, triangle or face; geometry of each triangular quarter remains visible.')
elif mode=='cylinder':
    qid='Solid96';scene=AD.scene(qid)
    try:
        scene.fig.canvas.draw();paths=describe_paths(scene,'largetoprim')
    finally:scene.close()
    write(TASK/qid/'fresh_large_rim_paths.json',paths)
    path=paths[0]
    def partial(start,end,color,role):
        a,r=style('largetoprim',color,role)
        a['interval']={'path_id':path['id'],'path_sha256':path['sha256'],'start':start,'end':end,'wrap':False}
        return a,r
    save(qid,'two_strip_rim_transfer','A',[
        style('small1toprim',R,'First source cylinder circumference, one complete strip width'),
        style('small2toprim',B,'Second source cylinder circumference, other complete strip width'),
        partial(0,.5,R,'First result semicircumference, same arc length as first source circumference'),
        partial(.5,1,B,'Second result semicircumference, same arc length as second source circumference')],
        'Bind the two complete small rims to two halves of the large rim and transfer the true additive circumference correspondence directly to a false additive volume ratio2.',
        'Two same-height strips of width2*pi*r join to give width4*pi*r. Height remains h and radius becomes2r. Volume ratio is4, uniquelyD; A2 is a lateral-area/circumference-to-volume transfer error. Each source circumference really has the same arc length as either semicircumference of the result. The two existing result seams remain unchanged; original geometry/projection/bottom visibility remain frozen. Partial styling uses a fresh exact original vector-path hash, with no added chords or radii.')
