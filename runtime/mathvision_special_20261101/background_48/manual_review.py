import task_env
from task_env import OWN
from prepare import read,write,hashfile
from datetime import datetime,timezone

manual={
'Plane468':[('5',False,'Final explicitly5, from an incorrect12-tile border; not preset23.'),('|7 - n|',False,'Terminal answer is the formula |7-n| with unspecified border count n. Incidental7 is not a final23 or a numeric solution.')],
'Plane469':[('6',False,'Terminal6; misses preset3. It misses an original black cell and its purported reflection closure is internally incorrect.'),('3',True,'Terminal3 unambiguously hits the preregistered wrong value. Its actual derivation mixes two diagonal conventions; the intended vertical-axis mechanism is not demonstrated.')],
'Plane472':[('B; 6',False,'TerminalB and value6 agree; misses presetA=4. Its narrative fabricates a central diamond, which does not change the terminal result.'),('A; 4',True,'TerminalA and value4 agree; hits presetA. Actual narrative uses incorrectly located triangular bases, so local unit-L transfer is not established.')],
'Plane473':[('E; 1:1',False,'TerminalE and1:1 agree; misses presetB=3:8.'),('D',False,'Terminal choiceD. Narrative computes3:2 and then conditionally3:5, selectingD as intended; no terminalB or3:8. Neither incidental nor contradictory arithmetic is promoted to a hit.')],
'Plane475':[('3',False,'Terminal3, not preset9. It misreads two highlighted local examples as separated grids and drops cross-group triangles.'),('4',False,'Terminal4, not preset9. Multiple nonexistent metric classes in narrative do not change its unambiguous final4.')],
}
for q,decisions in manual.items():
    d=next(f.parent for f in (OWN/q).glob('r48_*/design.json'))
    if q=='Plane473':d=OWN/q/'r48_white_unit_corner_to_outer_denominator_exact_edges'
    audits=read(d/'frozen_evidence_audit.json');runs=[]
    for a,(answer,hit,reason) in zip(audits['runs'],decisions):
        runs.append({**a,'entire_raw_response_manually_read':True,'manual_terminal_answer':answer,'hits_unchanged_predeclared_preset':hit,'manual_reason':reason})
    write(d/'manual_final_review.json',{'question_id':q,'variant_id':audits['variant_id'],'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'preset_wrong_answer':audits['binding']['expected_wrong_answer'],'manual_runs':runs,'two_hits':all(x[1] for x in decisions),'decision':'MISS','image_design_preset_unchanged':True,'no_mechanism_causal_or_statistical_claim':True,'parent_new_independent_review_required_for_any_future_candidate':True})
print('Five complete pairs manually adjudicated; no two-hit candidate')
