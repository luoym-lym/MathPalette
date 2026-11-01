from tools06 import *
import math
Q194={
 'question_id':'Plane194','status':'prescreen_only_no_clean_nonarbitrary_targeted_design','original_PNG_actually_viewed':True,'unique_answer':'E',
 'mathematics':'After the two perpendicular half-folds, the four corners of the quarter-sheet represent: an original corner,A(four clipped outer corners); an edge-fold corner,B(two opposite top/bottom V-notches); the other edge-fold corner,D(two opposite left/right V-notches); or the center,C(a central diamond). Unfolding reflects a single corner-cut oblique segment horizontally and vertically. Every new cut edge is oblique to the original sheet edges; the square hole in E has horizontal/vertical cut edges and cannot arise. Thus E uniquely fails; the four realizable classes A/B/C/D are all displayed.',
 'rejected_hypothesis':'Pairing the cut diagonal with C diamond would correctly explain a possible result, but predicting C as impossible would require a polarity/wording error unsupported by that geometric correspondence. Pairing dashed uncut corner legs with E square might obscure the distinction between removed and retained edges; this risks substituting a different cut interpretation without giving a specific predeclared wrong impossible option. No isolated option contour highlight is tested.',
 'marker_roles':[],'designs_saved':0,'API_calls':0,
 'human_gate':'Original all fold dashes,diagonal cut,sample outlines and labels remain legible; no candidateimage or extra equality/angle condition was made.'}
Q195={
 'question_id':'Plane195','status':'prescreen_only_no_clean_nonarbitrary_targeted_design','original_PNG_actually_viewed':True,'unique_answer':'E',
 'mathematics':'A convex vertex on the union outline of two triangular cards must be a visible original card vertex; a transverse intersection of two card edges is concave for their union, not convex. Every original card vertex is60degrees. E has four convex90degree corners, so it is impossible. A is the union of an upward side2 triangle with base[(-1,0),(1,0)] and a downward side2 triangle with base[(-1,2.0784609690826525),(1,2.0784609690826525)]. B is two side2 equilateral triangles on opposite sides of the shared segment[(5,0),(5,2)]. C is the union of right-pointing triangles[(10,0),(10,2),(11.732050807568877,1)] and its translation[1.0392304845413263,0]. D uses[(15,0),(15,2),(16.732050807568877,1)] and left-pointing[(16.732050807568877,0.5),(16.732050807568877,2.5),(15,1.5)]. Hence A/B/C/D are realizable and E uniquely not.',
 'rejected_hypothesis':'Color-binding triangle edges to E rectangle would have to pair a60degree vertex with a90degree vertex. Though appearance colors add no formal condition, this has no clear predeclared alternative impossible option. Simply emphasizing the more concave valid C or D is generic wrong-option salience. Additional internal triangle lines would look like added source piece boundaries and could change the human interpretation. No purposeful design reaching the current information gate was found.',
 'marker_roles':[],'designs_saved':0,'API_calls':0,
 'human_gate':'Original card and option outline geometry unchanged; all source cards and five labels inspected.'}
Q204={
 'question_id':'Plane204','status':'prescreen_only_no_clean_nonarbitrary_targeted_design','original_PNG_actually_viewed':True,'unique_answer':'D',
 'mathematics':'The target consists of18 unit equilateral triangles. Full placement enumeration over six rotations and reflected orientations, allowing every source triangle as anchor, gives A4placements/1cover,B21/9covers,C24/2covers,D18/0covers,E30/29covers. Any valid lattice tile must align a boundary edge and therefore has one of these six orientations; all possible centroid anchors are included. D has many local fits but none extends to a full disjoint tiling. A/B/C/E each have a stored explicit full cover. See tiling_exact_cover_audit.json for all placements and witnesses.',
 'rejected_hypothesis':'A locally fitting D could be matched to its18 genuine source placements, but such a local correspondence only supplies a false positive for D and does not select one specific incorrect answer among the four actually tileable alternatives. Marking the complex C contour alone would be arbitrary option salience. Coloring an entire proposed source partition would either exhibit a valid tiling and aid the correct answer, or imply nonidentical tile fragments/overlaps. No clean targeted wrong-answer design was forced.',
 'marker_roles':[],'designs_saved':0,'API_calls':0,
 'human_gate':'No candidate created. Original source elementarytriangles, all five tile sizes and boundaries remain intact.',
 'math_evidence_path':str(HERE/'Plane204/tiling_exact_cover_audit.json')}
for qid,data in [('Plane194',Q194),('Plane195',Q195),('Plane204',Q204)]:
 check=eligibility(qid);assert check['eligible'];write(HERE/qid/'eligibility_before_prescreen.json',check);write(HERE/qid/'primary_prescreen.json',data)
m=json.loads((HERE/'Plane202/context.json').read_text(encoding='utf-8'));segments=[o['geometry']['points'] for o in m['objects'] if o['id'] not in ['o0','o1601','o1602','o1603','o1604']]
def k(seg):return tuple(sorted(tuple(round(x,10) for x in p) for p in seg))
base={k(s) for s in segments}
counts={name:sum(k([f(*p) for p in s]) in base for s in segments) for name,f in [('x0',lambda x,y:(-x,y)),('y0',lambda x,y:(x,-y)),('y=x',lambda x,y:(y,x)),('y=-x',lambda x,y:(-y,-x))]}
assert counts['x0']==counts['y0']==1600 and counts['y=x']<1600 and counts['y=-x']<1600
write(HERE/'Plane202/reflection_segment_audit.json',{'method':'Compare all1600 frozen head segments as unorderedendpoint pairs after each exact candidate reflection; round10decimal only to normalize arithmetic noise. Appearance overlays are excluded.','segment_count':1600,'transformed_segments_matching_original':counts,'unique_answer':'2','original_PNG_actually_viewed':True,'geometry_changed':False})
print(counts)
