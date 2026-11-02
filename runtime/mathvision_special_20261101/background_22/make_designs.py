from unit_tools import *
RED,BLUE,GREEN,ORANGE='#DC2626','#2563EB','#16A34A','#EA580C'
def partial(qid,target,index,color,width=2):
    path=read(HERE/qid/'exact_paths.json')[target][0]
    n=len(path['controls'])
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width,
            'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':index/n,'end':(index+1)/n,'wrap':False}}
def role(action,description):return {'action':action,'information_role':description,'necessary_to_hypothesis':True}
actions=[];roles=[]
for src,dst,k,color,why in [
    ('graytile0','eggray22',2,RED,'NW-gray input tile diagonal paired to bottom-right cell of the actual diamond'),
    ('graytile1','eggray21',2,BLUE,'NE-gray input tile diagonal paired to bottom-left cell of the actual diamond'),
    ('graytile2','eggray11',2,GREEN,'SE-gray input tile diagonal paired to top-left cell of the actual diamond'),
    ('graytile3','eggray12',1,ORANGE,'SW-gray input tile diagonal paired to top-right cell of the actual diamond')]:
    for target,index in [(src,2 if src!='graytile3' else 1),(dst,k)]:
        a=partial('Plane482',target,index,color);actions.append(a);roles.append(role(a,why+'; '+('input feature' if target==src else 'example feature')))
plane=[{'question_id':'Plane482','name':'four_tile_single_window_binding','expected_wrong_answer':'B',
    'description':'Pair the four input tile diagonals with the four existing sides of the example gray diamond.',
    'hypothesis':'Four distinct color correspondences bind the full four-tile event to one illustrated 2x2 window. Intended error: calculate its probability (1/4)^4=1/256 and omit the other three possible window locations.',
    'primary_math':'For each of four 2x2 locations exactly one arrangement of its four oriented tiles forms a gray diamond, probability 1/256. Any pair of locations shares a cell demanding conflicting gray orientations, so events are disjoint. Total 4/256=1/64, choice C.',
    'semantic_review':'Only existing diagonal strokes change color/width; gray halves, square boundaries, blank grid and example are frozen. No new cut, region, text, tile, or probability condition is added.',
    'marker_roles':roles,'actions':actions}]
actions=[];roles=[]
for indices,color,label in [([0,1,5,6,7,11],RED,'descending strip P with vertices (1,4),(2,5),(5,2),(4,1)'),([2,3,4,8,9,10],BLUE,'ascending strip Q with vertices (1,2),(2,1),(5,4),(4,5)')]:
    for index in indices:
        a=partial('Plane481','logo',index,color);actions.append(a)
        roles.append(role(a,f'Existing exposed edge {index} assigned to {label}; binds the separated visible ends of that same arm across the overlap.'))
plane.append({'question_id':'Plane481','name':'two_strip_overlap_binding','expected_wrong_answer':'12',
    'description':'Color the existing exposed edges of each diagonal arm as one strip across the shared center.',
    'hypothesis':'Red and blue connect the two disconnected visible boundary portions of each area-6 diagonal strip. Intended error: sum 6+6 without subtracting their common central area 2, returning 12.',
    'primary_math':'The original filled polygon is the union of two parallelograms of area 6 each. Their common diamond has vertices (2,3),(3,4),(4,3),(3,2), area 2. Thus total area 6+6-2=10. Direct 12-vertex shoelace also gives 10.',
    'semantic_review':'Only existing outer boundary edges receive color. No central separator, new closed contour, new shaded region, new piece, or extra mathematical condition is introduced. Grid, gray fill and Math Team text stay frozen.',
    'marker_roles':roles,'actions':actions})
write(HERE/'plane_design_specs.json',plane)
actions=[];roles=[]
for target,color,why in [
    ('0line_1',RED,'First view left YES top edge: first member of a false repeated-face match'),
    ('1line_1',RED,'Second view left YES top edge: binds it to the first left YES despite different printed orientation'),
    ('2line_1',RED,'Third view left YES top edge: binds inverted YES to the same proposed left-face identity'),
    ('0line_4',BLUE,'First view right YES top edge: other member of a false two-YES-face inventory'),
    ('1line_5',BLUE,'Second view top YES rear edge: binds top YES to first right YES while ignoring full cube/word rotation')]:
    a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':2};actions.append(a);roles.append(role(a,why))
write(HERE/'solid_design_specs.json',[{'question_id':'Solid201','name':'two_yes_identity_edge_binding','expected_wrong_answer':'A',
    'description':'Use five existing face-border edges to pair repeated YES faces across the three die views.',
    'hypothesis':'Three red edge marks group the three left-face YES sightings; two blue edge marks pair first right YES with second top YES. Intended error: collapse the five YES sightings to only two physical YES faces, giving 2/6=1/3 (A), instead of respecting printed word orientations.',
    'primary_math':'Use fresh enumeration of all 24 proper cube rotations for each of views two and three relative to view one, respecting face normal and printed word baseline/up direction. Exactly one consistent oriented face assignment has three YES, two no, one maybe, hence 3/6=1/2 (B). Enumeration evidence saved separately.',
    'semantic_review':'Five existing open edges change color/width; no face fill, glyph, label direction, edge location, projection, hidden geometry or visibility interval changes. Colors are appearance cues only; all nine original words remain readable.',
    'marker_roles':roles,'actions':actions}])
print('Saved 3 predeclared designs: Plane482/B, Plane481/12, Solid201/A.')
