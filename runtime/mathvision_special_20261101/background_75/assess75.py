import bootstrap75 as boot
from research75 import *

REASONS={
 'Plane375':{
  'status':'reasoned_skip_no_unambiguous_new_information_binding',
  'considered_new_hypothesis':'Transfer the two source3x2 tilings independently into two apparent3x2 target windows, predicting4 instead of2.',
  'concrete_reason':'The actual twelve-cell target has only two exact covers. The two rightmost corner L pieces are identical in both covers; the remaining left6-cell region carries the only binary choice. Two3x2 windows suggested by the source overlap in actual target cells. Marking full windows would prescribe an invalid fixed partition; open grid runs do not identify two independently variable modules. Merely recoloring the existing demonstration L-spines gives a correct local exemplar, without a distinct human-clear wrong receiver. No fake module or extra target spine is drawn.',
  'old_objection_disposition':'background09 rejected a full colored target decomposition and found isolated notches insufficient. The considered new overlapping-window transfer does not resolve that ambiguity without adding a partition, so it is not forced into a design.'},
 'Plane381':{
  'status':'reasoned_skip_no_unambiguous_new_information_binding',
  'considered_new_hypothesis':'Transfer a shared short arm/reentrant corner between actual3-cell T and4-cell F into an exterior board step; mistake local fit for a whole-board all-F packing or a forced larger T count.',
  'concrete_reason':'The actual area is22, not an assumed conventional T/F pentomino area. 3t+4f=22 forces t>=2; the saved exact construction attains2. A true open arm correspondence does not supply a different count or establish why extra T pieces are required. Obtaining preset0 or6 would need ignoring actual cells, assuming an area-equality not present, or drawing a fixed partition. Comparing only source T/F arms would be generic similarity, with no useful wrong-count receiver in this board. No new geometry or source partition is introduced.',
  'old_objection_disposition':'background09 already rejected isolated F salience and conflicting full partition. New independent minimum proof and inspection do not expose a distinct concise receiver that resolves those objections.'},
 'Plane384':{
  'status':'reasoned_skip_whole_diagram_symmetry_semantics',
  'considered_new_hypothesis':'Bind true shaded/white counterparts around a nonminimal reflection axis, predicting4 or5 instead of global minimum3.',
  'concrete_reason':'The actual frame permits exactly four axes with required additions5,4,3,5. Selective counterpart-edge color around one axis can itself become part of the whole diagram whose symmetry is requested, removing other axes and changing the minimum or existence of an answer. Making every added stroke D4-invariant avoids that conflict but no longer binds the proposed nonminimal axis to a distinct false global target. No new legend can remove the competing reading. Original eight shaded cells and all41 frame cells remain unchanged.',
  'old_objection_disposition':'background10 independently screened this exact question despite its visual resemblance toPlane325. No Plane325 failed image was copied or retested. The prospective symmetry direction does not authorize an asymmetric marking that changes the requested whole-diagram symmetry.'},
 'Plane389':{
  'status':'reasoned_skip_no_distinct_legal_wrong_receiver',
  'considered_new_hypothesis':'Compare a ship boundary unit edge to neighboring cell boundaries, encouraging edge-only exclusion11 and forgetting corner contacts required for true8.',
  'concrete_reason':'All30 horizontal/vertical3x1 placements were enumerated with closed-cell Chebyshev exclusion; eight are legal and edge-only exclusion gives11. Highlighting actual forbidden edge contacts is correct guidance, rather than an information transfer that justifies treating the three corner-touching positions as legal. Explicitly identifying those positions would require outlining additional ships/candidate3-cell groups, which risks adding ships or a fixed placement to the count target. Arbitrarily styling free cell boundaries is not a meaningful receiver. No ship, occupancy, endpoint or candidate placement is added.',
  'old_objection_disposition':'background19 rejected extra region outlines and arbitrary wrong-cell salience. The newly proved11 edge-only alternative is a concrete mathematical error model, but no new human-unambiguous mark binding it was found; a numerical preset alone is not sufficient.'},
 'Plane454':{
  'status':'reasoned_skip_pattern_identity_semantics',
  'considered_new_hypothesis':'Transfer the directed corner-edge order of the shown adjacent gray pair as if turns-only equivalence were sufficient, predicting rotation-only classes instead of D4 classes.',
  'concrete_reason':'The36 unordered pairs partition into8 D4 orbits (10 under rotations alone). All four actual examples belong to the same corner-edge adjacency orbit. Selective red/blue edge roles could reasonably become additional pattern identity, causing physically color-preserving flips/turns to have different equivalences. A D4-invariant uniform frame avoids this but supplies no directed local receiver for the proposed turns-only error. Extra shaded pairs would change the examples, and merely emphasizing one existing pair would be salience. No colored pattern or new pair was generated.',
  'old_objection_disposition':'background21 found matching original edges reinforce true equivalence. The direction from source65 is prospective, not approval to transport colored-edge identity or add an example.'}
}

def main():
    result=[]
    for q in IDS:
        common={'question_id':q,'assessed_at':now(),'review_role':'primary research only','actual_source_JPG_viewed':True,'actual_formal_native_PNG_viewed':True,'math_proof_path':str(OWN/q/'math_proof.json'),'native_capture_audit_path':str(OWN/q/'native_capture_audit.json'),'eligibility_path':str(OWN/q/'eligibility_start.json'),'mark_count_cap':None,'quota_thrift_skip':False,'not_a_global_impossibility_claim':True,'solver_calls_so_far':0}
        if q in REASONS:entry={**common,**REASONS[q],'candidate_designs_created':0,'marker_audit':{'actual_new_mark_count':0,'each_actual_mark_role':'not applicable; no candidate created'},'status_final_for_assessment':True}
        else:entry={**common,'status':'new_substantive_design_under_local_validation','candidate_designs_planned':1,'status_final_for_assessment':False}
        put(OWN/q/'assessment.json',entry);result.append(entry)
    put(OWN/'checkpoint.json',{'unit':'background_75','stage':'material_refinement','updated_at':now(),'status':'local_design_validation','scope':IDS,'actual_assessed_question_ids':IDS,'unworked_question_ids':[],'primary_assessments':result,'current_API_calls':0,'complete_candidate_pairs':0,'credible_primary_doublehits':[],'errors':[],'aborts':[],'owned_live_API_requests':0,'second_review':'Parent must launch a NEW independent delegate; this unit does not self-review independently.','environment':{'strict_writeguard':str(OWN),'thread_env':{k:__import__('os').environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']},'routing':boot.ROUTING},'scope65_66_gates':'65 exact-cover/minT/symmetry/original dots/corner contact/D4 all independently computed. 66 paint/voxel9blocks/211nine-vs221eight remain intact as readonly inherited constraints; no Solid scope or work performed.','original65_66_never_started':True,'fresh_quota_failure':False,'formal_or_approval_or_Special_writes':False})
    put(OWN/'second_review_queue.json',{'unit':'background_75','updated_at':now(),'status':'local_validation_no_calls_yet','primary_candidates':[],'independent_review_required_before_delivery':True})
    print(json.dumps({'assessed':8,'reasoned_skips':len(REASONS),'local_designs_planned':3,'API_calls':0}))

if __name__=='__main__':main()
