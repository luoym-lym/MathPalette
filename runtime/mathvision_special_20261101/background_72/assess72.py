from tools72 import *

write(HERE/'Plane355/unique_math.json',{
 'original_source_and_formal_native_viewed':True,
 'givens':['Strip width 4 cm and original straight length 13 cm','45-degree fold shown','P and Q are the two exposed rectangles','P=2Q','x is only the exposed P length, not the turn diagonal'],
 'proof':['Let y be the exposed length of Q. Both P and Q have the unchanged strip width 4.','The 45-degree crease turns the original strip axis by 90 degrees. The two parallel original long edges meet the crease at longitudinal coordinates separated by 4, since cot(45 degrees)=1. Thus the diagonal transition consumes 4 cm of original strip length.','The original material-length decomposition is x+4+y=13, independent of the doubled-layer triangular overlap.','P=4x=2Q=8y implies x=2y. Thus x+y=9, y=3, x=6 uniquely, C.','The turn diagonal has length sqrt(4^2+4^2)=4sqrt(2), E, but is a distinct segment from x.'],
 'choices_checked':{'A':5,'B':5.5,'C':6,'D':6.5,'E':'4sqrt(2)'},
 'no_display_scale_used_as_given':True
})
write(HERE/'Plane365/unique_math.json',{
 'original_source_and_formal_native_viewed':True,
 'native_region_count_correction':'The actual source and formal image contain three gray exposed components (top, lower, and right protruding tip), collectively G. Older phrase two gray tips is not a count proof. All three original components remain unchanged.',
 'multiplicity':['Let O be the white overlap area, and G=1 be the total gray exposed single-layer area over all three components.','Folding is a reflection preserving material area. The final visible union is U=G+O; original paper area S=G+2O.','Given S=3U/2, 2G+4O=3G+3O, so O=G=1. Therefore S=3 uniquely.','No fold-position or scale assumption is required, beyond the shown single fold and exact gray/white layer membership.'],
 'answer':'3','new_API_calls':0
})
write(HERE/'Plane386/unique_math.json',{
 'original_source_and_formal_native_viewed':True,
 'native_bars_zero_based':[(0,2,1,3),(1,4,3,1),(1,3,3,1),(4,2,1,3),(1,0,1,3),(2,1,3,1),(2,0,3,1)],
 'operation':'Slide existing bars without rotation or deformation inside the box. Incoming 1x3 bar can use either axis orientation in this unit-bar sliding puzzle.',
 'stronger_lower_bound':'Independent enumeration of all 29 subsets of sizes 0,1,2 and all integer final translations of their bars, even allowing removal and arbitrary relocation with no path restrictions, finds no packing of an additional bar in either orientation. See independent_search.json. This strengthens the old grid-only BFS conclusion.',
 'continuous_translation_reduction':['Suppose a continuous final translated packing exists for a chosen subset and axis orientation of the incoming bar. Choose one true horizontal or vertical separating inequality for each pair of nonoverlapping rectangles and for each moving/fixed pair.','Containment and those chosen separations form independent x and y systems of difference constraints. All constants are integers because every width, height, fixed coordinate and box boundary is integral.','A real feasible difference-constraint system with integer constants has an integer feasible potential: anchor a zero node, add a super-source and use shortest-path distances, which are integers whenever there is no negative cycle. Translation by the anchored zero value preserves all inequalities.','Thus a continuous final packing would imply an integer final packing with the same orientations. The exhaustive integer static infeasibility therefore proves the at-least-three bound for continuous translations too.'],
 'construction':['Slide bar0 from (0,2) to (0,0) along the empty 1x2 channel below it.','Slide bar1 from (1,4) to (0,4) left by 1.','Slide bar2 from (1,3) to (0,3) left by 1.','The vertical slot x in [3,4], y in [2,5] is now empty; place the eighth 1x3 bar there. Each slide has a collision-free swept rectangle and no bars overlap.'],
 'count':'Three distinct bars. The two unit steps used for bar0 in the BFS are one length-two slide of the same bar, not two bars.',
 'not_claimed':'No proof for rotating existing bars, removing bars, deforming bars or an independently tilted incoming rectangle; those are outside the fixed-orientation sliding operation used here.',
 'unique_minimum':3,'new_API_calls':0
})

for q,reason,directions in [
 ('Plane365','No clean distinct targeted wrong hypothesis survived actual layer-role and human-semantics review.',[
  {'direction':'Pair the original flap two open outer edges with their reflected edges in the folded view.','disposition':'True material correspondence is possible and would preserve ink under the fold, but it supplies the correct flap/layer identity. It gives no concrete new rationale for treating the whole resultant as the gray given area; using 1.5 as a guessed preset would not be evidence-based.'},
  {'direction':'Swap the gray single-layer and white overlap roles.','disposition':'For this particular 1.5 ratio the algebra forces G=O. Merely swapping them still returns 3; it is not a genuinely wrong numerical hypothesis.'},
  {'direction':'Close or recolor a selected white/gray region to force the gray-area given onto another region.','disposition':'Would introduce a painted-region or partition reading and change which area is given as 1. The explicit source shading and all three exposed tips must be preserved. Rejected before any render or call.'}]),
 ('Plane386','The independently verified minimum is 3, but no materially new concise useful binding survived the selected-bar/false-gap objections.',[
  {'direction':'Compare the true central 2x1 gap with the 3-long horizontal bar edges above it, intending 2 by counting those two bars.','disposition':'This comparison describes the real one-unit capacity shortfall but does not encode permission for either bar to slide. To privilege only the two upper bars repeats the prior selected-bar salience issue and omits the prerequisite left vertical bar.'},
  {'direction':'Pair the 2-long left gap with the obstructing 3-long left bar.','disposition':'It correctly shows the prerequisite slide and supports the correct three-bar chain. No distinct wrong-count mechanism is established by this true comparison alone.'},
  {'direction':'Outline a new 1x3 slot or add move arrows or displaced copies.','disposition':'A new slot could be read as an already empty region or a new bar; arrows or displaced geometry would assert operations rather than compare existing information. These alter the physical puzzle or exceed allowed operations. No such candidate is rendered.'}])]:
    write(HERE/q/'assessment.json',{'question_id':q,'assessed_at':now(),'status':'reasoned_skip_before_candidate_API','current_eligibility':eligibility(q),'original_native_source_context':str(HERE/q/'context.json'),'baseline':str(HERE/q/'baseline_check.json'),'unique_math':str(HERE/q/'unique_math.json'),'reason':reason,'considered_substantive_directions':directions,'candidate_pngs':0,'new_API_calls':0,'no_forced_design_quota':True,'no_impossibility_claim_for_future_designs':True,'primary_only':True})
print('365 and386 reasoned zero-call skips saved; math proofs for355/365/386 saved',flush=True)
