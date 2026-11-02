import task_env
from task_env import OWN
from inspect_sources import read,save,eligibility,sha
from datetime import datetime,timezone

skips={
'Plane414':{
 'prospective_direction_rechecked':'Real unit outer edges and the L notch versus a possible square span; distinguish area lower bound from realizable tiling.',
 'actual_findings':'Only one5-cell L piece is present. The new exact-cover proof rules out5 pieces and constructs20. The image contains no receiving square or second piece.',
 'considered_new_hypotheses':['Mark the raised unit and the four base units to induce the5-piece area lower bound. This is only cell/area salience on the same one piece, without an actual receiving arrangement or new information correspondence.','Bind a concave notch to an implied fifth exterior span. The implied span/copy does not exist in the frozen image; drawing it would create a virtual assembly/cut beyond this scene.'],
 'reason':'No clean material new source-to-receiver or geometric-count design found after exact math/source/history review. A five-unit counting decoration would not resolve the old targeting objection. No API call; not a proof no future design can exist.'},
'Plane417':{
 'prospective_direction_rechecked':'Cross-panel source side/half-side and final gray rectangle edges, visible area versus accumulated layer material.',
 'actual_findings':'The two final gray rectangles are each4x2=8. Matching source half-sides to their actual reflected rectangle sides preserves the correct area16. The wording explicitly asks the visible rectangles, not total material in all layers.',
 'considered_new_hypotheses':['Use a true4-unit edge correspondence between the first/middle panels and final rectangles. This supplies correct dimensions, without a concrete wrong receiving-area unit.','Predict24 by counting one rectangle twice and the other once. No displayed layer identity justifies this asymmetric grouping; adding it would require unsupported layer marks or a changed target.','Use final bounding-span as rectangle width. The needed projected dimension line is absent and would create an extra interior boundary in the folded-paper diagram rather than transfer an existing source edge.'],
 'reason':'The inspected clean correspondences support16. The proposed wrong groupings have no actual displayed receiving role without new fold/layer semantics. Gray fill and original arrows/creases are preserved; no tested design.'},
'Plane419':{
 'prospective_direction_rechecked':'Original whole/half diagonal versus retained triangle/rhombus edges and repeated folded-edge counting.',
 'actual_findings':'Exact reflection fixes retained side7.5. The fold diagonal6sqrt5 remains a rhombus diagonal, not a side. Existing corresponding retained edges support7.5.',
 'considered_new_hypotheses':['Map half the true diagonal to a side, predicting3sqrt5. This would be an unsupported length substitution with no counterpart endpoint coincidence; none of the exact offered wrong values follows from the actual half-diagonal.','Target optionA=7sqrt5/2 or roundedD=7.85 through diagonal transfer. Producing factor7/2 requires inventing a source length/endpoint or measuring the sketch.','Trace a substitute cutting contour. That creates a reasonable different cut instruction, forbidden for this image.'],
 'reason':'No simple materially new mistake maps actual source endpoints to one offered wrong value while retaining the shown cuts. Refuse an invented equality, source endpoint or cut. The rejection is task-specific, not a general ban on color in numerical geometry.'},
'Plane424':{
 'prospective_direction_rechecked':'Folded source flap versus actual overlap and single-layer gray parts, material area versus union area.',
 'actual_findings':'T=S+2O,H=S+O,T=1.5H,S=1 uniquely givesO=1,H=2,T=3. The source/native right diagram distinguishes the white overlap and3 gray single-layer components.',
 'considered_new_hypotheses':['Pair original flap boundary edges to their actual reflected edges. This truthfully tracks the same flap but does not make all gray single-layer components equal to that flap.','Highlight the whole gray/union contour to induceH=1 andT=1.5. This only repeats regional salience and does not supply the requested information binding.','Invent an extra boundary to label one/two-layer area contributions. That would change visible layering or create another fold/partition not in the original scene.'],
 'reason':'No clean new informative wrong area correspondence remains after preserving the exact original single/double layer semantics. Color is not mechanically prohibited: the available existing-edge pairings simply do not provide a supported new wrong mechanism. No call.'},
'Plane443':{
 'prospective_direction_rechecked':'Divider/interval hierarchy versus folded overlap area; old two-thirds-boundary half-fold shortcut.',
 'actual_findings':'The two actual length dividers per opposite side and one oblique fold remain. Independent reflection computes overlapA/3 and union2A/3. There is no displayed folded receiving shape.',
 'considered_new_hypotheses':['Restyle the old two2/3 long boundaries and fold. This is the same failedA hypothesis with cosmetic changes, forbidden.','Group the4 displayed divider marks as4 equal intervals to predict3/4. The4 marks lie on opposite edges; they do not delimit4 physical intervals, so that is arbitrary mark counting without a real area receiver.','Draw the reflected overlap or the opposite diagonal. The former constructs new folded boundaries, and the latter can reasonably look like a second fold/cut. Neither is part of the frozen scene.'],
 'old_results_preserved':{'preset':'A','manual_finals':['5:6','E (4:5)'],'two_hits':False,'raw_response_count':2},
 'reason':'No new concise source-to-receiving-area mechanism was found that is more than the old boundary symmetry cue, arbitrary mark counting, or an added fold. No retest or posthoc relabel.'}
}
for qid,v in skips.items():
    e=eligibility(qid);assert e['eligible']
    save(OWN/qid/'eligibility_at_screen_close.json',e)
    save(OWN/qid/'material_refinement_assessment.json',{
        'question_id':qid,'assessed_at_utc':datetime.now(timezone.utc).isoformat(),'stage':'material_refinement',
        'status':'assessed_no_clean_material_new_design','native_original_JPG_and_formal_PNG_opened':True,
        'full_formal_question_choices_frozen_scenes_old_designs_raws_primary_records_read':True,
        'unique_math_audit':str(OWN/qid/'primary_math_audit.json'),'old_history_audit':str(OWN/qid/'old_history_audit.json'),
        'old_evidence_preserved':True,'new_designs':0,'API_calls':0,'not_quota_or_cost_stop':True,**v})
print('Five original/source/history/math assessments saved; no new calls for these questions.')

# Record actual polygon-unit areas for the only new triangulation design.
import math
def area(p):return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p))))/2
h=math.sqrt(3)/2;t=h/2
low=[[0,0],[3,0],[2.5,h],[1.5,h],[1,2*h]]
triangles=[[low[0],low[1],low[2]],[low[0],low[2],low[3]],[low[0],low[3],low[4]]]
assert all(abs(a-b)<1e-12 for a,b in zip([area(p)/t for p in triangles],[3,1,2]))
folder=OWN/'Plane421/r44_unequal_triangle_count_transfer'
save(folder/'triangle_area_validation.json',{'source_unit_area':t,'gray_triangles':triangles,
     'gray_triangle_areas_over_source_unit':[area(p)/t for p in triangles],
     'upper_gray_fan':'half-turn congruent to lower fan','original_gray_area_each_over_source_unit':area(low)/t,
     'source_triangles_per_hexagon':6,'valid_area_fraction':'1/2','false_unweighted_cell_fraction':'1/3',
     'no_new_givens_or_fixed_cuts':True,'original_gray_and_white_regions_unchanged':True})
